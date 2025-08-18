---
lang: "fr"
title: "Analyse de paquets"
meta_description: "Apprenez les bases de l'analyse de paquets avec tcpdump. Comprenez le trafic réseau, capturez des données et interprétez la sortie avec ce guide Linux pour débutants."
meta_keywords: "tcpdump, analyse de paquets, analyse réseau, réseau Linux, tutoriel débutant, Wireshark, commandes Linux, trafic réseau"
---

## Lesson Content

Le sujet de l'analyse de paquets pourrait à lui seul remplir un cours entier, et de nombreux livres sont écrits uniquement sur l'analyse de paquets. Cependant, aujourd'hui, nous n'apprendrons que les bases. Il existe deux analyseurs de paquets extrêmement populaires : Wireshark et tcpdump. Ces outils scannent vos interfaces réseau, capturent l'activité des paquets, analysent les paquets et affichent les informations pour que nous puissions les voir. Ils nous permettent d'entrer dans les détails de l'analyse réseau et d'approfondir les aspects de bas niveau. Nous utiliserons tcpdump car il a une interface plus simple ; cependant, si vous deviez ajouter l'analyse de paquets à votre boîte à outils, je vous recommanderais de vous intéresser à Wireshark.

### Install tcpdump

```bash
sudo apt install tcpdump
```

### Capture packet data on an interface

```plaintext
pete@icebox:~$ sudo tcpdump -i wlan0
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on wlan0, link-type EN10MB (Ethernet), capture size 65535 bytes
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

Vous remarquerez beaucoup de choses se produire lorsque vous exécutez une capture de paquets. Eh bien, c'est à prévoir ; il y a beaucoup d'activité réseau en arrière-plan. Dans mon exemple ci-dessus, je n'ai pris qu'un extrait de ma capture, spécifiquement le moment où j'ai décidé de faire un ping sur <www.google.com>.

### Understanding the output

```plaintext
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
```

- Le premier champ est un horodatage de l'activité réseau.
- IP: Ceci contient les informations de protocole.
- Ensuite, vous verrez l'adresse source et de destination : `icebox.lan > nuq04s29-in-f4.1e100.net`.
- `seq`: C'est le numéro de séquence de début et de fin du paquet TCP.
- `length`: Longueur en octets.

Comme vous pouvez le voir dans notre sortie tcpdump, nous envoyons un paquet de requête d'écho ICMP à <www.google.com> et recevons un paquet de réponse d'écho ICMP en retour ! Notez également que différents paquets afficheront des informations différentes ; consultez la page de manuel pour voir ce que sont ces informations.

### Writing tcpdump output to a file

```bash
sudo tcpdump -w /some/file
```

Quelques dernières réflexions : nous n'avons fait qu'effleurer le sujet de l'analyse de paquets. Il y a tellement de choses que vous pouvez examiner, et nous n'avons même pas abordé l'approfondissement avec la sortie Hex et ASCII. Il existe de nombreuses ressources en ligne pour vous aider à en apprendre davantage sur les analyseurs de paquets, et je vous exhorte à les trouver !

## Exercise

Téléchargez et installez l'outil Wireshark et jouez avec l'interface.

## Quiz Question

Quel est le flag pour capturer une interface spécifique avec tcpdump ?

## Quiz Answer

-i
