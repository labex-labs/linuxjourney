---
lesson_id: "ipv6"
course_id: "subnetting"
lang: "fr"
order_index: 7
title: "IPv6"
description: "Découvrez comment lire les adresses IPv6, les préfixes, les portées, l’autoconfiguration et l’état du routage Linux."
meta_title: "IPv6 - Sous-réseaux"
meta_description: "Guide d’introduction au protocole IPv6, à ses différences avec IPv4 et aux principes de son adressage dans les réseaux Linux modernes."
meta_keywords: "IPv6, IPv4, adresse IP, réseau Linux, protocoles réseau, protocole Internet, épuisement adresses, tutoriel"
---

IPv6 emploie des adresses de 128 bits et a été conçu pour offrir un espace d’adressage bien plus vaste ainsi qu’un comportement actualisé des paquets et de la découverte des voisins. IPv4 et IPv6 sont des protocoles distincts ; les hôtes à double pile peuvent exécuter les deux pendant la transition des réseaux.

## Lire la notation IPv6

Une adresse IPv6 s’écrit sous forme de huit groupes hexadécimaux de 16 bits :

```text
2001:0db8:0000:0000:0000:0000:0000:0025
```

Les zéros initiaux de chaque groupe peuvent être omis, et une suite consécutive de groupes nuls peut être compressée avec `::` :

```text
2001:db8::25
```

Un seul `::` peut apparaître, car sinon le nombre de groupes omis serait ambigu. `2001:db8::/32` est réservé aux exemples de documentation.

