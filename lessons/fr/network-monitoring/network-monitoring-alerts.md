---
lesson_id: "network-monitoring-alerts"
course_id: "network-monitoring"
lang: "fr"
order_index: 6
title: "Alertes réseau"
description: "Apprenez à relier une alerte réseau aux éléments nécessaires pour décider de la suite d’une enquête défensive."
meta_title: "Alertes réseau - Supervision réseau"
meta_description: "Apprenez à relier une alerte réseau aux éléments nécessaires pour décider de la suite d’une enquête défensive."
meta_keywords: "alertes réseau, supervision réseau, cybersécurité, Linux Journey"
---

Une alerte réseau indique qu’une condition de supervision est satisfaite. Lisez la condition et identifiez la source avant de conclure à ce qui s’est passé. Une alerte peut signaler du trafic inattendu, des échecs répétés ou l’absence d’observations attendues.

## Comprendre le périmètre de l’alerte

L’alerte simulée ci-dessous s’appuie sur le journal DNS. Elle regroupe les échecs par client sur une période de cinq minutes.

```text
Window: 09:20–09:25 UTC
Client: 192.0.2.10
Condition: at least 10 failed name lookups
Observed: 12 failures
```

Cela justifie d’examiner les résolutions de noms et leurs résultats. L’alerte ne précise pas quel programme les a demandées.

:::single-choice{#network-monitoring-alerts-alert-scope} Qu’a observé directement l’alerte ?

::option[Douze résolutions infructueuses pour le client indiqué pendant cette période.]{#network-monitoring-alerts-alert-scope-b .correct explanation="L’alerte donne ce nombre et ce périmètre."}
::option[Une perte de données confirmée.]{#network-monitoring-alerts-alert-scope-a explanation="La règle compte les échecs de résolution de noms."}
::option[Douze clients différents.]{#network-monitoring-alerts-alert-scope-c explanation="L’alerte regroupe des entrées pour une seule adresse client."}
:::

## Chercher une entrée correspondante sur l’hôte

Supposons que la plupart des échecs concernent `preview.example`. Le journal d’un service côté client peut montrer qu’un réglage obsolète a provoqué des tentatives répétées. Cherchez des entrées autour de la même heure dans le journal du programme susceptible d’envoyer ces requêtes. Vérifiez le nom donné à l’hôte dans l’outil de supervision avant de lui attribuer l’activité.

:::single-choice{#network-monitoring-alerts-evidence-choice} Quelle entrée aiderait à vérifier qu’un service a répété la résolution ?

::option[Une consultation ultérieure d’une page publique sur un autre hôte.]{#network-monitoring-alerts-evidence-choice-b explanation="L’adresse et l’heure ne correspondent pas à l’activité examinée."}
::option[Une liste des applications installées sans horaire d’activité.]{#network-monitoring-alerts-evidence-choice-c explanation="La liste des logiciels installés ne montre pas lequel a demandé la résolution."}
::option[Une entrée du journal du service qui indique l’échec de résolution pendant la période de l’alerte.]{#network-monitoring-alerts-evidence-choice-a .correct explanation="Elle peut relier les requêtes répétées à ce programme."}
:::

## Consigner la décision suivante

Si le journal du service correspond, notez l’explication et vérifiez une résolution représentative après avoir effectué la correction de configuration approuvée. S’il manque encore des éléments, précisez lesquels. Conservez ensemble l’alerte, l’entrée qui l’éclaire et le résultat de la vérification.

:::single-choice{#network-monitoring-alerts-uncertainty} Vous avez l’alerte DNS, mais aucune entrée correspondante sur l’hôte. Que devez-vous rapporter ?

::option[Le programme exact a été identifié.]{#network-monitoring-alerts-uncertainty-a explanation="Les données DNS seules n’identifient pas le processus."}
::option[Les résolutions répétées sont confirmées et le programme qui les a demandées est inconnu.]{#network-monitoring-alerts-uncertainty-c .correct explanation="Ce constat conserve l’observation et précise ce qu’il reste à établir."}
::option[L’alerte ne décrit absolument rien.]{#network-monitoring-alerts-uncertainty-b explanation="Elle décrit tout de même la condition observée par le résolveur."}
:::

## Vérifier des tentatives répétées attendues

Supposons qu’une équipe ait planifié une tâche qui résout plusieurs fois un nom d’hôte de test. Comparez l’horaire prévu, les noms dans le journal DNS et le journal de la tâche. Plusieurs champs concordants peuvent étayer cette explication. Poursuivez l’examen des échecs sans correspondance.

:::single-choice{#network-monitoring-alerts-final-application} Quel constat appuierait le mieux l’explication de la tâche planifiée ?

::option[L’alerte provient d’un hôte qui exécute d’autres tâches planifiées.]{#network-monitoring-alerts-final-application-c explanation="Ce contexte ne permet pas à lui seul d’identifier le programme qui a demandé les résolutions."}
::option[Le journal de la tâche indique le même nom d’hôte et des tentatives répétées pendant la période de l’alerte.]{#network-monitoring-alerts-final-application-a .correct explanation="Le nom et l’heure concordants permettent de relier l’activité observée à la tâche connue."}
::option[La tâche était prévue à un moment de la journée.]{#network-monitoring-alerts-final-application-b explanation="Un horaire approximatif laisse la période de l’alerte et les noms recherchés sans vérification."}
:::

## Résumé

Vous savez maintenant partir d’une alerte réseau pour orienter la suite de l’examen.

1. Identifiez la règle de détection et son périmètre.
2. Choisissez une entrée liée à l’alerte pour vérifier une explication.
3. Documentez l’observation et ce qui reste incertain.
