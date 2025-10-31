---
index: 9
lang: "fr"
title: "Utilisation du Disque"
meta_title: "Utilisation du Disque - Le Système de Fichiers"
meta_description: "Apprenez à vérifier l'utilisation du disque et l'espace libre sous Linux avec les commandes df et du. Ce guide explique comment analyser l'espace disque, y compris l'utilisation des inodes avec df -i linux, et trouver quels fichiers occupent de l'espace."
meta_keywords: "commande df, commande du, utilisation disque Linux, vérifier espace libre, df -i linux, gestion disque, tutoriel Linux, utilisation disque, utilisation système de fichiers"
---

## Lesson Content

La gestion de l'espace disque est une tâche fondamentale pour tout utilisateur ou administrateur Linux. Deux commandes essentielles à cet effet sont `df` et `du`. Explorons comment les utiliser pour surveiller efficacement l'utilisation de votre disque.

### Vérification de l'espace du système de fichiers avec df

La commande `df` (disk free) signale la quantité d'espace disque utilisée et disponible sur vos systèmes de fichiers montés actuellement. Elle fournit une vue d'ensemble de votre stockage.

Pour obtenir un rapport dans un format lisible par l'homme (par exemple, Go, Mo, Ko), utilisez l'indicateur `-h` :

```bash
pete@icebox:~$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       6.2G  2.3G  3.6G  40% /
```

Ce résultat montre le périphérique du système de fichiers, la taille totale, l'espace utilisé, l'espace disponible, le pourcentage d'utilisation et son point de montage.

### Analyse de l'utilisation des inodes

En plus de l'espace bloc, les systèmes de fichiers utilisent également des inodes pour stocker les métadonnées des fichiers (comme les permissions, la propriété et l'emplacement). Dans de rares cas, vous pouvez manquer d'inodes même s'il reste de l'espace disque libre. Pour vérifier l'utilisation des inodes, vous pouvez utiliser la commande `df -i`. L'exécution de `df -i` sous Linux vous donne une image claire de l'allocation des inodes.

```bash
pete@icebox:~$ df -i
Filesystem      Inodes  IUsed   IFree IUse% Mounted on
/dev/sda1      4128768 128768 4000000    4% /
```

### Résumé de l'utilisation des répertoires avec du

Lorsque vous remarquez qu'un disque se remplit, vous voudrez identifier quels fichiers ou répertoires consomment le plus d'espace. Pour cette tâche, la commande `du` (disk usage) est l'outil parfait.

Exécuter `du` sans arguments montre l'utilisation du disque pour chaque sous-répertoire de votre emplacement actuel. L'utilisation de l'indicateur `-h` fournit un résumé lisible par l'homme :

```bash
du -h
```

Vous pouvez également spécifier un chemin, comme `du -h /home/pete`, pour analyser un répertoire spécifique. L'exécuter sur le répertoire racine (`du -h /`) peut générer beaucoup de résultats, il est donc souvent préférable de vérifier les répertoires spécifiques que vous soupçonnez d'être volumineux.

### df vs du Un bref résumé

La syntaxe de `df` et `du` est si similaire qu'il peut être facile de les confondre. Voici un moyen simple de se souvenir de la différence :

- Utilisez `df` pour vérifier combien d'**e**space **d**isque est **l**ibre sur vos systèmes de fichiers.
- Utilisez `du` pour vérifier l'**u**tilisati**o**n du **d**isque des fichiers et répertoires spécifiques.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion et de l'utilisation de l'espace disque sous Linux :

1. **[Gérer les partitions et les systèmes de fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Entraînez-vous à créer, formater et monter des systèmes de fichiers, qui sont les structures sous-jacentes signalées par `df` et `du`.
2. **[Créer et activer un fichier d'échange (Swap) sous Linux](https://labex.io/fr/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Apprenez à gérer la mémoire virtuelle sur disque, un aspect critique de la gestion des ressources système qui a un impact sur l'espace disque.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion des ressources disque.

## Quiz Question

Quelle commande est utilisée pour afficher l'espace libre sur votre disque ? Veuillez répondre en lettres minuscules anglaises.

## Quiz Answer

df
