---
lang: "fr"
title: "Outils DNS"
description: "Apprenez les commandes nslookup et dig pour les requêtes DNS et le dépannage sur Linux. Comprenez comment utiliser ces outils DNS essentiels avec notre guide pour débutants."
keywords: "nslookup, commande dig, outils DNS, DNS Linux, dépannage DNS, tutoriel Linux, Linux pour débutants"
---

## Lesson Content

### nslookup

L'outil "name server lookup" est utilisé pour interroger les serveurs de noms afin de trouver des informations sur les enregistrements de ressources. Voyons où se trouve le serveur de noms pour google.com :

```bash
pete@icebox:~$ nslookup www.google.com
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
Name:   www.google.com
Address: 216.58.192.4
```

### dig

Dig (domain information groper) est un outil puissant pour obtenir des informations sur les serveurs de noms DNS. Il est plus flexible que nslookup et excellent pour le dépannage des problèmes DNS.

```bash
pete@icebox:~$ dig www.google.com

; <<>> DiG 9.9.5-3-Ubuntu <<>> www.google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 42376
;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; MBZ: 0005 , udp: 512
;; QUESTION SECTION:
;www.google.com.                        IN      A

;; ANSWER SECTION:
www.google.com.         5       IN      A       74.125.239.147
www.google.com.         5       IN      A       74.125.239.144
www.google.com.         5       IN      A       74.125.239.146
www.google.com.         5       IN      A       74.125.239.145
www.google.com.         5       IN      A       74.125.239.148

;; Query time: 27 msec
;; SERVER: 127.0.1.1#53(127.0.1.1)
;; WHEN: Sun Feb 07 10:14:00 PST 2016
;; MSG SIZE  rcvd: 123
```

## Exercise

Lisez la page de manuel pour dig.

## Quiz Question

Quel outil est utilisé pour obtenir des informations détaillées sur les serveurs de noms DNS ?

## Quiz Answer

dig
