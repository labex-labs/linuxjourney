---
lesson_id: "osi-model"
course_id: "network-basics"
lang: "fr"
order_index: 2
title: "Modèle OSI"
description: "Découvrez comment le modèle de référence OSI à sept couches organise les fonctions réseau et le vocabulaire du dépannage."
meta_title: "Modèle OSI - Réseaux"
meta_description: "Explorez le modèle OSI à sept couches, ses fonctions réseau et son usage comme cadre de compréhension et de dépannage des réseaux Linux."
meta_keywords: "modèle OSI, réseau Linux, TCP/IP, couches réseau, modèle sept couches, dépannage réseau"
---

Le modèle Open Systems Interconnection est un cadre de référence à sept couches. Il donne aux ingénieurs un vocabulaire commun pour situer les responsabilités, interfaces et défaillances ; il ne décrit pas littéralement chaque implémentation.

## Les sept couches

De la plus basse à la plus haute, les couches OSI sont :

1. Physique : signaux, supports, connecteurs et transmission des bits.
2. Liaison de données : trames locales, adressage de liaison et accès au support.
3. Réseau : adressage logique et transmission entre réseaux.
4. Transport : communication entre terminaux ou processus.
5. Session : gestion des sessions de communication.
6. Présentation : représentation, transformation et encodage des données.
7. Application : services réseau employés par les applications.

:::single-choice{#osi-network-layer-number} Quelle couche OSI traite l'adressage logique et la transmission entre réseaux ?

::option[La couche 3, Réseau.]{#osi-layer-three .correct explanation="La couche réseau décrit l'adressage logique et la transmission entre les réseaux."}
::option[La couche 1, Physique.]{#osi-layer-one explanation="La couche physique concerne les signaux et les supports."}
::option[La couche 7, Application.]{#osi-layer-seven explanation="La couche application décrit les services exposés aux applications réseau."}
:::

## Employer le modèle comme vocabulaire

Des expressions comme « boucle de couche 2 » ou « port de couche 4 » désignent une zone fonctionnelle sans expliquer chaque détail de l'implémentation. Un protocole réel peut franchir des limites, et le chiffrement, les tunnels, mandataires ou surcouches peuvent créer plusieurs couches imbriquées.

:::single-choice{#osi-model-purpose} À quoi le modèle OSI sert-il le plus dans le dépannage quotidien ?

::option[À garantir que chaque protocole possède exactement sept en-têtes.]{#osi-seven-headers explanation="Les implémentations ne correspondent pas une à une à sept en-têtes sur le réseau."}
::option[À remplacer toutes les captures de paquets par un diagramme.]{#osi-replace-captures explanation="Le modèle guide l'enquête, mais ne remplace pas les preuves."}
::option[À fournir une méthode commune de classement des fonctions réseau.]{#osi-shared-vocabulary .correct explanation="Le cadre aide les équipes à réduire la zone fonctionnelle examinée."}
:::

## Comparer OSI et TCP/IP

La suite de protocoles Internet et le modèle de référence OSI sont issus d'histoires de normalisation différentes. Le modèle pratique TCP/IP regroupe souvent dans sa couche application les responsabilités de session et de présentation d'OSI et réunit les aspects physiques et de liaison dans une couche liaison ou accès réseau. Les correspondances sont approximatives et ne prouvent pas que l'une des piles a été directement implémentée à partir de l'autre.

:::single-choice{#osi-tcpip-mapping} Comment faut-il interpréter une correspondance entre couches OSI et TCP/IP ?

::option[Comme une règle exacte à laquelle chaque protocole doit obéir.]{#osi-exact-rule explanation="Les responsabilités des protocoles franchissent souvent les limites conceptuelles."}
::option[Comme la preuve que TCP/IP emploie obligatoirement sept couches sur le réseau.]{#osi-tcp-seven explanation="TCP/IP est couramment présenté avec quatre ou cinq couches."}
::option[Comme une comparaison approximative entre des modèles fonctionnels.]{#osi-approximate-map .correct explanation="Les modèles regroupent certaines responsabilités différemment."}
:::

## Dépanner entre les couches

Partez du symptôme et testez les hypothèses plutôt que de vérifier mécaniquement les couches dans l'ordre numérique. Une défaillance web peut concerner l'état de la liaison locale, le routage IP, l'accessibilité du transport, TLS, la résolution des noms, l'authentification ou le comportement applicatif. Une preuve dans une couche peut guider le test suivant sans démontrer que les couches supérieures fonctionnent.

:::single-choice{#osi-link-success-limit} Que prouve une liaison Ethernet locale qui fonctionne ?

::option[Que tous les services HTTP distants sont sains.]{#osi-link-proves-http explanation="L'état de la liaison locale ne permet pas d'établir la santé d'une application distante."}
::option[Que le DNS ne contient aucun enregistrement incorrect.]{#osi-link-proves-dns explanation="Les données de noms sont indépendantes de la connectivité élémentaire de la liaison."}
::option[Uniquement que les conditions pertinentes de la liaison locale fonctionnent.]{#osi-link-limited-proof .correct explanation="Des défaillances de routage, transport, nommage, sécurité et application peuvent subsister."}
:::

## Résumé

Vous savez maintenant employer le modèle OSI comme vocabulaire de diagnostic en couches.

1. Nommer les sept couches dans l'ordre.
2. Associer chaque couche à sa grande responsabilité.
3. Considérer les correspondances avec TCP/IP comme approximatives.
4. Employer les preuves d'une couche pour guider les tests de bout en bout, pas les remplacer.
