---
index: 6
lang: "fr"
title: "Signaux"
meta_title: "Signaux - Processus"
meta_description: "Explorez les fondamentaux des signaux Linux, un mécanisme clé pour la gestion des processus. Découvrez le fonctionnement des signaux de processus Linux tels que SIGTERM (signal 15 linux) et SIGKILL, et comprenez leurs codes de signal OS."
meta_keywords: "signaux linux, signaux processus linux, signal 15 linux, code signal os, SIGKILL, SIGTERM, SIGINT, gestion processus, tutoriel linux"
---

## Lesson Content

Sous Linux, un signal est une interruption logicielle envoyée à un processus pour l'informer qu'un événement important s'est produit. Comprendre les **signaux linux** est fondamental pour gérer efficacement les processus et le comportement du système.

### L'Objectif des Signaux

Les signaux servent de méthode principale pour la communication inter-processus (IPC). Ils ont de nombreuses utilisations :

- **Interaction Utilisateur** : Un utilisateur peut taper des caractères de terminal spéciaux, comme `Ctrl-C` (SIGINT) ou `Ctrl-Z` (SIGTSTP), pour interrompre ou suspendre les processus au premier plan.
- **Notifications du Noyau** : Le noyau peut envoyer des signaux à un processus pour l'informer de problèmes matériels ou logiciels, tels qu'un accès mémoire illégal (SIGSEGV).
- **Gestion des Processus** : Les administrateurs système et d'autres processus utilisent des signaux pour gérer le cycle de vie d'autres processus, comme demander une terminaison ou un rechargement de configuration.

### Le Cycle de Vie des Signaux

Lorsqu'un événement génère un signal, il est d'abord délivré à un processus cible. Le signal reste dans un état "en attente" jusqu'à ce que le noyau exécute le processus. Lorsque le processus est planifié, le signal est délivré. Cependant, les processus ont des masques de signaux, qui peuvent être configurés pour bloquer la délivrance de signaux spécifiques.

Lorsqu'un signal est délivré, le processus peut prendre l'une des actions suivantes :

- **Ignorer le signal** : Le processus écarte simplement le signal et continue son exécution.
- **Intercepter le signal** : Le processus exécute une fonction personnalisée appelée gestionnaire de signal pour répondre à l'événement.
- **Exécuter l'action par défaut** : S'il n'est ni intercepté ni ignoré, l'action par défaut est effectuée. Pour de nombreux signaux, cela signifie terminer le processus.
- **Bloquer le signal** : Si le signal est dans le masque de signaux du processus, il reste en attente jusqu'à ce qu'il soit débloqué.

### Signaux de Processus Linux Courants

Chaque signal est défini par un entier, mais ils sont presque toujours désignés par leurs noms symboliques (le **code sig os**), qui commencent par `SIG`. Bien que les nombres puissent varier légèrement selon les architectures, les noms sont cohérents. Voici quelques-uns des **signaux de processus linux** les plus courants :

- **SIGHUP (1)** : Raccrochage (Hangup). Souvent utilisé pour demander à un démon de recharger sa configuration.
- **SIGINT (2)** : Interruption. Envoyé par `Ctrl-C`. C'est une demande de terminaison du processus.
- **SIGKILL (9)** : Tuer (Kill). C'est une terminaison immédiate et forcée. Le processus ne peut pas intercepter, ignorer ou bloquer ce signal.
- **SIGSEGV (11)** : Erreur de Segmentation. Indique que le processus a effectué une référence mémoire invalide.
- **SIGTERM (15)** : Terminaison. C'est la manière standard et polie de demander à un processus de se terminer. C'est le signal par défaut envoyé par la commande `kill`. Un processus peut intercepter ce signal pour effectuer un nettoyage avant de s'arrêter. On l'appelle souvent **signal 15 linux**.
- **SIGSTOP** : Arrêt. Met le processus en pause. Comme SIGKILL, il ne peut être ni intercepté ni ignoré.

La différence clé entre `SIGTERM` (**signal linux 15**) et `SIGKILL` est que `SIGTERM` est une requête qui peut être gérée, tandis que `SIGKILL` est une commande qui détruit le processus immédiatement.

## Exercise

La pratique rend parfait ! Voici un laboratoire pratique pour renforcer votre compréhension des processus et de la manière dont les signaux sont utilisés pour interagir avec eux :

1. **[Gérer et Surveiller les Processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Dans ce laboratoire, vous apprendrez les compétences essentielles pour gérer et surveiller les processus sur un système Linux. Vous explorerez comment interagir avec les processus au premier plan et en arrière-plan, les inspecter avec `ps`, surveiller les ressources avec `top`, ajuster la priorité avec `renice`, et les terminer avec `kill`. La terminaison des processus avec `kill` est une application directe de l'envoi de signaux.

Ce laboratoire vous aidera à appliquer les concepts de gestion des processus et l'utilisation sous-jacente des signaux dans des scénarios réels et à renforcer votre confiance dans l'administration système Linux.

## Quiz Question

Quel signal ne peut pas être bloqué ? Veuillez répondre en anglais, en utilisant le nom exact du signal et en faisant attention à la casse.

## Quiz Answer

SIGKILL
