---
lesson_id: "service-availability-errors"
course_id: "service-monitoring"
lang: "fr"
order_index: 3
title: "Disponibilité et erreurs"
description: "Apprenez à comparer les erreurs de requête en tenant compte de la période et du nombre total de requêtes."
meta_title: "Disponibilité et erreurs - Supervision des services"
meta_description: "Apprenez à comparer les erreurs de requête en tenant compte de la période et du nombre total de requêtes."
meta_keywords: "disponibilité et erreurs, supervision des services, DevOps, Linux Journey"
---

Un service peut répondre à la plupart des visiteurs alors que certaines requêtes échouent. Comptez le total des requêtes et les échecs sur la même période pour estimer la proportion de requêtes en échec.

## Calculer le taux d’erreur

Le **taux d’erreur** s’obtient en divisant le nombre de requêtes en échec par le nombre observé. Multipliez le résultat par 100 pour l’exprimer en pourcentage.

```text
Window          Requests   Failures
09:00–09:05          100          2
09:05–09:10           20          2
```

Sur la première période, deux requêtes sur cent échouent, soit 2 %. Sur la suivante, on compte encore deux échecs, mais sur vingt requêtes, soit 10 %.

:::single-choice{#service-availability-errors-compare-windows} Sur quelle période la proportion d’échecs était-elle la plus élevée ?

::option[De 09:05 à 09:10.]{#service-availability-errors-compare-windows-b .correct explanation="Deux échecs sur vingt représentent une part plus importante que deux sur cent."}
::option[Les deux périodes sont équivalentes, car elles comptent chacune deux échecs.]{#service-availability-errors-compare-windows-a explanation="Les dénominateurs diffèrent."}
::option[De 09:00 à 09:05, car il y avait plus de trafic.]{#service-availability-errors-compare-windows-c explanation="Avec un total plus élevé, le même nombre d’échecs représente une part plus faible."}
:::

## Comparer sur le même périmètre

Tenez compte de la période, de la route et de ce qui constitue un échec. Un point de contrôle de l’état du service peut répondre correctement alors qu’une page qui utilise une dépendance échoue. Pour vérifier l’expérience des personnes qui consultent cette page, comptez les requêtes qui lui sont adressées.

:::single-choice{#service-availability-errors-route-scope} Le contrôle d’état réussit toujours, mais des clients signalent des erreurs au moment de payer. Que devez-vous examiner ?

::option[Uniquement les réponses du contrôle d’état.]{#service-availability-errors-route-scope-b explanation="Ces réponses décrivent une autre opération."}
::option[Le nom du compte de service.]{#service-availability-errors-route-scope-c explanation="Ce nom ne permet pas de compter les requêtes concernées."}
::option[Les requêtes de paiement et leurs échecs.]{#service-availability-errors-route-scope-a .correct explanation="Le problème signalé concerne cette route."}
:::

## Interpréter un faible trafic

Si une requête sur deux échoue, le taux observé est de 50 %. Ce chiffre décrit l’échantillon. Quelques requêtes suffisent à provoquer de fortes variations, alors gardez le nombre de requêtes à côté du pourcentage. En l’absence de requêtes, le taux d’erreur du trafic réel est indéfini. Un test planifié séparément peut tout de même vous dire si une requête a réussi.

:::single-choice{#service-availability-errors-zero-traffic} Une période ne comporte aucune requête de visiteur. Que faut-il indiquer à propos du taux d’erreur des visiteurs ?

::option[Cela prouve que la disponibilité est parfaite.]{#service-availability-errors-zero-traffic-a explanation="Aucune requête de visiteur n’a été observée pour l’établir."}
::option[Cette période ne contient aucune donnée permettant de calculer un taux d’erreur.]{#service-availability-errors-zero-traffic-c .correct explanation="Effectuez un test séparé si vous souhaitez vérifier que le service répond."}
::option[Il est forcément de 100 %.]{#service-availability-errors-zero-traffic-b explanation="Le dénominateur ne contient aucune requête observée."}
:::

## Résumé

Vous savez maintenant expliquer un taux d’erreur avec le contexte nécessaire.

1. Rapportez les échecs au total des requêtes de la même période.
2. Adaptez la route et la définition d’un échec à la question posée.
3. Gardez les nombres de requêtes visibles lorsque le trafic est faible.
