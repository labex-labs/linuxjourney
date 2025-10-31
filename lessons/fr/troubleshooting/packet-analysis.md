---
index: 5
lang: "fr"
title: "Analyse de Paquets"
meta_title: "Analyse de Paquets - Dépannage"
meta_description: "Apprenez les fondamentaux de l'analyse de paquets réseau sous Linux. Ce guide présente tcpdump, un puissant analyseur de paquets, pour capturer et interpréter le trafic réseau."
meta_keywords: "tcpdump, analyse de paquets, analyse de paquets réseau, analyseur de paquets réseau, analyse réseau, outils d'analyse de paquets réseau, réseau Linux, Wireshark, commandes Linux, trafic réseau"
---

## Lesson Content

Le domaine de l'analyse des paquets réseau est vaste et peut faire l'objet de cours et de livres entiers. Cette leçon présentera les fondamentaux. L'analyse des paquets implique la capture et l'inspection des données qui transitent sur un réseau. C'est une compétence essentielle pour le dépannage réseau, l'optimisation des performances et l'analyse de sécurité. En examinant les paquets individuels, vous pouvez obtenir des aperçus approfondis de ce qui se passe sur votre réseau à un niveau bas.

### Outils populaires d'analyse de paquets réseau

Il existe deux outils d'analyse de paquets réseau extrêmement populaires : Wireshark et tcpdump. Ce sont tous deux de puissantes applications d'analyse de paquets qui scannent vos interfaces réseau, capturent l'activité des paquets et analysent les données pour inspection. Ils nous permettent d'entrer dans les détails de l'analyse réseau. Nous utiliserons tcpdump pour sa simplicité en ligne de commande, mais si vous prévoyez d'approfondir l'analyse des paquets réseau, explorer l'interface graphique de Wireshark est fortement recommandé.

### Installation de tcpdump

Sur les systèmes basés sur Debian comme Ubuntu, vous pouvez installer tcpdump avec la commande suivante :

```bash
sudo apt install tcpdump
```

### Capture de données de paquets en direct

Pour commencer à capturer des données sur une interface spécifique, utilisez l'indicateur `-i` suivi du nom de l'interface.

```plaintext
pete@icebox:~$ sudo tcpdump -i wlan0
tcpdump: sortie verbeuse supprimée, utilisez -v ou -vv pour un décodage de protocole complet
écoute sur wlan0, type de lien EN10MB (Ethernet), taille de capture 65535 octets
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
11:28:24.960464 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 3, length 64
11:28:24.979299 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 3, length 64
11:28:25.961869 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 4, length 64
11:28:25.976176 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 4, length 64
11:28:26.963667 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 5, length 64
11:28:26.976137 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 5, length 64
11:28:30.674953 ARP, Request who-has 172.254.1.0 tell ThePickleParty.lan, length 28
11:28:31.190665 IP ThePickleParty.lan.51056 > 192.168.86.255.rfe: UDP, length 306
```

Vous remarquerez beaucoup d'activité lorsque vous exécutez une capture de paquets, ce qui est attendu étant donné le trafic réseau constant en arrière-plan. L'exemple ci-dessus montre un extrait d'une capture effectuée lors du ping de `www.google.com`.

### Interprétation de la sortie tcpdump

Décomposons une ligne de la capture :

```plaintext
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
```

- **Horodatage** : Le premier champ (`11:28:23.958840`) indique quand le paquet a été capturé.
- **Protocole** : `IP` indique le protocole de la couche réseau.
- **Source et Destination** : `icebox.lan > nuq04s29-in-f4.1e100.net` montre l'origine et la destination du paquet.
- **Informations spécifiques au protocole** : Le reste de la ligne contient des détails spécifiques au protocole. Pour ce paquet ICMP :
  - `seq` : Le numéro de séquence du paquet.
  - `length` : La longueur du paquet en octets.

Comme vous pouvez le voir, notre machine a envoyé une requête d'écho ICMP et a reçu une réponse d'écho ICMP. Différents protocoles afficheront des informations différentes, veuillez donc consulter la page de manuel pour plus de détails.

### Sauvegarde des captures pour analyse ultérieure

Au lieu d'afficher le trafic en direct, vous pouvez enregistrer la capture dans un fichier à l'aide de l'indicateur `-w`. Ceci est utile pour une analyse de paquets hors ligne plus approfondie.

```bash
sudo tcpdump -w /some/file.pcap
```

Nous n'avons fait qu'effleurer la surface de l'analyse des paquets. Il y a beaucoup plus à explorer, y compris le filtrage avancé et l'inspection du contenu des paquets en Hexadécimal et ASCII. D'innombrables ressources en ligne peuvent vous aider à maîtriser les outils d'analyse de paquets réseau, et nous vous encourageons à poursuivre votre parcours d'apprentissage.

## Exercise

Pour consolider votre compréhension de l'analyse des paquets, essayez ce laboratoire pratique. La pratique rend parfait !

1. **[Analyser les trames Ethernet avec tcpdump sous Linux](https://labex.io/fr/labs/comptia-analyze-ethernet-frames-with-tcpdump-in-linux-592765)** - Entraînez-vous à capturer et inspecter les trames Ethernet, à générer du trafic et à analyser les en-têtes de trame et les adresses MAC à l'aide de `tcpdump`.

Ce laboratoire vous aidera à appliquer les concepts d'analyse de paquets dans un scénario réel et à renforcer votre confiance dans le dépannage réseau.

## Quiz Question

Quel est l'indicateur pour capturer une interface spécifique avec tcpdump ? Veuillez répondre en utilisant uniquement l'indicateur requis en anglais. La réponse est sensible à la casse.

## Quiz Answer

-i
