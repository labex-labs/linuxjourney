---
lesson_id: "job-control"
course_id: "processes"
lang: "fr"
order_index: 11
title: "Contrôle des tâches"
description: "Découvrez comment un shell interactif gère les tâches au premier plan, en arrière-plan et arrêtées."
meta_title: "Contrôle des tâches - Processus"
meta_description: "Découvrez le contrôle des tâches Linux pour gérer les processus en arrière-plan avec les commandes jobs, bg, fg et kill."
meta_keywords: "contrôle tâches Linux, processus arrière-plan, commande jobs, commande bg, commande fg, commande kill, tutoriel Linux"
---

Les shells interactifs emploient le contrôle des tâches pour coordonner les pipelines au sein d’une session de terminal. Une tâche peut contenir un processus ou tout un pipeline, normalement rassemblé dans un groupe de processus afin que le terminal et le shell puissent agir sur lui comme une unité.

## Démarrer une tâche en arrière-plan

Ajoutez `&` pour démarrer un pipeline de manière asynchrone :

```bash
$ sleep 1000 &
[1] 18420
```

Le shell rend l’invite sans attendre la fin de la tâche. L’état en arrière-plan ne redirige pas automatiquement la sortie, ne détache pas le terminal de contrôle et ne permet pas à la tâche de survivre à la déconnexion. Redirigez explicitement l’entrée et la sortie si nécessaire, et employez un gestionnaire de services, un planificateur ou un multiplexeur de terminal pour les travaux qui doivent survivre au shell interactif.

Une tâche en arrière-plan qui tente de lire le terminal de contrôle est normalement arrêtée par `SIGTTIN`, car elle n’est pas le groupe de processus au premier plan du terminal.

