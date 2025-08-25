---
index: 2
lang: "fr"
title: "ping"
meta_title: "ping - Dépannage"
meta_description: "Apprenez à utiliser la commande Linux ping pour tester la connectivité réseau et résoudre les problèmes. Comprenez ICMP, TTL et le temps d'aller-retour pour un diagnostic réseau efficace."
meta_keywords: "Linux ping, connectivité réseau, ICMP, TTL, réseau Linux, Linux pour débutants, tutoriel Linux, commande ping"
---

## Lesson Content

L'un des outils réseau les plus simples, **ping**, est utilisé pour vérifier si un paquet peut atteindre un hôte. Il fonctionne en envoyant des paquets de requête d'écho ICMP (Type 8) à l'hôte de destination et attend une réponse d'écho ICMP (Type 0). Le ping est réussi lorsqu'un hôte envoie le paquet de requête et reçoit une réponse de la cible. Voyons un exemple :

```plaintext
pete@icebox:~$ ping -c 3 www.google.com
PING www.google.com (74.125.239.112) 56(84) bytes of data.
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=1 ttl=128 time=29.0 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=2 ttl=128 time=23.7 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=3 ttl=128 time=15.1 ms
```

Dans cet exemple, nous utilisons ping pour vérifier si nous pouvons atteindre `www.google.com`. L'option `-c` (count) est utilisée pour arrêter l'envoi de paquets de requête d'écho une fois le compte atteint.

La première partie indique que nous envoyons des paquets de 64 octets à 74.125.239.112 (google.com), et le reste nous montre les détails du trajet. Par défaut, il envoie un paquet par seconde.

### icmp_seq

Le champ `icmp_seq` est utilisé pour afficher le numéro de séquence des paquets envoyés. Dans ce cas, j'ai envoyé 3 paquets, et nous pouvons voir que 3 paquets sont revenus. Si vous effectuez un ping et qu'il vous manque des numéros de séquence, cela signifie qu'un problème de connectivité se produit et que tous vos paquets ne passent pas. Si le numéro de séquence est désordonné, votre connexion est probablement très lente, car vos paquets dépassent la valeur par défaut d'une seconde.

### ttl

Le champ Time To Live (TTL) est utilisé comme un compteur de sauts. Au fur et à mesure que vous effectuez des sauts, il décrémente le compteur d'un, et une fois que le compteur de sauts atteint 0, notre paquet meurt. Cela est destiné à donner une durée de vie au paquet ; nous ne voulons pas que nos paquets voyagent éternellement.

### time

Le temps aller-retour qu'il a fallu entre l'envoi du paquet de requête d'écho et la réception d'une réponse d'écho.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la connectivité réseau et de la commande `ping` :

1. **[Explorer l'interaction de la couche réseau avec ping et arp sous Linux](https://labex.io/fr/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Utilisez `ping` et `arp` pour explorer les interactions des couches réseau et liaison de données et observer comment la passerelle par défaut gère le trafic distant.
2. **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Utilisez `ping` et `ip a` pour tester la pile TCP/IP locale, vérifier la connectivité Internet publique et explorer la joignabilité du réseau.
3. **[Simuler la connectivité de la couche réseau sous Linux](https://labex.io/fr/labs/linux-simulate-network-layer-connectivity-in-linux-592752)** - Apprenez à attribuer des adresses IP statiques avec `ip addr` et à tester la connectivité avec `ping` sur les mêmes sous-réseaux et sur des sous-réseaux différents.

Ces laboratoires vous aideront à appliquer les concepts de joignabilité réseau et la commande `ping` dans des scénarios réels et à renforcer votre confiance dans le diagnostic réseau sous Linux.

## Quiz Question

Quelle est l'unité de mesure du temps aller-retour ?

## Quiz Answer

ms
