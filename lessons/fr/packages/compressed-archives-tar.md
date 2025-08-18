---
index: 3
lang: "fr"
title: "tar et gzip"
meta_title: "tar et gzip - Packages"
meta_description: "Apprenez à utiliser tar et gzip pour l'archivage et la compression de fichiers sous Linux. Comprenez les commandes pour créer, extraire et compresser des fichiers. Démarrez avec ce guide pour débutants !"
meta_keywords: "tar, gzip, archivage Linux, compression de fichiers, commande tar, commande gzip, tutoriel Linux, Linux pour débutants"
---

## Lesson Content

Avant d'aborder l'installation de paquets et les différents gestionnaires, nous devons discuter de l'archivage et de la compression de fichiers, car vous les rencontrerez très probablement lorsque vous chercherez des logiciels sur internet.

Vous savez probablement déjà ce qu'est une archive de fichiers ; vous avez très probablement rencontré des types de fichiers tels que .rar et .zip. Ce sont des archives de fichiers ; elles contiennent de nombreux fichiers à l'intérieur, mais elles se présentent sous la forme d'un seul fichier très net, connu sous le nom d'archive.

### Compressing files with gzip

gzip est un programme utilisé pour compresser des fichiers sous Linux ; ils se terminent par une extension .gz.

Pour compresser un fichier :

```bash
gzip mycoolfile
```

Pour décompresser le fichier :

```bash
gunzip mycoolfile.gz
```

### Creating archives with tar

Malheureusement, gzip ne peut pas ajouter plusieurs fichiers dans une seule archive pour nous. Heureusement, nous avons le programme tar qui le fait. Lorsque vous créez une archive à l'aide de tar, elle aura une extension .tar.

```bash
tar cvf mytarfile.tar mycoolfile1 mycoolfile2
```

- `c` - create
- `v` - indique au programme d'être verbeux et de nous laisser voir ce qu'il fait
- `f` - le nom du fichier tar doit venir après cette option ; si vous créez un fichier tar, vous devrez trouver un nom

### Unpacking archives with tar

Pour extraire le contenu d'un fichier tar, utilisez :

```bash
tar xvf mytarfile.tar
```

- `x` - extract
- `v` - indique au programme d'être verbeux et de nous laisser voir ce qu'il fait
- `f` - le fichier que vous voulez extraire

### Compressing/uncompressing archives with tar and gzip

Souvent, vous verrez un fichier tar qui a été compressé, tel que : `mycompressedarchive.tar.gz`. Tout ce que vous avez à faire est de travailler de l'extérieur vers l'intérieur, donc d'abord supprimer la compression avec `gunzip`, puis vous pouvez décompresser le fichier tar. Ou vous pouvez alternativement utiliser l'option **z** avec tar, qui lui indique simplement d'utiliser l'utilitaire gzip ou gunzip.

Créer un fichier tar compressé :

```bash
tar czf myfile.tar.gz
```

Décompresser et déballer :

```bash
tar xzf file.tar
```

Si vous avez besoin d'aide pour vous en souvenir : e**X**traire tous les **Z**ee **F**ichiers !

tar est l'une de ces commandes si importantes et pourtant on ne s'en souvient jamais vraiment. xkcd pertinent : `https://xkcd.com/1168`

### Other Utilities

Tout au long de votre parcours avec Linux, vous rencontrerez d'autres types d'archives et de compression tels que : bzip2, compress, zip, unzip, etc. Ils sont un peu moins courants, mais gardez à l'esprit que différents utilitaires nécessiteront différentes commandes.

## Exercise

Familiarisez-vous avec la documentation tar et examinez les autres options disponibles dans la page de manuel.

## Quiz Question

Quel drapeau tar est utilisé pour créer des archives ?

## Quiz Answer

c
