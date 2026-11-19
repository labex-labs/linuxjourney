---
lesson_id: "incident-timelines"
course_id: "incident-response"
lang: "fr"
order_index: 3
title: "Chronologies d’incident"
description: "Apprenez à placer les observations sur une même chronologie en signalant les heures incertaines."
meta_title: "Chronologies d’incident - Réponse aux incidents"
meta_description: "Apprenez à placer les observations sur une même chronologie en signalant les heures incertaines."
meta_keywords: "chronologies d’incident, réponse aux incidents, cybersécurité, Linux Journey"
---

Une chronologie d’incident ordonne des observations issues de différentes sources. Utilisez un fuseau horaire commun et gardez l’horodatage d’origine visible dans vos notes. L’ordre des événements vous aide à repérer les liens possibles.

## Convertir un horodatage

Ici, un relevé web utilise l’heure UTC et une fiche de déploiement utilise un décalage de deux heures en avance sur UTC.

```text
Deployment record:  2026-11-19 11:17:00 +02:00
Web report:         2026-11-19 09:22:00 UTC
```

Sur un système Linux équipé de GNU date, `-d` lit l’horodatage fourni et `-u` demande une sortie en UTC. L’argument qui commence par `+` définit le format d’affichage.

```bash
$ date -u -d '2026-11-19 11:17:00+02:00' '+%Y-%m-%d %H:%M:%S UTC'
```

Le résultat est `2026-11-19 09:17:00 UTC`. Dans cet exemple, il précède le relevé web de cinq minutes.

:::single-choice{#incident-timelines-earlier-event} Quelle entrée est la plus ancienne après conversion des heures ?

::option[La fiche de déploiement.]{#incident-timelines-earlier-event-a .correct explanation="La conversion du décalage donne 09:17 UTC, soit avant le relevé de 09:22."}
::option[Le relevé web.]{#incident-timelines-earlier-event-b explanation="L’heure du relevé paraît plus tôt si vous comparez les valeurs affichées avant de les ramener au même fuseau."}
::option[Les deux entrées correspondent exactement à la même heure.]{#incident-timelines-earlier-event-c explanation="Les deux heures converties diffèrent de cinq minutes."}
:::

![Conversion enregistrée avec GNU date, de 11:17 avec le décalage +02:00 à 09:17 UTC](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-timelines/normalize-utc.png)

## Distinguer les observations des estimations

Un signalement peut indiquer que le premier échec a eu lieu vers 09:19. Conservez cette heure comme estimation. L’heure du signalement d’un utilisateur peut différer de celle de la première requête en échec. Pour chaque ligne, indiquez la source et le degré de précision de l’heure.

:::single-choice{#incident-timelines-estimated-time} Un collègue indique vers 09:19. Comment reporter cette heure ?

::option[Comme 09:19:00 exactement, avec confirmation par un journal.]{#incident-timelines-estimated-time-a explanation="La source fournit une estimation."}
::option[Comme un événement sans source.]{#incident-timelines-estimated-time-c explanation="La source est nécessaire pour savoir quel degré de confiance accorder à cette heure."}
::option[Comme une heure approximative attribuée à ce signalement.]{#incident-timelines-estimated-time-b .correct explanation="Vous conservez ainsi ce que dit la source et le degré de précision."}
:::

## Ordonner les événements avant de rechercher la cause

Un déploiement peut précéder un problème de service sans en être la cause. Vérifiez si la route touchée a changé et si d’autres signaux appuient ce lien. Gardez les questions ouvertes visibles à côté de la chronologie.

:::single-choice{#incident-timelines-timeline-cause} Qu’établit la chronologie à elle seule ?

::option[Le déploiement a provoqué la panne publique.]{#incident-timelines-timeline-cause-a explanation="L’ordre suggère une piste. Il ne suffit pas à établir la cause."}
::option[Le déploiement consigné précède le relevé web.]{#incident-timelines-timeline-cause-c .correct explanation="C’est la relation temporelle que les entrées démontrent."}
::option[Aucun autre événement ne peut être pertinent.]{#incident-timelines-timeline-cause-b explanation="La chronologie contient une sélection d’observations."}
:::

## Résumé

Vous savez maintenant construire une chronologie où les preuves et les incertitudes restent visibles.

1. Convertissez les heures consignées vers un fuseau commun.
2. Indiquez la source de chaque heure et signalez les estimations.
3. Appuyez-vous sur la chronologie pour choisir les prochaines vérifications.
