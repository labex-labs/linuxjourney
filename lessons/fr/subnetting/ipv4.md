---
index: 1
lang: "fr"
title: "IPv4"
meta_title: "IPv4 - Sous-réseautage"
meta_description: "Commencez votre parcours avec notre tutoriel Linux complet sur les adresses IPv4. Ce guide pour les utilisateurs Linux débutants est la meilleure façon d'apprendre le réseau Linux, couvrant la structure IP et les outils essentiels en ligne de commande comme ip addr."
meta_keywords: "IPv4, adresse IP, linux débutant, meilleure façon d'apprendre linux, tutoriel linux complet, meilleur cours linux en ligne gratuit, cours de certification linux gratuits, réseau linux, ifconfig, ip addr"
---

## Lesson Content

Chaque appareil sur un réseau possède un identifiant unique appelé adresse IP (Internet Protocol). Cette leçon, partie essentielle de notre `tutoriel linux complet`, se concentre sur les adresses IPv4 — le type le plus courant que vous rencontrerez. Pour tout `utilisateur linux débutant`, comprendre l'IPv4 est une première étape cruciale dans le monde du réseautage.

### Pourquoi l'IPv4 est Essentiel

Apprendre l'IPv4 est fondamental pour quiconque souhaite sérieusement s'occuper de l'administration système ou de la gestion de réseau. Il constitue l'épine dorsale de la plupart des communications réseau. Ce guide offre la `meilleure façon d'apprendre le linux` en matière de réseautage, en partant de zéro. Bien que ce ne soit pas l'un de ces `cours de certification linux gratuits`, maîtriser ces bases est une étape clé vers une certification professionnelle.

### Structure de l'Adresse IPv4

Une adresse IPv4 est un nombre de 32 bits, mais elle est généralement affichée dans un format lisible par l'homme comme ceci :

```
204.23.124.23
```

Cette adresse comporte deux parties principales : la **partie réseau**, qui identifie le réseau, et la **partie hôte**, qui identifie l'appareil spécifique sur ce réseau. L'adresse est divisée en quatre sections séparées par des points, chaque section étant appelée un **octet**. Un octet est un groupe de 8 bits, ce qui signifie qu'une adresse IPv4 fait 4 octets (32 bits) de long. Comprendre cette structure est crucial pour la configuration et le dépannage du réseau.

### Trouver Votre Adresse IP

L'une des premières tâches pour tout utilisateur Linux est de trouver l'adresse IP de son système. Vous pouvez le faire à l'aide de commandes simples en ligne de commande. La commande traditionnelle pour cela est `ifconfig`. Bien qu'elle soit encore présente sur de nombreux systèmes, elle est considérée comme un outil obsolète.

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

Dans la sortie ci-dessus, l'adresse IPv4 est `192.168.1.129`.

### Utilisation de la Commande ip addr

La méthode moderne et recommandée utilise la commande `ip`. La commande `ip addr` a remplacé `ifconfig` et est la norme sur la plupart des distributions Linux actuelles. Elle fournit des informations plus détaillées et est l'outil sur lequel vous devriez vous concentrer pour apprendre.

```bash
pete@icebox:~$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 1d:3a:32:24:4d:ce brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.129/24 brd 192.168.1.255 scope global dynamic eth0
       valid_lft 85646sec preferred_lft 85646sec
```

Ici, vous pouvez trouver la même adresse IPv4, `192.168.1.129`, répertoriée à côté de `inet` pour l'interface `eth0`.

## Exercise

Entraînez-vous avec ces laboratoires pratiques pour renforcer votre compréhension de l'adressage IP et de l'identification du réseau sous Linux :

1. **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Entraînez-vous à utiliser la commande `ip a` pour identifier les informations d'adressage réseau, y compris les adresses IPv4 et IPv6, sur un système Linux.
2. **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explorez différents types d'adresses IP et testez la joignabilité du réseau à l'aide de commandes telles que `ping` et `ip a`.
3. **[Effectuer le sous-réseautage IP et la conversion binaire dans le terminal Linux](https://labex.io/fr/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Maîtrisez le sous-réseautage IP et la conversion binaire, essentiels pour une compréhension plus approfondie de la façon dont les adresses IP et les réseaux sont structurés au niveau du bit.

Ces laboratoires vous aideront à appliquer les concepts d'adressage IP dans des scénarios réels et à renforcer votre confiance dans la configuration et le dépannage réseau sous Linux.

## Quiz Question

Combien d'octets y a-t-il dans une adresse IPv4 ?

## Quiz Answer

4
