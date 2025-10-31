---
index: 10
lang: "fr"
title: "cp (Copier)"
meta_title: "cp (Copier) - Ligne de Commande"
meta_description: "Maîtrisez la commande Linux cp pour copier des fichiers et des répertoires. Ce guide couvre les options essentielles comme la copie récursive (-r), la préservation des attributs avec le drapeau cp -p, et la force d'écrasement avec le drapeau cp -f. Apprenez comment cp -p sous Linux aide à maintenir les métadonnées des fichiers."
meta_keywords: "commande cp, copier fichiers linux, linux cp -p, drapeau cp -p, cp -p sous linux, drapeau cp -f, copie récursive, cp -r, jokers linux, ligne de commande linux"
---

## Lesson Content

La commande `cp` est l'outil standard pour copier des fichiers et des répertoires sous Linux. Sa syntaxe de base est `cp [SOURCE] [DESTINATION]`.

### Copie de Fichiers de Base

Pour copier un fichier, vous spécifiez le fichier source et le répertoire ou le chemin de destination.

```bash
cp monfichiercool /home/pete/Documents/docs_cools
```

Dans cet exemple, `monfichiercool` est le fichier source, et `/home/pete/Documents/docs_cools` est le répertoire de destination. Vous pouvez également copier un fichier et lui donner un nouveau nom à la destination.

```bash
cp monfichiercool /home/pete/Documents/monfichiercool_sauvegarde
```

### Utilisation des Jokers pour la Copie en Masse

Les jokers (wildcards) sont des caractères spéciaux qui vous aident à sélectionner plusieurs fichiers en fonction de modèles, offrant une grande flexibilité.

- `*`: Correspond à toute séquence de caractères.
- `?`: Correspond à n'importe quel caractère unique.
- `[]`: Correspond à l'un des caractères contenus dans les crochets.

Par exemple, pour copier toutes les images JPEG de votre emplacement actuel vers le répertoire `Images` :

```bash
cp *.jpg /home/pete/Images
```

### Copie Récursive de Répertoires

Si vous essayez de copier un répertoire en utilisant `cp` sans aucune option, vous recevrez une erreur. Pour copier un répertoire et tout son contenu, y compris les sous-répertoires, vous devez utiliser l'option `-r` (récursif).

```bash
cp -r Citrouille/ /home/pete/Documents
```

Cette commande copie le répertoire `Citrouille` et tout ce qu'il contient dans votre répertoire `Documents`.

### Gestion des Écrasements de Fichiers

Par défaut, `cp` écrasera un fichier à la destination s'il porte le même nom. Pour éviter toute perte de données accidentelle, utilisez l'option `-i` (interactif), qui demande une confirmation avant d'écraser.

```bash
cp -i monfichiercool /home/pete/Images
```

Inversement, si vous souhaitez forcer un écrasement sans aucune invite, vous pouvez utiliser l'option `cp -f`. Ceci est utile dans les scripts où l'interaction utilisateur n'est pas possible.

```bash
cp -f monfichiercool /home/pete/Images
```

### Préservation des Attributs de Fichier avec cp -p

Lorsque vous copiez un fichier, ses métadonnées, telles que l'heure de modification et la propriété, sont généralement mises à jour. Pour préserver ces attributs d'origine, l'option `cp -p` est essentielle. L'utilisation de `cp -p sous linux` garantit que la copie est une réplique exacte, non seulement en contenu mais aussi en métadonnées.

L'option `cp -p flag` est particulièrement utile pour les sauvegardes ou lors de la migration de fichiers où la préservation des horodatages est critique.

```bash
cp -p monfichiercool /home/pete/sauvegardes/
```

Cette commande montre comment utiliser `linux cp -p` pour copier `monfichiercool` tout en préservant son mode, sa propriété et ses horodatages.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la copie de fichiers et de répertoires sous Linux :

1. **[Commande cp Linux : Copie de Fichiers](https://labex.io/fr/labs/linux-linux-cp-command-file-copying-209744)** - Entraînez-vous à l'utilisation de base, aux options avancées comme la copie récursive, la préservation des attributs et l'utilisation des jokers pour copier efficacement des fichiers et des répertoires.
2. **[Organisation des Fichiers et Répertoires](https://labex.io/fr/labs/linux-organizing-files-and-directories-387877)** - Entraînez-vous aux compétences essentielles de gestion de fichiers Linux en utilisant les commandes `cp`, `mv` et `rm` pour organiser une structure de projet, déplacer des fichiers et nettoyer les répertoires inutiles.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance avec la copie et la gestion des fichiers sous Linux.

## Quiz Question

Quel indicateur devez-vous spécifier pour copier un répertoire ?

## Quiz Answer

-r
