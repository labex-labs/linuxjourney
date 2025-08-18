---
index: 6
lang: "fr"
title: "yum et apt"
meta_title: "yum et apt - Packages"
meta_description: "Apprenez yum et apt pour la gestion des paquets Linux. Installez, supprimez et mettez à jour des logiciels sur les systèmes Debian/RPM avec ce tutoriel pour débutants. Commencez dès aujourd'hui !"
meta_keywords: "yum, apt, gestion de paquets Linux, tutoriel apt, tutoriel yum, commandes Linux, guide du débutant, installation de paquets"
---

## Lesson Content

Ah, les Batmans de la gestion de paquets ! Ces systèmes sont livrés avec tous les éléments nécessaires pour faciliter l'installation, la suppression et les modifications de paquets, y compris l'installation des dépendances de paquets. Deux des systèmes de gestion les plus populaires sont **yum** et **apt**. Yum est exclusif à la famille Red Hat, et apt est exclusif à la famille Debian.

### Install a package from a repository

```bash
Debian: $ apt install package_name
RPM: $ yum install package_name
```

### Remove a package

```bash
Debian: $ apt remove package_name
RPM: $ yum erase package_name
```

### Updating packages for a repository

Il est toujours préférable de mettre à jour vos dépôts de paquets afin qu'ils soient à jour avant d'installer et de mettre à jour un paquet.

```bash
Debian: apt update; apt upgrade
RPM: yum update
```

### Get information about an installed package

```bash
Debian: apt show package_name
RPM: yum info package_name
```

## Exercise

Exécutez chacune de ces commandes de paquet et observez la sortie que vous recevez.

## Quiz Question

Quelle commande est utilisée pour afficher les informations d'un paquet sur un système Debian ?

## Quiz Answer

apt show
