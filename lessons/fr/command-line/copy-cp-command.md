---
index: 10
lang: "fr"
title: "cp (Copier)"
meta_title: "cp (Copier) - Ligne de commande"
meta_description: "Apprenez à utiliser la commande Linux cp pour copier des fichiers et des répertoires. Comprenez les options comme -r et les caractères génériques. Commencez votre parcours Linux dès aujourd'hui !"
meta_keywords: "commande cp, copier fichiers Linux, tutoriel Linux, Linux débutant, cp -r, caractères génériques Linux, guide Linux"
---

## Lesson Content

Commençons à faire des copies de ces fichiers. Tout comme copier-coller des fichiers dans d'autres systèmes d'exploitation, le shell nous offre un moyen encore plus simple de le faire.

```bash
cp mycoolfile /home/pete/Documents/cooldocs
```

`mycoolfile` est le fichier que vous souhaitez copier, et `/home/pete/Documents/cooldocs` est l'emplacement où vous copiez le fichier.

Vous pouvez copier plusieurs fichiers et répertoires, ainsi qu'utiliser des caractères génériques (wildcards). Un caractère générique est un caractère qui peut être substitué à une sélection basée sur un modèle, vous offrant plus de flexibilité dans les recherches. Vous pouvez utiliser des caractères génériques dans chaque commande pour plus de flexibilité.

- `*` le caractère générique des caractères génériques, il est utilisé pour représenter tous les caractères uniques ou toute chaîne de caractères.
- `?` utilisé pour représenter un seul caractère
- `[]` utilisé pour représenter n'importe quel caractère à l'intérieur des crochets

```bash
cp *.jpg /home/pete/Pictures
```

Ceci copiera tous les fichiers avec l'extension `.jpg` de votre répertoire actuel vers le répertoire `Pictures`.

Une commande utile est d'utiliser l'option `-r`; cela copiera récursivement les fichiers et répertoires à l'intérieur d'un répertoire.

Essayez de faire un `cp` sur un répertoire qui contient quelques fichiers vers votre répertoire `Documents`. Cela n'a pas fonctionné, n'est-ce pas ? Eh bien, c'est parce que vous devrez également copier les fichiers et répertoires à l'intérieur avec la commande `-r`.

```bash
cp -r Pumpkin/ /home/pete/Documents
```

Une chose à noter, si vous copiez un fichier vers un répertoire qui a le même nom de fichier, le fichier sera écrasé par ce que vous copiez. Ce n'est pas bon si vous avez un fichier que vous ne voulez pas écraser accidentellement. Vous pouvez utiliser l'option `-i` (interactive) pour vous demander confirmation avant d'écraser un fichier.

```bash
cp -i mycoolfile /home/pete/Pictures
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la copie de fichiers et de répertoires sous Linux :

1. **[Commande Linux cp : Copie de fichiers](https://labex.io/fr/labs/linux-linux-cp-command-file-copying-209744)** - Entraînez-vous à l'utilisation de base, aux options avancées comme la copie récursive, la préservation des attributs et l'utilisation de caractères génériques pour copier efficacement des fichiers et des répertoires.
2. **[Organisation des fichiers et répertoires](https://labex.io/fr/labs/linux-organizing-files-and-directories-387877)** - Entraînez-vous aux compétences essentielles de gestion de fichiers Linux en utilisant les commandes `cp`, `mv` et `rm` pour organiser une structure de projet, déplacer des fichiers et nettoyer les répertoires inutiles.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la copie et la gestion de fichiers sous Linux.

## Quiz Question

Quelle option devez-vous spécifier pour copier un répertoire ?

## Quiz Answer

-r