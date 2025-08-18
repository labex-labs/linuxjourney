---
lang: "fr"
title: "Protocoles à Vecteur de Distance"
meta_title: "Protocoles à Vecteur de Distance - Routage"
meta_description: "Découvrez les protocoles à vecteur de distance comme RIP, leur fonctionnement et leurs limitations pour le routage réseau. Comprenez le nombre de sauts et l'efficacité du réseau."
meta_keywords: "protocoles à vecteur de distance, RIP, protocole d'information de routage, nombre de sauts, routage réseau, mise en réseau Linux, guide du débutant, tutoriel"
---

## Lesson Content

Les protocoles à vecteur de distance déterminent le chemin vers d'autres réseaux en utilisant le nombre de sauts qu'un paquet effectue à travers le réseau. Par exemple, si le réseau A est à 3 sauts et que le réseau B est à côté du réseau A, alors nous supposons que le réseau B doit être à 4 sauts. Dans les protocoles à vecteur de distance, la prochaine route serait celle avec le moins de sauts.

Les protocoles à vecteur de distance sont excellents pour les petits réseaux. Cependant, lorsque les réseaux commencent à s'étendre, il faut plus de temps aux routeurs pour converger car ils envoient périodiquement l'intégralité de la table de routage à chaque routeur. Un autre inconvénient des protocoles à vecteur de distance est l'efficacité ; ils choisissent les routes qui sont plus proches en termes de sauts, mais ce n'est pas toujours la route la plus efficace.

L'un des protocoles à vecteur de distance courants est RIP (Routing Information Protocol). Il diffuse la table de routage à chaque routeur du réseau toutes les 30 secondes. Pour un grand réseau, cela peut consommer des ressources importantes. Pour cette raison, RIP limite son nombre de sauts à 15.

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Vrai ou faux : Les protocoles à vecteur de distance utilisent la route avec le moins de bande passante ?

## Quiz Answer

False
