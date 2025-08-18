---
index: 2
lang: "fr"
title: "rsync"
meta_title: "rsync - Partage Réseau"
meta_description: "Apprenez rsync pour une synchronisation et des sauvegardes de fichiers Linux efficaces. Comprenez le transfert de données à distance et local avec les commandes et options rsync. Améliorez vos compétences Linux !"
meta_keywords: "rsync, transfert de fichiers Linux, sauvegarde de données, synchronisation de fichiers, tutoriel Linux, commandes rsync, débutant, guide"
---

## Lesson Content

Un autre outil utilisé pour copier des données depuis différents hôtes est rsync (abréviation de synchronisation à distance). Rsync est très similaire à scp, mais il présente une différence majeure. Rsync utilise un algorithme spécial qui vérifie à l'avance s'il y a déjà des données vers lesquelles vous copiez et ne copiera que les différences. Par exemple, supposons que vous copiez un fichier et que votre réseau soit interrompu ; par conséquent, votre copie s'est arrêtée à mi-chemin. Au lieu de tout recopier depuis le début, rsync ne copiera que les parties qui n'ont pas été copiées.

Il vérifie également l'intégrité d'un fichier que vous copiez avec des sommes de contrôle (checksums). Ces petites optimisations permettent une plus grande flexibilité de transfert de fichiers et rendent rsync idéal pour la synchronisation de répertoires à distance et localement, les sauvegardes de données, les transferts de grandes quantités de données, et plus encore.

Quelques options rsync couramment utilisées :

- v - verbose output
- r - recursive into directories
- h - human-readable output
- z - compressed for easier transfer, great for slow connections

### Copy/sync files on the same host

```bash
rsync -zvr /my/local/directory/one /my/local/directory/two
```

### Copy/sync files to local host from a remote host

```bash
rsync /local/directory username@remotehost.com:/remote/directory
```

### Copy/sync files to a remote host from a local host

```bash
rsync username@remotehost.com:/remote/directory /local/directory
```

## Exercise

Utilisez rsync pour synchroniser un répertoire vers un autre répertoire. Assurez-vous de ne pas écraser un répertoire important !

## Quiz Question

Quelle commande serait utile pour les sauvegardes de données ?

## Quiz Answer

rsync
