# Jeu de données de test : « Souscription »

Un parcours de souscription fictif : écrans Home, Offers, Plan details, Personal details, Payment, Confirmation (et Account, cité par un ticket mais absent des onglets). 15 tickets Jira couvrent tous les cas de l'import.

| Fichier | Rôle |
|---|---|
| `jira-import-souscription.csv` | les tickets à importer dans un projet Jira de test (6 epics, 15 tâches) |
| `jira-export-test-1.json` | premier export Jira (format `/rest/api/2/search/jql`), 14 tickets |
| `jira-export-test-2.json` | second export, tous les tickets : 2 tickets modifiés, 1 nouveau |
| `jira-export-test-1-fr.csv` | les tickets de `jira-export-test-1.json` en export CSV de Jira, interface en français (séparateur point-virgule) |
| `jira-export-test-bp.json` | un ticket sur une bonne pratique (BP1, taille de cible), importé sans agent : « à traduire » dans les points à vérifier |
| `reponse-agent-test-1.json` | réponse attendue de l'agent pour l'export 1 |
| `reponse-agent-test-2.json` | réponse attendue de l'agent pour l'export 2 |
| `projet-test.json` | sauvegarde du projet de démonstration (Fichier, Ouvrir) |
| `axe-home-test.json` | rapport axe-core de l'écran Home |

## Les tickets

| Ticket | Cas testé | Écran(s) | Critère | Statut Jira |
|---|---|---|---|---|
| SUB-201 | NC simple | Personal details | 11.9 | To Do, puis Done (export 2) |
| SUB-202 | défaut sur tous les écrans (« All ») | All | 3.2 | In Progress |
| SUB-203 | ticket corrigé : à retester | Personal details | 11.10 | Done |
| SUB-204 | gravité modifiée entre deux exports | Payment | 12.8 | To Do (Critical, puis Major) |
| SUB-205 | un ticket sur deux écrans | Home ; Offers | 1.1 | To Do |
| SUB-206 | ticket fermé, défaut toujours compté (Won't Do) | Offers | 13.8 | Done |
| SUB-207 | doublon (Duplicate) | Home | 1.1 | Done |
| SUB-208 | écran absent des onglets | Account | 6.1 | To Do |
| SUB-209 | statut intermédiaire, tableau | Plan details | 5.7 | In Review |
| SUB-210 | critère RAWeb hors de l'outil | Personal details | 11.13 | To Do |
| SUB-211 | ticket UX sans critère | Personal details | aucun | To Do |
| SUB-212 | ticket sans label Accessibility | | | In Progress |
| SUB-213 | description au format ADF (Jira Cloud v3) | Offers | 10.7 | To Do |
| SUB-214 | « All » corrigé : à retester partout | All | 12.7 | Done |
| SUB-215 | nouveau ticket (export 2) | Personal details | 11.1 | To Do |

## Tester l'outil seul (sans Copilot)

1. Page Projet, tuile **Projet de démonstration** : 13 tickets importés, un onglet « Audit SIP » (Home, Offers, Personal details) et un scénario « Parcours de souscription ».
2. Onglet Audit SIP, **Compléter la grille**. Attendu :
   - 1.1 NC sur Home et Offers (SUB-205), 3.2 NC partout (SUB-202), 10.7 NC sur Offers, 11.9 NC sur Personal details ;
   - 11.10 sur Personal details et 12.7 partout : NT, tickets corrigés à retester ;
   - une case avec un ticket ouvert ne se change pas dans la grille : elle se corrige dans Jira.
3. Fiche d'un critère : lien vers le ticket, comment vérifier, impact, critère officiel.
4. Projet, **Importer un fichier** : `reponse-agent-test-2.json`. SUB-201 passe à retester, SUB-215 ajoute 11.1 NC sur Personal details.
5. Onglet, **Résumé et livrables** : charger la grille vierge du SIP, télécharger la grille remplie et les deux rapports.

Avec l'export Jira brut (`jira-export-test-1.json`) dans un projet vide : mêmes tickets, commentaires en anglais ; le nouvel onglet propose les écrans les plus cités.

## Tester l'agent d'import

Joindre `jira-export-test-1.json` à l'agent **[A11Y] Jira -> RUXAWeb** et comparer sa réponse à `reponse-agent-test-1.json` : mêmes tickets, mêmes statuts (SUB-206 en « open » avec un avertissement, SUB-207 en « rejected »), SUB-212 dans « skipped », SUB-211 sans critère avec un avertissement, SUB-213 lu malgré le format ADF. Les phrases françaises peuvent différer, mais doivent rester factuelles et sans nom d'écran au début.

Données entièrement fictives.

## Tester dans un vrai Jira

1. Projet Jira de test. **Paramètres, Système, Importation externe, CSV** (ou, dans un projet, **Importer des tickets**), fichier `jira-import-souscription.csv`.
2. Correspondance des colonnes : Issue Id, Issue Type, Summary, Epic Name, Description, Priority, Labels (les 3 colonnes), Parent. Les epics sont créés d'abord ; chaque tâche est rattachée à son epic par Parent.
3. Tous les tickets arrivent « À faire ». Pour tester les statuts, passer à la main :
   - en **Terminé** (corrigé) : « Personal details[field "Email"] » et « All.header[link "Skip to content"] » ;
   - en **Terminé** avec la résolution **Won't Do** : « Offers[carousel] » ;
   - en **Terminé** avec la résolution **Duplicate** : « Home[image "Spring offer"]: No alt ».
4. Filtre JQL : `project = <CLÉ> AND labels = Accessibility`. Dans RUXAWeb, renseigner l'adresse et le filtre (Projet, Réglages Jira), ouvrir l'export, enregistrer le JSON, l'importer (directement ou via l'agent).
5. Pour tester un second import : passer « Personal details[button "Continue"] » en Terminé, ajouter un ticket, réimporter.

La tâche « Update payment provider SDK » n'a pas le label : elle doit être ignorée.
