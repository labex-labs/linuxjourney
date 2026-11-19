---
lesson_id: "service-alerts"
course_id: "service-monitoring"
lang: "fr"
order_index: 6
title: "Alertes de service"
description: "Apprenez à interpréter la condition d’une alerte, la période concernée et l’action à entreprendre."
meta_title: "Alertes de service - Supervision des services"
meta_description: "Apprenez à interpréter la condition d’une alerte, la période concernée et l’action à entreprendre."
meta_keywords: "alertes de service, supervision des services, DevOps, Linux Journey"
---

Un tableau de bord affiche des mesures. Une **alerte** invite quelqu’un à examiner une situation qui peut nécessiter une intervention. Une alerte utile permet de comprendre ce qui s’est passé et de savoir quoi vérifier.

## Lire la condition de déclenchement

Prenons une règle qui se déclenche si plus de 5 % des requêtes vers la page d’accueil échouent en cinq minutes. Elle exige aussi au moins 100 requêtes pour que l’échantillon soit suffisamment grand pour ce service.

```text
Window   09:10–09:15 UTC
Route    /
Requests 120
Failures 12
```

Douze échecs sur 120 requêtes représentent 10 %. Les deux critères sont satisfaits. L’alerte signale les échecs observés sur la page d’accueil.

:::single-choice{#service-alerts-condition-match} La même règle déclencherait-elle une alerte pour un échec sur dix requêtes ?

::option[Non, le nombre minimal de requêtes n’a pas été atteint.]{#service-alerts-condition-match-b .correct explanation="Le taux et le nombre de requêtes doivent tous deux satisfaire la règle."}
::option[Oui, le taux d’erreur dépasse 5 %.]{#service-alerts-condition-match-a explanation="La condition exige aussi au moins 100 requêtes."}
::option[Non, un échec sur dix représente 1 %.]{#service-alerts-condition-match-c explanation="Un échec sur dix représente 10 %, mais le nombre de requêtes reste insuffisant."}
:::

## Examiner la période concernée

Utilisez la période indiquée dans l’alerte, même si le tableau de bord indique désormais un état normal. L’alerte peut décrire une situation antérieure. Vérifiez si la mesure est revenue à son niveau habituel et si les utilisateurs peuvent de nouveau effectuer les actions importantes.

:::single-choice{#service-alerts-alert-window} L’alerte est arrivée à 09:16 et concernait la période de 09:10 à 09:15. Où chercher d’abord les erreurs correspondantes ?

::option[Uniquement dans un rapport de la semaine précédente.]{#service-alerts-alert-window-b explanation="Ce rapport peut fournir un point de référence, mais il ne couvre pas la période touchée."}
::option[Uniquement après 09:16.]{#service-alerts-alert-window-c explanation="Le délai de notification peut expliquer que l’alerte arrive après les observations."}
::option[Dans la période indiquée par l’alerte.]{#service-alerts-alert-window-a .correct explanation="C’est la période pendant laquelle la règle a compté les erreurs."}
:::

## Choisir une première action utile

Une alerte sur les échecs de la page d’accueil peut renvoyer aux mesures et aux journaux récents de cette route. Vérifiez les conséquences pour les utilisateurs, puis recherchez la cause. Si le service s’est rétabli, conservez assez de contexte pour examiner les alertes qui se répètent.

:::single-choice{#service-alerts-next-check} Quelle première action permet de vérifier directement si la page d’accueil est toujours en échec ?

::option[Compter toutes les images de conteneur dans le cache.]{#service-alerts-next-check-a explanation="L’alerte porte sur les résultats des requêtes adressées au service en activité."}
::option[Envoyer une requête de test autorisée à la route concernée.]{#service-alerts-next-check-c .correct explanation="Une nouvelle requête montre si le problème signalé touche toujours cette route."}
::option[Désactiver la règle pour faire taire les alertes.]{#service-alerts-next-check-b explanation="Cette action modifie les notifications sans vérifier le service."}
:::

## Résumé

Vous savez maintenant lire une alerte et décider quoi vérifier.

1. Vérifiez la mesure, le seuil et la taille minimale de l’échantillon.
2. Recherchez les éléments correspondants dans la période indiquée.
3. Vérifiez le symptôme visible par l’utilisateur à l’aide d’un contrôle adapté.
