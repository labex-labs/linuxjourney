---
lang: "fr"
title: "Signaux"
meta_description: "Découvrez les signaux Linux, leur but, les types courants comme SIGINT et SIGKILL, et comment les processus les gèrent. Comprenez les bases des signaux pour un meilleur contrôle de Linux."
meta_keywords: "signaux Linux, SIGKILL, SIGINT, communication de processus, tutoriel Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

Un signal est une notification envoyée à un processus indiquant que quelque chose s'est produit.

### Pourquoi avons-nous des signaux

Ce sont des interruptions logicielles et elles ont de nombreuses utilisations :

- Un utilisateur peut taper l'un des caractères spéciaux du terminal (Ctrl-C) ou (Ctrl-Z) pour tuer, interrompre ou suspendre des processus.
- Des problèmes matériels peuvent survenir, et le noyau souhaite en informer le processus.
- Des problèmes logiciels peuvent survenir, et le noyau souhaite en informer le processus.
- Ce sont essentiellement des moyens par lesquels les processus peuvent communiquer.

### Processus de signal

Lorsqu'un signal est généré par un événement, il est ensuite délivré à un processus ; il est considéré comme en attente jusqu'à ce qu'il soit délivré. Lorsque le processus est exécuté, le signal sera délivré. Cependant, les processus ont des masques de signal, et ils peuvent bloquer la livraison du signal si spécifié. Lorsqu'un signal est délivré, un processus peut faire une multitude de choses :

- Ignorer le signal.
- « Capter » le signal et exécuter une routine de gestion spécifique.
- Le processus peut être terminé, par opposition à l'appel système de sortie normal.
- Bloquer le signal, en fonction du masque de signal.

### Signaux courants

Chaque signal est défini par des entiers avec des noms symboliques qui sont sous la forme de SIGxxx. Certains des signaux les plus courants sont :

- SIGHUP ou HUP ou 1: Hangup
- SIGINT ou INT ou 2: Interrupt
- SIGKILL ou KILL ou 9: Kill
- SIGSEGV ou SEGV ou 11: Segmentation fault
- SIGTERM ou TERM ou 15: Software termination
- SIGSTOP ou STOP: Stop

Les numéros peuvent varier avec les signaux, ils sont donc généralement désignés par leurs noms.

Certains signaux sont non bloquables ; un exemple est le signal SIGKILL. Le signal KILL détruit le processus.

## Exercise

No exercises for this lesson.

## Quiz Question

Quel signal est non bloquable ?

## Quiz Answer

SIGKILL
