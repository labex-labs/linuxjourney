---
index: 9
lang: "fr"
title: "États des Processus"
meta_title: "États des Processus Linux - Processus"
meta_description: "Guide complet sur les états des processus Linux. Découvrez les différents états (R, S, D, Z, T) et comment les interpréter avec la commande `ps`."
meta_keywords: "états processus linux, états des processus linux, état processus linux, états processus expliqués, commande ps, codes STAT, gestion des processus"
---

## Lesson Content

Lorsque vous inspectez les processus en cours d'exécution, par exemple avec la commande `ps aux`, vous remarquerez une colonne STAT. Comprendre les codes de cette colonne est essentiel pour maîtriser la gestion des processus. Chaque code représente un **état de processus Linux** spécifique.

```bash
ps aux
```

Un **état de processus sous Linux** fournit un instantané de ce que fait actuellement un processus. Est-il en train d'utiliser activement le CPU, d'attendre une entrée, ou s'est-il terminé ? Explorons les états les plus courants que vous rencontrerez.

### Décoder les codes d'état de processus courants

La colonne STAT révèle l'**état de processus Linux** actuel. Bien qu'il existe de nombreux états possibles, voici ceux que vous rencontrerez le plus souvent. Avoir ces **états de processus Linux expliqués** vous aidera à diagnostiquer le comportement du système.

- **R (Running ou Runnable)** : Un processus dans cet état est soit en cours d'exécution active sur un cœur de CPU, soit dans la file d'attente d'exécution, prêt à être exécuté dès qu'un cœur de CPU devient disponible.

- **S (Interruptible Sleep / Sommeil Interruptible)** : C'est l'un des **états de processus sous Linux** les plus courants. Le processus attend qu'un événement se termine, comme une entrée utilisateur depuis le terminal ou l'arrivée d'un paquet réseau. Il est « interruptible », ce qui signifie qu'il peut être réveillé par des signaux.

- **D (Uninterruptible Sleep / Sommeil Ininterruptible)** : Ce processus dort également, mais il est dans un état où il ne peut pas être interrompu par un signal. Ceci est généralement utilisé pendant de courtes périodes lors d'opérations d'E/S où interrompre le processus pourrait entraîner un état corrompu. Si un processus reste longtemps dans cet état, cela peut indiquer un problème matériel ou de pilote.

- **Z (Zombie)** : Un processus zombie a terminé son exécution, mais il conserve toujours une entrée dans la table des processus. Il attend que son processus parent lise son statut de sortie. Quelques zombies sont normaux, mais un grand nombre peut indiquer un bogue dans l'application parente.

- **T (Stopped / Arrêté)** : Un processus entre dans cet état lorsqu'il a été suspendu par un signal de contrôle de tâche (comme appuyer sur `Ctrl+Z`) ou parce qu'il est tracé par un débogueur. Il peut être repris avec le signal `SIGCONT`.

En comprenant ces **états de processus Linux** fondamentaux, vous pouvez acquérir une compréhension plus approfondie de l'activité de votre système et gérer plus efficacement les applications en cours d'exécution.

## Exercise

Appliquez vos connaissances avec une pratique concrète. Le laboratoire suivant vous aidera à renforcer votre compréhension de la gestion des processus Linux et de leurs états :

1. **[Gérer et Surveiller les Processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Dans ce laboratoire, vous apprendrez les compétences essentielles pour gérer et surveiller les processus sur un système Linux. Vous explorerez comment interagir avec les processus au premier plan et en arrière-plan, les inspecter avec `ps`, surveiller les ressources avec `top`, ajuster la priorité avec `renice` et les terminer avec `kill`.

Ce laboratoire vous aidera à appliquer les concepts des états de processus dans des scénarios réels et à renforcer votre confiance dans la gestion des processus Linux.

## Quiz Question

Quel code STAT est utilisé pour représenter un sommeil ininterruptible ? (Veuillez fournir la lettre anglaise majuscule unique pour le code d'état.)

## Quiz Answer

D
