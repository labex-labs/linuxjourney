---
lesson_id: "transport-layer"
course_id: "network-basics"
lang: "fr"
order_index: 6
title: "Couche transport"
description: "Découvrez comment TCP et UDP emploient les ports et offrent différentes sémantiques de livraison entre terminaux applicatifs."
meta_title: "Couche transport - Réseaux"
meta_description: "Explorez la couche transport sous Linux : TCP, UDP, ports réseau, segmentation, flux, datagrammes et poignée de main TCP."
meta_keywords: "couche transport Linux, TCP, UDP, poignée de main TCP, ports réseau, segmentation, protocoles réseau"
---

La couche transport relie les terminaux applicatifs à travers un réseau IP. TCP et UDP emploient tous deux des numéros de ports sur 16 bits, mais exposent aux applications des modèles de communication et garanties différents.

## Ports et sockets

Un port de destination aide le système d'exploitation à livrer le trafic à un socket en écoute. Une connexion ou un flux est identifié par plus d'un port : le protocole, les adresses source et destination ainsi que les ports source et destination comptent tous. Un même port de serveur peut donc prendre en charge de nombreux clients simultanés.

:::single-choice{#transport-layer-many-clients} Comment un seul port de serveur TCP peut-il gérer plusieurs clients en même temps ?

::option[Chaque connexion possède une combinaison distincte d'adresses et de ports de terminaux.]{#transport-layer-connection-tuple .correct explanation="Le tuple complet de transport distingue les connexions simultanées qui partagent un port d'écoute."}
::option[Le serveur renomme définitivement son port après chaque paquet.]{#transport-layer-renames-port explanation="Le port d'écoute peut rester stable tandis que les connexions acceptées possèdent des tuples de pairs distincts."}
::option[IP supprime toutes les adresses source avant la livraison.]{#transport-layer-removes-source explanation="Les adresses source participent à l'identification du pair et du trajet."}
:::

## Flux d'octets TCP

TCP fournit un flux d'octets ordonné et fiable tant que la connexion reste viable. Il emploie des numéros de séquence, accusés de réception, retransmissions et contrôles de flux et de congestion. TCP ne préserve pas les limites des messages applicatifs : une écriture peut arriver par plusieurs lectures, ou plusieurs écritures être renvoyées par une seule lecture. Les applications définissent leur propre encadrement.

La fiabilité ne signifie pas une livraison absolue. Une connexion peut expirer, être réinitialisée ou échouer, et un accusé de réception ne prouve pas que l'application a durablement validé les données.

:::single-choice{#transport-layer-tcp-boundaries} Que deviennent les limites des messages applicatifs dans TCP ?

::option[TCP expose un flux d'octets ordonné sans préserver les limites des écritures.]{#transport-layer-byte-stream .correct explanation="Le protocole applicatif doit définir la délimitation ou la taille de ses messages."}
::option[Chaque écriture devient exactement un paquet IP et une lecture.]{#transport-layer-one-write-packet explanation="La segmentation, la mise en tampon et les API de réception ne préservent pas cette correspondance."}
::option[TCP convertit chaque message en enregistrement DNS.]{#transport-layer-tcp-dns explanation="DNS est un protocole applicatif distinct."}
:::

## La poignée de main TCP

Une connexion TCP normale commence par une poignée de main en trois étapes :

1. L'initiateur envoie `SYN` avec ses informations de séquence initiales.
2. Le processus en écoute répond `SYN-ACK` avec ses propres informations de séquence et son accusé de réception.
3. L'initiateur renvoie `ACK`.

Cet échange établit l'état du transport dans les deux terminaux. Il n'authentifie pas le serveur applicatif et ne prouve pas que l'opération applicative demandée réussira.

:::single-choice{#transport-layer-handshake-order} Quel est l'ordre normal de la poignée de main TCP en trois étapes ?

::option[SYN, SYN-ACK, ACK.]{#transport-layer-syn-order .correct explanation="L'échange synchronise et accuse réception de l'état initial de la connexion dans les deux directions."}
::option[ACK, ACK, SYN.]{#transport-layer-ack-ack-syn explanation="L'initiateur demande d'abord la synchronisation."}
::option[SYN, FIN, RST.]{#transport-layer-syn-fin-rst explanation="FIN et RST ferment ou abandonnent l'état plutôt que d'établir une connexion normale."}
:::

## Datagrammes UDP

UDP préserve les limites des datagrammes et fournit une détection des erreurs par somme de contrôle, mais n'offre pas l'état de connexion, l'ordre, la retransmission ni les contrôles de flux et de congestion de TCP. Une application peut ajouter elle-même la fiabilité ou le comportement de congestion dont elle a besoin. UDP n'est pas automatiquement plus rapide : les performances dépendent de la conception du protocole, de la charge, du trajet et de l'implémentation.

:::single-choice{#transport-layer-udp-boundaries} Quelle propriété UDP fournit-il aux applications ?

::option[Un flux d'octets ordonné automatiquement retransmis.]{#transport-layer-udp-stream explanation="Cela décrit des services comparables à TCP, pas UDP de base."}
::option[La préservation des limites entre les datagrammes soumis.]{#transport-layer-udp-datagrams .correct explanation="Un datagramme UDP reçu correspond à un datagramme envoyé, sauf s'il est perdu."}
::option[La livraison garantie avant une échéance fixe.]{#transport-layer-udp-deadline explanation="UDP ne garantit aucune échéance de livraison."}
:::

## Examiner les terminaux de transport

Employez `ss` pour examiner les sockets en écoute et connectés sans les modifier :

```bash
$ ss -lntup
$ ss -tn state established
```

Les détails des processus peuvent exiger des privilèges. Un socket en écoute prouve seulement la disponibilité locale à la frontière du transport ; le pare-feu, le routage, la famille d'adresses, TLS et la santé applicative exigent encore des tests adaptés.

:::single-choice{#transport-layer-listener-proof} Qu'établit un socket TCP en écoute ?

::option[Que chaque pare-feu distant autorise la connexion.]{#transport-layer-all-firewalls explanation="L'état du socket local ne révèle pas toutes les règles du trajet."}
::option[Que l'application a réussi chacun de ses contrôles de santé.]{#transport-layer-all-health explanation="L'écoute constitue une preuve plus faible qu'une transaction applicative réussie."}
::option[Qu'un processus local est prêt à accepter les connexions TCP correspondantes.]{#transport-layer-local-listener .correct explanation="L'accessibilité distante et les bonnes réponses applicatives restent des questions distinctes."}
:::

## Résumé

Vous savez maintenant distinguer le comportement des flux TCP de celui des datagrammes UDP.

1. Identifier un flux par le protocole, les adresses et les ports.
2. Considérer TCP comme un flux d'octets fiable et ordonné sans limites de messages.
3. Reconnaître ce que la poignée de main TCP prouve et ne prouve pas.
4. Considérer la fiabilité et la congestion d'UDP comme des choix de conception applicatifs.
5. Vérifier la santé applicative au-delà de l'état du socket local.
