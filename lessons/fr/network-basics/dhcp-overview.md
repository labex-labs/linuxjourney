---
index: 9
lang: "fr"
title: "Aperçu du DHCP"
meta_title: "Aperçu du DHCP - Bases du Réseau"
meta_description: "Apprenez les fondamentaux du DHCP (Protocole de Configuration Dynamique des Hôtes). Ce guide couvre comment le DHCP attribue les adresses IP, son processus en quatre étapes (DORA) et son rôle dans la couche DHCP du réseau. Idéal pour les débutants en réseau Linux."
meta_keywords: "DHCP, Protocole de Configuration Dynamique des Hôtes, couche dhcp, adresse IP, réseau Linux, processus DHCP, DORA, configuration réseau"
---

## Lesson Content

Le protocole de configuration dynamique des hôtes (DHCP) est un protocole réseau fondamental utilisé pour attribuer automatiquement des adresses IP et d'autres paramètres de configuration réseau aux périphériques d'un réseau.

### Qu'est-ce que le DHCP ?

Pensez au DHCP comme à un opérateur téléphonique pour vos appareils. Lorsque vous obtenez un nouveau téléphone, vous avez besoin d'un numéro pour commencer à communiquer. Vous contactez votre opérateur, et il vous en attribue un. De même, lorsqu'un appareil se connecte à un réseau, il a besoin d'une adresse IP pour communiquer avec les autres appareils. Le DHCP est le service qui fournit cette adresse IP.

Cette adresse IP est généralement « louée » pour une période spécifique. Avant l'expiration du bail, l'appareil peut le renouveler, assurant ainsi une connectivité continue. Ce processus automatisé est essentiel pour gérer les appareils sur n'importe quel réseau.

### Le rôle d'un serveur DHCP

Un serveur DHCP est responsable de la gestion d'un pool d'adresses IP et de leur attribution aux appareils clients. Dans un réseau domestique typique, votre routeur agit souvent comme serveur DHCP. Dans les réseaux plus vastes, un serveur dédié gère cette tâche.

L'utilisation du DHCP offre des avantages significatifs :

- **Automatisation :** Les administrateurs réseau n'ont pas besoin de configurer manuellement chaque appareil, ce qui leur fait gagner du temps et des efforts.
- **Précision :** Il empêche les erreurs courantes telles que l'attribution d'adresses IP dupliquées, ce qui peut provoquer des conflits réseau.

Chaque réseau physique doit disposer de son propre serveur DHCP pour rationaliser le processus par lequel les hôtes demandent et reçoivent des adresses IP. Ce protocole fonctionne au niveau Application, constituant une partie cruciale des services de configuration du réseau, parfois conceptuellement appelé la `couche dhcp`.

### Le processus DHCP en quatre étapes

Le processus par lequel un appareil obtient une adresse IP via DHCP implique un échange en quatre étapes, souvent mémorisé par l'acronyme DORA :

1. **DHCP Discover (Découverte DHCP) :** L'appareil client diffuse un message `DISCOVER` sur le réseau pour trouver un serveur DHCP disponible.
2. **DHCP Offer (Offre DHCP) :** Tout serveur DHCP qui reçoit le message de découverte peut répondre avec un message `OFFER`. Ce message contient une adresse IP proposée, un masque de sous-réseau, une adresse de passerelle et une durée de bail.
3. **DHCP Request (Requête DHCP) :** Le client reçoit une ou plusieurs offres et en choisit une. Il diffuse ensuite un message `REQUEST` pour informer tous les serveurs DHCP de l'offre qu'il a acceptée.
4. **DHCP Acknowledgment (ACK) (Accusé de réception DHCP) :** Le serveur qui a fait l'offre acceptée envoie un message `ACK` final au client, confirmant le bail et finalisant la configuration.

Bien que le protocole complet soit plus complexe, ces quatre étapes représentent le cœur de la manière dont le DHCP configure dynamiquement les hôtes sur un réseau.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'adressage IP dynamique et de la configuration réseau :

1. **[Gérer l'adressage IP sous Linux](https://labex.io/fr/labs/comptia-manage-ip-addressing-in-linux-592736)** - Entraînez-vous à utiliser la commande `ip` pour inspecter les interfaces et utilisez spécifiquement `dhclient` pour obtenir une adresse IP dynamique, appliquant directement vos connaissances sur le DHCP.
2. **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Apprenez à utiliser la commande `ip a` pour identifier les informations d'adressage réseau, y compris les adresses IP attribuées par DHCP, et inspectez les interfaces réseau.
3. **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explorez l'adressage IP et la joignabilité du réseau à l'aide de `ping` et `ip a`, ce qui vous aidera à comprendre comment les adresses IP attribuées dynamiquement fonctionnent au sein d'un réseau.

Ces laboratoires vous aideront à appliquer les concepts d'attribution d'IP dynamique et de configuration réseau dans des scénarios réels et à renforcer votre confiance en matière de mise en réseau sous Linux.

## Quiz Question

Quelles sont les quatre étapes du processus DHCP, dans l'ordre ? Veuillez répondre en anglais, en utilisant des mots en majuscules séparés par une virgule et un espace.

## Quiz Answer

DISCOVER, OFFER, REQUEST, ACK
