---
lesson_id: "distance-vector-protocols"
course_id: "routing"
lang: "fr"
order_index: 5
title: "Protocoles à vecteur de distance"
description: "Découvrez comment les protocoles à vecteur de distance déduisent les routes des annonces des voisins et limitent les boucles."
meta_title: "Protocoles à vecteur de distance - Routage"
meta_description: "Guide des protocoles à vecteur de distance, du fonctionnement de RIP, du nombre de sauts et de leurs limites pour le routage."
meta_keywords: "protocoles vecteur distance, routage réseau, RIP, protocole information routage, nombre sauts, réseau Linux, tutoriel"
---

Le routage à vecteur de distance indique aux voisins quelles destinations sont accessibles et une métrique qui décrit leur distance. Un routeur associe l’annonce d’un voisin au coût pour atteindre ce voisin afin de déduire son propre chemin candidat.

## Apprendre par les voisins

Si le routeur A annonce une distance de trois vers un préfixe et que le routeur B atteint A avec un coût de un, B peut déduire une distance de quatre par A. L’information décrit une direction et une métrique, et non une carte complète de la topologie, raison pour laquelle cette approche est parfois appelée routage par rumeur.

:::single-choice{#distance-vector-derived-distance}
Si un voisin annonce la métrique 3 et que le coût de la liaison vaut 1, quelle métrique en déduit-on par ce voisin ?

::option[2]{#distance-vector-two explanation="Le coût de la liaison est ajouté, et non soustrait."}
::option[31]{#distance-vector-thirty-one explanation="Ces valeurs sont des métriques, et non des chiffres décimaux à concaténer."}
::option[4]{#distance-vector-four .correct explanation="La distance du voisin et le coût de la liaison locale se combinent pour former le chemin candidat."}
:::

## Boucles et comptage jusqu’à l’infini

Après une panne, des voisins peuvent annoncer par erreur une route l’un vers l’autre et augmenter progressivement sa métrique. Les protocoles limitent ce phénomène avec des valeurs d’infini finies, l’horizon partagé, l’empoisonnement des routes, le retour empoisonné, les mises à jour déclenchées et des minuteurs. Ces mécanismes réduisent le problème, mais ne rendent pas instantanée la convergence après chaque changement de topologie.

:::single-choice{#distance-vector-split-horizon}
Que cherche à réduire l’horizon partagé ?

::option[Le nombre de bits de chaque adresse IPv4.]{#distance-vector-ip-bits explanation="La taille des adresses IPv4 est fixe indépendamment des mises à jour de routage."}
::option[Le coût du chiffrement des charges utiles applicatives.]{#distance-vector-encryption explanation="Cette technique concerne la direction des annonces de routes."}
::option[L’annonce d’une route apprise vers le voisin dont elle provient.]{#distance-vector-no-return .correct explanation="La suppression de cette direction aide à éviter les boucles de rétroaction simples."}
:::

## Métriques et limites de RIP

RIP emploie le nombre de sauts. Une route de métrique 16 est inaccessible ; la plus grande métrique utilisable est donc 15. Cette limite borne l’escalade des boucles, mais aussi le diamètre du réseau. Un nombre inférieur de sauts ne signifie pas nécessairement une latence inférieure ou davantage de bande passante.

RIPv2 emploie des mises à jour périodiques et déclenchées et prend en charge les informations CIDR. Il diffuse couramment les mises à jour en multidiffusion plutôt que de diffuser toute une table dans chaque situation. L’authentification et le filtrage exigent toujours une configuration délibérée.

:::single-choice{#distance-vector-rip-infinity}
Que représente la métrique RIP 16 ?

::option[Le chemin le plus rapide avec seize liaisons parallèles.]{#distance-vector-fastest-16 explanation="RIP considère cette valeur comme inaccessible."}
::option[L’infini, qui signifie que la destination est inaccessible.]{#distance-vector-unreachable .correct explanation="RIP limite les chemins utilisables à 15 sauts."}
::option[Une route apprise par BGP.]{#distance-vector-bgp-route explanation="Ce nombre possède une signification propre à RIP."}
:::

## Évaluer une route apprise

Vérifiez l’état du voisin, les préfixes reçus et annoncés, la métrique, le prochain saut, l’installation de la route et l’accessibilité du plan de données. Une route peut être valide dans RIP, mais perdre face à une autre source de route selon la politique de préférence locale.

:::single-choice{#distance-vector-fewest-hop-limit}
Pourquoi la route RIP au plus faible nombre de sauts peut-elle offrir de mauvaises performances ?

::option[Le nombre de sauts n’encode ni la bande passante, ni la latence, ni les pertes, ni la congestion des liaisons.]{#distance-vector-hop-limited .correct explanation="Un chemin comportant davantage de sauts peut posséder de meilleures liaisons et offrir de meilleures performances applicatives."}
::option[RIP choisit toujours la route qui possède le plus de sauts.]{#distance-vector-most-hops explanation="Sa métrique favorise les plus petits nombres de sauts utilisables."}
::option[Le nombre de sauts se mesure en octets d’espace disque.]{#distance-vector-disk-bytes explanation="Il compte les transitions routées, et non le stockage."}
:::

## Résumé

Vous savez maintenant expliquer la simplicité et les limites du routage à vecteur de distance.

1. Déduire une distance candidate de l’annonce d’un voisin.
2. Reconnaître les boucles et le comptage jusqu’à l’infini.
3. Expliquer la limite utilisable de 15 sauts de RIP et sa métrique 16.
4. Vérifier séparément l’installation de la route et le résultat dans le plan de données.
