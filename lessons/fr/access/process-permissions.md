---
index: 7
lang: "fr"
title: "Permissions de processus"
meta_title: "Permissions de processus - Permissions"
meta_description: "Découvrez les permissions de processus Linux, y compris les ID utilisateur réels, effectifs et sauvegardés. Comprenez comment les UID impactent la sécurité et l'exécution des commandes. Commencez à apprendre dès aujourd'hui !"
meta_keywords: "permissions de processus Linux, UID réel, UID effectif, UID sauvegardé, sécurité Linux, commande passwd, tutoriel Linux, Linux pour débutants"
---

## Lesson Content

Passons un instant aux permissions de processus. Vous souvenez-vous que je vous ai dit que lorsque vous exécutez la commande `passwd` avec le bit de permission SUID activé, vous exécuterez le programme en tant que root ? C'est vrai. Cependant, cela signifie-t-il que, puisque vous êtes temporairement root, vous pouvez modifier les mots de passe des autres utilisateurs ? Non, heureusement pas !

Ceci est dû aux nombreux UID que Linux implémente. Il y a trois UID associés à chaque processus :

Lorsque vous lancez un processus, il s'exécute avec les mêmes permissions que l'utilisateur ou le groupe qui l'a lancé. C'est ce qu'on appelle un **ID utilisateur effectif**. Cet UID est utilisé pour accorder des droits d'accès à un processus. Donc, naturellement, si Bob a exécuté la commande `touch`, le processus s'exécuterait en tant que lui, et tous les fichiers qu'il a créés seraient sous sa propriété.

Il existe un autre UID, appelé **ID utilisateur réel**. C'est l'ID de l'utilisateur qui a lancé le processus. Ceux-ci sont utilisés pour savoir qui est l'utilisateur qui a lancé le processus.

Un dernier UID est l'**ID utilisateur sauvegardé**. Cela permet à un processus de basculer entre l'UID effectif et l'UID réel, et vice versa. C'est utile car nous ne voulons pas que notre processus s'exécute avec des privilèges élevés tout le temps ; c'est une bonne pratique d'utiliser des privilèges spéciaux à des moments spécifiques.

Maintenant, assemblons tout cela en examinant la commande `passwd` une fois de plus.

Lors de l'exécution de la commande `passwd`, votre UID effectif est votre ID utilisateur ; disons que c'est 500 pour l'instant. Oh, mais attendez, rappelez-vous que la commande `passwd` a la permission SUID activée. Donc, lorsque vous l'exécutez, votre UID effectif est maintenant 0 (0 est l'UID de root). Maintenant, ce programme peut accéder aux fichiers en tant que root.

Disons que vous avez un petit goût de pouvoir, et que vous voulez modifier le mot de passe de Sally. Sally a un UID de 600. Eh bien, vous n'aurez pas de chance. Heureusement, le processus a aussi votre UID réel, dans ce cas 500. Il sait que votre UID est 500, et donc vous ne pouvez pas modifier le mot de passe de l'UID 600. (Ceci, bien sûr, est toujours contourné si vous êtes un superutilisateur sur une machine et pouvez tout contrôler et modifier).

Puisque vous avez exécuté `passwd`, il démarrera le processus en utilisant votre UID réel, et il sauvegardera l'UID du propriétaire du fichier (UID effectif), afin que vous puissiez basculer entre les deux. Pas besoin de modifier tous les fichiers avec un accès root si ce n'est pas nécessaire.

La plupart du temps, l'UID réel et l'UID effectif sont les mêmes, mais dans des cas comme la commande `passwd`, ils changeront.

## Exercise

La pratique rend parfait ! Comprendre les ID utilisateur et les permissions de processus est crucial pour la sécurité et l'administration de Linux. Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des utilisateurs et des groupes, qui constitue la base du fonctionnement des UID :

1. **[Groupes d'utilisateurs Linux et permissions de fichiers](https://labex.io/fr/labs/linux-linux-user-group-and-file-permissions-18002)** - Apprenez les concepts essentiels de la gestion des utilisateurs et des groupes Linux, y compris la création et la gestion des utilisateurs, l'exploration des appartenances aux groupes, la compréhension des permissions de fichiers et la manipulation de la propriété des fichiers. Ce laboratoire offre une expérience pratique pour sécuriser un environnement Linux multi-utilisateur.
2. **[Ajouter un nouvel utilisateur et un nouveau groupe](https://labex.io/fr/labs/linux-add-new-user-and-group-17987)** - Dans ce défi, vous simulerez l'ajout de nouveaux membres d'équipe à un environnement serveur en créant de nouveaux comptes utilisateur, en configurant des groupes personnalisés et en gérant les appartenances aux groupes. Cela testera vos compétences en administration des utilisateurs et des groupes Linux, essentielles pour les administrateurs système et les professionnels DevOps.

Ces laboratoires vous aideront à appliquer les concepts de gestion des utilisateurs et des groupes dans des scénarios réels, en construisant une base solide pour comprendre comment les UID contrôlent l'accès et les permissions dans Linux.

## Quiz Question

Quel UID décide quel accès accorder ?

## Quiz Answer

effective
