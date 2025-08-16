---
lang: "fr"
title: "Adressage Réseau"
description: "Apprenez les bases de l'adressage réseau : adresses MAC vs. IP, et noms d'hôte. Comprenez comment les appareils communiquent sur un réseau. Commencez votre parcours de mise en réseau Linux !"
keywords: "adressage réseau, adresse MAC, adresse IP, nom d'hôte, mise en réseau Linux, débutant, tutoriel, guide"
---

## Lesson Content

Avant de nous lancer dans la façon dont un paquet se déplace sur un réseau, nous devons nous familiariser avec une certaine terminologie. Lorsque vous envoyez une lettre, vous devez savoir à qui elle est envoyée et d'où elle vient. Les paquets ont besoin des mêmes informations. Nos hôtes et les autres hôtes sont identifiés à l'aide d'adresses MAC (Media Access Control) et d'adresses IP. Pour nous faciliter la tâche, nous utilisons des noms d'hôte pour identifier un hôte.

### MAC Addresses

Une adresse MAC est un identifiant unique utilisé comme adresse matérielle. Cette adresse ne changera jamais. Lorsque vous souhaitez accéder à Internet, votre machine doit disposer d'un périphérique appelé carte d'interface réseau. Cet adaptateur réseau possède sa propre adresse matérielle qui est utilisée pour identifier votre machine. Une adresse MAC pour un périphérique Ethernet ressemble à ceci : `00:C4:B5:45:B2:43`. Les adresses MAC sont attribuées aux adaptateurs réseau lors de leur fabrication. Chaque fabricant possède un identifiant unique d'organisation (OUI) pour l'identifier en tant que fabricant. Cet OUI est désigné par les 3 premiers octets de l'adresse MAC. Par exemple, Dell a `00-14-22`, donc un adaptateur réseau de Dell pourrait avoir une adresse MAC comme : `00-14-22-34-B2-C2`.

### IP Addresses

Une adresse IP est utilisée pour identifier un périphérique sur un réseau. Elles sont indépendantes du matériel et peuvent varier en syntaxe selon que vous utilisez IPv4 ou IPv6 (plus d'informations à ce sujet plus tard). Pour l'instant, nous supposerons que vous utilisez IPv4, donc une adresse IP typique ressemblerait à : `10.24.12.4`. Les adresses IP sont utilisées avec la partie logicielle du réseau. Chaque fois qu'un système est connecté à Internet, il doit avoir une adresse IP. Elles peuvent également changer si votre réseau change et sont uniques à l'ensemble d'Internet (ce n'est pas toujours le cas une fois que nous aurons appris le NAT).

N'oubliez pas qu'il faut à la fois des logiciels et du matériel pour déplacer des paquets sur les réseaux, nous avons donc deux identifiants pour chacun : MAC (matériel) et IP (logiciel).

### Hostnames

Une dernière façon d'identifier vos machines est par les noms d'hôte. Les noms d'hôte prennent votre adresse IP et vous permettent de lier cette adresse à un nom lisible par l'homme. Au lieu de vous souvenir de `192.12.41.4`, vous pouvez simplement vous souvenir de `myhost.com`.

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Combien d'octets y a-t-il dans une adresse IPv4 ?

## Quiz Answer

4
