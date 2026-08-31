---
lesson_id: "memory-monitoring"
course_id: "process-utilization"
lang: "fr"
order_index: 6
title: "Surveillance de la mémoire"
description: "Découvrez comment interpréter les échantillons de vmstat relatifs à la mémoire, la pagination, les processus, les entrées-sorties et le processeur."
meta_title: "Surveillance de la mémoire - Utilisation des processus"
meta_description: "Maîtrisez la surveillance de la mémoire Linux avec vmstat et analysez les mesures de performances du système."
meta_keywords: "surveillance mémoire, utilisation mémoire, vmstat, mémoire Linux, performances système, tutoriel Linux"
---

Linux emploie intentionnellement la mémoire autrement inactive pour les caches ; une faible valeur `free` ne prouve donc pas à elle seule une pression mémoire. `vmstat` aide à relier la mémoire aux tâches exécutables, à la pagination, aux entrées-sorties et à l’activité du processeur.

## Échantillonner avec vmstat

Recueillez un échantillon par seconde :

```bash
$ vmstat 1
```

La première ligne de données indique généralement les moyennes depuis le démarrage ; les lignes suivantes couvrent chaque intervalle. Arrêtez avec `Ctrl-C` après avoir enregistré une période représentative. Les unités et les champs disponibles varient ; consultez `vmstat --unit` et le manuel local.

:::single-choice{#vmstat-interval-rows}
Quelles lignes conviennent le mieux à l’observation des changements seconde par seconde avec `vmstat 1` ?

::option[Les lignes qui suivent le rapport initial.]{#vmstat-later-rows .correct explanation="Les lignes suivantes décrivent chaque intervalle demandé plutôt que toute la période cumulée."}
::option[Uniquement les en-têtes au-dessus de la première ligne de données.]{#vmstat-headings explanation="Les en-têtes définissent les champs, mais ne contiennent aucun échantillon d’activité."}
::option[Uniquement une ligne copiée depuis un autre hôte.]{#vmstat-other-host explanation="Un autre système ne représente pas la charge de travail actuelle."}
:::

## Processus et mémoire

Les champs courants des processus sont `r`, pour les tâches exécutables, et `b`, pour les tâches bloquées en sommeil non interruptible. Les champs de mémoire comprennent l’espace d’échange utilisé (`swpd`), la mémoire inactive (`free`), les tampons (`buff`) et le cache (`cache`). Il s’agit de valeurs pour tout le système, et non de la consommation de chaque processus.

Pour une vue plus simple de la mémoire actuellement disponible, comparez avec :

```bash
$ free -h
```

L’estimation `available` est généralement plus utile que `free` seule, car le cache récupérable peut satisfaire de nouvelles allocations.

:::single-choice{#vmstat-free-memory}
Pourquoi une faible valeur `free` peut-elle être normale sous Linux ?

::option[Cette valeur exclut toujours toute la mémoire vive physique.]{#vmstat-excludes-ram explanation="Il s’agit d’un champ de mémoire, même si son unité exacte doit être vérifiée."}
::option[Le noyau peut employer la mémoire inactive pour des caches récupérables.]{#vmstat-reclaimable-cache .correct explanation="La mémoire mise en cache peut souvent être récupérée lorsque les applications en ont besoin."}
::option[Une faible mémoire libre prouve que le processeur est éteint.]{#vmstat-cpu-off explanation="L’allocation de mémoire et l’état d’alimentation du processeur sont sans rapport."}
:::

## Pagination et entrées-sorties

`si` et `so` indiquent les débits d’entrée et de sortie de l’espace d’échange. Une pagination soutenue associée à une latence et à une activité de récupération de mémoire peut signaler une pression, mais une utilisation non nulle de l’espace d’échange (`swpd`) ne prouve pas à elle seule un problème actuel. `bi` et `bo` indiquent les débits d’entrée et de sortie de blocs et ne se limitent pas au trafic d’échange.

:::single-choice{#vmstat-swap-pressure}
Quel indice étaye le mieux un diagnostic de pression mémoire actuelle ?

::option[Une valeur `swpd` non nulle sans aucune autre observation.]{#vmstat-swpd-alone explanation="Des pages peuvent rester dans l’espace d’échange après une pression passée ; la quantité seule ne suffit donc pas."}
::option[Une pagination soutenue corrélée à la récupération de mémoire et à la latence de la charge.]{#vmstat-correlated-pressure .correct explanation="Des indices répétés et corrélés relient le comportement de la mémoire aux conséquences actuelles."}
::option[Le nom de l’hôte affiché lors de la connexion.]{#vmstat-hostname explanation="Le nom d’hôte ne mesure ni la récupération de mémoire ni la pagination."}
:::

## Activité du processeur et du système

Les colonnes du processeur comprennent couramment les pourcentages utilisateur (`us`), système (`sy`), inactif (`id`), d’attente d’entrées-sorties (`wa`) et de vol (`st`). Les colonnes système comprennent les interruptions (`in`) et les changements de contexte (`cs`) par seconde. Interprétez les pics par rapport à une référence ; un taux élevé de changements de contexte peut être normal pour certaines charges.

:::single-choice{#vmstat-r-column}
Que représente le champ de processus `r` ?

::option[Les systèmes de fichiers montés en lecture seule.]{#vmstat-readonly explanation="Les options de montage ne sont pas représentées par ce champ de processus."}
::option[Les utilisateurs distants possédant un shell actif.]{#vmstat-remote-users explanation="Les sessions de connexion sont indiquées par d’autres outils."}
::option[Les tâches exécutables ou en attente du processeur.]{#vmstat-runnable .correct explanation="La comparaison de ce nombre à la capacité du processeur peut aider à identifier une demande de calcul."}
:::

## Résumé

Vous savez maintenant interpréter `vmstat` comme une vue du système corrélée dans le temps.

1. Distinguer le rapport cumulatif initial des échantillons par intervalle.
2. Considérer le cache comme de la mémoire potentiellement récupérable.
3. Mettre la pagination en relation avec la récupération et les conséquences sur l’application.
4. Lire ensemble les champs des processus, des entrées-sorties, du système et du processeur.
