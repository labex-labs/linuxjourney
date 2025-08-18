---
index: 6
lang: "fr"
title: "Couche de Transport"
meta_title: "Couche de Transport - Bases du Réseau"
meta_description: "Découvrez la couche de transport dans le réseau Linux, y compris les protocoles TCP/UDP, les ports et la segmentation des données. Comprenez comment les données sont transférées de manière fiable."
meta_keywords: "Couche de transport Linux, TCP/UDP, ports réseau, segmentation des données, réseau Linux, tutoriel débutant, protocoles réseau"
---

## Lesson Content

La couche de transport nous aide à transférer nos données d'une manière que les réseaux peuvent lire. Elle divise nos données en morceaux qui seront transportés et réassemblés dans le bon ordre. Ces morceaux sont appelés segments. Les segments facilitent le transport des données à travers les réseaux.

### Ports

Même si nous savons où nous envoyons nos données via les adresses IP, elles ne sont pas assez spécifiques pour envoyer nos données à certains processus ou services. Des services tels que HTTP utilisent un canal de communication via les ports. Si nous voulons envoyer des données de page web, nous devons les envoyer via le port HTTP (port 80). En plus de former des segments, la couche de transport attachera également les ports source et destination au segment, de sorte que lorsque le récepteur recevra le paquet final, il saura quel port utiliser.

### UDP

Il existe deux protocoles de transport populaires : UDP et TCP. Nous discuterons brièvement d'UDP et passerons la majeure partie de notre temps sur TCP, car c'est le plus couramment utilisé.

UDP n'est pas une méthode fiable de transport de données ; en fait, il ne se soucie pas vraiment si vous recevez toutes vos données originales. Cela peut sembler terrible, mais il a ses utilisations, comme pour le streaming multimédia. Ce n'est pas grave si vous perdez quelques frames ; en retour, vous obtenez vos données un peu plus rapidement.

### TCP

TCP fournit un flux de données fiable et orienté connexion. TCP utilise des ports pour envoyer des données vers et depuis les hôtes. Une application ouvre une connexion d'un port sur son hôte à un autre port sur un hôte distant. Pour établir la connexion, nous utilisons le TCP handshake.

- Le client (processus de connexion) envoie un segment SYN au serveur pour demander une connexion.
- Le serveur envoie au client un segment SYN-ACK pour accuser réception de la demande de connexion du client.
- Le client envoie un ACK au serveur pour accuser réception de la demande de connexion du serveur.

Une fois cette connexion établie, les données peuvent être échangées via une connexion TCP. Les données sont envoyées en différents segments et sont suivies avec des numéros de séquence TCP afin qu'elles puissent être organisées dans le bon ordre lorsqu'elles sont livrées. Dans notre exemple d'e-mail, la couche de transport attache le port de destination (25) au port source de l'hôte source.

## Exercise

No exercises for this lesson.

## Quiz Question

Quel est un protocole de transport fiable ?

## Quiz Answer

TCP
