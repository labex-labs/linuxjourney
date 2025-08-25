---
index: 1
lang: "fr"
title: "Qu'est-ce que le DNS ?"
meta_title: "Qu'est-ce que le DNS ? - DNS"
meta_description: "Apprenez ce qu'est le DNS et comment il traduit les noms de domaine en adresses IP. Comprenez ce concept fondamental d'Internet avec notre guide Linux convivial pour débutants."
meta_keywords: "DNS, Système de Noms de Domaine, adresse IP, nom d'hôte, réseau Linux, débutant, tutoriel, guide"
---

## Lesson Content

Imaginez que chaque fois que vous vouliez faire une recherche sur Google, vous deviez taper `http://192.78.12.4` au lieu de `www.google.com`. Eh bien, sans le DNS ("Domain Name System"), c'est exactement ce qui se passerait. Le réseau de bas niveau ne comprend que l'adresse IP brute pour identifier un hôte. Le DNS permet à nous, les humains, de garder une trace des sites web et des hôtes par leur nom au lieu d'une adresse IP. C'est comme une liste de contacts pour Internet. Si vous connaissez le nom de quelqu'un mais ne connaissez pas son numéro de téléphone, vous pouvez simplement le chercher dans votre liste de contacts.

Le DNS est fondamentalement une base de données distribuée de noms d'hôtes vers des adresses IP. Nous gérons notre base de données afin que les gens sachent comment accéder à notre site/domaine, et ailleurs, une autre personne gère sa base de données afin que d'autres puissent accéder à leur domaine. Ces domaines peuvent alors communiquer entre eux et construire une liste de contacts massive d'Internet.

Dans ce cours, nous aborderons quelques bases du DNS, mais soyez conscient que le DNS est un sujet exhaustif, et si vous voulez vraiment vous y plonger, vous devrez faire des recherches supplémentaires.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du DNS et de la résolution de noms d'hôtes :

1. **[Interroger les enregistrements DNS sous Linux avec dig et nslookup](https://labex.io/fr/labs/linux-query-dns-records-in-linux-with-dig-and-nslookup)** - Apprenez à utiliser des outils Linux essentiels comme `dig` et `nslookup` pour interroger différents types d'enregistrements DNS, vous aidant à comprendre comment les noms d'hôtes sont résolus en adresses IP.
2. **[Gérer la résolution locale des noms d'hôtes sous Linux](https://labex.io/fr/labs/linux-manage-local-hostname-resolution-in-linux)** - Entraînez-vous à modifier le fichier `/etc/hosts` pour gérer la résolution locale des noms d'hôtes, une compétence fondamentale pour contrôler la façon dont votre système Linux résout les noms sans dépendre de serveurs DNS externes.
3. **[Mettre en place un serveur DNS autoritaire local sous Linux](https://labex.io/fr/labs/linux-set-up-a-local-authoritative-dns-server-on-linux)** - Acquérez une expérience pratique en configurant votre propre serveur DNS autoritaire local à l'aide de `bind9`, ce qui vous permettra d'approfondir la gestion des zones et des enregistrements DNS.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance avec le DNS et la résolution de noms d'hôtes dans un environnement Linux.

## Quiz Question

Vrai ou faux : Le DNS nous aide à trouver les adresses MAC pour les noms d'hôtes ?

## Quiz Answer

False
