---
lesson_id: "monitor-processes-ps-command"
course_id: "processes"
lang: "fr"
order_index: 1
title: "ps (processus)"
description: "Découvrez comment prendre des instantanés des processus avec `ps` et surveiller l’évolution de l’activité avec `top`."
meta_title: "ps (processus) - Processus"
meta_description: "Explorez la commande ps sous Linux, notamment ps -ef, pour afficher les processus, comprendre les PID et surveiller les tâches du système."
meta_keywords: "commande ps, ps -ef Linux, commande ps -ef, ps -e Linux, processus Linux, identifiant processus, PID, commande top"
---

Un processus est une instance en cours d’exécution d’un programme, accompagnée de sa mémoire, de ses identifiants, de ses ressources ouvertes et de son état d’exécution. Linux identifie chaque processus actif par un identifiant numérique, ou PID. Un PID est unique parmi les processus qui existent au même moment, mais le noyau peut le réutiliser après la fin d’un processus.

## Prendre un instantané élémentaire

Exécutez `ps` sans option pour obtenir un instantané sélectionné selon les valeurs par défaut de l’implémentation, généralement les processus associés à votre terminal et à votre utilisateur actuels :

```text
$ ps
    PID TTY          TIME CMD
  41230 pts/4    00:00:00 bash
  51224 pts/4    00:00:00 ps
```

Les champs courants comprennent :

- `PID` : identifiant du processus ;
- `TTY` : terminal de contrôle, ou `?` si aucun n’est associé ;
- `TIME` : temps processeur cumulé, et non durée réelle écoulée ;
- `CMD` : nom ou ligne de commande selon le format choisi.

Les colonnes exactes et les sélections par défaut varient selon les implémentations de `ps` et les environnements.

:::single-choice{#ps-command-pid-meaning}
Qu’identifie la colonne `PID` ?

::option[Le numéro du répertoire actuel du processus.]{#ps-command-pid-directory explanation="Un répertoire actuel est une référence du système de fichiers et n’est pas représenté par le PID."}
::option[Le temps processeur cumulé en secondes.]{#ps-command-pid-cpu explanation="L’utilisation du processeur apparaît dans un champ distinct tel que `TIME`."}
::option[L’identifiant de processus attribué par le noyau.]{#ps-command-pid-kernel .correct explanation="Le PID est l’identifiant numérique employé pour désigner un processus actif."}
:::

## Répertorier les processus avec les options de style BSD

Sous Linux, `ps` accepte plusieurs styles d’options. Les options de style BSD s’écrivent couramment sans tiret initial :

```bash
$ ps aux
```

Dans cette combinaison :

- `a` étend la sélection aux processus d’autres utilisateurs qui possèdent un terminal ;
- `x` inclut également les processus sans terminal de contrôle et élargit la sélection avec `a` ;
- `u` sélectionne un format orienté utilisateur avec des champs tels que `USER`, `%CPU`, `%MEM`, `VSZ` et `RSS`.

Comme les significations des options peuvent interagir, interprétez toute la combinaison au lieu de considérer chaque lettre comme une commande indépendante.

:::single-choice{#ps-command-aux-user-format}
Dans `ps aux`, quelle option demande le format de sortie orienté utilisateur ?

::option[`u`]{#ps-command-aux-u .correct explanation="L’option de style BSD `u` sélectionne un ensemble de colonnes orienté utilisateur."}
::option[`x`]{#ps-command-aux-x explanation="L’option `x` affecte la sélection des processus, notamment ceux qui ne possèdent pas de terminal de contrôle."}
::option[`a`]{#ps-command-aux-a explanation="L’option `a` étend la sélection au-delà des seuls processus du terminal de l’utilisateur actuel."}
:::

## Employer les options de style standard

La commande courante de style standard `ps -ef` écrit ses options avec un tiret initial :

```bash
$ ps -ef
```

- `-e` sélectionne chaque processus visible par l’appelant.
- `-f` demande une liste au format complet.

La sortie comprend couramment `UID`, `PID`, `PPID`, l’heure de démarrage et la commande. `PPID` est l’identifiant du processus parent. Cette liste n’est pas intrinsèquement hiérarchique ; employez une option telle que `--forest` lorsqu’elle est prise en charge, ou un outil dédié tel que `pstree`, lorsque la disposition parent-enfant importe.

:::single-choice{#ps-command-ef-selection}
Que demande `-e` dans `ps -ef` ?

::option[Une actualisation chaque seconde jusqu’à l’interruption.]{#ps-command-e-refresh explanation="`ps` produit un instantané ; l’actualisation continue appartient à des outils tels que `top`."}
::option[Une sélection contenant chaque processus visible par l’appelant.]{#ps-command-e-every .correct explanation="L’option de style standard `-e` élargit l’instantané à tous les processus sélectionnables."}
::option[Uniquement les processus dont la commande s’est terminée par une erreur.]{#ps-command-e-errors explanation="La sélection des processus ne dépend pas de l’état de sortie futur d’une commande."}
:::

## Surveiller l’activité au fil du temps

`ps` se termine après avoir produit un instantané. Employez `top` pour une vue interactive qui s’actualise périodiquement :

```bash
$ top
```

`top` aide à identifier l’évolution des consommateurs de processeur et de mémoire, mais ses valeurs sont des échantillons et peuvent fluctuer. Confirmez un problème supposé sur plusieurs observations et reliez les pourcentages au nombre de processeurs de la machine, à la comptabilisation de la mémoire et à la charge.

:::single-choice{#ps-command-snapshot-versus-top}
Quel outil présenté actualise périodiquement son affichage des processus par défaut ?

::option[`top`]{#ps-command-top-refresh .correct explanation="`top` est un moniteur interactif qui actualise son affichage à intervalles réguliers."}
::option[`ps -ef`]{#ps-command-ps-ef-snapshot explanation="Cette commande affiche un instantané complet des processus, puis se termine."}
::option[`ls -l`]{#ps-command-ls-files explanation="`ls -l` affiche les entrées du système de fichiers, et non un moniteur actif des processus."}
:::

Pour vous exercer, utilisez [Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864) afin de comparer les instantanés à un moniteur interactif, ou explorez le tri et le filtrage dans l’atelier [Commande Linux `top`](https://labex.io/fr/labs/linux-linux-top-command-real-time-system-monitoring-388500).

## Résumé

Vous savez maintenant choisir une vue des processus et interpréter ses identifiants élémentaires.

1. Considérer un PID comme un identifiant réutilisable d’un processus actuellement actif.
2. Employer `ps` seul pour un petit instantané par défaut.
3. Employer `ps aux` ou `ps -ef` pour des sélections plus larges et des colonnes plus riches.
4. Employer `top` lorsque les changements au fil du temps importent.
