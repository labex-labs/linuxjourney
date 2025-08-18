---
lang: "fr"
title: "ICMP"
meta_description: "Découvrez les bases du protocole ICMP, les types de messages et les codes pour le dépannage réseau. Comprenez comment ICMP fonctionne pour déboguer les problèmes réseau."
meta_keywords: "ICMP, protocole ICMP, dépannage réseau, types ICMP, réseau Linux, débutant, tutoriel, guide"
---

## Lesson Content

Le protocole ICMP (Internet Control Message Protocol) fait partie de la suite de protocoles TCP/IP. Il est utilisé pour envoyer des mises à jour et des messages d'erreur et est un protocole extrêmement utile pour le débogage des problèmes réseau, tels que l'échec de la livraison des paquets.

Chaque message ICMP contient un champ type, code et checksum. Le champ type indique le type de message ICMP, le code est un sous-type qui fournit plus d'informations sur le message, et le checksum est utilisé pour détecter tout problème d'intégrité du message.

Examinons quelques types ICMP courants :

- Type 0 - Echo Reply
- Type 3 - Destination Unreachable
- Type 8 - Echo Request
- Type 11 - Time Exceeded

Lorsqu'un paquet ne peut pas atteindre une destination, un message ICMP de Type 3 est généré. Au sein du Type 3, il existe 16 valeurs de code qui décrivent plus précisément pourquoi il ne peut pas atteindre la destination :

- Code 0 - Network Unreachable
- Code 1 - Host Unreachable
  etc...etc...

Ces messages prendront plus de sens à mesure que nous utiliserons certains outils de dépannage réseau.

## Exercise

No exercises for this lesson.

## Quiz Question

Quel est le type ICMP pour une requête d'écho ?

## Quiz Answer

8
