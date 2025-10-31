---
index: 3
lang: "fr"
title: "traceroute"
meta_title: "traceroute - Dépannage"
meta_description: "Maîtrisez la commande traceroute Linux pour tracer les chemins réseau et dépanner les problèmes de connectivité. Ce tutoriel explique comment traceroute utilise le TTL pour cartographier le chemin emprunté par les paquets jusqu'à leur destination."
meta_keywords: "traceroute, traceroute linux, réseau Linux, dépannage réseau, TTL, routage de paquets, commandes Linux, débutant, tutoriel"
---

## Lesson Content

La commande `traceroute` est un outil de diagnostic réseau fondamental utilisé pour tracer le chemin emprunté par les paquets depuis votre ordinateur jusqu'à un hôte de destination. En révélant chaque « saut » ou routeur rencontré en cours de route, elle vous aide à identifier les goulots d'étranglement du réseau et à dépanner les problèmes de connectivité. L'utilitaire `traceroute linux` est essentiel pour tout administrateur système ou ingénieur réseau.

### Comment fonctionne Traceroute

Le mécanisme derrière `traceroute` réside dans sa manipulation astucieuse du champ Time To Live (TTL) dans l'en-tête d'un paquet IP. Le processus fonctionne comme suit :

1. `traceroute` envoie un paquet de sonde avec une valeur TTL de 1.
2. Le premier routeur sur le chemin reçoit le paquet, décrémente le TTL à 0 et le supprime. Le routeur renvoie ensuite un message ICMP « Time Exceeded » (Temps dépassé) à votre ordinateur.
3. `traceroute` enregistre l'adresse IP du routeur et le temps de trajet aller-retour.
4. Il envoie ensuite un autre paquet, cette fois avec un TTL de 2. Ce paquet passe le premier routeur avec succès mais est supprimé par le deuxième routeur, qui renvoie à nouveau un message « Time Exceeded ».
5. Ce processus se répète, le TTL s'incrémentant de un pour chaque ensemble de paquets subséquent. En construisant une liste des routeurs qui renvoient des messages « Time Exceeded », `traceroute` cartographie l'itinéraire complet.
6. Le processus se termine lorsque les paquets atteignent finalement la destination, qui répond avec un message ICMP « Echo Reply » (Réponse d'écho).

### Comprendre la sortie de Traceroute

Examinons un exemple de sortie de l'exécution de `traceroute` dans un terminal Linux :

```bash
$ traceroute google.com
traceroute vers google.com (216.58.216.174), 30 sauts max, paquets de 60 octets
 1  192.168.4.254 (192.168.4.254)  0.028 ms  0.009 ms  0.008 ms
 2  100.64.1.113 (100.64.1.113)  1.227 ms  1.226 ms 0.920 ms
 3  100.64.0.20 (100.64.0.20)  1.501 ms 1.556 ms  0.855 ms
```

Chaque ligne numérotée représente un saut le long du chemin réseau. Voici comment interpréter les informations :

- **Numéro de saut :** La première colonne (par exemple, `1`, `2`, `3`) indique la séquence du routeur dans le chemin.
- **Nom et adresse IP du routeur :** La partie suivante montre le nom d'hôte (s'il peut être résolu) et l'adresse IP du routeur à ce saut.
- **Temps de trajet aller-retour (RTT) :** Les trois dernières colonnes indiquent le temps de trajet aller-retour pour chacun des trois paquets de sonde envoyés à ce saut spécifique. Ces temps, mesurés en millisecondes (ms), vous aident à évaluer la latence à chaque étape du parcours.

Utiliser la commande `traceroute linux` efficacement fournit un aperçu inestimable des performances et de la structure de votre réseau.

## Exercise

La pratique est essentielle pour maîtriser le diagnostic réseau. Les laboratoires pratiques suivants vous aideront à renforcer votre compréhension de la découverte de chemin réseau et du dépannage avec des outils comme `traceroute` :

1. **[Gérer l'adressage IP sous Linux](https://labex.io/fr/labs/comptia-manage-ip-addressing-in-linux-592736)** - Entraînez-vous à utiliser la commande `ip` pour configurer les paramètres réseau, puis vérifiez la connectivité et les chemins de routage avec `traceroute`.
2. **[Explorer l'interaction de la couche réseau avec ping et arp sous Linux](https://labex.io/fr/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Apprenez comment `ping` et `arp` fonctionnent ensemble pour comprendre les interactions de la couche réseau, qui sont des concepts fondamentaux pour le fonctionnement de `traceroute`.

Ces laboratoires vous aideront à appliquer les concepts de diagnostic réseau dans des scénarios réels et à renforcer votre confiance avec les outils réseau Linux essentiels.

## Quiz Question

Qu'est-ce qui est décrémenté de un lors des sauts à travers le réseau ? (Veuillez répondre en anglais, en faisant attention à la casse)

## Quiz Answer

TTL
