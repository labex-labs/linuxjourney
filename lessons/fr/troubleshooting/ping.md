---
index: 2
lang: "fr"
title: "ping"
meta_title: "ping - Dépannage"
meta_description: "Apprenez à utiliser la commande Linux ping pour tester la connectivité réseau. Ce guide explique la sortie de ping, y compris la signification de icmp_seq, TTL et le temps de trajet aller-retour. Comprenez comment interpréter la séquence ping pour diagnostiquer les problèmes réseau."
meta_keywords: "ping Linux, connectivité réseau, ICMP, TTL, commande ping, icmp_seq, séquence ping, icmp seq, signification icmp_seq, ping icmp_seq, réseau Linux"
---

## Lesson Content

La commande **ping** est l'un des utilitaires réseau les plus fondamentaux, utilisé pour tester si un hôte distant est accessible sur un réseau IP. Elle fonctionne en envoyant des paquets ICMP (Internet Control Message Protocol) de type « demande d'écho » à l'hôte cible et en attendant une « réponse d'écho » ICMP. Un ping réussi se produit lorsqu'un paquet de demande est envoyé et qu'une réponse est reçue.

Examinons une commande `ping` typique en action :

```plaintext
pete@icebox:~$ ping -c 3 www.google.com
PING www.google.com (74.125.239.112) 56(84) bytes of data.
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=1 ttl=128 time=29.0 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=2 ttl=128 time=23.7 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=3 ttl=128 time=15.1 ms
```

Dans cet exemple, nous utilisons `ping` pour vérifier la connectivité à `www.google.com`. L'option `-c 3` indique à `ping` d'envoyer exactement trois paquets de demande d'écho, puis de s'arrêter. Par défaut, `ping` envoie un paquet par seconde.

### Comprendre la sortie de Ping

La sortie de la commande `ping icmp_seq` fournit des informations de diagnostic précieuses. Décomposons les éléments clés.

### Séquence ICMP (icmp_seq)

Le champ `icmp_seq` affiche le numéro de séquence de chaque paquet ICMP. Dans notre exemple, nous avons envoyé trois paquets, et la sortie montre que les trois (`icmp_seq=1`, `icmp_seq=2`, `icmp_seq=3`) ont été renvoyés avec succès. Le `ping seq` est crucial pour diagnostiquer la perte de paquets. Si vous remarquez des numéros de séquence manquants, cela indique un problème de connectivité où certains paquets n'atteignent pas leur destination ou ne reviennent pas. Si les numéros `icmp seq` apparaissent dans le désordre, cela peut suggérer une congestion du réseau ou une latence, car les paquets mettent plus de temps que l'intervalle par défaut d'une seconde pour effectuer le aller-retour. Comprendre la `signification icmp_seq` est essentiel pour le dépannage.

### Time To Live (TTL)

Le champ Time To Live (TTL) agit comme un compteur de sauts pour le paquet. Chaque fois que le paquet passe par un routeur (un « saut »), la valeur TTL est décrémentée de un. Si le compteur atteint zéro avant que le paquet n'arrive à destination, le paquet est supprimé. Ce mécanisme empêche les paquets de circuler indéfiniment sur le réseau.

### Temps (Time)

Le champ `time` mesure le temps de trajet aller-retour — la durée nécessaire au paquet pour voyager de votre machine à l'hôte cible et pour que la réponse d'écho revienne. Cette valeur est généralement mesurée en millisecondes (ms) et est un indicateur principal de la latence du réseau.

## Exercise

La pratique est essentielle pour maîtriser le diagnostic réseau. Ces laboratoires pratiques vous aideront à renforcer votre compréhension de la commande `ping` :

1.  **[Explorer l'interaction de la couche réseau avec ping et arp sous Linux](https://labex.io/fr/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Utilisez `ping` et `arp` pour explorer les interactions des couches réseau et liaison de données et observer comment la passerelle par défaut gère le trafic distant.
2.  **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Utilisez `ping` et `ip a` pour tester la pile TCP/IP locale, vérifier la connectivité Internet publique et explorer la joignabilité du réseau.
3.  **[Simuler la connectivité de la couche réseau sous Linux](https://labex.io/fr/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Apprenez à attribuer des adresses IP statiques avec `ip addr` et testez la connectivité avec `ping` sur le même sous-réseau et sur des sous-réseaux différents.

Ces laboratoires vous aideront à appliquer les concepts de joignabilité réseau et de commande `ping` dans des scénarios réels, renforçant ainsi votre confiance dans le diagnostic réseau sous Linux.

## Quiz Question

Quelle est l'unité de mesure du temps de trajet aller-retour ? Veuillez répondre en anglais, en faisant attention à la casse.

## Quiz Answer

ms
