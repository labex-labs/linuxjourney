---
lang: "fr"
title: "Gestionnaire de Réseau"
description: "Découvrez NetworkManager sous Linux, comment il automatise la configuration réseau, et utilisez les commandes nm-tool et nmcli. Démarrez avec ce guide pour débutants !"
keywords: "NetworkManager, nm-tool, nmcli, réseau Linux, configuration réseau, tutoriel Linux, guide du débutant"
---

## Lesson Content

Bien sûr, si vous voulez que la mise en réseau de votre système fonctionne automatiquement, il y a déjà quelque chose en place pour cela. La plupart des distributions utilisent le démon NetworkManager pour configurer leurs réseaux automatiquement.

Vous remarquerez NetworkManager sous la forme d'une applet quelque part dans la barre des tâches de votre bureau si vous utilisez une interface graphique. Comme vous pouvez le voir, il gère le matériel réseau et les informations de connexion de votre réseau. Par exemple, au démarrage, NetworkManager recueillera les informations sur le matériel réseau, recherchera les connexions (sans fil, filaires, etc.), puis les activera.

Il existe également des outils en ligne de commande pour interagir avec NetworkManager :

### nm-tool

`nm-tool` rapporte l'état de NetworkManager et ses périphériques.

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

Pas d'exercices pour cette leçon.

## Quiz Question

Quelle est la commande pour afficher les informations de NetworkManager ?

## Quiz Answer

nm-tool
