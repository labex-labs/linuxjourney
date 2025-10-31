---
index: 2
lang: "fr"
title: "rsync"
meta_title: "rsync - Partage Réseau"
meta_description: "Découvrez comment utiliser la puissante commande rsync sous Linux pour une synchronisation de fichiers efficace, le transfert de données à distance et des sauvegardes fiables. Ce guide couvre les commandes et options clés de rsync."
meta_keywords: "rsync, rsync linux, synchronisation fichiers, sauvegarde données, synchronisation distante, commande rsync, transfert fichiers linux, tutoriel rsync"
---

## Lesson Content

### Qu'est-ce que rsync ?

Un autre outil essentiel pour copier des données entre différents hôtes est `rsync`, qui signifie synchronisation à distance (remote synchronization). Bien que similaire à `scp`, `rsync` présente une différence clé qui le rend incroyablement efficace. Il utilise un algorithme de transfert delta qui vérifie intelligemment la destination pour les données existantes et ne transfère que les parties des fichiers qui ont changé.

Par exemple, si un transfert de fichier volumineux est interrompu, `rsync` peut reprendre la copie, ne transférant que les parties restantes du fichier au lieu de recommencer à zéro. Cela en fait un choix robuste pour les connexions réseau instables.

### Caractéristiques clés de rsync

L'efficacité de `rsync` provient de ses optimisations intelligentes. Il vérifie l'intégrité des fichiers à l'aide de sommes de contrôle pour s'assurer que les données copiées ne sont pas corrompues pendant le transfert. Ces fonctionnalités offrent une flexibilité considérable, faisant de `rsync` un outil idéal pour :

- La synchronisation de répertoires (à distance et localement)
- La création de sauvegardes de données incrémentielles
- La gestion efficace des transferts de données volumineux

### Options courantes de rsync

Vous pouvez modifier le comportement de la commande `rsync` avec plusieurs options. Parmi les plus couramment utilisées, on trouve :

- `-v` : Sortie verbeuse, affichant les fichiers en cours de transfert.
- `-r` : Récursif, nécessaire pour copier des répertoires entiers.
- `-h` : Sortie lisible par l'homme, affichant les nombres dans un format plus compréhensible (par exemple, Ko, Mo).
- `-z` : Compresse les données des fichiers pendant le transfert, ce qui est excellent pour les connexions lentes.
- `-a` : Mode archive, un raccourci pratique qui combine plusieurs options (`-rlptgoD`) pour préserver les permissions, la propriété et les horodatages.

### Exemples d'utilisation de rsync

#### Synchroniser des fichiers sur le même hôte

Vous pouvez utiliser `rsync` pour synchroniser deux répertoires sur votre machine locale. Ceci est utile pour créer des sauvegardes locales.

```bash
rsync -avh /mon/repertoire/local/un/ /mon/repertoire/local/deux/
```

#### Synchroniser des fichiers d'un hôte distant vers un hôte local

Pour récupérer des fichiers d'un serveur distant vers votre machine locale, spécifiez d'abord la source distante.

```bash
rsync -avh utilisateur@hote_distant.com:/repertoire/distant/ /repertoire/local/
```

#### Synchroniser des fichiers d'un hôte local vers un hôte distant

Pour envoyer des fichiers de votre machine locale vers un serveur distant, spécifiez d'abord la source locale.

```bash
rsync -avh /repertoire/local/ utilisateur@hote_distant.com:/repertoire/distant/
```

## Exercise

Bien qu'il n'y ait pas de laboratoires spécifiques pour ce sujet, nous vous recommandons d'explorer le [Parcours d'apprentissage Linux](https://labex.io/fr/learn/linux) complet pour pratiquer les compétences et concepts Linux associés.

## Quiz Question

What command, known for its delta-transfer algorithm, is particularly useful for creating efficient data backups? Please answer in English, paying attention to case sensitivity.

## Quiz Answer

rsync
