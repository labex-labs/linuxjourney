---
lesson_id: "tracking-processes-top"
course_id: "process-utilization"
lang: "fr"
order_index: 1
title: "Suivre les processus : top"
description: "Découvrez comment employer top pour interpréter la charge du système, le processeur, la mémoire et l’activité de chaque processus."
meta_title: "Suivre les processus : top - Utilisation des processus"
meta_description: "Maîtrisez la commande top sous Linux pour surveiller les ressources, suivre les processus et comprendre des mesures telles que VIRT et RES."
meta_keywords: "commande top Linux, surveiller processus, utilisation système, fonctionnement Linux, top VIRT RES, performances Linux, gestion processus"
---

`top` fournit une vue régulièrement actualisée de l’activité du système et des processus en cours d’exécution. Il aide à formuler une hypothèse de performances, mais un échantillon chargé ne prouve pas à lui seul la cause d’un problème. Comparez plusieurs actualisations et mettez-les en relation avec les journaux et les mesures propres à la charge de travail.

## Lire le résumé du système

Un affichage courant commence par des lignes de résumé suivies d’une table des processus :

```text
top - 18:06:26 up 6 days, 4:07, 2 users, load average: 0.92, 0.62, 0.59
Tasks: 389 total, 1 running, 387 sleeping, 0 stopped, 1 zombie
%Cpu(s): 1.8 us, 0.4 sy, 0.0 ni, 97.6 id, 0.1 wa, 0.0 hi, 0.0 si, 0.0 st
MiB Mem : 32099.0 total, 5276.3 free, 7031.2 used, 19791.5 buff/cache
MiB Swap: 32700.0 total, 32661.0 free, 39.0 used
```

La première ligne contient l’heure actuelle, la durée de fonctionnement, le nombre d’utilisateurs connectés et les charges moyennes sur 1, 5 et 15 minutes. La ligne des tâches compte les états des processus. La charge moyenne n’est pas un pourcentage direct d’utilisation du processeur ; sous Linux, elle reflète les tâches exécutables et celles en sommeil non interruptible. Interprétez-la donc avec le nombre de processeurs, l’activité d’entrées-sorties et la latence.

