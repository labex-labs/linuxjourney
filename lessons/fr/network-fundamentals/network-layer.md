---
index: 7
lang: "fr"
title: "Couche Réseau"
meta_title: "Couche Réseau - Bases du Réseau"
meta_description: "Découvrez la couche Réseau sous Linux, comment les adresses IP acheminent les paquets à travers les sous-réseaux, et son rôle dans la transmission de données. Commencez votre parcours de mise en réseau Linux !"
meta_keywords: "Couche Réseau, adresses IP, subnets, mise en réseau Linux, routage de paquets, débutant, tutoriel, guide"
---

## Lesson Content

La couche Réseau détermine le routage de nos paquets de notre hôte source vers un hôte de destination. Heureusement, dans notre exemple, notre paquet ne voyage qu'au sein du même réseau, mais Internet est composé de nombreux réseaux. Ces réseaux plus petits qui composent Internet sont appelés des subnets. Tous les subnets se connectent les uns aux autres d'une manière ou d'une autre, c'est pourquoi nous pouvons accéder à `https://www.google.com` même s'il se trouve sur son propre réseau. Je n'entrerai pas dans les détails car nous avons un cours entier dédié aux subnets, mais pour l'instant, en ce qui concerne notre couche Réseau, sachez que les adresses IP définissent les règles pour voyager vers différents subnets.

Dans la couche Réseau, elle reçoit le segment provenant de la couche Transport et encapsule ce segment dans un paquet IP, puis attache l'adresse IP de l'hôte source et l'adresse IP de l'hôte de destination à l'en-tête du paquet. Donc, à ce stade, notre paquet contient des informations sur sa destination et son origine. Maintenant, il envoie notre paquet à la couche matérielle physique.

## Exercise

No exercises for this lesson.

## Quiz Question

Comment appelle-t-on les réseaux plus petits qui composent Internet ?

## Quiz Answer

subnets
