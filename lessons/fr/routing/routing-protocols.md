---
index: 4
lang: "fr"
title: "Protocoles de Routage"
meta_title: "Protocoles de Routage - Routage"
meta_description: "Découvrez les protocoles de routage comme le vecteur de distance et l'état de lien. Comprenez la convergence réseau et comment les routeurs s'adaptent aux changements. Démarrez votre parcours en réseau Linux !"
meta_keywords: "protocoles de routage, convergence réseau, vecteur de distance, état de lien, réseau Linux, guide du débutant, tutoriel réseau"
---

## Lesson Content

Ce serait fastidieux de devoir configurer manuellement les routes sur une table de routage pour chaque appareil de votre réseau. Au lieu de cela, nous utilisons ce que l'on appelle des protocoles de routage. Les protocoles de routage aident notre système à s'adapter aux changements du réseau ; ils apprennent différentes routes, les intègrent dans la table de routage, puis acheminent nos paquets de cette manière. Il existe deux types principaux de protocoles de routage : les protocoles à vecteur de distance et les protocoles à état de lien.

### Convergence

Avant de parler des protocoles, nous devrions aborder un terme utilisé en routage, connu sous le nom de convergence. Lors de l'utilisation de protocoles de routage, les routeurs communiquent avec d'autres routeurs pour collecter et échanger des informations sur le réseau. Lorsqu'ils s'accordent sur l'apparence d'un réseau, chaque table de routage cartographie la topologie complète du réseau, ainsi "convergeant". Lorsqu'un événement se produit dans la topologie du réseau, la convergence sera temporairement rompue jusqu'à ce que tous les routeurs soient conscients de ce changement.

## Exercise

C'est en forgeant qu'on devient forgeron ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du routage réseau et de l'adressage IP :

1. **[Gérer l'adressage IP sous Linux](https://labex.io/fr/labs/linux-manage-ip-addressing-in-linux-592736)** - Entraînez-vous à configurer des adresses IP statiques et dynamiques, à définir une passerelle par défaut et à vérifier les configurations réseau, ce qui est crucial pour comprendre comment les tables de routage sont construites et utilisées.
2. **[Explorer l'interaction de la couche réseau avec ping et arp sous Linux](https://labex.io/fr/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Apprenez comment les appareils interagissent au niveau de la couche réseau, en observant ARP et comment la passerelle par défaut gère le trafic distant, ce qui donne un aperçu des mécanismes gérés par les protocoles de routage.
3. **[Simuler la connectivité de la couche réseau sous Linux](https://labex.io/fr/labs/linux-simulate-network-layer-connectivity-in-linux-592752)** - Utilisez Docker pour simuler des nœuds réseau, attribuer des adresses IP et tester la connectivité entre les sous-réseaux, en appliquant directement les concepts liés aux changements de réseau et aux décisions de routage.

Ces laboratoires vous aideront à appliquer les concepts de configuration et de connectivité réseau dans des scénarios réels, renforçant ainsi votre confiance avec les éléments fondamentaux que les protocoles de routage automatisent.

## Quiz Question

Quel est le terme utilisé lorsque toutes les tables de routage connaissent la topologie du réseau ?

## Quiz Answer

Convergence
