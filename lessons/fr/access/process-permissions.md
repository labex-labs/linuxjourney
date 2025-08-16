---
lang: "fr"
title: "Permissions de processus"
description: "Découvrez les permissions de processus Linux, y compris les ID utilisateur réels, effectifs et sauvegardés. Comprenez comment les UID impactent la sécurité et l'exécution des commandes. Commencez à apprendre dès aujourd'hui !"
keywords: "permissions de processus Linux, UID réel, UID effectif, UID sauvegardé, sécurité Linux, commande passwd, tutoriel Linux, Linux pour débutants"
---

## Lesson Content

Passons un instant aux permissions de processus. Vous souvenez-vous que je vous ai dit que lorsque vous exécutez la commande `passwd` avec le bit de permission SUID activé, vous exécuterez le programme en tant que root ? C'est vrai. Cependant, cela signifie-t-il que, puisque vous êtes temporairement root, vous pouvez modifier les mots de passe d'autres utilisateurs ? Non, heureusement pas !

Ceci est dû aux nombreux UID que Linux implémente. Il y a trois UID associés à chaque processus :

Lorsque vous lancez un processus, il s'exécute avec les mêmes permissions que l'utilisateur ou le groupe qui l'a lancé. C'est ce qu'on appelle un **ID utilisateur effectif**. Cet UID est utilisé pour accorder des droits d'accès à un processus. Donc, naturellement, si Bob a exécuté la commande `touch`, le processus s'exécuterait en tant que lui, et tous les fichiers qu'il a créés seraient sous sa propriété.

Il existe un autre UID, appelé l'**ID utilisateur réel**. C'est l'ID de l'utilisateur qui a lancé le processus. Ceux-ci sont utilisés pour retrouver l'utilisateur qui a lancé le processus.

Un dernier UID est l'**ID utilisateur sauvegardé**. Cela permet à un processus de basculer entre l'UID effectif et l'UID réel, et vice versa. C'est utile car nous ne voulons pas que notre processus s'exécute avec des privilèges élevés tout le temps ; c'est simplement une bonne pratique d'utiliser des privilèges spéciaux à des moments spécifiques.

Maintenant, assemblons tout cela en examinant la commande `passwd` une fois de plus.

Lors de l'exécution de la commande `passwd`, votre UID effectif est votre ID utilisateur ; disons que c'est 500 pour l'instant. Oh, mais attendez, rappelez-vous que la commande `passwd` a la permission SUID activée. Donc, lorsque vous l'exécutez, votre UID effectif est maintenant 0 (0 est l'UID de root). Maintenant, ce programme peut accéder aux fichiers en tant que root.

Disons que vous avez un petit avant-goût du pouvoir, et que vous voulez modifier le mot de passe de Sally. Sally a un UID de 600. Eh bien, vous n'aurez pas de chance. Heureusement, le processus a aussi votre UID réel, dans ce cas 500. Il sait que votre UID est 500, et par conséquent vous ne pouvez pas modifier le mot de passe de l'UID 600. (Ceci, bien sûr, est toujours contourné si vous êtes un superutilisateur sur une machine et pouvez tout contrôler et modifier).

Puisque vous avez exécuté `passwd`, il démarrera le processus en utilisant votre UID réel, et il sauvegardera l'UID du propriétaire du fichier (UID effectif), afin que vous puissiez basculer entre les deux. Pas besoin de modifier tous les fichiers avec un accès root si ce n'est pas nécessaire.

La plupart du temps, l'UID réel et l'UID effectif sont les mêmes, mais dans des cas comme la commande `passwd`, ils changeront.

## Exercise

Nous n'avons pas encore discuté des processus, mais nous pouvons toujours observer ce changement en temps réel :

1. Open one terminal window and run the command: `watch -n 1 "ps aux | grep passwd"`. This will watch for the `passwd` process.
2. Open a second terminal window and run: `passwd`.
3. Look at the first terminal window; you'll see a process come up for `passwd`. The first column in the process table is the effective user ID. Lo and behold, it's the root user!

## Quiz Question

Quel UID décide de l'accès à accorder ?

## Quiz Answer

effective
