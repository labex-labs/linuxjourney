---
lesson_id: "cpu-monitoring"
course_id: "process-utilization"
lang: "fr"
order_index: 4
title: "Surveillance du processeur"
description: "Découvrez comment interpréter les charges moyennes Linux avec le nombre de processeurs, leur utilisation et l’état des tâches."
meta_title: "Surveillance du processeur - Utilisation des processus"
meta_description: "Découvrez les bases de la surveillance du processeur sous Linux avec uptime, l’interprétation de la charge moyenne et l’évaluation des performances."
meta_keywords: "commande uptime, surveillance processeur Linux, charge moyenne, performances système, utilisation processus, tutoriel Linux, guide débutant"
---

Le diagnostic du processeur commence par la distinction entre la charge, l’utilisation et la réactivité. Aucune valeur isolée ne démontre un goulot d’étranglement ; comparez plusieurs fenêtres temporelles et reliez les mesures de l’hôte à la charge de travail réellement ressentie par les utilisateurs.

## Lire uptime

`uptime` fournit un point de départ compact :

```text
$ uptime
 17:23:35 up 1 day, 5:59, 2 users, load average: 0.00, 0.02, 0.05
```

Les trois dernières valeurs sont les charges moyennes sur environ 1, 5 et 15 minutes. Leur comparaison indique la tendance : une valeur sur 1 minute nettement supérieure peut signaler une charge croissante, tandis qu’une valeur sur 15 minutes plus élevée peut indiquer une charge en baisse.

:::single-choice{#cpu-uptime-windows} Dans quel ordre `uptime` affiche-t-il les fenêtres de charge moyenne ?

::option[15, 5 et 1 secondes.]{#cpu-windows-seconds explanation="Ces valeurs sont des moyennes à l’échelle de la minute et ne sont pas affichées de la plus longue à la plus courte."}
::option[1, 5 et 15 minutes.]{#cpu-windows-one-five-fifteen .correct explanation="La fenêtre récente la plus courte apparaît en premier et la plus longue en dernier."}
::option[Pourcentages actuel, minimal et maximal du processeur.]{#cpu-windows-percentages explanation="La charge moyenne n’est pas un pourcentage minimal ou maximal du processeur."}
:::

## Comprendre la charge Linux

La charge moyenne de Linux compte les tâches exécutables, notamment celles qui utilisent ou attendent le processeur, ainsi que les tâches en sommeil non interruptible, souvent associées aux entrées-sorties. Elle ne correspond donc pas à l’utilisation du processeur.

Une charge de `4.0` n’a pas les mêmes conséquences sur des systèmes dotés d’un ou de seize processeurs logiques. Trouvez le nombre d’unités de traitement disponibles pour le système avec :

```bash
$ nproc
```

Les quotas du processeur, l’affinité, la virtualisation et les limites des conteneurs peuvent réduire la capacité visible par une charge de travail particulière ; le nombre de processeurs de l’hôte ne constitue donc qu’un point de départ.

:::single-choice{#cpu-load-not-percentage} Pourquoi la charge moyenne n’est-elle pas un pourcentage d’utilisation du processeur ?

::option[Elle indique uniquement la fréquence d’horloge du processeur.]{#cpu-load-clock explanation="La fréquence d’horloge est une mesure distincte du matériel ou de sa régulation."}
::option[Elle mesure uniquement la mémoire physique libre.]{#cpu-load-memory explanation="La disponibilité de la mémoire est indiquée par d’autres mesures."}
::option[Elle comprend les tâches exécutables et celles en sommeil non interruptible.]{#cpu-load-task-count .correct explanation="La charge repose sur la demande des tâches et leur état d’attente plutôt que sur un pourcentage du temps processeur écoulé."}
:::

## Comparer la charge à l’activité du processeur

Recueillez plusieurs échantillons plutôt que de vous fier à une seule sortie. Parmi les outils complémentaires utiles figurent :

```bash
$ top
$ vmstat 1
$ mpstat -P ALL 1
```

`top` associe les vues de l’hôte et des processus. `vmstat` montre le nombre de tâches exécutables et bloquées ainsi que les catégories du processeur. `mpstat`, fourni par `sysstat` sur de nombreuses distributions, affiche l’activité de chaque processeur. La disponibilité et les champs exacts varient ; consultez donc les manuels locaux.

Une charge élevée accompagnée de processeurs occupés peut signaler une forte demande de calcul. Une charge élevée associée à un nombre notable de tâches bloquées, à une latence d’entrées-sorties ou à des observations d’attente d’entrées-sorties oriente vers une autre ressource limitée. Une faible utilisation moyenne peut également masquer un seul processeur saturé ou un bref pic de latence.

:::single-choice{#cpu-high-load-next-step} Quelle est la meilleure étape suivante après l’observation d’une charge moyenne élevée ?

::option[Comparer des mesures répétées du processeur, de l’état des tâches, des entrées-sorties et de la charge de travail.]{#cpu-load-correlate .correct explanation="Des échantillons corrélés permettent de distinguer plusieurs explications concurrentes de la charge."}
::option[Redémarrer immédiatement sans recueillir d’autres données.]{#cpu-load-reboot explanation="Le redémarrage supprime des indices et peut interrompre les services sans identifier la cause."}
::option[Supposer que chaque processeur est entièrement utilisé.]{#cpu-load-assume explanation="La charge peut comprendre des tâches non interruptibles et être répartie de manière inégale entre les processeurs."}
:::

## Évaluer la capacité et les conséquences

Il n’existe aucune règle universelle selon laquelle la charge doit toujours rester inférieure au nombre de processeurs. Les systèmes de traitement par lots peuvent accepter des files d’attente, tandis que les services interactifs peuvent dépasser leurs objectifs de latence avant ce seuil. Établissez une référence pour le même hôte et la même charge de travail, puis comparez le temps de réponse, le débit, le taux d’erreurs, la saturation et l’utilisation des ressources.

:::single-choice{#cpu-capacity-threshold} Qu’est-ce qui doit déterminer si la charge observée est acceptable ?

::option[L’obligation de toujours maintenir la valeur sous un.]{#cpu-below-one explanation="La capacité multicœur et les objectifs de la charge de travail rendent ce seuil fixe peu fiable."}
::option[Uniquement le nombre d’utilisateurs affiché par `uptime`.]{#cpu-user-count explanation="Les utilisateurs connectés à un shell ne représentent pas toute la demande de la charge de travail."}
::option[La référence et les objectifs de service de la charge de travail.]{#cpu-baseline-objectives .correct explanation="L’acceptabilité dépend du comportement attendu et des performances visibles par les utilisateurs, et non d’un seuil universel."}
:::

## Résumé

Vous savez maintenant interpréter la charge moyenne comme un élément d’une investigation sur le processeur.

1. Lire les fenêtres de charge sur 1, 5 et 15 minutes.
2. Distinguer la charge des tâches des pourcentages de temps processeur.
3. Comparer la charge à la capacité de traitement disponible.
4. Mettre en relation des mesures répétées de l’hôte avec les résultats du service.
