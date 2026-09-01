---
lesson_id: "process-niceness"
course_id: "processes"
lang: "fr"
order_index: 8
title: "Valeur nice"
description: "Découvrez comment les valeurs nice influencent le poids de planification du processeur pour les processus Linux ordinaires."
meta_title: "Valeur nice - Processus"
meta_description: "Découvrez la valeur nice sous Linux, son influence sur la priorité des processus et l’utilisation des commandes nice et renice."
meta_keywords: "nice Linux, valeur nice Linux, priorité processus, commande nice, commande renice, planification processeur"
---

Linux peut exécuter simultanément des threads sur plusieurs cœurs et partager dans le temps un cœur entre davantage de threads exécutables qu’il ne peut en exécuter à la fois. L’ordonnanceur effectue ces choix selon la politique de planification, la priorité, l’affinité et la charge. Une valeur nice constitue l’un des paramètres des politiques ordinaires de partage du temps.

## Interpréter les valeurs nice

La plage conventionnelle des valeurs nice va de `-20` à `19` :

- une valeur plus faible accorde à une tâche un poids de planification supérieur à celui de tâches comparables ;
- une valeur plus élevée la rend plus « aimable » en lui accordant un poids relatif inférieur ;
- la valeur par défaut est généralement `0`.

La valeur nice ne réserve pas un pourcentage du processeur et ne garantit pas une exécution immédiate. Son effet est surtout visible lorsque des tâches exécutables comparables se disputent le temps processeur. Les politiques temps réel, les cgroups, l’affinité du processeur, les attentes d’entrées-sorties et d’autres contrôles peuvent dominer le comportement observé.

:::single-choice{#process-niceness-lower-value} Sous une même politique de planification ordinaire, quelle valeur nice donne un poids relatif supérieur pour le processeur ?

::option[`10`]{#process-niceness-value-ten explanation="Une valeur positive est plus aimable et possède normalement un poids inférieur à zéro ou à une valeur négative."}
::option[`19`]{#process-niceness-value-nineteen explanation="Il s’agit de l’extrémité la plus aimable de la plage conventionnelle, dotée d’un poids relativement faible."}
::option[`-5`]{#process-niceness-value-minus-five .correct explanation="Les valeurs nice plus faibles correspondent à un poids relatif supérieur parmi les tâches ordinaires comparables."}
:::

## Afficher la valeur nice

Dans `top`, la colonne `NI` affiche la valeur nice. Vous pouvez également la demander à `ps` :

```bash
$ ps -o pid,ni,pri,stat,cmd -p 3245
```

`NI` est la valeur nice visible par l’utilisateur. Une colonne `PRI` ou semblable peut indiquer une priorité dérivée de l’ordonnanceur dont l’échelle varie selon l’outil et la classe de planification ; ne supposez donc pas que les deux colonnes sont interchangeables.

:::single-choice{#process-niceness-top-column} Quelle colonne de `top` affiche normalement la valeur nice ?

::option[`PID`]{#process-niceness-column-pid explanation="`PID` identifie un processus au lieu d’afficher son ajustement de planification."}
::option[`TTY`]{#process-niceness-column-tty explanation="`TTY` identifie une association avec un terminal de contrôle."}
::option[`NI`]{#process-niceness-column-ni .correct explanation="`NI` est l’abréviation conventionnelle de la valeur nice du processus ou du thread."}
:::

## Lancer une commande avec `nice`

Employez `nice` pour lancer une nouvelle commande avec une valeur ajustée :

```bash
$ nice -n 5 long-computation
```

La méthode exacte de demande de l’ajustement et la syntaxe acceptée peuvent être vérifiées dans le manuel local. Un utilisateur sans privilèges peut normalement rendre une commande plus aimable en augmentant sa valeur. Lui attribuer une valeur plus faible, et donc un poids de planification plus favorable, exige les privilèges ou les limites de ressources configurées appropriés.

:::single-choice{#process-niceness-nice-command} Que fait `nice -n 5 long-computation` ?

::option[La commande démarre avec la valeur nice 5, si cela est autorisé.]{#process-niceness-start-five .correct explanation="`nice` lance une nouvelle commande avec l’ajustement de planification demandé."}
::option[Elle attribue au PID 5 la valeur nice la plus faible possible.]{#process-niceness-pid-five explanation="L’opérande après `-n` est une valeur nice, et non un PID cible."}
::option[Elle garantit à la commande exactement cinq pour cent d’un processeur.]{#process-niceness-five-percent explanation="Les valeurs nice expriment un poids relatif et ne réservent pas de pourcentage fixe du processeur."}
:::

## Modifier un processus existant avec `renice`

Employez `renice` pour un processus déjà en cours d’exécution :

```bash
$ renice -n 10 -p 3245
```

Cette commande demande la valeur nice `10` pour le PID `3245`. Vérifiez d’abord la cible, car les PID peuvent être réutilisés, puis confirmez la valeur obtenue. Les permissions dépendent de la propriété, des privilèges, des limites de ressources et de la politique du système. L’augmentation de la valeur nice est généralement autorisée pour un processus que vous possédez ; l’annulation de ce changement peut ne pas l’être sans privilèges.

:::single-choice{#process-niceness-renice-purpose} Quel outil modifie la valeur nice d’un processus existant ?

::option[`nice`]{#process-niceness-tool-nice explanation="`nice` sert principalement à lancer une nouvelle commande avec une valeur ajustée."}
::option[`kill`]{#process-niceness-tool-kill explanation="`kill` envoie des signaux et ne constitue pas l’outil ordinaire de modification de la valeur nice."}
::option[`renice`]{#process-niceness-tool-renice .correct explanation="`renice` vise un PID, un groupe de processus ou un utilisateur existant selon ses options."}
:::

L’atelier [Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864) offre un environnement contrôlé pour afficher et modifier les valeurs nice. Comparez des tâches gourmandes en processeur qui se disputent les ressources plutôt que d’attendre une différence visible sur un système inactif.

## Résumé

Vous savez maintenant interpréter et ajuster la valeur nice sans la considérer comme une garantie de processeur.

1. Lire les valeurs nice plus faibles comme un poids de planification relatif supérieur.
2. Examiner `NI` séparément des champs de priorité dérivés.
3. Employer `nice` lors du lancement d’une commande.
4. Employer `renice` pour un processus existant et vérifié.
