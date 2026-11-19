---
lesson_id: "service-logs"
course_id: "service-monitoring"
lang: "fr"
order_index: 2
title: "Journaux de service"
description: "Apprenez à suivre une requête dans les journaux de service à l’aide de son identifiant et de son horaire."
meta_title: "Journaux de service - Supervision des services"
meta_description: "Apprenez à suivre une requête dans les journaux de service à l’aide de son identifiant et de son horaire."
meta_keywords: "journaux de service, supervision des services, DevOps, Linux Journey"
---

Un utilisateur voit une erreur. Un journal de service peut indiquer quelle partie du traitement a échoué pour sa requête. Commencez par l’heure, puis cherchez un **identifiant de requête**, une valeur transmise et inscrite dans les entrées relatives à la même requête.

## Lire les entrées d’une requête

L’exemple ci-dessous montre deux services. Une **dépendance** est un service dont un autre programme a besoin pour terminer son travail. Ici, le service web demande une liste d’articles à un service de catalogue.

```text
09:14:02 service=web     request=r17 path=/items status=502
09:14:02 service=catalog request=r17 action=read result=timeout
09:14:03 service=catalog request=r18 action=read result=ok
```

La ligne du service web indique un échec pour `r17`. La ligne du catalogue avec le même identifiant indique un dépassement de délai. La requête du catalogue qui a réussi presque au même moment porte l’identifiant `r18`.

:::single-choice{#service-logs-matching-request} Quel résultat du catalogue correspond à l’échec du service web pour r17 ?

::option[Le résultat positif de r18.]{#service-logs-matching-request-a explanation="Cette ligne appartient à une autre requête."}
::option[Les deux résultats du catalogue.]{#service-logs-matching-request-c explanation="Des horodatages proches peuvent correspondre à des requêtes différentes."}
::option[Le dépassement de délai pour r17.]{#service-logs-matching-request-b .correct explanation="L’identifiant commun relie les deux entrées de cette requête."}
:::

## Filtrer l’échantillon

Enregistrez les trois lignes ci-dessus dans un fichier `requests.log` dans un dossier d’exercice. Utilisez `grep -F` pour rechercher du texte littéral. Incluez l’espace après l’identifiant pour respecter la limite du champ dans cet exemple.

```bash
$ grep -F 'request=r17 ' requests.log
```

Vous devriez obtenir les lignes du service web et du catalogue pour `r17`. Les journaux réels peuvent changer de format ou omettre l’identifiant de requête. Vérifiez donc que les champs recherchés représentent la même chose d’un service à l’autre.

:::single-choice{#service-logs-choose-filter} Pourquoi inclure tout le champ de la requête au lieu de rechercher le mot timeout ?

::option[Cela garantit que tout le trafic a rencontré la même erreur.]{#service-logs-choose-filter-b explanation="Le filtre sélectionne les entrées d’une seule requête."}
::option[Cela renvoie les entrées du service web et du catalogue, même si une seule contient timeout.]{#service-logs-choose-filter-a .correct explanation="L’identifiant commun permet de suivre la requête dans les deux services."}
::option[Cela modifie le journal pour que les recherches suivantes trouvent le bon résultat.]{#service-logs-choose-filter-c explanation="Grep lit le fichier et affiche les lignes correspondantes."}
:::

![Résultat de grep reliant l’erreur du service web au dépassement de délai du catalogue pour la requête r17](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/service-monitoring/service-logs/request-id.png)

## Délimiter le constat

Le dépassement de délai situe l’échec observé pour cette requête. Il reste à déterminer quel composant du catalogue a ralenti. Examinez ensuite les mesures ou les entrées récentes de cette dépendance. Lorsque vous transmettez un extrait de journal à un collègue, conservez l’identifiant de requête et retirez les secrets et les données personnelles dont il n’a pas besoin.

:::single-choice{#service-logs-evidence-limit} Que devriez-vous indiquer dans un premier rapport ?

::option[Le catalogue a dépassé le délai pendant r17 et doit être examiné de plus près.]{#service-logs-evidence-limit-c .correct explanation="Ce constat résume les entrées correspondantes sans supposer la cause profonde."}
::option[Toutes les requêtes du catalogue ont dépassé le délai.]{#service-logs-evidence-limit-a explanation="L’échantillon contient une autre requête du catalogue qui a réussi."}
::option[Un disque précis de la base de données est tombé en panne.]{#service-logs-evidence-limit-b explanation="Les entrées ne contiennent aucune observation sur les disques."}
:::

Pour vous entraîner à interroger les journaux de service sur un hôte Linux, essayez [Analyser les journaux pour répondre à un incident](https://labex.io/labs/linux-monitoring-and-incident-response-log-analysis-594586).

## Résumé

Vous savez maintenant suivre une requête dans les journaux de plusieurs services.

1. Repérez le même identifiant de requête dans les entrées pertinentes.
2. Utilisez un filtre littéral pour cibler les lignes de l’échantillon.
3. Rapportez ce que les entrées établissent et déterminez la prochaine vérification.
