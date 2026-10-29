# RUXAWEB : Revue UX Accessibilité (web)

**FR** : Outil HTML autonome (un seul fichier, hors ligne) qui aide à **préparer et prioriser un audit d'accessibilité de site web**, avant l'audit complet. L'audit se fait **par observations** : l'auditeur note ce qu'il constate, et la grille des critères se remplit. Il croise :

- **les 52 critères du RAWeb 1.1** (référentiel du SIP, Luxembourg) retenus par la [méthode de contrôle simplifié v1.2.1 du SIP](https://accessibilite.public.lu/fr/monitoring/controle-simplifie.html), dont 24 « si présent », qui donnent un **taux de conformité** ;
- **6 critères RAWeb hors sélection du SIP** (3.3, 7.1, 7.5, 9.3, 10.4, 13.11), qui comptent dans un **taux élargi**, affiché à côté du taux sélection SIP ;
- **3 bonnes pratiques** hors RAWeb (taille des cibles, fermeture d'une fenêtre modale, retour du focus), hors taux ;
- pour les scénarios, **une lecture POUR/UX** qualitative, **exclue du taux**.

Deux types d'audit : audit rapide (3 écrans au moins, comme l'audit simplifié du SIP) et scénario. Parcours guidé écran par écran (tour à vide, 4 étapes de test, clôture), aide toujours au même endroit, observations valables sur plusieurs écrans, retest, import de rapports axe ou Lighthouse. Exports Excel (grille des critères), CSV (import Jira) et JSON.

RUXAWEB n'est **pas un audit de conformité** et ne produit aucune déclaration d'accessibilité : c'est un outil de pré-diagnostic, qui complète l'audit d'un expert. Il fait partie de la famille RUXAL, avec [RUXAAM](https://github.com/lijko/ruxaam) pour les applications mobiles.

**EN** : Standalone, offline, single-file HTML tool to **prepare and prioritise a website accessibility audit**. The auditor records observations and the criteria grid fills itself: the **52 RAWeb 1.1 criteria** of the SIP simplified audit method (Luxembourg's web accessibility standard; compliance rate), plus 6 extra criteria (extended rate) and 3 best practices. Guided screen-by-screen flow, axe and Lighthouse report import, Excel, Jira and JSON exports. It is **not a compliance audit**.

## Utilisation
Ouvrir `ruxaweb.html` dans un navigateur. Aucune installation, aucun serveur, aucun appel réseau. Les données restent dans le navigateur ; l'audit se sauvegarde et se rouvre en JSON (menu Fichier).

## Contenu du dépôt
| Fichier | Rôle |
|---|---|
| `ruxaweb.html` | l'outil |
| `DOCUMENTATION.md` | observations et taux, sélection des critères, règle « si présent », parcours d'audit, gravités, limites, liste des 58 critères |
| `LICENSE` | EUPL-1.2 |
| `README.md` | ce fichier |

## Licence et attributions
- **Code, textes d'impact et de test, thèmes, gravités et bonnes pratiques de RUXAWEB** : © 2026 Bertrand Kempf, [EUPL-1.2](LICENSE).
- **Critères du RAWeb 1.1** (intitulés, niveaux, références WCAG et EN 301 549) : © Service information et presse (SIP), Luxembourg, [CC BY 3.0 LU](https://creativecommons.org/licenses/by/3.0/lu/), reproduits sans modification. Le RAWeb contient une copie adaptée du RGAA 4.1.2 de la DINUM. Source : <https://github.com/accessibility-luxembourg/ReferentielAccessibiliteWeb>. Ces éléments restent sous leur licence d'origine ; l'EUPL ne s'y applique pas.
  Modifications de RUXAWEB : regroupement par thèmes, étapes de test, gravités, textes d'impact et de test.
- **Sélection des critères** : méthode de contrôle simplifié de l'accessibilité v1.2.1 du SIP, <https://accessibilite.public.lu/fr/monitoring/controle-simplifie.html> (liste des critères ; la grille Excel n'est pas reproduite).
- **WCAG 2.1 et 2.2, WAI-ARIA Authoring Practices** : © W3C. Les numéros et intitulés des critères de succès viennent du RAWeb ; les textes de RUXAWEB sont originaux.
- **Heuristiques d'utilisabilité** : Nielsen Norman Group, <https://www.nngroup.com/articles/ten-usability-heuristics/> (questions reformulées par RUXAWEB, texte d'origine non reproduit).
- **Échelle de gravité** : noms des quatre niveaux inspirés de l'échelle d'impact de Deque (axe-core, MPL-2.0), aucun code repris.

RUXAWEB n'est ni approuvé ni certifié par le SIP, l'OSAPS, le W3C ou Deque Systems.

## Contribuer
Ouvrez une issue avant une évolution importante. Les critères officiels (numéro, intitulé, niveau) ne se modifient pas. L'outil doit rester accessible (clavier, contrastes, lecteurs d'écran) et sans dépendance réseau. N'ajoutez aucune donnée confidentielle. Le développement se fait dans le dépôt <https://github.com/lijko/ruxal-a11y>.
