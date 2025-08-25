---
index: 6
lang: "fr"
title: "Outils de gestion des utilisateurs"
meta_title: "Outils de gestion des utilisateurs - Gestion des utilisateurs"
meta_description: "Apprenez la gestion des utilisateurs Linux : ajouter, supprimer et changer les mots de passe avec les commandes useradd, userdel et passwd. Démarrez avec ce guide convivial pour débutants !"
meta_keywords: "gestion des utilisateurs Linux, adduser, userdel, passwd, tutoriel Linux, Linux débutant, comptes utilisateurs, commandes Linux"
---

## Lesson Content

La plupart des environnements d'entreprise utilisent des systèmes de gestion pour gérer les utilisateurs, les comptes et les mots de passe. Cependant, sur un ordinateur monoposte, il existe des commandes utiles à exécuter pour gérer les utilisateurs.

### Ajout d'utilisateurs

Vous pouvez utiliser la commande `adduser` ou `useradd`. La commande `adduser` contient des fonctionnalités plus utiles, telles que la création d'un répertoire personnel et plus encore. Il existe des fichiers de configuration pour l'ajout de nouveaux utilisateurs qui peuvent être personnalisés en fonction de ce que vous souhaitez allouer à un utilisateur par défaut.

```bash
sudo useradd bob
```

Vous verrez que la commande ci-dessus crée une entrée dans `/etc/passwd` pour bob, configure les groupes par défaut et ajoute une entrée au fichier `/etc/shadow`.

### Suppression d'utilisateurs

Pour supprimer un utilisateur, vous pouvez utiliser la commande `userdel`.

```bash
sudo userdel bob
```

Ceci annule essentiellement au mieux les modifications de fichiers effectuées par `useradd`.

### Modification des mots de passe

```bash
passwd bob
```

Cela vous permettra de changer votre propre mot de passe ou celui d'un autre utilisateur (si vous êtes root).

## Exercise

C'est en forgeant qu'on devient forgeron ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des utilisateurs et des comptes sous Linux :

1. **[Gérer les comptes d'utilisateurs Linux avec useradd, usermod et userdel](https://labex.io/fr/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Pratiquez le cycle de vie complet de l'administration des utilisateurs, de la création et la sécurisation de nouveaux comptes à leur modification et suppression.
2. **[Gérer les groupes Linux avec groupadd, usermod et groupdel](https://labex.io/fr/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Acquérez une expérience pratique avec les utilitaires de ligne de commande essentiels pour l'administration des groupes, y compris l'ajout, la modification et la suppression de groupes.
3. **[Configurer les comptes d'utilisateurs et les privilèges Sudo sous Linux](https://labex.io/fr/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Apprenez les techniques essentielles pour gérer les comptes d'utilisateurs et les privilèges sudo afin d'améliorer la sécurité d'un système Linux.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion des utilisateurs et des groupes sous Linux.

## Quiz Question

Quelle commande est utilisée pour changer un mot de passe ?

## Quiz Answer

passwd
