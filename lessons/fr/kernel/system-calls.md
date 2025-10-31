---
index: 3
lang: "fr"
title: "Appels Système"
meta_title: "Appels Système - Noyau"
meta_description: "Explorez les fondamentaux d'un appel système sous Linux. Apprenez comment les processus en espace utilisateur utilisent les appels système (syscalls) pour demander des services au noyau, changer de mode, et comment fonctionne la table d'appels système. Utilisez `strace` pour voir les appels système en action."
meta_keywords: "appel système linux, appels système, table syscall, mode noyau, mode utilisateur, strace, noyau linux, API syscall"
---

## Lesson Content

Imaginez que vous êtes à un grand concert. Pour passer de la zone du public général aux coulisses exclusives, vous ne pouvez pas simplement marcher. Vous avez besoin d'un laissez-passer spécial qui vous donne accès par une porte spécifique et gardée. Dans le monde de l'informatique, les **appels système** (system calls) sont ces laissez-passer spéciaux.

### Que sont les appels système ?

Les appels système, souvent abrégés en syscalls, fournissent un moyen aux processus en espace utilisateur de demander des services directement au noyau. Le noyau expose un ensemble de services via l'API des appels système. Ces services sont essentiels pour des opérations telles que la lecture ou l'écriture dans un fichier, la gestion de la mémoire ou le traitement des connexions réseau. Le nombre d'appels système disponibles est fixe ; vous ne pouvez pas en ajouter de nouveaux arbitrairement. Votre système maintient une `table d'appels système` (syscall table) où chaque appel système est enregistré avec un ID unique.

### Le mécanisme d'appel système sous Linux

Lorsque vous exécutez un programme comme `ls`, le code qu'il contient n'exécute pas directement la commande **system call linux**. Au lieu de cela, il utilise une fonction de bibliothèque, qui agit comme un enveloppeur (wrapper). Cette fonction enveloppe prépare les paramètres nécessaires, puis déclenche une interruption logicielle, ou un « piège » (trap).

Ce piège signale au processeur de passer du mode utilisateur non privilégié au mode noyau privilégié. Une fois en mode noyau, un gestionnaire d'appel système prend le relais. Il utilise l'ID unique pour rechercher la fonction demandée dans la `table d'appels système` et l'exécute. Par exemple, l'appel système `stat()`, utilisé pour interroger l'état d'un fichier, est trouvé et exécuté de cette manière. Une fois que le noyau a terminé la tâche, il bascule le contexte en mode utilisateur et renvoie un code d'état à votre processus, indiquant le succès ou une erreur.

### Visualiser les appels système avec strace

Vous pouvez observer les appels système effectués par un processus en temps réel à l'aide de la commande `strace`. Cet outil est incroyablement utile pour le débogage et pour comprendre comment un programme interagit avec le noyau.

Pour voir les appels système effectués par la commande `ls`, vous exécuteriez :

```bash
strace ls
```

Ceci affichera une liste détaillée de chaque appel système effectué par `ls` lors de son exécution.

## Exercise

La pratique rend parfait ! Bien que le fonctionnement interne des appels système soit complexe, comprendre comment les programmes en espace utilisateur interagissent avec le noyau est fondamental. La meilleure façon de saisir cette interaction est de s'exercer avec des commandes qui effectuent ces opérations sous-jacentes. Voici quelques laboratoires pratiques pour renforcer votre compréhension des interactions avec le système de fichiers, qui dépendent fortement des appels système :

1. **[Naviguer dans le système de fichiers sous Linux](https://labex.io/fr/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Entraînez-vous avec des commandes essentielles comme `ls`, `cd` et `pwd` pour vous déplacer et inspecter votre système de fichiers Linux, en vous engageant directement avec les services du système de fichiers du noyau.
2. **[Gérer les fichiers et les répertoires sous Linux](https://labex.io/fr/labs/comptia-manage-files-and-directories-in-linux-590835)** - Apprenez à créer, supprimer, copier et déplacer des fichiers et des répertoires à l'aide de commandes telles que `mkdir`, `rm`, `cp` et `mv`, qui impliquent toutes des appels système pour effectuer leurs actions.
3. **[Trouver des fichiers et des commandes sous Linux](https://labex.io/fr/labs/comptia-find-files-and-commands-in-linux-590834)** - Maîtrisez les techniques pour localiser des fichiers et des commandes à l'aide de `find`, `whereis` et `which`, illustrant davantage comment les commandes utilisateur tirent parti des services du noyau pour interagir avec le système de fichiers.

Ces laboratoires vous aideront à appliquer les concepts d'interaction avec le système de fichiers dans des scénarios réels et à renforcer votre confiance dans les opérations Linux fondamentales qui reposent implicitement sur les appels système.

## Quiz Question

What is used to switch from user mode to kernel mode? Please answer in English, using two words.

## Quiz Answer

System call
