---
title: "Setgid"
description: "Apprenez-en davantage sur les permissions Linux SGID (Set Group ID), leur fonctionnement et comment les modifier. Comprenez ce concept crucial de sécurité Linux."
keywords: "Linux SGID, Set Group ID, permissions Linux, chmod g+s, sécurité Linux, Linux débutant, tutoriel Linux"
---

## Lesson Content

Similaire au bit de permission set user ID, il existe un bit de permission set group ID (SGID). Ce bit permet à un programme de s'exécuter comme s'il était membre de ce groupe.

Examinons un exemple :

```bash
$ ls -l /usr/bin/wall
-rwxr-sr-x 1 root tty 19024 Dec 14 11:45 /usr/bin/wall
```

Nous pouvons maintenant voir que le bit de permission se trouve dans l'ensemble des permissions de groupe.

### Modifying SGID

```bash
sudo chmod g+s myfile
sudo chmod 2555 myfile
```

La représentation numérique pour SGID est 2.

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Quel nombre représente le SGID ?

## Quiz Answer

2
