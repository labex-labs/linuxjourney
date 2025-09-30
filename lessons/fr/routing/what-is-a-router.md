---
index: 1
lang: "fr"
title: "Qu'est-ce qu'un routeur ?"
meta_title: "Qu'est-ce qu'un routeur ? - Routage"
meta_description: "Apprenez ce qu'est un routeur, comment il fonctionne et son rôle dans la mise en réseau. Comprenez le routage, les sauts et la livraison de paquets pour les débutants."
meta_keywords: "routeur, mise en réseau, routage, sauts, commutation de paquets, mise en réseau Linux, tutoriel pour débutants, guide réseau"
---

## Lesson Content

Nous avons déjà utilisé le terme routeur ; j'espère que vous savez ce que c'est, puisque vous en avez probablement un chez vous. Un routeur permet aux machines d'un réseau de communiquer entre elles ainsi qu'avec d'autres réseaux. Sur un routeur typique, vous aurez des ports LAN qui permettent à vos machines de se connecter au même réseau local, et vous aurez également un port de liaison Internet qui vous connecte à Internet. Parfois, ce port est étiqueté WAN car il vous connecte essentiellement à un réseau plus large. Lorsque nous effectuons une activité de mise en réseau, elle doit passer par le routeur. Le routeur décide où vont nos paquets réseau et lesquels entrent. Il achemine nos paquets entre plusieurs réseaux pour aller de leur hôte source à leur hôte de destination.

### Comment fonctionne un routeur ?

Pensez au routage de la même manière qu'à la livraison du courrier. Nous avons une adresse à laquelle nous voulons envoyer une lettre. Lorsque nous l'envoyons à la poste, ils reçoivent la lettre et voient : « Oh, ça va en Californie. » Je vais la mettre dans le camion qui va en Californie (honnêtement, je n'ai aucune idée de la façon dont fonctionne le système postal). La lettre est ensuite envoyée à San Francisco. À San Francisco, il y a différents codes postaux, puis dans ces codes postaux, il y a des codes d'adresse plus petits jusqu'à ce que, finalement, quelqu'un puisse livrer votre lettre à l'adresse que vous vouliez. D'un autre côté, si vous viviez déjà à San Francisco et dans le même code postal, le livreur de courrier saura probablement exactement où la lettre doit aller sans la remettre à quelqu'un d'autre.

Lorsque nous acheminons des paquets, ils utilisent des « routes » d'adresse similaires, telles que « pour atteindre le réseau A, envoyez ces paquets au réseau B ». Lorsque nous n'avons pas de route définie pour cela, nous avons une route par défaut que nos paquets utiliseront. Ces routes sont définies sur une table de routage que notre système utilise pour nous naviguer à travers les réseaux.

### Hops

Lorsque les paquets se déplacent à travers les réseaux, ils voyagent par sauts. Un saut est la façon dont nous mesurons approximativement la distance que le paquet doit parcourir pour aller de la source à la destination. Disons que j'ai deux routeurs connectant l'hôte A à l'hôte B ; par conséquent, nous disons qu'il y a deux sauts entre l'hôte A et l'hôte B. Chaque saut est un périphérique intermédiaire, comme les routeurs, que nous devons traverser.

### Comprendre la différence fondamentale entre la commutation, le routage et l'inondation ?

- **La COMMUTATION de paquets** consiste essentiellement à recevoir, traiter et transférer des données vers le périphérique de destination.
- Le **ROUTAGE** est un processus de création de la table de routage afin que nous puissions mieux faire la COMMUTATION.
- Avant le routage, l'**INONDATION** était utilisée. Si un routeur ne sait pas par où envoyer un paquet, alors chaque paquet entrant est envoyé par chaque lien sortant, sauf celui par lequel il est arrivé.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la connectivité réseau et du routage :

1. **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Entraînez-vous à tester la pile TCP/IP locale, à identifier les adresses IP privées et publiques, et à vérifier la joignabilité du réseau, qui sont des éléments clés pour comprendre comment un routeur facilite la communication.
2. **[Explorer l'interaction de la couche réseau avec ping et arp sous Linux](https://labex.io/fr/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Apprenez comment les commandes `ping` et `arp` vous aident à observer comment les couches réseau et liaison de données interagissent, et comment la passerelle par défaut (routeur) gère le trafic distant.
3. **[Simuler la connectivité de la couche réseau sous Linux](https://labex.io/fr/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Utilisez Docker pour simuler des nœuds réseau et attribuer des adresses IP, puis testez la connectivité pour comprendre comment les sous-réseaux IP et le routage régissent la communication réseau.

Ces laboratoires vous aideront à appliquer les concepts de communication réseau, d'adressage IP et le rôle du routage dans des scénarios réels, renforçant ainsi votre confiance dans les fondamentaux du réseau.

## Quiz Question

Comment les paquets mesurent-ils la distance ?

## Quiz Answer

Hops
