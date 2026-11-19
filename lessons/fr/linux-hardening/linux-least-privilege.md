---
lesson_id: "linux-least-privilege"
course_id: "linux-hardening"
lang: "fr"
order_index: 3
title: "Moindre privilège"
description: "Apprenez à choisir les permissions sur les fichiers et les droits d’administration nécessaires à une tâche de service."
meta_title: "Moindre privilège - Durcissement de Linux"
meta_description: "Apprenez à choisir les permissions sur les fichiers et les droits d’administration nécessaires à une tâche de service."
meta_keywords: "moindre privilège, durcissement de Linux, cybersécurité, Linux Journey"
---

Le **moindre privilège** consiste à donner à un compte les accès nécessaires à son travail. Commencez par nommer les actions. Le compte peut avoir besoin de lire un fichier et d’en écrire un autre, sans effectuer de tâches d’administration.

## Adapter les droits au travail

Un processus web doit lire `index.html`. Le compte de déploiement met le fichier à jour. Ces deux tâches peuvent utiliser des permissions différentes. Le processus web peut lire la page et le compte de déploiement peut y écrire.

:::single-choice{#linux-least-privilege-read-only-page} De quelle permission sur la page le processus web a-t-il besoin dans cet exemple ?

::option[L’accès en lecture.]{#linux-least-privilege-read-only-page-a .correct explanation="Pour servir le fichier, il doit en lire le contenu."}
::option[L’accès en écriture.]{#linux-least-privilege-read-only-page-b explanation="C’est le compte de déploiement qui modifie la page."}
::option[Le droit d’administrer des services sans rapport avec le site.]{#linux-least-privilege-read-only-page-c explanation="Ce travail sort du rôle du processus web."}
:::

## Vérifier l’ensemble du chemin

Les permissions du fichier ne sont qu’une partie de la vérification. Sous Linux, il faut aussi pouvoir traverser les répertoires qui mènent au fichier. Sur un répertoire, la permission d’exécution permet à un programme de le traverser s’il connaît le nom de l’élément recherché. Si le processus ne peut pas traverser un répertoire du chemin, il ne peut pas atteindre le fichier, même si celui-ci est lisible.

:::single-choice{#linux-least-privilege-path-boundary} Les permissions du fichier index.html permettent au processus de le lire, mais celui-ci ne peut pas accéder au répertoire parent. Que faut-il examiner ?

::option[Si la page est plus volumineuse.]{#linux-least-privilege-path-boundary-a explanation="La taille ne donne aucun accès au répertoire."}
::option[S’il faut laisser tout le monde modifier la page.]{#linux-least-privilege-path-boundary-c explanation="Le droit d’écriture ne corrige pas l’absence d’accès au chemin."}
::option[Le droit du processus de traverser le répertoire.]{#linux-least-privilege-path-boundary-b .correct explanation="Le processus doit pouvoir suivre le chemin et lire le fichier."}
:::

## Limiter les actions privilégiées

Des outils d’administration comme `sudo` peuvent autoriser un utilisateur approuvé à effectuer certaines tâches de maintenance. Définissez l’action, les personnes autorisées et la manière de vérifier le nouvel accès. Assurez-vous que la maintenance approuvée fonctionne toujours et qu’une action administrative sans rapport reste interdite par la même politique.

:::single-choice{#linux-least-privilege-policy-test} Un rôle de maintenance doit pouvoir consulter l’état du service. Quel plan de test vérifie le mieux les droits prévus ?

::option[Vérifier que toutes les commandes d’administration fonctionnent désormais.]{#linux-least-privilege-policy-test-a explanation="Ces droits supplémentaires dépasseraient les besoins de la tâche documentée."}
::option[Vérifier que le rôle peut consulter l’état et que les modifications privilégiées sans rapport restent restreintes.]{#linux-least-privilege-policy-test-c .correct explanation="Cela vérifie l’accès nécessaire et la limite prévue."}
::option[Vérifier uniquement que le nom d’utilisateur existe.]{#linux-least-privilege-policy-test-b explanation="L’existence du compte ne renseigne pas sur ses droits."}
:::

## Résumé

Vous savez maintenant déterminer les accès minimaux nécessaires à une tâche.

1. Distinguez les actions de lecture, d’écriture et d’administration.
2. Vérifiez l’accès à travers les répertoires d’un chemin.
3. Pour chaque rôle, vérifiez les actions autorisées et celles qui doivent rester restreintes.
