---
index: 8
lang: "fr"
title: "Couche de liaison"
meta_title: "Couche de liaison - Bases du réseau"
meta_description: "Apprenez-en davantage sur la couche de liaison dans TCP/IP, comment ARP résout les adresses MAC et le parcours des paquets. Comprenez les fondamentaux du réseau avec ce tutoriel de mise en réseau Linux."
meta_keywords: "Couche de liaison, ARP, TCP/IP, adresse MAC, fondamentaux du réseau, mise en réseau Linux, débutant, tutoriel"
---

## Lesson Content

Au bas du modèle TCP/IP se trouve la couche de liaison (Link Layer). Cette couche est spécifique au matériel.

Dans la couche de liaison, notre paquet est encapsulé une fois de plus dans ce qu'on appelle une trame. L'en-tête de la trame attache les adresses MAC source et destination de nos hôtes, des sommes de contrôle et des séparateurs de paquets afin que le récepteur puisse savoir quand un paquet se termine.

Heureusement, nous sommes sur le même réseau, donc notre paquet n'aura pas à voyager trop loin. Tout d'abord, la couche de liaison attache mon adresse MAC source à l'en-tête de la trame, mais elle a également besoin de connaître l'adresse MAC de Patty. Comment le sait-elle, et comment la trouver puisque ce n'est pas sur Internet ? Nous utilisons ARP !

### ARP (Address Resolution Protocol)

ARP trouve l'adresse MAC associée à une adresse IP. ARP est utilisé au sein du même réseau. Si Patty n'était pas sur le même réseau, nous utiliserions un système de routage pour déterminer le routeur suivant qui recevrait le paquet, et une fois que nous serions sur le même réseau, nous pourrions utiliser ARP.

Une fois que nous sommes sur le même réseau, les systèmes utilisent d'abord la table de recherche ARP qui stocke des informations sur les adresses IP associées à quelle adresse MAC. Si la valeur n'est pas présente, alors ARP est utilisé. Ensuite, le système enverra un message de diffusion au réseau en utilisant le protocole ARP pour savoir quel hôte a l'IP 10.10.1.4. Un message de diffusion est un message spécial qui est envoyé à tous les hôtes d'un réseau (nommé à juste titre pour l'envoi d'une diffusion). Toute machine avec l'adresse IP demandée répondra avec un paquet ARP contenant l'adresse IP et l'adresse MAC.

Maintenant que nous avons toutes les données nécessaires — adresse IP et adresses MAC — notre couche de liaison transmet cette trame via notre carte d'interface réseau, vers le périphérique suivant, et trouve le réseau de Patty. Cette étape est un peu plus complexe que la façon dont je viens de l'expliquer, mais nous discuterons de plus de détails dans le cours sur le routage.

Et voilà : un parcours de paquet simple (ou pas si simple) à travers la couche TCP/IP. Gardez à l'esprit que les paquets ne voyagent pas de manière unidirectionnelle comme cela. Nous ne sommes même pas encore arrivés au réseau de Patty ! Lors du transit à travers les réseaux, il faut passer par le modèle TCP/IP au moins deux fois avant que des données ne soient envoyées ou reçues. En réalité, l'apparence de ce paquet serait quelque chose comme ceci :

### Parcours du paquet

1. Pete envoie un e-mail à Patty : ces données sont envoyées à la couche de transport.
2. La couche de transport encapsule les données dans un en-tête TCP ou UDP pour former un segment. Le segment attache le port TCP ou UDP de destination et de source, puis le segment est envoyé à la couche réseau.
3. La couche réseau encapsule le segment TCP à l'intérieur d'un paquet IP ; elle attache l'adresse IP source et destination. Ensuite, elle route le paquet vers la couche de liaison.
4. Le paquet atteint ensuite le matériel physique de Pete et est encapsulé dans une trame. Les adresses MAC source et destination sont ajoutées à la trame.
5. Patty reçoit cette trame de données via sa couche physique et vérifie chaque trame pour l'intégrité des données, puis désencapsule le contenu de la trame et envoie le paquet IP à la couche réseau.
6. La couche réseau lit le paquet pour trouver l'IP source et destination qui avait été précédemment attachée. Elle vérifie si son IP est la même que l'IP de destination, ce qui est le cas ! Elle désencapsule le paquet et envoie le segment à la couche de transport.
7. La couche de transport désencapsule les segments, vérifie les numéros de port TCP ou UDP, et établit une connexion avec la couche application basée sur ces numéros de port.
8. La couche application reçoit les données de la couche de transport sur le port spécifié et les présente à Patty sous la forme du message e-mail final.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la couche de liaison, des adresses MAC et d'ARP :

1. **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Entraînez-vous à utiliser la commande `ip a` pour identifier les informations d'adressage réseau, y compris les adresses MAC, sur un système Linux.
2. **[Explorer l'interaction de la couche réseau avec ping et arp sous Linux](https://labex.io/fr/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Apprenez comment les commandes `ping` et `arp` fonctionnent ensemble pour résoudre les adresses IP en adresses MAC et comprendre les interactions de la couche réseau.
3. **[Analyser les trames Ethernet avec tcpdump sous Linux](https://labex.io/fr/labs/comptia-analyze-ethernet-frames-with-tcpdump-in-linux-592765)** - Acquérez une expérience pratique de la capture et de l'inspection des trames Ethernet, y compris les adresses MAC, pour comprendre les communications réseau de bas niveau.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance avec les fondamentaux du réseau au niveau de la couche de liaison.

## Quiz Question

Qu'est-ce qui est utilisé pour trouver l'adresse MAC sur le même réseau ?

## Quiz Answer

ARP
