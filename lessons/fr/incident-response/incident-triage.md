---
lesson_id: "incident-triage"
course_id: "incident-response"
lang: "fr"
order_index: 1
title: "Triage des incidents"
description: "Apprenez à délimiter les premières vérifications à partir d’un signalement d’incident."
meta_title: "Triage des incidents - Réponse aux incidents"
meta_description: "Apprenez à délimiter les premières vérifications à partir d’un signalement d’incident."
meta_keywords: "triage des incidents, réponse aux incidents, cybersécurité, Linux Journey"
---

Un premier signalement peut indiquer qu’une page a échoué ou qu’une alerte s’est déclenchée. Le **triage** consiste à décider de ce qui doit être traité en priorité. Notez le service touché, l’heure et le comportement observé avant de choisir une réponse.

## Lire le signalement

Un membre de l’équipe rédige ce signalement simulé.

```text
09:22 UTC: Visitors received 503 from the public homepage.
The staff preview still loaded during the same check.
First failure observed at approximately 09:19 UTC.
```

Le signalement donne deux routes et deux observations différentes. Confirmez le résultat de la page d’accueil publique, puis notez l’heure du contrôle et l’adresse testée.

:::single-choice{#incident-triage-affected-service} Sur quel symptôme le premier contrôle doit-il porter ?

::option[La prévisualisation destinée au personnel renvoie 503.]{#incident-triage-affected-service-b explanation="Le signalement indique que la prévisualisation s’affiche toujours."}
::option[La page d’accueil publique renvoie 503.]{#incident-triage-affected-service-a .correct explanation="C’est le chemin touché indiqué dans le signalement."}
::option[Une page est introuvable sur un hôte sans rapport.]{#incident-triage-affected-service-c explanation="Ce chemin n’entre pas dans le périmètre du signalement."}
:::

## Estimer les conséquences

Vérifiez combien d’utilisateurs ou de requêtes sont touchés et si le service reste utilisable. Déterminez si l’incident est toujours en cours. Présentez les estimations comme telles tant que vous ne disposez pas d’éléments plus précis. Consultez le plan de réponse pour savoir qui prévenir.

:::single-choice{#incident-triage-triage-scope} Quelle observation aide à décider si le problème reste urgent ?

::option[Un contrôle actuel du chemin en échec et les résultats des requêtes récentes.]{#incident-triage-triage-scope-b .correct explanation="Vous pouvez ainsi voir si le symptôme persiste et quelle est son ampleur."}
::option[L’âge du premier commit du dépôt.]{#incident-triage-triage-scope-a explanation="Cela ne montre pas les conséquences actuelles."}
::option[Le niveau de gravité du signalement initial à lui seul.]{#incident-triage-triage-scope-c explanation="Le niveau initial donne du contexte. Les conséquences actuelles aident à décider si le problème reste urgent."}
:::

## Choisir une première action utile

Si la nouvelle requête échoue aussi, gardez le résultat et examinez les changements récents du service ainsi que les journaux de la période touchée. Un autre chemin qui fonctionne aide à circonscrire la panne. Gardez la première explication plausible au stade de l’hypothèse.

:::single-choice{#incident-triage-first-next-step} Le chemin public échoue toujours et la prévisualisation du personnel fonctionne toujours. Que faut-il examiner ensuite ?

::option[Tous les projets sans rapport dans l’entreprise.]{#incident-triage-first-next-step-a explanation="Le signalement indique un service et une période plus précis."}
::option[Une ancienne erreur choisie au hasard à une autre date.]{#incident-triage-first-next-step-b explanation="Commencez par les éléments proches de l’échec observé."}
::option[Les entrées concernant la route publique sur la période signalée.]{#incident-triage-first-next-step-c .correct explanation="Elles peuvent aider à distinguer un problème de routage d’une panne du service."}
:::

## Résumé

Vous savez maintenant engager une première réponse ciblée après un signalement d’incident.

1. Indiquez le chemin touché, l’heure et le symptôme.
2. Vérifiez les conséquences actuelles pour les utilisateurs.
3. Choisissez la prochaine source à examiner pour le chemin touché.
