---
index: 1
lang: "fr"
title: "Qu'est-ce qu'un routeur ?"
meta_title: "Qu'est-ce qu'un routeur ? - Routage"
meta_description: "Guide pour débutants pour comprendre ce qu'est un routeur en réseau. Apprenez le routage, la commutation de paquets, les sauts et comment les routeurs utilisent les tables de routage pour transférer des données entre réseaux. Ce guide réseau est essentiel pour apprendre le réseau sous Linux."
meta_keywords: "routeur, réseau, routage, sauts, commutation de paquets, réseau Linux, tutoriel débutant, guide réseau"
---

## Lesson Content

Un routeur est un appareil fondamental dans la mise en réseau informatique. Vous en avez probablement un chez vous qui vous connecte à Internet. Sa tâche principale est de permettre aux machines d'un réseau de communiquer entre elles et avec d'autres réseaux. Ce processus est un élément essentiel du fonctionnement d'Internet et des réseaux locaux.

### La fonction principale d'un routeur

Un routeur domestique typique possède des ports LAN (Local Area Network) pour connecter vos appareils à un réseau local et un port WAN (Wide Area Network) qui fournit une connexion Internet. Chaque morceau de données, ou « paquet », que vous envoyez ou recevez lors de toute activité réseau doit passer par le routeur. Le routeur inspecte ces paquets réseau et décide où ils doivent aller. Il achemine efficacement le trafic entre plusieurs réseaux, garantissant que chaque paquet voyage de sa source à sa destination finale.

### Le processus de routage

Pensez au processus de routage comme à la livraison du courrier. Lorsque vous envoyez une lettre, la poste détermine la destination générale (par exemple, un état ou une ville) et l'envoie là-bas. À partir de là, elle est triée en régions plus petites comme les codes postaux jusqu'à ce qu'elle atteigne enfin l'adresse de rue spécifique.

En mise en réseau, un routeur utilise une **table de routage** pour prendre ces décisions. Cette table contient un ensemble de règles, ou routes, qui indiquent au routeur comment transférer les paquets vers une destination réseau particulière. Par exemple, une règle pourrait dire : « Pour atteindre le réseau A, envoyez les paquets au routeur B. » S'il n'y a pas de règle spécifique pour une destination, le routeur utilise une **route par défaut**, qui dirige généralement le trafic vers Internet. Ce système est crucial dans les configurations domestiques simples et les environnements complexes de **mise en réseau Linux**.

### Les sauts (Hops)

Lorsque les paquets traversent les réseaux, leur parcours est mesuré en **sauts** (hops). Un saut représente une étape du parcours où un paquet passe par un appareil intermédiaire, comme un routeur. Par exemple, si un paquet doit passer par deux routeurs pour aller de l'Hôte A à l'Hôte B, on dit que le chemin comporte deux sauts. Les sauts fournissent une métrique simple pour mesurer la distance entre une source et une destination dans un réseau.

### Commutation de paquets, routage et inondation (Flooding)

Pour comprendre comment les données se déplacent, il est utile de connaître ces termes connexes :

- **Commutation de paquets** (Packet Switching) est la méthode fondamentale de réception, de traitement et de transfert des paquets de données vers leur destination. C'est ce que font continuellement les routeurs.
- **Routage** est le processus intelligent de construction et de maintenance de la table de routage. Un routage efficace permet une commutation de paquets plus efficace et plus fiable.
- **Inondation** (Flooding) est une méthode plus ancienne et moins efficace utilisée lorsqu'un routeur ne sait pas où envoyer un paquet. Il envoie le paquet entrant sur toutes les connexions, sauf celle par laquelle il est arrivé, en espérant qu'un chemin atteindra la destination. La mise en réseau moderne repose sur le routage pour éviter ce type d'inefficacité.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la connectivité réseau et du routage :

1.  **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Entraînez-vous à tester la pile TCP/IP locale, à identifier les adresses IP privées et publiques, et à vérifier la joignabilité du réseau, éléments clés pour comprendre comment un routeur facilite la communication.
2.  **[Explorer l'interaction de la couche réseau avec ping et arp sous Linux](https://labex.io/fr/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Apprenez comment les commandes `ping` et `arp` vous aident à observer comment les couches réseau et liaison de données interagissent, et comment la passerelle par défaut (routeur) gère le trafic distant.
3.  **[Simuler la connectivité de la couche réseau sous Linux](https://labex.io/fr/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Utilisez Docker pour simuler des nœuds réseau et attribuer des adresses IP, puis testez la connectivité pour comprendre comment les sous-réseaux IP et le routage régissent la communication réseau.

Ces laboratoires vous aideront à appliquer les concepts de communication réseau, d'adressage IP et le rôle du routage dans des scénarios réels, renforçant ainsi votre confiance dans les fondamentaux du réseau.

## Quiz Question

Comment les paquets mesurent-ils la distance ? (Veuillez répondre en anglais. La réponse est sensible à la casse.)

## Quiz Answer

Hops
