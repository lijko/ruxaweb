# RUXAWeb : Revue UX Accessibilité (web), suivi par tickets

RUXAWeb réunit les tickets Jira d'accessibilité d'un projet web dans la grille du RAWeb 1.1 (sélection de l'audit simplifié du SIP). Il remplit la **grille officielle du SIP** et produit deux rapports Word : un pour le SIP (en français), un pour l'équipe (en anglais). Jira reste la seule source des non-conformités : pas de double saisie, pas d'écart entre les tickets et la grille.

Il fait partie de la famille RUXAL, avec [RUXAAM](https://github.com/lijko/ruxaam) (applications mobiles). RUXAWeb 4 est l'ancien **RUXAWeb Tasks**, renommé le 26 novembre 2026 ; l'ancien RUXAWeb 2 (audit par observations) est archivé sur la branche `archive/v2.67`. Un mode sans Jira est spécifié dans [docs/mode-autonome.md](docs/mode-autonome.md). L'audit simple est un **pré-diagnostic**, pas un audit de conformité. L'audit complet suit la méthodologie de test du SIP ; l'auditeur reste responsable du résultat et de la déclaration d'accessibilité.

## Utiliser

Ouvrir `ruxaweb.html` dans un navigateur. L'outil fonctionne hors ligne ; le projet est gardé dans le navigateur et se sauvegarde en `.json` (menu Fichier).

Même interface que RUXAWeb 2 : onglets en haut, grille et fiches des critères, panneau à droite avec les repères et l'aide « Comment tester ».

Le bouton **English / Français** de la barre du haut change la langue de l'interface. En anglais, les intitulés des critères sont les intitulés officiels anglais du RAWeb 1.1 ; les consignes « Comment vérifier », les impacts, les tests officiels et le contenu des tickets restent tels quels. Les livrables gardent leur langue : grille et rapport du SIP en français, rapport équipe en anglais.

1. **Projet** : exporter les tickets de Jira en CSV, les convertir avec l'agent **[A11Y] Jira -> RUXAWeb** (commentaires SIP en français), puis importer son fichier .json. Un ticket connu est mis à jour, jamais doublé.
2. **Onglet** : un audit simple (les 3 écrans de l'échantillon du SIP), un audit complet (les 136 critères, tests officiels, taux selon la méthodologie du SIP) ou un scénario. Les écrans se choisissent parmi ceux des tickets.
3. **Grille** : les NC viennent des tickets ouverts ; on pose C ou NA sur le reste. Un ticket corrigé remet la case à tester.
4. **Résumé** : grille officielle du SIP remplie, rapport d'audit (Word, français, sur le modèle de rapport d'audit RAWeb du SIP), rapport équipe (Word, anglais). Les boutons restent indisponibles tant qu'il manque les tickets Jira, la grille vierge ou les écrans, et disent ce qui manque.

Les tickets s'écrivent avec l'agent **[A11Y] Obs. -> Jira & RAWeb** ; les non-conformités automatiques viennent de Playwright (axe-core). Règles et formats : [DOCUMENTATION.md](DOCUMENTATION.md) ; agents : [`agents/copilot/`](agents/copilot/).

## Contenu du dépôt

| Fichier | Rôle |
|---|---|
| `ruxaweb.html` | l'outil, un seul fichier hors ligne |
| `DOCUMENTATION.md` | règles de statut, import, formats |
| `agents/copilot/` | instructions des deux agents (Microsoft 365 Copilot ou tout autre assistant) |
| `axe-raweb-mapping.txt` | correspondance des règles axe-core vers les critères RAWeb : table du SIP (méthode de contrôle simplifié) pour ses 41 règles, table RUXAL pour les autres |
| `exemples/` | jeu de données de test « Souscription » (tickets à importer dans Jira, exports, réponses d'agent attendues) |
| `raweb-1.1-criteria.txt` | les 136 critères du RAWeb 1.1 (EN et FR, niveau officiel et correspondance WCAG du SIP), connaissance de l'agent Obs. -> Jira & RAWeb |

## Licences et crédits

- **Code, textes et agents** : © 2026 Bertrand Kempf, [EUPL-1.2](LICENSE) ; instructions des agents et documentation sous CC BY 4.0.
- **Critères du RAWeb 1.1** : © Service information et presse (SIP), Luxembourg, CC BY 3.0 LU.
- **Heuristiques d'utilisabilité** : Nielsen Norman Group (noms reformulés).
- **Assistance IA** : RUXAWeb a été créé avec l'aide de Claude (Anthropic), qui a généré une grande partie du code et donné des conseils de conception. Bertrand Kempf définit l'outil, relit et valide chaque modification.

RUXAWeb n'est ni approuvé ni certifié par le SIP, l'OSAPS ou le W3C.
