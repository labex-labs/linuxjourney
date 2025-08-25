---
index: 2
lang: "fr"
title: "Composants DNS"
meta_title: "Composants DNS - DNS"
meta_description: "Découvrez les composants DNS : serveurs de noms, fichiers de zone et enregistrements de ressources. Comprenez comment fonctionne le DNS pour les débutants. Commencez votre parcours de mise en réseau Linux !"
meta_keywords: "composants DNS, serveur de noms, fichier de zone, enregistrements de ressources, tutoriel DNS, mise en réseau Linux, guide du débutant"
---

## Lesson Content

La base de données DNS d'Internet repose sur des sites et des organisations qui fournissent une partie de cette base de données. Pour ce faire, ils ont besoin de :

### Serveur de noms

Nous configurons le DNS via des "serveurs de noms". Les serveurs de noms chargent nos paramètres et configurations DNS et répondent à toutes les questions des clients ou d'autres serveurs qui veulent savoir des choses comme "Qui est google.com ?". Si le serveur de noms ne connaît pas la réponse à cette requête, il redirigera la demande vers d'autres serveurs de noms. Les serveurs de noms peuvent être "autoritaires", ce qui signifie qu'ils détiennent les enregistrements DNS réels que vous recherchez, ou "récursifs", ce qui signifie qu'ils interrogeraient d'autres serveurs, et ces serveurs interrogeraient d'autres serveurs jusqu'à ce qu'ils trouvent un serveur autoritaire contenant les enregistrements DNS. Les serveurs récursifs peuvent également avoir les informations que nous voulons en cache au lieu d'atteindre un serveur autoritaire.

### Fichier de zone

À l'intérieur d'un serveur de noms se trouve ce qu'on appelle des fichiers de zone. Les fichiers de zone sont la manière dont le serveur de noms stocke les informations sur le domaine ou comment accéder au domaine s'il ne le connaît pas.

### Enregistrements de ressources

Un fichier de zone est composé d'entrées d'enregistrements de ressources. Chaque ligne est un enregistrement et contient des informations sur les hôtes, les serveurs de noms, d'autres ressources, etc. Les champs sont les suivants :

- Nom de l'enregistrement
- TTL - Le temps après lequel nous rejetons l'enregistrement et en obtenons un nouveau. En DNS, le TTL est indiqué par le temps, de sorte que les enregistrements peuvent avoir un TTL d'une heure. La raison pour laquelle nous faisons cela est que l'Internet est en constante évolution ; une minute un hôte peut être mappé à une adresse IP X, puis la minute suivante il peut être à une adresse IP Y.
- Classe - Espace de noms des informations d'enregistrement. Le plus souvent, IN est utilisé pour Internet.
- Type - Type d'informations stockées dans les données de l'enregistrement. Nous n'entrerons pas dans les types d'enregistrements, mais vous en avez probablement vu des courants comme A pour l'adresse, MX pour l'échangeur de courrier, etc.
- Données - Ce champ peut contenir une adresse IP s'il s'agit d'un enregistrement A ou autre chose selon le type d'enregistrement.

```plaintext
patty    IN  A      192.168.0.4
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du DNS et de la résolution de noms d'hôtes :

1. **[Configurer un serveur DNS autoritaire local sous Linux](https://labex.io/fr/labs/linux-set-up-a-local-authoritative-dns-server-on-linux-592803)** - Entraînez-vous à installer et configurer un serveur DNS local (`bind9`), à définir des zones et à valider votre configuration.
2. **[Interroger les enregistrements DNS sous Linux avec dig et nslookup](https://labex.io/fr/labs/linux-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - Apprenez à utiliser les outils de ligne de commande essentiels (`dig`, `nslookup`) pour interroger différents types d'enregistrements DNS et dépanner les problèmes DNS.
3. **[Gérer la résolution de noms d'hôtes locale sous Linux](https://labex.io/fr/labs/linux-manage-local-hostname-resolution-in-linux-592792)** - Comprenez comment gérer la résolution de noms d'hôtes locale en modifiant le fichier `/etc/hosts`, une compétence clé pour le développement et les tests.

Ces laboratoires vous aideront à appliquer les concepts de DNS et de résolution de noms d'hôtes dans des scénarios réels et à renforcer votre confiance avec les services réseau.

## Quiz Question

Quel type d'enregistrement de ressource est utilisé pour les échangeurs de courrier ?

## Quiz Answer

MX
