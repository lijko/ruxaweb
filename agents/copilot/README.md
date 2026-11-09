# Agents Copilot pour RUXAWEB

Trois agents pour **Microsoft 365 Copilot** (Agent Builder), un par usage, à créer une fois et à réutiliser. Ils acceptent des notes en français ou en anglais et répondent en anglais, sauf si vous demandez explicitement le français (« en français »).

| Agent | Ce qu'il fait | Critères couverts | Connaissance | Instructions |
|---|---|---|---|---|
| **[A11Y] Observation -> RUXAWEB** | Transforme des notes libres en lignes à coller dans RUXAWEB (« Coller des observations »), puis explique brièvement chaque critère | Les 58 critères et 3 bonnes pratiques de RUXAWEB, inclus dans les instructions | Aucune | [`observation-ruxaweb-instructions.txt`](observation-ruxaweb-instructions.txt) |
| **[A11Y] Observation -> RAWeb** | Donne les critères RAWeb concernés par une observation, avec leur intitulé officiel et la raison | Les 136 critères du RAWeb 1.1 | Liste des critères | [`observation-raweb-instructions.txt`](observation-raweb-instructions.txt) |
| **[A11Y] JIRA Task** | Écrit un ticket Jira au format de l'équipe à partir d'une observation, de notes ou d'un ticket existant | Les 136 critères du RAWeb 1.1 | Liste des critères | [`jira-task-instructions.txt`](jira-task-instructions.txt) |

## Installer un agent

1. Dans Microsoft 365 Copilot, ouvrir **Agents**, puis **Create agent** (onglet **Configure**).
2. **Name** et **Description** : recopier ceux du tableau ci-dessous.
3. **Instructions** : ouvrir le fichier d'instructions de l'agent, cliquer sur « Raw », tout sélectionner, copier, coller. Chaque fichier fait moins de 8 000 caractères, la limite d'Agent Builder.
4. **Knowledge** (agents RAWeb et JIRA Task seulement) : ajouter le lien de la liste des 136 critères du RAWeb 1.1 :
   `https://github.com/lijko/ruxaweb/blob/main/raweb-1.1-criteria.txt`
   Copilot ne consulte pas toujours cette connaissance. Un intitulé qu'il ne trouve pas est remplacé par le numéro seul, signalé sous « To clarify: ». Joindre alors le fichier [`raweb-1.1-criteria.txt`](../../raweb-1.1-criteria.txt) à la conversation.
5. **Suggested prompts** : facultatif, voir ci-dessous.
6. **Create**, puis tester.

| | Name | Description | Suggested prompts |
|---|---|---|---|
| RUXAWEB | `[A11Y] Observation -> RUXAWEB` | `Turns accessibility notes into lines to paste into RUXAWEB, with RAWeb 1.1 criteria.` | `Convert my notes` · `lines only` |
| RAWeb | `[A11Y] Observation -> RAWeb` | `Lists the RAWeb 1.1 criteria concerned by an accessibility observation.` | `Which criteria apply?` |
| JIRA | `[A11Y] JIRA Task` | `Writes an accessibility Jira ticket in the team format from an observation or notes.` | `Write a ticket from this observation` · `Reformat this ticket` |

## Utiliser l'agent Observation -> RUXAWEB

Coller ses notes dans l'agent, par exemple :

> page Login : la case « Don't ask again on this computer » a un contour trop pâle.

L'agent rend deux blocs :

1. un **bloc de code** avec les lignes `statut | élément | observation | critères` : bouton « Copier » du bloc, puis RUXAWEB, Saisie, « Coller des observations » ;
2. **Criteria:** chaque critère avec son sujet et la raison, pour vérifier avant de coller.

Coller toute la réponse fonctionne aussi : RUXAWEB lit les lignes et ignore les explications. Option : `lines only` pour le bloc de lignes seul. Un défaut hors des critères de RUXAWEB n'est pas forcé dans une ligne : l'agent le signale et renvoie vers l'agent JIRA Task.

Les critères proposés par une IA restent à vérifier par l'auditeur.

---

**EN**: three Microsoft 365 Copilot agents. Create each one in Agent Builder: copy the Name and Description above and paste the instruction file into Instructions (under the 8,000 character limit). The RAWeb and JIRA Task agents also need the RAWeb 1.1 criteria list as Knowledge (link above); the RUXAWEB agent needs none, its 58 criteria and 3 good practices are in its instructions.

Licence : instructions © 2026 Bertrand Kempf, CC BY 4.0. Liste des critères du RAWeb 1.1 : © SIP Luxembourg, CC BY 3.0 LU.
