---
lang: "fr"
title: "Sous-réseaux"
meta_description: "Découvrez les sous-réseaux et les masques de sous-réseau dans le réseau Linux. Comprenez les préfixes de réseau et comment les sous-réseaux segmentent le trafic. Démarrez avec ce guide convivial pour débutants !"
meta_keywords: "sous-réseaux, masque de sous-réseau, préfixe de réseau, réseau Linux, adresse IP, débutant, tutoriel, ifconfig"
---

## Lesson Content

Comment savoir si je suis sur le même réseau que Patty ? Eh bien, nous pouvons simplement regarder le subnet, abréviation de sous-réseau. Un subnet est un groupe d'hôtes avec des adresses IP qui sont similaires d'une certaine manière. Ces hôtes sont généralement situés à proximité les uns des autres, et vous pouvez facilement envoyer et recevoir des données vers et depuis des hôtes sur le même subnet. Pensez-y comme envoyer du courrier dans le même code postal ; c'est beaucoup plus facile que d'envoyer du courrier dans un autre État.

Par exemple, tous les hôtes avec une adresse IP qui commence par 123.45.67 seraient sur le même subnet. Mon hôte a une IP de 123.45.67.8, et celle de Patty a une IP de 123.45.67.9. Les nombres communs sont mon network prefix, et le 8 et le 9 sont nos hôtes ; par conséquent, mon réseau est le même que celui de Patty. Un subnet est divisé en un network prefix, tel que 123.45.67.0, et un subnet mask.

### Subnet Masks

Les subnet masks déterminent quelle partie de votre adresse IP est la partie réseau et quelle partie est la partie hôte.

Un subnet mask typique peut ressembler à ceci :

```plaintext
255.255.255.0
```

La portion 255 est en fait notre mask. Pour rendre cela un peu plus facile à comprendre, rappelez-vous comment nous appelons chaque octet 8 bits ? En informatique, un bit est désigné par un 0 ou un 1 sous forme binaire. Lorsque des nombres binaires sont utilisés, 1 signifie allumé et 0 signifie éteint. Alors, à quoi correspondent 8 0 ou 1 ?

Recherchez sur Google "calculateur binaire vers décimal" et convertissez 11111111 en forme décimale. Qu'obtenez-vous ? 255 ! Donc un octet varie de 0 à 255. Donc si nous avions un subnet mask de 255.255.255.0, et une adresse IP de 192.168.1.0, combien d'hôtes y a-t-il sur ce subnet ? Nous trouverons la réponse à cela dans notre leçon de mathématiques sur les subnets.

De plus, lorsque nous parlons de notre subnet, nous le désignons couramment par le network prefix suivi du subnet mask :

```plaintext
123.234.0.0/255.255.0.0
```

### Pourquoi ?

Pourquoi diable faisons-nous des subnets ? Le subnetting est utilisé pour segmenter les réseaux et contrôler le flux de trafic au sein de ce réseau. Ainsi, un hôte sur un subnet ne peut pas interagir avec un autre hôte sur un subnet différent.

Mais attendez une minute, et si je veux me connecter à d'autres hôtes comme yahoo.com ? Alors vous devez connecter les subnets entre eux. Pour connecter des subnets, il vous suffit de trouver les hôtes qui sont connectés à plus d'un subnet. Par exemple, si mon hôte à 192.168.1.129 est connecté à un réseau local de 192.168.1.129/24, il peut atteindre n'importe quel hôte sur ce réseau. Pour atteindre les hôtes sur le reste d'Internet, il doit communiquer via le router. Traditionnellement, sur la plupart des réseaux avec un subnet mask de 255.255.255.0, le router est généralement à l'adresse 1 du subnet, donc 192.168.1.1. Maintenant, ce router aura un port qui le connecte à un autre subnet (plus dans le cours sur le Routing). Certaines adresses IP (private networks) ne sont pas visibles sur Internet, et nous avons des choses comme NAT en place (plus à ce sujet plus tard).

## Exercise

Use `ifconfig` to view your subnet mask.

## Quiz Question

Vrai ou faux, un sous-réseau se compose d'un masque de sous-réseau et d'un préfixe de réseau.

## Quiz Answer

True
