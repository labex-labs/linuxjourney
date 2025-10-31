---
index: 4
lang: "fr"
title: "Astuces de Sous-réseautage"
meta_title: "Astuces de Sous-réseautage - Sous-réseautage"
meta_description: "Maîtrisez le sous-réseautage avec notre guide sur les astuces de conversion binaire. Apprenez à utiliser le tableau 128+64+32+16+8+4+2+1 pour convertir rapidement les adresses IP du décimal au binaire et vice-versa. Essentiel pour les entretiens et certifications en réseautique."
meta_keywords: "sous-réseautage, conversion binaire, adresse IP, réseau, réseautique Linux, 128+64+32+16+8+4+2+1, 128 64 32 16 8 4 2 1, décimal vers binaire, calcul de sous-réseau, tutoriel, guide"
---

## Lesson Content

Dans le réseautage moderne, vous effectuerez rarement des calculs de sous-réseau à la main, car les outils et les calculateurs automatisent le processus. Cependant, comprendre la conversion manuelle entre le décimal et le binaire est crucial pour les entretiens en réseautique, les examens de certification et pour acquérir une compréhension plus approfondie du fonctionnement de l'adressage IP. Cette leçon fournit quelques astuces simples pour vous aider à le maîtriser.

Premièrement, il est très bénéfique de mémoriser les calculs en base 2, car ils constituent le fondement des mathématiques binaires.

- 2^1 = 2
- 2^2 = 4
- 2^3 = 8
- 2^4 = 16
- 2^5 = 32
- 2^6 = 64
- 2^7 = 128
- 2^8 = 256

### Le Tableau de Conversion Binaire

Pour convertir facilement des nombres, nous utilisons un tableau qui représente la valeur de chaque bit dans un octet de 8 bits d'une adresse IP.

```plaintext
1   1  1  1  1 1 1 1
128 64 32 16 8 4 2 1
```

Ce tableau est votre outil principal. Chaque nombre correspond à la position d'un bit. La somme totale, `128+64+32+16+8+4+2+1`, est égale à 255, qui est la valeur la plus élevée possible dans un octet.

### Conversion du Décimal au Binaire

Convertissons l'adresse IP `192.168.23.43` en binaire. Nous allons parcourir le premier octet, `192`, pour démontrer le processus. Nous utilisons les valeurs de notre tableau : `128 64 32 16 8 4 2 1`.

1. Commencez par le nombre `192`. Pouvez-vous lui soustraire 128 ? Oui (192 - 128 = 64). Le premier bit est donc **1**.
2. Notre nouveau nombre est `64`. Pouvez-vous lui soustraire la valeur suivante, 64 ? Oui (64 - 64 = 0). Le deuxième bit est **1**.
3. Notre reste est maintenant `0`. Nous ne pouvons soustraire ni 32, ni 16, ni 8, ni 4, ni 2, ni 1. Par conséquent, les bits restants sont tous **0**.

La forme binaire de 192 est `11000000`. Vous pouvez appliquer cette même méthode de soustraction aux autres octets.

### Conversion du Binaire au Décimal

Pour reconvertir du binaire au décimal, vous additionnez simplement les valeurs du tableau là où un `1` apparaît dans le nombre binaire. Convertissons `11000000` en décimal.

En regardant le tableau `128 64 32 16 8 4 2 1`, les deux premiers bits sont `1`. Cela signifie que nous additionnons les deux premières valeurs :

`128 + 64 = 192`

Puisque tous les autres bits sont `0`, nous n'ajoutons aucune autre valeur. La formule `128 + 64 + 0 + 0 + 0 + 0 + 0 + 0` nous donne 192. C'est aussi simple que ça !

## Exercise

La pratique rend parfait ! Bien que les calculs de sous-réseau soient souvent automatisés dans le monde réel, comprendre les conversions binaires sous-jacentes est crucial pour les entretiens et une compréhension plus approfondie du réseautage. Voici un laboratoire pratique pour renforcer votre compréhension :

1. **[Effectuer le sous-réseautage IP et la conversion binaire dans le terminal Linux](https://labex.io/fr/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Maîtrisez le sous-réseautage IP et la conversion binaire en utilisant Python dans un terminal Linux pour convertir des adresses IP, traduire des masques CIDR et calculer des détails de réseau.

Ce laboratoire vous aidera à appliquer les concepts de conversion binaire et de sous-réseautage dans un scénario pratique et à renforcer votre confiance dans les fondamentaux de l'adressage réseau.

## Quiz Question

Quelle est la conversion binaire de 123 ? Veuillez fournir la réponse en caractères anglais (nombres).

## Quiz Answer

1111011
