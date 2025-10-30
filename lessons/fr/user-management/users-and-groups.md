---
index: 1
lang: "fr"
title: "Utilisateurs et Groupes"
meta_title: "Utilisateurs et Groupes - Gestion des Utilisateurs"
meta_description: "Une partie essentielle des bases de Linux est la compréhension de la gestion des utilisateurs et des groupes. Ce guide couvre les utilisateurs et groupes Linux, le superutilisateur root, et l'utilisation de la commande sudo pour les privilèges élevés. L'une des meilleures leçons de tutoriel Linux pour débutants."
meta_keywords: "utilisateurs et groupes linux, bases de linux, sudo, utilisateur root, UID, GID, gestion des utilisateurs, meilleur tutoriel linux, chemin le plus rapide vers linux avancé"
---

## Lesson Content

Dans tout système d'exploitation multi-utilisateur, la gestion des utilisateurs et des groupes est un concept fondamental. C'est un élément central des **bases de linux**, conçu pour le contrôle d'accès et les permissions. Lorsqu'un processus s'exécute, il le fait en tant qu'utilisateur qui l'a lancé. De même, l'accès aux fichiers et la propriété dépendent des permissions, empêchant un utilisateur d'accéder aux documents privés d'un autre.

### Les bases des utilisateurs et des groupes Linux

Chaque utilisateur d'un système Linux se voit attribuer un répertoire personnel, généralement situé dans `/home/nom_utilisateur`. Ce répertoire est l'endroit où sont stockés ses fichiers et configurations spécifiques à l'utilisateur, bien que le chemin exact puisse varier selon les distributions Linux.

Le système identifie les utilisateurs par un ID utilisateur (UID) et les groupes par un ID de groupe (GID). Bien que nous utilisions des noms d'utilisateur lisibles par l'homme, le système d'exploitation s'appuie sur ces identifiants numériques uniques pour toutes les tâches liées aux permissions. Les groupes sont simplement des collections d'utilisateurs, ce qui facilite la gestion des permissions pour plusieurs comptes à la fois.

### Le Superutilisateur et la commande Sudo

Au sein de la hiérarchie des **utilisateurs et groupes linux**, un utilisateur se situe au-dessus de tous les autres : `root`, également connu sous le nom de superutilisateur. L'utilisateur `root` dispose d'un pouvoir illimité, capable d'accéder à n'importe quel fichier et de gérer n'importe quel processus. Opérer continuellement en tant que `root` est risqué, car une simple erreur pourrait endommager le système.

Pour atténuer ce risque, les utilisateurs autorisés peuvent exécuter des commandes avec des privilèges root en utilisant la commande `sudo` (superuser do). Cela permet d'effectuer des tâches administratives sans se connecter en tant qu'utilisateur `root`. Comprendre comment utiliser correctement `sudo` est essentiel pour quiconque souhaite acquérir les compétences d'administration **du niveau avancé linux le plus rapide**.

Essayons de visualiser un fichier protégé, tel que `/etc/shadow`, qui stocke les mots de passe utilisateur chiffrés.

```bash
cat /etc/shadow
```

Vous recevrez une erreur "Permission non accordée". Examinons les permissions du fichier :

```bash
$ ls -la /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
```

Bien que nous abordions les permissions en détail plus tard, cette sortie montre que seuls l'utilisateur `root` et les membres du groupe `shadow` peuvent lire ce fichier. Exécutez maintenant la commande à nouveau avec `sudo` :

```bash
sudo cat /etc/shadow
```

Cette fois, votre mot de passe vous sera demandé et, après une authentification réussie, le contenu du fichier sera affiché.

## Exercise

Bien que de nombreuses applications pour apprendre linux existent, la pratique concrète est essentielle. Voici quelques laboratoires pour renforcer votre compréhension des utilisateurs, des groupes Linux et de `sudo` :

1. **[Gérer les comptes utilisateurs Linux avec useradd, usermod et userdel](https://labex.io/fr/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Entraînez-vous au cycle complet de l'administration des utilisateurs, de la création et de la sécurisation des nouveaux comptes à leur modification et suppression.
2. **[Gérer les groupes Linux avec groupadd, usermod et groupdel](https://labex.io/fr/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Acquérir une expérience pratique avec les utilitaires de ligne de commande de base pour l'administration des groupes, y compris la création de nouveaux groupes, la modification des appartenances des utilisateurs et la suppression de groupes.
3. **[Configurer les comptes utilisateurs et les privilèges Sudo sous Linux](https://labex.io/fr/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Apprenez les techniques essentielles pour gérer les comptes utilisateurs et les privilèges `sudo` afin d'améliorer la sécurité d'un système Linux, y compris l'octroi de permissions administratives.

Ces laboratoires vous aideront à appliquer les concepts de gestion des utilisateurs et des groupes, ainsi que l'utilisation de `sudo`, dans des scénarios réels et à renforcer votre confiance dans l'administration système Linux.

## Quiz Question

Quelle commande vous permet d'exécuter une seule commande avec les privilèges `root` ? (Veuillez répondre en anglais, en utilisant uniquement des lettres minuscules).

## Quiz Answer

sudo