:::single-choice{#top-load-average-periods}
Que représentent les trois valeurs de charge moyenne dans `top` ?

::option[La charge moyenne sur 1, 5 et 15 minutes.]{#top-one-five-fifteen .correct explanation="Ces valeurs résument des fenêtres récentes de durée progressivement plus longue."}
::option[L’utilisation du processeur par les trois processus les plus actifs.]{#top-three-processes explanation="L’utilisation par processus apparaît dans la table des processus, et non dans ces trois valeurs du résumé."}
::option[La mémoire libre, le cache et l’espace d’échange en mégaoctets.]{#top-three-memory-values explanation="La mémoire et l’espace d’échange possèdent leurs propres lignes de résumé."}
:::

## Interpréter le temps processeur

Les champs courants du processeur comprennent :

- `us` : temps d’exécution dans l’espace utilisateur ;
- `sy` : temps d’exécution dans le noyau ;
- `ni` : temps dans l’espace utilisateur pour les tâches dont la priorité nice a été modifiée ;
- `id` : temps d’inactivité ;
- `wa` : temps d’inactivité pendant qu’une requête d’entrée-sortie est en attente ;
- `hi` et `si` : traitement des interruptions matérielles et logicielles ;
- `st` : temps de processeur virtuel pris par l’hyperviseur pour d’autres invités.

Une valeur `wa` élevée peut étayer l’hypothèse d’une attente d’entrées-sorties, mais n’identifie pas un périphérique et ne prouve pas que le stockage soit le seul goulot d’étranglement. Examinez la latence des périphériques et le comportement de l’application avant de conclure.

:::single-choice{#top-cpu-wa-meaning}
Que mesure le champ processeur `wa` ?

::option[Le temps consacré à l’exécution du code utilisateur ordinaire.]{#top-wa-user explanation="L’exécution dans l’espace utilisateur est indiquée sous `us`."}
::option[Les pages mémoire écrites dans l’espace d’échange depuis le démarrage.]{#top-wa-swap explanation="L’activité d’échange n’est pas une catégorie de temps processeur."}
::option[Le temps d’inactivité du processeur pendant qu’une requête d’entrée-sortie est en attente.]{#top-wa-io .correct explanation="Ce champ représente le temps d’attente d’entrées-sorties et exige des preuves complémentaires sur les périphériques pour établir un diagnostic."}
:::

## Lire la table des processus

Les colonnes importantes comprennent généralement :

- `PID`, `USER` et `COMMAND` : identité et propriété ;
- `S` : état, par exemple en cours d’exécution (`R`), en sommeil (`S`), en sommeil non interruptible (`D`), arrêté (`T`) ou zombie (`Z`) ;
- `%CPU` et `%MEM` : activité échantillonnée du processeur et part de la mémoire physique ;
- `TIME+` : temps processeur cumulé ;
- `VIRT` : espace d’adressage virtuel total associé à la tâche ;
- `RES` : mémoire physique résidente, non placée dans l’espace d’échange, actuellement attribuée à la tâche ;
- `SHR` : mémoire résidente qui peut être partagée avec d’autres processus.

`VIRT` n’est pas la quantité de mémoire vive physique consommée. Il peut comprendre les fichiers mappés, les bibliothèques partagées, l’espace d’adressage réservé et les pages dans l’espace d’échange. Même `RES` exige de la prudence, car les pages partagées compliquent leur attribution.

:::single-choice{#top-res-versus-virt}
Quel champ se rapproche le plus de la mémoire physique actuellement résidente d’un processus ?

::option[`TIME+`]{#top-time-field explanation="Ce champ cumule le temps processeur, et non la mémoire."}
::option[`VIRT`]{#top-virt-field explanation="La taille virtuelle comprend un espace d’adressage qui ne réside pas nécessairement en mémoire vive."}
::option[`RES`]{#top-res-field .correct explanation="La taille résidente reflète les pages physiques actuellement présentes pour le processus, sous réserve des difficultés liées au partage."}
:::

## Cibler et trier

Surveillez directement des PID connus :

```bash
$ top -p 1234,5678
```

Dans `top`, appuyez sur `P` pour trier par processeur, `M` pour trier par mémoire, `1` pour afficher ou masquer les lignes de chaque processeur et `q` pour quitter dans les implémentations courantes de procps-ng. Appuyez sur `h` pour consulter l’aide interactive locale, car les touches et les champs peuvent varier selon l’implémentation.

Relevez le PID, la commande, l’horodatage et plusieurs échantillons avant d’agir. Un processus qui atteint brièvement la première place peut être normal, et l’arrêter peut entraîner une perte de données ou une interruption de service.

:::single-choice{#top-monitor-known-pid}
Quel appel limite l’affichage au PID 1234 ?

::option[`top -u 1234`]{#top-user-filter explanation="La forme `-u` filtre par utilisateur au lieu d’interpréter la valeur comme un PID."}
::option[`top -d 1234`]{#top-delay-filter explanation="Sur les implémentations courantes, l’option `-d` contrôle le délai d’actualisation."}
::option[`top -p 1234`]{#top-pid-filter .correct explanation="L’option `-p` sélectionne un ou plusieurs identifiants de processus à surveiller."}
:::

## Résumé

Vous savez maintenant employer `top` pour formuler et tester une hypothèse sur les performances du système.

1. Lire les charges moyennes comme des charges sur des fenêtres de temps, et non comme des pourcentages du processeur.
2. Comparer les catégories du processeur sur plusieurs échantillons.
3. Distinguer l’espace d’adressage virtuel de la mémoire résidente.
4. Cibler des PID connus et vérifier les preuves avant d’agir.
