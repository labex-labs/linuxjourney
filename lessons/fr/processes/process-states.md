---
index: 9
lang: "fr"
title: "États des processus"
meta_title: "États des processus - Processus"
meta_description: "Apprenez les états des processus Linux (R, S, D, Z, T) en utilisant `ps aux`. Comprenez les codes STAT courants et gérez les processus efficacement. Commencez votre parcours Linux !"
meta_keywords: "états des processus Linux, ps aux, gestion des processus, tutoriel Linux, Linux pour débutants, codes STAT, guide Linux"
---

## Lesson Content

Examinons à nouveau la commande `ps aux` :

```bash
ps aux
```

Dans la colonne STAT, vous verrez de nombreuses valeurs. Un processus Linux peut être dans plusieurs états différents. Les codes d'état les plus courants que vous verrez sont décrits ci-dessous :

- **R**: En cours d'exécution ou exécutable ; il attend juste que le CPU le traite.
- **S**: Sommeil interruptible ; en attente de la fin d'un événement, tel qu'une entrée du terminal.
- **D**: Sommeil ininterruptible ; processus qui ne peuvent pas être tués ou interrompus par un signal. Généralement, pour les faire disparaître, il faut redémarrer ou résoudre le problème.
- **Z**: Zombie ; nous avons discuté dans une leçon précédente que les zombies sont des processus terminés qui attendent que leurs statuts soient collectés.
- **T**: Arrêté ; un processus qui a été suspendu/arrêté.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion et des états des processus Linux :

1. **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Dans ce laboratoire, vous apprendrez les compétences essentielles pour gérer et surveiller les processus sur un système Linux. Vous explorerez comment interagir avec les processus de premier plan et d'arrière-plan, les inspecter avec `ps`, surveiller les ressources avec `top`, ajuster la priorité avec `renice` et les terminer avec `kill`.

Ce laboratoire vous aidera à appliquer les concepts des états de processus dans des scénarios réels et à renforcer votre confiance dans la gestion des processus Linux.

## Quiz Question

Quel code STAT est utilisé pour représenter un sommeil ininterruptible ?

## Quiz Answer

D
