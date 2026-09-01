---
lesson_id: "io-monitoring"
course_id: "process-utilization"
lang: "fr"
order_index: 5
title: "Surveillance des entrées-sorties"
description: "Découvrez comment employer les échantillons d’iostat pour analyser l’activité du processeur et des périphériques bloc."
meta_title: "Surveillance des entrées-sorties - Utilisation des processus"
meta_description: "Maîtrisez la surveillance des entrées-sorties Linux avec iostat et analysez les mesures du processeur et des disques pour comprendre les performances."
meta_keywords: "surveillance entrées-sorties, iostat, surveillance E/S Linux, utilisation processeur, utilisation disque, performances système, iowait, commandes Linux"
---

`iostat`, généralement fourni par le paquet `sysstat`, indique l’activité du processeur et des périphériques bloc. Associez des échantillons répétés à la latence de l’application : le débit ou l’utilisation seuls ne prouvent pas que le stockage provoque un problème visible par l’utilisateur.

## Recueillir des échantillons utiles

Affichez des statistiques étendues des périphériques à intervalles d’une seconde :

```bash
$ iostat -xz 1
```

Sur les implémentations courantes, le premier rapport contient les moyennes depuis le démarrage et les suivants couvrent chaque intervalle. L’option `-x` ajoute des champs étendus, tandis que `-z` masque les périphériques inactifs. Laissez passer plusieurs intervalles afin de saisir des périodes normales et problématiques.

:::single-choice{#iostat-first-report} Que représente couramment le premier rapport d’`iostat` ?

::option[Uniquement les opérations de la dernière seconde de la commande.]{#iostat-final-second explanation="Cela ne décrit pas le rapport cumulatif initial."}
::option[Les moyennes d’activité depuis le démarrage du système.]{#iostat-since-boot .correct explanation="Les rapports suivants concernent généralement chaque intervalle ; le premier doit donc être interprété séparément."}
::option[Une prévision de l’utilisation des périphériques pour demain.]{#iostat-forecast explanation="L’outil indique les statistiques observées, et non la demande future."}
:::

## Lire les champs du processeur

La section du processeur comprend couramment le temps utilisateur (`%user`), système (`%system`), d’inactivité (`%idle`), d’attente d’entrées-sorties (`%iowait`) et de vol par une machine virtuelle (`%steal`). L’attente d’entrées-sorties est le temps d’inactivité du processeur pendant lequel le système possède une requête d’entrée-sortie en attente ; ce n’est pas le pourcentage d’occupation d’un disque.

:::single-choice{#iostat-iowait-meaning} Que décrit `%iowait` ?

::option[Le pourcentage de la capacité du disque déjà rempli.]{#iostat-capacity explanation="La capacité du système de fichiers et le temps processeur sont des mesures différentes."}
::option[Le temps d’inactivité du processeur pendant qu’une requête d’entrée-sortie est en attente.]{#iostat-iowait-cpu .correct explanation="Il s’agit d’une catégorie de temps processeur qui ne peut identifier un périphérique à elle seule."}
::option[Le nombre de fichiers en attente de suppression.]{#iostat-delete-queue explanation="Ce champ ne représente pas un nombre de suppressions de fichiers."}
:::

## Lire les champs des périphériques

Les noms des champs varient selon la version de sysstat, mais les notions utiles comprennent :

- les opérations ou volumes lus et écrits par seconde, qui indiquent le rythme de la charge ;
- `await`, qui mesure la latence moyenne des requêtes, y compris le temps en file d’attente et de service ;
- les champs de taille moyenne de la file, qui indiquent les requêtes en attente ou en cours de traitement ;
- `%util`, qui indique le pourcentage du temps écoulé pendant lequel le périphérique a traité des entrées-sorties.

Une valeur `%util` élevée peut signaler la saturation d’un périphérique série simple, mais ne se traduit pas directement en capacité de performances pour un stockage parallèle, une grappe ou un périphérique virtuel. Comparez la latence à la conception du périphérique, au profil de la charge et à l’objectif de service.

:::single-choice{#iostat-await-purpose} Quel champ est le plus directement associé à la latence moyenne des requêtes d’entrée-sortie ?

::option[Le nom du périphérique.]{#iostat-device-name explanation="Le nom identifie le périphérique, mais ne mesure pas la durée des requêtes."}
::option[`await`]{#iostat-await .correct explanation="Await reflète le temps moyen des requêtes, y compris l’attente dans la file et le service."}
::option[`%idle`]{#iostat-idle explanation="Il s’agit d’un champ du processeur, et non de la latence des requêtes du périphérique."}
:::

## Mettre les indices en relation

Associez les noms des périphériques aux montages et aux périphériques sous-jacents avant de conclure :

```bash
$ lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS
$ findmnt
```

Mettez ensuite les intervalles d’`iostat` en relation avec le temps de réponse de l’application, les mesures de la base de données ou du système de fichiers et les entrées-sorties des processus. Device Mapper, RAID, les conteneurs et le stockage réseau peuvent ajouter des couches qui nécessitent leurs propres outils.

:::single-choice{#iostat-high-util-conclusion} Que faire après avoir observé une valeur `%util` élevée sur un périphérique ?

::option[Supposer que chaque système de fichiers manque d’espace libre.]{#iostat-assume-full explanation="Le temps d’occupation n’indique pas la capacité du système de fichiers."}
::option[Supprimer des fichiers avant d’identifier la charge montée.]{#iostat-delete-first explanation="La suppression modifie l’état et ne prouve pas un goulot d’étranglement des entrées-sorties."}
::option[Mettre la latence et le comportement de la charge en relation avec la conception du stockage.]{#iostat-correlate .correct explanation="Le parallélisme du périphérique et les objectifs de la charge déterminent si l’observation est nuisible."}
:::

## Résumé

Vous savez maintenant employer `iostat` comme indice dans une investigation sur les entrées-sorties.

1. Recueillir plusieurs intervalles de statistiques étendues.
2. Distinguer l’attente d’entrées-sorties du processeur du temps d’occupation du périphérique.
3. Interpréter ensemble la latence, la mise en file, le débit et l’utilisation.
4. Associer les périphériques aux charges et vérifier les conséquences sur l’application.
