---
lesson_id: "network-addressing"
course_id: "network-basics"
lang: "fr"
order_index: 4
title: "Adressage réseau"
description: "Découvrez comment les adresses de liaison, les adresses IP et les noms d'hôtes identifient différentes parties d'une communication réseau."
meta_title: "Adressage réseau - Réseaux"
meta_description: "Découvrez les principes de l'adressage réseau : adresses MAC, adresses IPv4 et IPv6, préfixes et noms d'hôtes."
meta_keywords: "adressage réseau, adresse MAC, adresse IP, nom hôte, IPv4, IPv6, identifiants réseau, réseau Linux"
---

Les communications réseau emploient des identifiants différents selon leur portée. Les adresses de la couche liaison livrent les trames sur une liaison locale, les adresses IP permettent une livraison routée et les noms aident les applications et les personnes à choisir des services.

## Adresses de la couche liaison

Une adresse MAC Ethernet comporte 48 bits, généralement écrits sous la forme de six octets hexadécimaux comme `00:c4:b5:45:b2:43`. Une adresse source identifie une interface sur la liaison actuelle, tandis que la destination peut être unicast, multicast ou broadcast.

Les adresses MAC ne sont pas garanties permanentes ni mondialement uniques. Un logiciel peut attribuer une adresse administrée localement, les interfaces virtuelles génèrent des adresses et les fonctions de confidentialité Wi-Fi peuvent les rendre aléatoires. Les routeurs remplacent normalement les trames Ethernet à chaque saut ; un serveur distant ne reçoit donc pas l'adresse source Ethernet locale d'origine.

:::single-choice{#network-addressing-mac-scope}
Quelle est la portée normale d'une adresse MAC Ethernet dans la livraison des paquets ?

::option[La liaison locale actuelle.]{#network-addressing-local-link .correct explanation="Les routeurs créent une nouvelle encapsulation de la couche liaison pour les sauts suivants."}
::option[Chaque saut routé jusqu'au serveur Internet final.]{#network-addressing-all-hops explanation="La trame d'origine ne traverse pas les routeurs sans changement."}
::option[Uniquement l'encodage du texte de l'application.]{#network-addressing-text-encoding explanation="Une adresse MAC appartient à l'encapsulation de la couche liaison."}
:::

## Adresses IP et préfixes

Une adresse IPv4 comporte 32 bits, soit quatre octets, tandis qu'une adresse IPv6 en possède 128. Une adresse IP est normalement attribuée à une interface et interprétée avec une longueur de préfixe comme `192.0.2.10/24` ou `2001:db8::10/64`. Le préfixe indique les bits initiaux qui décrivent le réseau.

Une même interface peut posséder plusieurs adresses IP, et une adresse peut changer par DHCP, adressage de confidentialité, basculement ou administration. Les adresses IPv4 privées peuvent être réutilisées dans des réseaux distincts ; les règles de routage public et de NAT déterminent l'accessibilité externe.

:::single-choice{#network-addressing-ipv4-size}
Quelle est la taille d'une adresse IPv4 ?

::option[32 bits répartis en quatre octets.]{#network-addressing-thirty-two .correct explanation="Chaque composant décimal affiché représente huit bits."}
::option[4 bits dans un seul chiffre hexadécimal.]{#network-addressing-four-bits explanation="Quatre bits ne représentent qu'un seul chiffre hexadécimal."}
::option[128 bits répartis en seize octets.]{#network-addressing-128-octets explanation="IPv6 comporte 128 bits, et non 128 octets."}
:::

## Noms d'hôtes et résolution des noms

Un nom d'hôte est un nom, pas une adresse. Selon la configuration des services de noms de l'hôte, la résolution peut consulter `/etc/hosts`, le DNS, des systèmes multicast ou d'autres sources. Un nom peut se résoudre vers plusieurs adresses et plusieurs noms peuvent désigner un même service.

Employez le chemin du résolveur système pour tester ce qu'une application est susceptible de voir :

```bash
$ getent ahosts example.com
```

Les réponses DNS peuvent changer ou être mises en cache, et une résolution réussie ne prouve pas que le service est accessible.

:::single-choice{#network-addressing-getent-purpose}
Pourquoi employer `getent ahosts` pendant un contrôle de résolution des noms ?

::option[La commande attribue définitivement l'adresse renvoyée à chaque interface.]{#network-addressing-getent-assign explanation="Elle interroge des bases de données et ne configure pas les interfaces."}
::option[Elle demande des adresses au chemin de services de noms configuré du système.]{#network-addressing-system-resolver .correct explanation="Celui-ci peut inclure les fichiers locaux et le DNS selon les règles de l'hôte."}
::option[Elle garantit la santé d'une application sur chaque hôte renvoyé.]{#network-addressing-getent-health explanation="La recherche d'un nom et la santé d'une application sont des tests distincts."}
:::

## Examiner un hôte Linux

Affichez séparément la configuration des liaisons et celle des adresses IP :

```bash
$ ip -brief link
$ ip -brief address
```

Examinez ensuite les routes et l'état des voisins lors d'un diagnostic d'accessibilité. Ne déduisez jamais l'interface ou l'adresse source correcte de son seul nom ; le choix des routes, les règles de politique, espaces de noms et tunnels peuvent modifier le trajet.

:::single-choice{#network-addressing-ip-link-versus-address}
Quelle vue de commande se concentre sur les adresses IP attribuées ?

::option[`ip -brief address`]{#network-addressing-address-view .correct explanation="L'objet address affiche les adresses IPv4 et IPv6 attribuées aux interfaces."}
::option[Uniquement `ip -brief link`.]{#network-addressing-link-only explanation="La vue link se concentre sur l'interface et son état à la couche liaison."}
::option[`pwd`]{#network-addressing-pwd explanation="Pwd affiche le répertoire de travail du shell."}
:::

## Résumé

Vous savez maintenant distinguer les noms et adresses selon leur portée réseau.

1. Considérer les adresses MAC comme des identifiants de liaison locale susceptibles de changer.
2. Lire les adresses IPv4 et IPv6 avec leur longueur de préfixe.
3. Reconnaître qu'une interface peut porter plusieurs adresses logiques.
4. Interroger les noms d'hôtes au moyen du résolveur système configuré.
