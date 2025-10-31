---
index: 3
lang: "fr"
title: "Serveur HTTP Simple"
meta_title: "Serveur HTTP Simple - Partage Réseau"
meta_description: "Apprenez à configurer rapidement un serveur HTTP simple sous Linux en utilisant le module http.server de Python. Ce guide explique comment créer un serveur web Linux simple pour un partage de fichiers facile sur votre réseau."
meta_keywords: "serveur http simple linux, serveur http simple sous linux, serveur web linux simple, python http.server, qu'est-ce que python simplehttpserver, partage de fichiers, serveur réseau"
---

## Lesson Content

Python inclut un module intégré qui vous permet de créer instantanément un serveur web, ce qui est incroyablement utile pour le partage de fichiers sur un réseau. La configuration d'un **serveur http simple linux** est un processus simple qui ne nécessite qu'une seule commande.

### Démarrer un serveur HTTP simple sous Linux

Pour commencer, accédez au répertoire que vous souhaitez partager via votre terminal. Une fois que vous êtes dans le répertoire souhaité, vous pouvez démarrer un environnement de **serveur http simple linux** avec la commande suivante si vous utilisez Python 3 :

```bash
python -m http.server
```

Cette commande lance un serveur web de base, rendant le contenu de votre répertoire actuel accessible via HTTP.

### Méthode héritée pour Python 2

Pour les systèmes plus anciens qui utilisent encore Python 2, la commande est légèrement différente. Le module s'appelait auparavant `SimpleHTTPServer`. Si vous vous êtes déjà demandé **qu'est-ce que python simplehttpserver**, c'est simplement l'équivalent Python 2 du module `http.server`. Vous pouvez l'exécuter avec :

```bash
python -m SimpleHTTPServer
```

### Accéder à votre serveur web linux simple

Après avoir exécuté la commande, votre **serveur web linux simple** sera actif. Vous pouvez accéder aux fichiers partagés depuis une autre machine sur le même réseau en ouvrant un navigateur web et en naviguant vers `http://ADRESSE_IP:8000`, en remplaçant `ADRESSE_IP` par l'IP locale de la machine exécutant le serveur.

Pour visualiser les fichiers sur la même machine, vous pouvez utiliser l'adresse localhost : `http://localhost:8000`.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la connectivité réseau et de l'adressage IP, essentiels pour le partage de fichiers sur un réseau :

1. **[Explorer les types d'adresses IP et la joignabilité sous Linux](https://labex.io/fr/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Entraînez-vous à identifier différents types d'adresses IP et à tester la joignabilité du réseau, crucial pour s'assurer que votre serveur HTTP Python est accessible.
2. **[Identifier les adresses MAC et IP sous Linux](https://labex.io/fr/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Apprenez à utiliser la commande `ip a` pour trouver l'adresse IP de votre machine, une étape nécessaire avant d'accéder à vos fichiers partagés depuis un autre appareil.
3. **[Gérer la résolution de noms d'hôte locaux sous Linux](https://labex.io/fr/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Apprenez à gérer la résolution de noms d'hôte locaux sous Linux en modifiant le fichier /etc/hosts, une compétence clé pour le développement web et les tests réseau.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans les opérations réseau de base sous Linux.

## Quiz Question

Pour Python 3, quel est le nom du module utilisé pour créer un serveur HTTP simple ? (Veuillez répondre en anglais, en faisant attention à la casse).

## Quiz Answer

http.server
