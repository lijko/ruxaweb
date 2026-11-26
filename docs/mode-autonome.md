# Mode autonome (spécification)

Statut : spécification, non développée. L'outil actuel (version 3.43) n'est pas modifié.

## Objectif

Pouvoir mener un audit avec RUXAWeb sans Jira. Jira reste le mode habituel ; le mode autonome sert à un auditeur qui n'a pas Jira (autre client, indépendant, SIP) ou qui ne veut pas créer de tickets.

Le point de convergence n'est plus Jira mais le **format d'import** de RUXAWeb. Toutes les sources écrivent ce même format ; l'outil importe sans savoir d'où viennent les tickets.

## Deux modes, choisis à la création du projet

| | Mode Jira (actuel) | Mode autonome |
|---|---|---|
| Entrées | Export CSV de Jira, converti par l'agent « Jira -> RUXAWeb » | Import Playwright (a11y-tests) et observations formatées par un agent IA |
| Clés des tickets | Clés Jira (`POST-123`) | Clés locales (voir plus bas) |
| Statut d'un ticket | Vient de Jira | Défini dans RUXAWeb |
| Réglages Jira | Affichés | Masqués |
| Grille, taux, livrables | Identiques | Identiques |

Le mode est exclusif : un projet ne mélange pas tickets Jira et tickets locaux. Cela évite les doublons et les règles de fusion entre Jira et le reste.

Non-régression : un projet sauvegardé sans mode est en mode Jira. Le mode Jira garde exactement le comportement actuel.

## Format commun

On garde `ruxaweb-tasks-1` (voir DOCUMENTATION.md, « Format d'import »), avec deux ajouts facultatifs, ignorés par l'outil actuel :

```json
{
  "format": "ruxaweb-tasks-1",
  "source": "playwright",
  "tickets": [
    {
      "key": "",
      "summary": "[A11Y] | Souscription | Forms | Personal details[field \"Email\"]: No label",
      "status": "open",
      "priority": "Major",
      "criteria": ["11.1"],
      "lines": [{"screen": "Personal details", "element": "Personal details[field \"Email\"]", "sip": "..."}],
      "epic": "Forms",
      "labels": ["Accessibility", "code"],
      "reco": "...",
      "recommendations": ["..."],
      "pour": "", "ux": [], "warnings": []
    }
  ]
}
```

- `source` (racine) : `jira`, `playwright` ou `observation`. Absent : `jira`.
- `key` vide autorisé en mode autonome : l'outil attribue la clé à l'import. **Attention** : la version 3.43 ignore tout ticket sans clé (vérifié sur son code d'import) ; la sortie « json » de l'agent ne sera importable qu'une fois l'étape 2 faite.
- `jiraStatus` et `updated` deviennent facultatifs.

Le format est le contrat : a11y-tests, l'agent d'observation et l'agent Jira écrivent tous cette structure, décrite une seule fois ici et dans DOCUMENTATION.md.

## Les deux entrées du mode autonome

### 1. Import Playwright (a11y-tests)

a11y-tests écrit un fichier `ruxaweb-tasks.json` (source `playwright`) par site et par jour, à côté de ses rapports.

- Seulement les **non-conformités axe** avec la correspondance SIP (`axe-raweb-mapping.txt`), comme les brouillons de tickets actuels.
- Les résultats « à revoir » et les pistes IBM n'y entrent jamais : une piste confirmée par l'auditeur passe par l'entrée 2.
- Clé stable : `PW-` suivi d'un court hachage de (règle, critère, écran, élément). Un nouveau passage de tests met donc à jour le même ticket au lieu d'en créer un autre.
- Un ticket Playwright absent d'un nouveau passage passe en **Corrigé** (à retester) : axe ne trouve plus le défaut, la confirmation reste à l'auditeur.

### 2. Observations par agent IA

L'auditeur écrit son observation en langage normal ; un agent la convertit en fichier JSON (source `observation`), à importer.

- L'auditeur ne voit jamais la syntaxe : c'est la différence avec les lignes à coller de RUXAWeb 2, jugées trop lourdes.
- `key` vide : l'outil attribue `OBS-001`, `OBS-002`… dans l'ordre d'import.
- Consignes de l'agent **agnostiques** : aucun assistant nommé, aucune fonction propre à un outil, 8 000 caractères au plus. C'est l'agent « [A11Y] Obs. -> Jira & RAWeb » lui-même, avec la sortie « json » : même analyse que pour un ticket Jira (critères, notation, gravité, epic, labels), champs `sip` et `reco` en français comme l'agent « Jira -> RUXAWeb ».
- Sortie : le fichier `.json` ; si l'assistant ne sait pas produire de fichier, le même JSON dans un bloc de code, à enregistrer à la main.

## Règles d'import

Aujourd'hui, un import met à jour par clé et, dès qu'il y a déjà des tickets, marque « absents » ceux qui ne sont pas dans le fichier. En mode autonome, cette règle ne vaut que **par source** :

| Import | Ajoute et met à jour | Marque absents |
|---|---|---|
| `jira` (mode Jira) | oui | les tickets Jira manquants (comportement actuel) |
| `playwright` | oui | aucun : les tickets Playwright manquants passent en Corrigé (à retester) |
| `observation` | oui | jamais : un import d'observations s'ajoute, il n'efface rien |

L'utilisateur importe toujours « un fichier », sans mode d'import à choisir (l'import partiel a été retiré le 23 novembre 2026 parce qu'il était confus).

Doublon possible entre sources (une NC Playwright aussi décrite par une observation) : l'outil le signale dans les points à vérifier (même critère, même écran, même élément), sans fusion automatique. L'auditeur rejette l'un des deux.

## Statut des tickets en mode autonome

Sans Jira, c'est l'outil qui porte le statut. Sur la fiche d'un ticket : **Ouvert**, **Corrigé** (à retester), **Rejeté**, avec les mêmes effets sur la grille et le taux qu'en mode Jira (un ticket corrigé remet la case en NT, un ticket rejeté ne compte pas).

En mode Jira, rien ne change : le statut se corrige dans Jira.

## Livrables

Identiques dans les deux modes : grille officielle du SIP, rapport d'audit, rapport équipe. En mode autonome, le rapport équipe cite les clés locales, sans lien vers Jira.

## Hors périmètre (pour plus tard)

- Passer un projet autonome en mode Jira (créer les tickets dans Jira et reprendre leurs clés).
- Un formulaire de saisie sans IA, en secours de l'agent.

## Décisions (26 novembre 2026)

1. Ticket Playwright absent d'un nouveau passage : Corrigé, à retester.
2. Clés locales : `OBS-` pour les observations, `PW-` pour Playwright.
3. Agents : deux seulement. « [A11Y] Obs. -> Jira & RAWeb » (ticket Jira par défaut, critères seuls avec « raweb », fichier JSON avec « json ») remplace « Observation -> Jira Task », « Observation -> RAWeb » et l'agent d'observation prévu ; « axe -> Jira Tasks » est retiré (a11y-tests produit les tickets axe). « Jira -> RUXAWeb » reste pour le mode Jira.

## Étapes

1. Cette spécification.
2. RUXAWeb : choix du mode, champ `source`, clés locales, règles d'import par source, statut éditable en mode autonome.
3. a11y-tests : export `ruxaweb-tasks.json` depuis les non-conformités.
4. Jeu d'exemples d'observations en JSON dans `exemples/` (l'agent est fait).
