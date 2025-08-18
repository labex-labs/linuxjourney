---
lang: "fr"
title: "/etc/group"
meta_title: "/etc/group - Gestion des Utilisateurs"
meta_description: "Découvrez le fichier /etc/group sous Linux, comprenez la gestion des groupes, le GID et les permissions des utilisateurs. Tutoriel essentiel sur le fichier de groupe Linux pour les débutants."
meta_keywords: "/etc/group, groupes Linux, gestion des groupes, GID, permissions Linux, tutoriel Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

Un autre fichier utilisé dans la gestion des utilisateurs est le fichier `/etc/group`. Ce fichier permet de créer différents groupes avec différentes permissions.

```bash
$ cat /etc/group

root:*:0:pete
```

Très similaire au fichier `/etc/passwd`, les champs de `/etc/group` sont les suivants :

1. Nom du groupe
2. Mot de passe du groupe - il n'est pas nécessaire de définir un mot de passe de groupe ; l'utilisation d'un privilège élevé comme `sudo` est standard. Un astérisque (`*`) sera mis en place comme valeur par défaut.
3. Group ID (GID)
4. Liste des utilisateurs - vous pouvez spécifier manuellement les utilisateurs que vous souhaitez dans un groupe spécifique

## Exercise

Run the command `groups`. What do you see?

## Quiz Question

Quel est le GID de root ?

## Quiz Answer

0
