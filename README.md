# RUXAWEB : Revue UX Accessibilité (web)

**FR** : Outil HTML autonome (un seul fichier, hors ligne) qui aide à **préparer et prioriser un audit d'accessibilité de site web**, avant l'audit complet. Il croise :

- **les 52 critères du RAWeb 1.1** (référentiel du SIP, Luxembourg) retenus par la [méthode de contrôle simplifié v1.2.1 du SIP](https://accessibilite.public.lu/fr/monitoring/controle-simplifie.html), dont 24 « si présent », évalués un à un (conforme, non conforme, non testé, non applicable), qui donnent un **taux de conformité** ;
- **une lecture UX qualitative** (principes POUR de WCAG et heuristiques d'utilisabilité), **exclue du taux** ;
- **le critère RAWeb 13.11** (annulation d'une action au pointeur), absent de la sélection du SIP : évalué à titre indicatif, **hors taux** ;
- **3 bonnes pratiques** hors RAWeb (taille des cibles, fermeture d'une fenêtre modale, retour du focus), également hors taux.

Trois types d'audit : audit rapide, fonctionnalité primaire, scénario. Exports CSV, Jira, JSON et PDF.

- **Même sélection que l'audit simplifié du SIP** : les 52 critères, sur un échantillon de 3 pages au moins (accueil, page avec formulaire, page au contenu particulier). Le taux se lit donc à côté d'un audit simplifié du SIP, sans en être un résultat officiel.
- **Protocole de test en 4 étapes** : 1. usage standard, 2. code et outils (Axe, inspecteur), 3. lecteur d'écran (3a contenus et structure, 3b formulaires), 4. navigation au clavier. Chaque critère est rattaché à l'étape où on le constate le plus facilement. Séquence construite par RUXAWEB à partir de l'environnement de test et de la méthodologie du RAWeb 1.1 et de la méthode simplifiée du SIP ; ce n'est pas un protocole officiel.
- **Vue « Par étape de test »** : la liste d'un onglet RAWeb se range par thème ou par étape, sans effet sur le taux ni les exports.
- **Support** (Ordinateur ou Mobile) : un audit = un support ; il détermine les recommandations et l'étiquette des tickets Jira.
- **Contenu des pages** : un interrupteur par page et par type de contenu (CAPTCHA, image complexe, média temporel ou son, média non temporel, tableau de données, cadre, formulaire, autre langue). Un critère « si présent » ne s'affiche que là où le contenu existe ; ailleurs il compte comme NA, sans rien effacer.
- **Pages testées** : dans un onglet, le panneau « Pages testées » permet de renommer, d'ajouter ou de supprimer (en deux clics) une page en cours d'audit. Un ajout ou une suppression repasse l'onglet en brouillon ; une nouvelle page part en NT. L'audit rapide garde au moins 3 pages. Les tickets Jira déjà créés ne sont pas modifiés.
- **Une page à la fois** : au-delà de 6 pages (outil pensé pour l'ordinateur), la liste n'affiche plus que la page choisie en tête de liste, avec la colonne « Toutes » et le statut d'ensemble de l'onglet sur chaque critère.
- **Élément concerné** : pour chaque critère non conforme, la notation `Page[type "Libellé"] (état)` (expliquée dans l'Aide) désigne l'élément en cause ; l'export Jira la reprend, avec la référence « RAWeb 1.1, Criterion X.Y » et son lien officiel.
- **Exports** : jamais de fichier vide ; un message explique pourquoi un export n'a pas lieu. L'outil retient les tickets Jira déjà exportés et ne les exporte pas deux fois (« Tickets Jira : tout réexporter » pour tout reprendre).

RUXAWEB n'est **pas un audit de conformité** et ne produit aucune déclaration d'accessibilité : c'est un outil de pré-diagnostic, qui complète l'audit d'un expert. Il fait partie de la famille RUXAL, avec [RUXAAM](https://github.com/lijko/ruxaam) pour les applications mobiles.

**EN** : Standalone, offline, single-file HTML tool to **prepare and prioritise a website accessibility audit**. It combines the **52 RAWeb 1.1 criteria** of the SIP simplified audit method (Luxembourg's web accessibility standard; compliance rate) with a **qualitative UX layer** (WCAG POUR principles and usability heuristics; excluded from the rate). It offers a 4-step test protocol (standard use, code and tools, screen reader, keyboard), a view by test step, per-page content switches for conditional criteria, an « affected element » field, and Jira export with memory of exported tickets. It is **not a compliance audit**.

## Utilisation
Ouvrir `ruxaweb.html` dans un navigateur. Aucune installation, aucun serveur, aucun appel réseau. Les données restent dans le navigateur ; l'état s'exporte et s'importe en JSON. Pour essayer l'outil, importer `donnees-fictives-ruxaweb-v1.0.json` (bouton « Importer »).

## Contenu du dépôt
| Fichier | Rôle |
|---|---|
| `ruxaweb.html` | l'outil |
| `DOCUMENTATION.md` | sélection des critères, règle « si présent », protocole de test, gravités, limites, liste des 52 critères |
| `donnees-fictives-ruxaweb-v1.0.json` | audit fictif à importer pour essayer l'outil |
| `LICENSE` | EUPL-1.2 |
| `README.md` | ce fichier |

## Licence et attributions
- **Code, textes d'impact et de test, thèmes, gravités et bonnes pratiques de RUXAWEB** : © 2026 Bertrand Kempf, [EUPL-1.2](LICENSE).
- **Critères du RAWeb 1.1** (intitulés, niveaux, références WCAG et EN 301 549) : © Service information et presse (SIP), Luxembourg, [CC BY 3.0 LU](https://creativecommons.org/licenses/by/3.0/lu/), reproduits sans modification. Le RAWeb contient une copie adaptée du RGAA 4.1.2 de la DINUM. Source : <https://github.com/accessibility-luxembourg/ReferentielAccessibiliteWeb>. Ces éléments restent sous leur licence d'origine ; l'EUPL ne s'y applique pas.
  Modifications de RUXAWEB : regroupement par thèmes, étapes de test, gravités, textes d'impact et de test.
- **Sélection des critères** : méthode de contrôle simplifié de l'accessibilité v1.2.1 du SIP, <https://accessibilite.public.lu/fr/monitoring/controle-simplifie.html> (liste des critères et règles Axe citées ; la grille Excel n'est pas reproduite).
- **jsPDF 2.5.1** (embarqué dans `ruxaweb.html`) : © 2010-2021 James Hall et contributeurs, licence MIT. Les en-têtes de copyright de la bibliothèque et de ses greffons sont conservés dans le fichier.
- **WCAG 2.1 et 2.2, WAI-ARIA Authoring Practices** : © W3C. Les numéros et intitulés des critères de succès viennent du RAWeb ; les textes de RUXAWEB sont originaux.
- **Heuristiques d'utilisabilité** : Nielsen Norman Group, <https://www.nngroup.com/articles/ten-usability-heuristics/> (questions reformulées par RUXAWEB, texte d'origine non reproduit).
- **Échelle de gravité** : noms des quatre niveaux inspirés de l'échelle d'impact de Deque (axe-core, MPL-2.0), aucun code repris.

RUXAWEB n'est ni approuvé ni certifié par le SIP, l'OSAPS, le W3C ou Deque Systems.

## Contribuer
Ouvrez une issue avant une évolution importante. Les critères officiels (numéro, intitulé, niveau) ne se modifient pas. L'outil doit rester accessible (clavier, contrastes, lecteurs d'écran) et sans dépendance réseau. N'ajoutez aucune donnée confidentielle. Le développement se fait dans le dépôt <https://github.com/lijko/ruxal-a11y>.
