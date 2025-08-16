---
title: "Umask"
description: "Apprenez à utiliser la commande `umask` pour contrôler les permissions de fichier par défaut sous Linux. Comprenez les permissions numériques et gérez facilement l'accès aux nouveaux fichiers."
keywords: "umask, permissions linux, permissions de fichier, commandes linux, linux débutant, tutoriel linux, permissions par défaut"
---

## Lesson Content

Chaque fichier créé est livré avec un ensemble de permissions par défaut. Si vous souhaitez modifier cet ensemble de permissions par défaut, vous pouvez le faire avec la commande `umask`. Cette commande utilise l'ensemble de permissions de 3 bits que nous voyons dans les permissions numériques.

Cependant, au lieu d'ajouter ces permissions, `umask` les retire.

```bash
umask 021
```

Dans l'exemple ci-dessus, nous indiquons que nous voulons que les permissions par défaut des nouveaux fichiers permettent aux utilisateurs d'accéder à tout, mais pour les groupes, nous voulons leur retirer la permission d'écriture, et pour les autres, nous voulons leur retirer la permission d'exécution. Le `umask` par défaut sur la plupart des distributions est `022`, ce qui signifie un accès complet pour l'utilisateur, mais pas d'accès en écriture pour le groupe et les autres utilisateurs.

Lorsque vous exécutez la commande `umask`, elle applique cet ensemble de permissions par défaut à tout nouveau fichier que vous créez. Cependant, si vous voulez que cela persiste, vous devrez modifier votre fichier de démarrage (`.profile`), mais nous en discuterons dans une leçon ultérieure.

## Exercise

1. Create a new file, then note its permissions.
2. Modify the `umask` and then create another new file.
3. Check the permissions once more on the new file. What do you expect to see?

## Quiz Question

Quelle commande est utilisée pour modifier les permissions de fichier par défaut ?

## Quiz Answer

umask
