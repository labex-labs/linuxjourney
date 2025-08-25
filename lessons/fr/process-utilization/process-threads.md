---
index: 3
lang: "fr"
title: "Threads de processus"
meta_title: "Threads de processus - Utilisation des processus"
meta_description: "Découvrez les threads de processus Linux, les concepts mono-thread et multi-thread, et comment les visualiser à l'aide de 'ps m'. Comprenez efficacement les processus légers !"
meta_keywords: "Threads Linux, threads de processus, commande ps m, multi-thread, mono-thread, processus Linux, Linux pour débutants, tutoriel Linux"
---

## Lesson Content

Vous avez peut-être entendu parler des termes processus mono-thread et multi-thread. Les threads sont très similaires aux processus, en ce sens qu'ils sont utilisés pour exécuter le même programme ; ils sont souvent appelés processus légers. Si un processus a un seul thread, il est mono-thread, et si un processus a plus d'un thread, il est multi-thread. Cependant, tous les processus ont au moins un thread.

Les processus fonctionnent avec leurs propres ressources système isolées ; cependant, les threads peuvent partager ces ressources entre eux facilement, ce qui leur facilite la communication. Parfois, il est plus efficace d'avoir une application multi-thread qu'une application multi-processus.

En gros, disons que vous ouvrez LibreOffice Writer et Chrome ; chacun est son propre processus distinct. Maintenant, vous allez dans Writer et commencez à éditer du texte. Lorsque vous éditez le texte, il est automatiquement enregistré. Ces deux « processus légers » parallèles d'enregistrement et d'édition sont des threads.

Pour afficher les threads de processus, vous pouvez utiliser :

```plaintext
pete@icebox:~$ ps m
  PID TTY      STAT   TIME COMMAND
 2207 pts/2    -      0:01 bash
    - -        Ss     0:01 -
 5252 pts/2    -      0:00 ps m
    - -        R+     0:00 -
```

Les processus sont indiqués par chaque PID, et sous les processus se trouvent leurs threads (indiqués par un `--`). Vous pouvez donc voir que les processus ci-dessus sont tous deux mono-thread.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des processus Linux et de leur gestion :

1. **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Dans ce laboratoire, vous apprendrez les compétences essentielles pour gérer et surveiller les processus sur un système Linux. Vous explorerez comment interagir avec les processus de premier plan et d'arrière-plan, les inspecter avec `ps`, surveiller les ressources avec `top`, ajuster la priorité avec `renice` et les terminer avec `kill`.

Ce laboratoire vous aidera à appliquer les concepts de gestion des processus dans des scénarios réels et à renforcer votre confiance dans la surveillance de l'activité du système.

## Quiz Question

Vrai ou faux, tous les processus commencent par être mono-thread.

## Quiz Answer

True
