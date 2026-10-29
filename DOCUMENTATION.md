# Documentation RUXAWEB

## 1. Principe
RUXAWEB sert à **trier avant d'auditer**. Il ne remplace pas l'audit complet du RAWeb 1.1 (136 critères) : il en retient les 52 de la méthode de contrôle simplifié du SIP, qui suffisent à repérer vite les barrières les plus fréquentes sur un site web, puis il aide à rédiger et prioriser les tickets.

L'audit se fait **par observations** : l'auditeur note ce qu'il constate, et la grille des critères se remplit.

## 2. Types d'audit
- **Audit rapide** : les 52 critères sur un échantillon de 3 écrans au moins (accueil, écran avec formulaire, écran au contenu particulier), comme l'audit simplifié du SIP. Dans RUXAWEB, un écran est une page du site, ou un état de page (fenêtre modale ouverte, étape d'un formulaire).
- **Scénario** : un parcours, écran par écran, avec en plus la lecture POUR/UX (section 6).

Chaque onglet garde son propre taux, jamais fusionné avec un autre.

## 3. Observations, statuts et taux
- **Observation** : ce que l'auditeur a vu, entendu ou atteint, un tag (#c conforme, #nc non conforme, #na non applicable) et les critères concernés, proposés à partir d'un point de contrôle. Sans critère, c'est une note libre, sans effet sur les statuts.
- **Statuts** : quatre statuts par critère et par écran, **C**, **NC**, **NT** (non testé), **NA**. Un critère sans observation reste NT ; le pire statut l'emporte (NC, puis C). Un critère n'est conforme pour l'onglet que s'il l'est sur tous ses écrans.
- **Élément et écrans concernés** : deux champs ordinaires de toute observation. L'écran en cours est toujours coché ; l'auditeur coche les autres écrans où l'observation est vraie et peut nommer l'élément (ex. Menu principal). Un élément observé sur au moins deux écrans figure dans la liste « Éléments répétés ». Un #nc vaut NC sur les écrans cochés, un #c y reste à confirmer. Une observation n'a jamais de statut propre : le taux reste comparable à celui du SIP. Un même élément écrit avec une casse, des accents ou des espaces différents est reconnu comme le même.
- **Retest** : depuis la grille, un critère se remet à NT sur un écran ; les observations précédentes restent visibles, barrées.
- **Taux** : calculé sans les NA. Deux taux, même formule : le **taux sélection SIP** (les 52 critères de la méthode du SIP), taux principal, et le **taux élargi**, qui ajoute les 6 critères hors sélection (section 4). La lecture POUR/UX et les bonnes pratiques hors RAWeb n'entrent pas dans le taux.

