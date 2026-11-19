# RUXAWeb : Revue UX Accessibilité (web)

**FR** : Outil HTML autonome (un seul fichier, hors ligne) qui aide à **préparer et prioriser un audit d'accessibilité de site web**, avant l'audit complet. L'audit se fait **par observations** : l'auditeur note ce qu'il constate, et la grille des critères se remplit. Il croise :

- **les 53 critères du RAWeb 1.1** (référentiel du SIP, Luxembourg) retenus par la [méthode de contrôle simplifié v1.2.1 du SIP](https://accessibilite.public.lu/fr/monitoring/controle-simplifie.html), dont 24 « si présent », qui donnent un **taux de conformité** ;
- **7 critères RAWeb hors sélection du SIP** (3.3, 7.1, 7.5, 9.3, 10.4, 10.6, 13.11), qui comptent dans un **taux élargi**, affiché à côté du taux sélection SIP ;
- **3 bonnes pratiques** hors RAWeb (taille des cibles, fermeture d'une fenêtre modale, retour du focus), hors taux ;
- pour les scénarios, **une lecture POUR/UX** qualitative, **exclue du taux**.

Un projet A11Y, trois modules : audit simple (3 à 5 écrans, comme l'audit simplifié du SIP), audit complet (les 136 critères du RAWeb 1.1 sur un échantillon représentatif, tests officiels dans chaque fiche, taux selon la méthodologie du SIP, processus, exemptions et dérogations, rapport d'audit) et scénario, chacun avec son rapport HTML imprimable en PDF, avec un configurateur de fonctions primaires commun au projet. Parcours guidé étape par étape, chaque étape sur tous les écrans (tour à vide, 4 étapes de test, clôture), panneau Parcours toujours au même endroit, observations valables sur plusieurs écrans, retest, import de rapports axe ou Lighthouse. Exports Excel (grille des critères), CSV (import Jira) et JSON.

L'audit simple est un **pré-diagnostic**, pas un audit de conformité. L'audit complet suit la méthodologie de test du SIP, mais reste un outil : l'auditeur est responsable du résultat et de la déclaration d'accessibilité. Il fait partie de la famille RUXAL, avec [RUXAAM](https://github.com/lijko/ruxaam) pour les applications mobiles et [RUXAWeb Tasks](https://github.com/lijko/ruxaweb-tasks) pour le suivi par tickets Jira.

**Référence** : RUXAWeb Tasks est désormais l'outil de référence pour l'audit web (Jira, seule source des non-conformités), ainsi que pour les agents Copilot de tickets. RUXAWeb reste utilisable pour un audit par observations, sans Jira.

**EN** : Standalone, offline, single-file HTML tool to **prepare and prioritise a website accessibility audit**. The auditor records observations and the criteria grid fills itself: the **53 RAWeb 1.1 criteria** of the SIP simplified audit method (Luxembourg's web accessibility standard; compliance rate), plus 7 extra criteria (extended rate) and 3 best practices. A full audit covers all 136 criteria, with the official tests in each criterion sheet and the SIP rate. Guided screen-by-screen flow, axe and Lighthouse report import, Excel, Jira and JSON exports. The simple audit is **not a compliance audit**.

## Utilisation
Ouvrir `ruxaweb.html` dans un navigateur. Aucune installation, aucun serveur, aucun appel réseau. Les données restent dans le navigateur ; l'audit se sauvegarde et se rouvre en JSON (menu Fichier).

## Contenu du dépôt
| Fichier | Rôle |
|---|---|
| `ruxaweb.html` | l'outil |
| `DOCUMENTATION.md` | observations et taux, sélection des critères, règle « si présent », parcours d'audit, gravités, limites, liste des 59 critères |
| `donnees-fictives-ruxaweb-v2.0.json` | projet fictif à ouvrir (Fichier, « Ouvrir une sauvegarde ») pour essayer l'outil : boutique en ligne, fonctions primaires, audit simple et scénario d'achat |
| `raweb-1.1-criteria.txt` | liste des 136 critères du RAWeb 1.1, une ligne par critère : numéro, intitulé officiel anglais (EN:) et français (FR:) ; sert de connaissance aux agents Copilot |
| `outils/` | `referentiel.py` : insère dans l'outil le référentiel de l'audit complet (critères, intitulés, tests officiels) depuis le JSON officiel du SIP ; `referentiel-raweb-1.1.json` : ses réglages (voir DOCUMENTATION, section 12) |
| `agents/copilot/` | **agents Microsoft 365 Copilot à installer** : « [A11Y] Observation -> RUXAWeb » (notes vers lignes à coller dans RUXAWeb), « [A11Y] Observation -> RAWeb » (critères d'une observation) et « [A11Y] JIRA Task » (ticket Jira) ; instructions et guide d'installation |
| `LICENSE` | EUPL-1.2 |
| `README.md` | ce fichier |

## Licence et attributions
- **Code, textes d'impact et de test, thèmes, gravités et bonnes pratiques de RUXAWeb** : © 2026 Bertrand Kempf, [EUPL-1.2](LICENSE).
- **Critères du RAWeb 1.1** (intitulés, tests, cas particuliers, notes techniques, niveaux, références WCAG et EN 301 549) : © Service information et presse (SIP), Luxembourg, [CC BY 3.0 LU](https://creativecommons.org/licenses/by/3.0/lu/), reproduits sans modification. Le RAWeb contient une copie adaptée du RGAA 4.1.2 de la DINUM. Source : <https://github.com/accessibility-luxembourg/ReferentielAccessibiliteWeb>. Ces éléments restent sous leur licence d'origine ; l'EUPL ne s'y applique pas.
  Modifications de RUXAWeb : regroupement par thèmes, étapes de test, gravités, textes d'impact et de test.
- **Sélection des critères** : méthode de contrôle simplifié de l'accessibilité v1.2.1 du SIP, <https://accessibilite.public.lu/fr/monitoring/controle-simplifie.html> (liste des critères ; la grille Excel n'est pas reproduite).
- **WCAG 2.1 et 2.2, WAI-ARIA Authoring Practices** : © W3C. Les numéros et intitulés des critères de succès viennent du RAWeb ; les textes de RUXAWeb sont originaux.
- **Heuristiques d'utilisabilité** : Nielsen Norman Group, <https://www.nngroup.com/articles/ten-usability-heuristics/> (questions reformulées par RUXAWeb, texte d'origine non reproduit).
- **Polices du rapport d'audit** : Plus Jakarta Sans et Lora (Google Fonts, SIL Open Font License), chargées en ligne ; hors ligne, le rapport prend les polices du système.
- **Échelle de gravité** : noms des quatre niveaux inspirés de l'échelle d'impact de Deque (axe-core, MPL-2.0), aucun code repris.
- **Assistance IA** : RUXAWeb a été créé avec l'aide de Claude (Anthropic), qui a participé à la conception de l'outil, a généré une grande partie du code et a donné des conseils de conception. Bertrand Kempf définit l'outil, relit et valide chaque modification.

RUXAWeb n'est ni approuvé ni certifié par le SIP, l'OSAPS, le W3C ou Deque Systems.

## Contribuer
Ouvrez une issue avant une évolution importante. Les critères officiels (numéro, intitulé, niveau) ne se modifient pas. L'outil doit rester accessible (clavier, contrastes, lecteurs d'écran) et sans dépendance réseau. N'ajoutez aucune donnée confidentielle. Le développement se fait dans le dépôt <https://github.com/lijko/ruxal-a11y>.
