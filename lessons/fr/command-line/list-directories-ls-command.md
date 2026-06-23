---
index: 4
lang: "fr"
title: "ls (Lister les Répertoires)"
meta_title: "ls (Lister les Répertoires) - Ligne de Commande"
meta_description: "Apprenez la commande Linux ls avec des exemples pour lister les fichiers, les fichiers cachés, le format long, les tailles lisibles, le tri et la combinaison d'options."
meta_keywords: "commande ls, linux ls, lister fichiers linux, lister répertoires, ls -a, ls -l, ls -lh, ls -r, fichiers cachés"
---

## Lesson Content

Maintenant que nous savons comment naviguer dans le système de fichiers, comment savoir ce qui est disponible ? La commande `ls` liste les fichiers et répertoires pour que vous puissiez inspecter votre emplacement actuel ou un autre chemin.

### Utilisation de base de la commande ls

Par défaut, la commande `ls` liste les répertoires et fichiers dans votre répertoire courant. Cependant, vous pouvez aussi spécifier un chemin pour lister le contenu d’un autre répertoire.

```bash
$ ls
$ ls /home/pete
```

Vous pouvez aussi lister un fichier spécifique :

```bash
$ ls /etc/hosts
/etc/hosts
```

### Voir les fichiers cachés

Tous les fichiers d’un répertoire ne sont pas visibles par défaut. Sous Linux, les noms de fichiers qui commencent par un point (`.`) sont cachés. Vous pouvez les voir avec l’option `-a`, qui signifie all (tout).

```bash
$ ls -a
.  ..  .bashrc  Documents  Pictures
```

### Obtenir des informations détaillées

Une autre option essentielle de `ls` est `-l` pour le format long. Elle affiche les permissions, le nombre de liens, le propriétaire, le groupe, la taille, la date de modification et le nom.

```bash
$ ls -l
```

Voici un exemple de sortie :

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

Pour des tailles plus faciles à lire, ajoutez `-h` pour un affichage lisible par l’humain :

```bash
$ ls -lh
```

### Trier dans l’ordre inverse

Parfois, vous pouvez vouloir changer l’ordre de tri. L’option `-r` liste les fichiers et répertoires dans l’ordre inverse.

```bash
$ ls -r
```

Vous pouvez trier par date de modification avec `-t`, puis inverser avec `-r` :

```bash
$ ls -lt
$ ls -ltr
```

### Combinaison des options de commande

Les commandes ont des options, aussi appelées flags, pour ajouter des fonctionnalités. Comme nous l’avons vu avec `-a` et `-l`, vous pouvez les combiner dans une seule commande comme `ls -la`. L’ordre des options importe rarement, donc `ls -al` fonctionne de la même manière.

```bash
$ ls -la
```

Des combinaisons utiles incluent :

```bash
$ ls -lh
$ ls -la
$ ls -ltr
```

### Options courantes de ls

- `-a` : Affiche tous les fichiers, y compris les fichiers cachés.
- `-l` : Utilise le format long.
- `-h` : Affiche les tailles lisibles avec `-l`.
- `-r` : Inverse l’ordre de tri.
- `-t` : Trie par date de modification.
- `-S` : Trie par taille de fichier.
- `-d` : Liste le répertoire lui-même au lieu de son contenu.

### Questions fréquentes

**Pourquoi certains noms de fichiers commencent-ils par un point ?** Les fichiers pointés sont cachés par défaut et contiennent souvent des configurations, comme `.bashrc`.

**Comment lister uniquement un répertoire lui-même ?** Utilisez `ls -d directory/`.

**Comment voir les fichiers les plus récents en dernier ?** Utilisez `ls -ltr`.

**Pourquoi ls affiche-t-il des couleurs ?** Beaucoup de systèmes configurent `ls` pour colorer les types de fichiers via un alias ou une variable d’environnement.

## Exercise

La pratique rend parfait ! Voici un laboratoire pratique pour renforcer votre compréhension de la commande `ls` :

- **[Commande Linux ls : Liste de contenu](https://labex.io/fr/labs/linux-linux-ls-command-content-listing-219205)** - Entraînez-vous à utiliser la commande `ls` pour lister et analyser efficacement le contenu des fichiers et répertoires. Vous apprendrez diverses options pour des listes détaillées, l’affichage des fichiers cachés, les tailles lisibles et les techniques de tri pour améliorer vos compétences en ligne de commande.

Ce laboratoire vous aidera à appliquer les concepts dans un scénario réel et à gagner en confiance avec la liste des répertoires sous Linux.

## Quiz Question

Quelle commande utiliseriez-vous pour voir les fichiers cachés ? Veuillez répondre en anglais, en faisant attention à la casse.

## Quiz Answer

ls -a
