---
index: 8
lang: "fr"
title: "Couche Liaison de Données"
meta_title: "Couche Liaison de Données - Bases Réseau"
meta_description: "Explorez les fondamentaux de la couche liaison de données du TCP/IP. Apprenez comment l'en-tête de la couche liaison est construit, comment l'ARP résout les adresses IP en adresses MAC, et le processus de traversée des paquets sur un réseau local."
meta_keywords: "couche liaison de données, en-tête couche liaison, ARP, TCP/IP, adresse MAC, fondamentaux réseau, réseau Linux, traversée de paquets, protocole de résolution d'adresse"
---

## Lesson Content

La **Couche Liaison de Données** (Link Layer) est la couche fondamentale du modèle TCP/IP, responsable des communications sur le segment de réseau local. Cette couche est spécifique au matériel, traitant directement avec les cartes d'interface réseau et l'adressage physique.

### Trames et En-tête de la Couche Liaison de Données

Au niveau de la **couche liaison de données**, le paquet provenant de la couche réseau est encapsulé dans une structure appelée trame. Une partie cruciale de ce processus est l'ajout de l'**en-tête de la couche liaison de données**. Cet en-tête contient les adresses MAC source et destination des hôtes, des sommes de contrôle pour la détection d'erreurs, et des séparateurs de paquets, qui permettent au périphérique récepteur d'identifier où une trame se termine et où la suivante commence.

Pour construire l'**en-tête de la couche liaison de données**, le système a besoin des adresses MAC source et destination. Bien que l'adresse MAC source soit connue, l'adresse MAC de destination pour une IP sur le même réseau local doit être découverte. C'est là qu'intervient le Protocole de Résolution d'Adresse (ARP).

### ARP (Protocole de Résolution d'Adresse)

ARP est un protocole de la **couche liaison de données** utilisé pour trouver l'adresse MAC associée à une adresse IP spécifique au sein du même réseau. Si l'hôte de destination se trouvait sur un réseau différent, le paquet serait envoyé à une passerelle par défaut (routeur), et ARP serait utilisé pour trouver l'adresse MAC du routeur.

Les systèmes consultent d'abord leur table de recherche ARP, qui met en cache les mappages IP vers adresse MAC connus. Si l'adresse requise n'est pas dans le cache, le système diffuse une requête ARP à l'ensemble du réseau. Ce message spécial demande quel hôte possède une adresse IP spécifique, par exemple, 10.10.1.4. L'hôte possédant cette adresse IP enverra une réponse ARP contenant son adresse IP et son adresse MAC.

Avec toutes les adresses IP et MAC nécessaires, la **couche liaison de données** peut maintenant acheminer la trame via la carte d'interface réseau. Le voyage d'un paquet est un processus en plusieurs étapes d'encapsulation et de désencapsulation lorsqu'il monte et descend dans la pile TCP/IP aux extrémités d'envoi et de réception.

### Parcours du Paquet

Voici une description étape par étape du voyage d'un paquet d'un expéditeur (Pete) à un destinataire (Patty) :

1. Pete envoie un e-mail à Patty. Ces données sont envoyées à la couche transport.
2. La couche transport encapsule les données dans un en-tête TCP ou UDP pour former un segment. Elle attache les ports de destination et source, puis envoie le segment à la couche réseau.
3. La couche réseau encapsule le segment dans un paquet IP et attache les adresses IP source et destination. Elle achemine ensuite le paquet vers la **couche liaison de données**.
4. Le paquet atteint la **couche liaison de données**, où il est encapsulé dans une trame. L'**en-tête de la couche liaison de données**, contenant les adresses MAC source et destination, est ajouté.
5. Patty reçoit cette trame de données via sa couche physique, vérifie l'intégrité des données de la trame, puis la désencapsule et envoie le paquet IP à sa couche réseau.
6. La couche réseau lit le paquet pour trouver les adresses IP source et destination. Elle confirme que l'adresse IP de destination correspond à la sienne, désencapsule le paquet et envoie le segment à la couche transport.
7. La couche transport désencapsule le segment, vérifie les numéros de port TCP ou UDP, et établit une connexion avec la couche application en fonction de ces ports.
8. La couche application reçoit les données de la couche transport sur le port spécifié et les présente à Patty comme le message e-mail final.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la Couche Liaison de Données, des adresses MAC et d'ARP :

1. **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Entraînez-vous à utiliser la commande `ip a` pour identifier les informations d'adressage réseau, y compris les adresses MAC, sur un système Linux.
2. **[Explorer l'interaction de la couche réseau avec ping et arp sous Linux](https://labex.io/fr/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Apprenez comment les commandes `ping` et `arp` fonctionnent ensemble pour résoudre les adresses IP en adresses MAC et comprendre les interactions de la couche réseau.
3. **[Analyser les trames Ethernet avec tcpdump sous Linux](https://labex.io/fr/labs/comptia-analyze-ethernet-frames-with-tcpdump-in-linux-592765)** - Acquérir une expérience pratique en capturant et en inspectant les trames Ethernet, y compris les adresses MAC, pour comprendre les communications réseau de bas niveau.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans les fondamentaux du réseau au niveau de la Couche Liaison de Données.

## Quiz Question

Quel protocole est utilisé pour trouver l'adresse MAC d'un hôte sur le même réseau local ? (Veuillez répondre avec l'acronyme anglais en lettres majuscules).

## Quiz Answer

ARP
