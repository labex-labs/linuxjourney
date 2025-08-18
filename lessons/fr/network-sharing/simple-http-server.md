---
lang: "fr"
title: "Serveur HTTP Simple"
meta_title: "Serveur HTTP Simple - Partage Réseau"
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

Cela met en place un serveur web basique auquel vous pouvez accéder via l'adresse localhost. Donc, prenez l'adresse IP de la machine sur laquelle vous avez exécuté cela, puis sur une autre machine, accédez-y dans le navigateur avec : `http://IP_ADDRESS:8000`. Sur votre propre machine, vous pouvez visualiser les fichiers disponibles en tapant : `http://localhost:8000` dans votre navigateur web.

## Exercise

Essayez de configurer un `http.server` !

## Quiz Question

Quel outil pouvez-vous utiliser pour créer un serveur HTTP simple avec Python ?

## Quiz Answer

http.server
