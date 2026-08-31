---
lesson_id: "controlling-terminal"
course_id: "processes"
lang: "fr"
order_index: 2
title: "Terminal de contrôle"
description: "Découvrez comment les terminaux de contrôle relient les sessions aux entrées interactives, aux signaux et au contrôle des tâches du shell."
meta_title: "Terminal de contrôle - Processus"
meta_description: "Explorez le terminal de contrôle sous Linux, les différences entre TTY et PTS et la colonne TTY de ps pour les processus sans terminal."
meta_keywords: "terminal de contrôle, ps tty, définition tty, utiliser ps, TTY, PTS, terminal Linux, processus démon, processus Linux"
---

Une session de connexion interactive peut posséder un terminal de contrôle : un périphérique terminal associé à la session et employé par le noyau pour les signaux générés par le terminal et le contrôle des tâches. Le champ `TTY` des listes de processus aide à identifier cette association.

## Terminaux et pseudo-terminaux

Le nom TTY vient des anciens télétypes. Sous Linux moderne, les interfaces de terminal sont des abstractions de périphériques et pas nécessairement du matériel physique.

Une console virtuelle du système peut porter un nom tel que `tty1`. Les raccourcis du bureau qui permettent de changer de console varient selon la distribution et ne doivent pas être supposés. Un émulateur de terminal, une connexion distante ou un multiplexeur emploie couramment une paire de pseudo-terminaux, dont le côté interactif porte un nom tel que `pts/3`.

Affichez le terminal relié à l’entrée standard de la commande actuelle avec :

```bash
$ tty
/dev/pts/3
```

Ce résultat est lié à la notion plus large de terminal de contrôle, mais ne lui est pas identique. Un processus peut rediriger son entrée ou sa sortie standard tout en restant dans une session qui possède un terminal de contrôle.

