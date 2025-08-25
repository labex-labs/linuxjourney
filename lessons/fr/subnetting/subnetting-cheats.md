---
index: 4
lang: "fr"
title: "Astuces de sous-réseau"
meta_title: "Astuces de sous-réseau - Sous-réseau"
meta_description: "Apprenez les bases du sous-réseau et la conversion binaire pour le réseautage. Comprenez les adresses IP et les masques de sous-réseau avec ce guide convivial pour débutants. Commencez à apprendre maintenant !"
meta_keywords: "sous-réseau, conversion binaire, adresse IP, réseau, réseau Linux, débutant, tutoriel, guide"
---

## Lesson Content

Je déteste devoir ajouter cette section. Dans le monde réel, il est fort probable que vous n'auriez jamais à faire de calculs de sous-réseau à la main. Cependant, si vous étiez interviewé à ce sujet, vous devrez savoir comment convertir vers et depuis la forme binaire pour le sous-réseau. Heureusement, il existe des astuces arithmétiques que vous pouvez mémoriser.

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

### Tableau de conversion décimal-binaire

```plaintext
1   1  1  1  1 1 1 1
128 64 32 16 8 4 2 1
```

Il y a de nombreuses raisons pour lesquelles le tableau suivant se présente de cette manière. Si vous êtes curieux de savoir comment cela fonctionne, il existe de nombreuses ressources en ligne.

Ok, vous les avez mémorisés ? Faisons une conversion rapide du décimal au binaire :

### Convertir 192.168.23.43 en binaire

Rappelez-vous : 128 / 64 / 32 / 16 / 8 / 4 / 2 / 1

Passons en revue la conversion du premier octet en binaire, et vous comprendrez comment le reste fonctionne.

1. Pouvez-vous soustraire 192 - 128 ? Oui, donc le premier bit est 1.
2. 192 - 128 = 64. Le nombre suivant dans le tableau est 64. Pouvez-vous soustraire 64 - 64 ? Oui, donc le deuxième bit est 1.
3. Nous n'avons plus de nombres à soustraire, donc notre forme binaire de 192 est 11000000.

### Convertir le binaire 11000000 en décimal

Pour la conversion du binaire au décimal, vous additionnez les nombres qui ont un 1, donc :

128 + 64 + 0 + 0 + 0 + 0 + 0 + 0 = 192!

## Exercise

La pratique rend parfait ! Bien que les calculs de sous-réseau soient souvent automatisés dans le monde réel, comprendre les conversions binaires sous-jacentes est crucial pour les entretiens et une compréhension plus approfondie du réseau. Voici un laboratoire pratique pour renforcer votre compréhension :

1. **[Effectuer le sous-réseau IP et la conversion binaire dans le terminal Linux](https://labex.io/fr/labs/linux-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Maîtrisez le sous-réseau IP et la conversion binaire en utilisant Python dans un terminal Linux pour convertir des adresses IP, traduire des masques CIDR et calculer les détails du réseau.

Ce laboratoire vous aidera à appliquer les concepts de conversion binaire et de sous-réseau dans un scénario pratique et à renforcer votre confiance dans les fondamentaux de l'adressage réseau.

## Quiz Question

Quelle est la conversion binaire de 123 ?

## Quiz Answer

1111011
