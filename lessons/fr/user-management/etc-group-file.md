---
index: 5
lang: "fr"
title: "/etc/group"
meta_title: "/etc/group - Gestion des utilisateurs"
meta_description: "Découvrez le fichier /etc/group sous Linux, comprenez la gestion des groupes, le GID et les permissions des utilisateurs. Tutoriel essentiel sur le fichier de groupe Linux pour les débutants."
meta_keywords: "/etc/group, groupes Linux, gestion de groupe, GID, permissions Linux, tutoriel Linux, Linux débutant, guide Linux"
---

## Lesson Content

Un autre fichier utilisé dans la gestion des utilisateurs est le fichier `/etc/group`. Ce fichier permet de créer différents groupes avec différentes permissions.

```bash
$ cat /etc/group

root:*:0:pete
```

Très similaire au fichier `/etc/passwd`, les champs du fichier `/etc/group` sont les suivants :

1. Nom du groupe
2. Mot de passe du groupe - il n'est pas nécessaire de définir un mot de passe de groupe ; l'utilisation d'un privilège élevé comme `sudo` est standard. Un astérisque (`*`) sera mis en place comme valeur par défaut.
3. Identifiant de groupe (GID)
4. Liste des utilisateurs - vous pouvez spécifier manuellement les utilisateurs que vous souhaitez inclure dans un groupe spécifique

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des utilisateurs et des groupes Linux :

1. **[Gérer les comptes d'utilisateurs Linux avec useradd, usermod et userdel](https://labex.io/fr/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Pratiquez le cycle de vie complet de l'administration des utilisateurs, de la création et la sécurisation de nouveaux comptes à leur modification et suppression.
2. **[Gérer les groupes Linux avec groupadd, usermod et groupdel](https://labex.io/fr/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Acquérez une expérience pratique avec les utilitaires de ligne de commande essentiels pour l'administration des groupes, y compris `groupadd`, `usermod` et `groupdel`.
3. **[Ajouter un nouvel utilisateur et un nouveau groupe](https://labex.io/fr/labs/linux-add-new-user-and-group-17987)** - Simulez l'ajout de nouveaux membres d'équipe à un environnement serveur en créant de nouveaux comptes d'utilisateurs, en configurant des groupes personnalisés et en gérant les appartenances aux groupes.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion des utilisateurs et des groupes Linux.

## Quiz Question

Quel est le GID de root ?

## Quiz Answer

0
