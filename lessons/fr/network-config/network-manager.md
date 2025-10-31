---
index: 4
lang: "fr"
title: "Gestionnaire de Réseau"
meta_title: "Gestionnaire de Réseau - Configuration Réseau"
meta_description: "Découvrez le rôle du démon NetworkManager dans la gestion moderne des réseaux Linux. Apprenez comment cet outil automatise la configuration réseau et comment interagir avec lui via nm-tool et le puissant utilitaire en ligne de commande nmcli."
meta_keywords: "NetworkManager, nm-tool, nmcli, gestionnaire réseau linux, networkmanager linux, gestionnaire réseau linux, gestion réseau linux, configuration réseau, réseau Linux"
---

## Lesson Content

Pour que le réseau d'un système soit configuré automatiquement, un service est généralement déjà en place. La plupart des distributions Linux modernes utilisent le démon NetworkManager à cette fin, ce qui en fait une pierre angulaire de la **gestion du réseau Linux**.

### Qu'est-ce que Network Manager sous Linux ?

Si vous utilisez une interface graphique (GUI), vous remarquerez probablement le service **Network Manager Linux** comme une applet sur la barre des tâches de votre bureau. Cet outil gère votre matériel réseau et les informations de connexion. Par exemple, au démarrage, NetworkManager recueille des informations sur le matériel réseau, recherche les connexions disponibles (telles que les réseaux sans fil ou câblés), puis les active pour vous connecter.

### Interaction en ligne de commande

Bien que l'applet GUI soit pratique, il existe également de puissants outils en ligne de commande pour interagir avec le service **networkmanager linux**. Ceux-ci sont essentiels pour l'administration de serveurs et le scripting.

### Utilisation de nm-tool

La commande `nm-tool` signale l'état actuel de NetworkManager et une liste de ses périphériques gérés. Notez que `nm-tool` est considéré comme obsolète sur de nombreux systèmes modernes au profit de `nmcli`.

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

### L'outil moderne nmcli

La commande `nmcli` est l'utilitaire principal en ligne de commande pour contrôler et modifier le **Gestionnaire de réseau Linux**. Elle vous permet d'afficher l'état, de gérer les connexions et de configurer les périphériques réseau directement depuis le terminal. Pour une liste complète de ses capacités, consultez sa page de manuel (`man nmcli`).

## Exercise

La pratique rend parfait ! Bien que NetworkManager automatise une grande partie de la configuration réseau, comprendre les commandes et les concepts sous-jacents qu'il gère est crucial pour le dépannage et l'administration avancée. Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'identification et de la gestion du réseau sous Linux :

1. **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Entraînez-vous à utiliser la commande `ip a` pour identifier les informations d'adressage réseau, y compris les adresses MAC et IP, sur un système Linux.
2. **[Gérer l'adressage IP sous Linux](https://labex.io/fr/labs/comptia-manage-ip-addressing-in-linux-592736)** - Apprenez à configurer des adresses IP statiques et dynamiques, à définir des passerelles par défaut et à vérifier les configurations réseau à l'aide de la commande `ip` et de `dhclient`.
3. **[Explorer l'interaction de la couche réseau avec ping et arp sous Linux](https://labex.io/fr/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Utilisez `ping` et `arp` pour comprendre comment les couches réseau et liaison de données interagissent, en observant ARP en action et comment les passerelles par défaut gèrent le trafic.

Ces laboratoires vous aideront à appliquer les concepts d'identification et de configuration du réseau dans des scénarios réels et à renforcer votre confiance dans les fondamentaux du réseau Linux.

## Quiz Question

Quelle est la commande pour afficher un résumé de l'état et des périphériques de NetworkManager tel que montré dans la leçon ? Veuillez répondre en utilisant uniquement le nom de la commande anglaise en minuscules.

## Quiz Answer

nm-tool
