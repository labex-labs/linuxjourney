---
index: 4
lang: "fr"
title: "netstat"
meta_title: "netstat - Dépannage"
meta_description: "Maîtrisez la commande linux netstat pour analyser les connexions réseau, les ports et les sockets. Ce guide couvre les états courants comme SYN_SENT et netstat close_wait pour un dépannage efficace."
meta_keywords: "netstat linux, netstat, commande netstat, syn_sent netstat, netstat close_wait, connexions réseau, réseau linux, analyse réseau, tutoriel linux"
---

## Lesson Content

### Ports Bien Connus

Nous avons discuté de la manière dont les données sont transmises via les ports de notre machine. Examinons quelques ports courants et bien connus. Vous pouvez trouver une liste de ces ports dans le fichier **/etc/services** :

```plaintext
ftp             21/tcp
ssh             22/tcp
smtp            25/tcp
domain          53/tcp  # DNS
http            80/tcp
https           443/tcp
..etc..
```

La première colonne indique le nom du service, suivi de son numéro de port attribué et du protocole de couche transport qu'il utilise.

### Introduction à netstat sous Linux

Un outil extrêmement utile pour recueillir des informations réseau détaillées est **netstat**. La commande `netstat sous linux` affiche un large éventail de données liées au réseau, y compris les connexions réseau actives, les tables de routage et les statistiques d'interface. On l'appelle souvent le couteau suisse des outils de mise en réseau.

Cette leçon se concentrera sur l'utilisation de `netstat` pour vérifier l'état des connexions réseau. Avant de plonger dans un exemple, clarifions la différence entre les sockets et les ports. Un **port** est un identifiant numérique utilisé pour diriger les données vers une application spécifique. Une **socket** est un point de terminaison pour la communication, permettant aux programmes d'envoyer et de recevoir des données. L'adresse de la socket est la combinaison unique d'une adresse IP et d'un numéro de port. Chaque connexion entre un hôte et une destination nécessite une socket unique. Par exemple, bien que le service HTTP s'exécute sur le port 80, plusieurs connexions HTTP peuvent exister simultanément, et une socket unique est créée pour chacune d'elles.

Examinons le résultat de `netstat -at` :

```bash
pete@icebox:~$ netstat -at
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 icebox:domain           *:*                     LISTEN
tcp        0      0 localhost:ipp           *:*                     LISTEN
tcp        0      0 icebox.lan:44468        124.28.28.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34751        124.28.29.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34604        economy.canonical.:http TIME_WAIT
tcp6       0      0 ip6-localhost:ipp       [::]:*                  LISTEN
tcp6       1      0 ip6-localhost:35094     ip6-localhost:ipp       CLOSE_WAIT
tcp6       0      0 ip6-localhost:ipp       ip6-localhost:35094     FIN_WAIT2
```

La commande `netstat -a` affiche toutes les sockets en écoute et non en écoute, tandis que l'indicateur `-t` filtre le résultat pour n'afficher que les connexions TCP.

Les colonnes sont les suivantes :

- **Proto**: Le protocole utilisé (par exemple, TCP ou UDP).
- **Recv-Q**: La file d'attente des données en attente de réception.
- **Send-Q**: La file d'attente des données en attente d'envoi.
- **Local Address**: L'adresse de l'hôte local.
- **Foreign Address**: L'adresse de l'hôte distant.
- **State**: L'état actuel de la socket.

### Comprendre les États de Connexion

La colonne **State** fournit des informations cruciales sur le statut d'une connexion. Voici quelques états courants que vous rencontrerez :

- **LISTENING** (ÉCOUTE) : La socket attend les connexions entrantes. Pour qu'une connexion TCP soit établie, la destination doit être en mode écoute.
- **SYN_SENT** : Lors de l'utilisation de `netstat`, un état `SYN_SENT` indique que la socket tente activement d'établir une connexion.
- **ESTABLISHED** (ÉTABLIE) : La socket dispose d'une connexion entièrement établie.
- **CLOSE_WAIT** (ATTENTE DE FERMETURE) : L'état `netstat close_wait` signifie que l'hôte distant s'est déconnecté et que le système local attend que l'application ferme la socket.
- **TIME_WAIT** : La socket attend après la fermeture pour gérer tout paquet qui pourrait encore être sur le réseau.

Vous pouvez trouver une liste complète des états de socket dans la page de manuel `netstat`.

## Exercise

La pratique rend parfait ! Voici un laboratoire pratique pour renforcer votre compréhension des paramètres des interfaces réseau :

1. **[Examiner les paramètres des interfaces réseau avec ethtool sous Linux](https://labex.io/fr/labs/comptia-examine-network-interface-settings-with-ethtool-in-linux-592759)** - Apprenez à utiliser la commande `ethtool` pour examiner et gérer les paramètres des interfaces réseau, y compris l'affichage et la définition de la vitesse et du duplex de l'interface, et l'analyse des modes de liaison pour dépanner les problèmes réseau de couche physique.

Ce laboratoire vous aidera à appliquer les concepts dans des scénarios réels et à gagner en confiance dans la gestion des interfaces réseau.

## Quiz Question

Quel port est utilisé pour HTTPS ?

## Quiz Answer

443
