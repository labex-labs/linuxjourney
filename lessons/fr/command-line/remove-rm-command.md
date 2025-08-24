---
index: 13
lang: "fr"
title: "rm (Supprimer)"
meta_title: "rm (Supprimer) - Ligne de commande"
meta_description: "Apprenez à utiliser la commande `rm` sous Linux pour supprimer des fichiers et des répertoires en toute sécurité. Comprenez les options comme -f, -i, -r et rmdir. Commencez votre parcours Linux !"
meta_keywords: "commande rm, supprimer fichiers Linux, supprimer répertoires, tutoriel Linux, Linux débutant, rmdir, guide Linux"
---

## Lesson Content

Maintenant, je pense que nous avons trop de fichiers ; supprimons-en quelques-uns. Pour supprimer des fichiers, vous pouvez utiliser la commande `rm`. La commande `rm` (remove) est utilisée pour supprimer des fichiers et des répertoires.

```bash
rm file1
```

Soyez prudent lorsque vous utilisez `rm` ; il n'y a pas de corbeille magique d'où vous pouvez récupérer les fichiers supprimés. Une fois qu'ils sont partis, ils sont partis pour de bon, alors soyez prudent.

Heureusement, il existe des mesures de sécurité, de sorte que l'utilisateur moyen ne peut pas simplement supprimer un tas de fichiers importants. Les fichiers protégés en écriture vous demanderont une confirmation avant de les supprimer. Si un répertoire est protégé en écriture, il ne sera pas non plus facilement supprimé.

Maintenant, si tout cela ne vous importe pas, vous pouvez absolument supprimer un tas de fichiers.

```bash
rm -f file1
```

L'option `-f` ou force indique à `rm` de supprimer tous les fichiers, qu'ils soient protégés en écriture ou non, sans demander à l'utilisateur (tant que vous avez les permissions appropriées).

```bash
rm -i file
```

L'ajout de l'indicateur `-i`, comme beaucoup d'autres commandes, vous demandera si vous voulez réellement supprimer les fichiers ou les répertoires.

```bash
rm -r directory
```

Vous ne pouvez pas simplement `rm` un répertoire par défaut ; vous devrez ajouter l'indicateur `-r` (récursif) pour supprimer tous les fichiers et tous les sous-répertoires qu'il pourrait contenir.

Vous pouvez supprimer un répertoire avec la commande `rmdir`.

```bash
rmdir directory
```

## Exercise

Pour une pratique concrète de la commande `rm`, essayez ce laboratoire interactif :

- [Linux rm Command: File Removing](https://labex.io/fr/labs/linux-linux-rm-command-file-removing-209741)

## Quiz Question

Comment supprimez-vous un fichier nommé `myfile` ?

## Quiz Answer

rm myfile
