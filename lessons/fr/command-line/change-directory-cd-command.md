---
index: 3
lang: "fr"
title: "cd (Changer de Répertoire)"
meta_title: "cd (Changer de Répertoire) - Ligne de Commande"
meta_description: "Apprenez la commande linux cd essentielle pour changer de répertoire. Ce guide couvre l'utilisation de la commande cd dans une invite de commande, la navigation vers n'importe quel dossier cd avec des chemins absolus et relatifs, et l'utilisation de raccourcis utiles."
meta_keywords: "commande cd, commande cd linux, dossier cd, invite de commande cd, commande cd cmd, changer de répertoire, navigation linux, chemin absolu, chemin relatif"
---

## Lesson Content

Pour vous déplacer dans le système de fichiers Linux, vous utiliserez des chemins pour spécifier votre destination. L'outil principal pour cela est la commande `cd` (change directory, changer de répertoire). Comprendre comment utiliser cette `commande cd linux` est une compétence fondamentale pour travailler dans le terminal ou l'invite de commande `cd command prompt`.

### Comprendre les Chemins

Il existe deux façons de spécifier un chemin : absolu et relatif.

- **Chemin Absolu** : C'est le chemin complet commençant par le répertoire racine (`/`). La racine est le répertoire de plus haut niveau dans le système de fichiers. Tout chemin commençant par `/` est un chemin absolu. Par exemple : `/home/pete/Desktop`.

- **Chemin Relatif** : Ce chemin est relatif à votre emplacement actuel dans le système de fichiers. Si vous êtes dans `/home/pete/Documents` et que vous souhaitez accéder à un sous-répertoire nommé `taxes`, vous n'avez pas besoin du chemin complet. Vous pouvez simplement utiliser le chemin relatif : `taxes/`.

### Utilisation de la commande cd

Une fois que vous comprenez les chemins, vous pouvez utiliser la `commande cd` pour changer votre répertoire courant. Que vous soyez dans un terminal Linux ou une invite de commande Windows `cd command cmd`, le concept de changement de répertoire est universel, bien que la syntaxe puisse légèrement différer.

Pour changer vers un répertoire spécifique en utilisant un chemin absolu, vous taperiez :

```bash
cd /home/pete/Pictures
```

Cette commande vous déplace directement vers le répertoire `Pictures`.

### Navigation vers un dossier cd

Si vous êtes déjà dans un répertoire et que vous souhaitez passer à un sous-répertoire, vous pouvez utiliser un chemin relatif. Par exemple, si votre emplacement actuel est `/home/pete/Pictures` et qu'il contient un `dossier cd` nommé `Hawaii`, vous pouvez y naviguer avec :

```bash
cd Hawaii
```

Remarquez que nous n'avons utilisé que le nom du dossier. C'est parce que nous étions déjà dans son répertoire parent, `/home/pete/Pictures`.

### Raccourcis de Navigation Essentiels

Naviguer avec des chemins complets peut être fastidieux. Heureusement, le shell fournit plusieurs raccourcis pour rendre les déplacements beaucoup plus rapides.

- `.` (répertoire courant) : Représente le répertoire dans lequel vous vous trouvez actuellement.
- `..` (répertoire parent) : Vous déplace d'un niveau vers le répertoire contenant votre répertoire actuel.
- `~` (répertoire personnel) : Un raccourci vers votre répertoire personnel, comme `/home/pete`.
- `-` (répertoire précédent) : Vous ramène au dernier répertoire dans lequel vous étiez.

You can use these shortcuts with the `cd command`:

```bash
cd .
cd ..
cd ~
cd -
```

Expérimentez avec ces raccourcis pour devenir plus efficace sur la ligne de commande.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la navigation dans les répertoires Linux :

1. **[Commande cd Linux : Changement de Répertoire](https://labex.io/fr/labs/linux-linux-cd-command-directory-changing-209733)** - Apprenez la commande `cd` de Linux pour naviguer efficacement dans votre système de fichiers, y compris diverses techniques pour changer de répertoire, comprendre les chemins et explorer la structure des fichiers.
2. **[Navigation dans les Répertoires Linux](https://labex.io/fr/labs/linux-directory-navigation-387844)** - Mettez à l'épreuve vos compétences de base en ligne de commande Linux en naviguant dans les répertoires à l'aide de commandes essentielles.
3. **[Configuration d'une Nouvelle Structure de Projet](https://labex.io/fr/labs/linux-setting-up-a-new-project-structure-387859)** - Pratiquez vos compétences en gestion de répertoires Linux en créant une structure de projet spécifique et en y naviguant à l'aide de commandes essentielles comme `mkdir` et `cd`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance dans la navigation du système de fichiers Linux.

## Quiz Question

If you are in `/home/pete/Pictures` and want to navigate to the parent directory (`/home/pete`), what is the full command you should use? Please answer in English, paying attention to case and spacing.

## Quiz Answer

cd ..
