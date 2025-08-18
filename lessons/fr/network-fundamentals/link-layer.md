---
index: 8
lang: "fr"
title: "Couche Liaison"
meta_title: "Couche Liaison - Bases du Réseau"
meta_description: "Découvrez la couche Liaison dans TCP/IP, comment ARP résout les adresses MAC et la traversée des paquets. Comprenez les fondamentaux du réseau avec ce tutoriel de mise en réseau Linux."
meta_keywords: "Couche Liaison, ARP, TCP/IP, adresse MAC, fondamentaux du réseau, mise en réseau Linux, débutant, tutoriel"
---

## Lesson Content

Au bas du modèle TCP/IP se trouve la couche Liaison (Link Layer). Cette couche est spécifique au matériel.

Dans la couche liaison, notre paquet est encapsulé une fois de plus dans ce qu'on appelle une trame (frame). L'en-tête de la trame attache les adresses MAC source et destination de nos hôtes, des sommes de contrôle (checksums) et des séparateurs de paquets afin que le récepteur puisse savoir quand un paquet se termine.

Heureusement, nous sommes sur le même réseau, donc notre paquet n'aura pas à voyager trop loin. Premièrement, la couche liaison attache mon adresse MAC source à l'en-tête de la trame, mais elle a aussi besoin de connaître l'adresse MAC de Patty. Comment le sait-elle, et comment la trouver puisqu'elle n'est pas sur Internet ? Nous utilisons ARP !

### ARP (Address Resolution Protocol)

ARP trouve l'adresse MAC associée à une adresse IP. ARP est utilisé au sein du même réseau. Si Patty n'était pas sur le même réseau, nous utiliserions un système de routage pour déterminer le routeur suivant qui recevrait le paquet, et une fois que nous serions sur le même réseau, nous pourrions utiliser ARP.

Une fois que nous sommes sur le même réseau, les systèmes utilisent d'abord la table de recherche ARP qui stocke des informations sur les adresses IP associées à quelle adresse MAC. Si la valeur n'y est pas, alors ARP est utilisé. Ensuite, le système enverra un message de diffusion (broadcast message) au réseau en utilisant le protocole ARP pour savoir quel hôte a l'IP 10.10.1.4. Un message de diffusion est un message spécial qui est envoyé à tous les hôtes d'un réseau (nommé à juste titre pour l'envoi d'une diffusion). Toute machine avec l'adresse IP demandée répondra avec un paquet ARP contenant l'adresse IP et l'adresse MAC.

Maintenant que nous avons toutes les données nécessaires — adresse IP et adresses MAC — notre couche liaison transmet cette trame via notre carte d'interface réseau, vers le périphérique suivant, et trouve le réseau de Patty. Cette étape est un peu plus complexe que la façon dont je viens de l'expliquer, mais nous discuterons de plus de détails dans le cours sur le Routage.

Et voilà : une traversée de paquet simple (ou pas si simple) à travers la couche TCP/IP. Gardez à l'esprit que les paquets ne voyagent pas à sens unique comme ceci. Nous ne sommes même pas encore arrivés au réseau de Patty ! Lors d'un voyage à travers les réseaux, il faut passer par le modèle TCP/IP au moins deux fois avant que des données ne soient envoyées ou reçues. En réalité, l'apparence de ce paquet serait quelque chose comme ceci :

### Packet Traversal

1. Pete envoie un e-mail à Patty : ces données sont envoyées à la couche transport.
2. La couche transport encapsule les données dans un en-tête TCP ou UDP pour former un segment. Le segment attache le port TCP ou UDP de destination et de source, puis le segment est envoyé à la couche réseau.
3. La couche réseau encapsule le segment TCP à l'intérieur d'un paquet IP ; elle attache l'adresse IP source et destination. Ensuite, elle route le paquet vers la couche liaison.
4. Le paquet atteint ensuite le matériel physique de Pete et est encapsulé dans une trame. Les adresses MAC source et destination sont ajoutées à la trame.
5. Patty reçoit cette trame de données via sa couche physique et vérifie chaque trame pour l'intégrité des données, puis désencapsule le contenu de la trame et envoie le paquet IP à la couche réseau.
6. La couche réseau lit le paquet pour trouver l'IP source et destination qui avait été précédemment attachée. Elle vérifie si son IP est la même que l'IP de destination, ce qui est le cas ! Elle désencapsule le paquet et envoie le segment à la couche transport.
7. La couche transport désencapsule les segments, vérifie les numéros de port TCP ou UDP, et établit une connexion avec la couche application basée sur ces numéros de port.
8. La couche application reçoit les données de la couche transport sur le port spécifié et les présente à Patty sous la forme du message e-mail final.

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Qu'est-ce qui est utilisé pour trouver l'adresse MAC sur le même réseau ?

## Quiz Answer

ARP
