---
lesson_id: "subnets"
course_id: "subnetting"
lang: "fr"
order_index: 2
title: "Sous-réseaux"
description: "Découvrez comment les préfixes définissent les sous-réseaux IPv4 et influencent la livraison locale, le routage et les politiques."
meta_title: "Sous-réseaux - Sous-réseaux"
meta_description: "Maîtrisez les bases des sous-réseaux et masques Linux, des préfixes réseau et de la segmentation."
meta_keywords: "sous-réseau Linux, masque sous-réseau Linux, sous-réseaux, préfixe réseau, réseau Linux, adresse IP"
---

Un sous-réseau est une plage d’adresses IP définie par un préfixe réseau. Les hôtes d’un sous-réseau se trouvent souvent sur la même liaison locale, mais la proximité physique ne le définit pas : les VLAN, les tunnels, les surcouches et les liaisons routées peuvent modifier la topologie.

## Préfixes et masques

IPv4 peut exprimer un préfixe de 24 bits par `/24` ou par le masque `255.255.255.0`. En binaire, un masque de sous-réseau conventionnel valide possède des uns contigus suivis de zéros :

```text
11111111.11111111.11111111.00000000
```

Pour l’adresse `192.168.1.8/24`, le préfixe réseau est `192.168.1.0/24`. Certains contextes comprennent `192.168.1.0/255.255.255.0`, mais la notation de préfixe CIDR est la forme compacte standard.

:::single-choice{#subnets-mask-24}
Quel masque décimal pointé correspond à `/24` ?

::option[`255.255.255.0`]{#subnets-mask-correct .correct explanation="Trois octets complets contiennent 24 bits un initiaux."}
::option[`255.255.0.255`]{#subnets-noncontiguous explanation="Les bits réseau ne sont pas contigus ; ce n’est pas le masque conventionnel `/24`."}
::option[`0.0.0.24`]{#subnets-prefix-as-octet explanation="Une longueur de préfixe ne se place pas dans le dernier octet du masque."}
:::

## Déterminer si une destination se trouve sur la liaison

Linux installe des routes connectées à partir des adresses et préfixes des interfaces. Il compare une destination aux routes admissibles au lieu de comparer simplement les trois premiers octets décimaux. Pour des limites qui ne coïncident pas avec les octets, telles que `/20`, la séparation se produit à l’intérieur d’un octet.

Examinez les routes connectées et la décision pour une adresse :

```bash
$ ip route show
$ ip route get 192.168.1.50
```

:::single-choice{#subnets-on-link-decision}
Comment un hôte Linux détermine-t-il s’il doit envoyer directement ou par un routeur ?

::option[Il suppose toujours que les adresses terminées par `.1` sont locales.]{#subnets-dot-one explanation="Les conventions de numéros d’hôtes ne remplacent pas les préfixes et les routes configurés."}
::option[Il consulte les préfixes et la politique de routage.]{#subnets-route-policy .correct explanation="La route sélectionnée indique si la destination est directement connectée et quelle interface ou quel prochain saut employer."}
::option[Il demande un masque de sous-réseau à l’application de destination après la connexion.]{#subnets-ask-application explanation="La sélection de route doit avoir lieu avant cet échange applicatif."}
:::

## Routage entre les sous-réseaux

Un routeur doté des interfaces et des routes appropriées peut acheminer le trafic entre des sous-réseaux. Une passerelle par défaut est simplement un prochain saut sélectionné par une route par défaut ; elle ne doit pas nécessairement employer la première adresse utilisable ni se terminer par `.1`.

La séparation en sous-réseaux crée un emplacement où appliquer des politiques de routage et de filtrage, mais ne constitue pas automatiquement une frontière de sécurité. Si l’acheminement est autorisé sans politique restrictive, des hôtes de sous-réseaux différents peuvent encore communiquer.

:::single-choice{#subnets-security-boundary}
La création de deux sous-réseaux bloque-t-elle automatiquement le trafic entre eux ?

::option[Oui, car les routeurs ne peuvent pas relier des préfixes différents.]{#subnets-never-route explanation="Relier des préfixes est le rôle principal du routage."}
::option[Non ; les politiques de routage et de filtrage déterminent le trafic autorisé.]{#subnets-policy-required .correct explanation="La segmentation permet l’application de politiques, mais ne définit pas elle-même ces politiques."}
::option[Oui, sauf si les deux emploient l’adresse d’hôte `.1`.]{#subnets-dot-one-security explanation="Une convention de numéro d’hôte ne contrôle pas l’acheminement."}
:::

## Raisons de créer des sous-réseaux

Les sous-réseaux peuvent organiser l’attribution des adresses, limiter la portée des diffusions de la couche liaison, séparer les domaines de panne et fournir des frontières de politique. Ils peuvent aussi accroître la complexité du routage, du pare-feu, de DHCP, de la surveillance et de la documentation. Concevez les préfixes selon l’échelle, la croissance, la redondance et les exigences de sécurité réelles plutôt que de supposer qu’un réseau plus petit est toujours plus rapide.

:::single-choice{#subnets-design-tradeoff}
Quel est un véritable compromis de la création de sous-réseaux ?

::option[Les domaines de diffusion plus petits n’exigent ni routage ni documentation.]{#subnets-no-complexity explanation="Davantage de frontières exigent généralement une gestion accrue des routes, des politiques, des adresses et des services."}
::option[La segmentation peut améliorer l’organisation tout en augmentant la complexité des politiques.]{#subnets-tradeoff .correct explanation="Les frontières de sous-réseaux peuvent faciliter le contrôle, mais ajoutent un état opérationnel à maintenir."}
::option[Chaque sous-réseau garantit la même latence vers Internet.]{#subnets-equal-latency explanation="Le chemin et les conditions de la charge déterminent la latence."}
:::

## Résumé

Vous savez maintenant relier un préfixe IPv4 à la livraison locale et à la politique routée.

1. Exprimer les masques contigus par des longueurs de préfixe CIDR.
2. Calculer le préfixe réseau à partir des bits de l’adresse et du masque.
3. Employer les routes pour distinguer la livraison locale de celle par un prochain saut.
4. Considérer l’isolation des sous-réseaux comme une possibilité de politique, et non une garantie.
