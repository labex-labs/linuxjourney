---
index: 4
lang: "fr"
title: "Umask"
meta_title: "Umask - Permissions"
meta_description: "Apprenez à utiliser la commande `umask` pour contrôler les permissions de fichiers par défaut sous Linux. Comprenez les permissions numériques et gérez facilement l'accès aux nouveaux fichiers."
meta_keywords: "umask, permissions linux, permissions de fichiers, commandes linux, linux débutant, tutoriel linux, permissions par défaut"
---

## Lesson Content

Chaque fichier créé est livré avec un ensemble de permissions par défaut. Si vous souhaitez modifier cet ensemble de permissions par défaut, vous pouvez le faire avec la commande `umask`. Cette commande utilise l'ensemble de permissions à 3 bits que nous voyons dans les permissions numériques.

Cependant, au lieu d'ajouter ces permissions, `umask` les retire.

```bash
umask 021
```

Dans l'exemple ci-dessus, nous indiquons que nous voulons que les permissions par défaut des nouveaux fichiers permettent aux utilisateurs d'accéder à tout, mais pour les groupes, nous voulons leur retirer la permission d'écriture, et pour les autres, nous voulons leur retirer la permission d'exécution. Le `umask` par défaut sur la plupart des distributions est `022`, ce qui signifie un accès complet pour l'utilisateur, mais pas d'accès en écriture pour le groupe et les autres utilisateurs.

Lorsque vous exécutez la commande `umask`, elle applique cet ensemble de permissions par défaut à tout nouveau fichier que vous créez. Cependant, si vous voulez qu'elle persiste, vous devrez modifier votre fichier de démarrage (`.profile`), mais nous en discuterons dans une leçon ultérieure.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des permissions de fichiers et de leur relation avec les paramètres par défaut :

1. **[Groupes d'utilisateurs Linux et permissions de fichiers](https://labex.io/fr/labs/linux-linux-user-group-and-file-permissions-18002)** - Entraînez-vous à créer et gérer des utilisateurs, à explorer les appartenances aux groupes, à comprendre les permissions de fichiers et à manipuler la propriété des fichiers. Ce laboratoire offre une expérience pratique dans la sécurisation d'un environnement Linux multi-utilisateur, ce qui est crucial pour comprendre comment `umask` influence les permissions des nouveaux fichiers.

Ce laboratoire vous aidera à appliquer les concepts de permissions de fichiers dans des scénarios réels et à renforcer votre confiance dans la gestion des accès sous Linux.

## Quiz Question

Quelle commande est utilisée pour modifier les permissions de fichiers par défaut ?

## Quiz Answer

umask
