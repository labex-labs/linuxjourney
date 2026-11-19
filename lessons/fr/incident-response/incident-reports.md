---
lesson_id: "incident-reports"
course_id: "incident-response"
lang: "fr"
order_index: 6
title: "Rapports d’incident"
description: "Apprenez à rédiger un point d’étape concis fondé sur les observations et les questions qui restent ouvertes."
meta_title: "Rapports d’incident - Réponse aux incidents"
meta_description: "Apprenez à rédiger un point d’étape concis fondé sur les observations et les questions qui restent ouvertes."
meta_keywords: "rapports d’incident, réponse aux incidents, cybersécurité, Linux Journey"
---

Un rapport d’incident court aide une autre personne à prendre le relais sans reconstituer toute l’enquête. Indiquez le service touché, quelques observations horodatées et la prochaine action.

## Rapporter les observations

Voici trois entrées simulées décrivant un incident de service.

```text
09:17 UTC  Deployment record: version 3 reached production
09:22 UTC  Visitor-path check: homepage returned 503
09:31 UTC  After rollback: version 2, homepage returned 200
```

Ces entrées décrivent une modification, un échec et un contrôle réussi après le rétablissement. Indiquez le chemin touché et l’heure. Précisez ce qui a été testé.

:::single-choice{#incident-reports-report-claim} Quel constat pouvez-vous tirer directement des entrées ?

::option[Le contrôle de la page d’accueil a échoué à 09:22 et a réussi après le retour à la version précédente.]{#incident-reports-report-claim-b .correct explanation="Ce constat résume les résultats observés et leur ordre."}
::option[La version 3 a forcément mis la base de données en panne.]{#incident-reports-report-claim-a explanation="Les entrées ne montrent pas comment la panne s’est produite."}
::option[Tous les utilisateurs ont été touchés pendant toute la période.]{#incident-reports-report-claim-c explanation="Les résultats fournis ne couvrent pas toutes les requêtes."}
:::

![Éléments simulés d’un incident montrant une modification en production, un code 503 et un contrôle de rétablissement réussi](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-reports/evidence-timeline.png)

## Expliquer ce qui reste incertain

Un retour à la version précédente suivi d’une requête réussie peut justifier d’examiner le déploiement. Laissez la cause ouverte jusqu’à disposer d’éléments qui l’établissent. Par exemple, une personne chargée de la maintenance peut comparer les journaux des deux versions pendant la période des requêtes en échec.

:::single-choice{#incident-reports-uncertainty-statement} Quelle phrase exprime une question encore ouverte ?

::option[Il n’y a rien d’utile à examiner.]{#incident-reports-uncertainty-statement-b explanation="Les traces du déploiement et des erreurs aident à cibler la prochaine vérification."}
::option[Le service est resté indisponible pour toujours.]{#incident-reports-uncertainty-statement-c explanation="La requête de test réussie qui a suivi contredit ce constat."}
::option[La cause du code 503 reste indéterminée.]{#incident-reports-uncertainty-statement-a .correct explanation="Les éléments recueillis montrent un échec puis un contrôle de rétablissement. Il reste à établir la cause."}
:::

## Confier une tâche à la personne qui prend le relais

Précisez qui peut effectuer la prochaine action, quelles entrées rechercher et quel résultat répondrait à la question ouverte. Retirez les secrets et les données personnelles des points d’étape diffusés largement. Un rapport court peut renvoyer vers des éléments protégés pour les personnes autorisées à les examiner.

:::single-choice{#incident-reports-useful-handoff} Quelle prochaine action découle le mieux de ce cas ?

::option[Demander une capture d’écran générale sans préciser l’heure ni le service.]{#incident-reports-useful-handoff-a explanation="Cette demande ne précise pas quels éléments permettraient d’examiner la panne."}
::option[Demander à la personne chargée de la maintenance du service d’examiner les journaux de la version 3 sur la période des échecs de la page d’accueil.]{#incident-reports-useful-handoff-c .correct explanation="Cette action précise la source et la période à examiner pour répondre à la question ouverte."}
::option[Demander à la personne chargée de la maintenance de répéter uniquement le contrôle déjà réussi de la version 2.]{#incident-reports-useful-handoff-b explanation="Ce contrôle peut confirmer de nouveau le rétablissement. Il n’expliquera pas l’échec antérieur de la version 3."}
:::

## Préciser le périmètre du rétablissement

Un rapport peut avoir à consigner un contrôle de rétablissement et un impact encore à estimer. Le contrôle réussi de la page d’accueil après le retour à la version précédente confirme le rétablissement pour le chemin testé. Pour estimer le nombre de visiteurs touchés, il faut encore des décomptes de requêtes ou d’autres observations pertinentes sur la période de la panne.

:::single-choice{#incident-reports-final-application} Quelle note de transmission décrit fidèlement les deux types d’éléments ?

::option[L’accès a été rétabli pour tous les visiteurs, car une requête a renvoyé 200.]{#incident-reports-final-application-b explanation="La requête réussie vérifie uniquement le chemin à l’heure du test."}
::option[Le contrôle en échec doit être retiré du rapport puisque le rétablissement a été vérifié.]{#incident-reports-final-application-c explanation="L’échec initial fait partie des preuves de l’incident."}
::option[Le contrôle de la page d’accueil a réussi après le retour à la version précédente et le nombre total de requêtes touchées reste inconnu.]{#incident-reports-final-application-a .correct explanation="Le rapport distingue le résultat vérifié du décompte que les données actuelles ne fournissent pas."}
:::

Pour un exercice plus long après vous être entraîné à examiner les paquets et les traces d’hôte, consultez [Révision des bases du SOC](https://labex.io/courses/project-soc-foundations-review).

## Résumé

Vous savez maintenant transmettre un dossier d’incident avec les faits, les incertitudes et la prochaine action.

1. Indiquez le chemin touché et la chronologie observée.
2. Distinguez une cause soupçonnée des éléments confirmés.
3. Attribuez une action de suivi qui précise une source et une période.
