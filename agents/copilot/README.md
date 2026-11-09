# Agents Copilot pour RUXAWEB

Deux agents pour **Microsoft 365 Copilot** (Agent Builder), à créer une fois et à réutiliser. Ils acceptent des notes en français ou en anglais et répondent en anglais par défaut (en français sur demande).

| Agent | Ce qu'il fait | Instructions |
|---|---|---|
| **[A11Y] Observation** | Transforme des notes libres en lignes à coller dans RUXAWEB (« Coller des observations »), puis explique chaque critère RAWeb retenu | [`observation-instructions.txt`](observation-instructions.txt) |
| **[A11Y] JIRA Task** | Écrit un ticket Jira au format de l'équipe à partir d'une observation, de notes ou d'un ticket existant | [`jira-task-instructions.txt`](jira-task-instructions.txt) |

## Installer un agent

1. Dans Microsoft 365 Copilot, ouvrir **Agents**, puis **Create agent** (onglet **Configure**).
2. **Name** et **Description** : recopier ceux du tableau ci-dessous.
3. **Instructions** : ouvrir le fichier d'instructions de l'agent, cliquer sur « Raw », tout sélectionner, copier, coller. Moins de 8 000 caractères, la limite d'Agent Builder.
4. **Knowledge** : ajouter le lien de la liste des 136 critères du RAWeb 1.1 :
   `https://github.com/lijko/ruxaweb/blob/main/raweb-1.1-criteria.txt`
   Si l'agent ne trouve pas les critères, joindre le fichier [`raweb-1.1-criteria.txt`](../../raweb-1.1-criteria.txt) à la conversation.
5. **Suggested prompts** : facultatif, voir ci-dessous.
6. **Create**, puis tester avec l'exemple proposé.

| | [A11Y] Observation | [A11Y] JIRA Task |
|---|---|---|
| Name | `[A11Y] Observation` | `[A11Y] JIRA Task` |
| Description | `Turns accessibility notes into RUXAWEB lines and explains the RAWeb 1.1 criteria.` | `Writes an accessibility Jira ticket in the team format from an observation or notes.` |
| Suggested prompts | `Convert my notes` · `RAWeb only` | `Write a ticket from this observation` · `Reformat this ticket` |

## Utiliser l'agent Observation avec RUXAWEB

Coller ses notes dans l'agent, par exemple :

> page Cart : le focus est invisible dans le menu principal ; la case à cocher « Don't ask again on this computer » a une bordure trop pâle.

L'agent rend deux blocs :

1. un **bloc de code** avec les lignes `statut | élément | observation | critères` : bouton « Copier » du bloc, puis RUXAWEB, Saisie, « Coller des observations » ;
2. **Criteria:** chaque critère avec son intitulé officiel et la raison, pour vérifier avant de coller.

Coller toute la réponse fonctionne aussi : RUXAWEB lit les lignes et ignore les explications. Options : `lines only` (le bloc de lignes seul), `RAWeb only` (les critères seuls, sans RUXAWEB).

Les critères proposés par une IA restent à vérifier par l'auditeur.

---

**EN**: two Microsoft 365 Copilot agents. Create each one in Agent Builder: copy the Name and Description above, paste the instruction file into Instructions (under the 8,000 character limit), and add the RAWeb 1.1 criteria list as Knowledge (link above). **[A11Y] Observation** turns notes into lines for RUXAWEB's "Coller des observations" and explains each criterion; **[A11Y] JIRA Task** writes a Jira ticket in the team format.

Licence : instructions © 2026 Bertrand Kempf, CC BY 4.0. Liste des critères du RAWeb 1.1 : © SIP Luxembourg, CC BY 3.0 LU.
