---
lang: "fr"
title: "Qu'est-ce qu'un routeur ?"
meta_title: "Qu'est-ce qu'un routeur ? - Routage"
meta_description: "Découvrez ce qu'est un routeur, comment il fonctionne et son rôle dans la mise en réseau. Comprenez le routage, les sauts et la livraison de paquets pour les débutants."
meta_keywords: "routeur, mise en réseau, routage, sauts, commutation de paquets, réseau Linux, tutoriel pour débutants, guide réseau"
---

## Lesson Content

Nous avons déjà utilisé le terme routeur ; j'espère que vous savez ce que c'est, puisque vous en avez probablement un chez vous. Un routeur permet aux machines d'un réseau de communiquer entre elles ainsi qu'avec d'autres réseaux. Sur un routeur typique, vous aurez des ports LAN qui permettent à vos machines de se connecter au même réseau local, et vous aurez également un port de liaison montante Internet qui vous connecte à Internet. Parfois, vous verrez ce port étiqueté comme WAN car il vous connecte essentiellement à un réseau plus large. Lorsque nous effectuons une activité de mise en réseau, elle doit passer par le routeur. Le routeur décide où vont nos paquets réseau et lesquels entrent. Il achemine nos paquets entre plusieurs réseaux pour aller de leur hôte source à leur hôte de destination.

### Comment fonctionne un routeur ?

Pensez au routage de la même manière que la livraison du courrier. Nous avons une adresse à laquelle nous voulons envoyer une lettre. Lorsque nous l'envoyons à la poste, ils reçoivent la lettre et voient : « Oh, ça va en Californie. » Je vais la mettre dans le camion qui va en Californie (honnêtement, je n'ai aucune idée de la façon dont le système postal fonctionne). La lettre est ensuite envoyée à San Francisco. À l'intérieur de San Francisco, il y a différents codes postaux, puis dans ces codes postaux, il y a des codes d'adresse plus petits jusqu'à ce que finalement, quelqu'un puisse livrer votre lettre à l'adresse que vous vouliez. D'un autre côté, si vous viviez déjà à San Francisco et dans le même code postal, le livreur de courrier saura probablement exactement où la lettre doit aller sans la remettre à quelqu'un d'autre.

Lorsque nous acheminons des paquets, ils utilisent des « routes » d'adresse similaires, telles que « pour atteindre le réseau A, envoyez ces paquets au réseau B ». Lorsque nous n'avons pas de route définie pour cela, nous avons une route par défaut que nos paquets utiliseront. Ces routes sont définies sur une table de routage que notre système utilise pour nous naviguer à travers les réseaux.

### Hops

Lorsque les paquets se déplacent à travers les réseaux, ils voyagent par sauts (hops). Un saut est la façon dont nous mesurons approximativement la distance que le paquet doit parcourir pour aller de la source à la destination. Disons que j'ai deux routeurs connectant l'hôte A à l'hôte B ; par conséquent, nous disons qu'il y a deux sauts entre l'hôte A et l'hôte B. Chaque saut est un périphérique intermédiaire, comme les routeurs, que nous devons traverser.

### Comprendre la différence fondamentale entre le Switching, le Routing et le Flooding ?

- **Packet SWITCHING** consiste essentiellement à recevoir, traiter et transférer des données vers le périphérique de destination.
- Le **ROUTING** est un processus de création de la table de routage afin que nous puissions mieux faire du SWITCHING.
- Avant le routage, le **FLOODING** était utilisé. Si un routeur ne sait pas par où envoyer un paquet, alors chaque paquet entrant est envoyé par chaque lien sortant, sauf celui par lequel il est arrivé.

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Comment les paquets mesurent-ils la distance ?

## Quiz Answer

Hops
