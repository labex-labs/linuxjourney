---
lang: "fr"
title: "Interfaces réseau"
meta_title: "Interfaces réseau - Configuration Réseau"
meta_description: "Découvrez les interfaces réseau Linux, les commandes ifconfig et ip. Comprenez comment configurer et gérer les paramètres réseau. Démarrez votre parcours de mise en réseau Linux !"
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

### The ifconfig command

L'outil **ifconfig** nous permet de configurer nos interfaces réseau. Si nous n'avons aucune interface réseau configurée, les pilotes de périphérique du noyau et le réseau ne sauront pas comment communiquer entre eux. Ifconfig s'exécute au démarrage et configure nos interfaces via des fichiers de configuration, mais nous pouvons également les modifier manuellement. La sortie de ifconfig affiche le nom de l'interface sur le côté gauche, et le côté droit affiche des informations détaillées. Vous verrez le plus souvent des interfaces nommées eth0 (première carte Ethernet de la machine), wlan0 (interface sans fil) et lo (interface de bouclage). L'interface de bouclage est utilisée pour représenter votre ordinateur ; elle vous renvoie simplement à vous-même. C'est utile pour le débogage ou la connexion à des serveurs exécutés localement.

L'état des interfaces peut être up ou down. Comme vous pouvez le deviner, si vous vouliez « éteindre » une interface, vous pouvez la mettre en état down. Les champs que vous consulterez probablement le plus dans la sortie ifconfig sont le HWaddr (adresse MAC de l'interface), l'adresse inet (adresse IPv4) et l'inet6 (adresse IPv6). Bien sûr, vous pouvez voir que le masque de sous-réseau et l'adresse de diffusion sont également présents. Vous pouvez également consulter les informations d'interface dans /etc/network/interfaces.

### To create an interface and bring it up

```bash
ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up
```

Ceci attribue une adresse IP et un masque de sous-réseau à l'interface eth0 et la met également en service.

### To bring up or down an interface

```bash
ifup eth0
ifdown eth0
```

### The ip command

La commande **ip** nous permet également de manipuler la pile réseau d'un système. Selon la distribution que vous utilisez, cela peut être la méthode préférée pour manipuler vos paramètres réseau.

Voici quelques exemples de son utilisation :

### To show interface information for all interfaces

```bash
ip link show
```

### To show the statistics of an interface

```bash
ip -s link show eth0
```

### To show IP addresses allocated to interfaces

```bash
ip address show
```

### To bring interfaces up and down

```bash
ip link set eth0 up
ip link set eth0 down
```

### To add an IP address to an interface

```bash
ip address add 192.168.1.1/24 dev eth0
```

## Exercise

Essayez de changer l'état de vos interfaces réseau en up ou down et observez ce qui se passe.

Pouvez-vous modifier vos interfaces réseau avec les commandes ifconfig et ip ?

## Quiz Question

Quelle est la commande pour configurer nos interfaces réseau ?

## Quiz Answer

ifconfig
