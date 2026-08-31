---
lesson_id: "process-creation"
course_id: "processes"
lang: "fr"
order_index: 4
title: "Création des processus"
description: "Découvrez comment fork, exec, les PID et les relations parentales participent à la création des processus Linux."
meta_title: "Création des processus - Processus"
meta_description: "Explorez la création des processus sous Linux : appels système fork et execve, relations parent-enfant, PID, PPID et rôle du processus init."
meta_keywords: "création processus Linux, créer processus Linux, création processus système exploitation, fork, execve, PID, PPID, processus init"
---

Les processus Linux forment des relations parent-enfant. Un shell lance généralement une commande externe en créant un processus enfant et en faisant exécuter le programme demandé à cet enfant. L’explication classique sépare ce travail en opérations `fork` et `exec`.

## Créer un enfant avec `fork`

L’appel système `fork()` crée un processus enfant à partir du processus appelant. Le parent et l’enfant poursuivent à partir du point de retour de `fork`, mais reçoivent des valeurs de retour différentes et possèdent des PID différents.

L’enfant reçoit un état de processus logiquement distinct. Linux peut initialement partager les pages de mémoire physique au moyen de la copie à l’écriture, et ne copier une page que lorsqu’un processus la modifie. Les descripteurs de fichiers ouverts sont hérités et désignent les mêmes descriptions de fichiers ouvertes sous-jacentes ; certains éléments tels que les positions dans les fichiers peuvent donc rester partagés.

:::single-choice{#process-creation-fork-result}
Que crée un appel `fork()` réussi ?

::option[Uniquement un programme de remplacement dans le même processus.]{#process-creation-fork-replacement explanation="Le remplacement de l’image du programme actuel est le rôle d’une opération `exec`."}
::option[Un processus enfant doté d’un nouveau PID.]{#process-creation-fork-child .correct explanation="`fork()` établit un processus enfant distinct et une relation parent-enfant."}
::option[Une copie permanente et immédiate de chaque page de mémoire physique.]{#process-creation-fork-full-copy explanation="Linux emploie couramment la copie à l’écriture au lieu de dupliquer immédiatement toutes les pages physiques."}
:::

## Remplacer un programme avec `execve`

Un appel `execve()` charge un nouveau programme dans le processus appelant. S’il réussit, il remplace l’image du processus et ne revient pas à l’ancien programme. Le PID reste identique, car `execve()` ne crée pas de nouveau processus.

De nombreuses commandes de shell suivent donc un modèle fork-exec :

1. Le shell crée un enfant.
2. L’enfant prépare les redirections et d’autres éléments de l’état d’exécution.
3. L’enfant exécute le programme demandé.
4. Le shell attend ou continue selon que l’exécution se déroule au premier plan ou en arrière-plan.

Les bibliothèques et les applications peuvent exposer des interfaces de plus haut niveau telles que `posix_spawn()`, et Linux possède d’autres primitives telles que `clone()`. Le modèle fork-exec bien connu reste utile sans être la seule interface possible.

:::single-choice{#process-creation-exec-pid}
Que devient le PID d’un processus après un appel `execve()` réussi ?

::option[Il devient identique au PID du parent.]{#process-creation-exec-parent-pid explanation="Le parent et l’enfant conservent des identifiants de processus distincts."}
::option[Il reste identique tandis que l’image du programme est remplacée.]{#process-creation-exec-same-pid .correct explanation="`execve()` transforme le processus appelant au lieu d’en créer un autre."}
::option[Il est supprimé avant le démarrage du nouveau programme.]{#process-creation-exec-pid-removed explanation="Le processus existant continue sous son PID avec de nouveaux code, données, pile et état de programme associé."}
:::

## Examiner les identifiants du parent et de l’enfant

`PID` identifie le processus, tandis que `PPID` identifie son parent. Demandez explicitement ces champs :

```bash
$ ps -o pid,ppid,stat,cmd
```

Si un shell lance `ps`, le PID du shell apparaît normalement comme `PPID` de ce processus `ps`. Le moment de l’observation compte : les processus très courts peuvent se terminer avant qu’une observation distincte ne les saisisse.

:::single-choice{#process-creation-ppid}
Que représente `PPID` dans une liste de processus ?

::option[L’ancien PID précédemment attribué au processus.]{#process-creation-previous-pid explanation="Les PID peuvent être réutilisés, mais `PPID` ne conserve pas l’historique des identifiants."}
::option[L’identifiant de priorité de planification du processus.]{#process-creation-priority-id explanation="La priorité de planification est représentée par d’autres champs tels que la priorité ou la valeur nice."}
::option[L’identifiant du processus parent.]{#process-creation-parent-pid .correct explanation="PPID enregistre la relation parentale actuelle du processus."}
:::

## PID 1 et changement de parent

Le noyau démarre le premier processus de l’espace utilisateur avec le PID 1. Selon le système, il peut s’agir de `systemd`, d’une autre implémentation d’init ou d’un petit init dans un conteneur ou un espace de noms de PID. Le PID 1 démarre et supervise certaines parties de l’environnement utilisateur et possède des responsabilités particulières concernant les signaux et la récupération des orphelins.

Lorsqu’un parent se termine avant son enfant, celui-ci est rattaché à un sous-récupérateur approprié ou au processus init de son espace de noms de PID. Il ne doit pas nécessairement se terminer simplement parce que son parent d’origine a pris fin.

:::single-choice{#process-creation-pid-one}
Quelle affirmation sur le PID 1 est exacte ?

::option[Il doit toujours s’agir d’un programme dont l’exécutable se nomme exactement `init`.]{#process-creation-pid-one-name explanation="L’implémentation peut être `systemd`, un autre init ou un programme propre au conteneur."}
::option[Il est le parent qui a directement créé chaque processus actuellement en cours d’exécution.]{#process-creation-pid-one-direct explanation="La plupart des processus sont créés par de nombreuses générations de parents intermédiaires."}
::option[Il est le premier processus de son espace de noms de PID et possède des responsabilités semblables à celles d’init.]{#process-creation-pid-one-init .correct explanation="Le PID 1 constitue l’ancrage de la supervision et de la récupération des processus de l’espace utilisateur dans un espace de noms de PID."}
:::

L’atelier [Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864) permet d’observer les identifiants des parents et des enfants pendant l’exécution de commandes au premier plan et en arrière-plan.

## Résumé

Vous savez maintenant suivre la séquence classique de création des processus Linux.

1. Employer `fork()` pour créer un enfant doté d’un PID distinct.
2. Employer `execve()` pour remplacer l’image d’un processus sans modifier son PID.
3. Lire PID et PPID pour identifier les relations parent-enfant.
4. Reconnaître le PID 1 et les sous-récupérateurs comme destinations des enfants rattachés à un nouveau parent.
