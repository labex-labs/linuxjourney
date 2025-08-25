---
index: 5
lang: "fr"
title: "Setuid"
meta_title: "Setuid - Permissions"
meta_description: "Découvrez les permissions Linux Setuid (SUID), leur fonctionnement et comment les modifier. Comprenez SUID pour un accès sécurisé aux fichiers sous Linux."
meta_keywords: "Linux Setuid, SUID, permissions Linux, chmod, commande passwd, sécurité Linux, Linux débutant, tutoriel Linux"
---

## Lesson Content

Il existe de nombreux cas où les utilisateurs normaux ont besoin d'un accès élevé pour effectuer certaines tâches. L'administrateur système ne peut pas toujours être là pour saisir un mot de passe root chaque fois qu'un utilisateur a besoin d'accéder à un fichier protégé. Il existe donc des bits de permission de fichier spéciaux pour permettre ce comportement. Le Set User ID (SUID) permet à un utilisateur d'exécuter un programme en tant que propriétaire du fichier programme plutôt qu'en tant que lui-même.

Examinons un exemple :

Disons que je veux changer mon mot de passe, simple n'est-ce pas ? J'utilise simplement la commande `passwd` :

```bash
passwd
```

Que fait la commande `passwd` ? Elle modifie quelques fichiers, mais surtout elle modifie le fichier `/etc/shadow`. Regardons ce fichier un instant :

```bash
$ ls -l /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
```

Attendez une minute, ce fichier appartient à root ? Comment est-il possible que nous puissions modifier un fichier appartenant à root ?

Regardons un autre ensemble de permissions, cette fois de la commande que nous avons exécutée :

```bash
$ ls -l /usr/bin/passwd

-rwsr-xr-x 1 root root 47032 Dec 1 11:45 /usr/bin/passwd
```

Vous remarquerez un nouveau bit de permission ici : **s**. Ce bit de permission est le SUID. Lorsqu'un fichier a cette permission définie, il permet aux utilisateurs qui ont lancé le programme d'obtenir la permission du propriétaire du fichier ainsi que la permission d'exécution, dans ce cas root. Donc, essentiellement, lorsqu'un utilisateur exécute la commande `passwd`, il s'exécute en tant que root.

C'est pourquoi nous pouvons accéder à un fichier protégé comme `/etc/shadow` lorsque nous exécutons la commande `passwd`. Maintenant, si vous supprimiez ce bit, vous verriez que vous ne pourrez pas modifier `/etc/shadow` et donc changer votre mot de passe.

### Modification du SUID

Tout comme les permissions régulières, il existe deux façons de modifier les permissions SUID.

_Manière symbolique :_

```bash
sudo chmod u+s myfile
```

_Manière numérique :_

```bash
sudo chmod 4755 myfile
```

Comme vous pouvez le voir, le SUID est représenté par un 4 et est ajouté au début de l'ensemble de permissions. Vous pouvez voir le SUID représenté par un **S** majuscule. Cela signifie qu'il fait toujours la même chose, mais qu'il n'a pas les permissions d'exécution.

## Exercise

La pratique rend parfait ! Comprendre le fonctionnement des permissions de fichiers, des groupes d'utilisateurs et des bits spéciaux comme SUID est crucial pour gérer et sécuriser les systèmes Linux. L'expérience pratique consolidera vos connaissances.

Voici un laboratoire pratique pour renforcer votre compréhension des permissions de fichiers et de la gestion des utilisateurs :

1. **[Groupes d'utilisateurs Linux et permissions de fichiers](https://labex.io/fr/labs/linux-linux-user-group-and-file-permissions-18002)** - Entraînez-vous à créer et gérer des utilisateurs et des groupes, à comprendre les permissions de fichiers et à manipuler la propriété des fichiers. Ce laboratoire fournit les connaissances fondamentales nécessaires pour comprendre comment SUID exploite ces concepts pour un accès élevé.

Ce laboratoire vous aidera à appliquer les concepts dans un scénario réel et à renforcer votre confiance dans la gestion des utilisateurs et des fichiers sous Linux.

## Quiz Question

Quel nombre représente le SUID ?

## Quiz Answer

4
