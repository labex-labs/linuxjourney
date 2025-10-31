---
index: 1
lang: "fr"
title: "Qu'est-ce que le DNS ?"
meta_title: "Qu'est-ce que le DNS ? - DNS"
meta_description: "Si vous souhaitez apprendre le réseau sous Linux, comprendre le DNS est crucial. Ce guide explique ce qu'est le système de noms de domaine (DNS), comment il traduit les noms de domaine en adresses IP, et pourquoi il est l'annuaire essentiel d'Internet. Un point de départ parfait pour quiconque souhaite apprendre Linux."
meta_keywords: "DNS, Système de noms de domaine, Adresse IP, Apprendre Linux, Linux apprendre, Nom d'hôte, Réseau Linux, Débutant, Tutoriel, Guide, Labex Linux"
---

## Lesson Content

### L'annuaire téléphonique d'Internet

Imaginez que chaque fois que vous vouliez visiter Google, vous deviez taper `http://192.78.12.4` au lieu de `www.google.com`. Sans le Domain Name System (DNS), c'est exactement à cela que ressemblerait Internet. Les protocoles réseau de bas niveau ne comprennent que les adresses IP numériques pour identifier un hôte. Le DNS est le système qui nous permet, à nous humains, d'utiliser des noms mémorables pour les sites Web et les serveurs au lieu de longues chaînes de chiffres. Considérez-le comme un carnet d'adresses pour Internet : vous recherchez un nom pour trouver le numéro correspondant.

### Comment fonctionne le DNS

À la base, le DNS traduit les noms d'hôte lisibles par l'homme (comme `www.google.com`) en adresses IP lisibles par la machine (comme `192.78.12.4`). Ce processus est appelé résolution. Lorsque vous tapez un nom de domaine dans votre navigateur, votre ordinateur envoie une requête à un serveur DNS, qui recherche ensuite l'adresse IP correcte et la renvoie, permettant à votre navigateur de se connecter au serveur du site Web.

### Un système mondial distribué

Le DNS n'est pas une base de données unique et centrale. C'est plutôt un système distribué massif. Les propriétaires de sites Web gèrent leurs propres enregistrements DNS pour indiquer au monde comment trouver leur domaine. Ces domaines individuels communiquent entre eux, formant un vaste répertoire interconnecté pour l'ensemble d'Internet. Cette structure décentralisée rend le système incroyablement résilient et évolutif.

### Pourquoi vous devriez apprendre le DNS sous Linux

Si vous souhaitez **apprendre Linux** pour l'administration système ou le développement Web, comprendre le DNS est essentiel. La capacité de configurer, de gérer et de dépanner le DNS est une compétence fondamentale. Ce cours couvrira les bases, mais sachez que le DNS est un sujet vaste et complexe. Pour le maîtriser véritablement, vous devrez effectuer des recherches et des pratiques supplémentaires. C'est un excellent premier pas sur votre chemin vers **linux learn**.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du DNS et de la résolution de noms d'hôte. Utiliser un **labex linux terminal** pour ces exercices est un excellent moyen d'acquérir une expérience pratique.

1. **[Interroger les enregistrements DNS sous Linux avec dig et nslookup](https://labex.io/fr/labs/comptia-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - Apprenez à utiliser des outils Linux essentiels comme `dig` et `nslookup` pour interroger différents types d'enregistrements DNS, vous aidant à comprendre comment les noms d'hôte sont résolus en adresses IP.
2. **[Gérer la résolution de noms d'hôte locaux sous Linux](https://labex.io/fr/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Entraînez-vous à modifier le fichier `/etc/hosts` pour gérer la résolution de noms d'hôte locaux, une compétence fondamentale pour contrôler la manière dont votre système Linux résout les noms sans dépendre de serveurs DNS externes.
3. **[Configurer un serveur DNS faisant autorité local sur Linux](https://labex.io/fr/labs/comptia-set-up-a-local-authoritative-dns-server-on-linux-592803)** - Acquérir une expérience pratique en configurant votre propre serveur DNS faisant autorité local à l'aide de `bind9`, vous permettant d'approfondir la manière dont les zones et les enregistrements DNS sont gérés.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance avec le DNS et la résolution de noms d'hôte dans un environnement Linux.

## Quiz Question

Vrai ou faux : Le DNS nous aide à trouver les adresses MAC pour les noms d'hôte ?

## Quiz Answer

False
