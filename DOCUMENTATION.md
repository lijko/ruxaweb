# RUXAWeb : documentation

## Principe

Jira est la seule source des non-conformités. RUXAWeb lit les tickets, les place dans la grille RAWeb 1.1 (écran × critère), laisse l'auditeur définir le reste (C, NA) et exporte la grille SIP. L'outil reste hors ligne et sans IA : l'IA travaille dans Copilot, l'auditeur colle son résultat.

Le processus n'est pas linéaire. Les tickets se créent au fil de l'audit et des corrections, l'import se fait aussi souvent que nécessaire.

## Interface

RUXAWeb 4 (anciennement RUXAWeb Tasks) reprend l'interface et la grille de RUXAWeb 2 (version 2.62 ; la 2.67 est archivée sur la branche `archive/v2.67`), sans la saisie des observations ni les fonctions primaires. Un NC vient d'un ticket : la fiche d'un critère permet seulement d'étendre le NC d'un ticket ouvert à d'autres écrans.

| Où | Rôle |
|---|---|
| Projet | import des tickets Jira, points à vérifier, réglages Jira (adresse, filtre), onglets, démo |
| Onglet, Écrans | écrans de l'onglet, choisis parmi ceux des tickets ; contenus des écrans (NA) |
| Onglet, Grille | statut de chaque critère par écran ; la fiche d'un critère donne comment vérifier, l'impact, le lien vers le RAWeb et les tickets |
| Onglet, Lecture POUR/UX | scénarios seulement, comme dans RUXAWeb 2 |
| Onglet, Résumé | taux, non-conformités, livrables |
| Panneau de droite | repères (tickets, écrans, grille, résumé) et « Comment tester » : tour à vide, usage standard et vues responsives, code et outils, lecteur d'écran, clavier. Une aide à consulter, rien à cocher. |

**Langue de l'interface.** Le bouton English / Français de la barre du haut bascule l'interface entre le français et l'anglais ; le choix est gardé dans le navigateur. Une couche de traduction agit sur le texte affiché seulement : textes, noms accessibles, bulles et textes indicatifs. En anglais :

- traduits : menus, boutons, étapes, messages, thèmes, contenus des écrans, intitulés des critères (intitulés officiels anglais du RAWeb 1.1), liens vers le site du SIP (pages anglaises) ;
- inchangés : « Comment vérifier », impacts, tests officiels, notes techniques, contenu des tickets et noms saisis (projet, onglets, écrans). Un texte resté en français reçoit `lang="fr"` pour le lecteur d'écran ;
- livrables : aucun changement, la grille du SIP et le rapport d'audit restent en français, le rapport équipe en anglais. La sauvegarde JSON est la même dans les deux langues.

**Et maintenant ?** Après un import ou un téléchargement, une ou deux lignes sous le bouton indiquent la suite, selon la situation : créer un onglet, ajouter un écran cité par les tickets, retester les tickets corrigés, compléter la grille, envoyer la grille et le rapport au SIP, partager le rapport équipe.

## Conventions Jira

- **Label** `Accessibility` sur chaque ticket d'accessibilité (les titres en `[A11Y]` sont aussi acceptés). Labels indicatifs `design`, `code`.
- **Epic** : un epic par thème RUXAL, au nom anglais (Navigation & structure, Interactive components, Images & media, Colors & contrast, Content & readability, Technical foundations, Forms). Il donne le thème des recommandations.
- **Priority** : Critical, Major, Medium, Minor (gravité).
- **Description** : les rubriques de l'agent [A11Y] Obs. -> Jira & RAWeb, dont `Reference` (`RAWeb 1.1, Criterion X.Y`, ou `Good practice BP1` pour une bonne pratique), seule source du critère.

## Import

- **Réglages** : l'adresse de Jira est ramenée au site (une adresse de ticket ou de tableau collée telle quelle fonctionne) ; le filtre est nettoyé (« jql= », adresse encodée, guillemets typographiques, ORDER BY retirés). Jira montre une éventuelle erreur de filtre dans sa recherche.
- **Export** : « Ouvrir le filtre dans Jira » ouvre la recherche de Jira avec le filtre entier du projet. On exporte toujours tous les tickets du filtre. Dans Jira : Exporter, CSV (tous les champs).
- **Conversion** : le CSV de Jira est joint à l'agent « [A11Y] Jira -> RUXAWeb », qui rend un fichier JSON (format `ruxaweb-tasks-1`) avec les commentaires de la grille SIP en français. C'est ce fichier qu'on importe.
- **Sans agent** : le CSV de Jira (en-têtes en anglais ou en français, séparateur virgule ou point-virgule) ou le JSON de l'API de Jira s'importent aussi directement ; les commentaires restent alors en anglais et sont signalés « à traduire ».
- **Écrans** : un écran cité dans un ticket et absent du projet est ajouté automatiquement.
- **Nom d'écran lu** : ce qui précède `[` ou `.` dans « Element(s) in concern », sans commentaire libre (une parenthèse ou un deux-points coupe le nom : « Sign-in (and potentially…) » donne Sign-in). Un élément global cité sans écran (Footer, Header, Main navigation, Menu, Breadcrumb, Search…) vaut pour tous les écrans (« All »). Les lignes de parcours (`->` ou `→`, Jira remplaçant la flèche) sont ignorées.
- **Mise à jour** : la clé Jira identifie le ticket. Un ticket connu est remplacé par sa nouvelle version, jamais dupliqué. Les statuts posés dans la grille (C, NA, NC étendu) ne sont pas touchés.
- **Ticket absent** : un ticket connu absent du fichier (supprimé dans Jira ou sorti du filtre) est signalé « absent » dans les points à vérifier, et sort de la grille. Il revient s'il réapparaît dans un import suivant.

