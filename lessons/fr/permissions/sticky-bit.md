---
index: 8
lang: "fr"
title: "Le Sticky Bit"
meta_title: "Le Sticky Bit - Permissions"
meta_description: "Découvrez le sticky bit Linux, son utilité dans les répertoires partagés comme /tmp, et comment le définir en utilisant chmod. Comprenez cette permission de fichier clé !"
meta_keywords: "sticky bit Linux, chmod +t, répertoire /tmp, permissions Linux, sécurité des fichiers, tutoriel Linux, Linux pour débutants"
---

## Lesson Content

Un dernier bit de permission spécial dont je veux parler est le sticky bit.

Ce bit de permission "colle un fichier/répertoire", ce qui signifie que seul le propriétaire ou l'utilisateur root peut supprimer ou modifier le fichier. C'est très utile pour les répertoires partagés. Jetez un œil à l'exemple ci-dessous :

```bash
$ ls -ld /tmp
drwxrwxrwx+t 6 root root 4096 Dec 15 11:45 /tmp
```

Vous verrez un bit de permission spécial à la fin ici **t**. Cela signifie que tout le monde peut ajouter des fichiers, écrire des fichiers et modifier des fichiers dans le répertoire `/tmp`, mais seul root peut supprimer le répertoire `/tmp`.

### Modifier le sticky bit

```bash
sudo chmod +t mydir

sudo chmod 1755 mydir
```

La représentation numérique du sticky bit est **1**.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des permissions de fichiers Linux et de leur impact sur la gestion des fichiers et des répertoires :

1. **[Groupe d'utilisateurs Linux et permissions de fichiers](https://labex.io/fr/labs/linux-linux-user-group-and-file-permissions-18002)** - Entraînez-vous à créer et gérer des utilisateurs et des groupes, à comprendre les permissions de fichiers et à manipuler la propriété des fichiers. Ce laboratoire fournit les connaissances fondamentales pour comprendre comment fonctionnent les permissions spéciales comme le sticky bit.
2. **[Supprimer et déplacer des fichiers](https://labex.io/fr/labs/linux-delete-and-move-files-7777)** - Apprenez à supprimer et déplacer des fichiers dans les systèmes Linux. Ce laboratoire vous aidera à comprendre les implications pratiques des permissions, y compris comment elles peuvent restreindre ces actions.
3. **[Trouver un fichier](https://labex.io/fr/labs/linux-find-a-file-17993)** - Entraînez-vous à localiser des fichiers et à définir l'autorité d'accès. Ce laboratoire renforce l'importance des permissions de fichiers et la manière dont elles contrôlent l'accès et la modification.

Ces laboratoires vous aideront à appliquer les concepts de permissions de fichiers dans des scénarios réels et à renforcer votre confiance dans la gestion de l'accès aux fichiers sous Linux.

## Quiz Question

Quel symbole représente le sticky bit ?

## Quiz Answer

t