:::single-choice{#controlling-terminal-pts-meaning}
Qu’identifie généralement un nom tel que `pts/3` ?

::option[Un identifiant de processus attribué au troisième shell.]{#controlling-terminal-pts-pid explanation="Un PID est une métadonnée numérique du processus et ne s’écrit pas comme un nom de périphérique `pts/N`."}
::option[Un périphérique pseudo-terminal employé par une session interactive.]{#controlling-terminal-pts-device .correct explanation="Les entrées de `/dev/pts` sont des périphériques esclaves de pseudo-terminaux couramment employés par les émulateurs et les sessions distantes."}
::option[Une partition de système de fichiers qui contient les programmes de terminal.]{#controlling-terminal-pts-partition explanation="Ce nom identifie une interface de terminal, et non une partition de stockage."}
:::

## Sessions, groupes de processus et contrôle des tâches

Un terminal de contrôle appartient à une session, et pas seulement à la commande qui a ouvert une fenêtre. Dans cette session, le terminal suit un groupe de processus au premier plan. Le shell place un pipeline au premier plan dans ce groupe afin qu’il puisse lire l’entrée et recevoir les signaux produits par le terminal.

Par exemple, l’appui sur `Ctrl-C` demande normalement au pilote du terminal d’envoyer `SIGINT` au groupe de processus au premier plan. Un groupe en arrière-plan qui essaie de lire le terminal peut recevoir `SIGTTIN`. Ces règles permettent au shell de coordonner les tâches au premier plan et en arrière-plan.

:::single-choice{#controlling-terminal-ctrl-c-target}
À quels processus un terminal adresse-t-il normalement le signal produit par `Ctrl-C` ?

::option[À chaque processus appartenant à l’utilisateur actuel.]{#controlling-terminal-ctrl-c-user explanation="Les signaux du terminal visent le groupe de processus au premier plan, et non tous les processus d’un utilisateur."}
::option[Uniquement au shell de connexion, quelle que soit la tâche au premier plan.]{#controlling-terminal-ctrl-c-shell explanation="Lorsqu’une autre tâche est au premier plan, son groupe constitue la cible normale du signal."}
::option[Au groupe de processus au premier plan du terminal.]{#controlling-terminal-ctrl-c-foreground .correct explanation="Le pilote du terminal envoie `SIGINT` au groupe de processus actuellement au premier plan."}
:::

## Lire la colonne `TTY`

Demandez explicitement certains champs des processus lorsque vous souhaitez une vue stable :

```bash
$ ps -o pid,tty,stat,cmd
```

Un nom de terminal tel que `pts/3` identifie le terminal de contrôle enregistré pour ce processus. Un point d’interrogation (`?`) signifie normalement que le processus ne possède aucun terminal de contrôle.

De nombreux processus de services n’en possèdent pas, car un gestionnaire de services les démarre indépendamment d’une session de connexion interactive. Cependant, l’absence de TTY ne prouve pas à elle seule qu’un processus est un démon, et une tâche de shell en arrière-plan peut toujours posséder un terminal de contrôle.

:::single-choice{#controlling-terminal-question-mark}
Que signifie normalement `?` dans la colonne `TTY` de `ps` ?

::option[Le processus ne possède aucun terminal de contrôle.]{#controlling-terminal-no-tty .correct explanation="Le point d’interrogation est l’affichage conventionnel lorsqu’aucun terminal de contrôle n’est associé au processus."}
::option[Le terminal du processus ne peut pas être lu parce qu’il est occupé.]{#controlling-terminal-busy-tty explanation="Ce marqueur représente l’absence d’un terminal de contrôle, et non une contention temporaire du périphérique."}
::option[Le processus est toujours un thread du noyau.]{#controlling-terminal-kernel-only explanation="Les threads du noyau manquent souvent de terminal, mais de nombreux services de l’espace utilisateur aussi."}
:::

## Fermeture du terminal et raccrochage

Lorsqu’une connexion de terminal disparaît, le noyau ou le logiciel du terminal ou de la session peut envoyer `SIGHUP` aux processus associés. Un processus peut se terminer, intercepter le signal, l’ignorer ou avoir déjà été configuré pour lui survivre. Des fonctions du shell telles que `disown`, des utilitaires tels que `nohup`, les multiplexeurs et les gestionnaires de services influencent tous le cycle de vie.

La fermeture d’un terminal ne garantit donc pas que chaque commande lancée depuis celui-ci se termine. Examinez la session du processus, sa gestion des signaux, ses redirections et son superviseur lorsque sa persistance importe.

:::single-choice{#controlling-terminal-close-effect}
Pourquoi est-il inexact d’affirmer que la fermeture d’un terminal termine toujours chaque processus lancé depuis celui-ci ?

::option[Les terminaux Linux ne produisent jamais de signal à leur fermeture.]{#controlling-terminal-never-signals explanation="Le signal de raccrochage est un comportement réel des terminaux et des sessions, même s’il n’entraîne pas nécessairement la terminaison."}
::option[Seuls les processus dont le PID est numérique peuvent recevoir un raccrochage.]{#controlling-terminal-pid-hangup explanation="Tous les processus ordinaires possèdent un PID numérique ; ce fait ne détermine pas leur survie au terminal."}
::option[Les processus peuvent gérer ou éviter le raccrochage et être administrés indépendamment.]{#controlling-terminal-hangup-handling .correct explanation="La disposition du signal, le comportement du shell, les multiplexeurs et les superviseurs peuvent permettre au processus de continuer après la fermeture du terminal."}
:::

L’atelier [Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864) fournit un environnement sûr pour comparer les tâches au premier plan et en arrière-plan ainsi que leurs champs `TTY`.

## Résumé

Vous savez maintenant relier un terminal de contrôle à la gestion interactive des processus.

1. Distinguer les terminaux virtuels des pseudo-terminaux.
2. Relier les signaux du terminal au groupe de processus au premier plan.
3. Interpréter les noms de terminaux et `?` dans la sortie de `ps`.
4. Considérer la fermeture du terminal comme une signalisation, et non une garantie de terminaison du processus.
