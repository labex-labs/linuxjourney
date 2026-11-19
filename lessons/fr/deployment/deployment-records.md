---
lesson_id: "deployment-records"
course_id: "deployment"
lang: "fr"
order_index: 6
title: "Suivi des déploiements"
description: "Apprenez à reconstituer un déploiement et un retour arrière à partir d’une courte chronologie de mise en service."
meta_title: "Suivi des déploiements - Déploiement"
meta_description: "Apprenez à reconstituer un déploiement et un retour arrière à partir d’une courte chronologie de mise en service."
meta_keywords: "suivi des déploiements, chronologie, retour arrière, DevOps, Linux Journey"
---

Une fiche de déploiement aide une autre personne à relier un résultat visible par les utilisateurs à une modification. Notez d’abord l’heure, l’environnement, la révision source et l’artefact. Ajoutez le résultat du contrôle et les mesures prises ensuite.

## Indiquer ce qui a changé

Cette fiche d’exercice suit un déploiement. Les identifiants sont raccourcis pour faciliter la lecture.

```text
UTC    Target   Commit   Artifact  Observation
09:00  staging  8a61e1   digest-C  version 3, home returned 200
09:12  prod     8a61e1   digest-C  version 3, home returned 503
09:18  prod     72b110   digest-B  version 2, home returned 200
```

HTTP 200 indique une réponse réussie. HTTP 503 indique que le service était indisponible pour cette requête. Dans une fiche réelle, notez aussi la vérification et l’adresse auxquelles correspond le résultat.

:::single-choice{#deployment-records-first-prod-change} Quelle ligne indique le premier résultat observé en production pour digest-C ?

::option[La ligne 09:12 prod.]{#deployment-records-first-prod-change-b .correct explanation="Elle indique la version que l’on a essayé de déployer en production et la vérification en échec."}
::option[La ligne 09:00 staging.]{#deployment-records-first-prod-change-a explanation="Cette vérification s’est déroulée dans un autre environnement."}
::option[La ligne 09:18 prod.]{#deployment-records-first-prod-change-c explanation="Cette ligne décrit un autre artefact après le retour arrière."}
:::

![Chronologie simulée avec une vérification réussie en préproduction, un HTTP 503 en production et le rétablissement de la version 2](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/deployment/deployment-records/release-timeline.png)

## Expliquer le retour arrière

La dernière ligne montre un retour à digest-B. La version vérifiée et le résultat de la requête vers la page d’accueil décrivent ce qui a été observé après le retour arrière. Ils ne suffisent pas à expliquer la cause précise du premier échec. Consignez à part les hypothèses jusqu’à obtenir des éléments qui les étayent.

:::single-choice{#deployment-records-rollback-evidence} Que peut-on dire du résultat de 09:18 ?

::option[L’échec de 09:12 était dû à l’absence d’une base de données.]{#deployment-records-rollback-evidence-b explanation="La fiche ne contient aucun résultat concernant les dépendances."}
::option[Toutes les requêtes ont réussi à partir de cette heure.]{#deployment-records-rollback-evidence-c explanation="Le contrôle réussi renseigne sur cette seule requête."}
::option[La production est revenue à la version 2 et la requête vers la page d’accueil a réussi.]{#deployment-records-rollback-evidence-a .correct explanation="La ligne indique la version rétablie et la réponse HTTP observée."}
:::

## Transmettre la fiche

La personne qui reprend l’examen doit pouvoir reproduire la vérification dans les mêmes conditions. Précisez la méthode, ajoutez l’heure avec le fuseau horaire et, si possible, un lien vers le build. Si la cause reste inconnue, indiquez ce qu’il faut examiner ensuite.

:::single-choice{#deployment-records-handoff-detail} Quel détail aiderait la prochaine personne à répéter la vérification de la page d’accueil ?

::option[Uniquement l’identifiant de la version précédente.]{#deployment-records-handoff-detail-a explanation="Il aide à comparer les versions, mais n’indique ni où ni quand la vérification a été exécutée."}
::option[L’adresse cible exacte et l’heure de la vérification.]{#deployment-records-handoff-detail-c .correct explanation="Avec ces détails, elle pourra vérifier le même chemin et comparer d’autres signaux sur la période concernée."}
::option[L’heure de la création du commit source.]{#deployment-records-handoff-detail-b explanation="L’heure du commit correspond à un événement antérieur. La vérification exige l’heure et la destination de la requête."}
:::

## Consigner l’image réellement utilisée

L’étiquette d’une note de déploiement peut changer de cible après la mise en service. Si le service indique déjà la version 2, notez à la fois l’artefact qu’il exécute et son étiquette lisible. Ces deux informations permettent de comparer la version plus tard, même si l’étiquette a été réattribuée dans le registre.

:::single-choice{#deployment-records-final-application} La note de version indique site:2. Quel détail supplémentaire rendrait une comparaison ultérieure plus fiable ?

::option[L’empreinte obtenue par la dernière personne qui a récupéré site:2.]{#deployment-records-final-application-c explanation="Une récupération ultérieure peut renvoyer un contenu différent de l’image en cours d’exécution."}
::option[L’empreinte complète de l’image réellement exécutée.]{#deployment-records-final-application-a .correct explanation="Elle identifie le contenu utilisé même si l’étiquette pointe plus tard vers un autre objet."}
::option[La même étiquette recopiée dans un deuxième champ.]{#deployment-records-final-application-b explanation="Répéter l’étiquette ne lève pas l’ambiguïté."}
:::

## Résumé

Vous savez maintenant lire une chronologie de déploiement et la transmettre.

1. Repérez l’environnement, la révision et l’artefact dans la fiche.
2. Décrivez le retour arrière à partir du résultat observé.
3. Conservez les détails utiles à la prochaine vérification.
