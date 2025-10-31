---
index: 1
lang: "fr"
title: "Interfaces Réseau"
meta_title: "Interfaces Réseau - Configuration Réseau"
meta_description: "Un guide complet sur l'interface réseau Linux. Apprenez à utiliser ifconfig et la commande ip moderne, et comprenez les fichiers de configuration comme /etc/network/interfaces, notamment sur les systèmes Debian."
meta_keywords: "interface linux, interface réseau linux, etc interfaces réseau, interfaces réseau debian, ifconfig, commande ip, configuration réseau, réseau linux"
---

## Lesson Content

Une **interface réseau linux** est le point de connexion crucial entre la pile logicielle de mise en réseau du noyau et le matériel réseau physique. Elle permet à votre système d'exploitation d'envoyer et de recevoir des données sur un réseau. Nous avons déjà vu un exemple de ce à quoi ressemble une `interface linux` configurée :

```plaintext
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

### Comprendre les Interfaces Réseau

Lorsque vous consultez vos paramètres réseau, vous verrez des interfaces nommées comme `eth0` (la première carte Ethernet), `wlan0` (une interface sans fil) ou `lo` (l'interface de boucle locale). L'interface de boucle locale est une interface virtuelle spéciale qui représente votre propre ordinateur, vous permettant de vous connecter à des services s'exécutant localement.

Une interface peut être à l'état "up" (activée) ou "down" (désactivée). Un état "up" signifie qu'elle est active et prête à transmettre des données, tandis que "down" la désactive. Les informations clés affichées pour chaque interface comprennent l'`HWaddr` (son adresse MAC unique), l'adresse `inet` (son adresse IPv4) et l'adresse `inet6` (son adresse IPv6), ainsi que le masque de sous-réseau et l'adresse de diffusion.

### La Commande Héritée ifconfig

La commande **ifconfig** est un outil classique pour configurer une `interface réseau linux`. Au démarrage du système, elle s'exécute généralement pour configurer les interfaces en fonction des fichiers de configuration. Bien qu'elle soit toujours disponible sur de nombreux systèmes, elle est maintenant considérée comme un outil hérité (legacy).

Vous pouvez utiliser `ifconfig` pour attribuer manuellement une adresse IP et activer une interface :

```bash
ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up
```

Vous pouvez également utiliser les commandes associées `ifup` et `ifdown` pour activer ou désactiver facilement une interface :

```bash
ifup eth0
ifdown eth0
```

### La Commande Moderne ip

La commande **ip** est le remplacement moderne et plus puissant de `ifconfig`. C'est la méthode préférée pour gérer la pile réseau sur la plupart des distributions Linux actuelles.

Voici quelques exemples courants de son utilisation :

**Afficher les informations pour toutes les interfaces :**

```bash
ip link show
```

**Afficher les statistiques détaillées pour une interface spécifique :**

```bash
ip -s link show eth0
```

**Afficher les adresses IP attribuées aux interfaces :**

```bash
ip address show
```

**Activer ou désactiver une interface :**

```bash
ip link set eth0 up
ip link set eth0 down
```

**Ajouter une adresse IP à une interface :**

```bash
ip address add 192.168.1.1/24 dev eth0
```

### Fichiers de Configuration Réseau

Bien que des commandes comme `ip` et `ifconfig` configurent l'état actif d'une interface, ces modifications ne sont pas permanentes et seront perdues au redémarrage. Pour rendre les paramètres persistants, vous devez modifier les fichiers de configuration.

Un emplacement courant pour ces fichiers est `/etc/network/interfaces`. Le fichier `etc network interfaces` est particulièrement répandu sur les systèmes basés sur Debian comme Ubuntu. La gestion des **debian network interfaces** via ce fichier vous permet de définir des adresses IP statiques, des passerelles et d'autres paramètres qui sont appliqués automatiquement au démarrage. La structure dans `debian network/interfaces` est simple et bien documentée.

## Exercise

Mettez vos connaissances en pratique avec ces laboratoires pratiques. Ils vous aideront à renforcer votre compréhension des interfaces réseau et de l'adressage IP.

1.  **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Entraînez-vous à utiliser la commande `ip a` pour identifier les informations d'adressage réseau, y compris les adresses MAC, IPv4 et IPv6 sur un système Linux.
2.  **[Gérer l'adressage IP sous Linux](https://labex.io/fr/labs/comptia-manage-ip-addressing-in-linux-592736)** - Apprenez à configurer des adresses IP statiques et dynamiques, à définir une passerelle par défaut et à vérifier les configurations réseau à l'aide de la commande `ip`.
3.  **[Explorer les types d'adresses IP et l'accessibilité sous Linux](https://labex.io/fr/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explorez différents types d'adresses IP (privées, publiques, multicast) et testez l'accessibilité du réseau à l'aide de `ping` et `ip a`.

Ces laboratoires vous aideront à appliquer les concepts d'identification d'interface réseau et d'adressage IP dans des scénarios réels et à renforcer votre confiance dans la mise en réseau Linux.

## Quiz Question

Quelle est la commande héritée utilisée pour configurer une interface réseau Linux ? Veuillez répondre en anglais, en utilisant uniquement des lettres minuscules.

## Quiz Answer

ifconfig
