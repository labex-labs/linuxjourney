---
lesson_id: "process-details"
course_id: "processes"
lang: "fr"
order_index: 3
title: "Détails des processus"
description: "Découvrez quels états et ressources distinguent un processus en cours d’exécution d’un programme enregistré sur disque."
meta_title: "Détails des processus - Processus"
meta_description: "Explorez les bases des processus Linux, la manière dont le noyau les gère et l’attribution des ressources telles que le processeur et la mémoire."
meta_keywords: "processus Linux, détails processus, noyau, gestion processus, ressources système, ps aux, processeur, mémoire, tutoriel Linux"
---

Un programme est du code exécutable et des données enregistrés dans un fichier. Un processus est un contexte d’exécution actif : il comprend du code mappé, de la mémoire, des identifiants, des descripteurs de fichiers ouverts, l’état des signaux, des informations de planification et un ou plusieurs threads. Un même programme peut posséder de nombreuses instances de processus indépendantes.

## Instances de programme et PID

Par exemple, lancez `cat` sans opérande dans deux terminaux. Chaque instance attend une entrée et possède son propre identifiant de processus :

```bash
$ pgrep -a cat
18420 cat
18457 cat
```

Les deux processus exécutent le même programme, mais peuvent posséder des flux d’entrée, un contenu mémoire, des identifiants, des répertoires de travail et des durées de vie différents. Un PID désigne un processus actif à un instant donné et peut être réutilisé après la fin de ce processus.

:::single-choice{#process-details-program-versus-process}
Qu’est-ce qui distingue deux instances en cours d’exécution du même programme ?

::option[Le fichier exécutable doit être copié une fois pour chaque instance.]{#process-details-copied-executable explanation="Plusieurs processus peuvent mapper et partager les pages de code du même fichier exécutable sans dupliquer celui-ci."}
::option[Une seule instance peut posséder de la mémoire ou des fichiers ouverts.]{#process-details-one-instance-resources explanation="Chaque processus peut posséder ses propres mappages mémoire et sa table de descripteurs de fichiers."}
::option[Chaque instance possède son propre contexte de processus et son PID.]{#process-details-independent-context .correct explanation="Des exécutions distinctes reçoivent un état de processus actif différent, même lorsque leur code exécutable provient du même fichier."}
:::

## État suivi par le noyau

Le noyau conserve les informations nécessaires à la planification et au contrôle de chaque processus, notamment :

- les identifiants du processus et de son parent ;
- les identifiants utilisateur et groupe ;
- les mappages de mémoire virtuelle ;
- les descripteurs de fichiers ouverts et le répertoire actuel ;
- les dispositions et les signaux en attente ;
- la politique de planification, la priorité et l’état d’exécution ;
- les données comptables telles que le temps processeur.

Certaines ressources sous-jacentes peuvent être partagées. Des processus apparentés peuvent partager de la mémoire mappée, et les threads d’un même processus partagent un espace d’adressage et de nombreuses ressources du processus. Un processus fournit donc des frontières d’isolation sans que chaque octet ou objet du noyau soit nécessairement privé physiquement.

:::single-choice{#process-details-kernel-state}
Quel composant conserve l’état de planification et les identifiants des processus Linux ?

::option[Le noyau.]{#process-details-kernel .correct explanation="Le noyau suit l’état des processus et applique les règles de planification, de mémoire, de signaux et de contrôle d’accès."}
::option[Le répertoire du fichier exécutable.]{#process-details-directory explanation="Un répertoire conserve une association entre noms et inodes et ne planifie pas les processus actifs."}
::option[Uniquement l’émulateur de terminal de l’utilisateur.]{#process-details-terminal explanation="Un terminal peut interagir avec les processus, mais leur gestion reste une responsabilité du noyau."}
:::

## Planification du processeur et mémoire

Les threads exécutables se disputent le temps processeur. L’ordonnanceur du noyau choisit quel thread s’exécute sur quel processeur selon la classe de planification, la priorité, l’affinité du processeur, la charge et la politique. Cela ne garantit pas une part égale à chaque processus.

Chaque processus voit normalement un espace d’adressage virtuel. Le noyau et le matériel associent les adresses virtuelles à la mémoire physique ou à un autre stockage sous-jacent, appliquent des protections et peuvent partager des pages. Une valeur de mémoire dans `ps` ou `top` n’est donc pas automatiquement la quantité de mémoire vive physique unique attribuable à ce processus.

:::single-choice{#process-details-scheduler-role}
Que sélectionne l’ordonnanceur Linux ?

::option[Le thread exécutable qui s’exécute sur un processeur disponible.]{#process-details-runnable-thread .correct explanation="La politique de planification choisit parmi les contextes d’exécution prêts et leur attribue du temps processeur."}
::option[Le propriétaire de fichier enregistré lors du formatage d’un disque.]{#process-details-format-owner explanation="La propriété du système de fichiers est sans rapport avec la planification du processeur."}
::option[La ligne de commande qu’un utilisateur est autorisé à saisir.]{#process-details-command-entry explanation="L’ordonnanceur gère le temps d’exécution plutôt que la syntaxe des commandes interactives."}
:::

## Fin du processus et libération des ressources

Lorsqu’un processus se termine, le noyau libère la plupart de ses ressources privées, ferme les descripteurs restants et enregistre les informations de fin pour son parent. Une petite entrée dans la table des processus peut rester sous forme de zombie jusqu’à ce que le parent récupère l’état de sortie. « Le processus a fini de s’exécuter » et « toute trace a disparu de la table des processus » ne sont donc pas toujours simultanés.

:::single-choice{#process-details-exit-status}
Pourquoi un processus terminé peut-il rester brièvement sous forme de zombie ?

::option[Il exécute encore des instructions avec toute sa mémoire allouée.]{#process-details-zombie-running explanation="Un zombie a terminé son exécution et ne conserve plus un espace d’adressage actif normal."}
::option[Son parent n’a pas encore récupéré l’état de fin enregistré.]{#process-details-parent-wait .correct explanation="Le noyau conserve des informations minimales de sortie jusqu’à ce que le parent effectue une opération d’attente."}
::option[Son fichier exécutable est définitivement verrouillé par le noyau.]{#process-details-zombie-file-lock explanation="L’état zombie concerne la comptabilisation de la fin entre parent et enfant, et non un verrou permanent de l’exécutable."}
:::

Utilisez l’atelier [Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864) pour lancer plusieurs instances et comparer leurs PID et leurs états. L’atelier [Commande Linux `top`](https://labex.io/fr/labs/linux-linux-top-command-real-time-system-monitoring-388500) fournit une vue évolutive de la planification et des mesures de ressources.

## Résumé

Vous savez maintenant décrire un processus comme davantage qu’un fichier de programme.

1. Distinguer le code exécutable enregistré d’une instance de processus active.
2. Identifier l’état et les ressources suivis par le noyau.
3. Relier la planification aux threads exécutables plutôt qu’à des parts égales.
4. Reconnaître que l’état de sortie peut subsister jusqu’à ce que le parent le récupère.
