---
lesson_id: "network-traffic-baselines"
course_id: "network-monitoring"
lang: "fr"
order_index: 5
title: "Trafic de référence"
description: "Apprenez à comparer des périodes de trafic similaires avant de considérer un changement comme anormal."
meta_title: "Trafic de référence - Supervision réseau"
meta_description: "Apprenez à comparer des périodes de trafic similaires avant de considérer un changement comme anormal."
meta_keywords: "trafic de référence, supervision réseau, cybersécurité, Linux Journey"
---

Une **référence** décrit le comportement habituellement observé dans des conditions définies. Pour la supervision du trafic, il peut s’agir d’un volume habituel ou d’une plage de valeurs pour le même service à la même heure.

## Choisir des périodes comparables

Une page publique peut recevoir davantage de trafic pendant les heures de travail. Si vous cherchez à détecter un changement, comparez des périodes où l’activité habituelle est comparable. Cet exemple compte les requêtes d’un même service par périodes de cinq minutes.

```text
Window                 Requests
Typical weekdays 09:00  90–120
Today 09:00                230
Typical nights 02:00       2–8
```

Les 230 requêtes dépassent la plage habituelle du matin en semaine. La plage nocturne serait un point de comparaison moins pertinent.

:::single-choice{#network-traffic-baselines-baseline-fit} Quelle ligne fournit une référence utile pour la période de 09:00 aujourd’hui ?

::option[Une nuit ordinaire à 02:00.]{#network-traffic-baselines-baseline-fit-b explanation="Cette ligne décrit un autre rythme de trafic."}
::option[Les 230 requêtes mesurées aujourd’hui, prises isolément.]{#network-traffic-baselines-baseline-fit-c explanation="Un décompte actuel seul nécessite un point de comparaison pour établir ce qui a changé."}
::option[Un jour de semaine ordinaire à 09:00.]{#network-traffic-baselines-baseline-fit-a .correct explanation="La ligne correspond à l’heure et au service examinés."}
:::

## Chercher du contexte

Une annonce sur une bannière ou une tâche planifiée peut expliquer un changement. Examinez les routes, les horaires et les modifications approuvées avant de décider s’il faut poursuivre l’enquête. La référence met en évidence un écart et vous aide à formuler une première question.

:::single-choice{#network-traffic-baselines-baseline-explain} Le trafic a doublé après un lancement annoncé. Que vérifier ?

::option[Considérer l’écart comme la preuve qu’un compte a été compromis.]{#network-traffic-baselines-baseline-explain-a explanation="Le décompte seul ne montre ni la cause ni un événement lié à un compte."}
::option[Comparer l’heure et les chemins observés à ceux attendus après le lancement.]{#network-traffic-baselines-baseline-explain-b .correct explanation="Cette comparaison confronte une explication plausible aux observations pertinentes."}
::option[Ignorer le changement, car les lancements expliquent toujours tous les pics.]{#network-traffic-baselines-baseline-explain-c explanation="Un changement attendu peut coïncider avec une activité indépendante."}
:::

## Examiner la mesure

Une modification du collecteur peut changer le décompte alors que le trafic réel reste stable. Si la supervision couvre un réseau de plus depuis hier, vérifiez quel trafic inclut chaque période. Consignez le service, le point d’observation, l’heure et l’unité avec la comparaison.

:::single-choice{#network-traffic-baselines-changed-coverage} Le collecteur a commencé à enregistrer un deuxième site. Comment rendre la prochaine comparaison plus utile ?

::option[Comparer des décomptes portant sur le même site et les mêmes sources.]{#network-traffic-baselines-changed-coverage-c .correct explanation="Un périmètre stable aide à distinguer une évolution du trafic d’un changement de couverture."}
::option[Comparer les deux totaux sans vérifier leur périmètre.]{#network-traffic-baselines-changed-coverage-a explanation="Le changement de collecte rend ces totaux moins comparables."}
::option[Comparer le nouveau total à celui d’hier après avoir allongé la période.]{#network-traffic-baselines-changed-coverage-b explanation="Une période plus longue mélange quand même des périmètres différents si les totaux n’incluent pas les mêmes sites et sources."}
:::

## Résumé

Vous savez maintenant déterminer si une comparaison réseau possède une référence exploitable.

1. Faites correspondre le service, l’heure et l’unité.
2. Cherchez des changements attendus avant d’interpréter un écart.
3. Vérifiez si la portée de la collecte a changé.
