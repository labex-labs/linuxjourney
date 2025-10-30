---
index: 1
lang: "fr"
title: "Interfaces réseau"
meta_title: "Interfaces réseau - Configuration réseau"
meta_description: "Découvrez les interfaces réseau Linux, les commandes ifconfig et ip. Comprenez comment configurer et gérer les paramètres réseau. Commencez votre parcours de mise en réseau Linux !"
meta_keywords: "interfaces réseau Linux, ifconfig, commande ip, configuration réseau, mise en réseau Linux, débutant, tutoriel, guide"
---

## Lesson Content

Une interface réseau est la manière dont le noyau relie le côté logiciel du réseau au côté matériel. Nous en avons déjà vu un exemple :

```plaintext
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

### La commande ifconfig

L'outil **ifconfig** nous permet de configurer nos interfaces réseau. Si aucune interface réseau n'est configurée, les pilotes de périphérique du noyau et le réseau ne sauront pas comment communiquer entre eux. Ifconfig s'exécute au démarrage et configure nos interfaces via des fichiers de configuration, mais nous pouvons également les modifier manuellement. La sortie de ifconfig affiche le nom de l'interface sur le côté gauche, et le côté droit affiche des informations détaillées. Vous verrez le plus souvent des interfaces nommées eth0 (première carte Ethernet de la machine), wlan0 (interface sans fil) et lo (interface de bouclage). L'interface de bouclage est utilisée pour représenter votre ordinateur ; elle vous renvoie simplement à vous-même. C'est utile pour le débogage ou la connexion à des serveurs exécutés localement.

L'état des interfaces peut être "up" (actif) ou "down" (inactif). Comme vous pouvez le deviner, si vous vouliez "éteindre" une interface, vous pouvez la mettre en état "down". Les champs que vous consulterez probablement le plus dans la sortie de ifconfig sont le HWaddr (adresse MAC de l'interface), l'adresse inet (adresse IPv4) et l'inet6 (adresse IPv6). Bien sûr, vous pouvez voir que le masque de sous-réseau et l'adresse de diffusion sont également présents. Vous pouvez également consulter les informations d'interface dans /etc/network/interfaces.

### Pour créer une interface et l'activer

```bash
ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up
```

Ceci attribue une adresse IP et un masque de sous-réseau à l'interface eth0 et l'active également.

### Pour activer ou désactiver une interface

```bash
ifup eth0
ifdown eth0
```

### La commande ip

La commande **ip** nous permet également de manipuler la pile réseau d'un système. Selon la distribution que vous utilisez, il peut s'agir de la méthode préférée pour manipuler vos paramètres réseau.

Voici quelques exemples de son utilisation :

### Pour afficher les informations d'interface pour toutes les interfaces

```bash
ip link show
```

### Pour afficher les statistiques d'une interface

```bash
ip -s link show eth0
```

### Pour afficher les adresses IP allouées aux interfaces

```bash
ip address show
```

### Pour activer et désactiver les interfaces

```bash
ip link set eth0 up
ip link set eth0 down
```

### Pour ajouter une adresse IP à une interface

```bash
ip address add 192.168.1.1/24 dev eth0
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des interfaces réseau et de l'adressage IP :

1. **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Entraînez-vous à utiliser la commande `ip a` pour identifier les informations d'adressage réseau, y compris les adresses MAC, IPv4 et IPv6 sur un système Linux.
2. **[Gérer l'adressage IP sous Linux](https://labex.io/fr/labs/comptia-manage-ip-addressing-in-linux-592736)** - Apprenez à configurer des adresses IP statiques et dynamiques, à définir une passerelle par défaut et à vérifier les configurations réseau à l'aide de la commande `ip`.
3. **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explorez différents types d'adresses IP (privées, publiques, multicast) et testez la joignabilité du réseau à l'aide de `ping` et `ip a`.

Ces laboratoires vous aideront à appliquer les concepts d'identification d'interface réseau et d'adressage IP dans des scénarios réels et à renforcer votre confiance en matière de mise en réseau Linux.

## Quiz Question

Quelle est la commande pour configurer nos interfaces réseau ?

## Quiz Answer

ifconfig
