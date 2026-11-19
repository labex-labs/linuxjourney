---
lesson_id: "network-monitoring-records"
course_id: "network-monitoring"
lang: "fr"
order_index: 1
title: "Données de supervision réseau"
description: "Apprenez à choisir une source de données réseau adaptée à une question de supervision."
meta_title: "Données de supervision réseau - Supervision réseau"
meta_description: "Apprenez à choisir une source de données réseau adaptée à une question de supervision."
meta_keywords: "données réseau, supervision réseau, cybersécurité, Linux Journey"
---

Une observation réseau décrit ce qu’un outil a pu voir depuis un emplacement donné. Demandez-vous d’abord ce que vous cherchez à savoir. Chaque source rend visibles certains aspects de la même activité.

## Choisir le type de données

Un **résumé de flux** décrit les échanges entre deux extrémités du réseau. Un **journal DNS** consigne les résolutions de noms qu’un résolveur a observées. Une **capture de paquets** conserve une copie de chaque paquet observé au point de capture. Une extrémité représente un côté de la communication et se repère souvent par une adresse et un port.

:::single-choice{#network-monitoring-records-choose-dns} Vous cherchez la réponse d’un résolveur pour site.example. Quelle source est la plus adaptée ?

::option[Un décompte des processus web en cours d’exécution.]{#network-monitoring-records-choose-dns-b explanation="Le nombre de processus n’a aucun rapport avec la résolution."}
::option[Un journal DNS de ce résolveur.]{#network-monitoring-records-choose-dns-a .correct explanation="Le résolveur peut enregistrer la question et la réponse qu’il a traitées."}
::option[Un résumé de flux qui indique seulement le volume du trafic.]{#network-monitoring-records-choose-dns-c explanation="Un résumé de flux peut omettre la question et la réponse DNS."}
:::

## Repérer le point d’observation

Une capture sur un ordinateur portable contient les paquets visibles sur l’interface sélectionnée. Un journal de serveur reflète ce qui est arrivé au serveur ou ce que ce dernier a consigné. Par exemple, une requête peut échouer avant de parvenir au serveur. Utilisez une source dont l’emplacement correspond à votre question.

:::single-choice{#network-monitoring-records-capture-scope} Vous ne trouvez aucune requête dans une capture effectuée sur un autre ordinateur. Que vérifier avant de tirer une conclusion ?

::option[Si l’interface de capture pouvait observer le chemin concerné pendant la période pertinente.]{#network-monitoring-records-capture-scope-b .correct explanation="L’absence d’un paquet peut refléter les limites de visibilité du point d’observation."}
::option[Si la capture contient quelques paquets sans rapport.]{#network-monitoring-records-capture-scope-a explanation="Ces paquets montrent qu’une collecte a eu lieu. Il reste à vérifier la visibilité du chemin et de la période qui vous intéressent."}
::option[Si un autre hôte effectuait une capture au même moment.]{#network-monitoring-records-capture-scope-c explanation="Une capture simultanée sur un autre hôte n’établit pas ce que cette interface pouvait voir."}
:::

## Limiter la taille de l’échantillon

Les captures peuvent contenir des données que des personnes ne souhaitaient pas partager. Pour apprendre à lire les paquets, utilisez une capture préparée contenant un trafic d’exercice sans danger. Lorsque vous transmettez un petit extrait, indiquez la période examinée et le filtre utilisé pour que le destinataire en comprenne les limites.

:::single-choice{#network-monitoring-records-choosing-evidence} Quel échantillon convient le mieux pour apprendre à identifier une réponse DNS ?

::option[Une longue capture de trafic du personnel sans rapport avec l’exercice.]{#network-monitoring-records-choosing-evidence-a explanation="Elle ajoute des données inutiles et peut révéler des informations privées."}
::option[Un résumé sans champ décrivant la résolution.]{#network-monitoring-records-choosing-evidence-b explanation="Le lecteur n’aurait pas les éléments nécessaires à examiner."}
::option[Une petite capture préparée qui contient la requête et la réponse de l’exercice.]{#network-monitoring-records-choosing-evidence-c .correct explanation="Elle contient précisément l’échange nécessaire pour répondre à la question."}
:::

## Résumé

Vous savez maintenant choisir une source réseau et expliquer ce qu’elle pouvait observer.

1. Distinguez les résumés de flux, les journaux DNS et les captures de paquets.
2. Choisissez un point d’observation qui correspond au chemin réseau.
3. Utilisez un échantillon ciblé et adapté à l’examen.
