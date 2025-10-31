---
index: 6
lang: "fr"
title: "Outils DNS"
meta_title: "Outils DNS - DNS"
meta_description: "Explorez les outils DNS essentiels pour Linux comme nslookup et la puissante commande dig. Ce tutoriel Linux pour débutants couvre les requêtes DNS et les techniques de dépannage DNS."
meta_keywords: "nslookup, commande dig, outils DNS, DNS Linux, dépannage DNS, recherche de serveur de noms, tutoriel Linux, Linux débutant"
---

## Lesson Content

Sous Linux, plusieurs utilitaires en ligne de commande sont disponibles pour le diagnostic réseau. Lorsqu'il s'agit de problèmes de système de noms de domaine (DNS), deux **outils DNS** principaux se distinguent : `nslookup` et `dig`. Comprendre comment les utiliser est crucial pour tout **dépannage DNS** sur un serveur ou un client **DNS Linux**.

### Utilisation de nslookup pour les requêtes DNS de base

L'outil `nslookup` (name server lookup) est une utilité classique pour interroger les serveurs DNS afin d'obtenir des informations de mappage de nom de domaine ou d'adresse IP. Bien qu'il soit parfois considéré comme obsolète au profit de `dig`, il reste un outil rapide et facile pour les recherches simples.

Pour trouver l'adresse IP d'un domaine comme `www.google.com`, vous pouvez exécuter :

```bash
pete@icebox:~$ nslookup www.google.com
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
Name:   www.google.com
Address: 216.58.192.4
```

Dans ce résultat, `Server` et `Address` indiquent le serveur DNS qui a répondu à la requête. La `Non-authoritative answer` signifie que le serveur a fourni un résultat mis en cache plutôt que de consulter directement la source faisant autorité. `Name` et `Address` montrent l'adresse IP résolue pour le domaine.

### Dépannage DNS avancé avec dig

La commande `dig` (domain information groper) est un outil puissant et flexible pour interroger les serveurs de noms DNS. Elle fournit des informations plus détaillées que `nslookup`, ce qui en fait le choix privilégié pour un **dépannage DNS** sérieux.

Voici un exemple d'utilisation de la **commande dig** :

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

Le résultat de `dig` est organisé en sections :

- **QUESTION SECTION** : Montre la requête qui a été envoyée. Ici, nous avons demandé un enregistrement `A` (adresse) pour `www.google.com`.
- **ANSWER SECTION** : Affiche la réponse reçue du serveur DNS. Dans ce cas, Google a plusieurs adresses IP associées à son domaine.
- **Statistics** : La section finale fournit des métadonnées sur la requête, telles que le temps de requête et le serveur qui a répondu.

En raison de sa sortie détaillée et de sa flexibilité, `dig` est un utilitaire indispensable pour quiconque gère ou dépanne des services réseau sous Linux.

## Exercise

Pour acquérir plus d'expérience avec les utilitaires réseau Linux, envisagez d'essayer le laboratoire pratique suivant :

1. **[Examiner les paramètres de l'interface réseau avec ethtool sous Linux](https://labex.io/fr/labs/comptia-examine-network-interface-settings-with-ethtool-in-linux-592759)** - Apprenez à utiliser la commande `ethtool` pour examiner et gérer les paramètres de l'interface réseau, y compris l'affichage et la définition de la vitesse et du duplex de l'interface, et l'analyse des modes de liaison pour dépanner les problèmes réseau de couche physique.

Ce laboratoire vous aidera à appliquer les concepts dans des scénarios réels et à gagner en confiance dans la gestion des interfaces réseau.

## Quiz Question

Quel outil est utilisé pour obtenir des informations détaillées sur les serveurs de noms DNS ? Veuillez répondre en utilisant uniquement des caractères anglais en minuscules.

## Quiz Answer

dig