## 4. Sélection des critères
- Les 52 critères du RAWeb 1.1 retenus par la [méthode de contrôle simplifié v1.2.1 du SIP](https://accessibilite.public.lu/fr/monitoring/controle-simplifie.html) : 47 testés manuellement et 19 avec l'extension Axe (14 critères des deux façons), soit 52 critères distincts. Intitulés, niveaux (A, AA) et références WCAG / EN 301 549 **identiques** au référentiel officiel.
- Contrairement à RUXAAM, aucune adaptation : la méthode du SIP est faite pour le web. Le taux de l'audit rapide porte donc sur la même sélection que l'audit simplifié du SIP, sans en être un résultat officiel (échantillon, environnement et auditeur différents).
- La méthode du SIP ne retient pas certains critères pourtant fréquents en audit complet, par exemple l'agrandissement du texte (10.4), les messages de statut (7.5) ou la compatibilité des scripts avec les technologies d'assistance (7.1).
- **Six critères officiels hors sélection : 3.3, 7.1, 7.5, 9.3, 10.4 et 13.11.** Ils comptent dans le taux élargi et sont exportés vers Jira comme les autres. Ils n'entrent ni dans le taux sélection SIP, ni dans sa complétion.
- Plus 3 bonnes pratiques hors RAWeb (section 10), soit 61 éléments dans l'outil.

## 5. Règle « si présent »
24 critères sur 52 ne s'appliquent que si l'écran contient le contenu concerné. Chacun est rattaché à l'un des huit déclencheurs ci-dessous.

Dans « Préparer les écrans », un interrupteur par écran et par contenu indique ce que contient l'écran. Tout est désactivé au départ. Sur un écran qui ne contient pas le contenu, les critères concernés comptent comme NA. Rien n'est effacé : réactiver un interrupteur retrouve les observations. Il n'y a pas d'interrupteur global : la limite de temps (13.1) est un critère cœur.

| Déclencheur | Le critère s'applique si… | Critères |
|---|---|---|
| CAPTCHA | l'écran contient un CAPTCHA | 1.4, 1.5 |
| Image complexe | l'écran contient une image complexe (graphique, schéma, carte, infographie) | 1.6, 1.7 |
| Média temporel ou son | l'écran contient un audio, une vidéo, ou un son qui se lance seul | 4.1, 4.2, 4.3, 4.4, 4.10, 4.11 |
| Média non temporel | l'écran contient un média non temporel (carte interactive, visite virtuelle, animation ou objet embarqué) | 4.8, 4.9 |
| Tableau de données | l'écran contient un tableau de données | 5.6, 5.7 |
| Cadre (iframe) | l'écran contient un cadre (iframe : vidéo intégrée, carte, formulaire externe) | 2.1 |
| Formulaire | l'écran contient au moins un champ de saisie | 11.1, 11.2, 11.5, 11.6, 11.7, 11.9, 11.10 |
| Autre langue | l'écran contient un passage dans une autre langue que celle de la page | 8.7, 8.8 |

## 6. Parcours d'audit
Le panneau Parcours, fixe et toujours au même endroit, montre l'étape en cours, avec les boutons Précédente et Suivante ; « Voir toutes les étapes » déplie la liste complète (dépliée par défaut sur le tableau de bord, l'outil retient ton choix). Il dit quoi faire et quoi chercher à l'étape en cours.

1. **Préparer les écrans** : noms et contenus.
2. **Étape par étape, sur tous les écrans** : un **tour à vide** (sans outil, pour comprendre les écrans), puis les 4 étapes de test ci-dessous. Chaque étape se fait sur tous les écrans avant de passer à la suivante : on règle l'outil une seule fois (zoom, lecteur d'écran) et on repère tôt les éléments répétés. « Fait sur cet écran » passe à l'écran suivant, puis à l'étape suivante ; la colonne des écrans coche ceux déjà faits pour l'étape en cours. La navigation reste libre : on peut changer d'écran ou d'étape à tout moment, par exemple pour un écran accessible peu de temps.
3. **Lecture POUR/UX** (scénarios seulement) : 8 questions sur le parcours entier, Succès, Difficile, Échec ou N/A, avec un commentaire si difficile ou échec. Le score (succès sur réponses hors N/A) est affiché à part et n'entre jamais dans le taux.
4. **Clôture** : un critère à la fois, avec sa fiche (niveau, comment vérifier, impact, lien officiel, observations), puis le statut de chaque écran encore sans statut (C, NC avec une observation, NA). « Conforme sur les N écrans » existe, mais critère par critère, pour éviter de tout valider en série.
5. **Résumé et exports**.

Les 4 étapes de test, toujours dans cet ordre :

