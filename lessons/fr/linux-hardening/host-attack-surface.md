---
lesson_id: "host-attack-surface"
course_id: "linux-hardening"
lang: "fr"
order_index: 1
title: "Surface d’attaque"
description: "Apprenez à déterminer ce qu’un hôte Linux doit exposer et quels accès méritent un examen."
meta_title: "Surface d’attaque - Durcissement de Linux"
meta_description: "Apprenez à déterminer ce qu’un hôte Linux doit exposer et quels accès méritent un examen."
meta_keywords: "surface d’attaque, durcissement de Linux, cybersécurité, Linux Journey"
---

Un hôte Linux peut héberger une page web publique, offrir un accès de maintenance et exécuter des services en arrière-plan. Notez d’abord le rôle de chaque service et qui doit pouvoir y accéder. Vous pourrez alors repérer les accès dont l’utilité reste à établir.

## Recenser les accès prévus

Un inventaire simple associe chaque ressource aux personnes ou aux programmes qui en ont besoin. Voici un hôte d’exercice.

```text
Resource           Intended access
Public homepage    Visitors
Maintenance SSH    Operations team
Preview panel      Local staff on this host only
```

Un **chemin d’accès** est un moyen pour un utilisateur ou un programme d’atteindre une ressource. Les interfaces accessibles par lesquelles quelqu’un pourrait agir sur un système font partie de sa **surface d’attaque**.

:::single-choice{#host-attack-surface-intended-audience} Quelle ressource de cet inventaire doit être accessible depuis le réseau public ?

::option[L’accès SSH de maintenance.]{#host-attack-surface-intended-audience-b explanation="Il est destiné à l’équipe d’exploitation."}
::option[La page d’accueil publique.]{#host-attack-surface-intended-audience-a .correct explanation="Elle est destinée, entre autres, aux visiteurs extérieurs à l’hôte."}
::option[Le panneau de prévisualisation.]{#host-attack-surface-intended-audience-c explanation="L’usage indiqué est local à l’hôte."}
:::

## Comparer les accès prévus et observés

Supposons que le panneau de prévisualisation soit accessible par le réseau, alors que l’inventaire le réserve à un usage local. Consultez le responsable et vérifiez le chemin d’accès réel avant de le modifier. Un service peut devoir fonctionner tout en étant réservé aux requêtes locales.

:::single-choice{#host-attack-surface-mismatch} Quelle observation mérite un examen au regard de la politique indiquée ?

::option[Un visiteur peut accéder au panneau de prévisualisation.]{#host-attack-surface-mismatch-b .correct explanation="Le panneau est ainsi accessible à des personnes auxquelles il n’est pas destiné."}
::option[Un visiteur peut charger la page d’accueil.]{#host-attack-surface-mismatch-a explanation="C’est l’usage prévu de la page d’accueil."}
::option[Le personnel peut ouvrir la prévisualisation directement sur l’hôte.]{#host-attack-surface-mismatch-c explanation="L’accès local correspond au besoin indiqué."}
:::

## Choisir les vérifications prioritaires

Commencez par les accès superflus qui peuvent avoir des conséquences importantes. Dans un exercice, un panneau de prévisualisation capable de modifier le site est plus prioritaire qu’un service inutilisé sans données importantes. Notez à qui la ressource est destinée, les accès réellement observés et le test qui confirmerait que la restriction protège le service tout en préservant l’accès légitime.

:::single-choice{#host-attack-surface-priority-check} Après avoir modifié l’accès à la prévisualisation, quelles deux observations confirmeraient que la restriction répond à l’objectif ?

::option[Le panneau accepte toujours une requête locale.]{#host-attack-surface-priority-check-a explanation="Cela confirme l’accès nécessaire sans vérifier l’accès distant non prévu."}
::option[La machine a redémarré et utilise le même nom d’hôte.]{#host-attack-surface-priority-check-b explanation="L’état de l’hôte ne montre pas si la règle d’accès est respectée."}
::option[Le personnel y accède toujours localement et l’accès distant non prévu est fermé.]{#host-attack-surface-priority-check-c .correct explanation="Ces contrôles vérifient à la fois l’accès nécessaire et la restriction."}
:::

## Résumé

Vous savez maintenant repérer les chemins d’accès à examiner pour durcir un hôte.

1. Décrivez la ressource et les personnes ou programmes auxquels elle est destinée.
2. Comparez les accès prévus et observés.
3. Après une modification, vérifiez la protection et l’usage légitime.
