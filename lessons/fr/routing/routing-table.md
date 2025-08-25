---
index: 2
lang: "fr"
title: "Table de Routage"
meta_title: "Table de Routage - Routage"
meta_description: "Apprenez à comprendre la table de routage Linux et comment les paquets sont acheminés à l'aide de la commande route. Explorez les destinations, les passerelles et les interfaces pour les bases du réseau."
meta_keywords: "table de routage Linux, commande route, routage réseau, mise en réseau Linux, Linux pour débutants, tutoriel Linux, guide réseau"
---

## Lesson Content

Regardez la table de routage de votre machine :

```plaintext
pete@icebox:~$ sudo route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.224.2   0.0.0.0         UG    0      0        0 eth0
192.168.224.0   0.0.0.0         255.255.255.0   U     1      0        0 eth0
```

### Destination

Dans le premier champ, nous avons une adresse IP de destination de 192.168.224.0. Cela signifie que tout paquet qui tente d'aller vers ce réseau sort par mon câble Ethernet (eth0). Si j'étais 192.168.224.5 et que je voulais atteindre 192.168.224.7, j'utiliserais directement l'interface réseau eth0.

Notez que nous avons des adresses de **0.0.0.0**. Cela signifie qu'aucune adresse n'est spécifiée ou qu'elle est inconnue. Donc, si par exemple, je voulais envoyer un paquet à l'adresse IP 151.123.43.6, notre table de routage ne sait pas où cela va, elle la désigne donc comme 0.0.0.0 et achemine par conséquent notre paquet vers la passerelle (Gateway).

### Passerelle

Si nous envoyons un paquet qui n'est pas sur le même réseau, il sera envoyé à cette adresse de passerelle, qui est bien nommée comme étant une passerelle vers un autre réseau.

### Masque de sous-réseau (Genmask)

C'est le masque de sous-réseau, utilisé pour déterminer quelles adresses IP correspondent à quelle destination.

### Drapeaux (Flags)

- UG - Le réseau est actif (Up) et est une passerelle (Gateway)
- U - Le réseau est actif (Up)

### Interface (Iface)

C'est l'interface par laquelle notre paquet va sortir. `eth0` désigne généralement le premier périphérique Ethernet de votre système.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du routage réseau et de l'adressage IP :

1. **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Entraînez-vous à utiliser la commande `ip a` pour identifier les informations d'adressage réseau, y compris les adresses IP et les interfaces réseau, qui sont des composants clés d'une table de routage.
2. **[Gérer l'adressage IP sous Linux](https://labex.io/fr/labs/linux-manage-ip-addressing-in-linux-592736)** - Apprenez à gérer l'adressage IP, à configurer des IP statiques, à définir des passerelles par défaut et à vérifier les configurations réseau, en relation directe avec les entrées trouvées dans une table de routage.
3. **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Explorez l'adressage IP et la joignabilité réseau à l'aide de `ping` et `ip a`, ce qui vous aidera à comprendre comment les différents types d'IP interagissent et comment la joignabilité réseau est déterminée, ce qui est reflété dans les décisions de routage.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance en matière de configuration et de dépannage réseau.

## Quiz Question

Où les paquets sont-ils acheminés si notre table de routage ne sait pas où les envoyer ?

## Quiz Answer

Gateway
