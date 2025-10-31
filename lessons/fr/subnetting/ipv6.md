---
index: 7
lang: "fr"
title: "IPv6"
meta_title: "IPv6 - Sous-réseautage"
meta_description: "Un guide pour débutants sur le protocole IPv6. Découvrez pourquoi IPv6 a été créé, en quoi il diffère d'IPv4, et comprenez les bases de son schéma d'adressage pour le réseau Linux moderne."
meta_keywords: "IPv6, IPv4, adresse IP, réseau Linux, protocoles réseau, protocole internet, épuisement des adresses, débutant, tutoriel, guide"
---

## Lesson Content

Chaque appareil qui se connecte à Internet, de votre serveur à votre smartphone, nécessite une adresse IP unique pour communiquer. La version la plus utilisée, IPv4, offre un nombre fini d'adresses, une limite que nous approchons rapidement dans notre monde de plus en plus connecté. Ce problème est connu sous le nom d'épuisement des adresses IPv4.

### Qu'est-ce qu'IPv6 ?

Pour résoudre ce problème, l'Internet Engineering Task Force (IETF) a développé une nouvelle version du Protocole Internet : IPv6. L'objectif principal d'IPv6 est d'étendre considérablement le pool d'adresses IP disponibles, garantissant ainsi qu'Internet puisse continuer à croître et à accueillir des milliards de nouveaux appareils. Il inclut également d'autres améliorations au protocole réseau.

### IPv4 contre IPv6

Bien qu'IPv6 ait été créé pour pallier les limites d'IPv4, son adoption a été progressive. Il n'est pas destiné à remplacer immédiatement IPv4. Au contraire, les deux protocoles réseau sont conçus pour coexister et se compléter. De nombreux réseaux fonctionnent aujourd'hui en mode "double pile" (dual-stack), prenant en charge IPv4 et IPv6 simultanément. Si vous êtes familier avec IPv4, les concepts fondamentaux d'IPv6 seront faciles à appréhender.

### Comprendre les adresses IPv6

La différence la plus significative que vous remarquerez est le format de l'adresse. Une adresse IPv4 est un nombre de 32 bits généralement écrit sous la forme de quatre nombres décimaux séparés par des points (ex. : `192.168.1.1`). En revanche, une adresse IPv6 est un nombre de 128 bits écrit en hexadécimal et séparé par des deux-points.

Voici à quoi ressemble une adresse IPv6 typique :

```plaintext
2dde:1235:1256:3:200:f8ed:fe23:59cf
```

Ce format plus long permet un nombre beaucoup plus grand d'adresses IP uniques, assurant l'avenir de la connectivité Internet.

## Exercise

Pour maîtriser les concepts d'IPv6, la pratique est essentielle. Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'adressage IPv6 et de son interaction avec IPv4 dans un environnement Linux :

1. **[Configurer et vérifier les adresses IPv6 sous Linux](https://labex.io/fr/labs/comptia-configure-and-verify-ipv6-addresses-in-linux-592858)** - Entraînez-vous à attribuer des adresses IPv6 statiques et à tester la connectivité à l'aide des commandes `ip` et `ping6`.
2. **[Effectuer des recherches DNS IPv6 sous Linux](https://labex.io/fr/labs/comptia-perform-ipv6-dns-lookups-in-linux-592862)** - Apprenez à interroger les enregistrements AAAA et à vérifier la résolution DNS IPv6 à l'aide de `dig`, `nslookup` et `ping6`.
3. **[Configurer un tunnel 6to4 d'IPv4 vers IPv6 sous Linux](https://labex.io/fr/labs/comptia-configure-an-ipv4-to-ipv6-6to4-tunnel-in-linux-592867)** - Acquérir une expérience pratique de la configuration d'un tunnel 6to4 pour permettre la connectivité IPv6 sur un réseau IPv4 existant.

Ces laboratoires vous aideront à appliquer les concepts d'IPv6 dans des scénarios réels et à renforcer votre confiance dans la configuration et le dépannage réseau.

## Quiz Question

Quel est le nom du protocole IP conçu pour augmenter le nombre d'adresses disponibles pour les hôtes sur Internet ? Veuillez répondre en anglais en utilisant le nom commun du protocole, en faisant attention à la casse.

## Quiz Answer

IPv6