1. **Usage standard** (navigateur sans réglage particulier, à la souris) : information portée par la seule couleur, la forme ou la position, contrastes (avec Colour Contrast Analyser), sous-titres et transcriptions, sons et contenus en mouvement, flashs, limites de temps, CAPTCHA.
2. **Code et outils** : inspecteur du navigateur (clic droit, Inspecter) pour ce qui ne se voit pas à l'écran : alternatives des images, titres des cadres, langue, titre de page, en-têtes des tableaux, zones de la page. Un outil de test automatique gratuit (une extension de navigateur, Axe par exemple) aide à repérer vite certains défauts, en appoint : il ne remplace pas la vérification et ne prouve jamais la conformité. Les consignes « Comment vérifier » de l'outil n'en dépendent pas.
3. **Lecteur d'écran** : NVDA avec Firefox ou Chrome (Windows), ou VoiceOver avec Safari (macOS) ; sur mobile, TalkBack avec Chrome ou VoiceOver avec Safari. 3a : contenus et structure (alternatives, liens, titres, repères, langue) ; 3b : formulaires (étiquettes, groupes, boutons, champs obligatoires, erreurs).
4. **Navigation au clavier** : Tab, Maj+Tab, Entrée, Espace, flèches et Échap ; lien d'évitement, tout atteignable et activable, focus visible, ordre logique, contenus au survol accessibles au clavier, aucun piège. Commande vocale optionnelle en audit rapide.

