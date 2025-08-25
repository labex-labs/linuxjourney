---
index: 3
lang: "fr"
title: "Modèle TCP/IP"
meta_title: "Modèle TCP/IP - Bases du réseau"
meta_description: "Découvrez les couches du modèle TCP/IP : Application, Transport, Réseau et Liaison. Comprenez comment les données voyagent à travers les réseaux. Commencez votre parcours de mise en réseau Linux !"
meta_keywords: "modèle TCP/IP, bases du réseau, réseau Linux, TCP, IP, tutoriel débutant, couches réseau, guide"
---

## Lesson Content

Le modèle OSI a donné naissance à ce qui est finalement devenu le modèle TCP/IP, et ce modèle est en fait la base d'Internet. C'est l'implémentation réelle du réseau. Le modèle TCP/IP utilise la suite de protocoles TCP/IP, que nous appelons communément TCP/IP. Ces protocoles travaillent ensemble pour spécifier comment les données doivent être collectées, adressées, transmises et acheminées à travers un réseau. En utilisant le modèle TCP/IP, nous pouvons voir comment ces protocoles sont utilisés pour montrer la décomposition de la façon dont un paquet voyage à travers le réseau.

### Couche Application

La couche supérieure du modèle TCP/IP. Elle détermine comment les programmes de votre ordinateur (tels que votre navigateur web) interagissent avec les services de la couche transport pour visualiser les données envoyées ou reçues.

Cette couche utilise :

- HTTP (Hypertext Transfer Protocol) - utilisé pour les pages web sur Internet.
- SMTP (Simple Mail Transfer Protocol) - transmission de courrier électronique (email)

### Couche Transport

Comment les données seront transmises, inclut la vérification des ports corrects, l'intégrité des données, et la livraison de nos paquets.

Cette couche utilise :

- TCP (Transmission Control Protocol) - livraison fiable des données
- UDP (User Datagram Protocol) - livraison non fiable des données

### Couche Réseau

Cette couche spécifie comment déplacer les paquets entre les hôtes et à travers les réseaux.

Cette couche utilise :

- IP (Internet Protocol) - Aide à acheminer les paquets d'une machine à l'autre.
- ICMP (Internet Control Message Protocol) - Aide à nous informer de ce qui se passe, comme les messages d'erreur et les informations de débogage.

### Couche Liaison

Cette couche spécifie comment envoyer des données à travers un élément physique de matériel, comme les données voyageant via Ethernet, la fibre, etc.

Les listes de protocoles que chaque couche utilise ci-dessus ne sont pas exhaustives, et vous rencontrerez de nombreux autres protocoles qui entrent en jeu.

Dans les leçons suivantes, nous allons explorer chacune de ces couches et discuter de la façon dont notre paquet traverse le réseau du point de vue du modèle TCP/IP (il existe de nombreuses perspectives sur la façon dont un paquet voyage à travers les réseaux ; nous ne les examinerons pas toutes, mais sachez qu'elles existent).

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du modèle TCP/IP et des fondamentaux du réseau :

1. **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Entraînez-vous à identifier les informations clés d'adressage réseau comme les adresses MAC et IP en utilisant la commande `ip a`, ce qui est fondamental pour comprendre les couches réseau et liaison de données du modèle TCP/IP.
2. **[Explorer l'interaction de la couche réseau avec ping et arp sous Linux](https://labex.io/fr/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Apprenez comment les commandes `ping` et `arp` démontrent l'interaction entre les couches réseau et liaison de données, offrant un aperçu pratique de la façon dont les appareils communiquent au sein de la pile TCP/IP.
3. **[Simuler la connectivité de la couche réseau sous Linux](https://labex.io/fr/labs/linux-simulate-network-layer-connectivity-in-linux-592752)** - Acquérez une expérience pratique en simulant la connectivité réseau entre des nœuds Linux, en attribuant des adresses IP et en testant la communication, en appliquant directement les concepts liés à la couche réseau du modèle TCP/IP.

Ces laboratoires vous aideront à appliquer les concepts du modèle TCP/IP dans des scénarios réels et à renforcer votre confiance dans la configuration et le dépannage réseau.

## Quiz Question

Quelle est la couche supérieure du modèle TCP/IP ?

## Quiz Answer

Application