:::single-choice{#ipv6-double-colon-rule}
Pourquoi `::` ne peut-il apparaître qu’une seule fois dans une adresse IPv6 ?

::option[Plusieurs marqueurs `::` rendraient le développement ambigu.]{#ipv6-compression-ambiguity .correct explanation="Un seul marqueur de compression peut être développé en un nombre exact de groupes pour atteindre huit."}
::option[Les adresses IPv6 ne contiennent qu’un seul bit zéro.]{#ipv6-one-zero explanation="Une adresse peut contenir de nombreux bits et groupes nuls."}
::option[Ce marqueur sélectionne le port TCP zéro.]{#ipv6-port-zero explanation="La compression des adresses est sans rapport avec les ports de transport."}
:::

## Types et portées des adresses

Les adresses et plages importantes comprennent :

- `::1/128` : boucle locale sur l’hôte ;
- `fe80::/10` : unicast lien-local, normalement présent sur les interfaces IPv6 ;
- `2000::/3` : espace unicast global actuellement attribué ;
- `ff00::/8` : multidiffusion.

IPv6 ne possède aucune adresse de diffusion ; la multidiffusion et la découverte de voisins remplissent des fonctions qu’IPv4 assure souvent par diffusion. Une destination lien-local peut exiger une zone d’interface telle que `fe80::1%eth0`, car le même préfixe existe sur chaque liaison.

:::single-choice{#ipv6-link-local-scope}
Quelle est la portée normale d’une adresse `fe80::/10` ?

::option[Chaque hôte de l’Internet mondial.]{#ipv6-global-link-local explanation="Les adresses unicast globales servent à la portée globale routée."}
::option[Uniquement un fichier de zone DNS.]{#ipv6-dns-only explanation="Les adresses lien-local sont attribuées aux interfaces et employées sur les réseaux."}
::option[Une liaison locale.]{#ipv6-one-link .correct explanation="Les routeurs n’acheminent pas le trafic lien-local ordinaire entre les liaisons."}
:::

## Préfixes et adresses des interfaces

La notation CIDR d’IPv6 emploie une longueur de préfixe de `/0` à `/128`. Un `/64` est la taille standard de la plupart des sous-réseaux locaux et prend en charge l’autoconfiguration sans état. Une interface peut porter simultanément des adresses lien-local, globales stables, temporaires de confidentialité et autres, chacune dotée de durées de vie privilégiée et valide.

:::single-choice{#ipv6-address-multiplicity}
Pourquoi une interface peut-elle afficher plusieurs adresses IPv6 ?

::option[IPv6 exige une adresse pour chaque chiffre hexadécimal.]{#ipv6-one-per-digit explanation="Les chiffres sont une représentation, et non des attributions distinctes à l’interface."}
::option[Des portées et des rôles de confidentialité ou de durée de vie différents peuvent coexister.]{#ipv6-several-roles .correct explanation="Une adresse lien-local et une ou plusieurs adresses globales ou temporaires sont normales."}
::option[Chaque adresse identifie une carte réseau physique distincte.]{#ipv6-separate-card explanation="Une interface peut posséder plusieurs adresses."}
:::

## Découverte des voisins et des routeurs

La découverte de voisins IPv6 emploie ICMPv6 pour la résolution des adresses, la détection des adresses en double, la découverte des routeurs et les informations d’accessibilité. Les annonces de routeur peuvent fournir les préfixes et les informations sur le routeur par défaut. Les hôtes peuvent associer SLAAC à DHCPv6 pour d’autres paramètres ; DHCPv6 ne fournit normalement pas le routeur par défaut.

Le blocage de tout ICMPv6 brise des fonctions essentielles du protocole. La politique du pare-feu doit autoriser les types de messages nécessaires avec une portée appropriée plutôt que de considérer ICMPv6 comme facultatif.

:::single-choice{#ipv6-default-router-source}
Comment un hôte IPv6 apprend-il normalement un routeur par défaut de manière dynamique ?

::option[Par les annonces de routeur.]{#ipv6-router-advertisements .correct explanation="La découverte des routeurs fait partie de la découverte de voisins ICMPv6."}
::option[À partir d’une adresse de diffusion Ethernet.]{#ipv6-ethernet-broadcast explanation="IPv6 n’emploie aucune adresse de diffusion IP."}
::option[À partir de la poignée de main TCP en trois étapes.]{#ipv6-tcp-handshake explanation="TCP établit l’état de transport après la mise à disposition du routage."}
:::

## Examiner et tester IPv6

Examinez séparément les adresses, les routes et les voisins :

```bash
$ ip -6 address show
$ ip -6 route show
$ ip -6 neighbor show
$ ping -6 -c 3 2001:db8::25
```

Employez une véritable adresse de test attribuée plutôt que l’adresse de documentation présentée. Une application à double pile peut réussir par IPv4 alors qu’IPv6 est cassé, ou inversement ; testez donc explicitement chaque famille et ses enregistrements DNS `A` ou `AAAA`.

:::single-choice{#ipv6-dual-stack-test}
Pourquoi tester IPv4 et IPv6 séparément sur un service à double pile ?

::option[Chaque paquet IPv6 doit d’abord devenir une diffusion IPv4.]{#ipv6-becomes-ipv4 explanation="IPv6 et IPv4 natifs constituent des chemins de protocole distincts."}
::option[Les deux familles peuvent posséder des DNS, routes, filtres et pannes différents.]{#ipv6-independent-paths .correct explanation="Une solution de repli réussie peut masquer une famille d’adresses privilégiée défaillante."}
::option[Les outils IPv6 ne peuvent pas afficher l’état des interfaces.]{#ipv6-tools-cannot explanation="Les commandes `ip -6` exposent l’état des adresses, des routes et des voisins."}
:::

## Résumé

Vous savez maintenant lire et tester l’état courant des interfaces et du routage IPv6.

1. Développer ou compresser correctement huit groupes hexadécimaux d’adresse.
2. Distinguer les portées boucle locale, lien-local, globale et multidiffusion.
3. Prévoir plusieurs adresses IPv6 et durées de vie sur une interface.
4. Préserver le trafic nécessaire de découverte des voisins et d’annonces de routeur.
5. Tester indépendamment les chemins IPv4 et IPv6 des services à double pile.
