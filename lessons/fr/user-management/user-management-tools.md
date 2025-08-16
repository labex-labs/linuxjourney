---
title: "Outils de gestion des utilisateurs"
description: "Apprenez la gestion des utilisateurs Linux : ajouter, supprimer et changer les mots de passe avec les commandes useradd, userdel et passwd. Démarrez avec ce guide convivial pour débutants !"
keywords: "gestion des utilisateurs Linux, adduser, userdel, passwd, tutoriel Linux, Linux débutant, comptes utilisateurs, commandes Linux"
---

## Lesson Content

La plupart des environnements d'entreprise utilisent des systèmes de gestion pour gérer les utilisateurs, les comptes et les mots de passe. Cependant, sur un ordinateur à machine unique, il existe des commandes utiles à exécuter pour gérer les utilisateurs.

### Adding Users

Vous pouvez utiliser la commande `adduser` ou `useradd`. La commande `adduser` contient des fonctionnalités plus utiles, telles que la création d'un répertoire personnel et plus encore. Il existe des fichiers de configuration pour l'ajout de nouveaux utilisateurs qui peuvent être personnalisés en fonction de ce que vous souhaitez allouer à un utilisateur par défaut.

```bash
sudo useradd bob
```

Vous verrez que la commande ci-dessus crée une entrée dans `/etc/passwd` pour bob, configure les groupes par défaut et ajoute une entrée au fichier `/etc/shadow`.

### Removing Users

Pour supprimer un utilisateur, vous pouvez utiliser la commande `userdel`.

```bash
sudo userdel bob
```

Ceci annule essentiellement les modifications de fichiers effectuées par `useradd`.

### Changing Passwords

```bash
passwd bob
```

Cela vous permettra de changer le mot de passe de vous-même ou d'un autre utilisateur (si vous êtes root).

## Exercise

Créez un nouvel utilisateur, puis changez son mot de passe et connectez-vous en tant que nouvel utilisateur.

## Quiz Question

Quelle commande est utilisée pour changer un mot de passe ?

## Quiz Answer

passwd
