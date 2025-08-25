---
index: 5
lang: "fr"
title: "Protocoles à vecteur de distance"
meta_title: "Protocoles à vecteur de distance - Routage"
meta_description: "Découvrez les protocoles à vecteur de distance comme RIP, leur fonctionnement et leurs limites pour le routage réseau. Comprenez le nombre de sauts et l'efficacité du réseau."
meta_keywords: "protocoles à vecteur de distance, RIP, protocole d'information de routage, nombre de sauts, routage réseau, mise en réseau Linux, guide du débutant, tutoriel"
---

## Lesson Content

Les protocoles à vecteur de distance déterminent le chemin vers d'autres réseaux en utilisant le nombre de sauts qu'un paquet effectue à travers le réseau. Par exemple, si le réseau A est à 3 sauts et que le réseau B est à côté du réseau A, alors nous supposons que le réseau B doit être à 4 sauts. Dans les protocoles à vecteur de distance, la prochaine route serait celle avec le moins de sauts.

Les protocoles à vecteur de distance sont excellents pour les petits réseaux. Cependant, lorsque les réseaux commencent à s'étendre, il faut plus de temps aux routeurs pour converger car ils envoient périodiquement l'intégralité de la table de routage à chaque routeur. Un autre inconvénient des protocoles à vecteur de distance est l'efficacité ; ils choisissent les routes qui sont plus proches en termes de sauts, mais ce n'est pas toujours la route la plus efficace.

L'un des protocoles à vecteur de distance courants est RIP (Routing Information Protocol). Il diffuse la table de routage à chaque routeur du réseau toutes les 30 secondes. Pour un grand réseau, cela peut consommer des ressources importantes. Pour cette raison, RIP limite son nombre de sauts à 15.

## Exercise

C'est en forgeant qu'on devient forgeron ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du routage et de la connectivité réseau :

1. **[Explorer l'interaction de la couche réseau avec ping et arp sous Linux](https://labex.io/fr/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Entraînez-vous à utiliser `ping` et `arp` pour comprendre comment les appareils se découvrent mutuellement et comment le trafic est acheminé au niveau de la couche réseau.
2. **[Simuler la connectivité de la couche réseau sous Linux](https://labex.io/fr/labs/linux-simulate-network-layer-connectivity-in-linux-592752)** - Apprenez à attribuer des adresses IP et à tester la connectivité entre des nœuds Linux simulés, en observant comment les sous-réseaux IP influencent la communication réseau.
3. **[Gérer l'adressage IP sous Linux](https://labex.io/fr/labs/linux-manage-ip-addressing-in-linux-592736)** - Acquérez une expérience pratique de la configuration des adresses IP statiques et dynamiques et de la définition des passerelles par défaut, qui sont des composants essentiels du routage réseau.

Ces laboratoires vous aideront à appliquer les concepts d'adressage et de connectivité réseau dans des scénarios réels, en construisant une base solide pour comprendre comment fonctionnent les protocoles de routage.

## Quiz Question

Vrai ou faux : Les protocoles à vecteur de distance utilisent la route avec le moins de bande passante ?

## Quiz Answer

False
