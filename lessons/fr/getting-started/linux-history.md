---
lesson_id: "linux-history"
course_id: "getting-started"
lang: "fr"
order_index: 1
title: "Histoire de Linux"
description: "Découvrez comment UNIX, GNU et le noyau Linux ont contribué aux systèmes Linux modernes."
meta_title: "Histoire de Linux - Premiers pas"
meta_description: "Commencez votre parcours Linux en découvrant ses origines : UNIX, le projet GNU et la création du noyau Linux par Linus Torvalds."
meta_keywords: "histoire de Linux, parcours Linux, UNIX, projet GNU, Linus Torvalds, noyau Linux, Linux débutant"
---

Bienvenue dans votre **parcours Linux** ! Si vous êtes prêt à découvrir le puissant univers de Linux, vous êtes au bon endroit. Je m'appelle Penguin Pete et je serai votre guide. Pour commencer, explorons brièvement l'**histoire de Linux**.

## Les prédécesseurs de Linux

Pour comprendre la création de Linux, remontons à 1969, lorsque Ken Thompson et Dennis Ritchie, des laboratoires Bell, ont développé le système d'exploitation UNIX. Celui-ci a ensuite été réécrit dans le langage de programmation C, ce qui l'a rendu portable et a favorisé sa large adoption.

![Chronologie d'Unix](https://file.labex.io/images/ed9c245d-e8be-4287-bf34-67750b042542.jpg)

:::single-choice{#understand-unix-portability}
Quel résultat important la réécriture d'UNIX en C a-t-elle produit ?

::option[Il est devenu le noyau libre créé pour le système GNU.]{#unix-became-gnu-kernel explanation="UNIX existait avant le projet GNU et n'était pas son noyau. GNU a ensuite commencé à développer un noyau distinct appelé Hurd."}
::option[Il est devenu plus facile à porter sur différents systèmes matériels.]{#portable-across-hardware .correct explanation="L'écriture d'UNIX en C l'a rendu plus portable. Cette portabilité a favorisé sa diffusion au-delà de son matériel d'origine."}
::option[Il est devenu un shell de commandes utilisé uniquement aux laboratoires Bell.]{#unix-became-shell explanation="UNIX est un système d'exploitation, pas seulement un shell. Sa réécriture en C a favorisé son adoption hors des laboratoires Bell."}
:::

Plus de dix ans après, Richard Stallman a lancé le projet GNU. GNU est un acronyme récursif de « GNU's Not UNIX » et son objectif était de créer un système d'exploitation de type UNIX entièrement libre et open source. Le projet a produit de nombreux composants essentiels ainsi que la GNU General Public License (GPL), mais son propre noyau, GNU Hurd, n'était pas prêt pour un usage général lorsque Linux est devenu disponible.

:::single-choice{#identify-gnu-missing-component}
Quel composant majeur de GNU n'était pas prêt lorsque Linux est devenu disponible ?

::option[Un noyau prêt pour la production]{#gnu-kernel .correct explanation="GNU avait produit de nombreux composants système, mais son propre noyau, GNU Hurd, n'était pas prêt pour un usage général."}
::option[Une licence de logiciel libre]{#gnu-license explanation="Le projet GNU avait déjà produit la GNU General Public License. Le composant système manquant était un noyau utilisable."}
::option[Des outils système essentiels]{#gnu-tools explanation="GNU avait déjà produit de nombreux outils essentiels. Son noyau restait la principale partie inachevée du système."}
:::

## Le rôle du noyau

Le noyau est le composant central d'un système d'exploitation. Il sert de pont et permet au matériel de communiquer avec les logiciels. Il gère les ressources du système, notamment le processeur, la mémoire et les périphériques. Un système d'exploitation complet a besoin de ce cœur chargé des ressources, en plus des outils et applications utilisés par les personnes.

:::single-choice{#recognize-kernel-role}
Quelle responsabilité appartient au noyau du système d'exploitation ?

::option[Écrire chaque commande saisie dans le shell]{#write-shell-commands explanation="Les personnes ou les scripts fournissent les commandes du shell. Le noyau procure les ressources de bas niveau nécessaires à leur exécution."}
::option[Choisir la licence de chaque application installée]{#choose-software-licenses explanation="Les auteurs et distributeurs choisissent les licences des applications. Ce choix ne relève pas de la gestion des ressources par le noyau."}
::option[Gérer le processeur, la mémoire et les périphériques connectés]{#manage-system-resources .correct explanation="Le noyau gère les ressources matérielles et les met à la disposition des logiciels. Le temps processeur, la mémoire et les périphériques en sont des exemples essentiels."}
:::

## La naissance du noyau Linux

Nous arrivons ainsi en 1991, lorsqu'un étudiant finlandais nommé Linus Torvalds commence à développer un nouveau noyau comme projet personnel. Ce noyau deviendra le noyau Linux. Après la publication de Linux comme logiciel libre en 1992, il a pu être associé au système GNU presque complet pour former un système d'exploitation libre complet, couramment appelé GNU/Linux. Cette étape a marqué un tournant dans l'**histoire de Linux**.

![Linus Torvalds en 2018](https://file.labex.io/images/3e1311fd-b8ca-45e7-8d02-9aac6377bb36.jpg)

_Linus Torvalds en 2018 (source : [Wikipédia](https://fr.wikipedia.org/wiki/Linus_Torvalds))_

:::single-choice{#identify-linux-kernel-creator}
Qui a commencé à développer le noyau Linux en 1991 ?

::option[Richard Stallman]{#richard-stallman explanation="Richard Stallman a lancé le projet GNU. GNU a fourni de nombreux composants système, mais Linus Torvalds a commencé le noyau Linux."}
::option[Dennis Ritchie]{#dennis-ritchie explanation="Dennis Ritchie a contribué au développement d'UNIX et du langage C. Le projet de noyau Linux a été lancé plus tard par Linus Torvalds."}
::option[Linus Torvalds]{#linus-torvalds .correct explanation="Linus Torvalds a lancé le projet de noyau en 1991. Ce projet est devenu le noyau Linux."}
:::

Pour poursuivre votre **parcours Linux**, essayez ces laboratoires pratiques afin de vous exercer aux commandes fondamentales et de prendre confiance dans l'environnement en ligne de commande.

1. **[Premiers pas avec Linux](https://labex.io/fr/labs/linux-getting-started-with-linux-446315)** — Commencez votre parcours Linux avec des commandes essentielles du terminal comme `echo`, `date` et des calculs simples. Idéal pour les débutants complets.
2. **[Votre premier laboratoire Linux](https://labex.io/fr/labs/linux-your-first-linux-lab-270253)** — Ce laboratoire d'introduction vous guide dans le classique « Hello, World! » sous Linux et vous enseigne quelques commandes fondamentales.
3. **[Créer un message d'accueil personnalisé dans le terminal](https://labex.io/fr/labs/linux-create-personalized-terminal-greeting-446322)** — Un défi court et ludique qui emploie les commandes élémentaires du terminal Linux pour créer un message de bienvenue attrayant.

## Résumé

Vous savez maintenant expliquer comment UNIX, GNU et le noyau Linux ont contribué aux systèmes Linux modernes.

1. Décrire pourquoi la portabilité d'UNIX était importante.
2. Identifier le noyau comme le principal composant manquant de GNU.
3. Expliquer le rôle du noyau dans la gestion des ressources système.
4. Identifier Linus Torvalds comme créateur du noyau Linux.
