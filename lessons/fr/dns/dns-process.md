---
lang: "fr"
title: "Processus DNS"
meta_title: "Processus DNS - DNS"
meta_description: "Apprenez comment le DNS fonctionne étape par étape, des serveurs racine au DNS faisant autorité. Comprenez le processus de résolution DNS pour les utilisateurs débutants et intermédiaires."
meta_keywords: "processus DNS, résolution DNS, comment fonctionne le DNS, tutoriel DNS, DNS pour débutants, DNS Linux, TLD, serveurs racine"
---

## Lesson Content

Examinons un exemple de la façon dont votre hôte trouve un domaine (catzontheinterwebz.com) avec DNS. Essentiellement, nous nous frayons un chemin jusqu'à ce que nous atteignions le serveur DNS qui connaît ce domaine.

### Local DNS Server

Tout d'abord, notre hôte demande : « Où est catzontheinterwebz.com ? » Notre serveur DNS local ne le sait pas, il va donc commencer par le haut de l'entonnoir pour interroger les Root Servers. Gardez à l'esprit que notre hôte ne fait pas ces requêtes pour trouver directement catzontheinterwebz.com ; la plupart des utilisateurs s'adressent à un serveur DNS récursif fourni par leurs FAI, et ce serveur est ensuite chargé de trouver l'emplacement de catzontheinterwebz.com.

### Root Servers

Il existe 13 Root Servers pour Internet. Ils sont mis en miroir et distribués dans le monde entier pour gérer les requêtes DNS pour Internet, il y a donc en réalité des centaines de serveurs qui fonctionnent. Ils sont contrôlés par différentes organisations et contiennent des informations sur les Top-Level Domains. Les domaines de premier niveau sont ce que vous connaissez comme les adresses .org, .com, .net, etc. Ainsi, le Root Server ne sait pas où se trouve catzontheinterwebz.com, mais il nous dit de demander au serveur DNS de Top-Level Domain .com à une adresse IP qu'il nous donne.

### Top-Level Domain

Nous envoyons donc maintenant une autre requête au serveur de noms qui connaît les adresses « .com » et lui demandons s'il sait où se trouve catzontheinterwebz.com. Le TLD n'a pas catzontheinterwebz.com dans ses fichiers de zone, mais il voit un enregistrement pour le serveur de noms de catzontheinterwebz.com. Il nous donne donc l'adresse IP de ce serveur de noms et nous dit de chercher là.

### Authoritative DNS Server

Nous envoyons maintenant une dernière requête au serveur DNS qui possède réellement l'enregistrement que nous voulons. Le serveur de noms voit qu'il a un fichier de zone pour catzontheinterwebz.com, et il y a un enregistrement de ressource pour 'www' pour cet hôte. Il nous donne ensuite l'adresse IP de cet hôte, et nous pouvons enfin voir des chats sur Internet.

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Quelle est l'abréviation des serveurs de noms où se trouvent les adresses .com, .net, .org, etc. ?

## Quiz Answer

TLD
