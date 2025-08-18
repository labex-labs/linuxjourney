---
lang: "fr"
title: "Astuces de Subnetting"
meta_description: "Apprenez les bases du subnetting et la conversion binaire pour le réseautage. Comprenez les adresses IP et les masques de sous-réseau avec ce guide convivial pour débutants. Commencez à apprendre maintenant !"
meta_keywords: "subnetting, conversion binaire, adresse IP, réseau, réseautage Linux, débutant, tutoriel, guide"
---

## Lesson Content

Je déteste devoir ajouter cette section. Dans le monde réel, vous n'auriez très probablement jamais à faire de calculs de sous-réseau à la main. Cependant, si vous étiez interviewé à ce sujet, vous devrez savoir comment convertir vers et depuis la forme binaire pour le subnetting. Heureusement, il existe des astuces arithmétiques que vous pouvez mémoriser.

Tout d'abord, mémorisez vos calculs en base 2 ; faites-le simplement :

- 2^1 = 2
- 2^2 = 4
- 2^3 = 8
- 2^4 = 16
- 2^5 = 32
- 2^6 = 64
- 2^7 = 128
- 2^8 = 256
- 2^9 = 512
- 2^10 = 1024
- 2^11 = 2048
- 2^12 = 4096

### Decimal to Binary Chart

```plaintext
1   1  1  1  1 1 1 1
128 64 32 16 8 4 2 1
```

Il y a de nombreuses raisons pour lesquelles le tableau suivant se présente de cette manière. Si vous êtes curieux de savoir comment cela fonctionne, il existe de nombreuses ressources en ligne.

Ok, vous avez mémorisé cela ? Faisons une conversion rapide du décimal au binaire :

### Convert 192.168.23.43 to Binary

Rappelez-vous : 128 / 64 / 32 / 16 / 8 / 4 / 2 / 1

Voyons comment convertir le premier octet en binaire, et vous comprendrez comment le reste fonctionne.

1. Pouvez-vous soustraire 192 - 128 ? Oui, donc le premier bit est 1.
2. 192 - 128 = 64. Le nombre suivant dans le tableau est 64. Pouvez-vous soustraire 64 - 64 ? Oui, donc le deuxième bit est 1.
3. Nous n'avons plus de nombres à soustraire, donc notre forme binaire de 192 est 11000000.

### Convert Binary 11000000 to Decimal

Pour la conversion du binaire au décimal, vous additionnez les nombres qui ont un 1, donc :

128 + 64 + 0 + 0 + 0 + 0 + 0 + 0 = 192!

## Exercise

Regardez votre adresse IP et votre masque de sous-réseau et voyez combien d'hôtes vous pouvez avoir sur votre sous-réseau.

## Quiz Question

Quelle est la conversion binaire de 123 ?

## Quiz Answer

1111011
