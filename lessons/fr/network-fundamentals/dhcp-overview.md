---
lang: "fr"
title: "Présentation du DHCP"
meta_description: "Découvrez le DHCP (Dynamic Host Configuration Protocol) sous Linux. Comprenez comment DHCP attribue les adresses IP et son processus en quatre étapes. Commencez votre parcours de mise en réseau Linux !"
meta_keywords: "DHCP, Dynamic Host Configuration Protocol, réseau Linux, adresse IP, tutoriel DHCP, débutant, guide"
---

## Lesson Content

Un concept de réseau important que nous n'avons pas encore abordé est le DHCP (Dynamic Host Configuration Protocol).

DHCP attribue des adresses IP, des masques de sous-réseau et des passerelles à nos machines. Par exemple, disons que vous avez un téléphone portable et que vous voulez obtenir un numéro de téléphone portable pour commencer à parler aux gens. Vous devez appeler votre opérateur téléphonique, et il vous donnera un numéro. Tant que vous payez vos factures, vous pouvez continuer à utiliser votre téléphone. DHCP est l'opérateur téléphonique dans ce cas ; il vous donne une adresse IP afin que vous puissiez parler à d'autres adresses IP. Une adresse IP vous est également louée ; celles-ci durent une certaine période de temps, puis seront renouvelées en fonction de vos paramètres de bail.

DHCP est excellent pour de nombreuses raisons : il permet à un administrateur réseau de ne pas se soucier de l'attribution des adresses IP, et il les empêche également de configurer des adresses IP en double. Chaque réseau physique devrait avoir son propre serveur DHCP afin qu'un hôte puisse demander une adresse IP. Dans un cadre domestique ordinaire, le routeur agit généralement comme serveur DHCP.

La façon dont DHCP obtient toutes vos informations d'hôte dynamique est la suivante :

1. DHCP DISCOVER - Ce message est diffusé pour rechercher un serveur DHCP.
2. DHCP OFFER - Le serveur DHCP du réseau répond avec un message d'offre. L'offre contient un paquet avec le temps de bail DHCP, le masque de sous-réseau, l'adresse IP, etc.
3. DHCP REQUEST - Le client envoie une autre diffusion pour faire savoir à tous les serveurs DHCP quelle offre il a acceptée.
4. DHCP ACK - Un accusé de réception est envoyé par le serveur.

DHCP est plus complexe que cela, mais c'est l'essentiel.

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Quelles sont les étapes d'une requête DHCP ?

## Quiz Answer

DISCOVER, OFFER, REQUEST, ACK
