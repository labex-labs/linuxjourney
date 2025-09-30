---
index: 3
lang: "fr"
title: "Serveur HTTP simple"
meta_title: "Serveur HTTP simple - Partage réseau"
meta_description: "Apprenez à créer un serveur HTTP simple en utilisant le module http.server de Python. Partagez rapidement des fichiers sur votre réseau avec ce tutoriel Linux convivial pour les débutants."
meta_keywords: "http.server, SimpleHTTPServer, serveur web Python, partage de fichiers, tutoriel Linux, guide du débutant"
---

## Lesson Content

Python dispose d'un outil très utile pour servir des fichiers via HTTP. C'est excellent si vous voulez simplement créer un partage réseau rapide auquel d'autres machines de votre réseau peuvent accéder. Pour ce faire, il suffit d'aller dans le répertoire que vous souhaitez partager et d'exécuter :

```bash
python -m http.server
```

Ou, si vous êtes toujours sur Python 2 :

```bash
python -m SimpleHTTPServer
```

Cela met en place un serveur web basique auquel vous pouvez accéder via l'adresse localhost. Donc, prenez l'adresse IP de la machine sur laquelle vous avez exécuté ceci, puis sur une autre machine, accédez-y dans le navigateur avec : `http://IP_ADDRESS:8000`. Sur votre propre machine, vous pouvez visualiser les fichiers disponibles en tapant : `http://localhost:8000` dans votre navigateur web.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la connectivité réseau et de l'adressage IP, qui sont essentiels pour partager des fichiers sur un réseau :

1. **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Entraînez-vous à identifier différents types d'adresses IP et à tester la joignabilité du réseau, crucial pour s'assurer que votre serveur HTTP Python est accessible.
2. **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Apprenez à utiliser la commande `ip a` pour trouver l'adresse IP de votre machine, une étape nécessaire avant d'accéder à vos fichiers partagés depuis un autre appareil.
3. **[Gérer la résolution de nom d'hôte local sous Linux](https://labex.io/fr/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Apprenez à gérer la résolution de nom d'hôte local sous Linux en éditant le fichier /etc/hosts, une compétence clé pour le développement web et les tests réseau.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans les opérations réseau de base sous Linux.

## Quiz Question

Quel outil pouvez-vous utiliser pour créer un serveur HTTP simple avec Python ?

## Quiz Answer

http.server
