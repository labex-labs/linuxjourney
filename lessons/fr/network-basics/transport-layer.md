---
index: 6
lang: "fr"
title: "Couche Transport"
meta_title: "Couche Transport - Bases Réseau"
meta_description: "Explorez la Couche Transport dans le réseau Linux. Cette leçon couvre les protocoles clés comme TCP et UDP, la fonction des ports réseau, la segmentation des données et la poignée de main TCP pour un transfert de données fiable."
meta_keywords: "Couche Transport Linux, TCP, UDP, poignée de main TCP, ports réseau, segmentation des données, réseau Linux, protocoles réseau, transfert de données fiable"
---

## Lesson Content

La couche transport est une partie fondamentale du réseautage Linux responsable de la communication de bout en bout et du transfert de données fiable entre les applications sur différents hôtes. Elle prépare les données pour le transport sur le réseau d'une manière structurée et gérable.

### Segmentation des Données

L'une des fonctions principales de la couche transport est la segmentation des données. Elle divise de grandes quantités de données en morceaux plus petits et plus gérables appelés segments. Ce processus rend le transfert de données plus efficace et résilient. Si un segment est perdu ou corrompu pendant la transmission, seule cette petite partie doit être renvoyée, et non l'ensemble des données. Une fois que les segments arrivent à destination, la couche transport les réassemble dans le bon ordre.

### Comprendre les Ports Réseau

Alors que les adresses IP identifient l'hôte correct sur un réseau, elles ne spécifient pas quelle application ou quel service doit recevoir les données. C'est là qu'interviennent les ports réseau. Des services comme HTTP (trafic web) ou SMTP (e-mail) écoutent sur des ports spécifiques et bien connus. Par exemple, HTTP utilise généralement le port 80. La couche transport attache les numéros de port source et de destination à chaque segment, garantissant que les données sont livrées au processus correct sur l'hôte récepteur.

### Protocoles de Transport Principaux TCP et UDP

Il existe deux protocoles de transport principaux utilisés dans les réseaux modernes : TCP (Transmission Control Protocol) et UDP (User Datagram Protocol). Nous allons brièvement aborder UDP puis nous concentrer sur TCP, car il est le plus largement utilisé pour la communication fiable.

### UDP (User Datagram Protocol)

UDP est un protocole sans connexion qui offre une méthode de transport de données rapide mais non fiable. Il ne garantit pas que tous les segments arriveront ou qu'ils arriveront dans le bon ordre. Bien que cela puisse sembler être un inconvénient, UDP est très efficace pour les applications où la vitesse est plus critique que la précision parfaite, comme le streaming vidéo en direct ou les jeux en ligne. La perte de quelques images vidéo est souvent un compromis acceptable pour un flux plus fluide et plus rapide.

### TCP (Transmission Control Protocol)

TCP fournit un flux de données fiable et orienté connexion. Avant que toute donnée ne soit échangée, TCP établit une connexion formelle entre les deux hôtes pour s'assurer qu'ils sont tous deux prêts à communiquer.

### La Poignée de Main TCP

Pour établir une connexion, TCP utilise un processus appelé la poignée de main en trois étapes :

1.  **SYN** : Le client envoie un segment SYN (synchroniser) au serveur pour initier une connexion.
2.  **SYN-ACK** : Le serveur répond avec un segment SYN-ACK (synchroniser-acquitter) pour accuser réception de la demande du client.
3.  **ACK** : Le client renvoie un segment ACK (acquitter) au serveur, confirmant que la connexion est établie.

Une fois la poignée de main terminée, les données peuvent être échangées de manière fiable. TCP utilise des numéros de séquence pour suivre chaque segment, permettant à l'hôte récepteur de les réassembler dans le bon ordre et de demander la retransmission de tout segment manquant. Dans notre exemple de courrier électronique, la couche transport attacherait le port de destination pour SMTP (port 25) et un port source de l'hôte client à chaque segment.

## Exercise

Bien qu'il n'y ait pas de laboratoires spécifiques pour ce sujet, nous vous recommandons d'explorer le [Parcours d'Apprentissage Linux](https://labex.io/fr/learn/linux) complet pour pratiquer les compétences et concepts Linux associés.

## Quiz Question

What is a reliable transport protocol? (Your answer should be in English and is case-sensitive).

## Quiz Answer

TCP
