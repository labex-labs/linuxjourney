---
lang: "fr"
title: "netstat"
description: "Apprenez la commande netstat pour l'analyse réseau Linux. Comprenez les connexions réseau, les ports et les sockets avec ce guide convivial pour débutants."
keywords: "netstat, commande netstat, réseau Linux, connexions réseau, tutoriel Linux, débutant, guide"
---

## Lesson Content

### Ports Bien Connus

Nous avons discuté de la transmission de données via les ports de notre machine ; examinons quelques ports bien connus.

Vous pouvez obtenir une liste des ports bien connus en consultant le fichier **/etc/services** :

```plaintext
ftp             21/tcp
ssh             22/tcp
smtp            25/tcp
domain          53/tcp  # DNS
http            80/tcp
https           443/tcp
..etc..
```

La première colonne est le nom du service, puis le numéro de port et le protocole de couche de transport qu'il utilise.

### netstat

Un outil extrêmement utile pour obtenir des informations détaillées sur votre réseau est **netstat**. Netstat affiche diverses informations liées au réseau telles que les connexions réseau, les tables de routage, les informations sur les interfaces réseau, et plus encore ; c'est le couteau suisse des outils de mise en réseau. Nous nous concentrerons principalement sur une fonctionnalité de netstat, à savoir l'état des connexions réseau. Avant d'examiner un exemple, parlons d'abord des sockets et des ports. Un socket est une interface qui permet aux programmes d'envoyer et de recevoir des données, tandis qu'un port est utilisé pour identifier quelle application doit envoyer ou recevoir des données. L'adresse du socket est la combinaison de l'adresse IP et du port. Chaque connexion entre un hôte et une destination nécessite un socket unique. Par exemple, HTTP est un service qui s'exécute sur le port 80 ; cependant, nous pouvons avoir de nombreuses connexions HTTP, et pour maintenir chaque connexion, un socket est créé par connexion.

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

La commande `netstat -a` affiche les sockets d'écoute et non d'écoute pour les connexions réseau ; le drapeau `-t` affiche uniquement les connexions TCP.

Les colonnes sont les suivantes de gauche à droite :

- **Proto**: Protocole utilisé, TCP ou UDP.
- **Recv-Q**: Données en file d'attente pour être reçues.
- **Send-Q**: Données en file d'attente pour être envoyées.
- **Local Address**: Hôte connecté localement.
- **Foreign Address**: Hôte connecté à distance.
- **State**: L'état du socket.

Consultez la page de manuel pour une liste des états de socket, mais en voici quelques-uns :

- **LISTENING**: Le socket est en écoute pour les connexions entrantes. N'oubliez pas que lorsque nous établissons une connexion TCP, notre destination doit être en écoute pour nous avant que nous puissions nous connecter.
- **SYN_SENT**: Le socket tente activement d'établir une connexion.
- **ESTABLISHED**: Le socket a une connexion établie.
- **CLOSE_WAIT**: L'hôte distant s'est arrêté, et nous attendons que le socket se ferme.
- **TIME_WAIT**: Le socket attend après la fermeture pour gérer les paquets encore présents dans le réseau.

## Exercise

Consultez la page de manuel de `netstat` et apprenez toutes les fonctionnalités qu'il a à offrir.

## Quiz Question

Quel port est utilisé pour HTTPS ?

## Quiz Answer

443
