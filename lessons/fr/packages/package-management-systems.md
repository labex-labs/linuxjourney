---
index: 6
lang: "fr"
title: "yum et apt"
meta_title: "yum et apt - Paquets"
meta_description: "Apprenez yum et apt pour la gestion des paquets Linux. Installez, supprimez et mettez à jour des logiciels sur les systèmes Debian/RPM avec ce tutoriel pour débutants. Commencez dès aujourd'hui !"
meta_keywords: "yum, apt, gestion de paquets Linux, tutoriel apt, tutoriel yum, commandes Linux, guide du débutant, installation de paquets"
---

## Lesson Content

Ah, les Batmans de la gestion de paquets ! Ces systèmes sont livrés avec toutes les fonctionnalités pour faciliter l'installation, la suppression et les modifications de paquets, y compris l'installation des dépendances de paquets. Deux des systèmes de gestion les plus populaires sont **yum** et **apt**. Yum est exclusif à la famille Red Hat, et apt est exclusif à la famille Debian.

### Installer un paquet depuis un dépôt

```bash
Debian: $ apt install package_name
RPM: $ yum install package_name
```

### Supprimer un paquet

```bash
Debian: $ apt remove package_name
RPM: $ yum erase package_name
```

### Mettre à jour les paquets pour un dépôt

Il est toujours préférable de mettre à jour vos dépôts de paquets afin qu'ils soient à jour avant d'installer et de mettre à jour un paquet.

```bash
Debian: apt update; apt upgrade
RPM: yum update
```

### Obtenir des informations sur un paquet installé

```bash
Debian: apt show package_name
RPM: yum info package_name
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des paquets Linux :

1. **[Interroger et mettre à jour des paquets avec YUM sous Linux](https://labex.io/fr/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - Entraînez-vous à gérer les paquets logiciels sur les systèmes Linux basés sur RHEL à l'aide de YUM, y compris l'inspection, la mise à jour et l'exploration des dépôts.
2. **[Installation de logiciels sous Linux](https://labex.io/fr/labs/linux-software-installation-on-linux-18005)** - Apprenez diverses méthodes pour installer et gérer des logiciels sur les systèmes Ubuntu, y compris l'utilisation d'apt, de dpkg et la gestion des fichiers .deb.
3. **[Installation et suppression de paquets](https://labex.io/fr/labs/linux-installing-and-removing-packages-385380)** - Entraînez-vous à mettre à jour le système, à installer et à supprimer des paquets, et à optimiser la configuration logicielle sur un système basé sur Debian à l'aide de `apt`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance en la gestion des paquets Linux.

## Quiz Question

Quelle commande est utilisée pour afficher les informations sur un paquet sur un système Debian ?

## Quiz Answer

apt show
