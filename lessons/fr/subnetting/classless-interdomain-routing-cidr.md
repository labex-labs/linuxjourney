---
lesson_id: "classless-interdomain-routing-cidr"
course_id: "subnetting"
lang: "fr"
order_index: 5
title: "CIDR"
description: "Découvrez comment les préfixes CIDR représentent les plages d’adresses, les limites des sous-réseaux et les routes agrégées."
meta_title: "CIDR - Sous-réseaux"
meta_description: "Guide de la notation CIDR, du calcul des plages et des hôtes, des limites de sous-réseaux et de l’agrégation des routes."
meta_keywords: "CIDR, sous-réseaux CIDR, format CIDR, masque sous-réseau, adressage IP, préfixe réseau, réseau Linux"
---

Le routage interdomaine sans classe représente une plage d’adresses par une longueur de préfixe plutôt que par les anciennes classes d’adresses. CIDR permet des attributions de tailles variables, la création de sous-réseaux et l’agrégation des routes pour IPv4 et IPv6.

## Lire la notation des préfixes

Dans `10.42.3.17/24`, les 24 premiers bits constituent le préfixe réseau et huit bits restent variables dans la plage. Le réseau canonique est `10.42.3.0/24` ; l’adresse d’hôte fournie peut néanmoins s’écrire avec le préfixe lors de la configuration d’une interface.

:::single-choice{#cidr-prefix-meaning} Que précise `/24` dans une valeur CIDR IPv4 ?

::option[Vingt-quatre bits initiaux de préfixe réseau.]{#cidr-24-prefix-bits .correct explanation="Les huit bits restants parmi les 32 bits IPv4 varient au sein du préfixe."}
::option[Vingt-quatre adresses utilisables dans chaque sous-réseau.]{#cidr-24-addresses explanation="Un `/24` contient 256 valeurs d’adresses au total."}
::option[Le port TCP de destination du réseau.]{#cidr-24-port explanation="CIDR et les ports de transport sont indépendants."}
:::

## Calculer la taille d’une plage

Le préfixe IPv4 `/23` laisse neuf bits d’hôte et couvre donc `2^9 = 512` adresses au total. Le préfixe aligné `123.12.24.0/23` s’étend sur :

```text
première : 123.12.24.0
dernière : 123.12.25.255
```

Dans un usage de diffusion traditionnel, la première est l’adresse réseau et la dernière la diffusion dirigée. N’appliquez pas aveuglément le raccourci « moins deux » aux liaisons point à point `/31` ou aux routes d’hôtes `/32`.

:::single-choice{#cidr-23-total} Combien d’adresses IPv4 au total un `/23` contient-il ?

::option[512]{#cidr-total-512 .correct explanation="Neuf bits variables créent 2^9 combinaisons."}
::option[23]{#cidr-total-23 explanation="Le numéro du préfixe compte les bits fixes, et non les adresses."}
::option[510]{#cidr-total-510 explanation="Il s’agit du nombre traditionnel utilisable après le retrait des extrémités spéciales, et non de la taille totale de la plage."}
:::

## Vérifier l’alignement

Un préfixe doit commencer sur sa limite binaire. Un `/23` avance par blocs de deux dans le troisième octet lorsque les octets précédents sont fixes ; `123.12.24.0/23` est donc aligné, tandis que `123.12.25.0/23` se réduit à la même plage canonique `123.12.24.0/23`.

:::single-choice{#cidr-canonical-25} Quel est le réseau canonique `/23` qui contient `123.12.25.0` ?

::option[`123.12.25.0/23` uniquement, à partir de 25.]{#cidr-25-unaligned explanation="Le dernier bit du préfixe regroupe les valeurs du troisième octet par paires alignées."}
::option[`123.12.0.0/23`]{#cidr-third-zero explanation="Cela décrit une autre plage `/23`."}
::option[`123.12.24.0/23`]{#cidr-24-canonical .correct explanation="Les valeurs 24 et 25 du troisième octet partagent le même préfixe aligné de 23 bits."}
:::

## Agréger les routes

CIDR peut annoncer un agrégat unique pour plusieurs préfixes contigus, de même taille et correctement alignés. Par exemple, `192.0.2.0/25` et `192.0.2.128/25` se combinent en `192.0.2.0/24`. L’agrégation n’est sûre que si le routeur annonceur peut atteindre correctement tout l’agrégat ou possède une politique qui prévient les boucles et les trous noirs.

:::single-choice{#cidr-aggregate-two-25s} Quel agrégat couvre les deux moitiés de `192.0.2.0/24` ?

::option[`192.0.2.0/26`]{#cidr-aggregate-26 explanation="Un `/26` ne couvre que 64 adresses, moins que chacune des moitiés."}
::option[`192.0.3.0/25`]{#cidr-aggregate-other explanation="Cette plage se trouve hors de la plage d’adresses indiquée."}
::option[`192.0.2.0/24`]{#cidr-aggregate-24 .correct explanation="Les deux plages `/25` contiguës et alignées ne diffèrent que par le bit suivant et partagent le préfixe `/24`."}
:::

## Routage au préfixe le plus long

Lorsque des routes se chevauchent, l’acheminement sélectionne normalement la route admissible dont le préfixe correspondant est le plus long. Une route `/24` est plus spécifique qu’une route `/16` qui la couvre, tandis qu’une route par défaut `/0` ne l’emporte que si aucune route admissible plus spécifique ne correspond.

:::single-choice{#cidr-route-specificity} Pour la destination `10.42.3.8`, quelle route admissible est la plus spécifique ?

::option[`10.42.3.0/24`]{#cidr-route-24 .correct explanation="La correspondance sur 24 bits est plus longue, donc plus spécifique, que `/8`."}
::option[`10.0.0.0/8`]{#cidr-route-8 explanation="Cette route correspond, mais fixe moins de bits de destination."}
::option[`0.0.0.0/0`]{#cidr-default explanation="La route par défaut est le préfixe IPv4 le moins spécifique possible."}
:::

## Résumé

Vous savez maintenant employer la notation CIDR pour les plages d’adresses et la sélection des routes.

1. Interpréter la valeur après la barre comme un nombre de bits initiaux du préfixe.
2. Calculer la taille totale de la plage à partir des bits restants.
3. Ramener un préfixe à sa limite réseau alignée canonique.
4. N’agréger que des plages contiguës et alignées dont l’accessibilité est valide.
5. Préférer le préfixe admissible le plus long lors de la recherche d’une route.
