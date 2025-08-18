---
lang: "fr"
title: "Création de processus"
meta_title: "Création de processus - Processus"
meta_description: "Découvrez la création de processus Linux, le fork et les processus parent/enfant. Comprenez le PID, le PPID et le processus init. Obtenez un guide pour débutants sur la gestion des processus Linux."
meta_keywords: "création de processus Linux, fork, PID, PPID, processus init, processus Linux, débutant, tutoriel, guide"
---

## Lesson Content

Encore une fois, cette leçon et la suivante sont purement informatives pour vous permettre de voir ce qui se passe sous le capot. N'hésitez pas à y revenir une fois que vous aurez un peu plus travaillé avec les processus.

Lorsqu'un nouveau processus est créé, un processus existant se clone essentiellement en utilisant ce qu'on appelle l'appel système `fork` (les appels système seront abordés beaucoup plus tard). L'appel système `fork` crée un processus enfant presque identique. Ce processus enfant prend un nouvel identifiant de processus (PID), et le processus original devient son processus parent et a ce qu'on appelle un identifiant de processus parent **PPID**. Ensuite, le processus enfant peut soit continuer à utiliser le même programme que son parent utilisait auparavant, soit, plus souvent, utiliser l'appel système `execve` pour lancer un nouveau programme. Cet appel système détruit la gestion de la mémoire que le noyau a mise en place pour ce processus et en configure de nouvelles pour le nouveau programme.

Nous pouvons le voir en action :

```bash
ps l
```

L'option `l` nous donne un « format long » ou une vue encore plus détaillée de nos processus en cours d'exécution. Vous verrez une colonne intitulée **PPID** ; c'est l'ID parent. Regardez maintenant votre terminal ; vous verrez un processus en cours d'exécution qui est votre shell. Ainsi, sur mon système, j'ai un processus `bash` en cours d'exécution. Maintenant, rappelez-vous que lorsque vous avez exécuté la commande `ps l`, vous l'exécutiez à partir du processus qui exécutait `bash`. Vous verrez que le **PID** du shell `bash` est le **PPID** de la commande `ps l`.

Donc, si chaque processus doit avoir un parent et qu'ils ne sont que des forks les uns des autres, il doit y avoir une mère de tous les processus, n'est-ce pas ? Vous avez raison. Lorsque le système démarre, le noyau crée un processus appelé **init** ; il a un PID de 1. Le processus `init` ne peut pas être terminé à moins que le système ne s'arrête. Il s'exécute avec les privilèges root et exécute de nombreux processus qui maintiennent le système en marche. Nous examinerons de plus près `init` dans le cours sur le démarrage du système ; pour l'instant, sachez simplement que c'est le processus qui engendre tous les autres processus.

## Exercise

Examinez vos processus en cours d'exécution. Pouvez-vous voir quels autres processus ont des parents ?

## Quiz Question

Quel appel système crée un nouveau processus ?

## Quiz Answer

fork
