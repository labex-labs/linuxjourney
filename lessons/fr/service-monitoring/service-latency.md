---
lesson_id: "service-latency"
course_id: "service-monitoring"
lang: "fr"
order_index: 4
title: "Latence"
description: "Apprenez à comparer les durées de réponse habituelles aux observations les plus lentes."
meta_title: "Latence - Supervision des services"
meta_description: "Apprenez à comparer les durées de réponse habituelles aux observations les plus lentes."
meta_keywords: "latence, supervision des services, DevOps, Linux Journey"
---

La **latence** correspond au temps que prend une requête. Un seul chiffre peut masquer des expériences différentes. Comparez la durée d’une requête typique à celle des plus lentes, pour la même route et sur la même période.

## Lire un petit échantillon

Les cinq durées suivantes sont données en millisecondes. Quatre requêtes ont abouti en moins de 100 millisecondes et une a pris deux secondes.

```text
40  50  60  70  2000
```

La **médiane**, aussi appelée 50e percentile, est la valeur centrale de l’échantillon une fois trié. Elle vaut ici 60 millisecondes. L’observation la plus lente est de 2 000 millisecondes. La moyenne, obtenue en divisant la somme par cinq, vaut 444 millisecondes.

:::single-choice{#service-latency-sample-median} Quelle valeur correspond à la requête du milieu dans cet échantillon trié ?

::option[444 millisecondes.]{#service-latency-sample-median-a explanation="C’est la moyenne, sur laquelle la requête lente pèse aussi."}
::option[60 millisecondes.]{#service-latency-sample-median-b .correct explanation="La troisième des cinq valeurs triées est la médiane."}
::option[2 000 millisecondes.]{#service-latency-sample-median-c explanation="C’est la plus grande valeur observée."}
:::

## Examiner les requêtes les plus lentes

Un **percentile** donne le seuil en dessous duquel se situe une certaine part des observations. Le 95e percentile de latence, souvent appelé p95, donne un seuil proche des valeurs les plus lentes dans un échantillon plus large. Utilisez la définition de votre tableau de bord de façon cohérente dans vos comparaisons. Avec très peu de mesures, l’estimation des valeurs élevées est instable.

:::single-choice{#service-latency-slow-end} La médiane varie à peine, mais des visiteurs signalent encore des lenteurs par intermittence. Que serait-il utile d’examiner ?

::option[Les latences élevées, avec le nombre de requêtes.]{#service-latency-slow-end-a .correct explanation="Les réponses lentes peuvent évoluer alors que la valeur centrale varie peu."}
::option[Uniquement la médiane une fois de plus.]{#service-latency-slow-end-b explanation="Cette approche peut manquer les changements qui touchent une petite partie des visites."}
::option[La taille totale du fichier journal.]{#service-latency-slow-end-c explanation="La taille du fichier n’indique pas la durée des requêtes."}
:::

## Comparer des requêtes similaires

Comparez la même route sous un trafic comparable. Un téléchargement peut naturellement prendre plus de temps qu’un simple contrôle d’état. Si une route se distingue par sa lenteur, examinez les journaux de requêtes et les dépendances sur la même période. Utilisez la mesure pour repérer le problème et les autres éléments pour l’examiner.

:::single-choice{#service-latency-compare-route} Quelle comparaison permet le mieux de vérifier si la même page d’accueil a ralenti après une mise en service ?

::option[Comparer les réponses de la page d’accueil aujourd’hui aux téléchargements du mois dernier.]{#service-latency-compare-route-a explanation="Les opérations et les périodes diffèrent, ce qui rend la comparaison difficile."}
::option[Examiner une seule requête par version, sans indication de période.]{#service-latency-compare-route-b explanation="Une mesure isolée ne rend pas compte des variations."}
::option[Comparer la latence de la page d’accueil sur des périodes comparables avant et après la mise en service.]{#service-latency-compare-route-c .correct explanation="Une route et une charge comparables facilitent l’interprétation du changement."}
:::

## Résumé

Vous savez maintenant examiner ensemble les durées habituelles et les durées les plus longues.

1. Trouvez la médiane dans un petit échantillon trié.
2. Examinez les latences élevées avec le nombre de requêtes.
3. Comparez des requêtes similaires avant de chercher à expliquer les écarts.
