---
lesson_id: "arp-command"
course_id: "network-config"
lang: "fr"
order_index: 5
title: "arp"
description: "Découvrez comment examiner et interpréter l’état du cache ARP d’IPv4 et du cache de voisins d’IPv6 sous Linux."
meta_title: "arp - Configuration réseau"
meta_description: "Découvrez la commande ARP sous Linux, le cache de voisins, ip neighbor show et le rôle d’ARP dans les communications réseau."
meta_keywords: "ARP Linux, cache ARP, ip neighbour show, commandes réseau, réseau Linux, Linux débutant, tutoriel Linux"
---

Linux enregistre les adresses de liaison des prochains sauts récemment résolues dans la table des voisins. Pour IPv4 sur Ethernet, les entrées sont apprises par ARP ; IPv6 emploie la découverte de voisins. L’ancienne commande `arp` ne montre qu’une partie de cet état, tandis que `ip neighbor` prend en charge les deux familles.

## Afficher les entrées de voisins

Examinez toutes les entrées ou celles d’une seule interface :

```bash
$ ip neighbor show
$ ip neighbor show dev enp1s0
```

Une entrée contient une adresse IP, une adresse de couche liaison, un périphérique et un état d’accessibilité. La table peut être vide après le démarrage, puis se remplir lorsque le trafic nécessite des prochains sauts locaux.

:::single-choice{#arp-command-modern-view} Quelle commande affiche l’état moderne de la table des voisins sous Linux ?

::option[`pwd neighbor`]{#arp-command-pwd explanation="Pwd indique le répertoire de travail du shell."}
::option[`ip neighbor show`]{#arp-command-ip-neighbor .correct explanation="Elle affiche à la fois les entrées IPv4 dérivées d’ARP et les entrées de découverte de voisins IPv6."}
::option[`route --passwords`]{#arp-command-route-passwords explanation="Aucune commande d’examen des routes de ce type ne doit exposer d’identifiants secrets."}
:::

## Résoudre un voisin IPv4

Lorsqu’une association IPv4 sur la liaison est absente, l’hôte diffuse une requête ARP pour demander qui possède l’adresse cible. La cible, ou un routeur configuré explicitement comme proxy ARP, répond. L’émetteur met l’association en cache et transmet la trame en attente.

Pour une destination IP distante, l’hôte résout l’adresse de la passerelle sélectionnée plutôt que l’adresse MAC de l’hôte distant.

:::single-choice{#arp-command-remote-target} Quel voisin IPv4 un hôte résout-il pour une destination hors liaison ?

::option[Le serveur distant final au-delà de tous les routeurs.]{#arp-command-final-server explanation="Son adresse MAC n’a aucune signification sur la liaison source."}
::option[Chaque serveur DNS indiqué dans la configuration du résolveur.]{#arp-command-all-dns explanation="La résolution des voisins suit la route sélectionnée, et non la liste des résolveurs."}
::option[La passerelle sélectionnée sur la liaison locale.]{#arp-command-gateway .correct explanation="La trame Ethernet locale est adressée au routeur qui achemine le paquet IP."}
:::

## Interpréter les états

Les états courants comprennent `REACHABLE`, `STALE`, `DELAY`, `PROBE`, `INCOMPLETE` et `FAILED`. `STALE` signifie que la confirmation récente de l’accessibilité a expiré ; l’adresse en cache peut encore être utilisée pendant que la pile effectue des sondes si nécessaire. `FAILED` indique l’échec de la résolution ou de la détection d’accessibilité, mais la cause peut provenir de la liaison, du VLAN, de l’adresse, de la route, du filtrage ou de l’arrêt du pair.

:::single-choice{#arp-command-stale-state} L’état `STALE` signifie-t-il que le voisin est réputé inaccessible ?

::option[Non ; il manque une confirmation récente et le voisin peut être sondé lors de son utilisation.]{#arp-command-stale-probe .correct explanation="Cet état n’équivaut pas à `FAILED`."}
::option[Oui, et l’entrée ne pourra plus jamais être utilisée.]{#arp-command-stale-dead explanation="Les entrées périmées restent utilisables et peuvent changer d’état après un contrôle d’accessibilité."}
::option[Oui, parce que son enregistrement DNS a expiré.]{#arp-command-stale-dns explanation="L’état des voisins et le cache DNS sont distincts."}
:::

## Modifier prudemment l’état des voisins

Les entrées statiques et le vidage du cache modifient l’état ; ils peuvent perturber le trafic actif ou masquer les indices d’origine. Relevez d’abord les routes actuelles, les compteurs de paquets et l’état des voisins. Préférez une sonde ciblée et une capture de paquets sur un réseau de test autorisé avant de vider une interface entière.

ARP ne possède aucun mécanisme d’authentification intégré : des adresses en double ou des réponses usurpées peuvent empoisonner les associations. Les protections des commutateurs, la segmentation, la surveillance et l’authentification des couches supérieures contribuent à réduire les conséquences.

:::single-choice{#arp-command-flush-first} Pourquoi éviter de vider toute la table des voisins comme première étape du diagnostic ?

::option[Les entrées de voisins sont enregistrées uniquement dans les serveurs racine DNS.]{#arp-command-neighbors-dns explanation="Elles sont gérées par la pile réseau locale."}
::option[Un vidage supprime définitivement le matériel de l’interface.]{#arp-command-flush-hardware explanation="Il supprime les entrées du cache, et non les périphériques physiques."}
::option[Il modifie les indices et peut interrompre des prochains sauts qui fonctionnaient.]{#arp-command-flush-disrupts .correct explanation="L’examen en lecture seule et les tests ciblés préservent l’état nécessaire au diagnostic de la cause."}
:::

## Résumé

Vous savez maintenant examiner la résolution des voisins sans considérer chaque état du cache comme une panne.

1. Utiliser `ip neighbor` pour l’état IPv4 et IPv6.
2. Résoudre la destination uniquement lorsqu’elle se trouve sur la liaison locale.
3. Résoudre une passerelle pour le trafic IP hors liaison.
4. Préserver les indices du cache avant toute modification ciblée de l’état.
