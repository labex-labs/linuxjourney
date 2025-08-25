---
index: 2
lang: "fr"
title: "Sous-réseaux"
meta_title: "Sous-réseaux - Sous-réseautage"
meta_description: "Apprenez les sous-réseaux et les masques de sous-réseau dans le réseau Linux. Comprenez les préfixes réseau et comment les sous-réseaux segmentent le trafic. Démarrez avec ce guide convivial pour débutants !"
meta_keywords: "sous-réseaux, masque de sous-réseau, préfixe réseau, réseau Linux, adresse IP, débutant, tutoriel, ifconfig"
---

## Lesson Content

Comment savoir si je suis sur le même réseau que Patty ? Eh bien, nous pouvons simplement regarder le sous-réseau, abréviation de sous-réseau. Un sous-réseau est un groupe d'hôtes avec des adresses IP qui sont similaires d'une certaine manière. Ces hôtes sont généralement situés à proximité les uns des autres, et vous pouvez facilement envoyer des données vers et depuis des hôtes sur le même sous-réseau. Pensez-y comme envoyer du courrier dans le même code postal ; c'est beaucoup plus facile que d'envoyer du courrier dans un autre État.

Par exemple, tous les hôtes avec une adresse IP qui commence par 123.45.67 seraient sur le même sous-réseau. Mon hôte a une IP de 123.45.67.8, et celui de Patty a une IP de 123.45.67.9. Les nombres communs sont mon préfixe réseau, et les 8 et 9 sont nos hôtes ; par conséquent, mon réseau est le même que celui de Patty. Un sous-réseau est divisé en un préfixe réseau, tel que 123.45.67.0, et un masque de sous-réseau.

### Masques de sous-réseau

Les masques de sous-réseau déterminent quelle partie de votre adresse IP est la partie réseau et quelle partie est la partie hôte.

Un masque de sous-réseau typique peut ressembler à ceci :

```plaintext
255.255.255.0
```

La portion 255 est en fait notre masque. Pour rendre cela un peu plus facile à comprendre, rappelez-vous comment nous appelons chaque octet 8 bits ? En informatique, un bit est représenté par un 0 ou un 1 sous forme binaire. Lorsque des nombres binaires sont utilisés, 1 signifie activé et 0 signifie désactivé. Alors, à quoi correspondent 8 zéros ou 8 uns ?

Recherchez sur Google "calculatrice binaire vers décimal" et convertissez 11111111 en forme décimale. Qu'obtenez-vous ? 255 ! Donc un octet varie de 0 à 255. Donc si nous avions un masque de sous-réseau de 255.255.255.0, et une adresse IP de 192.168.1.0, combien d'hôtes y a-t-il sur ce sous-réseau ? Nous trouverons la réponse à cela dans notre leçon de calcul de sous-réseau.

Aussi, lorsque nous parlons de notre sous-réseau, nous le désignons généralement par le préfixe réseau suivi du masque de sous-réseau :

```plaintext
123.234.0.0/255.255.0.0
```

### Pourquoi ?

Pourquoi diable faisons-nous des sous-réseaux ? Le sous-réseautage est utilisé pour segmenter les réseaux et contrôler le flux de trafic au sein de ce réseau. Ainsi, un hôte sur un sous-réseau ne peut pas interagir avec un autre hôte sur un sous-réseau différent.

Mais attendez une minute, et si je veux me connecter à d'autres hôtes comme yahoo.com ? Alors vous devez connecter les sous-réseaux entre eux. Pour connecter des sous-réseaux, il vous suffit de trouver les hôtes qui sont connectés à plus d'un sous-réseau. Par exemple, si mon hôte à 192.168.1.129 est connecté à un réseau local de 192.168.1.129/24, il peut atteindre n'importe quel hôte sur ce réseau. Pour atteindre les hôtes sur le reste d'Internet, il doit communiquer via le routeur. Traditionnellement, sur la plupart des réseaux avec un masque de sous-réseau de 255.255.255.0, le routeur est généralement à l'adresse 1 du sous-réseau, donc 192.168.1.1. Maintenant, ce routeur aura un port qui le connecte à un autre sous-réseau (plus dans le cours sur le routage). Certaines adresses IP (réseaux privés) ne sont pas visibles sur Internet, et nous avons des choses comme le NAT en place (plus à ce sujet plus tard).

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'adressage IP et du sous-réseautage :

1. **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Entraînez-vous à utiliser la commande `ip a` pour identifier les informations d'adressage réseau, y compris les adresses IPv4, ce qui est fondamental pour comprendre les sous-réseaux.
2. **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Apprenez à explorer différents types d'adresses IP et à tester la joignabilité du réseau, ce qui vous aidera à vérifier si les hôtes sont sur le même réseau.
3. **[Effectuer le sous-réseautage IP et la conversion binaire dans le terminal Linux](https://labex.io/fr/labs/linux-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Maîtrisez le sous-réseautage IP et la conversion binaire, en appliquant directement les concepts de préfixes réseau et d'identification d'hôte abordés dans la leçon.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance en matière d'adressage réseau et de sous-réseautage.

## Quiz Question

Vrai ou faux, un sous-réseau se compose d'un masque de sous-réseau et d'un préfixe réseau.

## Quiz Answer

True
