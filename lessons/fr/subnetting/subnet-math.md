---
index: 3
lang: "fr"
title: "Calcul de Sous-réseau"
meta_title: "Calcul de Sous-réseau - Subnetting"
meta_description: "Apprenez les bases du calcul de sous-réseau et comment calculer les hôtes disponibles sur un réseau. Comprenez l'adressage IP et les masques de sous-réseau pour les débutants. Commencez votre parcours Linux !"
meta_keywords: "calcul de sous-réseau, adresse IP, masque de sous-réseau, hôtes réseau, binaire, réseau Linux, tutoriel débutant, guide"
---

## Lesson Content

Nous savons donc que les masques de sous-réseau sont importants pour déterminer le nombre d'hôtes que nous pouvons avoir sur notre sous-réseau. Alors, combien d'hôtes cela représenterait-il ?

Disons que j'ai une adresse IP de **192.168.1.0** et un masque de sous-réseau de **255.255.255.0**. Maintenant, alignons ces nombres sous forme binaire. Pour l'instant, utilisez un calculateur en ligne pour convertir ces valeurs du décimal au binaire.

```
192.168.1.165  = 11000000.10101000.00000001.10100101
255.255.255.0  = 11111111.11111111.11111111.00000000
```

L'adresse IP est masquée par notre masque de sous-réseau. Quand vous voyez un 1, il est masqué, et nous faisons comme si nous ne le voyions pas. Donc, les seuls hôtes possibles que nous pouvons avoir proviennent de la région `00000000`. Rappelez-vous, `11111111` en forme binaire est égal à 255. Nous comptons également 0 comme numéro d'hôte, il y a donc 256 options possibles. Cependant, il peut sembler que nous ayons 256 options possibles, mais nous soustrayons en fait 2 hôtes car nous devons tenir compte de l'adresse de diffusion (broadcast address) et de l'adresse de sous-réseau (subnet address), ce qui nous laisse avec 254 hôtes possibles sur notre sous-réseau. Nous savons donc que nous pouvons avoir des hôtes avec des adresses IP allant de 192.168.1.1 à 192.168.1.254.

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Quel est l'équivalent binaire de 255 ?

## Quiz Answer

11111111
