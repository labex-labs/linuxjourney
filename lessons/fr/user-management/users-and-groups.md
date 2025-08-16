---
lang: "fr"
title: "Utilisateurs et Groupes"
description: "Apprenez-en davantage sur les utilisateurs et les groupes Linux, comprenez les UID, les GID et l'utilisateur root. Découvrez comment utiliser la commande sudo pour des permissions élevées. Commencez votre parcours Linux !"
keywords: "utilisateurs Linux, groupes Linux, commande sudo, utilisateur root, permissions Linux, tutoriel Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

Dans tout système d'exploitation traditionnel, il y a des utilisateurs et des groupes. Ils existent uniquement pour l'accès et les permissions. Lors de l'exécution d'un processus, il s'exécutera en tant que propriétaire de ce processus, que ce soit Jane ou Bob. L'accès aux fichiers et la propriété dépendent également des permissions. Vous ne voudriez pas que Jane voie les documents de Bob et vice versa.

Chaque utilisateur a son propre répertoire personnel où ses fichiers spécifiques à l'utilisateur sont stockés. Celui-ci est généralement situé dans `/home/username`, mais peut varier selon les distributions.

Le système utilise des identifiants d'utilisateur (UID) pour gérer les utilisateurs. Les noms d'utilisateur sont la manière conviviale d'associer les utilisateurs à une identification, mais le système identifie les utilisateurs par leur UID. Le système utilise également des groupes pour gérer les permissions. Les groupes sont simplement des ensembles d'utilisateurs avec des permissions définies par ce groupe ; ils sont identifiés par le système avec leur identifiant de groupe (GID).

Sous Linux, vous aurez des utilisateurs en plus des humains normaux qui utilisent le système. Parfois, ces utilisateurs sont des démons système qui exécutent continuellement des processus pour maintenir le système en fonctionnement. L'un des utilisateurs les plus importants est `root` ou `superuser`. `root` est l'utilisateur le plus puissant du système ; `root` peut accéder à n'importe quel fichier et démarrer et terminer n'importe quel processus. Pour cette raison, il peut être dangereux d'opérer en tant que `root` tout le temps ; vous pourriez potentiellement supprimer des fichiers critiques pour le système. Heureusement, si un accès `root` est nécessaire et qu'un utilisateur a un accès `root`, il peut exécuter une commande en tant que `root` à la place avec la commande `sudo`. La commande `sudo` (superuser do) est utilisée pour exécuter une commande avec un accès `root`. Nous verrons plus en détail comment un utilisateur reçoit l'accès `root` dans une leçon ultérieure.

Allez-y et essayez de visualiser un fichier protégé comme `/etc/shadow` :

```bash
cat /etc/shadow
```

Remarquez comment vous obtenez une erreur de permission refusée. Regardez les permissions avec :

```bash
$ ls -la /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
```

Nous n'avons pas encore abordé les permissions, mais ce qui se passe ici, c'est que `root` est le propriétaire du fichier, et vous aurez besoin d'un accès `root` ou de faire partie du groupe `shadow` pour lire le contenu. Maintenant, exécutez la commande avec `sudo` :

```bash
sudo cat /etc/shadow
```

Maintenant, vous pourrez voir le contenu du fichier !

## Exercise

No exercises for this lesson.

## Quiz Question

Quelle commande utilisez-vous pour exécuter en tant que `root` ?

## Quiz Answer

sudo
