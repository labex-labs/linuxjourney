---
lang: "fr"
title: "Le Sticky Bit"
meta_description: "Découvrez le sticky bit de Linux, son but dans les répertoires partagés comme /tmp, et comment le définir en utilisant chmod. Comprenez cette permission de fichier clé !"
meta_keywords: "sticky bit Linux, chmod +t, répertoire /tmp, permissions Linux, sécurité des fichiers, tutoriel Linux, Linux pour débutants"
---

## Lesson Content

Un dernier bit de permission spécial dont je veux parler est le sticky bit.

Ce bit de permission « colle un fichier/répertoire », ce qui signifie que seul le propriétaire ou l'utilisateur root peut supprimer ou modifier le fichier. C'est très utile pour les répertoires partagés. Jetez un œil à l'exemple ci-dessous :

```bash
$ ls -ld /tmp
drwxrwxrwx+t 6 root root 4096 Dec 15 11:45 /tmp
```

Vous verrez un bit de permission spécial à la fin ici **t**. Cela signifie que tout le monde peut ajouter des fichiers, écrire des fichiers et modifier des fichiers dans le répertoire `/tmp`, mais seul root peut supprimer le répertoire `/tmp`.

### Modify sticky bit

```bash
sudo chmod +t mydir

sudo chmod 1755 mydir
```

La représentation numérique du sticky bit est **1**.

## Exercise

Quels autres fichiers et répertoires, selon vous, ont un sticky bit activé ?

## Quiz Question

Quel symbole représente le sticky bit ?

## Quiz Answer

t