## Règles de statut d'une case (écran × critère)

1. Un ticket **ouvert** sur ce critère et cet écran (ou « All ») : **NC**.
2. Un ticket **corrigé** : **NT, à retester**, jusqu'à ce qu'un statut soit posé après la correction.
3. Un statut posé dans la grille (C, NA) : ce statut.
4. Contenu absent de l'écran (interrupteur de la vue Projet) : **NA** pour les critères liés.
5. Sinon : **NT**.

### Contenus des écrans (critères « si présent »)

- **Un seul endroit** : « Écrans de l'onglet ». La grille et la fiche d'un critère affichent le résultat, sans interrupteur ; la fiche renvoie vers « Écrans de l'onglet ».
- **Tout est activé au départ** : on désactive ce que l'écran ne contient pas. Un oubli laisse le critère à tester, jamais en NA silencieux. Penser aux états (erreur, chargement, après soumission).
- **Colonne « Tous »** : un switch par contenu, activé si le contenu est sur tous les écrans ; le désactiver le retire de tous les écrans (sauf ceux verrouillés par un ticket NC), l'activer le met sur tous.
- **Verrou NC** : un contenu dont un critère est NC sur l'écran (ticket ouvert) est verrouillé : switch activé, au rouge du NC, cadenas dans le bouton, clé du ticket en lien dessous. Il se libère quand le ticket est corrigé ou rejeté, puis réimporté. Un ticket NC ouvert sur un contenu désactivé active ce contenu à l'import.
- **Statut gardé** : désactiver un contenu masque les C déjà posés ; ils reviennent si on le réactive.
- **Contenus** : CAPTCHA, image complexe, média temporel, média non temporel, tableau de données, cadre, formulaire, autre langue, contenu au survol ou au focus (10.14, 12.11 ; 10.13 en audit complet), contenu en mouvement ou clignotant (13.7, 13.8), limite de temps (13.1), et pour l'audit complet tableau de mise en forme, document à télécharger, outil d'édition, communication en temps réel.
- **Grille** : un NA par contenu absent s'affiche « — » ; un critère dont le contenu est absent de tous les écrans passe dans le bloc replié « Non applicables » (visible avec le filtre NA). Un NC à ticket ouvert porte un cadenas ; la clé du ticket est dans la fiche du critère. Le chiffre à côté d'un statut compte les tickets, à partir de 2.
- **Liste des écrans** : « 9 NC · 1 BP » = 9 critères RAWeb non conformes, 1 bonne pratique non suivie (hors RAWeb, hors taux).
- **Grille du SIP** : seuls les NC reçoivent un commentaire (colonne Problèmes détectés) ; les NA, C et NT restent sans commentaire.
- **Sauvegardes d'avant la 3.24** : les contenus non activés restent absents (mêmes statuts) ; les trois contenus ajoutés en 3.24 restent présents.

Bouton NC de la fiche d'un critère :

- un ticket **ouvert** porte déjà ce critère sur un autre écran de l'onglet : l'écran passe en NC, **rattaché à ce ticket** (« via CLÉ »), avec le texte du défaut du ticket. S'il y a plusieurs tickets, on choisit lequel ;
- aucun ticket ouvert sur ce critère : rien n'est posé, l'outil rappelle de créer le ticket dans Jira, puis d'importer.

Un NC étendu suit son ticket : ticket corrigé, l'écran repasse en NT à retester ; ticket rejeté, le NC ne compte plus ; écran ajouté au ticket dans Jira puis réimporté, le NC étendu s'efface au profit de celui du ticket. Le commentaire de la grille du SIP reprend la clé du ticket. Après l'extension, l'outil rappelle d'ajouter l'écran au ticket dans Jira.

