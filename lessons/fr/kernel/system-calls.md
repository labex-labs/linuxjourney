---
lang: "fr"
title: "Appels Système"
description: "Apprenez-en davantage sur les appels système Linux (syscalls) et leur interaction avec le kernel. Comprenez les modes utilisateur et kernel, et utilisez `strace` pour le débogage. Commencez votre parcours Linux !"
keywords: "Appels système Linux, syscalls, mode kernel, mode utilisateur, commande strace, tutoriel Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

Vous vous souvenez de Britney dans la leçon précédente ? Disons que nous voulons la voir et prendre un verre ensemble. Comment passer de l'extérieur, au milieu de la foule, à l'intérieur de son cercle le plus intime ? Nous utiliserions des appels système. Les appels système sont comme les laissez-passer VIP qui vous mènent à une porte dérobée secrète qui mène directement à Britney.

Les appels système (syscalls) offrent aux processus de l'espace utilisateur un moyen de demander au kernel de faire quelque chose pour nous. Le kernel met certains services à disposition via l'API d'appel système. Ces services nous permettent de lire ou d'écrire dans un fichier, de modifier l'utilisation de la mémoire, de modifier notre réseau, etc. Le nombre de services est fixe, vous ne pouvez donc pas ajouter d'appels système à tort et à travers. Votre système dispose déjà d'une table des appels système existants, et chaque appel système a un ID unique.

Je n'entrerai pas dans les détails des appels système, car cela vous obligerait à connaître un peu de C, mais les bases sont que lorsque vous appelez un programme comme `ls`, le code à l'intérieur de ce programme contient un wrapper d'appel système (donc pas encore l'appel système réel). À l'intérieur de ce wrapper, il invoque l'appel système qui exécutera un trap. Ce trap est ensuite intercepté par le gestionnaire d'appels système, qui fait ensuite référence à l'appel système dans la table des appels système. Disons que nous essayons d'appeler l'appel système `stat()` ; il est identifié par un syscall ID, et le but de l'appel système `stat()` est d'interroger l'état d'un fichier. Maintenant, rappelez-vous, vous exécutiez le programme `ls` en mode non privilégié. Donc, maintenant qu'il voit que vous essayez de faire un syscall, il vous bascule en mode kernel. Là, il fait beaucoup de choses, mais surtout, il recherche votre numéro de syscall, le trouve dans une table basée sur le syscall ID, puis exécute la fonction que vous vouliez exécuter. Une fois terminé, il reviendra en mode utilisateur, et votre processus recevra un statut de retour s'il a réussi ou s'il y a eu une erreur. Le fonctionnement interne des syscalls est très détaillé ; je vous recommande de chercher des informations en ligne si vous voulez en savoir plus.

Vous pouvez en fait visualiser les appels système qu'un processus effectue avec la commande `strace`. La commande `strace` est utile pour déboguer l'exécution d'un programme.

```bash
strace ls
```

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Qu'est-ce qui est utilisé pour passer du mode utilisateur au mode kernel ?

## Quiz Answer

System call
