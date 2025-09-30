---
index: 5
lang: "fr"
title: "CIDR"
meta_title: "CIDR - Sous-réseautage"
meta_description: "Apprenez la notation CIDR pour le réseau Linux. Comprenez les masques de sous-réseau, l'adressage IP et le calcul d'hôtes avec ce guide convivial pour débutants. Améliorez vos compétences réseau !"
meta_keywords: "CIDR, masque de sous-réseau, adressage IP, préfixe réseau, réseau Linux, débutant, tutoriel, guide"
---

## Lesson Content

Le CIDR (Classless Inter-Domain Routing) est utilisé pour représenter un masque de sous-réseau de manière plus compacte. Vous pouvez voir des sous-réseaux notés en notation CIDR, où un sous-réseau tel que 10.42.3.0/255.255.255.0 est écrit comme 10.42.3.0/24. Cette notation inclut à la fois le préfixe du sous-réseau et le masque de sous-réseau.

Rappelez-vous, une adresse IP se compose de 4 octets ou 32 bits. Le CIDR indique le nombre de bits utilisés comme préfixe réseau. Ainsi, 123.12.24.0/23 signifie que les 23 premiers bits sont utilisés. Qu'est-ce que cela signifie ? Combien d'hôtes cela représente-t-il ?

Une astuce simple consiste à soustraire l'adresse CIDR (23) du nombre total de bits qu'une adresse IP peut avoir (32). Cela laisse 9 bits. Par conséquent, 2^9 = 512. Cependant, nous devons retirer 2 adresses (l'adresse du sous-réseau et l'adresse de diffusion), nous avons donc 510 hôtes utilisables.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du CIDR, de l'adressage IP et du sous-réseautage :

1. **[Effectuer le sous-réseautage IP et la conversion binaire dans le terminal Linux](https://labex.io/fr/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Maîtrisez le sous-réseautage IP et la conversion binaire, y compris la traduction des masques CIDR et le calcul des hôtes utilisables.
2. **[Simuler la connectivité de la couche réseau sous Linux](https://labex.io/fr/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Apprenez à attribuer des adresses IP statiques et observez comment les sous-réseaux IP régissent la communication réseau directe dans un environnement simulé.
3. **[Explorer les types d'adresses IP et l'accessibilité sous Linux](https://labex.io/fr/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explorez l'adressage IP et l'accessibilité réseau à l'aide de commandes comme `ping` et `ip a` pour tester différents types d'IP et la connectivité.

Ces laboratoires vous aideront à appliquer les concepts de CIDR et d'adressage IP dans des scénarios réels et à renforcer votre confiance dans la configuration réseau.

## Quiz Question

Pas de questions, passez votre chemin !

## Quiz Answer
