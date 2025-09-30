---
index: 3
lang: "fr"
title: "Processus DNS"
meta_title: "Processus DNS - DNS"
meta_description: "Apprenez comment DNS fonctionne étape par étape, des serveurs racine au DNS faisant autorité. Comprenez le processus de recherche DNS pour les utilisateurs débutants et intermédiaires."
meta_keywords: "processus DNS, recherche DNS, comment fonctionne DNS, tutoriel DNS, DNS débutant, DNS Linux, TLD, serveurs racine"
---

## Lesson Content

Examinons un exemple de la façon dont votre hôte trouve un domaine (catzontheinterwebz.com) avec DNS. Essentiellement, nous descendons l'entonnoir jusqu'à ce que nous atteignions le serveur DNS qui connaît ce domaine.

### Serveur DNS local

Tout d'abord, notre hôte demande : « Où est catzontheinterwebz.com ? » Notre serveur DNS local ne le sait pas, alors il va commencer par le haut de l'entonnoir pour demander aux serveurs racine. Gardez à l'esprit que notre hôte ne fait pas ces requêtes pour trouver directement catzontheinterwebz.com ; la plupart des utilisateurs parlent à un serveur DNS récursif fourni par leurs FAI, et ce serveur est ensuite chargé de trouver l'emplacement de catzontheinterwebz.com.

### Serveurs racine

Il existe 13 serveurs racine pour Internet. Ils sont mis en miroir et distribués dans le monde entier pour gérer les requêtes DNS pour Internet, il y a donc en réalité des centaines de serveurs qui fonctionnent. Ils sont contrôlés par différentes organisations et contiennent des informations sur les domaines de premier niveau. Les domaines de premier niveau sont ce que vous connaissez comme les adresses .org, .com, .net, etc. Ainsi, le serveur racine ne sait pas où se trouve catzontheinterwebz.com, mais il nous dit de demander au serveur DNS de domaine de premier niveau .com à une adresse IP qu'il nous donne.

### Domaine de premier niveau

Nous envoyons donc maintenant une autre requête au serveur de noms qui connaît les adresses ".com" et lui demandons s'il sait où se trouve catzontheinterwebz.com. Le TLD n'a pas catzontheinterwebz.com dans ses fichiers de zone, mais il voit un enregistrement pour le serveur de noms de catzontheinterwebz.com. Il nous donne donc l'adresse IP de ce serveur de noms et nous dit de regarder là.

### Serveur DNS faisant autorité

Nous envoyons maintenant une dernière requête au serveur DNS qui possède réellement l'enregistrement que nous voulons. Le serveur de noms voit qu'il a un fichier de zone pour catzontheinterwebz.com, et il y a un enregistrement de ressource pour 'www' pour cet hôte. Il nous donne ensuite l'adresse IP de cet hôte, et nous pouvons enfin voir des chats sur Internet.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la résolution et de la gestion DNS :

1. **[Interroger les enregistrements DNS sous Linux avec dig et nslookup](https://labex.io/fr/labs/comptia-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - Apprenez à interroger les enregistrements DNS comme A, PTR et MX, et à identifier votre serveur DNS par défaut, essentiel pour le dépannage réseau.
2. **[Configurer un serveur DNS local faisant autorité sous Linux](https://labex.io/fr/labs/comptia-set-up-a-local-authoritative-dns-server-on-linux-592803)** - Acquérez une expérience pratique en installant et en configurant un serveur DNS local faisant autorité, en définissant des zones et en testant la résolution DNS.
3. **[Gérer la résolution de nom d'hôte local sous Linux](https://labex.io/fr/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Entraînez-vous à gérer la résolution de nom d'hôte local en modifiant le fichier `/etc/hosts`, une compétence clé pour le développement web et les tests réseau.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance avec DNS.

## Quiz Question

Quelle est l'abréviation des serveurs de noms où se trouvent les adresses .com, .net, .org, etc. ?

## Quiz Answer

TLD
