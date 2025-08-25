---
index: 3
lang: "fr"
title: "Appels système"
meta_title: "Appels système - Noyau"
meta_description: "Découvrez les appels système Linux (syscalls) et comment ils interagissent avec le noyau. Comprenez les modes utilisateur et noyau, et utilisez `strace` pour le débogage. Commencez votre parcours Linux !"
meta_keywords: "appels système Linux, syscalls, mode noyau, mode utilisateur, commande strace, tutoriel Linux, Linux débutant, guide Linux"
---

## Lesson Content

Vous vous souvenez de Britney dans la leçon précédente ? Disons que nous voulons la voir et prendre un verre ensemble. Comment passer de l'extérieur, au milieu de la foule, à son cercle le plus intime ? Nous utiliserions des appels système. Les appels système sont comme les passes VIP qui vous mènent à une porte dérobée secrète qui mène directement à Britney.

Les appels système (syscalls) permettent aux processus de l'espace utilisateur de demander au noyau de faire quelque chose pour nous. Le noyau met certains services à disposition via l'API d'appel système. Ces services nous permettent de lire ou d'écrire dans un fichier, de modifier l'utilisation de la mémoire, de modifier notre réseau, etc. Le nombre de services est fixe, vous ne pouvez donc pas ajouter d'appels système à tort et à travers. Votre système dispose déjà d'une table des appels système existants, et chaque appel système a un ID unique.

Je n'entrerai pas dans les détails des appels système, car cela vous obligerait à connaître un peu de C, mais les bases sont que lorsque vous appelez un programme comme `ls`, le code à l'intérieur de ce programme contient un wrapper d'appel système (donc pas encore l'appel système réel). À l'intérieur de ce wrapper, il invoque l'appel système qui exécutera un piège. Ce piège est ensuite intercepté par le gestionnaire d'appels système, qui fait ensuite référence à l'appel système dans la table des appels système. Disons que nous essayons d'appeler l'appel système `stat()` ; il est identifié par un ID de syscall, et le but de l'appel système `stat()` est d'interroger l'état d'un fichier. Maintenant, rappelez-vous, vous exécutiez le programme `ls` en mode non privilégié. Il voit donc que vous essayez de faire un syscall, il vous bascule alors en mode noyau. Là, il fait beaucoup de choses, mais surtout, il recherche votre numéro de syscall, le trouve dans une table basée sur l'ID de syscall, puis exécute la fonction que vous vouliez exécuter. Une fois terminé, il reviendra en mode utilisateur, et votre processus recevra un statut de retour s'il a réussi ou s'il a eu une erreur. Le fonctionnement interne des syscalls est très détaillé ; je vous recommande de chercher des informations en ligne si vous voulez en savoir plus.

Vous pouvez en fait visualiser les appels système qu'un processus effectue avec la commande `strace`. La commande `strace` est utile pour déboguer l'exécution d'un programme.

```bash
strace ls
```

## Exercise

La pratique rend parfait ! Bien que le fonctionnement interne des appels système soit complexe, comprendre comment les programmes de l'espace utilisateur interagissent avec le noyau est fondamental. La meilleure façon de saisir cette interaction est de s'exercer avec des commandes qui effectuent ces opérations sous-jacentes. Voici quelques laboratoires pratiques pour renforcer votre compréhension des interactions avec le système de fichiers, qui dépendent fortement des appels système :

1. **[Naviguer dans le système de fichiers sous Linux](https://labex.io/fr/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Pratiquez les commandes essentielles comme `ls`, `cd` et `pwd` pour vous déplacer et inspecter votre système de fichiers Linux, en interagissant directement avec les services du système de fichiers du noyau.
2. **[Gérer les fichiers et les répertoires sous Linux](https://labex.io/fr/labs/comptia-manage-files-and-directories-in-linux-590835)** - Apprenez à créer, supprimer, copier et déplacer des fichiers et des répertoires à l'aide de commandes comme `mkdir`, `rm`, `cp` et `mv`, qui impliquent toutes des appels système pour effectuer leurs actions.
3. **[Trouver des fichiers et des commandes sous Linux](https://labex.io/fr/labs/comptia-find-files-and-commands-in-linux-590834)** - Maîtrisez les techniques de localisation de fichiers et de commandes à l'aide de `find`, `whereis` et `which`, illustrant davantage comment les commandes utilisateur exploitent les services du noyau pour interagir avec le système de fichiers.

Ces laboratoires vous aideront à appliquer les concepts d'interaction avec le système de fichiers dans des scénarios réels et à renforcer votre confiance avec les opérations Linux fondamentales qui reposent implicitement sur les appels système.

## Quiz Question

Qu'est-ce qui est utilisé pour passer du mode utilisateur au mode noyau ?

## Quiz Answer

System call
