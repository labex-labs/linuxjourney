---
index: 3
lang: "fr"
title: "tar et gzip"
meta_title: "tar et gzip - Paquets"
meta_description: "Un guide complet sur l'utilisation de tar et gzip sous Linux. Apprenez la compression tar, comment créer et extraire des archives, et la différence entre gzip et tar. Maîtrisez les commandes pour compresser les fichiers tar gz et gérer efficacement vos paquets logiciels."
meta_keywords: "tar et gzip, compression tar, gzip tar, compresser tar gz, gzip et tar, archivage Linux, compression de fichiers, commande tar, commande gzip, tutoriel Linux"
---

## Lesson Content

Avant de plonger dans les gestionnaires de paquets, il est essentiel de comprendre l'archivage et la compression de fichiers. Lorsque vous téléchargez des logiciels en ligne, vous les trouverez souvent empaquetés dans des formats archivés et compressés. Cette leçon se concentre sur deux utilitaires fondamentaux à cette fin : `tar` et `gzip`.

### Comprendre l'archivage par rapport à la compression

Il est important de distinguer l'archivage de la compression. L'**archivage** est le processus de combinaison de plusieurs fichiers et répertoires en un seul fichier, appelé archive. Cela facilite la gestion et le transfert d'un groupe de fichiers. La **compression**, quant à elle, est le processus de réduction de la taille d'un fichier pour économiser de l'espace disque et accélérer les transferts. L'utilitaire `tar` est utilisé pour l'archivage, tandis que `gzip` est utilisé pour la compression. Souvent, vous verrez `gzip et tar` utilisés ensemble.

### Compression de fichiers uniques avec gzip

Le programme `gzip` est utilisé pour compresser des fichiers individuels sous Linux. Lorsque vous compressez un fichier avec `gzip`, il est remplacé par un fichier portant l'extension `.gz`.

Pour compresser un fichier :

```bash
gzip monfichiercool
```

Ceci créera `monfichiercool.gz` et supprimera l'original. Pour décompresser le fichier, vous pouvez utiliser `gunzip` :

```bash
gunzip monfichiercool.gz
```

### Création d'archives avec tar

Bien que `gzip` soit excellent pour la compression, il ne peut pas regrouper plusieurs fichiers dans une seule archive. Pour cela, nous utilisons l'utilitaire `tar` (Tape Archive). Un fichier créé avec `tar` est souvent appelé "tarball" et porte l'extension `.tar`.

Pour créer une nouvelle archive contenant plusieurs fichiers :

```bash
tar cvf monarchive.tar fichier1 fichier2 repertoire1
```

Décortiquons les options :

- `c` : **c**réer une nouvelle archive.
- `v` : mode **v**erbose, qui liste les fichiers au fur et à mesure de leur traitement.
- `f` : **f**ichier, qui spécifie que l'argument suivant est le nom du fichier archive.

### La puissance combinée de tar et gzip

La véritable puissance réside dans l'utilisation conjointe de `tar et gzip`. Vous pouvez d'abord créer une archive `.tar`, puis la compresser avec `gzip`, ce qui donne un fichier `.tar.gz`. Cependant, `tar` offre un moyen pratique de gérer la **compression tar** en une seule étape à l'aide de l'option `z`. Ce processus est parfois appelé création d'une archive **gzip tar**.

Pour créer une archive compressée, ce qui est une façon courante de **compresser tar gz** :

```bash
tar czvf monarchive.tar.gz fichier1 fichier2 repertoire1
```

Ici, l'option `z` indique à `tar` d'utiliser `gzip` pour la compression.

### Extraction des archives tar et gzip

Pour extraire des fichiers d'une archive, vous utilisez l'option `x`.

Pour extraire une archive `.tar` simple :

```bash
tar xvf monarchive.tar
```

Pour décompresser et extraire une archive `.tar.gz` en une seule commande, ajoutez simplement à nouveau l'option `z` :

```bash
tar xzvf monarchive.tar.gz
```

Récapitulons les options d'extraction :

- `x` : **e**xtraire les fichiers de l'archive.
- `z` : Décompresser l'archive en utilisant **g**u**z**ip.
- `v` : mode **v**erbose, listant les fichiers au fur et à mesure de leur extraction.
- `f` : **f**ichier, spécifiant le fichier archive à extraire.

Aide-mémoire utile pour ceci : **E**xtraire **Z**e **V**raiment **F**acilement !

`tar` est une commande si essentielle mais souvent oubliée. xkcd pertinent : `https://xkcd.com/1168`

### Autres utilitaires

Bien que `tar` et `gzip` soient extrêmement courants, vous rencontrerez d'autres formats d'archivage et de compression lors de votre parcours sous Linux. Ceux-ci incluent `bzip2` (qui crée des fichiers `.bz2` et utilise l'indicateur `j` dans `tar`), `xz` (créant des fichiers `.xz` avec l'indicateur `J`), et les utilitaires familiers `zip`/`unzip`. Chacun a son propre ensemble de commandes et ses propres ratios de compression, mais les concepts sous-jacents restent les mêmes.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'archivage et de la compression de fichiers :

1. **[Packaging et compression de fichiers](https://labex.io/fr/labs/linux-file-packaging-and-compression-385413)** - Apprenez les techniques essentielles de compression et d'empaquetage de fichiers Linux à l'aide d'outils tels que tar, gzip et zip.
2. **[Créer et restaurer une sauvegarde avec tar sous Linux](https://labex.io/fr/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843)** - Acquérir une expérience pratique de la création et de la restauration de sauvegardes de systèmes de fichiers à l'aide de la commande tar.
3. **[Sauvegarder le journal système](https://labex.io/fr/labs/linux-backup-system-log-17989)** - Apprenez la compétence essentielle de sauvegarde des fichiers journaux système à l'aide de la commande tar et du formatage de date.

Ces laboratoires vous aideront à appliquer les concepts d'archivage et de compression dans des scénarios réels et à renforcer votre confiance dans la gestion des fichiers sous Linux.

## Quiz Question

Quel drapeau tar est utilisé pour créer des archives ? Veuillez répondre avec une seule lettre minuscule anglaise.

## Quiz Answer

c
