---
lang: "fr"
title: "Modèle TCP/IP"
meta_title: "Modèle TCP/IP - Bases du Réseau"
meta_description: "Découvrez les couches du modèle TCP/IP : Application, Transport, Réseau et Liaison. Comprenez comment les données voyagent à travers les réseaux. Commencez votre parcours de mise en réseau Linux !"
meta_keywords: "modèle TCP/IP, bases du réseau, réseau Linux, TCP, IP, tutoriel débutant, couches réseau, guide"
---

## Lesson Content

Le modèle OSI a donné naissance à ce qui est finalement devenu le modèle TCP/IP, et ce modèle est en fait la base d'Internet. C'est l'implémentation réelle du réseau. Le modèle TCP/IP utilise la suite de protocoles TCP/IP, que nous appelons communément TCP/IP. Ces protocoles travaillent ensemble pour spécifier comment les données doivent être collectées, adressées, transmises et acheminées à travers un réseau. En utilisant le modèle TCP/IP, nous pouvons voir comment ces protocoles sont utilisés pour montrer la décomposition de la façon dont un paquet voyage à travers le réseau.

### Application Layer

La couche supérieure du modèle TCP/IP. Elle détermine comment les programmes de votre ordinateur (tels que votre navigateur web) interagissent avec les services de la couche transport pour visualiser les données envoyées ou reçues.

Cette couche utilise :

- HTTP (Hypertext Transfer Protocol) - utilisé pour les pages web sur Internet.
- SMTP (Simple Mail Transfer Protocol) - transmission de courrier électronique (email)

### Transport Layer

Comment les données seront transmises, inclut la vérification des ports corrects, l'intégrité des données, et fondamentalement la livraison de nos paquets.

Cette couche utilise :

- TCP (Transmission Control Protocol) - livraison fiable des données
- UDP (User Datagram Protocol) - livraison non fiable des données

### Network Layer

Cette couche spécifie comment déplacer les paquets entre les hôtes et à travers les réseaux.

Cette couche utilise :

- IP (Internet Protocol) - Aide à acheminer les paquets d'une machine à l'autre.
- ICMP (Internet Control Message Protocol) - Aide à nous informer de ce qui se passe, comme les messages d'erreur et les informations de débogage.

### Link Layer

Cette couche spécifie comment envoyer des données à travers un élément physique de matériel, comme les données voyageant via Ethernet, la fibre, etc.

Les listes de protocoles que chaque couche utilise ci-dessus ne sont pas exhaustives, et vous rencontrerez de nombreux autres protocoles qui entrent en jeu.

Dans les leçons suivantes, nous allons explorer chacune de ces couches et discuter de la façon dont notre paquet traverse le réseau du point de vue du modèle TCP/IP (il existe de nombreuses perspectives sur la façon dont un paquet voyage à travers les réseaux ; nous ne les examinerons pas toutes, mais sachez qu'elles existent).

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Quelle est la couche supérieure du modèle TCP/IP ?

## Quiz Answer

Application
