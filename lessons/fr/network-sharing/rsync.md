---
index: 2
lang: "fr"
title: "rsync"
meta_title: "rsync - Partage réseau"
meta_description: "Apprenez rsync pour une synchronisation et des sauvegardes de fichiers Linux efficaces. Comprenez le transfert de données à distance et local avec les commandes et options rsync. Améliorez vos compétences Linux !"
meta_keywords: "rsync, transfert de fichiers Linux, sauvegarde de données, synchronisation de fichiers, tutoriel Linux, commandes rsync, débutant, guide"
---

## Lesson Content

Un autre outil utilisé pour copier des données entre différents hôtes est rsync (abréviation de remote synchronization). Rsync est très similaire à scp, mais il présente une différence majeure. Rsync utilise un algorithme spécial qui vérifie à l'avance s'il y a déjà des données vers lesquelles vous copiez et ne copiera que les différences. Par exemple, supposons que vous copiez un fichier et que votre réseau soit interrompu ; par conséquent, votre copie s'est arrêtée à mi-chemin. Au lieu de tout recopier depuis le début, rsync ne copiera que les parties qui n'ont pas été copiées.

Il vérifie également l'intégrité d'un fichier que vous copiez avec des sommes de contrôle (checksums). Ces petites optimisations permettent une plus grande flexibilité de transfert de fichiers et rendent rsync idéal pour la synchronisation de répertoires à distance et localement, les sauvegardes de données, les transferts de grandes quantités de données, et plus encore.

Quelques options rsync couramment utilisées :

- v - sortie verbeuse
- r - récursif dans les répertoires
- h - sortie lisible par l'homme
- z - compressé pour un transfert plus facile, idéal pour les connexions lentes

### Copier/synchroniser des fichiers sur le même hôte

```bash
rsync -zvr /my/local/directory/one /my/local/directory/two
```

### Copier/synchroniser des fichiers vers l'hôte local depuis un hôte distant

```bash
rsync /local/directory username@remotehost.com:/remote/directory
```

### Copier/synchroniser des fichiers vers un hôte distant depuis un hôte local

```bash
rsync username@remotehost.com:/remote/directory /local/directory
```

## Exercise

Bien qu'il n'y ait pas de laboratoires spécifiques pour ce sujet, nous vous recommandons d'explorer le [Parcours d'apprentissage Linux](https://labex.io/fr/learn/linux) complet pour pratiquer les compétences et concepts Linux associés.

## Quiz Question

Quelle commande serait utile pour les sauvegardes de données ?

## Quiz Answer

rsync
