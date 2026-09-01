---
lesson_id: "network-basics"
course_id: "network-basics"
lang: "fr"
order_index: 1
title: "Notions fondamentales des réseaux"
description: "Découvrez comment les hôtes, liaisons, commutateurs, routeurs et paquets forment les réseaux locaux et étendus."
meta_title: "Notions fondamentales des réseaux - Réseaux"
meta_description: "Découvrez les notions fondamentales des réseaux : hôtes, interfaces, LAN, WLAN, WAN, commutateurs, routeurs, trames et paquets."
meta_keywords: "notions réseau, Linux réseau, WAN, LAN, WLAN, routeur, hôte, interface réseau, tutoriel réseau"
---

Un réseau relie des interfaces afin que les applications de différents hôtes puissent échanger des données. Comprendre quel périphérique, quelle adresse et quelle liaison prennent en charge chaque partie du trajet facilite ensuite l'interprétation des commandes Linux.

## Hôtes et interfaces

Un hôte est un terminal ou un système en réseau, par exemple un ordinateur portable, un serveur, un téléphone ou une machine virtuelle. Un même hôte peut posséder plusieurs interfaces : Ethernet, Wi-Fi, boucle locale, tunnels, ponts ou adaptateurs virtuels. Chaque interface peut recevoir une configuration des couches liaison et réseau adaptée à sa technologie.

Examinez les interfaces et adresses d'un hôte Linux avec :

```bash
$ ip address show
```

La présence d'une interface ou son état administrativement actif ne prouve pas une connectivité de bout en bout.

:::single-choice{#network-basics-host-interface} Qu'est-ce qu'une interface réseau ?

::option[Une copie permanente de chaque paquet d'Internet.]{#network-basics-interface-copy explanation="Une interface transmet et reçoit du trafic ; ce n'est pas une archive mondiale de paquets."}
::option[Le point de rattachement d'un hôte à un réseau ou à une liaison virtuelle.]{#network-basics-interface-attachment .correct explanation="Un hôte peut posséder plusieurs interfaces physiques ou virtuelles configurées séparément."}
::option[Un alias lisible pour la facture d'un fournisseur d'accès.]{#network-basics-interface-invoice explanation="Les étiquettes de facturation sont sans rapport avec les rattachements réseau d'un hôte."}
:::

## Réseaux locaux

Un réseau local, ou LAN, couvre un environnement limité comme un domicile, un bureau ou un segment de centre de données. Les commutateurs Ethernet transmettent les trames entre les ports d'une liaison locale. Un réseau local sans fil, ou WLAN, emploie une technologie de liaison radio. Des interfaces filaires et sans fil peuvent néanmoins appartenir au même sous-réseau IP lorsqu'un pont ou un point d'accès les réunit.

:::single-choice{#network-basics-wlan-relationship} Quelle relation un WLAN entretient-il avec un LAN ?

::option[Un WLAN est toujours un Internet mondial distinct.]{#network-basics-wlan-global explanation="Il s'agit d'un réseau local qui emploie une technologie de liaison sans fil."}
::option[Un WLAN est une partition de disque employée par les routeurs.]{#network-basics-wlan-disk explanation="Le terme décrit le réseau, pas l'organisation du stockage."}
::option[Un WLAN est une forme sans fil de réseau local.]{#network-basics-wlan-local .correct explanation="Des liaisons filaires et sans fil peuvent même être réunies dans un même domaine de diffusion local."}
:::

## Routeurs et réseaux étendus

Un routeur transmet des paquets de la couche réseau entre des réseaux IP selon sa table de routage. Un appareil domestique réunit souvent routage, commutation, accès Wi-Fi, pare-feu, NAT et DHCP, mais ces fonctions restent distinctes.

Un réseau étendu, ou WAN, franchit de plus grandes limites géographiques ou administratives. Un fournisseur d'accès à Internet peut relier le réseau d'un client à d'autres réseaux, mais « WAN » ne signifie pas simplement tout appareil situé hors d'une maison.

:::single-choice{#network-basics-router-role} Quel est le rôle caractéristique d'un routeur ?

::option[Transmettre les paquets entre les réseaux de la couche réseau.]{#network-basics-forward-networks .correct explanation="Le routage choisit les sauts suivants au-delà des frontières des réseaux IP."}
::option[Stocker obligatoirement tous les fichiers des utilisateurs comme sauvegarde.]{#network-basics-router-backup explanation="La conservation des fichiers n'est pas la fonction qui définit le routage."}
::option[Traduire chaque nom d'hôte sans consulter le DNS.]{#network-basics-router-hostnames explanation="La résolution des noms et la transmission des paquets sont des fonctions distinctes."}
:::

## Paquets, trames et flux

Les applications produisent des données que les couches de protocoles découpent et encapsulent pour leur transmission. IP transporte des paquets à travers les réseaux ; une liaison locale transporte chaque paquet dans une trame propre à sa technologie. À chaque saut, les routeurs remplacent normalement l'encapsulation de la couche liaison tout en transmettant le paquet IP.

Une conversation peut comporter de nombreux paquets dans les deux directions. Les pertes, changements d'ordre, fragmentations, retransmissions et modifications de chemin signifient qu'un seul paquet capturé décrit rarement toute la transaction applicative.

:::single-choice{#network-basics-router-frame} Que devient normalement l'encapsulation de la couche liaison au passage d'un routeur ?

::option[Le routeur retire la trame entrante et crée une trame pour la liaison suivante.]{#network-basics-reframe .correct explanation="Le paquet IP transmis est transporté dans une nouvelle trame adaptée à l'interface de sortie."}
::option[La même trame Ethernet traverse tout Internet sans changer.]{#network-basics-same-frame explanation="Les trames sont limitées à leurs liaisons et remplacées aux sauts routés."}
::option[L'application supprime définitivement les adresses IP.]{#network-basics-delete-ip explanation="Le routage dépend des adresses de la couche réseau."}
:::

## Résumé

Vous savez maintenant décrire les principaux composants d'un trajet réseau élémentaire.

1. Distinguer les hôtes de leurs interfaces physiques et virtuelles.
2. Reconnaître les formes filaires et sans fil des réseaux locaux.
3. Séparer le routage des autres fonctions réunies dans un appareil domestique.
4. Distinguer les trames de liaison des paquets IP routés.
