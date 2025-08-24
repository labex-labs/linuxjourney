---
index: 10
lang: "fr"
title: "cp (Copier)"
meta_title: "cp (Copier) - Ligne de Commande"
meta_description: "Apprenez à utiliser la commande Linux cp pour copier des fichiers et des répertoires. Comprenez les options comme -r et les caractères génériques. Commencez votre parcours Linux dès aujourd'hui !"
meta_keywords: "commande cp, copier fichiers Linux, tutoriel Linux, Linux débutant, cp -r, caractères génériques Linux, guide Linux"
---

## Lesson Content

Commençons par faire des copies de ces fichiers. Tout comme copier-coller des fichiers dans d'autres systèmes d'exploitation, le shell nous offre un moyen encore plus simple de le faire.

```bash
cp mycoolfile /home/pete/Documents/cooldocs
```

`mycoolfile` est le fichier que vous voulez copier, et `/home/pete/Documents/cooldocs` est l'endroit où vous copiez le fichier.

Vous pouvez copier plusieurs fichiers et répertoires, ainsi qu'utiliser des caractères génériques (wildcards). Un caractère générique est un caractère qui peut être substitué à une sélection basée sur un motif, vous donnant plus de flexibilité dans les recherches. Vous pouvez utiliser des caractères génériques dans chaque commande pour plus de flexibilité.

- `*` le caractère générique des caractères génériques, il est utilisé pour représenter tous les caractères uniques ou n'importe quelle chaîne.
- `?` utilisé pour représenter un caractère
- `[]` utilisé pour représenter n'importe quel caractère entre crochets

```bash
cp *.jpg /home/pete/Pictures
```

Ceci copiera tous les fichiers avec l'extension `.jpg` de votre répertoire actuel vers le répertoire `Pictures`.

Une commande utile est d'utiliser le drapeau `-r`; cela copiera récursivement les fichiers et répertoires à l'intérieur d'un répertoire.

Essayez de faire un `cp` sur un répertoire qui contient quelques fichiers vers votre répertoire `Documents`. Ça n'a pas marché, n'est-ce pas ? Eh bien, c'est parce que vous devrez également copier les fichiers et répertoires à l'intérieur avec la commande `-r`.

```bash
cp -r Pumpkin/ /home/pete/Documents
```

Une chose à noter, si vous copiez un fichier vers un répertoire qui a le même nom de fichier, le fichier sera écrasé par ce que vous copiez. Ce n'est pas bon si vous avez un fichier que vous ne voulez pas écraser accidentellement. Vous pouvez utiliser le drapeau `-i` (interactif) pour vous demander confirmation avant d'écraser un fichier.

```bash
cp -i mycoolfile /home/pete/Pictures
```

## Exercise

Copiez quelques fichiers ; faites attention à ne rien écraser d'important.

Pour une pratique concrète de la commande `cp`, essayez ce laboratoire interactif :

- [Linux cp Command: File Copying](https://labex.io/fr/labs/linux-linux-cp-command-file-copying-209744)

## Quiz Question

Quel drapeau devez-vous spécifier pour copier un répertoire ?

## Quiz Answer

-r
