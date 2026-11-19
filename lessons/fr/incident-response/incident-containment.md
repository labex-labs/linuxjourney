---
lesson_id: "incident-containment"
course_id: "incident-response"
lang: "fr"
order_index: 4
title: "Confinement"
description: "Apprenez à comparer des mesures de confinement approuvées selon leur objectif, leur impact et les éléments à préserver."
meta_title: "Confinement - Réponse aux incidents"
meta_description: "Apprenez à comparer des mesures de confinement approuvées selon leur objectif, leur impact et les éléments à préserver."
meta_keywords: "confinement, réponse aux incidents, cybersécurité, Linux Journey"
---

Le **confinement** est une mesure de courte durée qui vise à limiter les dommages pendant l’enquête. La mesure appropriée dépend de ce qui est touché et des accès dont les personnes ont encore besoin.

## Définir le périmètre du confinement

Imaginez qu’un panneau de prévisualisation interne soit accessible par une route publique et que la page d’accueil doive rester accessible. Une option consiste à restreindre la route vers la prévisualisation. Une mesure plus large serait de mettre tout le site hors ligne. Comparez les effets de chaque option.

:::single-choice{#incident-containment-narrow-action} Quel choix répond le mieux à l’objectif de fermer l’accès public à la prévisualisation tout en gardant la page d’accueil disponible ?

::option[Désactiver toutes les routes publiques quel que soit leur rôle.]{#incident-containment-narrow-action-b explanation="Cela désactiverait aussi la page d’accueil."}
::option[Restreindre la route de prévisualisation concernée et vérifier les deux chemins.]{#incident-containment-narrow-action-a .correct explanation="Cette mesure vise l’exposition signalée et vérifie que le service nécessaire reste disponible."}
::option[Changer le nom du service de prévisualisation.]{#incident-containment-narrow-action-c explanation="Renommer le service n’empêche pas les requêtes de l’atteindre."}
:::

## Prévoir la conservation des preuves et des accès

Consultez le plan de réponse et les personnes habilitées à effectuer la modification. Notez qui l’a approuvée, combien de temps elle doit durer et quels éléments préserver en priorité si la situation le permet. Vérifiez si la mesure pourrait interrompre la journalisation du service ou couper l’accès aux personnes chargées d’intervenir.

:::single-choice{#incident-containment-action-impact} Une mesure d’isolement envisagée pourrait aussi empêcher les enquêteurs de récupérer les journaux. Que doit examiner l’équipe ?

::option[Les éléments à préserver et la manière de maintenir l’accès des personnes autorisées.]{#incident-containment-action-impact-b .correct explanation="Cela tient compte de l’objectif de confinement et des besoins de l’enquête."}
::option[Uniquement si le fichier de configuration porte un nom court.]{#incident-containment-action-impact-a explanation="Le nom du fichier ne préserve ni les journaux ni l’accès."}
::option[S’il faut publier les données d’authentification pour que tout le monde puisse se reconnecter.]{#incident-containment-action-impact-c explanation="Les données d’authentification doivent rester protégées et les accès contrôlés."}
:::

## Vérifier une mesure de confinement

Vérifiez que l’accès non prévu est fermé. Testez séparément un accès prévu pour repérer d’éventuels effets secondaires. Notez quand vous avez appliqué la mesure et quand l’équipe doit la réévaluer. Le confinement peut réussir alors que la cause du problème reste à déterminer.

:::single-choice{#incident-containment-containment-success} La route publique vers la prévisualisation est fermée et la page d’accueil fonctionne toujours. Quel constat ces contrôles permettent-ils ?

::option[La cause profonde a forcément été corrigée.]{#incident-containment-containment-success-a explanation="Les contrôles confirment le périmètre d’accès. La réparation reste à établir."}
::option[Tous les chemins possibles vers la prévisualisation ont été testés.]{#incident-containment-containment-success-b explanation="Ces contrôles couvrent les chemins utilisés pour les tests."}
::option[L’accès public testé à la prévisualisation est bloqué et la page d’accueil attendue reste disponible.]{#incident-containment-containment-success-c .correct explanation="Ce constat reste dans le périmètre vérifié."}
:::

## Résumé

Vous savez maintenant évaluer une mesure de confinement de courte durée.

1. Indiquez le chemin ou l’accès que la mesure doit restreindre.
2. Vérifiez l’autorisation, les éléments à préserver et les effets attendus.
3. Vérifiez séparément la restriction prévue et le service indispensable.
