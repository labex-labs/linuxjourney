---
lesson_id: "ipv4"
course_id: "subnetting"
lang: "fr"
order_index: 1
title: "IPv4"
description: "Découvrez comment les adresses IPv4, les préfixes, les portées et la sortie des interfaces Linux s’articulent."
meta_title: "IPv4 - Sous-réseaux"
meta_description: "Découvrez les adresses IPv4, leur structure, leurs portées et les outils en ligne de commande Linux tels que ip addr."
meta_keywords: "IPv4, adresse IP, Linux débutant, tutoriel Linux, réseau Linux, ifconfig, ip addr"
---

IPv4 fournit des adresses source et destination de 32 bits aux paquets routés. Une adresse prend son sens avec son préfixe, son interface, sa portée, sa politique de routage et sa durée de vie, et non comme identifiant permanent d’un périphérique entier.

## Notation décimale pointée

IPv4 s’affiche sous forme de quatre octets de huit bits séparés par des points :

```text
192.0.2.165
```

Chaque octet va de 0 à 255 ; l’adresse complète contient donc quatre octets. La longueur du préfixe indique combien de bits initiaux appartiennent au préfixe réseau, comme dans `192.0.2.165/24`.

:::single-choice{#ipv4-address-size} Quelle est la taille d’une adresse IPv4 ?

::option[32 bits répartis en quatre octets.]{#ipv4-thirty-two-bits .correct explanation="Quatre groupes de huit bits produisent la représentation décimale pointée."}
::option[24 bits dans chaque réseau.]{#ipv4-always-twenty-four explanation="Un `/24` est une longueur de préfixe, et non la taille de chaque adresse IPv4."}
::option[128 octets séparés par des deux-points.]{#ipv4-128-bytes explanation="IPv6 comporte 128 bits et emploie une notation hexadécimale séparée par des deux-points."}
:::

## Portée et rôle des adresses

Toutes les adresses IPv4 ne sont pas routables globalement. Citons la boucle locale `127.0.0.0/8`, les adresses lien-local `169.254.0.0/16`, les plages privées telles que `10.0.0.0/8` et les plages de documentation telles que `192.0.2.0/24`. Les adresses de multidiffusion et de diffusion limitée possèdent d’autres sémantiques.

Les adresses privées peuvent être réutilisées dans des réseaux distincts. Le NAT peut les traduire pour une communication externe, mais n’est pas nécessaire à la communication au sein du domaine privé routé.

:::single-choice{#ipv4-private-reuse} Pourquoi `10.0.0.1` peut-elle apparaître dans de nombreuses organisations ?

::option[Chaque instance identifie le même routeur physique.]{#ipv4-same-router explanation="Cette adresse prend son sens dans chaque réseau et n’est pas globalement unique."}
::option[Les routeurs IPv4 ignorent le premier octet.]{#ipv4-ignore-octet explanation="Tous les bits d’adresse participent à la correspondance des routes."}
::option[Elle appartient à une plage destinée à être réutilisée dans les réseaux privés.]{#ipv4-private-range .correct explanation="Des réseaux privés distincts peuvent employer les mêmes adresses sans les annoncer globalement."}
:::

## Examiner les adresses IPv4 sous Linux

Affichez les attributions IPv4 avec :

```bash
$ ip -4 address show
```

Une ligne telle que celle-ci indique davantage que l’adresse :

```text
inet 192.0.2.165/24 brd 192.0.2.255 scope global dynamic eth0
```

Elle montre le préfixe, la diffusion, la portée, le marqueur d’origine dynamique et l’interface. D’autres lignes peuvent indiquer les durées de vie valide et privilégiée. Une interface peut porter plusieurs adresses IPv4.

:::single-choice{#ipv4-ip-output-prefix} Que signifie `/24` dans `192.0.2.165/24` ?

::option[L’adresse expire après 24 secondes.]{#ipv4-prefix-seconds explanation="La durée de vie est indiquée séparément."}
::option[Les 24 premiers bits de l’adresse forment le préfixe réseau.]{#ipv4-prefix-bits .correct explanation="Les huit bits restants identifient des positions au sein de ce préfixe."}
::option[L’interface est le port TCP 24.]{#ipv4-prefix-port explanation="La notation de préfixe CIDR est indépendante des ports de transport."}
:::

## Déterminer la source sélectionnée

La présence d’une adresse ne prouve pas que Linux l’emploiera pour une destination. Les routes, les règles de politique, les métriques et la liaison de l’application influencent la sélection de la source. Interrogez la décision de routage actuelle :

```bash
$ ip route get 198.51.100.20
```

Lisez le prochain saut, l’interface et la source sélectionnés, puis testez le chemin réel de l’application. Ne modifiez pas les adresses d’un hôte distant sans accès à la console ni plan de retour en arrière.

:::single-choice{#ipv4-route-get-purpose} Que peut afficher `ip route get DESTINATION` ?

::option[La configuration de chaque routeur sur tout le chemin Internet.]{#ipv4-all-router-config explanation="Une recherche locale n’interroge pas la configuration des périphériques en aval."}
::option[La décision de routage locale, notamment l’interface et la source privilégiée.]{#ipv4-route-decision .correct explanation="La commande évalue la politique de routage actuelle de l’hôte pour la destination fournie."}
::option[Le mot de passe de l’utilisateur de destination.]{#ipv4-password explanation="Les commandes de routage n’exposent pas les identifiants applicatifs."}
:::

## Résumé

Vous savez maintenant lire une adresse IPv4 comme une partie de l’état de l’interface et du routage.

1. Reconnaître IPv4 comme quatre octets totalisant 32 bits.
2. Interpréter une adresse avec son préfixe.
3. Distinguer les portées privée, boucle locale, lien-local et autres.
4. Examiner les attributions et la source sélectionnée pour une destination.
