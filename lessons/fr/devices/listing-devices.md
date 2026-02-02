---
index: 6
lang: "fr"
title: "lsusb, lspci, lsscsi"
meta_title: "lsusb, lspci, lsscsi - Périphériques"
meta_description: "Découvrez comment lister et inspecter le matériel USB, PCI et SCSI sur votre système Linux. Ce guide couvre les commandes lsusb, lspci et lsscsi, y compris des options comme lsusb -t pour afficher les arborescences des périphériques."
meta_keywords: "lsusb, lspci, lsscsi, lsusb -t, lister périphériques usb, lister périphériques pci, lister périphériques scsi, matériel linux, information périphériques"
---

## Lesson Content

Tout comme vous utilisez la commande `ls` pour lister les fichiers, Linux fournit des outils similaires pour lister les périphériques matériels. Ces commandes sont essentielles pour identifier le matériel connecté à votre système.

### Lister les périphériques USB avec lsusb

Pour voir tous les périphériques USB connectés à votre système, vous pouvez utiliser la commande `lsusb`. Cette commande analyse les concentrateurs USB et signale les informations sur les périphériques qu'elle trouve, tels que les webcams, les claviers et les disques externes.

```bash
lsusb
```

Pour une vue plus structurée, vous pouvez utiliser la commande `lsusb -t`. Cette option affiche les périphériques USB dans une structure arborescente, ce qui est utile pour comprendre comment les périphériques sont physiquement connectés aux contrôleurs et concentrateurs USB.

### Lister les périphériques PCI avec lspci

La commande `lspci` est utilisée pour lister tous les périphériques PCI (Peripheral Component Interconnect). Ce sont généralement des composants internes connectés à la carte mère, tels que les cartes graphiques, les cartes réseau et les cartes son. Cette commande fournit un aperçu rapide du matériel de base de votre système.

```bash
lspci
```

### Lister les périphériques SCSI et SATA avec lsscsi

Pour les périphériques de stockage, la commande `lsscsi` est particulièrement utile. Elle liste tous les périphériques SCSI et SATA connectés, qui comprennent couramment les disques durs, les SSD et les lecteurs optiques (CD/DVD/Blu-ray). Bien que d'autres commandes puissent montrer le contrôleur de stockage, `lsscsi` fournit des informations directes sur les périphériques de stockage eux-mêmes, ce qui en fait un outil précieux pour les administrateurs système et les utilisateurs gérant le stockage.

```bash
lsscsi
```

## Exercise

Pour renforcer votre compréhension de l'exploration des périphériques matériels sous Linux, essayez le laboratoire pratique suivant :

1. **[Explorer les périphériques matériels sous Linux](https://labex.io/fr/labs/comptia-explore-hardware-devices-in-linux-590861)** - Dans ce laboratoire, vous apprendrez les compétences essentielles pour explorer, identifier et inspecter les périphériques matériels dans un environnement Linux. Vous acquerrez une expérience pratique avec de puissants utilitaires en ligne de commande pour comprendre comment le système d'exploitation interagit avec les composants physiques.

Ce laboratoire vous aidera à appliquer ces concepts dans un scénario réel et à renforcer votre confiance dans la gestion des informations relatives aux périphériques.

## Quiz Question

Quelle commande est utilisée pour afficher une liste des périphériques USB connectés ? (Veuillez répondre uniquement en caractères anglais minuscules.)

## Quiz Answer

lsusb
