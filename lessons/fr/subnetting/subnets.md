---
index: 2
lang: "fr"
title: "Sous-réseaux"
meta_title: "Sous-réseaux - Sous-réseautage"
meta_description: "Maîtrisez les fondamentaux du sous-réseau et du masque de sous-réseau Linux. Ce guide explique le sous-réseautage, les préfixes réseau et comment gérer la segmentation réseau dans un environnement Linux avec sous-réseaux."
meta_keywords: "subnet linux, sous-réseau linux, masque sous-réseau linux, sous-réseautage sous-réseaux, sous-réseaux, masque de sous-réseau, préfixe réseau, réseau Linux, adresse IP"
---

## Lesson Content

Comment savoir si deux ordinateurs se trouvent sur le même réseau ? La réponse réside dans la compréhension du sous-réseau (subnet), abréviation de sous-réseau logique. Un sous-réseau est une division logique d'un réseau IP, regroupant des hôtes ayant des adresses IP similaires. Ces hôtes sont généralement à proximité physique, ce qui permet un transfert de données efficace entre eux. Pensez-y comme à l'envoi de courrier dans le même code postal ; c'est beaucoup plus rapide et simple que de l'envoyer dans un autre État.

Pour qu'un hôte fasse partie d'un **sous-réseau linux**, son adresse IP est divisée en deux parties : un préfixe réseau et un identifiant d'hôte. Par exemple, si un hôte a une IP de 192.168.1.8 et un autre 192.168.1.9, ils partagent probablement le même préfixe réseau. La partie commune identifie le réseau, tandis que les numéros uniques (8 et 9) identifient les hôtes individuels.

### Comprendre le masque de sous-réseau Linux

Un **masque de sous-réseau linux** est ce qui détermine quelle partie d'une adresse IP est la portion réseau et quelle partie est la portion hôte. Un masque de sous-réseau typique ressemble à ceci :

```plaintext
255.255.255.0
```

Pour comprendre cela, nous devons penser en binaire. Chaque nombre dans une adresse IP ou un masque de sous-réseau est un octet, représentant 8 bits. En binaire, un `1` signifie "activé" et un `0` signifie "désactivé". Si vous convertissez le nombre binaire `11111111` en décimal, vous obtenez 255. Cela signifie qu'un octet peut aller de 0 (`00000000`) à 255 (`11111111`).

Les `255` dans le masque "masquent" la partie réseau de l'adresse IP. Ainsi, avec un masque de `255.255.255.0` et une IP de `192.168.1.8`, la partie `192.168.1` est le réseau, et `8` est l'hôte. Nous désignons souvent une configuration de **subnet linux** par son préfixe réseau suivi du masque de sous-réseau, comme `192.168.1.0/255.255.255.0`.

### L'objectif de la segmentation des sous-réseaux (Subnetting Subnets)

Pourquoi créons-nous des sous-réseaux ? La pratique de la **segmentation des sous-réseaux (subnetting subnets)** est cruciale pour organiser et gérer efficacement les réseaux. Elle consiste à diviser un réseau plus grand en segments plus petits et plus gérables. Cela offre plusieurs avantages clés :

- **Performance Améliorée :** En segmentant un réseau, vous réduisez le volume de trafic de diffusion au sein de chaque sous-réseau, ce qui entraîne moins de congestion et une meilleure performance globale.
- **Sécurité Renforcée :** Les sous-réseaux vous permettent d'isoler différentes parties de votre réseau. Un hôte sur un sous-réseau ne peut pas interagir directement avec un hôte sur un autre sans routeur, créant ainsi une frontière de sécurité. Vous pouvez implémenter des règles d'accès sur le routeur pour contrôler le flux de trafic entre les sous-réseaux.
- **Administration Simplifiée :** Décomposer un grand réseau en unités logiques plus petites facilite la gestion, le dépannage et l'application des politiques réseau.

### Connexion des sous-réseaux

Et si vous devez vous connecter à des hôtes sur un réseau différent, comme yahoo.com ? Pour connecter différents sous-réseaux, vous avez besoin d'un appareil connecté à plusieurs sous-réseaux : un routeur.

Par exemple, un hôte à `192.168.1.129` sur un réseau avec un masque `255.255.255.0` peut atteindre n'importe quel autre hôte du réseau `192.168.1.0`. Pour atteindre Internet, il doit envoyer le trafic via sa passerelle, qui est le routeur. Sur de nombreux réseaux domestiques, l'adresse du routeur est souvent `.1` du sous-réseau (par exemple, `192.168.1.1`). Ce routeur possède une autre connexion à un sous-réseau différent (comme le réseau de votre FAI), permettant la communication avec le reste d'Internet.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'adressage IP et du sous-réseautage :

1.  **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Entraînez-vous à utiliser la commande `ip a` pour identifier les informations d'adressage réseau, y compris les adresses IPv4, ce qui est fondamental pour comprendre les sous-réseaux.
2.  **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Apprenez à explorer différents types d'adresses IP et à tester la joignabilité du réseau, ce qui vous aidera à vérifier si les hôtes sont sur le même réseau.
3.  **[Effectuer le sous-réseautage IP et la conversion binaire dans le terminal Linux](https://labex.io/fr/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Maîtrisez le sous-réseautage IP et la conversion binaire, en appliquant directement les concepts de préfixe réseau et d'identification d'hôte abordés dans la leçon.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance avec l'adressage réseau et le sous-réseautage.

## Quiz Question

Un sous-réseau est défini par un préfixe réseau et un masque de sous-réseau. Vrai ou Faux ? (Veuillez répondre par 'True' ou 'False'. La réponse est sensible à la casse et doit être en anglais.)

## Quiz Answer

True
