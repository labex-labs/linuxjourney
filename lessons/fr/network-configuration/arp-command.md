---
title: "arp"
description: "Découvrez la commande Linux ARP et comment visualiser votre cache ARP. Comprenez le rôle d'ARP dans la communication réseau. Un guide pour débutants sur ARP."
keywords: "Linux ARP, cache ARP, ip neighbour show, commandes réseau, réseau Linux, Linux pour débutants, tutoriel Linux"
---

## Lesson Content

Lorsque nous recherchons une adresse MAC avec ARP, il vérifie d'abord le cache ARP stocké localement sur notre système. Vous pouvez en fait visualiser ce cache :

```
pete@icebox:~$ arp
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.22.1            ether   00:12:24:fc:12:cc   C                     eth0
192.168.22.254          ether   00:12:45:f2:84:64   C                     eth0
```

Le cache ARP est en fait vide lorsqu'une machine démarre ; il se remplit au fur et à mesure que des paquets sont envoyés à d'autres hôtes. Si nous envoyons un paquet à une destination qui n'est pas dans le cache ARP, les événements suivants se produisent :

1. L'hôte source crée la trame Ethernet avec un paquet de requête ARP.
2. L'hôte source diffuse cette trame sur l'ensemble du réseau.
3. Si l'un des hôtes du réseau connaît la bonne adresse MAC, il enverra un paquet de réponse et une trame contenant l'adresse MAC.
4. L'hôte source ajoute le mappage IP vers l'adresse MAC au cache ARP, puis procède à l'envoi du paquet.

Vous pouvez également visualiser votre cache ARP via la commande `ip` :

```bash
ip neighbour show
```

## Exercise

Observez ce qui arrive à votre cache ARP lorsque vous redémarrez votre machine, puis effectuez une action sur le réseau.

## Quiz Question

Quelle commande pouvez-vous utiliser pour visualiser votre cache ARP ?

## Quiz Answer

arp
