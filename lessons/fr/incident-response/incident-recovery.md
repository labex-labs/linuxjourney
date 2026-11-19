---
lesson_id: "incident-recovery"
course_id: "incident-response"
lang: "fr"
order_index: 5
title: "Rétablissement"
description: "Apprenez à vérifier que le service est dans l’état approuvé avant de déclarer le rétablissement terminé."
meta_title: "Rétablissement - Réponse aux incidents"
meta_description: "Apprenez à vérifier que le service est dans l’état approuvé avant de déclarer le rétablissement terminé."
meta_keywords: "rétablissement, réponse aux incidents, cybersécurité, Linux Journey"
---

Le **rétablissement** consiste à remettre le service dans l’état attendu et à vérifier qu’il reste utilisable. Le démarrage d’un processus est un premier signal. L’équipe doit également vérifier que la configuration, les dépendances et le comportement visible par les utilisateurs correspondent à l’état attendu.

## Identifier l’état restauré

Notez la version candidate et la configuration approuvées. Si un service a été isolé, vérifiez quels accès doivent rester restreints. Rouvrir un chemin peut modifier le périmètre du confinement.

:::single-choice{#incident-recovery-restore-target} Quel résultat indique si vous avez restauré la version prévue ?

::option[Un horodatage récent sur une machine virtuelle sans rapport.]{#incident-recovery-restore-target-b explanation="Cela n’identifie pas le service restauré."}
::option[Une liste des paquets disponibles, à elle seule.]{#incident-recovery-restore-target-c explanation="La liste des paquets disponibles ne montre pas ce qui traite les requêtes."}
::option[Une réponse ou une fiche de déploiement qui identifie la version approuvée sur la cible.]{#incident-recovery-restore-target-a .correct explanation="Ce résultat relie le service en activité à la version choisie par l’équipe."}
:::

## Vérifier de nouveau le problème signalé

Dans l’incident simulé, les visiteurs ont vu le code `503` sur la page d’accueil publique. Après le rétablissement, demandez cette même page depuis un emplacement de test adapté. Vérifiez que la requête produit le résultat attendu et surveillez les erreurs récentes. Une prévisualisation interne réussie laisse la route publique sans contrôle.

:::single-choice{#incident-recovery-verify-original-path} Quel test montre le mieux que le symptôme initial a disparu pour les utilisateurs ?

::option[Vérifier uniquement que le fichier exécutable du service existe.]{#incident-recovery-verify-original-path-a explanation="Le fichier peut être présent sans traiter les requêtes publiques."}
::option[Vérifier la page d’accueil publique en passant par le chemin client pertinent.]{#incident-recovery-verify-original-path-b .correct explanation="Ce contrôle reproduit l’observation qui avait initialement échoué."}
::option[Vérifier seulement la prévisualisation interne.]{#incident-recovery-verify-original-path-c explanation="Ce chemin diffère de la route touchée."}
:::

## Poursuivre l’observation

Convenez d’une période d’observation courte et de critères de réussite. Examinez les signaux pertinents, comme les erreurs, la latence ou les refus d’accès. Consignez les éventuelles limites, les actions qui restent à effectuer et l’heure du prochain examen. Conservez les preuves du rétablissement dans le dossier d’incident.

:::single-choice{#incident-recovery-observation-period} Le premier contrôle réussit, mais la panne était intermittente. Que faire avant de clore la vérification du rétablissement ?

::option[Continuer à surveiller les signaux convenus pendant la période d’observation.]{#incident-recovery-observation-period-c .correct explanation="Cela aide à établir que le comportement rétabli se maintient."}
::option[Clore immédiatement la vérification parce qu’une réponse est arrivée.]{#incident-recovery-observation-period-a explanation="Une seule observation peut manquer un problème intermittent."}
::option[Jeter toutes les données de comparaison.]{#incident-recovery-observation-period-b explanation="Les résultats précédents permettent de mesurer l’amélioration."}
:::

## Résumé

Vous savez maintenant vérifier l’état du service et ce que voient les utilisateurs après le rétablissement.

1. Identifiez la version et la configuration approuvées.
2. Testez de nouveau le symptôme visible par les utilisateurs.
3. Observez les signaux convenus avant de clore la vérification du rétablissement.
