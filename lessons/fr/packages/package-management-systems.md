---
index: 6
lang: "fr"
title: "yum et apt"
meta_title: "yum et apt - Paquets"
meta_description: "Explorez les différences clés dans le débat yum vs apt. Ce guide couvre comment utiliser yum et apt pour installer, supprimer et mettre à jour des paquets sur les systèmes Linux basés sur RPM et Debian."
meta_keywords: "yum vs apt, yum apt, gestion paquets linux, apt, yum, debian, red hat, installer paquets, mettre à jour paquets, commandes linux"
---

## Lesson Content

Les gestionnaires de paquets sont des outils essentiels sous Linux qui simplifient l'installation, la mise à jour et la suppression de logiciels. Ils gèrent automatiquement les dépendances, garantissant que toutes les bibliothèques et tous les composants requis sont installés correctement. Deux des systèmes de gestion de paquets les plus importants sont **yum** et **apt**.

### Yum vs Apt

La principale différence entre ces deux systèmes réside dans les distributions Linux qu'ils desservent. Le gestionnaire de paquets `yum` (Yellowdog Updater, Modified) est utilisé par les distributions basées sur RPM comme Red Hat, CentOS et Fedora. En revanche, `apt` (Advanced Package Tool) est la norme pour les distributions basées sur Debian, y compris Ubuntu. Bien que `yum` et `apt` atteignent les mêmes objectifs, leur syntaxe de commande diffère.

### Installation et Suppression de Paquets

Pour installer un nouveau logiciel à partir d'un dépôt, vous utilisez la commande `install`.

```bash
Debian: $ apt install nom_du_paquet
RPM: $ yum install nom_du_paquet
```

Pour supprimer un paquet, les commandes sont également simples. `apt` utilise `remove`, tandis que `yum` utilise `erase`.

```bash
Debian: $ apt remove nom_du_paquet
RPM: $ yum erase nom_du_paquet
```

### Mise à Jour et Inspection des Paquets

Il est recommandé de mettre à jour votre index de paquets local avant d'installer ou de mettre à niveau un logiciel. Cela garantit que vous obtenez les dernières versions disponibles.

Pour les systèmes Debian, il s'agit d'un processus en deux étapes : `apt update` actualise la liste des paquets et `apt upgrade` installe les nouvelles versions. Pour les systèmes RPM, `yum update` gère les deux actions avec une seule commande.

```bash
Debian: $ apt update; apt upgrade
RPM: $ yum update
```

Si vous avez besoin d'obtenir plus de détails sur un paquet spécifique, vous pouvez utiliser les commandes suivantes pour afficher des informations telles que sa version, sa taille et sa description.

```bash
Debian: $ apt show nom_du_paquet
RPM: $ yum info nom_du_paquet
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des paquets sous Linux :

1. **[Interroger et Mettre à Jour les Paquets avec YUM sous Linux](https://labex.io/fr/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - Entraînez-vous à gérer les paquets logiciels sur les systèmes Linux basés sur RHEL en utilisant YUM, y compris l'inspection, la mise à jour et l'exploration des dépôts.
2. **[Installation de Logiciels sous Linux](https://labex.io/fr/labs/linux-software-installation-on-linux-18005)** - Apprenez différentes méthodes pour installer et gérer des logiciels sur les systèmes Ubuntu, y compris l'utilisation d'apt, dpkg et la gestion des fichiers .deb.
3. **[Installation et Suppression de Paquets](https://labex.io/fr/labs/linux-installing-and-removing-packages-385380)** - Entraînez-vous à mettre à jour le système, à installer et supprimer des paquets, et à optimiser la configuration logicielle sur un système basé sur Debian en utilisant `apt`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance avec la gestion des paquets sous Linux.

## Quiz Question

What command is used to show package information on a Debian system? Please answer in English, paying attention to case sensitivity.

## Quiz Answer

apt show
