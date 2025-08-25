---
index: 1
lang: "fr"
title: "Utilisateurs et Groupes"
meta_title: "Utilisateurs et Groupes - Gestion des utilisateurs"
meta_description: "Apprenez les utilisateurs et les groupes Linux, comprenez les UID, les GID et l'utilisateur root. Découvrez comment utiliser la commande sudo pour des permissions élevées. Commencez votre parcours Linux !"
meta_keywords: "utilisateurs Linux, groupes Linux, commande sudo, utilisateur root, permissions Linux, tutoriel Linux, Linux débutant, guide Linux"
---

## Lesson Content

Dans tout système d'exploitation traditionnel, il existe des utilisateurs et des groupes. Ils existent uniquement pour l'accès et les permissions. Lors de l'exécution d'un processus, il s'exécutera en tant que propriétaire de ce processus, que ce soit Jane ou Bob. L'accès aux fichiers et la propriété dépendent également des permissions. Vous ne voudriez pas que Jane voie les documents de Bob et vice versa.

Chaque utilisateur a son propre répertoire personnel où sont stockés ses fichiers spécifiques. Celui-ci est généralement situé dans `/home/username`, mais peut varier selon les distributions.

Le système utilise des identifiants d'utilisateur (UID) pour gérer les utilisateurs. Les noms d'utilisateur sont le moyen convivial d'associer les utilisateurs à une identification, mais le système identifie les utilisateurs par leur UID. Le système utilise également des groupes pour gérer les permissions. Les groupes sont simplement des ensembles d'utilisateurs avec des permissions définies par ce groupe ; ils sont identifiés par le système avec leur identifiant de groupe (GID).

Sous Linux, vous aurez des utilisateurs en plus des humains normaux qui utilisent le système. Parfois, ces utilisateurs sont des démons système qui exécutent continuellement des processus pour maintenir le système en fonctionnement. L'un des utilisateurs les plus importants est `root` ou `superuser`. `root` est l'utilisateur le plus puissant du système ; `root` peut accéder à n'importe quel fichier et démarrer et terminer n'importe quel processus. Pour cette raison, il peut être dangereux d'opérer en tant que `root` tout le temps ; vous pourriez potentiellement supprimer des fichiers critiques du système. Heureusement, si un accès `root` est nécessaire et qu'un utilisateur a un accès `root`, il peut exécuter une commande en tant que `root` à la place avec la commande `sudo`. La commande `sudo` (superuser do) est utilisée pour exécuter une commande avec un accès `root`. Nous approfondirons la manière dont un utilisateur reçoit un accès `root` dans une leçon ultérieure.

Allez-y et essayez de visualiser un fichier protégé comme `/etc/shadow` :

```bash
cat /etc/shadow
```

Remarquez comment vous obtenez une erreur de permission refusée. Regardez les permissions avec :

```bash
$ ls -la /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
```

Nous n'avons pas encore abordé les permissions, mais ce qui se passe ici, c'est que `root` est le propriétaire du fichier, et vous aurez besoin d'un accès `root` ou de faire partie du groupe `shadow` pour lire le contenu. Exécutez maintenant la commande avec `sudo` :

```bash
sudo cat /etc/shadow
```

Maintenant, vous pourrez voir le contenu du fichier !

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des utilisateurs, des groupes et de `sudo` sous Linux :

1. **[Gérer les comptes d'utilisateurs Linux avec useradd, usermod et userdel](https://labex.io/fr/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Pratiquez le cycle de vie complet de l'administration des utilisateurs, de la création et la sécurisation de nouveaux comptes à leur modification et suppression.
2. **[Gérer les groupes Linux avec groupadd, usermod et groupdel](https://labex.io/fr/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Acquérez une expérience pratique avec les utilitaires de ligne de commande essentiels pour l'administration des groupes, y compris la création de nouveaux groupes, la modification des appartenances des utilisateurs et la suppression de groupes.
3. **[Configurer les comptes d'utilisateurs et les privilèges Sudo sous Linux](https://labex.io/fr/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Apprenez les techniques essentielles pour gérer les comptes d'utilisateurs et les privilèges `sudo` afin d'améliorer la sécurité d'un système Linux, y compris l'octroi de permissions administratives.

Ces laboratoires vous aideront à appliquer les concepts de gestion des utilisateurs et des groupes, et l'utilisation de `sudo`, dans des scénarios réels et à renforcer votre confiance en l'administration des systèmes Linux.

## Quiz Question

Quelle commande utilisez-vous pour exécuter en tant que `root` ?

## Quiz Answer

sudo
