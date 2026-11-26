# Agents pour RUXAWeb

Deux agents, à créer une fois. Leurs instructions sont agnostiques : écrites pour **Microsoft 365 Copilot** (Agent Builder, 8 000 caractères au plus), elles fonctionnent dans tout assistant qui accepte des instructions et un fichier de connaissance. Ils acceptent le français et l'anglais et répondent en anglais par défaut.

| Agent | Ce qu'il fait | Instructions |
|---|---|---|
| **[A11Y] Obs. -> Jira & RAWeb** | D'une observation, de notes ou d'un ticket existant : un ticket Jira au format de l'équipe (par défaut), les critères RAWeb seuls (« raweb »), ou un fichier à importer dans RUXAWeb (« json », mode autonome). **Référence** : ce fichier fait foi | [`A11Y-Obs-to-Jira-and-RAWeb.txt`](A11Y-Obs-to-Jira-and-RAWeb.txt) |
| **[A11Y] Jira -> RUXAWeb** | Mode Jira : lit l'export CSV de Jira et rend le fichier d'import de RUXAWeb, avec un commentaire SIP en français par écran | [`A11Y-Jira-to-RUXAWeb.txt`](A11Y-Jira-to-RUXAWeb.txt) |

L'agent Obs. -> Jira & RAWeb remplace depuis le 26 novembre 2026 les agents « Observation -> Jira Task » et « Observation -> RAWeb ». L'agent « axe -> Jira Tasks » est retiré : les non-conformités axe viennent de Playwright (a11y-tests). Les copies des anciennes consignes dans RUXAL sont à mettre à jour (celles de RUXAWeb 2 sont archivées avec lui).

## Installer un agent

1. Microsoft 365 Copilot, **Agents**, **Create agent**, onglet **Configure** (ou l'équivalent de l'assistant utilisé).
2. **Name** et **Description** : voir le tableau ci-dessous.
3. **Instructions** : ouvrir le fichier, « Raw », tout copier, coller.
4. **Knowledge** (agent Obs. -> Jira & RAWeb) : téléverser [`raweb-1.1-criteria.txt`](../../raweb-1.1-criteria.txt) (les critères du RAWeb 1.1, puis les bonnes pratiques BP1 à BP3). En secours, le lien public : `https://github.com/lijko/ruxaweb/blob/main/raweb-1.1-criteria.txt`. Le fichier change : le téléverser à nouveau.
5. **Create**, puis tester avec le jeu de données de [`../../exemples/`](../../exemples/).

| | Name | Description | Suggested prompts |
|---|---|---|---|
| Observation | `[A11Y] Obs. -> Jira & RAWeb` | `Turns an accessibility observation into a Jira ticket in the team format, or into a RUXAWeb import file.` | `Write a ticket from this observation` · `raweb` · `json` |
| Import | `[A11Y] Jira -> RUXAWeb` | `Converts a Jira CSV export of accessibility tickets into an import block for RUXAWeb, with French SIP comments.` | `Convert this export` |

## Utiliser l'agent Obs. -> Jira & RAWeb

| Écrire | Obtenir |
|---|---|
| l'observation seule | le ticket Jira |
| l'observation + `raweb` | les critères seuls : numéro, intitulé officiel, raison, et « Also check » pour ce qui dépend de ce que l'agent ne voit pas |
| l'observation + `json` | le fichier d'import RUXAWeb |

- **Mode Jira** : coller l'observation. L'agent choisit les critères dans le fichier de connaissance (ou garde ceux donnés), écrit le ticket (rubriques en titre 2), puis propose priorité, labels et epic. À copier dans Jira.
- **Mode autonome** : coller une ou plusieurs observations et ajouter « json ». L'agent rend le fichier `ruxaweb-observations.json`, à importer dans RUXAWeb ; l'outil attribue les clés `OBS-`. **Pas encore utilisable** : la version 3.43 ignore les tickets sans clé, il faut d'abord développer le mode autonome. Voir [`../../docs/mode-autonome.md`](../../docs/mode-autonome.md).
- Dans les deux cas, « To clarify: » liste ce qui manque ; c'est l'auditeur qui décide C, NC ou NA.

## Utiliser l'agent d'import

1. RUXAWeb, page Projet : **Ouvrir le filtre dans Jira**, puis dans Jira **Exporter**, **CSV (tous les champs)**.
   Le filtre garde les tickets corrigés (Ready for testing, Ready to deploy in production, In production) pour que le retest soit proposé ; seul Canceled peut en être exclu. L'agent classe lui-même chaque statut.
2. Ouvrir l'agent, joindre le fichier. Sans fichier, l'agent le demande.
3. Télécharger le fichier `ruxaweb-import.json` que l'agent propose, puis RUXAWeb, page Projet, **Importer les tickets**. L'agent liste aussi les tickets avec des avertissements, à vérifier avant l'import.

Sans agent, le fichier de Jira s'importe aussi directement : les commentaires de la grille restent alors en anglais.

Les bonnes pratiques arrivent dans un ticket par la ligne `Good practice BP1` de Reference ; l'agent d'import les rend en `BP1`.

L'agent ne décide d'aucun statut : il lit les tickets et traduit le défaut en une phrase pour la grille SIP. Les commentaires restent à relire.

Licence : instructions © 2026 Bertrand Kempf, CC BY 4.0.
