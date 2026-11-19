---
lesson_id: "service-troubleshooting"
course_id: "service-monitoring"
lang: "fr"
order_index: 7
title: "Diagnostic des problèmes de service"
description: "Apprenez à choisir la prochaine vérification en cas d’arrêt de service, d’erreur dans une dépendance ou de requête lente."
meta_title: "Diagnostic des problèmes de service - Supervision des services"
meta_description: "Apprenez à choisir la prochaine vérification en cas d’arrêt de service, d’erreur dans une dépendance ou de requête lente."
meta_keywords: "diagnostic des services, supervision des services, DevOps, Linux Journey"
---

Partez d’un symptôme concret, comme une requête en échec vers la page d’accueil. Comparez ensuite les observations faites à des heures proches et depuis l’endroit pertinent pour les utilisateurs.

## Quand un serveur s’arrête

Dans le premier cas, le navigateur signale un refus de connexion et le conteneur du service affiche `Exited (1)`. Ces deux observations justifient de vérifier pourquoi le programme s’est arrêté. Consultez les journaux conservés. Repérez l’heure de l’arrêt avant de la comparer avec celle des autres événements.

:::single-choice{#service-troubleshooting-stopped-case} Quelle vérification est la plus susceptible d’expliquer l’arrêt du processus ?

::option[Demander de nouveau la même page d’accueil pour obtenir un état plus récent.]{#service-troubleshooting-stopped-case-a explanation="Un nouvel essai vérifie le symptôme. Les journaux conservés peuvent expliquer pourquoi le programme s’est arrêté."}
::option[Lire les dernières lignes disponibles du journal du conteneur.]{#service-troubleshooting-stopped-case-b .correct explanation="Les messages de démarrage ou de sortie peuvent montrer à quelle étape le programme s’est arrêté."}
::option[Examiner les journaux d’un autre conteneur qui utilise la même image et qui fonctionne.]{#service-troubleshooting-stopped-case-c explanation="Cet autre conteneur a son propre historique et peut n’avoir jamais rencontré la panne."}
:::

## Quand une dépendance échoue

Dans le deuxième cas, le processus web tourne, mais la page renvoie une erreur serveur. Son journal signale un dépassement de délai lors de l’appel au catalogue pour la requête `r17`. Examinez donc les entrées de cette dépendance pour la même requête. Un premier service en état de marche ne dit rien sur l’ensemble de la chaîne.

:::single-choice{#service-troubleshooting-dependency-case} Quel élément chercher ensuite pour r17 ?

::option[L’entrée du catalogue pour cette requête à l’heure correspondante.]{#service-troubleshooting-dependency-case-a .correct explanation="Elle montre ce qui s’est passé pendant l’appel à la dépendance."}
::option[La taille de l’image Docker archivée.]{#service-troubleshooting-dependency-case-b explanation="La taille de l’image ne décrit pas l’appel réel."}
::option[Un contrôle réussi de la page d’accueil effectué la veille et sans rapport avec cette requête.]{#service-troubleshooting-dependency-case-c explanation="Ce contrôle décrit un autre moment et ne peut expliquer cette requête."}
:::

## Quand les requêtes ralentissent

Dans un troisième exemple, la plupart des réponses aboutissent, mais des utilisateurs signalent des lenteurs. La latence augmente pendant la période où la file de traitement s’allonge. Examinez la demande et l’activité des processus avant d’attribuer une cause. Après une modification, refaites le contrôle du point de vue de l’utilisateur et examinez les mêmes signaux.

:::single-choice{#service-troubleshooting-slow-case} Quelle comparaison permet le mieux de vérifier si une modification a aidé dans ce cas ?

::option[Des captures d’écran du dépôt de code avant et après.]{#service-troubleshooting-slow-case-a explanation="Ces images ne mesurent ni les durées des requêtes ni les files d’attente."}
::option[La taille du cache comparée au nombre de branches déployées.]{#service-troubleshooting-slow-case-b explanation="Ces données ne renseignent pas sur l’attente signalée."}
::option[Les durées de requêtes comparables et les files de traitement avant et après.]{#service-troubleshooting-slow-case-c .correct explanation="Cette comparaison vérifie le symptôme initial et la contrainte soupçonnée."}
:::

## Interpréter des contrôles contradictoires

Supposons qu’une sonde locale réussisse alors que les utilisateurs voient encore des erreurs. Notez le chemin suivi par chaque contrôle. Une sonde locale peut montrer qu’un processus répond sur l’hôte, tandis qu’une requête côté client révèle un problème sur le chemin qui y mène.

:::single-choice{#service-troubleshooting-final-application} Quel résultat doit guider la suite de l’enquête sur les utilisateurs touchés ?

::option[Un contrôle effectué depuis l’emplacement des utilisateurs et par le même chemin qu’eux.]{#service-troubleshooting-final-application-a .correct explanation="Il observe la partie du service où le symptôme s’est manifesté."}
::option[Uniquement le résultat obtenu sur l’hôte.]{#service-troubleshooting-final-application-b explanation="Ce résultat aide à circonscrire le problème, mais laisse le chemin extérieur sans contrôle."}
::option[La capacité actuelle du registre d’images.]{#service-troubleshooting-final-application-c explanation="Le registre peut fournir des images alors que la route empruntée par les utilisateurs présente un autre problème."}
:::

## Résumé

Vous savez maintenant choisir la prochaine vérification en fonction des éléments disponibles.

1. Utilisez l’état du processus et ses journaux pour examiner un arrêt.
2. Suivez une requête en échec jusqu’à sa dépendance.
3. Vérifiez l’amélioration à partir du symptôme initial visible par l’utilisateur.
