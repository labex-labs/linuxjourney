---
index: 2
lang: "fr"
title: "pwd (Afficher le Répertoire de Travail)"
meta_title: "pwd (Afficher le Répertoire de Travail) - Ligne de Commande"
meta_description: "Maîtrisez la commande linux pwd pour afficher votre répertoire actuel sous Linux. Cette leçon explique la signification complète de pwd sous linux et comment naviguer dans l'arborescence des répertoires sous linux."
meta_keywords: "linux pwd, répertoire actuel linux, arborescence répertoires linux, signification pwd linux, afficher répertoire de travail, chemin linux, navigation linux, bases ligne de commande"
---

## Lesson Content

Sous Linux, un concept fondamental est que tout est traité comme un fichier. Ces fichiers sont organisés au sein d'une structure hiérarchique connue sous le nom de système de fichiers. Comprendre cette structure est essentiel pour naviguer efficacement dans votre système.

### L'Arborescence des Répertoires sous Linux

L'intégralité du système de fichiers commence à partir d'un seul répertoire de niveau supérieur appelé le répertoire racine, représenté par une barre oblique (`/`). Depuis la racine, l'**arborescence des répertoires sous linux** se ramifie en divers sous-répertoires, qui peuvent contenir des fichiers et d'autres sous-répertoires.

Voici un exemple simplifié de cette structure :

```plaintext
/
|-- bin
|   |-- file1
|   |-- file2
|-- etc
|   |-- file3
|   `-- directory1
|       |-- file4
|       `-- file5
|-- home
|-- var
```

### Comprendre les Chemins de Fichiers

L'emplacement de tout fichier ou répertoire est décrit par son chemin. Un chemin est une séquence de répertoires qui mène d'un point de départ à une destination spécifique. Par exemple, si vous avez un dossier nommé `pete` à l'intérieur du répertoire `/home`, et un dossier `Movies` à l'intérieur de `pete`, le chemin complet serait `/home/pete/Movies`.

### Quelle est la Signification de PWD sous Linux ?

Lors de la navigation dans le système de fichiers, il est essentiel de connaître votre emplacement actuel. La commande pour cela est `pwd`. La **signification de pwd sous linux** est "print working directory" (afficher le répertoire de travail). Son seul objectif est d'afficher le chemin complet du répertoire dans lequel vous vous trouvez actuellement, en commençant par la racine (`/`).

### Utilisation de la Commande linux pwd

Pour trouver votre **répertoire actuel linux**, tapez simplement la commande **linux pwd** et appuyez sur Entrée. Elle affiche le chemin absolu de votre emplacement présent dans la ligne de commande.

```bash
pwd
```

Où êtes-vous ? Où suis-je ? Essayez pour voir votre propre répertoire de travail actuel.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la navigation dans le système de fichiers Linux et de l'identification de votre emplacement actuel :

1.  **[Commande Linux pwd : Affichage de Répertoire](https://labex.io/fr/labs/linux-linux-pwd-command-directory-displaying-209734)** - Ce laboratoire fournit un aperçu ciblé et une utilisation pratique de la commande `pwd`, s'alignant directement sur l'introduction de la leçon pour trouver votre répertoire actuel.
2.  **[Navigation dans les Répertoires Linux](https://labex.io/fr/labs/linux-directory-navigation-387844)** - Mettez à l'épreuve vos compétences de base en ligne de commande Linux en naviguant dans divers répertoires, consolidant ainsi votre compréhension des chemins et de la structure du système de fichiers.
3.  **[Commande Linux cd : Changement de Répertoire](https://labex.io/fr/labs/linux-linux-cd-command-directory-changing-209733)** - Apprenez à naviguer efficacement dans votre système de fichiers à l'aide de la commande `cd`, en comprenant les différentes techniques pour changer de répertoire et explorer la structure des fichiers.

Ces laboratoires vous aideront à appliquer les concepts de hiérarchie du système de fichiers et de navigation dans des scénarios réels et à gagner en confiance avec les commandes Linux essentielles.

## Quiz Question

Quelle commande est utilisée pour trouver le répertoire dans lequel vous vous trouvez actuellement ? (Veuillez répondre en anglais, en utilisant uniquement le nom de la commande en minuscules.)

## Quiz Answer

pwd
