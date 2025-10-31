---
index: 3
lang: "fr"
title: "Processus DNS"
meta_title: "Processus DNS - DNS"
meta_description: "Explorez le processus de résolution DNS étape par étape, des serveurs racine au serveur DNS faisant autorité. Comprenez comment un serveur Linux trouve un domaine, un concept crucial pour les environnements de production et l'hébergement de domaines."
meta_keywords: "processus DNS, recherche DNS, résolution de domaine, dns linux, serveur de production, hébergement de domaine, serveur dns, TLD, serveurs racine, dns faisant autorité"
---

## Lesson Content

Explorons comment un ordinateur, tel qu'un `serveur Linux`, trouve un `domaine` comme `catzontheinterwebz.com` en utilisant le DNS. Le processus fonctionne comme un entonnoir, réduisant la recherche jusqu'à ce que nous atteignions le `serveur DNS` spécifique qui détient la réponse.

### La Requête Initiale

D'abord, votre hôte demande à son serveur DNS récursif configuré : « Où se trouve `catzontheinterwebz.com` ? » Ce serveur récursif, souvent fourni par votre FAI, ne connaît probablement pas la réponse directement. Il commence donc le processus de résolution en contactant la plus haute autorité : les serveurs Root (Racine). Cette étape initiale est la même, que vous naviguiez depuis chez vous ou qu'un `serveur de production` communique avec une API.

### Serveurs Root (Racine)

La hiérarchie DNS d'Internet commence par 13 serveurs Root logiques, qui sont répliqués sur des centaines d'emplacements physiques à travers le monde. Ces serveurs ne connaissent pas l'adresse IP de chaque `domaine`, mais ils savent qui gère les domaines de premier niveau (TLD) comme `.com`, `.org` et `.net`. Lorsqu'on lui demande `catzontheinterwebz.com`, un serveur Root répondra : « Je ne sais pas, mais vous devriez demander au serveur TLD `.com` », et fournira son adresse IP.

### Serveurs TLD (Domaine de Premier Niveau)

Ensuite, le serveur récursif envoie une nouvelle requête au serveur TLD `.com`, demandant à nouveau l'emplacement de `catzontheinterwebz.com`. Le travail du serveur TLD est d'indiquer les serveurs de noms faisant autorité corrects pour ce `domaine` spécifique. Il ne possède pas l'adresse IP finale, mais il sait quel `serveur DNS` est responsable du `domaine`, un détail souvent configuré via votre fournisseur d'`hébergement de domaine`. Le serveur TLD répond avec l'adresse IP de ce serveur de noms faisant autorité.

### Serveur DNS Faisant Autorité

Enfin, le serveur récursif envoie une dernière requête au `serveur DNS` faisant autorité. C'est le serveur qui détient les enregistrements DNS réels pour le `domaine` `catzontheinterwebz.com`. Ce serveur consulte ses enregistrements, trouve l'enregistrement 'A' pour l'hôte et renvoie l'adresse IP finale. C'est une étape critique pour quiconque met un site web ou une application en ligne, car ce serveur fournit le lien définitif entre le nom de `domaine` et l'adresse IP du `serveur de production`. Avec l'adresse IP en main, votre ordinateur peut maintenant se connecter et récupérer le contenu.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la résolution et de la gestion DNS :

1. **[Interroger les enregistrements DNS sous Linux avec dig et nslookup](https://labex.io/fr/labs/comptia-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - Apprenez à interroger les enregistrements DNS comme A, PTR et MX, et à identifier votre serveur DNS par défaut, essentiel pour le dépannage réseau.
2. **[Configurer un serveur DNS faisant autorité local sous Linux](https://labex.io/fr/labs/comptia-set-up-a-local-authoritative-dns-server-on-linux-592803)** - Acquérir une expérience pratique en installant et configurant un serveur DNS faisant autorité local, en définissant des zones et en testant la résolution DNS.
3. **[Gérer la résolution de noms d'hôte locale sous Linux](https://labex.io/fr/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - S'exercer à gérer la résolution de noms d'hôte locaux en modifiant le fichier `/etc/hosts`, une compétence clé pour le développement web et les tests réseau.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance avec le DNS.

## Quiz Question

Quelle est l'abréviation des serveurs de noms où se trouvent les adresses .com, .net, .org, etc. ? Veuillez répondre en utilisant uniquement des lettres majuscules anglaises.

## Quiz Answer

TLD