:::single-choice{#job-control-ampersand-effect} Que demande un `&` final à un shell interactif ?

::option[Garantir que la tâche survit à la déconnexion et au redémarrage du système.]{#job-control-survive-restart explanation="L’exécution en arrière-plan ne fournit ni supervision durable ni persistance après redémarrage."}
::option[Exécuter le pipeline comme tâche en arrière-plan sans attendre avant l’invite suivante.]{#job-control-background-job .correct explanation="Le shell démarre la tâche de manière asynchrone et reste disponible pour d’autres commandes."}
::option[Ignorer la sortie standard et les erreurs de la tâche.]{#job-control-discard-output explanation="Sans redirection, une tâche en arrière-plan peut toujours écrire dans le terminal."}
:::

## Répertorier les tâches du shell

La commande intégrée `jobs` répertorie les tâches connues du shell actuel :

```text
$ jobs
[1]    Running    sleep 1000 &
[2]-   Running    sleep 1001 &
[3]+   Stopped    sleep 1002
```

Le nombre entre crochets est un identifiant de tâche du shell, et non un PID. Le préfixe `%` forme une spécification telle que `%1`. Le marqueur `+` désigne la tâche actuelle sélectionnée par de nombreuses commandes si aucun opérande n’est fourni ; `-` désigne la tâche précédente.

Comme la table des tâches appartient à un shell, celui d’un autre terminal ne peut normalement ni répertorier ni viser ces tâches avec ses propres commandes intégrées `jobs`, `fg` ou `bg`.

:::single-choice{#job-control-jobs-scope} Que répertorie la commande intégrée `jobs` ?

::option[Les tâches suivies par la session du shell actuel.]{#job-control-jobs-current-shell .correct explanation="Les identifiants et l’état des tâches sont conservés par le shell interactif qui a lancé ou adopté ces tâches."}
::option[Chaque processus actuellement visible sur le système.]{#job-control-jobs-all-processes explanation="Les outils tels que `ps` examinent les processus de tout le système ; la table des tâches du shell est plus étroite."}
::option[Uniquement les services lancés pendant le démarrage du système.]{#job-control-jobs-boot-services explanation="Les services du démarrage sont normalement supervisés par un gestionnaire de services, et non par la table des tâches du shell interactif."}
:::

## Arrêter et reprendre une tâche

Pendant qu’une tâche se trouve au premier plan, l’appui sur `Ctrl-Z` demande normalement au terminal d’envoyer `SIGTSTP` à son groupe de processus au premier plan. Le shell reprend le contrôle après l’arrêt de la tâche :

```text
$ sleep 1002
^Z
[3]+  Stopped    sleep 1002
```

Reprenez la tâche arrêtée actuelle en arrière-plan avec :

```bash
$ bg
```

`bg` envoie un signal de reprise et laisse la tâche hors du premier plan du terminal. Cette commande ne sert qu’à une tâche arrêtée ; une commande déjà en cours d’exécution en arrière-plan n’a pas besoin d’être reprise.

:::single-choice{#job-control-bg-purpose} Que fait `bg %3` à la tâche 3 arrêtée ?

::option[La commande déplace ses fichiers dans un répertoire nommé `bg`.]{#job-control-bg-files explanation="`bg` est une commande intégrée de contrôle des tâches et ne déplace pas d’objets du système de fichiers."}
::option[Elle la reprend comme tâche en arrière-plan.]{#job-control-bg-continue .correct explanation="Le shell reprend la tâche arrêtée sélectionnée sans lui attribuer le premier plan du terminal."}
::option[Elle la termine avec `SIGKILL`.]{#job-control-bg-kill explanation="La commande intégrée reprend la tâche au lieu de la terminer."}
:::

## Placer une tâche au premier plan

Employez `fg` avec une spécification de tâche pour en faire le groupe de processus au premier plan du terminal et l’attendre :

```bash
$ fg %1
```

Sans opérande, `fg` sélectionne normalement la tâche actuelle marquée par `+`. Une tâche arrêtée est reprise lorsqu’elle passe au premier plan.

:::single-choice{#job-control-fg-effect} Que fait `fg %1` ?

::option[Elle attribue le premier plan du terminal à la tâche 1 et l’attend.]{#job-control-fg-foreground .correct explanation="Le shell place la tâche sélectionnée au premier plan afin qu’elle puisse interagir avec le terminal."}
::option[Elle transforme la tâche 1 en PID 1.]{#job-control-fg-pid-one explanation="Un identifiant de tâche du shell ne remplace ni ne réécrit les identifiants de processus."}
::option[Elle lance une seconde copie de la tâche 1 en arrière-plan.]{#job-control-fg-copy explanation="`fg` agit sur la tâche existante au lieu d’en créer une copie."}
:::

## Envoyer un signal à une tâche

Les shells permettent à `kill` d’accepter une spécification de tâche :

```bash
$ kill -TERM %1
```

Cela envoie normalement le signal au groupe de processus de la tâche plutôt qu’à un seul membre du pipeline. Examinez d’abord la tâche sélectionnée et employez `SIGTERM` avant d’envisager une escalade forcée. Les spécifications de tâches appartiennent à la syntaxe du shell ; les scripts et les outils externes emploient plus couramment des PID ou des identifiants de groupes de processus vérifiés.

:::single-choice{#job-control-job-specification} Quel opérande désigne la tâche 1 du shell plutôt que le processus de PID 1 ?

::option[`1`]{#job-control-plain-one explanation="Un opérande numérique simple de `kill` est normalement interprété comme un PID."}
::option[`#1`]{#job-control-hash-one explanation="Le préfixe dièse n’est pas la syntaxe présentée pour un identifiant de tâche du shell."}
::option[`%1`]{#job-control-percent-one .correct explanation="Le préfixe pourcentage désigne une spécification de tâche du shell."}
:::

Entraînez-vous à ces opérations avec des commandes inoffensives telles que `sleep` dans l’atelier [Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864).

## Résumé

Vous savez maintenant déplacer délibérément les tâches entre les états contrôlés par le shell.

1. Employer `&` pour lancer une tâche en arrière-plan sans détachement automatique.
2. Employer `jobs` pour examiner la table des tâches du shell actuel.
3. Arrêter avec `Ctrl-Z` et reprendre en arrière-plan avec `bg`.
4. Ramener une tâche sélectionnée au premier plan avec `fg`.
5. Désigner les tâches du shell avec `%ID_TÂCHE` lors de l’envoi de signaux.
