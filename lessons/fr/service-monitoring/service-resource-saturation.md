---
lesson_id: "service-resource-saturation"
course_id: "service-monitoring"
lang: "fr"
order_index: 5
title: "Saturation des ressources"
description: "Apprenez à repérer les limites de capacité d’un service à l’aide du taux d’utilisation et des files d’attente."
meta_title: "Saturation des ressources - Supervision des services"
meta_description: "Apprenez à repérer les limites de capacité d’un service à l’aide du taux d’utilisation et des files d’attente."
meta_keywords: "saturation des ressources, supervision des services, DevOps, Linux Journey"
---

Lorsqu’un service reçoit plus de travail qu’une ressource ne peut en traiter immédiatement, des requêtes peuvent attendre. Si l’attente perdure, elle peut se traduire par une file et par des réponses plus lentes.

## Comprendre la capacité et la demande

Le **taux d’utilisation** indique quelle part d’une ressource est utilisée. Un ensemble de processus de traitement peut, par exemple, exécuter quatre tâches à la fois. Si les quatre processus sont occupés, la capacité est entièrement utilisée à cet instant. Une nouvelle tâche peut alors entrer dans une file jusqu’à ce qu’un processus se libère.

:::single-choice{#service-resource-saturation-worker-capacity} Quatre processus sont occupés et trois tâches sont en file d’attente. Que savez-vous ?

::option[Exactement sept processus sont en cours d’exécution.]{#service-resource-saturation-worker-capacity-b explanation="Trois tâches attendent sans occuper de place de traitement."}
::option[Toutes les requêtes ont déjà échoué.]{#service-resource-saturation-worker-capacity-c explanation="Les tâches en attente peuvent aboutir lorsqu’un processus se libère."}
::option[Toutes les places sont occupées et des tâches attendent.]{#service-resource-saturation-worker-capacity-a .correct explanation="Le nombre de processus occupés indique l’utilisation actuelle et la file montre la demande supplémentaire."}
:::

## Comparer dans le temps

Un pic bref diffère d’une file qui s’allonge au fil des observations. Comparez la file à la latence et au trafic de la même période.

```text
Time   Busy workers   Queued jobs   Typical response
09:10       2 / 4           0             80 ms
09:11       4 / 4           5            300 ms
09:12       4 / 4          14            640 ms
```

Dans cet exemple, les processus tous occupés et la file qui s’allonge indiquent que les tâches semblent arriver plus vite qu’elles ne se terminent. Vérifiez ce qui occupe les processus.

:::single-choice{#service-resource-saturation-sustained-pressure} Quelle observation indique le plus clairement une pression qui persiste ?

::option[Deux processus occupés à 09:10.]{#service-resource-saturation-sustained-pressure-a explanation="Cette ligne montre qu’il restait de la capacité et qu’aucune tâche n’attendait."}
::option[La file s’allonge alors que tous les processus restent occupés.]{#service-resource-saturation-sustained-pressure-b .correct explanation="Des tâches s’accumulent alors que toute la capacité reste utilisée."}
::option[Une réponse plus lente alors que la file reste vide.]{#service-resource-saturation-sustained-pressure-c explanation="Une réponse lente peut justifier un examen. Une file qui s’allonge sur plusieurs mesures à pleine capacité indique plus clairement une pression durable."}
:::

![Mesures simulées montrant des processus tous occupés et une file qui s’allonge](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/service-monitoring/service-resource-saturation/worker-queue.png)

## Rechercher la cause

Les processus peuvent être occupés parce que les requêtes arrivent plus vite, parce qu’une dépendance a ralenti ou parce qu’un changement récent allonge chaque tâche. Comparez le volume de requêtes, le temps de traitement et les observations sur les dépendances. Un signal de plus aide à choisir une réponse.

:::single-choice{#service-resource-saturation-next-observation} Le volume de requêtes est resté stable alors que le traitement a ralenti. Qu’est-ce qui pourrait éclairer l’accumulation de tâches ?

::option[Examiner ensemble la durée des tâches et les temps de réponse des dépendances.]{#service-resource-saturation-next-observation-c .correct explanation="Vous pourrez mieux comprendre pourquoi les tâches occupent les places plus longtemps."}
::option[Modifier la capacité avant de recueillir d’autres éléments.]{#service-resource-saturation-next-observation-a explanation="Une capacité accrue peut laisser entier le problème des tâches bloquées par une dépendance."}
::option[Compter les rôles dans le dépôt.]{#service-resource-saturation-next-observation-b explanation="Ces rôles ne montrent pas ce que les processus attendent."}
:::

## Résumé

Vous savez maintenant distinguer une ressource occupée d’une file qui s’accumule durablement.

1. Rapportez le nombre de processus occupés à la capacité totale.
2. Comparez les files au comportement des requêtes au fil du temps.
3. Examinez le travail qui occupe une ressource proche de sa limite.
