---
index: 3
lang: "fr"
title: "traceroute"
meta_title: "traceroute - Dépannage"
meta_description: "Apprenez à utiliser la commande Linux traceroute pour tracer les routes réseau et dépanner la connectivité. Comprenez le TTL et le routage des paquets pour les débutants."
meta_keywords: "traceroute, réseau Linux, dépannage réseau, TTL, commandes Linux, débutant, tutoriel"
---

## Lesson Content

La commande `traceroute` est utilisée pour voir comment les paquets sont acheminés. Elle fonctionne en envoyant des paquets avec des valeurs TTL (Time To Live) croissantes, en commençant par 1. Ainsi, le premier routeur reçoit le paquet et décrémente la valeur TTL de un, abandonnant ainsi le paquet. Le routeur nous renvoie un message ICMP Time Exceeded. Ensuite, le paquet suivant reçoit un TTL de 2, il passe donc le premier routeur, mais lorsqu'il arrive au second routeur, le TTL est de 0, et il renvoie un autre message ICMP Time Exceeded. Traceroute fonctionne de cette manière car en envoyant et en abandonnant des paquets, il construit une liste de routeurs que les paquets traversent jusqu'à ce qu'il atteigne finalement sa destination et reçoive un message ICMP Echo Reply.

Voici un petit extrait d'un traceroute :

```bash
$ traceroute google.com
traceroute to google.com (216.58.216.174), 30 hops max, 60 byte packets
 1  192.168.4.254 (192.168.4.254)  0.028 ms  0.009 ms  0.008 ms
 2  100.64.1.113 (100.64.1.113)  1.227 ms  1.226 ms 0.920 ms
 3  100.64.0.20 (100.64.0.20)  1.501 ms 1.556 ms  0.855 ms
```

Chaque ligne représente un routeur ou une machine qui se trouve entre vous et votre cible. Elle affiche le nom de la cible et son adresse IP, et les trois dernières colonnes correspondent au temps d'aller-retour d'un paquet pour atteindre ce routeur. Par défaut, trois paquets sont envoyés le long de l'itinéraire.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la découverte de chemins réseau et du dépannage :

1. **[Gérer l'adressage IP sous Linux](https://labex.io/fr/labs/linux-manage-ip-addressing-in-linux-592736)** - Entraînez-vous à utiliser la commande `ip` pour configurer les paramètres réseau et vérifier la connectivité avec `traceroute`.
2. **[Explorer l'interaction de la couche réseau avec ping et arp sous Linux](https://labex.io/fr/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Apprenez comment `ping` et `arp` fonctionnent pour comprendre les interactions de la couche réseau, qui sont fondamentales pour le fonctionnement de `traceroute`.

Ces laboratoires vous aideront à appliquer les concepts de diagnostic réseau dans des scénarios réels et à renforcer votre confiance avec les outils de mise en réseau Linux.

## Quiz Question

Qu'est-ce qui est décrémenté de un lors des sauts à travers le réseau ?

## Quiz Answer

TTL
