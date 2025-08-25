---
index: 3
lang: "fr"
title: "Calcul de sous-réseau"
meta_title: "Calcul de sous-réseau - Sous-réseautage"
meta_description: "Apprenez les bases du calcul de sous-réseau et comment calculer les hôtes disponibles sur un réseau. Comprenez l'adressage IP et les masques de sous-réseau pour les débutants. Commencez votre parcours Linux !"
meta_keywords: "calcul de sous-réseau, adresse IP, masque de sous-réseau, hôtes réseau, binaire, réseau Linux, tutoriel débutant, guide"
---

## Lesson Content

Nous savons donc que les masques de sous-réseau sont importants pour déterminer le nombre d'hôtes que nous pouvons avoir sur notre sous-réseau. Mais combien d'hôtes cela représente-t-il ?

Supposons que j'aie une adresse IP de **192.168.1.0** et un masque de sous-réseau de **255.255.255.0**. Maintenant, alignons ces nombres sous forme binaire. Pour l'instant, utilisez une calculatrice en ligne pour convertir ces valeurs du décimal au binaire.

```
192.168.1.165  = 11000000.10101000.00000001.10100101
255.255.255.0  = 11111111.11111111.11111111.00000000
```

L'adresse IP est masquée par notre masque de sous-réseau. Quand vous voyez un 1, il est masqué, et nous faisons comme si nous ne le voyions pas. Donc, les seuls hôtes possibles que nous pouvons avoir proviennent de la région `00000000`. Rappelez-vous, `11111111` en binaire est égal à 255. Nous comptons également 0 comme un numéro d'hôte, il y a donc 256 options possibles. Cependant, il peut sembler que nous ayons 256 options possibles, mais nous soustrayons en fait 2 hôtes car nous devons tenir compte de l'adresse de diffusion et de l'adresse du sous-réseau, ce qui nous laisse 254 hôtes possibles sur notre sous-réseau. Nous savons donc que nous pouvons avoir des hôtes avec des adresses IP allant de 192.168.1.1 à 192.168.1.254.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'adressage IP et du sous-réseautage :

1. **[Effectuer le sous-réseautage IP et la conversion binaire dans le terminal Linux](https://labex.io/fr/labs/linux-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Maîtrisez le sous-réseautage IP et la conversion binaire, compétences essentielles pour la configuration et la planification de réseau.
2. **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Approfondissez votre compréhension des différents types d'adresses IP et comment vérifier la joignabilité du réseau à l'aide des commandes Linux.
3. **[Simuler la connectivité de la couche réseau sous Linux](https://labex.io/fr/labs/linux-simulate-network-layer-connectivity-in-linux-592752)** - Appliquez vos connaissances en simulant des configurations réseau et en testant la connectivité entre différents sous-réseaux IP dans un environnement pratique.

Ces laboratoires vous aideront à appliquer les concepts d'adressage IP, de masques de sous-réseau et de calcul d'hôtes dans des scénarios réels et à renforcer votre confiance avec les fondamentaux du réseau.

## Quiz Question

Quel est l'équivalent binaire de 255 ?

## Quiz Answer

11111111
