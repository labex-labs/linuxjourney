---
index: 3
lang: "fr"
title: "Math des Sous-réseaux"
meta_title: "Math des Sous-réseaux - Sous-réseautage"
meta_description: "Maîtrisez les fondamentaux du calcul des sous-réseaux. Ce guide explique comment effectuer les calculs de masque de sous-réseau pour déterminer le nombre d'hôtes disponibles sur votre réseau. Apprenez les concepts essentiels d'adressage IP et de binaire pour le réseau Linux."
meta_keywords: "math sous-réseau, calcul masque sous-réseau, adresse IP, masque de sous-réseau, hôtes réseau, binaire, réseau Linux, calcul hôte, tutoriel débutant"
---

## Lesson Content

Pour déterminer le nombre d'hôtes qu'un sous-réseau peut prendre en charge, vous devez comprendre quelques notions de base sur les **calculs de sous-réseaux**. Le masque de sous-réseau est la clé de ce calcul.

### Le Rôle du Masque de Sous-Réseau

Prenons une adresse IP de **192.168.1.0** avec un masque de sous-réseau de **255.255.255.0**. La fonction principale du masque de sous-réseau est de distinguer la partie réseau de l'adresse de la partie hôte.

Pour voir comment cela fonctionne, nous pouvons convertir ces valeurs sous leur forme binaire.

```
192.168.1.165  = 11000000.10101000.00000001.10100101
255.255.255.0  = 11111111.11111111.11111111.00000000
```

### Effectuer les Calculs du Masque de Sous-Réseau

Dans la représentation binaire ci-dessus, les `1` dans le masque de sous-réseau correspondent à la partie réseau de l'adresse IP. Cette partie est "masquée" ou fixe. Les `0` dans le masque de sous-réseau correspondent à la partie hôte, qui représente la plage d'adresses que vous pouvez attribuer aux périphériques.

Dans notre exemple, la partie hôte est `00000000`. Il s'agit d'un champ de 8 bits, et avec 8 bits, vous pouvez créer 2^8, soit 256, combinaisons uniques (de 0 à 255).

### Calcul des Hôtes Disponibles

Bien qu'il y ait 256 combinaisons possibles, toutes ne peuvent pas être attribuées aux hôtes. Dans tout sous-réseau, deux adresses sont réservées :

1. **Adresse Réseau :** La première adresse, où tous les bits hôtes sont à `0` (ex: 192.168.1.0).
2. **Adresse de Diffusion (Broadcast) :** La dernière adresse, où tous les bits hôtes sont à `1` (ex: 192.168.1.255).

Par conséquent, le nombre réel d'hôtes utilisables est de 256 - 2 = 254. Cela signifie que pour le réseau `192.168.1.0` avec un masque `255.255.255.0`, vous pouvez attribuer des adresses IP de `192.168.1.1` à `192.168.1.254`. Ce calcul fondamental fait partie intégrante des **calculs de sous-réseaux**.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'adressage IP et du sous-réseautage :

1. **[Effectuer le Sous-réseautage IP et la Conversion Binaire dans le Terminal Linux](https://labex.io/fr/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Maîtrisez le sous-réseautage IP et la conversion binaire, des compétences essentielles pour la configuration et la planification réseau.
2. **[Explorer les Types d'Adresses IP et la Joignabilité sous Linux](https://labex.io/fr/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Approfondissez votre compréhension des différents types d'adresses IP et comment vérifier la joignabilité du réseau à l'aide des commandes Linux.
3. **[Simuler la Connectivité de la Couche Réseau sous Linux](https://labex.io/fr/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Appliquez vos connaissances en simulant des configurations réseau et en testant la connectivité entre différents sous-réseaux IP dans un environnement pratique.

Ces laboratoires vous aideront à appliquer les concepts d'adressage IP, de masque de sous-réseau et de calcul d'hôtes dans des scénarios réels et à renforcer votre confiance dans les fondamentaux du réseau.

## Quiz Question

Quel est l'équivalent binaire de 255 ?

## Quiz Answer

11111111
