#!/usr/bin/env python3
"""Insère le référentiel complet (critères, intitulés, tests officiels) dans ruxaweb.html.

Source : le dépôt officiel du SIP, https://github.com/accessibility-luxembourg/ReferentielAccessibiliteWeb
(fr/json/criteres.json et en/json/criteres.json), © SIP Luxembourg, CC BY 3.0 LU. Intitulés et tests repris tels quels ;
seuls les liens du glossaire sont retirés (leur texte reste).

Usage :
  python3 outils/referentiel.py <dossier du dépôt officiel> [réglages.json] [ruxaweb.html]

Nouvelle version du référentiel (RAWeb 2) : récupérer le dépôt officiel à jour, copier les réglages
(outils/referentiel-raweb-1.1.json) sous un nouveau nom, adapter le nom, le préfixe et les liens, relancer.
"""
import json, re, subprocess, sys, os

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = sys.argv[1] if len(sys.argv) > 1 else sys.exit(__doc__)
REGLAGES = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ICI, 'referentiel-raweb-1.1.json')
HTML = sys.argv[3] if len(sys.argv) > 3 else os.path.join(ICI, '..', 'ruxaweb.html')
DEBUT = '  // <<< DEBUT_REFERENTIEL : généré par outils/referentiel.py depuis le JSON officiel du SIP, ne pas modifier à la main >>>\n'
FIN = '  // <<< FIN_REFERENTIEL >>>\n'

cfg = json.load(open(REGLAGES, encoding='utf-8'))
fr = json.load(open(os.path.join(DEPOT, 'fr', 'json', 'criteres.json'), encoding='utf-8'))
en = json.load(open(os.path.join(DEPOT, 'en', 'json', 'criteres.json'), encoding='utf-8'))

def texte(s):
    """Retire les liens Markdown (le texte reste) et les espaces en trop ; garde le code entre accents graves."""
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', str(s))
    return re.sub(r'\s+', ' ', s).strip()

def lignes(bloc):
    """Cas particuliers et notes techniques : chaînes et listes {"ul": [...]} aplaties, une ligne par élément."""
    out = []
    for x in bloc or []:
        if isinstance(x, str): out.append(texte(x))
        elif isinstance(x, dict):
            for v in x.values():
                out.extend(lignes(v if isinstance(v, list) else [v]))
        elif isinstance(x, list): out.extend(lignes(x))
    return [l for l in out if l]

def niveau(refs):
    """Niveau WCAG le plus élevé cité (A, AA, AAA) ; vide si le critère ne vient que de la norme EN 301 549."""
    ns = []
    for r in refs:
        for w in r.get('wcag', []):
            m = re.search(r'\((A{1,3})\)\s*$', w)
            if m: ns.append(m.group(1))
    return max(ns, key=len) if ns else ''

def wcag(refs):
    return [re.match(r'[\d.]+', w).group(0) for r in refs for w in r.get('wcag', []) if re.match(r'[\d.]+', w)]

titres_en = {}
for t in en['topics']:
    for c in t['criteria']:
        titres_en[f"{t['number']}.{c['criterium']['number']}"] = texte(c['criterium']['title'])

themes, criteres = [], []
for t in fr['topics']:
    n = str(t['number'])
    themes.append([t['number'], t['topic']])
    defaut = cfg['themes'].get(n, {})
    for c in t['criteria']:
        k = c['criterium']
        ref = f"{n}.{k['number']}"
        reg = dict(defaut); reg.update(cfg['criteres'].get(ref, {}))
        tests = [{'n': ref + '.' + num, 'l': [texte(x) for x in l]} for num, l in k['tests'].items()]
        x = {'ref': ref, 't': t['number'], 'fr': texte(k['title']), 'en': titres_en.get(ref, ''),
             'niv': niveau(k.get('references', [])), 'wcag': wcag(k.get('references', [])), 'tests': tests,
             'ruxal': reg.get('ruxal', ''), 'etape': reg.get('etape', '1'), 'gravite': reg.get('gravite', 'modere'),
             'declencheur': reg.get('declencheur', '')}
        cas = lignes(k.get('particularCases')); note = lignes(k.get('technicalNote'))
        if cas: x['cas'] = cas
        if note: x['note'] = note
        if ref in cfg['globaux'] or n in cfg['globaux']: x['global'] = True
        criteres.append(x)

try: commit = subprocess.run(['git', '-C', DEPOT, 'log', '-1', '--format=%h %cs'], capture_output=True, text=True).stdout.strip()
except Exception: commit = ''

ref = {'nom': cfg['nom'], 'court': cfg['court'], 'prefixe': cfg['prefixe'], 'url': cfg['url_fr'], 'url_en': cfg['url_en'],
       'methodo': cfg['url_methodo'], 'source': 'accessibility-luxembourg/ReferentielAccessibiliteWeb' + (' (' + commit + ')' if commit else ''),
       'themes': themes, 'declencheurs': cfg['declencheurs'], 'criteres': criteres}
bloc = DEBUT + '  // Référentiel complet : ' + cfg['nom'] + ', ' + str(len(criteres)) + ' critères. © SIP Luxembourg, CC BY 3.0 LU.\n' + \
       '  var REFERENTIEL = ' + json.dumps(ref, ensure_ascii=False, separators=(',', ':')) + ';\n' + FIN

s = open(HTML, encoding='utf-8').read()
if DEBUT in s:
    i = s.index(DEBUT); j = s.index(FIN, i) + len(FIN); s = s[:i] + bloc + s[j:]
else:
    m = '  // <<< FIN_DONNEES >>>\n'; assert m in s, 'repère FIN_DONNEES absent'
    s = s.replace(m, m + bloc, 1)
open(HTML, 'w', encoding='utf-8').write(s)
print(cfg['nom'], len(criteres), 'critères,', sum(len(c['tests']) for c in criteres), 'tests,', round(len(bloc) / 1024), 'Ko')