Un ticket fermé dans Jira compte selon sa résolution : Done ou Fixed, corrigé (à retester, NT) ; Won't Fix, Won't Do, Declined, Rejected ou une autre résolution, toujours ouvert (le défaut reste, NC) ; Duplicate, Cannot Reproduce, Not a bug ou Obsolete, **rejeté** : il n'entre pas dans la grille. Statuts de l'équipe, prioritaires : **Ready for testing** (correction livrée en environnement de test), **Ready to deploy in production** et **In production** valent corrigé, **Canceled** vaut rejeté.

Filtre JQL : garder les statuts qui valent corrigé, sinon le ticket n'arrive jamais et le retest n'est jamais proposé Seul Canceled peut être exclu sans perte, par exemple `AND status != Canceled`. Un ticket qui sort du filtre est signalé « absent » au prochain import. Statut global d'un critère : le pire l'emporte (NC, puis NT), NA si non applicable partout.

## Taux

- **Taux sélection SIP** : critères de la sélection de l'audit simplifié du SIP, comparable à un audit simplifié.
- **Taux élargi** : sélection plus les critères hors sélection.
- Les bonnes pratiques n'entrent dans aucun taux. Un taux est **provisoire** tant qu'il reste des NT.
- Niveaux : Conforme (100 %), Bon (75 à 99), À améliorer (50 à 74), Insuffisant (moins de 50).

## Points à vérifier

Écran d'un ticket dans aucun onglet, critère inconnu du référentiel, critère présent seulement dans l'audit complet quand le projet n'en a pas, ticket sans critère ni bonne pratique, commentaire SIP à traduire (import sans l'agent), avertissements de l'agent, ticket absent du dernier import complet, NC étendu à des écrans que le ticket ne cite pas encore (à ajouter dans Jira).

Un écran ajouté plus tard dans le projet récupère ses tickets sans nouvel import.

## Audit complet

Un onglet d'audit complet couvre les 136 critères du RAWeb 1.1, comme dans RUXAWeb 2 : tests officiels dans chaque fiche, échantillon représentatif sans maximum (il part des écrans cités dans les tickets), un seul taux selon la méthodologie du SIP (validés sur tous les écrans / applicables sur un écran au moins) et l'état de conformité qu'il donne, taux par écran dans le résumé. Un ticket sur un critère hors de la sélection du SIP (11.13, par exemple) y trouve sa ligne.

