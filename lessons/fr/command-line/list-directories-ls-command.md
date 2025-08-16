---
title: "ls (Lister les répertoires)"
description: "Apprenez à utiliser la commande 'ls' sous Linux pour lister le contenu des répertoires, afficher les fichiers cachés et comprendre les détails des fichiers. Améliorez vos compétences en ligne de commande Linux !"
keywords: "commande ls, lister les répertoires, tutoriel Linux, fichiers cachés, commandes Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

Maintenant que nous savons comment nous déplacer dans le système, comment savoir ce qui est à notre disposition ? Pour l'instant, c'est comme si nous nous déplacions dans le noir. Eh bien, nous pouvons utiliser la merveilleuse commande `ls` pour lister le contenu des répertoires. La commande `ls` listera par défaut les répertoires et les fichiers du répertoire courant ; cependant, vous pouvez spécifier le chemin dont vous voulez lister les répertoires.

```bash
ls
ls /home/pete
```

`ls` est un outil très utile ; il vous montre également des informations détaillées sur les fichiers et les répertoires que vous consultez.

Notez également que tous les fichiers d'un répertoire ne seront pas visibles. Les noms de fichiers qui commencent par `.` sont cachés. Vous pouvez cependant les afficher avec la commande `ls` et lui passer l'option `-a` (`a` pour all).

```bash
ls -a
```

Il existe également une autre option utile de `ls`, `-l` pour long. Cela affiche une liste détaillée des fichiers dans un format long. Cela vous montrera des informations détaillées, en commençant par la gauche : les permissions du fichier, le nombre de liens, le nom du propriétaire, le groupe du propriétaire, la taille du fichier, l'horodatage de la dernière modification, et le nom du fichier/répertoire.

```bash
ls -l
```

```plaintext
pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos
```

Les commandes ont ce qu'on appelle des options (ou arguments, ou drapeaux, peu importe comment vous voulez les appeler) pour ajouter plus de fonctionnalités. Voyez comment nous avons ajouté `-a` et `-l` ; eh bien, vous pouvez les ajouter tous les deux ensemble avec `-la`. L'ordre des options détermine l'ordre dans lequel elles sont traitées. La plupart du temps, cela n'a pas vraiment d'importance, vous pouvez donc aussi faire `ls -al` et cela fonctionnerait toujours.

```bash
ls -la
```

## Exercise

Exécutez `ls` avec différentes options et observez la sortie que vous recevez.

## Quiz Question

Quelle commande utiliseriez-vous pour voir les fichiers cachés ?

## Quiz Answer

ls -a
