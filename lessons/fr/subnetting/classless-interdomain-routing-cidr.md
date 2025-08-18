---
index: 5
lang: "fr"
title: "CIDR"
meta_title: "CIDR - Subnetting"
meta_description: "Apprenez la notation CIDR pour le réseau Linux. Comprenez les masques de sous-réseau, l'adressage IP et le calcul d'hôtes avec ce guide convivial pour débutants. Améliorez vos compétences réseau !"
meta_keywords: "CIDR, masque de sous-réseau, adressage IP, préfixe réseau, réseau Linux, débutant, tutoriel, guide"
---

## Lesson Content

Le CIDR (Classless Inter-Domain Routing) est utilisé pour représenter un masque de sous-réseau de manière plus compacte. Vous pouvez voir des sous-réseaux notés en notation CIDR, où un sous-réseau tel que 10.42.3.0/255.255.255.0 est écrit 10.42.3.0/24. Cette notation inclut à la fois le préfixe du sous-réseau et le masque de sous-réseau.

Rappelez-vous, une adresse IP se compose de 4 octets ou 32 bits. Le CIDR indique le nombre de bits utilisés comme préfixe réseau. Ainsi, 123.12.24.0/23 signifie que les 23 premiers bits sont utilisés. Qu'est-ce que cela signifie ? Combien d'hôtes cela représente-t-il ?

Une astuce simple consiste à soustraire l'adresse CIDR (23) du nombre total de bits qu'une adresse IP peut avoir (32). Cela laisse 9 bits. Par conséquent, 2^9 = 512. Cependant, nous devons retirer 2 adresses (l'adresse du sous-réseau et l'adresse de diffusion), nous avons donc 510 hôtes utilisables.

## Exercise

No exercises for this lesson.

## Quiz Question

No questions, move along!

## Quiz Answer
