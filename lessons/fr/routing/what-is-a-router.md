---
lesson_id: "what-is-a-router"
course_id: "routing"
lang: "fr"
order_index: 1
title: "Qu’est-ce qu’un routeur ?"
description: "Découvrez comment les routeurs choisissent les prochains sauts et acheminent les paquets IP entre les réseaux."
meta_title: "Qu’est-ce qu’un routeur ? - Routage"
meta_description: "Guide d’introduction aux routeurs, au routage, à la commutation de paquets, aux sauts et à l’utilisation des tables de routage."
meta_keywords: "routeur, réseau, routage, sauts, commutation paquets, réseau Linux, tutoriel débutant, guide réseau"
---

Un routeur relie des domaines de couche réseau et achemine les paquets IP entre eux. Un hôte Linux peut agir comme routeur lorsque l’acheminement est activé et que ses interfaces, ses routes, sa découverte des voisins et sa politique de filtrage sont correctement configurées.

## Routage et acheminement

Le routage construit ou sélectionne les informations relatives aux préfixes accessibles. L’acheminement applique ces informations à chaque paquet : il examine la destination, choisit une route admissible et un prochain saut, décrémente la limite de sauts et transmet par une interface de sortie.

Il s’agit de questions distinctes du plan de contrôle et du plan de données. Une route peut exister tandis que le pare-feu bloque l’acheminement, ou une interface d’acheminement peut être active sans qu’aucune route valide n’existe.

:::single-choice{#router-forwarding-role}
Que fait l’acheminement des paquets ?

::option[Il applique les informations de routage pour envoyer un paquet vers son prochain saut.]{#router-apply-route .correct explanation="L’acheminement est l’action réalisée pour chaque paquet selon la route et la politique sélectionnées."}
::option[Il crée un identifiant applicatif permanent pour chaque destination.]{#router-create-login explanation="Le routage ne gère pas les comptes des applications distantes."}
::option[Il copie chaque paquet sur toutes les interfaces lorsqu’aucune route n’existe.]{#router-flood-no-route explanation="L’acheminement IP ordinaire abandonne un paquet sans route au lieu d’employer en secours une diffusion semblable à celle d’Ethernet."}
:::

## Tables de routage et routes par défaut

Une route associe un préfixe de destination à une interface de sortie, un prochain saut, une métrique, une préférence de source ou d’autres attributs. La correspondance au préfixe le plus long favorise la route admissible la plus spécifique. Une route par défaut, `/0` en IPv4 ou `::/0` en IPv6, est la correspondance la moins spécifique et n’est employée que lorsqu’aucune route plus spécifique ne l’emporte.

Si aucune route admissible n’existe, le routeur abandonne le paquet et peut produire un message ICMP de destination inaccessible. Une route par défaut est facultative et ne pointe pas nécessairement directement vers l’Internet public.

:::single-choice{#router-default-route}
Quand une route par défaut est-elle sélectionnée ?

::option[Avant l’examen des préfixes propres à la destination.]{#router-default-first explanation="Les préfixes admissibles plus spécifiques sont prioritaires."}
::option[Uniquement lorsque le paquet est une diffusion Ethernet.]{#router-default-broadcast explanation="La sélection d’une route IP repose sur les destinations de la couche réseau."}
::option[Lorsqu’aucune route admissible plus spécifique ne correspond.]{#router-default-fallback .correct explanation="Le préfixe de longueur nulle constitue la route la moins spécifique."}
:::

## Trafic local et routé

Deux hôtes situés sur le même sous-réseau directement connecté échangent normalement des trames sans faire passer le paquet IP par un routeur. Un routeur intervient lorsque la sélection de route le choisit comme prochain saut ou lorsque la topologie et la politique imposent délibérément un passage routé.

Un « routeur » domestique réunit couramment un routeur IP, un commutateur Ethernet, un point d’accès Wi-Fi, un service DHCP, un dispositif NAT et un pare-feu. Chaque fonction doit être diagnostiquée séparément.

:::single-choice{#router-same-subnet-path}
Le trafic entre deux hôtes directement connectés doit-il passer par leur routeur par défaut ?

::option[Oui, car chaque paquet doit atteindre un port WAN.]{#router-always-wan explanation="Une livraison locale directement sur la liaison peut avoir lieu sans routeur."}
::option[Oui, sauf si les deux hôtes possèdent des adresses publiques.]{#router-public-required explanation="La portée publique ou privée ne détermine pas l’acheminement élémentaire sur la liaison."}
::option[Non ; l’émetteur peut adresser directement la destination sur la liaison locale.]{#router-direct-on-link .correct explanation="La table de routage identifie le préfixe connecté comme directement accessible."}
:::

## Sauts et prévention des boucles

Un saut routé est une étape d’acheminement de la couche réseau. Le TTL d’IPv4 et la limite de sauts d’IPv6 sont décrémentés à chaque routeur afin de borner les boucles. Le nombre de sauts n’est pas une mesure complète de la distance ou de la qualité : les liaisons diffèrent en bande passante, latence, pertes, politique et congestion.

:::single-choice{#router-hop-count-limit}
Qu’est-ce qu’un nombre de sauts inférieur ne garantit pas ?

::option[Qu’au moins une étape routée existe.]{#router-hop-exists explanation="Un nombre de sauts positif indique directement un passage routé."}
::option[Un chemin applicatif plus rapide ou meilleur.]{#router-hop-not-quality .correct explanation="Un nombre inférieur de routeurs peut tout de même traverser des liaisons plus lentes, congestionnées ou limitées par une politique."}
::option[Que les champs de limite de sauts sont finis.]{#router-hop-limit-finite explanation="Ces champs sont finis par conception du protocole."}
:::

## Résumé

Vous savez maintenant distinguer la sélection des routes par un routeur de son action d’acheminement.

1. Définir les routeurs par l’acheminement entre réseaux IP.
2. Distinguer le routage du plan de contrôle de l’acheminement du plan de données.
3. Considérer la route par défaut comme la solution de repli la moins spécifique.
4. Reconnaître que le nombre de sauts ne mesure pas à lui seul la qualité du chemin.
