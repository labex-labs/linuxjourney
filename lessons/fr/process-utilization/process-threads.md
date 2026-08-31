---
lesson_id: "process-threads"
course_id: "process-utilization"
lang: "fr"
order_index: 3
title: "Threads des processus"
description: "Découvrez comment les threads Linux partagent les ressources d’un processus et comment les examiner avec ps."
meta_title: "Threads des processus - Utilisation des processus"
meta_description: "Guide des threads de processus Linux : différence entre processus mono et multithreads et utilisation de ps pour afficher les threads."
meta_keywords: "threads Linux, threads processus, ps afficher threads, ps m, multithread, monothread, processus léger, gestion processus Linux"
---

Un thread est un flux d’exécution planifié au sein d’un processus. Chaque processus en cours d’exécution possède au moins un thread, et un processus multithread possède plusieurs flux qui peuvent progresser simultanément.

## Processus et threads

Les threads d’un même processus partagent des ressources telles que l’espace d’adressage virtuel et les descripteurs de fichiers ouverts. Chaque thread conserve néanmoins son propre état d’exécution, notamment ses registres et sa pile. Le partage rend la communication efficace, mais signifie aussi qu’une modification non synchronisée par un thread peut affecter les autres.

Les processus distincts possèdent normalement des espaces d’adressage distincts et communiquent au moyen de mécanismes explicites de communication interprocessus. Aucune des deux conceptions n’est automatiquement plus rapide ou plus sûre ; la charge de travail et l’implémentation déterminent le compromis.

:::single-choice{#threads-shared-resource}
Quelle ressource les threads d’un même processus partagent-ils normalement ?

::option[L’espace d’adressage virtuel du processus.]{#threads-shared-address-space .correct explanation="Les threads peuvent accéder à la même mémoire du processus, sous réserve de la synchronisation du programme."}
::option[Une installation distincte du noyau pour chaque thread.]{#threads-separate-kernel explanation="Tous les threads emploient le noyau du système en cours d’exécution."}
::option[Une racine de système de fichiers différente pour chaque thread.]{#threads-different-root explanation="Les threads partagent normalement le contexte de système de fichiers du processus au lieu de recevoir des racines distinctes."}
:::

## Identifiants des threads

Linux représente chaque thread comme une tâche planifiable dotée de son propre identifiant de thread. L’identifiant du chef du groupe de threads est couramment présenté comme l’identifiant du processus, tandis que tous les membres partagent un identifiant de groupe de threads. Les outils emploient des étiquettes telles que `PID`, `TID`, `LWP` et `SPID` ; vérifiez la définition de leurs champs plutôt que de supposer que chaque étiquette possède la même signification.

:::single-choice{#threads-own-scheduling-state}
Qu’est-ce que chaque thread conserve indépendamment ?

::option[La table complète des fichiers ouverts du processus.]{#threads-open-files-shared explanation="Les threads d’un processus partagent normalement les descripteurs de fichiers ouverts."}
::option[La base des utilisateurs de toute la machine.]{#threads-user-database explanation="Les bases de comptes ne constituent pas un état privé du thread."}
::option[Son état d’exécution et sa pile.]{#threads-stack-state .correct explanation="Un thread a besoin de son propre contexte d’exécution même lorsque les ressources du processus sont partagées."}
:::

## Répertorier les threads avec ps

Employez des champs de sortie explicites pour éviter les présentations par défaut ambiguës :

```bash
$ ps -eLo pid,tid,psr,stat,comm
```

Dans `ps` de procps, `-L` affiche les threads et `-e` sélectionne tous les processus. `pid` identifie le groupe de threads, `tid` un thread particulier, `psr` le processeur sur lequel il s’est exécuté en dernier et `stat` son état. Pour examiner un processus :

```bash
$ ps -L -p 1234 -o pid,tid,stat,pcpu,comm
```

Les listes de threads sont des instantanés. Un thread peut se terminer ou changer d’état immédiatement après.

:::single-choice{#threads-ps-one-process}
Quelle commande répertorie les threads appartenant au PID 1234 avec des champs explicites ?

::option[`ps -p 1234 -o pid,ppid,stat,pcpu,comm`]{#threads-process-only explanation="Cette sortie ne demande pas de ligne par thread."}
::option[`ps -L -p 1234 -o pid,tid,stat,pcpu,comm`]{#threads-ps-l .correct explanation="L’option `-L` demande les lignes des threads pour le processus sélectionné."}
::option[`ps -e -o pid,user,stat,pcpu,comm`]{#threads-all-processes explanation="Cette commande sélectionne les processus de tout le système sans afficher les identifiants de threads."}
:::

## Interpréter l’activité des threads

Une forte utilisation du processeur par un thread peut être masquée par une moyenne calculée pour tout le processus. Associez les échantillons d’utilisation par thread aux journaux de l’application, aux traces de pile et aux outils de profilage. N’attachez pas de débogueur et n’envoyez pas de signal aux tâches de production sans comprendre les conséquences sur les pauses, les permissions et le service.

:::single-choice{#threads-snapshot-limit}
Pourquoi une liste de threads produite par `ps` ne doit-elle pas être considérée comme un état permanent ?

::option[`ps` crée un thread de remplacement pour chaque ligne.]{#threads-ps-creates explanation="La commande observe les tâches ; elle ne clone pas chacune de celles qu’elle affiche."}
::option[Les identifiants de threads sont identiques sur chaque hôte Linux.]{#threads-identical-ids explanation="Les identifiants sont attribués au sein d’un système en cours d’exécution et ne sont pas universels."}
::option[Les threads peuvent changer d’état ou se terminer après l’instantané.]{#threads-change-after-snapshot .correct explanation="L’examen des processus observe un instant d’un système qui évolue continuellement."}
:::

## Résumé

Vous savez maintenant distinguer les ressources d’un processus de l’état d’exécution propre à chaque thread.

1. Reconnaître que chaque processus possède au moins un thread.
2. Identifier les ressources partagées par les threads d’un même processus.
3. Répertorier explicitement les identifiants des processus et des threads avec `ps -L`.
4. Considérer la sortie des threads comme un instantané et la mettre en relation avec d’autres indices.
