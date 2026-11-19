---
lesson_id: "service-monitoring-signals"
course_id: "service-monitoring"
lang: "fr"
order_index: 1
title: "Signaux de supervision"
description: "Apprenez à choisir un signal de supervision qui répond à une question sur un service web."
meta_title: "Signaux de supervision - Supervision des services"
meta_description: "Apprenez à choisir un signal de supervision qui répond à une question sur un service web."
meta_keywords: "signaux de supervision, supervision des services, DevOps, Linux Journey"
---

Un visiteur trouve la page lente. Partez de son expérience, puis choisissez une mesure capable de la décrire. Un **signal** est une observation telle qu’un décompte, une mesure ou un événement enregistré.

## Vérifier l’expérience de l’utilisateur

La **disponibilité** indique si le service peut effectuer le travail attendu. Un contrôle pourrait demander la page d’accueil et vérifier que la réponse est un succès. La **latence** est le temps que prend la requête. Une page peut s’ouvrir correctement après plusieurs secondes.

:::single-choice{#service-monitoring-signals-slow-page} Les visiteurs reçoivent la page, mais cela prend plusieurs secondes. Quel signal décrit le plus directement ce symptôme ?

::option[Le nombre de conteneurs sur le serveur.]{#service-monitoring-signals-slow-page-b explanation="Ce nombre ne mesure pas l’attente des visiteurs."}
::option[Le temps nécessaire pour recevoir la page.]{#service-monitoring-signals-slow-page-a .correct explanation="La latence mesure la durée de la requête."}
::option[Le nombre d’octets dans le dépôt de code source.]{#service-monitoring-signals-slow-page-c explanation="La taille du dépôt ne renseigne pas sur la durée des requêtes."}
:::

## Compter les requêtes et les erreurs

Le **trafic** représente la demande adressée au service, par exemple en requêtes par minute. Suivez le total et le nombre de requêtes en échec. Cinq erreurs pour 1 000 requêtes représentent une situation différente de cinq erreurs pour dix requêtes.

:::single-choice{#service-monitoring-signals-count-context} Vous voyez cinq échecs sur chacune de deux périodes. Quelle information aide à comparer les conséquences pour les utilisateurs ?

::option[Le nombre total de requêtes sur chaque période.]{#service-monitoring-signals-count-context-b .correct explanation="Il faut le dénominateur de chaque décompte pour comparer les taux d’erreur."}
::option[Le nom du tableau de bord.]{#service-monitoring-signals-count-context-a explanation="Le nom indique où figure le graphique, sans mesurer le trafic."}
::option[L’ordre des services dans la liste.]{#service-monitoring-signals-count-context-c explanation="L’ordre de la liste ne mesure pas le nombre de requêtes touchées."}
:::

## Évaluer la pression sur les ressources

La **saturation** indique à quel point une ressource approche de sa capacité maximale. Un service peut attendre que sa base de données termine des opérations alors même que le processus web fonctionne. Comparez ce que voient les utilisateurs à la mesure de la ressource avant de tirer une conclusion.

:::single-choice{#service-monitoring-signals-saturation-check} Les requêtes ralentissent au moment où la file d’attente s’allonge. Quelle suite est raisonnable ?

::option[Affirmer que la file d’attente est certainement la cause profonde.]{#service-monitoring-signals-saturation-check-a explanation="Les deux changements donnent une piste. Il faut davantage d’éléments pour établir un lien de causalité."}
::option[Recompter les images stockées sur l’hôte.]{#service-monitoring-signals-saturation-check-b explanation="La disponibilité des images n’explique pas la file de requêtes en attente."}
::option[Examiner la ressource qui traite le travail en attente.]{#service-monitoring-signals-saturation-check-c .correct explanation="Vous pourrez voir si cette ressource peine à suivre la demande."}
:::

## Résumé

Vous savez maintenant choisir un signal à partir de ce qu’a remarqué un utilisateur.

1. Distinguez disponibilité et latence.
2. Interprétez les échecs en tenant compte du volume de requêtes.
3. Utilisez la saturation comme indice sur la capacité disponible.
