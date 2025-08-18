---
lang: "fr"
title: "États des Processus"
meta_title: "États des Processus - Processus"
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
- **D**: Sommeil ininterruptible ; processus qui ne peuvent pas être tués ou interrompus par un signal. Généralement, pour les faire disparaître, vous devez redémarrer ou résoudre le problème.
- **Z**: Zombie ; nous avons discuté dans une leçon précédente que les zombies sont des processus terminés qui attendent que leurs statuts soient collectés.
- **T**: Arrêté ; un processus qui a été suspendu/arrêté.

## Exercise

Examinez les processus en cours d'exécution sur votre système et vérifiez leurs états de processus.

## Quiz Question

Quel code STAT est utilisé pour représenter un sommeil ininterruptible ?

## Quiz Answer

D
