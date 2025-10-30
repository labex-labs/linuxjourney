---
index: 9
lang: "fr"
title: "Présentation du DHCP"
meta_title: "Présentation du DHCP - Bases du réseau"
meta_description: "Découvrez le DHCP (Dynamic Host Configuration Protocol) sous Linux. Comprenez comment le DHCP attribue les adresses IP et son processus en quatre étapes. Démarrez votre parcours de mise en réseau Linux !"
meta_keywords: "DHCP, Dynamic Host Configuration Protocol, réseau Linux, adresse IP, tutoriel DHCP, débutant, guide"
---

## Lesson Content

Un concept de réseau important que nous n'avons pas encore abordé est le DHCP (Dynamic Host Configuration Protocol).

Le DHCP attribue des adresses IP, des masques de sous-réseau et des passerelles à nos machines. Par exemple, disons que vous avez un téléphone portable et que vous voulez obtenir un numéro de téléphone portable pour commencer à parler aux gens. Vous devez appeler votre opérateur téléphonique, et il vous donnera un numéro. Tant que vous payez vos factures, vous pouvez continuer à utiliser votre téléphone. Le DHCP est l'opérateur téléphonique dans ce cas ; il vous donne une adresse IP afin que vous puissiez communiquer avec d'autres adresses IP. Une adresse IP vous est également louée ; celles-ci durent une certaine période, puis sont renouvelées en fonction de vos paramètres de bail.

Le DHCP est excellent pour de nombreuses raisons : il permet à un administrateur réseau de ne pas se soucier de l'attribution des adresses IP, et il les empêche également de configurer des adresses IP en double. Chaque réseau physique devrait avoir son propre serveur DHCP afin qu'un hôte puisse demander une adresse IP. Dans un environnement domestique typique, le routeur agit généralement comme serveur DHCP.

La manière dont le DHCP obtient toutes vos informations d'hôte dynamique est la suivante :

1. DHCP DISCOVER - Ce message est diffusé pour rechercher un serveur DHCP.
2. DHCP OFFER - Le serveur DHCP du réseau répond avec un message d'offre. L'offre contient un paquet avec la durée du bail DHCP, le masque de sous-réseau, l'adresse IP, etc.
3. DHCP REQUEST - Le client envoie une autre diffusion pour faire savoir à tous les serveurs DHCP quelle offre il a acceptée.
4. DHCP ACK - Un accusé de réception est envoyé par le serveur.

Le DHCP est plus complexe que cela, mais c'est l'essentiel.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'adressage IP dynamique et de la configuration réseau :

1. **[Gérer l'adressage IP sous Linux](https://labex.io/fr/labs/comptia-manage-ip-addressing-in-linux-592736)** - Entraînez-vous à utiliser la commande `ip` pour inspecter les interfaces et utilisez spécifiquement `dhclient` pour obtenir une adresse IP dynamique, en appliquant directement vos connaissances du DHCP.
2. **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Apprenez à utiliser la commande `ip a` pour identifier les informations d'adressage réseau, y compris les adresses IP attribuées par DHCP, et inspecter les interfaces réseau.
3. **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explorez l'adressage IP et la joignabilité réseau à l'aide de `ping` et `ip a`, ce qui vous aidera à comprendre comment les adresses IP attribuées dynamiquement fonctionnent au sein d'un réseau.

Ces laboratoires vous aideront à appliquer les concepts d'attribution IP dynamique et de configuration réseau dans des scénarios réels et à renforcer votre confiance en matière de réseau Linux.

## Quiz Question

Quelles sont les étapes d'une requête DHCP ?

## Quiz Answer

DISCOVER, OFFER, REQUEST, ACK
