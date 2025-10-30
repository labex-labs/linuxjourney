---
index: 5
lang: "fr"
title: "arp"
meta_title: "arp - Configuration réseau"
meta_description: "Découvrez la commande Linux ARP et comment visualiser votre cache ARP. Comprenez le rôle d'ARP dans la communication réseau. Un guide pour débutants sur ARP."
meta_keywords: "Linux ARP, cache ARP, ip neighbour show, commandes réseau, mise en réseau Linux, Linux pour débutants, tutoriel Linux"
---

## Lesson Content

Lorsque nous recherchons une adresse MAC avec ARP, le système vérifie d'abord le cache ARP stocké localement. Vous pouvez visualiser ce cache :

```
pete@icebox:~$ arp
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.22.1            ether   00:12:24:fc:12:cc   C                     eth0
192.168.22.254          ether   00:12:45:f2:84:64   C                     eth0
```

Le cache ARP est vide au démarrage d'une machine ; il se remplit au fur et à mesure que des paquets sont envoyés à d'autres hôtes. Si nous envoyons un paquet à une destination qui ne se trouve pas dans le cache ARP, voici ce qui se passe :

1. L'hôte source crée la trame Ethernet avec un paquet de requête ARP.
2. L'hôte source diffuse cette trame à l'ensemble du réseau.
3. Si l'un des hôtes du réseau connaît l'adresse MAC correcte, il enverra un paquet de réponse et une trame contenant l'adresse MAC.
4. L'hôte source ajoute le mappage IP vers l'adresse MAC au cache ARP, puis procède à l'envoi du paquet.

Vous pouvez également visualiser votre cache ARP via la commande `ip` :

```bash
ip neighbour show
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension d'ARP et de l'interaction de la couche réseau :

1. **[Explorer l'interaction de la couche réseau avec ping et arp sous Linux](https://labex.io/fr/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Utilisez les commandes `ping` et `arp` pour observer comment les adresses IP sont résolues en adresses MAC et comment la passerelle par défaut gère le trafic.
2. **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Apprenez à utiliser la commande `ip a` pour identifier les informations d'adressage réseau, y compris les adresses MAC et IP, qui sont fondamentales pour comprendre ARP.
3. **[Gérer l'adressage IP sous Linux](https://labex.io/fr/labs/comptia-manage-ip-addressing-in-linux-592736)** - Entraînez-vous à gérer l'adressage IP à l'aide de la commande `ip` et vérifiez la configuration réseau avec `arp` et `traceroute`.

Ces laboratoires vous aideront à appliquer les concepts d'ARP et d'adressage réseau dans des scénarios réels et à renforcer votre confiance en matière de mise en réseau Linux.

## Quiz Question

Quelle commande pouvez-vous utiliser pour visualiser votre cache ARP ?

## Quiz Answer

arp
