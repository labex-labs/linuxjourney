---
lesson_id: "ping"
course_id: "troubleshooting"
lang: "fr"
order_index: 2
title: "ping"
description: "Apprenez à lancer des tests ping bornés et à interpréter réponses, pertes, RTT, TTL et limites."
meta_title: "ping - Dépannage"
meta_description: "Utilisez ping sous Linux pour tester une connectivité et comprendre icmp_seq, TTL, pertes et temps aller-retour."
meta_keywords: "ping Linux, connectivité réseau, ICMP, TTL, icmp_seq, dépannage réseau"
---

`ping` envoie des requêtes ICMP Echo et rapporte les réponses observées. Il teste un chemin de messages de contrôle vers une adresse ; il ne prouve pas que TCP, UDP, DNS, l'authentification ou une application fonctionnent.

## Lancer un test borné

Sur les implémentations iputils courantes, envoyez trois requêtes IPv4 avec une attente de deux secondes par paquet :

```bash
$ ping -4 -c 3 -W 2 example.com
```

`-6` sélectionne IPv6. Notez l'adresse résolue, car un nom peut en renvoyer plusieurs et les exécutions successives en choisir des différentes.

:::single-choice{#ping-count-option}
Que demande `-c 3` ?

::option[Une charge utile de trois mégaoctets.]{#ping-three-megabytes explanation="La taille des paquets utilise une autre option."}
::option[Trois routes permanentes vers la destination.]{#ping-three-routes explanation="`ping` sonde le trafic et n'installe pas de route."}
::option[Trois requêtes Echo avant l'arrêt normal.]{#ping-three-requests .correct explanation="Un nombre fini rend le diagnostic borné et reproductible."}
:::

## Séquence et pertes

`icmp_seq` identifie les requêtes de l'exécution. Les réponses manquantes contribuent aux pertes observées ; les réponses désordonnées peuvent révéler des délais variables. Les petits échantillons sont bruyants : comparez plusieurs intervalles bornés et le taux d'erreur de l'application.

La perte peut survenir dans les deux sens, et la limitation d'ICMP peut la faire différer de celle de l'application.

:::single-choice{#ping-sequence-gap}
Que peut indiquer l'absence d'une réponse `icmp_seq` ?

::option[Que la destination a définitivement changé d'adresse MAC.]{#ping-sequence-mac explanation="Une lacune de séquence ne permet pas cette conclusion de liaison."}
::option[Que la requête ou la réponse a été perdue, filtrée, retardée au-delà de l'attente ou limitée.]{#ping-sequence-possibilities .correct explanation="La lacune indique une réponse non observée, mais ni le sens ni la cause exacte."}
::option[Que le disque source n'a plus d'inodes.]{#ping-sequence-inodes explanation="Les inodes du système de fichiers sont sans rapport avec ICMP."}
:::

## Temps aller-retour

Le champ `time` mesure en millisecondes l'intervalle entre l'envoi et la réception de la réponse. Il combine délai aller, traitement distant et délai retour. Sans horloges synchronisées aux extrémités, il ne donne pas la latence dans un seul sens.

:::single-choice{#ping-rtt-meaning}
Que mesure `time=23.7 ms` ?

::option[Uniquement la latence du trajet aller.]{#ping-outbound-only explanation="`ping` mesure l'intervalle complet requête-réponse."}
::option[La durée de fonctionnement du système cible.]{#ping-target-uptime explanation="Cette valeur chronomètre la sonde, pas le temps depuis le démarrage."}
::option[Le temps aller-retour de cet écho.]{#ping-round-trip .correct explanation="Il inclut les deux sens et le traitement de l'extrémité."}
:::

## TTL ou limite de sauts

Le TTL IPv4 ou Hop Limit IPv6 affiché est la valeur restante dans la réponse reçue. Sans connaître la valeur initiale et la route retour, sa soustraction ne donne pas un nombre exact de sauts. Un changement peut venir d'un autre répondant, d'une autre valeur initiale ou d'un autre retour.

:::single-choice{#ping-received-ttl}
Qu'est-ce que le TTL affiché sur un Echo Reply IPv4 ?

::option[La valeur restante lorsque la réponse atteint l'hôte local.]{#ping-remaining-ttl .correct explanation="Chaque routeur du trajet retour a décrémenté la valeur initiale de l'expéditeur."}
::option[Le nombre exact de routeurs dans les deux sens.]{#ping-exact-hop-count explanation="Le champ seul n'établit ni TTL initial ni chemin dans chaque sens."}
::option[La durée de cache de l'enregistrement DNS.]{#ping-dns-ttl explanation="Le TTL DNS et celui d'un paquet IP sont distincts."}
:::

## Tester la bonne couche

Si `ping` réussit mais que le service échoue, testez le port, TLS, le protocole et la requête réels. Si `ping` échoue, examinez la résolution, `ip route get`, les voisins, le pare-feu et les captures avant de déclarer l'hôte arrêté.

:::single-choice{#ping-success-limit}
Qu'est-ce qu'un `ping` réussi ne prouve pas ?

::option[Qu'un chemin ICMP de requête et réponse a fonctionné.]{#ping-icmp-worked explanation="C'est précisément la preuve fournie par les réponses."}
::option[Que la réponse contenait un numéro de séquence.]{#ping-sequence-present explanation="La sortie normale indique directement cette séquence."}
::option[Que l'application visée accepte et termine les requêtes.]{#ping-app-not-proven .correct explanation="Le transport et l'application exigent un test adapté."}
:::

## Résumé

Vous savez utiliser `ping` comme une mesure ICMP bornée et explicitement limitée.

1. Choisir la famille d'adresses et noter l'adresse résolue.
2. Borner le nombre et l'attente.
3. Interpréter la perte sans supposer son sens ou sa cause.
4. Traiter le RTT comme aller-retour et le TTL comme une valeur restante.
5. Tester séparément l'application réelle.
