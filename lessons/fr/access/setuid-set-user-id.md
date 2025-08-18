---
lang: "fr"
title: "Setuid"
meta_description: "Découvrez les permissions Linux Setuid (SUID), leur fonctionnement et comment les modifier. Comprenez le SUID pour un accès sécurisé aux fichiers sous Linux."
meta_keywords: "Linux Setuid, SUID, permissions Linux, chmod, commande passwd, sécurité Linux, Linux pour débutants, tutoriel Linux"
---

## Lesson Content

Il existe de nombreux cas où les utilisateurs normaux ont besoin d'un accès élevé pour effectuer certaines tâches. L'administrateur système ne peut pas toujours être là pour entrer un mot de passe root chaque fois qu'un utilisateur a besoin d'accéder à un fichier protégé, il existe donc des bits de permission de fichier spéciaux pour permettre ce comportement. Le Set User ID (SUID) permet à un utilisateur d'exécuter un programme en tant que propriétaire du fichier programme plutôt qu'en tant que lui-même.

Regardons un exemple :

Disons que je veux changer mon mot de passe, simple n'est-ce pas ? J'utilise simplement la commande `passwd` :

```bash
passwd
```

Que fait la commande `passwd` ? Elle modifie quelques fichiers, mais surtout elle modifie le fichier `/etc/shadow`. Regardons ce fichier un instant :

```bash
$ ls -l /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
```

Oh, attendez une minute, ce fichier est la propriété de root ? Comment est-il possible que nous puissions modifier un fichier appartenant à root ?

Regardons un autre ensemble de permissions, cette fois de la commande que nous avons exécutée :

```bash
$ ls -l /usr/bin/passwd

-rwsr-xr-x 1 root root 47032 Dec 1 11:45 /usr/bin/passwd
```

Vous remarquerez un nouveau bit de permission ici **s**. Ce bit de permission est le SUID. Lorsqu'un fichier a cette permission définie, il permet aux utilisateurs qui ont lancé le programme d'obtenir la permission du propriétaire du fichier ainsi que la permission d'exécution, dans ce cas root. Donc, essentiellement, lorsqu'un utilisateur exécute la commande `passwd`, il s'exécute en tant que root.

C'est pourquoi nous pouvons accéder à un fichier protégé comme `/etc/shadow` lorsque nous exécutons la commande `passwd`. Maintenant, si vous supprimiez ce bit, vous verriez que vous ne seriez pas en mesure de modifier `/etc/shadow` et donc de changer votre mot de passe.

### Modifying SUID

Tout comme les permissions régulières, il existe deux façons de modifier les permissions SUID.

_Symbolic way:_

```bash
sudo chmod u+s myfile
```

_Numerical way:_

```bash
sudo chmod 4755 myfile
```

Comme vous pouvez le voir, le SUID est représenté par un 4 et est ajouté au début de l'ensemble de permissions. Vous pouvez voir le SUID représenté par un **S** majuscule. Cela signifie qu'il fait toujours la même chose, mais qu'il n'a pas les permissions d'exécution.

## Exercise

Regardez les permissions de `/etc/passwd` en détail. Remarquez-vous autre chose ? Les fichiers avec SUID activé sont également facilement distinguables.

## Quiz Question

Quel nombre représente le SUID ?

## Quiz Answer

4
