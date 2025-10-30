---
index: 1
lang: "fr"
title: "IPv4"
meta_title: "IPv4 - Sous-réseautage"
meta_description: "Découvrez la meilleure façon d'apprendre le réseau Linux en comprenant les adresses IPv4. Ce guide pour débutants couvre la structure IP et comment trouver votre IP en utilisant la ligne de commande."
meta_keywords: "IPv4, adresse IP, linux débutant, meilleure façon d'apprendre linux, ligne de commande linux pour débutants, ifconfig, ip addr, bases réseau"
---

## Lesson Content

Chaque appareil connecté à un réseau possède une adresse unique, connue sous le nom d'adresse IP (Internet Protocol). Pour ce cours, nous nous concentrerons sur les adresses IPv4, qui sont le type le plus courant que vous rencontrerez. Les comprendre est un élément essentiel de l'apprentissage du réseautage sous Linux.

Une adresse IPv4 est un nombre de 32 bits généralement représenté dans un format lisible par l'homme, comme ceci :

```
204.23.124.23
```

Cette adresse contient deux parties distinctes : la partie **réseau**, qui identifie le réseau spécifique sur lequel se trouve l'appareil, et la partie **hôte**, qui identifie l'appareil spécifique sur ce réseau.

### La structure d'une adresse IP

Une adresse IPv4 est divisée en quatre sections séparées par des points. Chaque section est appelée un **octet**. En informatique, un octet est un groupe de 8 bits, et puisque 8 bits équivalent à 1 octet, une adresse IPv4 fait 4 octets de long. Cette structure est fondamentale, et la maîtriser est l'une des `meilleures ressources pour apprendre la ligne de commande linux pour débutants` en réseautage.

### Trouver votre adresse IP sous Linux

Pour tout utilisateur `débutant sous linux`, l'une des premières tâches consiste à trouver l'adresse IP du système. Vous pouvez le faire à l'aide d'outils en ligne de commande.

La commande traditionnelle pour cela est `ifconfig`. Bien qu'elle soit encore présente sur de nombreux systèmes, elle est considérée comme un outil hérité.

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

Dans la sortie ci-dessus, l'adresse IPv4 est `192.168.1.129`.

### L'approche moderne avec ip addr

La `meilleure façon d'apprendre le réseautage linux` aujourd'hui implique l'utilisation de la commande moderne `ip`. La commande `ip addr` a remplacé `ifconfig` et est la norme sur la plupart des distributions Linux actuelles.

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

Exercez-vous avec ces laboratoires pratiques pour renforcer votre compréhension de l'adressage IP et de l'identification du réseau sous Linux :

1. **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Entraînez-vous à utiliser la commande `ip a` pour identifier les informations d'adressage réseau, y compris les adresses IPv4 et IPv6, sur un système Linux.
2. **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explorez différents types d'adresses IP et testez la joignabilité du réseau à l'aide de commandes telles que `ping` et `ip a`.
3. **[Effectuer le sous-réseautage IP et la conversion binaire dans le terminal Linux](https://labex.io/fr/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Maîtrisez le sous-réseautage IP et la conversion binaire, essentiels pour une compréhension plus approfondie de la manière dont les adresses IP et les réseaux sont structurés au niveau du bit.

Ces laboratoires vous aideront à appliquer les concepts d'adressage IP dans des scénarios réels et à gagner en confiance avec la configuration et le dépannage réseau sous Linux.

## Quiz Question

Combien d'octets y a-t-il dans une adresse IPv4 ?

## Quiz Answer

4
