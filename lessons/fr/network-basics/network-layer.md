---
index: 7
lang: "fr"
title: "Couche réseau"
meta_title: "Couche réseau - Bases du réseau"
meta_description: "Découvrez la couche réseau sous Linux, comment les adresses IP acheminent les paquets à travers les sous-réseaux, et son rôle dans la transmission de données. Commencez votre parcours de mise en réseau Linux !"
meta_keywords: "Couche réseau, adresses IP, sous-réseaux, mise en réseau Linux, routage de paquets, débutant, tutoriel, guide"
---

## Lesson Content

La couche réseau détermine le routage de nos paquets de notre hôte source vers un hôte de destination. Heureusement, dans notre exemple, notre paquet ne voyage qu'au sein du même réseau, mais Internet est composé de nombreux réseaux. Ces réseaux plus petits qui composent Internet sont appelés sous-réseaux. Tous les sous-réseaux se connectent les uns aux autres d'une manière ou d'une autre, c'est pourquoi nous pouvons accéder à `https://www.google.com` même s'il se trouve sur son propre réseau. Je n'entrerai pas dans les détails car nous avons un cours entier dédié aux sous-réseaux, mais pour l'instant, en ce qui concerne notre couche réseau, sachez que les adresses IP définissent les règles pour voyager vers différents sous-réseaux.

Dans la couche réseau, elle reçoit le segment provenant de la couche transport et encapsule ce segment dans un paquet IP, puis attache l'adresse IP de l'hôte source et l'adresse IP de l'hôte de destination à l'en-tête du paquet. Ainsi, à ce stade, notre paquet contient des informations sur sa destination et son origine. Maintenant, il envoie notre paquet à la couche matérielle physique.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la couche réseau, de l'adressage IP et des sous-réseaux :

1. **[Simuler la connectivité de la couche réseau sous Linux](https://labex.io/fr/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Entraînez-vous à attribuer des adresses IP statiques et à tester la connectivité au sein et entre différents sous-réseaux à l'aide de conteneurs Docker.
2. **[Effectuer le sous-réseautage IP et la conversion binaire dans le terminal Linux](https://labex.io/fr/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Maîtrisez le sous-réseautage IP et la conversion binaire, y compris le calcul des hôtes utilisables et des sous-réseaux, directement dans le terminal Linux.
3. **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explorez différents types d'adresses IP (privées, publiques, multicast) et testez la joignabilité du réseau à l'aide de `ping` et `ip a`.

Ces laboratoires vous aideront à appliquer les concepts d'adressage IP et de sous-réseautage dans des scénarios réels et à renforcer votre confiance dans les fondamentaux de la couche réseau.

## Quiz Question

Comment appelle-t-on les réseaux plus petits qui composent Internet ?

## Quiz Answer

subnets
