---
lesson_id: "network-layer"
course_id: "network-basics"
lang: "fr"
order_index: 7
title: "Couche réseau"
description: "Découvrez comment l’adressage IP, les préfixes, les tables de routage et les limites de sauts acheminent les paquets entre les réseaux."
meta_title: "Couche réseau - Notions de base sur les réseaux"
meta_description: "Explorez la couche réseau sous Linux : adresses IP, sous-réseaux, tables de routage, acheminement des paquets et limites de sauts."
meta_keywords: "couche réseau, adresses IP, sous-réseaux, réseau Linux, routage de paquets, transmission de données, modèle OSI, paquet IP"
---

La couche réseau fournit un adressage logique et une livraison des paquets au mieux entre des réseaux interconnectés. Dans la suite de protocoles Internet, IPv4 et IPv6 transportent les paquets tandis que les routeurs choisissent le prochain saut vers chaque destination.

## Paquets IP

Un en-tête IP contient les adresses source et destination ainsi que les champs nécessaires à l’acheminement et au traitement du protocole. La charge utile contient généralement un segment TCP, un datagramme UDP ou un message ICMP. IP ne garantit ni l’arrivée, ni l’ordre, ni l’absence de doublons.

:::single-choice{#network-layer-ip-service} Quel service de livraison IP fournit-il à lui seul ?

::option[La validation garantie des transactions applicatives.]{#network-layer-guaranteed-commit explanation="Le résultat d’une livraison IP ne peut pas prouver la persistance des données dans l’application."}
::option[La livraison des paquets au mieux.]{#network-layer-best-effort .correct explanation="Les couches supérieures ou les applications ajoutent les mécanismes de récupération ou de remise en ordre nécessaires."}
::option[La réservation permanente d’un câble physique unique.]{#network-layer-cable-reservation explanation="L’acheminement par paquets ne réserve pas de chemin physique dédié."}
:::

## Préfixes et sous-réseaux

Une adresse et une longueur de préfixe définissent les bits initiaux qui forment un préfixe réseau. Les hôtes utilisent ces informations et leurs routes pour déterminer si une destination se trouve sur la liaison locale ou nécessite un routeur de prochain saut. Un sous-réseau est une plage d’adresses régie par un préfixe et une politique ; les sous-réseaux ne sont pas automatiquement connectés à tous les autres sous-réseaux.

:::single-choice{#network-layer-prefix-decision} Qu’est-ce qui aide un hôte à déterminer si une destination IPv4 se trouve sur la liaison locale ?

::option[Le mot de passe applicatif de la destination.]{#network-layer-password explanation="Les données d’authentification ne définissent pas les préfixes réseau."}
::option[La couleur du câble Ethernet.]{#network-layer-cable-color explanation="L’apparence d’un câble n’a aucune signification pour l’adressage."}
::option[Ses préfixes configurés et sa table de routage.]{#network-layer-prefix-routes .correct explanation="L’hôte compare les destinations aux routes, y compris aux préfixes directement connectés."}
:::

## Décisions de routage

Linux consulte les règles et les tables de routage afin de choisir une interface de sortie, un prochain saut et les informations de source privilégiées. Parmi les routes admissibles, celle dont le préfixe correspondant est le plus spécifique est normalement privilégiée. Examinez la décision réelle pour une destination avec :

```bash
$ ip route get 203.0.113.10
```

Il s’agit d’une recherche de route locale, et non d’une preuve que chaque routeur en aval possède une route fonctionnelle ou que la destination accepte le trafic.

:::single-choice{#network-layer-longest-prefix} Quelle route l’emporte normalement parmi les routes admissibles vers une même destination ?

::option[La route dont le nom d’interface arrive en premier dans l’ordre alphabétique.]{#network-layer-alphabetical explanation="L’orthographe du nom de l’interface ne constitue pas la règle de sélection."}
::option[La route la plus ancienne, quel que soit son préfixe.]{#network-layer-oldest explanation="L’ancienneté seule ne l’emporte pas sur la correspondance des préfixes."}
::option[La route dont le préfixe correspondant est le plus spécifique.]{#network-layer-most-specific .correct explanation="La correspondance au préfixe le plus long choisit la route couvrant la plage d’adresses correspondante la plus étroite."}
:::

## Limites de sauts et modifications lors de l’acheminement

Chaque paquet IPv4 possède un TTL, et chaque paquet IPv6 une limite de sauts. Un routeur décrémente cette valeur ; lorsqu’elle atteint zéro, il abandonne le paquet et peut envoyer une erreur ICMP. Ce mécanisme empêche les boucles de routage de faire circuler les paquets indéfiniment.

Les routeurs conservent normalement les adresses IP de bout en bout, mais le NAT, les tunnels, les proxys et d’autres équipements intermédiaires peuvent transformer ou encapsuler les paquets. Les en-têtes de la couche liaison changent à chaque saut routé dans tous les cas.

:::single-choice{#network-layer-hop-limit} Pourquoi le TTL ou la limite de sauts est-il décrémenté par les routeurs ?

::option[Pour augmenter les permissions de fichiers de l’application.]{#network-layer-hop-permissions explanation="Le nombre de sauts est sans rapport avec les autorisations du système de fichiers."}
::option[Pour convertir chaque paquet IPv4 en IPv6.]{#network-layer-hop-convert explanation="La traduction de protocole n’est pas la fonction de ce champ."}
::option[Pour empêcher les paquets de circuler indéfiniment en boucle.]{#network-layer-prevent-loop .correct explanation="Un nombre de sauts fini garantit qu’une boucle de routage persistante finira par provoquer l’abandon du paquet."}
:::

## Résumé

Vous savez maintenant expliquer comment un hôte IP choisit la prochaine étape vers une destination.

1. Considérer la livraison IP comme un service au mieux.
2. Utiliser les préfixes et les routes pour distinguer les destinations locales de celles qui nécessitent un routage.
3. Appliquer la correspondance au préfixe le plus long lors du choix d’une route.
4. Reconnaître comment les limites de sauts bornent les boucles d’acheminement.
