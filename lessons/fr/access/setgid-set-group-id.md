---
index: 6
lang: "fr"
title: "Setgid"
meta_title: "Setgid - Permissions"
meta_description: "Découvrez les permissions SGID (Set Group ID) de Linux, leur fonctionnement et comment les modifier. Comprenez ce concept crucial de sécurité Linux."
meta_keywords: "Linux SGID, Set Group ID, permissions Linux, chmod g+s, sécurité Linux, Linux pour débutants, tutoriel Linux"
---

## Lesson Content

Similaire au bit de permission set user ID, il existe un bit de permission set group ID (SGID). Ce bit permet à un programme de s'exécuter comme s'il était membre de ce groupe.

Examinons un exemple :

```bash
$ ls -l /usr/bin/wall
-rwxr-sr-x 1 root tty 19024 Dec 14 11:45 /usr/bin/wall
```

Nous pouvons maintenant voir que le bit de permission se trouve dans l'ensemble des permissions de groupe.

### Modification du SGID

```bash
sudo chmod g+s myfile
sudo chmod 2555 myfile
```

La représentation numérique pour SGID est 2.

## Exercise

C'est en forgeant qu'on devient forgeron ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des permissions d'utilisateur, de groupe et de fichier sous Linux :

1. **[Permissions d'utilisateur, de groupe et de fichier Linux](https://labex.io/fr/labs/linux-linux-user-group-and-file-permissions-18002)** - Apprenez les concepts essentiels de gestion des utilisateurs et des groupes Linux, y compris la création et la gestion des utilisateurs, l'exploration des appartenances aux groupes, la compréhension des permissions de fichier et la manipulation de la propriété des fichiers.
2. **[Ajouter un nouvel utilisateur et un nouveau groupe](https://labex.io/fr/labs/linux-add-new-user-and-group-17987)** - Entraînez-vous à créer de nouveaux comptes d'utilisateur, à configurer des groupes personnalisés et à gérer les appartenances aux groupes, en simulant des tâches d'administration système réelles.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance avec les permissions Linux et la gestion des utilisateurs.

## Quiz Question

Quel nombre représente le SGID ?

## Quiz Answer

2
