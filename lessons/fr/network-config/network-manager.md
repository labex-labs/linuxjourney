---
index: 4
lang: "fr"
title: "Network Manager"
meta_title: "Network Manager - Configuration réseau"
meta_description: "Découvrez NetworkManager sous Linux, comment il automatise la configuration réseau, et utilisez les commandes nm-tool et nmcli. Démarrez avec ce guide pour débutants !"
meta_keywords: "NetworkManager, nm-tool, nmcli, mise en réseau Linux, configuration réseau, tutoriel Linux, guide du débutant"
---

## Lesson Content

Bien sûr, si vous voulez que la mise en réseau de votre système soit opérationnelle automatiquement, il y a déjà quelque chose en place pour cela. La plupart des distributions utilisent le démon NetworkManager pour configurer leurs réseaux automatiquement.

Vous remarquerez NetworkManager sous la forme d'une applet quelque part dans la barre des tâches de votre bureau si vous utilisez une interface graphique. Comme vous pouvez le voir, il gère le matériel et les informations de connexion de votre réseau. Par exemple, au démarrage, NetworkManager recueillera les informations sur le matériel réseau, recherchera les connexions (sans fil, filaires, etc.), puis les activera.

Il existe également des outils en ligne de commande pour interagir avec NetworkManager :

### nm-tool

`nm-tool` rapporte l'état de NetworkManager et de ses périphériques.

```plaintext
pete@icebox:/$ nm-tool
NetworkManager Tool

State: connected (global)

- Device: eth0  [Wired connection 1] -------------------------------------------
  Type:              Wired
  Driver:            pcnet32
  State:             connected
  Default:           yes
  HW Address:        12:3D:45:56:7D:CC

  Capabilities:
    Carrier Detect:  yes

  Wired Properties
    Carrier:         on

  IPv4 Settings:
    Address:         192.168.22.1
    Prefix:          24 (255.255.255.0)
    Gateway:         192.168.22.2

    DNS:             192.168.22.2
```

### nmcli

La commande `nmcli` vous permet de contrôler et de modifier NetworkManager. Consultez la page de manuel pour plus de détails.

## Exercise

C'est en forgeant qu'on devient forgeron ! Bien que NetworkManager automatise une grande partie de la configuration réseau, comprendre les commandes et les concepts sous-jacents qu'il gère est crucial pour le dépannage et l'administration avancée. Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'identification et de la gestion du réseau sous Linux :

1. **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Entraînez-vous à utiliser la commande `ip a` pour identifier les informations d'adressage réseau, y compris les adresses MAC et IP, sur un système Linux.
2. **[Gérer l'adressage IP sous Linux](https://labex.io/fr/labs/comptia-manage-ip-addressing-in-linux-592736)** - Apprenez à configurer des adresses IP statiques et dynamiques, à définir des passerelles par défaut et à vérifier les configurations réseau à l'aide de la commande `ip` et de `dhclient`.
3. **[Explorer l'interaction de la couche réseau avec ping et arp sous Linux](https://labex.io/fr/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Utilisez `ping` et `arp` pour comprendre comment les couches réseau et liaison de données interagissent, en observant ARP en action et comment les passerelles par défaut gèrent le trafic.

Ces laboratoires vous aideront à appliquer les concepts d'identification et de configuration réseau dans des scénarios réels et à renforcer votre confiance dans les fondamentaux de la mise en réseau Linux.

## Quiz Question

Quelle est la commande pour afficher les informations de NetworkManager ?

## Quiz Answer

nm-tool
