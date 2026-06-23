---
index: 6
lang: "fr"
title: "file"
meta_title: "file - Ligne de commande"
meta_description: "Apprenez la commande Linux file avec des exemples pour identifier les fichiers texte, images, scripts, archives compressées, binaires et types MIME."
meta_keywords: "commande linux file, commande file, identifier type fichier linux, type mime linux, fichier texte, fichier binaire, fichier archive"
---

## Lesson Content

Dans la leçon précédente, nous avons appris à propos de `touch`. Revenons-y un instant. Avez-vous remarqué que le nom du fichier ne respectait pas les conventions de nommage standard, comme vous avez probablement vu avec d'autres systèmes d'exploitation tels que Windows ? Normalement, vous vous attendriez à ce qu'un fichier appelé `banana.jpeg` soit une image au format JPEG.

Sous Linux, les noms de fichiers ne sont pas obligés de représenter le contenu du fichier. Vous pouvez créer un fichier appelé `funny.gif` qui n'est en réalité pas un GIF.

Pour savoir quel type de fichier il s'agit, vous pouvez utiliser la commande `file`. Elle vous montrera une description du contenu du fichier.

```bash
$ file banana.jpg
banana.jpg: JPEG image data
```

### Pourquoi les extensions de fichiers ne suffisent pas

Les outils Linux n'ont généralement pas besoin d'une extension de fichier pour déterminer ce qu'est un fichier. Un script shell peut s'appeler `backup`, un fichier texte peut s'appeler `README`, et une image peut avoir une extension erronée. La commande `file` inspecte le contenu et les métadonnées du fichier pour faire une meilleure estimation.

```bash
$ file README
README: ASCII text
$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable
```

### Vérification de plusieurs fichiers

Vous pouvez vérifier plusieurs fichiers à la fois :

```bash
$ file notes.txt image.png archive.tar.gz
notes.txt: ASCII text
image.png: PNG image data
archive.tar.gz: gzip compressed data
```

Les caractères génériques fonctionnent aussi :

```bash
$ file *
```

### Afficher les types MIME

L'option `-i` affiche les informations au format MIME, ce qui est utile lors du travail avec des fichiers web ou des scripts.

```bash
$ file -i index.html
index.html: text/html; charset=us-ascii
```

### Options courantes de file

- `-i` : Affiche les informations de type MIME.
- `-b` : Mode bref, omet le nom du fichier dans la sortie.
- `-L` : Suit les liens symboliques.
- `-z` : Tente d'inspecter les fichiers compressés.

Par exemple :

```bash
$ file -b notes.txt
ASCII text
```

### Questions fréquentes

**La commande file se base-t-elle uniquement sur les extensions ?** Non. Elle inspecte principalement le contenu du fichier et les signatures connues.

**La commande file peut-elle se tromper ?** Oui. Elle fait une estimation éclairée, surtout pour les fichiers inhabituels ou endommagés.

**Pourquoi file affiche-t-elle "data" ?** Le fichier ne correspond pas à un type connu plus spécifique, ou il peut s'agir de données binaires sans signature reconnaissable.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'inspection du contenu et des propriétés des fichiers :

1. **[Commande Linux ls : Liste du contenu](https://labex.io/fr/labs/linux-linux-ls-command-content-listing-219205)** - Apprenez la commande Linux `ls` pour lister et analyser efficacement le contenu des fichiers et répertoires, ce qui précède ou suit souvent l'utilisation de la commande `file` pour comprendre ce qu'il y a dans vos répertoires.
2. **[Commande Linux cat : Concaténation de fichiers](https://labex.io/fr/labs/linux-linux-cat-command-file-concatenating-210986)** - Entraînez-vous à visualiser et manipuler des fichiers texte, une tâche courante après avoir identifié le type d'un fichier.
3. **[Commande Linux more : Défilement de fichiers](https://labex.io/fr/labs/linux-linux-more-command-file-scrolling-214299)** - Améliorez vos compétences en ligne de commande pour naviguer et explorer de grands fichiers texte, en vous appuyant sur la capacité à identifier les types de fichiers puis à en inspecter le contenu.

Ces laboratoires vous aideront à appliquer les concepts d'inspection et de visualisation du contenu des fichiers dans des scénarios réels et à gagner en confiance dans la gestion des fichiers sous Linux.

## Quiz Question

Quelle commande pouvez-vous utiliser pour connaître le type d'un fichier ?

## Quiz Answer

file