Le résumé de l'onglet porte les champs du **rapport d'audit** : site, réalisé par, adresses, technologies et outils, environnement de test, processus, exemptions et dérogations, avis. Le rapport se télécharge en Word, dans les livrables (voir Rapport d'audit plus bas). Les constats de l'annexe technique sont les commentaires SIP des tickets, avec leur clé Jira.

Un scénario a le même bloc, pour un **rapport de parcours** (taux sélection SIP et lecture POUR/UX), en page HTML à imprimer en PDF. La grille officielle du SIP reste ceux de l'audit simplifié : ils se font depuis un audit simple.

## Bonnes pratiques hors RAWeb

Trois bonnes pratiques complètent la grille : BP1 taille de cible (24 × 24 px CSS ou espacement), BP2 fermeture d'une modale (bouton visible et Échap), BP3 retour du focus à la fermeture d'une modale. Un ticket les vise par la ligne `Good practice BP1: ...` de sa rubrique Reference, seulement si aucun critère RAWeb ne couvre le défaut. Elles ont leur ligne dans la grille et entrent dans le rapport équipe ; elles restent hors taux, hors grille SIP et hors rapport SIP.

## Scénarios et lecture POUR / UX

Un scénario est un onglet comme dans RUXAWeb 2 : ses écrans, dans l'ordre du parcours, reçoivent les tickets qui les citent. Il a son taux et sa lecture UX/POUR, remplie dans l'onglet comme dans RUXAWeb. Aucun label de scénario n'est nécessaire dans Jira.

## Livrables

### Échantillon du SIP
La grille de l'audit simplifié compte 3 pages (P01 à P03) : les 3 premiers écrans de l'audit simple, avec leur adresse et le site (Résumé de l'onglet). La grille de l'audit complet compte 15 pages : les écrans de l'onglet d'audit complet (15 au plus), les pages inutilisées étant masquées comme le prévoit le mode d'emploi du SIP.

### Grilles officielles du SIP
- Source : les modèles du SIP, copiés dans le dossier [`sip/`](sip/) du dépôt : `template-grille-audit-simplifie.xlsx` (audit simple) et `raweb1-1-lu-modele-grille-audit.xlsx` (audit complet). La grille française du dépôt simplA11yMonit n'est plus acceptée : ses liens de calcul étaient cassés.
- Chaque type d'audit charge sa grille vierge, gardée dans le navigateur. Au chargement, l'outil vérifie les onglets (Sample, P01 et suivants), les colonnes Status et Problems detected et les critères (53 ou 136). Un fichier incompatible est refusé. Une version différente du modèle connu est signalée, et le remplissage continue.
- Remplissage : Status (C, NC, NA, NT) et Problems detected (`défaut (CLÉ)` en français, sans notation d'élément) pour chaque page ; onglet Sample : date, site, titres et adresses des pages. En audit complet, le statut suit la méthodologie du SIP (processus compris). Les formules du SIP restent intactes ; Excel recalcule à l'ouverture.
- La colonne Derogation reste à remplir à la main.

### Rapport d'audit (Word, français)
Un seul rapport pour l'audit simple et l'audit complet, sans charte graphique, sur la structure du modèle de rapport d'audit RAWeb du SIP (CC BY 3.0 LU) :
- **Introduction** : contexte (référentiel, technologies, outils, environnement de test, échantillon avec adresses ; dérogations et processus en audit complet) et accessibilité du site (taux, état de conformité en audit complet, critères non conformes par gravité).
- **Description des non-conformités**, par thématique du RAWeb : chaque critère non conforme avec son enjeu, sa gravité et les problèmes relevés par page (commentaire SIP du ticket et clé Jira). Pas de recommandations : elles sont dans le rapport équipe et dans les tickets. Une thématique sans NC le dit, en précisant s'il reste des critères non testés.
- **Conclusion** : avis de l'auditeur, priorisation des corrections (critères non conformes par gravité).
- **Annexe** : résultats par critère et par page (audit simple), par page et par thématique (audit complet).

Présentation reprise des rapports publiés par le SIP, sans logo : titres noirs soulignés d'un filet gris, encadré gris pour le taux, « Cas rencontré : critère X.Y » avec l'enjeu du critère puis « Exemples de problèmes détectés sur la page… » (lien vers l'adresse), code entre accents graves en police à chasse fixe, pied de page « rapport | site | n/N ». Le rapport équipe reprend la même présentation.

L'audit simple ne remplit que ce qui le concerne : 3 pages, sélection de la méthode de contrôle simplifié (taux selon l'échelle du SIP, mention « pré-diagnostic »), thématiques 14 à 17 signalées comme non évaluées. Les bonnes pratiques hors RAWeb n'y figurent pas (elles sont dans le rapport équipe).

### Boutons des livrables
Un livrable indisponible garde son bouton, grisé (`aria-disabled`, toujours atteignable au clavier) ; une ligne dessous dit ce qui manque :
- grille remplie : tickets Jira importés, grille vierge chargée, 3 écrans (audit simple) ou de 1 à 15 écrans (audit complet) ;
- rapport d'audit : tickets Jira importés, 3 écrans (audit simple) ou au moins un écran (audit complet) ;
- rapport équipe : tickets Jira importés.

### Rapport pour l'équipe (Word, anglais)
Résumé (tickets ouverts par gravité, retests, taux), priorités par thème avec recommandations des tickets, liste des retests, parcours (lecture POUR / UX), clés de lecture.

## Export Excel (menu Fichier)

- **Grille SIP (Excel)** : critère, sélection, thématique, intitulé, niveau WCAG, statut global, statut par écran, commentaire. Une ligne de commentaire par écran (ou « Tous les écrans »), avec la clé Jira en fin de ligne si l'option du Guide est active.
- **Lecture POUR / UX (Excel)** : un ticket par ligne, avec scénario, principe, heuristiques, gravité, critères, écrans.
- **Sauvegarde (.json)** : tout le projet, à rouvrir avec « Ouvrir un projet ».

## Format d'import (`ruxaweb-tasks-1`)

```json
{
  "format": "ruxaweb-tasks-1",
  "tickets": [{
    "key": "PHX-123", "summary": "...", "status": "open | fixed | rejected",
    "jiraStatus": "In Progress", "updated": "2026-11-12T09:14:00.000+0100", "priority": "Major",
    "criteria": ["11.10"],
    "lines": [{"screen": "Contact", "element": "Contact[field \"Email\"]", "sip": "Phrase en français."}],
    "labels": ["Accessibility", "code"],
    "epic": "Forms", "reco": "Recommandation en français.", "recommendations": ["Recommendation copied from the ticket."],
    "warnings": []
  }],
  "skipped": [{"key": "PHX-90", "reason": "..."}]
}
```

`criteria` : numéros RAWeb (`11.10`) et codes de bonnes pratiques (`BP1`). `screen` vaut `All` pour un défaut présent sur tous les écrans. `ux` : codes N1 à N10 (heuristiques de Nielsen). La gravité vient de la priorité Jira (Critical, Major, Medium, Minor), sinon du critère.

## Mode autonome (spécification)

Un mode sans Jira est spécifié dans [docs/mode-autonome.md](docs/mode-autonome.md) : import Playwright et observations formatées par un agent, même format d'import. Non développé.
