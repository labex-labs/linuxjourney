---
index: 2
lang: "fr"
title: "Dépôts de Paquets"
meta_title: "Dépôts de Paquets - Paquets"
meta_description: "Découvrez les dépôts de paquets Linux et comment ils gèrent les logiciels. Apprenez à trouver et à ajouter des sources de paquets comme /etc/apt/sources.list pour une installation facile."
meta_keywords: "dépôts de paquets Linux, liste de sources apt, /etc/apt/sources.list, paquets Linux, Linux débutant, tutoriel Linux, gestion des paquets"
---

## Lesson Content

Comment les paquets téléchargés sur Internet se retrouvent-ils sur nos ordinateurs ? Allez-vous sur la page de téléchargement de chaque paquet que vous souhaitez, puis cliquez-vous sur télécharger et installer ? Bien que cela soit possible, il existe une meilleure solution : les dépôts de paquets (package repositories). Les dépôts sont des emplacements de stockage centraux pour les paquets. Il existe des tonnes de dépôts contenant de nombreux paquets, et le meilleur de tout, ils se trouvent tous sur Internet — pas de disques d'installation inutiles. Votre machine ne sait pas où chercher ces dépôts à moins que vous ne lui indiquiez explicitement où regarder.

Par exemple, supposons que je veuille le logiciel Docker sur ma machine. Docker gère ses propres dépôts pour ses paquets de conteneurs. À l'intérieur de ce dépôt se trouvent plusieurs paquets, tels que le paquet `docker-ce`, le paquet `docker-ce-cli`, le paquet `containerd.io`, etc. Docker héberge ce dépôt à une source appelée : `https://download.docker.com/linux/ubuntu`

Maintenant, au lieu d'aller sur leur site web pour télécharger le paquet directement, vous pouvez dire à votre machine de trouver le logiciel Docker à partir du lien source.

Votre distribution est déjà livrée avec des sources pré-approuvées pour obtenir des paquets, et c'est ainsi qu'elle installe tous les paquets de base que vous voyez sur votre système. Sur un système Debian, ce fichier de sources est le fichier `/etc/apt/sources.list`. Votre machine saura regarder là et vérifier tout dépôt source que vous avez ajouté.

> **Note :** Sur les anciens systèmes Debian/Ubuntu, les dépôts sont configurés dans `/etc/apt/sources.list`, tandis que les versions plus récentes d'Ubuntu (22.04+) utilisent des fichiers structurés dans `/etc/apt/sources.list.d/` comme `ubuntu.sources`. Les deux formats sont pris en charge par `apt`.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des paquets et des dépôts Linux :

1. **[Installation de Logiciels sur Linux](https://labex.io/fr/labs/linux-software-installation-on-linux-18005)** - Pratiquez diverses méthodes pour installer et gérer des logiciels sur les systèmes Ubuntu, y compris l'utilisation d'apt et la gestion des fichiers `.deb`, en lien direct avec le concept de `sources.list`.
2. **[Installation et Suppression de Paquets](https://labex.io/fr/labs/linux-installing-and-removing-packages-385380)** - Apprenez à mettre à jour le système, à installer et à supprimer des paquets sur un système basé sur Debian, consolidant votre compréhension de la manière dont les gestionnaires de paquets interagissent avec les dépôts.
3. **[Interroger et Mettre à Jour des Paquets avec YUM sous Linux](https://labex.io/fr/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - Explorez comment gérer les paquets logiciels sur les systèmes Linux basés sur RHEL en utilisant YUM, offrant une perspective plus large sur la gestion des paquets à travers différentes distributions.

Ces laboratoires vous aideront à appliquer les concepts de dépôts de paquets et de gestion de logiciels dans des scénarios réels et à renforcer votre confiance dans les tâches d'administration système.

## Quiz Question

Où se trouve le fichier de sources dans un système Debian ?

## Quiz Answer

/etc/apt/sources.list
