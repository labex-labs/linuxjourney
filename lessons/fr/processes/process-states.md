---
lesson_id: "process-states"
course_id: "processes"
lang: "fr"
order_index: 9
title: "États des processus"
description: "Découvrez comment interpréter les codes courants d’état des processus Linux dans les instantanés de `ps`."
meta_title: "États des processus - Processus"
meta_description: "Guide des états des processus Linux R, S, D, Z et T et de leur interprétation avec la commande ps."
meta_keywords: "états processus Linux, état processus Linux, commande ps, codes STAT, gestion processus"
---

Une tâche Linux passe d’un état d’exécution à l’autre lorsqu’elle s’exécute, attend, s’arrête et se termine. Le champ `STAT` de `ps` saisit un instant ; plusieurs observations sont donc plus utiles qu’une lettre isolée pour diagnostiquer un comportement.

```bash
$ ps -o pid,ppid,stat,wchan:24,cmd
```

Le premier caractère de `STAT` est l’état principal. Les caractères supplémentaires sont des modificateurs qui décrivent des propriétés telles que la direction d’une session ou l’appartenance au groupe de processus au premier plan. Consultez le manuel local de `ps` pour obtenir la liste complète.

## Exécution et sommeil interruptible

- `R` signifie en cours d’exécution ou exécutable. La tâche s’exécute sur un processeur ou attend du temps processeur dans une file d’exécution.
- `S` signifie sommeil interruptible. La tâche attend un événement et peut être réveillée par un signal ou un événement approprié.

Le sommeil est normal. Les programmes interactifs et les services passent une grande partie de leur temps à attendre une entrée, un minuteur, du trafic réseau, un verrou ou d’autres événements plutôt qu’à consommer continuellement du processeur.

:::single-choice{#process-states-runnable-code}
Que signifie l’état principal `R` ?

::option[En cours d’exécution sur un processeur ou prêt à s’exécuter.]{#process-states-r-running .correct explanation="`R` regroupe les tâches actuellement exécutées et celles qui attendent le processeur dans une file d’exécution."}
::option[Récupéré après que son parent a recueilli son état.]{#process-states-r-reaped explanation="Un processus entièrement récupéré n’apparaît plus comme une entrée normale de la table des processus."}
::option[En attente dans un sommeil non interruptible.]{#process-states-r-uninterruptible explanation="Le sommeil non interruptible est représenté par `D`."}
:::

:::single-choice{#process-states-interruptible-code}
Quel état principal représente le sommeil interruptible ?

::option[`D`]{#process-states-sleep-d explanation="`D` désigne le sommeil non interruptible."}
::option[`Z`]{#process-states-sleep-z explanation="`Z` désigne un enfant terminé dont l’état n’a pas été récupéré."}
::option[`S`]{#process-states-sleep-s .correct explanation="`S` est le code conventionnel de `ps` pour une attente interruptible."}
:::

## Sommeil non interruptible

`D` signifie sommeil non interruptible, généralement pendant que la tâche attend dans une opération du noyau telle que certaines entrées-sorties de stockage ou de système de fichiers réseau. La tâche ne réagit pas aux signaux ordinaires avant de quitter cette attente ; un signal peut rester en attente entre-temps.

Un bref état `D` peut être normal. Des tâches nombreuses ou durablement en `D` peuvent signaler des entrées-sorties lentes, indisponibles ou défaillantes, mais l’état seul n’en identifie pas la cause. Examinez le canal d’attente, les journaux du noyau, la santé du stockage et du réseau ainsi que le sous-système concerné avant de conclure.

:::single-choice{#process-states-uninterruptible-code}
Quel état principal désigne le sommeil non interruptible ?

::option[`T`]{#process-states-d-stopped explanation="`T` identifie une tâche arrêtée."}
::option[`D`]{#process-states-d-uninterruptible .correct explanation="`D` désigne une tâche en attente dans un sommeil non interruptible du noyau."}
::option[`R`]{#process-states-d-runnable explanation="`R` identifie une tâche en cours d’exécution ou exécutable."}
:::

## États arrêté et zombie

- `T` signifie normalement arrêté par une action de contrôle des tâches, telle que `SIGTSTP`, ou par `SIGSTOP`. Certains outils emploient un `t` minuscule pour un arrêt dû au traçage.
- `Z` signifie zombie : le processus s’est terminé, mais son parent n’a pas encore recueilli l’enregistrement de fin.

Reprenez un arrêt de contrôle des tâches avec `SIGCONT` lorsque cela convient. Un zombie ne peut être ni repris ni tué, car il ne s’exécute plus ; son parent ou un récupérateur adoptant doit le recueillir.

:::single-choice{#process-states-zombie-code}
Qu’identifie l’état principal `Z` ?

::option[Un processus terminé dont l’enregistrement de fin attend d’être récupéré.]{#process-states-z-zombie .correct explanation="Un zombie conserve un état minimal visible par le parent après la fin de son exécution."}
::option[Un processus suspendu par un signal du terminal.]{#process-states-z-terminal-stop explanation="Un arrêt de contrôle des tâches s’affiche normalement sous la forme `T`."}
::option[Un processus qui emploie actuellement tout un cœur de processeur.]{#process-states-z-cpu explanation="Une tâche active est représentée par `R`, tandis qu’un zombie n’exécute aucune instruction."}
:::

## Lire les états dans leur contexte

Les codes d’état sont des observations, pas des diagnostics. Associez-les au temps écoulé, à l’utilisation du processeur, aux canaux d’attente, aux relations parentales, aux journaux et à plusieurs échantillons. Une tâche peut changer d’état entre l’instant où le noyau le signale et celui où vous lisez l’écran.

L’atelier [Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864) fournit un environnement sûr pour observer les tâches au premier plan, endormies, arrêtées et terminées.

## Résumé

Vous savez maintenant interpréter les principaux états de processus les plus courants.

1. Lire `R` comme en cours d’exécution ou exécutable et `S` comme sommeil interruptible.
2. Analyser un état `D` persistant comme le symptôme d’une attente, et non comme un diagnostic.
3. Distinguer l’état arrêté `T` de l’état terminé et non récupéré `Z`.
4. Employer plusieurs observations et les indices environnants.
