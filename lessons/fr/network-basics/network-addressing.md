---
index: 4
lang: "fr"
title: "Adressage Réseau"
meta_title: "Adressage Réseau - Bases du Réseau"
meta_description: "Découvrez les fondamentaux de l'adressage réseau. Ce guide explique les adresses MAC, les adresses IP et les noms d'hôte, des concepts clés pour comprendre la communication des appareils dans le réseau Linux."
meta_keywords: "adressage réseau, adresse MAC, adresse IP, nom d'hôte, identifiants réseau, réseau Linux, bases réseau, débutant, tutoriel, guide"
---

## Lesson Content

Avant d'explorer comment les paquets de données voyagent sur un réseau, il est essentiel de comprendre une terminologie de base. Tout comme une lettre physique nécessite une adresse de destination et de retour, les paquets réseau exigent des informations similaires pour atteindre leur cible. Dans la mise en réseau informatique, les appareils sont identifiés à l'aide d'adresses MAC (Media Access Control) et d'adresses IP. Pour simplifier les choses pour les humains, nous utilisons également des noms d'hôte (hostnames).

### Adresses MAC

Une adresse MAC est un identifiant matériel unique et permanent attribué à une carte d'interface réseau (NIC). Cette adresse est gravée dans l'appareil lors de sa fabrication et ne change pas. Chaque appareil qui se connecte à un réseau, comme votre ordinateur ou smartphone, possède une NIC avec une adresse MAC distincte. Cette adresse matérielle est cruciale pour la communication sur un segment de réseau local. Une adresse MAC Ethernet ressemble généralement à ceci : `00:C4:B5:45:B2:43`. Les trois premiers octets de l'adresse forment l'Identifiant Unique Organisationnel (OUI), qui identifie le fabricant. Par exemple, Dell utilise l'OUI `00-14-22`, donc une NIC Dell pourrait avoir une adresse MAC comme `00-14-22-34-B2-C2`.

### Adresses IP

Une adresse IP est un identifiant logique pour un appareil sur un réseau, le rendant accessible sur différents réseaux, y compris Internet. Contrairement à une adresse MAC, une adresse IP n'est pas liée au matériel et peut être attribuée dynamiquement. Nous nous concentrerons sur IPv4 pour l'instant, où une adresse ressemble à `10.24.12.4`. Les adresses IP sont fondamentales pour l'aspect logiciel du réseau, permettant le routage et la communication mondiale. Bien que les adresses IP publiques soient uniques sur Internet, elles peuvent changer, et des technologies comme la Traduction d'Adresses Réseau (NAT) permettent des adresses privées et non uniques au sein d'un réseau local. Il est important de se rappeler que les adresses MAC (matérielles) et IP (logicielles) sont toutes deux nécessaires pour une communication réseau réussie.

### Noms d'hôte (Hostnames)

Bien que les adresses IP soient efficaces pour les ordinateurs, elles sont difficiles à mémoriser pour les humains. Les noms d'hôte résolvent ce problème en mappant un nom convivial à une adresse IP. Par exemple, il est beaucoup plus facile de se souvenir de `myhost.com` que de son adresse IP correspondante, telle que `192.12.41.4`. Ce mappage est géré par le Système de Noms de Domaine (DNS), qui agit comme l'annuaire téléphonique d'Internet, traduisant les noms d'hôte mémorables en adresses IP numériques requises pour le routage réseau.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des identifiants réseau tels que les adresses MAC, les adresses IP et les noms d'hôte :

1. **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Entraînez-vous à utiliser la commande `ip a` pour identifier les informations d'adressage réseau, y compris les adresses MAC et IP, sur un système Linux.
2. **[Explorer les types d'adresses IP et l'accessibilité sous Linux](https://labex.io/fr/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explorez différents types d'adresses IP et testez l'accessibilité du réseau à l'aide de `ping` et `ip a`.
3. **[Gérer la résolution de nom d'hôte locale sous Linux](https://labex.io/fr/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Apprenez à gérer la résolution de nom d'hôte locale en modifiant le fichier `/etc/hosts` et en testant vos modifications.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance avec les bases du réseau Linux.

## Quiz Question

Combien d'octets y a-t-il dans une adresse IPv4 ?

## Quiz Answer

4