Un critère se constate parfois à plusieurs étapes : l'outil indique l'étape principale, mais un doute à une autre étape compte. En cas de résultats différents, retiens le pire (NC l'emporte sur C). L'[environnement de test du RAWeb 1.1](https://accessibilite.public.lu/fr/raweb1.1/environnement.html) fait foi pour les combinaisons navigateur et lecteur d'écran.

Séquence construite par RUXAWEB à partir de l'environnement de test et de la méthodologie du RAWeb 1.1 et de la méthode de contrôle simplifié du SIP ; ce n'est pas un protocole officiel.

Répartition (étape principale, bonnes pratiques comprises) : 1. Usage standard : 18 éléments ; 2. Code et outils : 11 ; 3. Lecteur d'écran : 22 ; 4. Navigation au clavier : 10.

**Scénario** : un champ « Transition vers » note une observation sur le passage d'un écran à l'autre, notée Écran -> Écran dans l'observation et dans le ticket Jira.

## 7. Interface, import et exports
- **En-tête** : le nom de l'audit, le **support** (Ordinateur ou Mobile, un audit = un support) et le menu Fichier, puis les onglets de l'audit avec leur état. Dans un onglet, deux vues : Saisie (les observations) et Grille (les critères, par thématique RAWeb ou par thème RUXAL).
- **Import axe ou Lighthouse** : bouton « Importer axe ou Lighthouse » sur l'écran en cours. Rapport JSON d'axe-core, export JSON ou CSV de l'extension axe DevTools (Chrome, Edge), ou rapport Lighthouse enregistré en JSON depuis les outils de développement d'Edge ou de Chrome. Les échecs et les points à vérifier deviennent des pistes, jamais des statuts : « Reprendre » les place dans le formulaire d'observation, « Écarter » les retire. Une règle réussie ne prouve pas la conformité. La correspondance des règles avec les critères a été relue contre la documentation officielle d'axe-core. Lighthouse teste l'écran dans l'état où il est : pour une fenêtre ouverte ou un formulaire en erreur, relance le rapport dans cet état.
- **Exports** (menu Fichier) : grille Excel (avec la lecture POUR/UX pour un scénario), un ticket Jira par observation non conforme (un seul pour une observation qui vaut sur plusieurs écrans), sauvegarde JSON. Chaque ticket reçoit l'étiquette `desktop` ou `mobile-web` selon le support. Référence : « RAWeb 1.1, Criterion X.Y: <intitulé officiel> », avec le lien `https://accessibilite.public.lu/en/raweb1.1/criteres.html#crit-X-Y`. Aucun fichier vide n'est produit : un message explique pourquoi un export n'a pas lieu. L'outil retient les tickets déjà exportés (mémoire gardée dans la sauvegarde) et ne les exporte pas deux fois ; « Tickets Jira : tout réexporter » les reprend tous.
- **Référentiel** (bouton du haut) : toutes les fiches (gravité, étape de test, comment vérifier, impact, lien vers le critère officiel), regroupées par thématique RAWeb ou par thème RUXAL, et la façon de noter les éléments. « Imprimer ou enregistrer en PDF » ouvre l'impression du navigateur : choisir « Enregistrer au format PDF ».
- Les sauvegardes RUXAWEB et RUXAAM sont distinctes : une sauvegarde RUXAAM ne s'ouvre pas dans RUXAWEB.

## 8. Thèmes RUXAL
Taxonomie commune à la famille RUXAL, qui regroupe les critères RAWeb autrement que les 13 thématiques officielles concernées, pour s'aligner sur la façon de travailler d'une équipe produit. Règle : tout ce qui empêche d'atteindre un élément ou un contenu au clavier relève de « Navigation & Structure ». La grille se range par défaut selon les thématiques officielles ; on peut basculer à tout moment vers les thèmes RUXAL.

Navigation & Structure · Composants Interactifs · Images & Médias · Couleurs & Contrastes · Contenu & Lisibilité · Fondations Techniques · Formulaires.

## 9. Gravité
**La gravité n'est pas normative.** Ni le RAWeb ni WCAG 2.x n'en définissent : un critère est conforme ou non. Les niveaux A et AA indiquent l'exigibilité, pas la gêne réelle.

La gravité de RUXAWEB sert à **trier** les non-conformités et à **fixer la priorité** des tickets. C'est une valeur par défaut par critère, pensée pour un défaut qui touche un élément important de l'écran. Elle n'entre jamais dans le taux. Les gravités par défaut reprennent celles des critères équivalents de RUXAAM quand il y en a : c'est une **base de discussion**, non relue critère par critère avec les partenaires.

| Niveau | Repère | Priorité Jira |
|---|---|---|
| **Critique** | Empêche, pour au moins un groupe d'utilisateurs, d'accéder à une fonction ou à un contenu essentiel, sans contournement ; ou met la personne en danger (effets de flash). | Highest |
| **Sérieux** | Barrière forte : rend la tâche très difficile, et peut la bloquer selon le contexte. | High |
| **Modéré** | Difficulté réelle, mais un contournement existe et l'essentiel reste accessible. | Medium |
| **Mineur** | Gêne ou ralentissement, sans empêcher la tâche. | Low |

Répartition par défaut des 52 critères RAWeb : 25 Sérieux, 18 Modéré, 8 Critique, 1 Mineur. Critères hors sélection : 7.1 Critique ; 3.3, 7.5 et 10.4 Sérieux ; 9.3 et 13.11 Modéré.

## 10. Bonnes pratiques hors RAWeb
Trois bonnes pratiques, signalées « Hors RAWeb » et exclues du taux :
- **Taille des cibles (bp1)** : au moins 24×24 px CSS, ou assez d'espace autour (WCAG 2.2, critère 2.5.8, niveau AA ; le RAWeb 1.1 repose sur WCAG 2.1, où seul le critère AAA 2.5.5 en parle).
- **Fermeture d'une fenêtre modale (bp2)** : un bouton visible atteignable au clavier, et la touche Échap.
- **Retour du focus (bp3)** : à la fermeture d'une fenêtre modale, le focus revient sur l'élément qui l'avait ouverte.

## 11. Limites
- Pré-diagnostic : ne produit ni déclaration d'accessibilité ni taux de conformité officiel.
- Même sélection de critères que l'audit simplifié du SIP, mais pas son résultat : l'échantillon, l'environnement de test et l'auditeur diffèrent.
- La méthode du SIP ne couvre pas tout (voir section 4) : l'audit complet du RAWeb reste la référence.
- Les consignes de test sont des aides de lecture : la méthodologie officielle du RAWeb 1.1 fait foi.

## 12. Modifier l'outil
Tout est dans `ruxaweb.html` : les critères et leurs textes se trouvent dans le bloc délimité par `DEBUT_DONNEES` et `FIN_DONNEES`, généré depuis le dépôt de développement (<https://github.com/lijko/ruxal-a11y>). Ne modifiez jamais le numéro, l'intitulé ni le niveau d'un critère officiel.

## 13. Les 58 critères (52 de la sélection SIP, 6 hors sélection)
Intitulés, niveaux et références du RAWeb 1.1 © SIP Luxembourg, CC BY 3.0 LU. Thèmes (regroupement), gravités et étapes : RUXAWEB.

### Navigation & Structure (14, plus 9.3 hors sélection)

| RAWeb | Niveau | Gravité | Étape | Si présent | Intitulé |
|---|---|---|---|---|---|
| 2.1 | A | Modéré | 2 | Cadre (iframe) | Chaque cadre a-t-il un titre de cadre ? |
| 6.1 | A | Sérieux | 3a |  | Chaque lien est-il explicite (hors cas particuliers) ? |
| 6.2 | A | Critique | 3a |  | Dans chaque page web, chaque lien a-t-il un intitulé ? |
| 7.3 | A | Critique | 4 |  | Chaque script est-il contrôlable par le clavier et par tout dispositif de pointage (hors cas particuliers) ? |
| 8.5 | A | Modéré | 2 |  | Chaque page web a-t-elle un titre de page ? |
| 8.6 | A | Modéré | 3a |  | Pour chaque page web ayant un titre de page, ce titre est-il pertinent ? |
| 9.1 | A | Modéré | 3a |  | Dans chaque page web, l’information est-elle structurée par l’utilisation appropriée de titres ? |
| 9.2 | A | Modéré | 2 |  | Dans chaque page web, la structure du document est-elle cohérente ? |
| 10.7 | A | Sérieux | 4 |  | Dans chaque page web, pour chaque élément recevant le focus du clavier, la prise de focus est-elle visible ? |
| 10.14 | A | Sérieux | 4 |  | Dans chaque page web, les contenus additionnels apparaissant via les styles CSS uniquement peuvent-ils être rendus visibles au clavier et par tout dispositif de pointage ? |
| 12.6 | A | Modéré | 3a |  | Les zones de regroupement de contenus présentes dans plusieurs pages web (à l’exception des zones principales constituant la structure du document) peuvent-elles être atteintes ou évitées, si nécessaire ? |
| 12.7 | A | Modéré | 4 |  | Dans chaque page web, un lien d’évitement ou d’accès rapide à la zone de contenu principal est-il présent (hors cas particuliers) ? |
| 12.8 | A | Modéré | 4 |  | Dans chaque page web, l’ordre de tabulation est-il cohérent ? |
| 12.9 | A | Critique | 4 |  | Dans chaque page web, la navigation ne doit pas contenir de piège au clavier. Cette règle est-elle respectée ? |
| 9.3 (hors sélection, taux élargi) | A | Modéré | 3a |  | Dans chaque page web, chaque liste est-elle correctement structurée ? |

### Composants Interactifs (2, plus 7.1, 7.5 et 13.11 hors sélection)

| RAWeb | Niveau | Gravité | Étape | Si présent | Intitulé |
|---|---|---|---|---|---|
| 12.11 | A | Modéré | 4 |  | Dans chaque page web, les contenus additionnels apparaissant au survol, à la prise de focus ou à l’activation d’un composant d’interface sont-ils si nécessaire atteignables au clavier ? |
| 13.1 | A | Sérieux | 1 |  | Pour chaque page web, l’utilisateur a-t-il le contrôle de chaque limite de temps modifiant le contenu (hors cas particuliers) ? |
| 13.11 (hors sélection, taux élargi) | A | Modéré | 1 |  | Dans chaque page web, les actions déclenchées au moyen d’un dispositif de pointage sur un point unique de l’écran peuvent-elles faire l’objet d’une annulation (hors cas particuliers) ? |
| 7.1 (hors sélection, taux élargi) | A | Critique | 3a |  | Chaque script est-il, si nécessaire, compatible avec les technologies d’assistance ? |
| 7.5 (hors sélection, taux élargi) | AA | Sérieux | 3a |  | Dans chaque page web, les messages de statut sont-ils correctement restitués par les technologies d’assistance ? |

### Images & Médias (15)

| RAWeb | Niveau | Gravité | Étape | Si présent | Intitulé |
|---|---|---|---|---|---|
| 1.1 | A | Critique | 2 |  | Chaque image porteuse d’information a-t-elle une alternative textuelle ? |
| 1.2 | A | Mineur | 2 |  | Chaque image de décoration, sans légende, est-elle correctement ignorée par les technologies d’assistance ? |
| 1.3 | A | Sérieux | 3a |  | Pour chaque image porteuse d’information ayant une alternative textuelle, cette alternative est-elle pertinente (hors cas particuliers) ? |
| 1.4 | A | Sérieux | 3a | CAPTCHA | Pour chaque image utilisée comme CAPTCHA ou comme image-test, ayant une alternative textuelle, cette alternative permet-elle d’identifier la nature et la fonction de l’image ? |
| 1.5 | A | Critique | 1 | CAPTCHA | Pour chaque image utilisée comme CAPTCHA, une solution d’accès alternatif au contenu ou à la fonction du CAPTCHA est-elle présente ? |
| 1.6 | A | Modéré | 3a | Image complexe | Chaque image porteuse d’information a-t-elle, si nécessaire, une description détaillée ? |
| 1.7 | A | Modéré | 3a | Image complexe | Pour chaque image porteuse d’information ayant une description détaillée, cette description est-elle pertinente ? |
| 4.1 | A | Sérieux | 1 | Média temporel ou son | Chaque média temporel pré-enregistré a-t-il, si nécessaire, une transcription textuelle ou une audiodescription (hors cas particuliers) ? |
| 4.2 | A | Modéré | 1 | Média temporel ou son | Pour chaque média temporel pré-enregistré ayant une transcription textuelle ou une audiodescription synchronisée, celles-ci sont-elles pertinentes (hors cas particuliers) ? |
| 4.3 | A | Critique | 1 | Média temporel ou son | Chaque média temporel synchronisé a-t-il, si nécessaire, des sous-titres synchronisés (hors cas particuliers) ? |
| 4.4 | A | Sérieux | 1 | Média temporel ou son | Pour chaque média temporel synchronisé ayant des sous-titres synchronisés, ces sous-titres sont-ils pertinents (hors cas particuliers) ? |
| 4.8 | A | Sérieux | 1 | Média non temporel | Chaque média non temporel a-t-il, si nécessaire, une alternative (hors cas particuliers) ? |
| 4.9 | A | Modéré | 1 | Média non temporel | Pour chaque média non temporel ayant une alternative, cette alternative est-elle pertinente ? |
| 4.10 | A | Sérieux | 1 | Média temporel ou son | Chaque son déclenché automatiquement est-il contrôlable par l’utilisateur ? |
| 4.11 | A | Sérieux | 4 | Média temporel ou son | La consultation de chaque média temporel est-elle, si nécessaire, contrôlable par le clavier et tout dispositif de pointage ? |

### Couleurs & Contrastes (4, plus 3.3 hors sélection)

| RAWeb | Niveau | Gravité | Étape | Si présent | Intitulé |
|---|---|---|---|---|---|
| 3.1 | A | Sérieux | 1 |  | Dans chaque page web, l’information ne doit pas être donnée uniquement par la couleur. Cette règle est-elle respectée ? |
| 3.2 | AA | Sérieux | 1 |  | Dans chaque page web, le contraste entre la couleur du texte et la couleur de son arrière-plan est-il suffisamment élevé (hors cas particuliers) ? |
| 10.9 | A | Modéré | 1 |  | Dans chaque page web, l’information ne doit pas être donnée uniquement par la forme, taille ou position. Cette règle est-elle respectée ? |
| 10.10 | A | Modéré | 3a |  | Dans chaque page web, l’information ne doit pas être donnée par la forme, taille ou position uniquement. Cette règle est-elle implémentée de façon pertinente ? |
| 3.3 (hors sélection, taux élargi) | AA | Sérieux | 1 |  | Dans chaque page web, les couleurs utilisées dans les composants d’interface ou les éléments graphiques porteurs d’informations sont-elles suffisamment contrastées (hors cas particuliers) ? |

### Contenu & Lisibilité (4, plus 10.4 hors sélection)

| RAWeb | Niveau | Gravité | Étape | Si présent | Intitulé |
|---|---|---|---|---|---|
| 5.6 | A | Sérieux | 2 | Tableau de données | Pour chaque tableau de données, chaque en-tête de colonne et chaque en-tête de ligne sont-ils correctement déclarés ? |
| 5.7 | A | Sérieux | 2 | Tableau de données | Pour chaque tableau de données, la technique appropriée permettant d’associer chaque cellule avec ses en-têtes est-elle utilisée (hors cas particuliers) ? |
| 13.7 | A | Critique | 1 |  | Dans chaque page web, les changements brusques de luminosité ou les effets de flash sont-ils correctement utilisés ? |
| 13.8 | A | Sérieux | 1 |  | Dans chaque page web, chaque contenu en mouvement ou clignotant est-il contrôlable par l’utilisateur (hors cas particuliers) ? |
| 10.4 (hors sélection, taux élargi) | AA | Sérieux | 1 |  | Dans chaque page web, le texte reste-t-il lisible lorsque la taille des caractères est augmentée jusqu’à 200 %, au moins (hors cas particuliers) ? |

### Fondations Techniques (6)

| RAWeb | Niveau | Gravité | Étape | Si présent | Intitulé |
|---|---|---|---|---|---|
| 8.2 | A | Sérieux | 2 |  | Pour chaque page web, le code source généré est-il valide selon le type de document spécifié ? |
| 8.3 | A | Sérieux | 2 |  | Dans chaque page web, la langue par défaut est-elle présente ? |
| 8.4 | A | Sérieux | 2 |  | Pour chaque page web ayant une langue par défaut, le code de langue est-il pertinent ? |
| 8.7 | AA | Modéré | 3a | Autre langue | Dans chaque page web, chaque changement de langue est-il indiqué dans le code source (hors cas particuliers) ? |
| 8.8 | AA | Modéré | 2 | Autre langue | Dans chaque page web, le code de langue de chaque changement de langue est-il valide et pertinent ? |
| 10.8 | A | Sérieux | 3a |  | Pour chaque page web, les contenus cachés ont-ils vocation à être ignorés par les technologies d’assistance ? |

### Formulaires (7)

| RAWeb | Niveau | Gravité | Étape | Si présent | Intitulé |
|---|---|---|---|---|---|
| 11.1 | A | Critique | 3b | Formulaire | Chaque champ de formulaire a-t-il une étiquette ? |
| 11.2 | A | Sérieux | 3b | Formulaire | Chaque étiquette associée à un champ de formulaire est-elle pertinente (hors cas particuliers) ? |
| 11.5 | A | Sérieux | 3b | Formulaire | Dans chaque formulaire, les champs de même nature sont-ils regroupés, si nécessaire ? |
| 11.6 | A | Sérieux | 3b | Formulaire | Dans chaque formulaire, chaque regroupement de champs de même nature a-t-il une légende ? |
| 11.7 | A | Modéré | 3b | Formulaire | Dans chaque formulaire, chaque légende associée à un regroupement de champs de même nature est-elle pertinente ? |
| 11.9 | A | Sérieux | 3b | Formulaire | Dans chaque formulaire, l’intitulé de chaque bouton est-il pertinent (hors cas particuliers) ? |
| 11.10 | A | Sérieux | 3b | Formulaire | Dans chaque formulaire, le contrôle de saisie est-il utilisé de manière pertinente (hors cas particuliers) ? |
