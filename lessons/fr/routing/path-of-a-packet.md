---
index: 3
lang: "fr"
title: "Parcours d'un Paquet"
meta_title: "Parcours d'un Paquet - Routage"
meta_description: "Explorez le chemin complet d'un paquet de données voyageant au sein d'un réseau local et sur Internet. Apprenez comment les adresses IP, les adresses MAC, l'ARP et les tables de routage collaborent pour assurer une communication réseau réussie sous Linux."
meta_keywords: "parcours paquet, communication réseau, ARP, adresse IP, adresse MAC, table de routage, passerelle par défaut, réseau Linux, voyage paquet"
---

## Lesson Content

Comprendre comment les données transitent sur un réseau est fondamental en mise en réseau. Ce voyage, souvent appelé le **chemin du paquet**, implique un effort coordonné entre différents protocoles et matériels. Traçons le **chemin du paquet** dans deux scénarios courants : la communication au sein d'un réseau local et la communication avec un réseau externe.

### Chemin du Paquet au Sein d'un Réseau Local

Lorsqu'un appareil envoie un paquet à un autre appareil sur le même réseau local, le processus est relativement simple.

1. Tout d'abord, l'hôte émetteur vérifie si l'adresse IP de destination se trouve sur le même sous-réseau en la comparant à sa propre adresse IP et à son masque de sous-réseau.
2. Pour envoyer un paquet, l'hôte a besoin de quatre informations clés : une IP source, une IP de destination, une adresse MAC source et une adresse MAC de destination. Initialement, l'hôte ne connaît pas l'adresse MAC de l'hôte de destination.
3. L'hôte utilise le Protocole de Résolution d'Adresse (ARP) pour trouver l'information manquante. Il diffuse une requête ARP sur le réseau local, demandant quel appareil possède l'adresse IP cible. L'appareil correspondant répond avec son adresse MAC.
4. L'adresse MAC de destination étant maintenant connue, le paquet est entièrement adressé et peut être envoyé directement à l'hôte de destination sur le réseau local.

### Chemin du Paquet vers un Réseau Externe

Lorsqu'un paquet est destiné à un appareil en dehors du réseau local, le processus implique des routeurs pour transférer le paquet.

1. L'hôte émetteur détermine que l'adresse IP de destination ne se trouve pas sur son réseau local. Comme les diffusions ARP sont limitées au réseau local, l'hôte ne peut pas découvrir directement l'adresse MAC de la destination finale.
2. L'hôte consulte sa table de routage. Comme il n'y a pas de route spécifique pour l'IP externe, il utilise la route par défaut, qui pointe vers la passerelle par défaut (un routeur). Le paquet est préparé avec les adresses IP source et de destination originales. L'adresse MAC de destination est cependant définie sur l'adresse MAC de la passerelle par défaut. Si l'adresse MAC de la passerelle est inconnue, l'hôte utilise ARP pour la trouver.
3. Une fois que le paquet atteint le routeur, celui-ci examine l'adresse IP de destination et consulte sa propre table de routage pour déterminer le prochain saut sur le **chemin du paquet**. Le routeur réécrit ensuite les adresses MAC du paquet : l'adresse MAC source devient l'adresse MAC du routeur, et l'adresse MAC de destination devient l'adresse MAC du prochain saut. Ce processus est répété à chaque routeur le long du chemin.
4. Lorsque le paquet arrive finalement au routeur connecté au réseau local de la destination, ce routeur utilise ARP pour trouver l'adresse MAC de l'hôte final et livre le paquet.
5. Tout au long de ce voyage, les adresses IP source et de destination dans l'en-tête du paquet restent inchangées. Seules les adresses MAC sont mises à jour à chaque saut.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion de base des fichiers et des répertoires sous Linux :

1. **[Opérations de Fichiers de Base sous Linux](https://labex.io/fr/labs/linux-basic-file-operations-in-linux-18001)** - Entraînez-vous à naviguer dans le système de fichiers, à gérer les fichiers et les répertoires, et à utiliser les raccourcis de la ligne de commande dans un environnement Linux réel.
2. **[Opérations sur les Fichiers et les Répertoires](https://labex.io/fr/labs/linux-file-and-directory-operations-17997)** - Apprenez à naviguer dans la structure des répertoires, à gérer les fichiers et les dossiers, et à utiliser des outils puissants en ligne de commande tels que `ls`, `cd`, `mkdir`, `cp`, `mv` et `rm`.
3. **[Organisation des Fichiers et des Répertoires](https://labex.io/fr/labs/linux-organizing-files-and-directories-387877)** - Pratiquez les compétences essentielles de gestion de fichiers Linux en utilisant les commandes `cp`, `mv` et `rm` pour organiser une structure de projet, déplacer des fichiers et nettoyer les répertoires inutiles.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance avec les interactions du système de fichiers Linux.

## Quiz Question

Quel protocole est utilisé pour trouver l'adresse MAC d'un hôte sur le réseau local, étant donnée son adresse IP ? Veuillez répondre avec l'acronyme de trois lettres en majuscules.

## Quiz Answer

ARP
