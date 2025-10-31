---
index: 7
lang: "fr"
title: "Couche Réseau"
meta_title: "Couche Réseau - Bases Réseau"
meta_description: "Explorez la couche Réseau dans le networking Linux. Ce guide explique comment les adresses IP et les sous-réseaux permettent le routage des paquets pour la transmission de données entre réseaux."
meta_keywords: "Couche réseau, adresses IP, sous-réseaux, networking Linux, routage de paquets, transmission de données, modèle OSI, paquet IP"
---

## Lesson Content

La couche Réseau est responsable de l'adressage logique et du routage des paquets de données d'un hôte source vers un hôte de destination. Bien qu'un paquet puisse parfois voyager au sein d'un seul réseau local, Internet est une vaste collection de réseaux interconnectés.

### Le Rôle du Routage de Paquets

La fonction principale de la couche Réseau est de déterminer le chemin optimal pour le voyage des données. Ce processus, connu sous le nom de **routage de paquets**, garantit que l'information atteint sa destination prévue efficacement, même si elle doit traverser plusieurs frontières de réseau. Dans le **réseau Linux**, cette couche est fondamentale pour toute communication Internet.

### Comprendre les Sous-réseaux et les Adresses IP

Les réseaux plus petits qui constituent Internet sont appelés **sous-réseaux** (subnets). Tous les sous-réseaux sont connectés, ce qui permet à un appareil d'un réseau de communiquer avec un appareil d'un autre, comme accéder à un site Web tel que `google.com`. Les règles de voyage entre ces différents sous-réseaux sont définies par les **adresses IP**. Une adresse IP fournit un identifiant unique pour un appareil sur un réseau, tout comme une adresse de rue pour une maison.

### Encapsulation à la Couche Réseau

À la couche Réseau, le segment de données reçu de la couche Transport est encapsulé dans une nouvelle unité appelée paquet IP. Au cours de ce processus, un en-tête est ajouté au paquet, qui inclut l'adresse IP source (d'où provient le paquet) et l'adresse IP de destination (où il va). Avec ces informations d'adressage cruciales jointes, le paquet possède désormais tout ce dont il a besoin pour son voyage et est transmis à la couche Liaison de Données pour être préparé à la transmission physique.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la couche Réseau, de l'adressage IP et des sous-réseaux :

1. **[Simuler la Connectivité de la Couche Réseau sous Linux](https://labex.io/fr/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Entraînez-vous à attribuer des adresses IP statiques et à tester la connectivité au sein et entre différents sous-réseaux à l'aide de conteneurs Docker.
2. **[Effectuer le Sous-réseautage IP et la Conversion Binaire dans le Terminal Linux](https://labex.io/fr/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Maîtrisez le sous-réseautage IP et la conversion binaire, y compris le calcul des hôtes et des sous-réseaux utilisables, directement dans le terminal Linux.
3. **[Explorer les Types d'Adresses IP et la Portée sous Linux](https://labex.io/fr/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explorez divers types d'adresses IP (privées, publiques, multicast) et testez la portée du réseau à l'aide de `ping` et `ip a`.

Ces laboratoires vous aideront à appliquer les concepts d'adressage IP et de sous-réseautage dans des scénarios réels et à renforcer votre confiance dans les fondamentaux de la couche Réseau.

## Quiz Question

Comment appelle-t-on les réseaux plus petits qui composent Internet ? Veuillez répondre en utilisant un seul mot anglais en minuscules.

## Quiz Answer

subnets
