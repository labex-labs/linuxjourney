---
index: 3
lang: "fr"
title: "Threads de Processus"
meta_title: "Threads de Processus - Utilisation des Processus"
meta_description: "Un guide sur les threads de processus Linux. Apprenez la différence entre les processus mono-thread et multi-thread et comment utiliser la commande ps pour afficher les threads."
meta_keywords: "threads Linux, threads de processus, ps afficher threads, ps m, multi-thread, mono-thread, processus léger, gestion des processus Linux"
---

## Lesson Content

### Que Sont les Threads de Processus ?

Vous avez peut-être entendu les termes mono-thread (single-threaded) et multi-thread (multi-threaded). Les threads sont des unités d'exécution au sein d'un processus et sont souvent appelés "processus légers" (lightweight processes). Alors que les processus fonctionnent avec leurs propres ressources système isolées, les threads au sein du même processus peuvent partager ces ressources, comme la mémoire. Ce modèle de partage de ressources rend la communication entre les threads beaucoup plus rapide et plus efficace que la communication entre des processus distincts.

### Mono-thread contre Multi-thread

Chaque processus possède au moins un thread. Un processus avec un seul thread est appelé mono-thread, tandis qu'un processus avec plus d'un est multi-thread.

Par exemple, lorsque vous utilisez un éditeur de texte moderne, il peut s'exécuter comme un seul processus. Cependant, au sein de ce processus, un thread pourrait gérer votre saisie au clavier, tandis qu'un autre thread s'exécute en arrière-plan pour effectuer la vérification orthographique ou l'enregistrement automatique. Cette exécution concurrente rend l'application plus réactive. L'utilisation de plusieurs threads est souvent plus efficace que le lancement de plusieurs processus pour des tâches connexes.

### Comment Afficher les Threads avec ps

Pour inspecter les processus en cours d'exécution et leurs threads, vous pouvez utiliser la commande `ps`. Bien que `ps` ait de nombreuses options, une façon courante d'**afficher les threads** est d'utiliser l'indicateur `m`.

```plaintext
pete@icebox:~$ ps m
  PID TTY      STAT   TIME COMMAND
 2207 pts/2    -      0:01 bash
    - -        Ss     0:01 -
 5252 pts/2    -      0:00 ps m
    - -        R+     0:00 -
```

### Interprétation du Résultat

Dans le résultat ci-dessus, les lignes avec un `PID` (ID de processus) représentent le processus principal. Les lignes situées directement en dessous, qui affichent un tiret (`-`) au lieu d'un `PID`, représentent les threads appartenant à ce processus. Dans cet exemple, les processus `bash` et `ps m` sont mono-thread, car chacun n'a qu'un seul thread principal listé.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des processus Linux et de leur gestion :

1. **[Gérer et Surveiller les Processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Dans ce laboratoire, vous apprendrez les compétences essentielles pour gérer et surveiller les processus sur un système Linux. Vous explorerez comment interagir avec les processus au premier plan et en arrière-plan, les inspecter avec `ps`, surveiller les ressources avec `top`, ajuster la priorité avec `renice` et les terminer avec `kill`.

Ce laboratoire vous aidera à appliquer les concepts de gestion des processus dans des scénarios réels et à renforcer votre confiance dans la surveillance de l'activité du système.

## Quiz Question

Vrai ou faux, tous les processus commencent par être mono-thread.

## Quiz Answer

True
