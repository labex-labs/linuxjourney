---
title: "rm (Supprimer)"
description: "Apprenez à utiliser la commande `rm` sous Linux pour supprimer en toute sécurité des fichiers et des répertoires. Comprenez les options comme -f, -i, -r et rmdir. Commencez votre parcours Linux !"
keywords: "commande rm, supprimer des fichiers Linux, supprimer des répertoires, tutoriel Linux, Linux pour débutants, rmdir, guide Linux"
---

## Lesson Content

Maintenant, je pense que nous avons trop de fichiers ; supprimons-en quelques-uns. Pour supprimer des fichiers, vous pouvez utiliser la commande `rm`. La commande `rm` (remove) est utilisée pour supprimer des fichiers et des répertoires.

```bash
rm file1
```

Soyez prudent lorsque vous utilisez `rm` ; il n'y a pas de corbeille magique à partir de laquelle vous pouvez récupérer les fichiers supprimés. Une fois qu'ils sont partis, ils sont partis pour de bon, alors soyez prudent.

Heureusement, il existe des mesures de sécurité, de sorte que l'utilisateur moyen ne peut pas simplement supprimer un tas de fichiers importants. Les fichiers protégés en écriture vous demanderont une confirmation avant de les supprimer. Si un répertoire est protégé en écriture, il ne sera pas non plus facilement supprimé.

Maintenant, si tout cela ne vous intéresse pas, vous pouvez absolument supprimer un tas de fichiers.

```bash
rm -f file1
```

L'option `-f` ou force indique à `rm` de supprimer tous les fichiers, qu'ils soient protégés en écriture ou non, sans demander à l'utilisateur (tant que vous avez les permissions appropriées).

```bash
rm -i file
```

L'ajout du drapeau `-i`, comme pour de nombreuses autres commandes, vous demandera si vous souhaitez réellement supprimer les fichiers ou les répertoires.

```bash
rm -r directory
```

Vous ne pouvez pas simplement `rm` un répertoire par défaut ; vous devrez ajouter le drapeau `-r` (récursif) pour supprimer tous les fichiers et tous les sous-répertoires qu'il pourrait contenir.

Vous pouvez supprimer un répertoire avec la commande `rmdir`.

```bash
rmdir directory
```

## Exercise

1. Create a file called `-file` (don't forget the dash!).
2. Remove that file.

## Quiz Question

Comment supprimez-vous un fichier nommé `myfile` ?

## Quiz Answer

To remove a file named `myfile`, you would use the command: `rm myfile`

If the file name starts with a hyphen (e.g., `-file`), you need to tell `rm` that the hyphen is part of the filename and not an option. You can do this in a few ways:

1. **Using `--` to signify end of options:**
   `rm -- -file`

2. **Using a relative or absolute path:**
   `rm ./-file`
   `rm /path/to/-file`

3. **Using an inode number (more advanced and less common for simple deletion):**
   First, find the inode number: `ls -i`
   Then, use `find . -inum <inode_number> -delete`

For the specific exercise of removing a file called `-file`, the most common and recommended methods are `rm -- -file` or `rm ./-file`.
