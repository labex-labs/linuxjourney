---
index: 3
lang: "fr"
title: "cd (Changer de répertoire)"
meta_title: "cd (Changer de répertoire) - Ligne de commande"
meta_description: "Apprenez la commande Linux cd avec des exemples de chemins absolus, chemins relatifs, raccourcis vers le répertoire personnel, répertoires parents et navigation vers le répertoire précédent."
meta_keywords: "commande cd, commande linux cd, changer de répertoire, cd répertoire parent, cd home, cd répertoire précédent, chemin absolu, chemin relatif"
---

## Lesson Content

Pour naviguer dans le système de fichiers Linux, vous utilisez des chemins pour spécifier votre destination. L'outil principal pour cela est la commande `cd`, abréviation de change directory (changer de répertoire). Elle modifie le répertoire de travail actuel du shell.

La syntaxe de base est :

```bash
cd [DIRECTORY]
```

### Comprendre les chemins

Il existe deux façons de spécifier un chemin : absolu et relatif.

- **Chemin absolu** : Le chemin complet à partir du répertoire racine (`/`). Par exemple : `/home/pete/Desktop`.

- **Chemin relatif** : Un chemin basé sur votre emplacement actuel. Si vous êtes dans `/home/pete/Documents` et souhaitez accéder à un sous-répertoire nommé `taxes`, vous pouvez utiliser `taxes/`.

### Utilisation de la commande cd

Pour changer vers un répertoire spécifique en utilisant un chemin absolu, tapez :

```bash
$ cd /home/pete/Pictures
```

Cette commande vous déplace directement dans le répertoire `Pictures`.

Vous pouvez confirmer votre emplacement avec `pwd` :

```bash
$ pwd
/home/pete/Pictures
```

### Naviguer vers un sous-répertoire

Si vous êtes déjà dans un répertoire et souhaitez vous déplacer vers un sous-répertoire, utilisez un chemin relatif. Par exemple, si votre emplacement actuel est `/home/pete/Pictures` et qu'il contient un dossier nommé `Hawaii`, vous pouvez y naviguer avec :

```bash
$ cd Hawaii
```

Notez que nous avons utilisé uniquement le nom du dossier. C'est parce que nous étions déjà dans son répertoire parent, `/home/pete/Pictures`.

### Raccourcis essentiels pour la navigation

Naviguer avec des chemins complets peut être fastidieux. Heureusement, le shell fournit plusieurs raccourcis pour rendre les déplacements beaucoup plus rapides.

- `.` (répertoire courant) : Représente le répertoire dans lequel vous vous trouvez actuellement.
- `..` (répertoire parent) : Vous fait remonter d'un niveau vers le répertoire contenant votre répertoire actuel.
- `~` (répertoire personnel) : Un raccourci vers votre répertoire personnel, comme `/home/pete`.
- `-` (répertoire précédent) : Vous ramène au dernier répertoire dans lequel vous étiez.

Vous pouvez utiliser ces raccourcis avec `cd` :

```bash
$ cd .
$ cd ..
$ cd ~
$ cd -
```

Expérimentez avec ces raccourcis pour devenir plus efficace en ligne de commande.

### Exemples pratiques de cd

Aller dans votre répertoire personnel :

```bash
$ cd
```

Remonter de deux niveaux :

```bash
$ cd ../..
```

Aller dans un répertoire dont le nom contient des espaces en le citant :

```bash
$ cd "Vacation Photos"
```

Revenir au répertoire précédent :

```bash
$ cd -
/home/pete/Documents
```

### Questions fréquentes

**Pourquoi cd affiche-t-il "No such file or directory" ?** Le chemin n'existe pas depuis votre emplacement actuel, ou le nom a été mal tapé. Utilisez `ls` pour lister les répertoires disponibles.

**Pourquoi cd affiche-t-il "Permission denied" ?** Vous n'avez pas la permission d'entrer dans ce répertoire.

**Que se passe-t-il lorsque j'exécute cd sans argument ?** Cela vous amène dans votre répertoire personnel.

**Est-ce que cd fonctionne sur les fichiers ?** Non. `cd` change de répertoire, pas de fichier ordinaire.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la navigation dans les répertoires Linux :

1. **[Commande Linux cd : Changement de répertoire](https://labex.io/fr/labs/linux-linux-cd-command-directory-changing-209733)** - Apprenez la commande Linux `cd` pour naviguer efficacement dans votre système de fichiers, y compris diverses techniques pour changer de répertoire, comprendre les chemins et explorer la structure des fichiers.
2. **[Navigation dans les répertoires Linux](https://labex.io/fr/labs/linux-directory-navigation-387844)** - Mettez vos compétences de base en ligne de commande Linux à l'épreuve en naviguant à travers les répertoires avec les commandes essentielles.
3. **[Mise en place d'une nouvelle structure de projet](https://labex.io/fr/labs/linux-setting-up-a-new-project-structure-387859)** - Entraînez-vous à gérer les répertoires Linux en créant une structure de projet spécifique et en naviguant à travers elle avec des commandes essentielles comme `mkdir` et `cd`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance dans la navigation du système de fichiers Linux.

## Quiz Question

If you are in `/home/pete/Pictures` and want to navigate to the parent directory (`/home/pete`), what is the full command you should use? Please answer in English, paying attention to case and spacing.

## Quiz Answer

cd ..
