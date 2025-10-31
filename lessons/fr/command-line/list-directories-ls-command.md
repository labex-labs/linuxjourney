---
index: 4
lang: "fr"
title: "ls (Lister les répertoires)"
meta_title: "ls (Lister les répertoires) - Ligne de commande"
meta_description: "Apprenez à utiliser la commande puissante ls sous Linux. Ce guide couvre comment lister le contenu des répertoires, afficher les fichiers cachés avec ls -a, obtenir des listes détaillées avec ls -l, et utiliser la commande ls -r pour un tri inversé. Une leçon parfaite pour maîtriser la commande ls."
meta_keywords: "commande ls, lister répertoires, cmd ls, commande ls -r, commande ls, linux ls -r, commande linux ls, fichiers cachés, commandes Linux, Linux débutant"
---

## Lesson Content

Maintenant que nous savons comment naviguer dans le système de fichiers, comment déterminer ce qui est à notre disposition ? Sans le bon outil, c'est comme se déplacer dans le noir. Heureusement, la merveilleuse `commande linux ls` est là pour aider en listant le contenu des répertoires.

### Utilisation de base de la commande ls

Par défaut, la `commande ls` listera les répertoires et les fichiers de votre répertoire actuel. Cependant, vous pouvez également spécifier un chemin pour lister le contenu d'un autre répertoire.

```bash
ls
ls /home/pete
```

La `commande ls` est un outil polyvalent qui peut vous montrer des informations détaillées sur les fichiers et les répertoires que vous consultez.

### Afficher les fichiers cachés

Notez que tous les fichiers d'un répertoire ne sont pas visibles par défaut. Sous Linux, les noms de fichiers qui commencent par un point (`.`) sont cachés. Vous pouvez les voir en utilisant la `cmd ls` avec le drapeau `-a`, qui signifie "all" (tout).

```bash
ls -a
```

### Obtenir des informations détaillées

Un autre drapeau essentiel de `ls` est `-l` pour "long" (long). Cette option fournit une liste détaillée des fichiers dans un format long. Cela vous montrera des informations détaillées, en commençant par la gauche : les permissions du fichier, le nombre de liens, le nom du propriétaire, le groupe propriétaire, la taille du fichier, l'horodatage de la dernière modification, et le nom du fichier ou du répertoire.

```bash
ls -l
```

Voici un exemple du résultat :

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

### Trier en ordre inverse

Parfois, vous voudrez peut-être changer l'ordre de tri. La `commande ls -r` liste les fichiers et les répertoires par ordre alphabétique inverse. L'option `linux ls -r` est particulièrement utile lorsque vous voulez voir les derniers éléments d'une longue liste en premier.

```bash
ls -r
```

### Combinaison des drapeaux de commande

Les commandes ont des drapeaux (aussi appelés arguments ou options) pour ajouter plus de fonctionnalités. Comme nous l'avons vu avec `-a` et `-l`, vous pouvez les combiner en une seule commande comme `ls -la`. L'ordre des drapeaux n'a généralement pas d'importance, donc `ls -al` fonctionnerait de manière identique. Vous pouvez également ajouter le drapeau inverse : `ls -lar`.

```bash
ls -la
```

## Exercise

La pratique rend parfait ! Voici un laboratoire pratique pour renforcer votre compréhension de la commande `ls` :

- **[Commande ls Linux : Listage de contenu](https://labex.io/fr/labs/linux-linux-ls-command-content-listing-219205)** - Entraînez-vous à utiliser la commande `ls` pour lister et analyser efficacement le contenu des fichiers et des répertoires. Vous apprendrez diverses options pour les listes détaillées, l'affichage des fichiers cachés, les tailles lisibles par l'homme et les techniques de tri pour améliorer vos compétences en ligne de commande.

Ce laboratoire vous aidera à appliquer les concepts dans un scénario réel et à gagner en confiance avec le listage de répertoires sous Linux.

## Quiz Question

Quelle commande utiliseriez-vous pour voir les fichiers cachés ? Veuillez répondre en anglais, en faisant attention à la sensibilité à la casse.

## Quiz Answer

ls -a
