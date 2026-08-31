---
lesson_id: "icmp"
course_id: "troubleshooting"
lang: "fr"
order_index: 1
title: "ICMP"
description: "Découvrez comment ICMP signale les erreurs IP, facilite le diagnostic et assure des fonctions essentielles en IPv4 et IPv6."
meta_title: "ICMP - Dépannage"
meta_description: "Comprenez le protocole ICMP, ses types et ses codes pour diagnostiquer efficacement les réseaux Linux."
meta_keywords: "ICMP, protocole ICMP, dépannage réseau, types ICMP, réseau Linux"
---

Internet Control Message Protocol transporte des informations de contrôle, d'erreur et de diagnostic parallèlement à IP. ICMP pour IPv4 et ICMPv6 sont des protocoles apparentés mais distincts, avec des numéros de type et des responsabilités différents.

## Types, codes et sommes de contrôle

Un message ICMP possède un type, éventuellement un code plus précis, et une somme de contrôle. Les erreurs incluent normalement une partie du paquet déclencheur afin que l'expéditeur les associe à un flux.

:::single-choice{#icmp-code-purpose}
Que fournit un code ICMP ?

::option[Un nom DNS permanent pour le routeur déclarant.]{#icmp-code-dns explanation="La résolution de noms n'est pas la fonction de ce champ."}
::option[Une signification plus précise au sein d'un type de message ICMP.]{#icmp-code-specific .correct explanation="Les codes Destination Unreachable distinguent par exemple plusieurs causes d'échec."}
::option[La charge utile complète de tous les paquets précédents.]{#icmp-code-all-payload explanation="Une erreur ne cite que la part du paquet déclencheur requise pour l'identifier."}
:::

## Messages d'écho et d'erreur

Pour ICMPv4, Echo Request est le type 8, Echo Reply le type 0, Destination Unreachable le type 3 et Time Exceeded le type 11. ICMPv6 emploie d'autres numéros : identifiez toujours la famille d'adresses avant d'interpréter une capture.

:::single-choice{#icmpv4-echo-request-type}
Quel est le type ICMPv4 Echo Request ?

::option[0]{#icmp-type-zero explanation="Le type zéro correspond à Echo Reply en ICMPv4."}
::option[11]{#icmp-type-eleven explanation="Le type onze correspond à Time Exceeded."}
::option[8]{#icmp-type-eight .correct explanation="`ping` envoie couramment ce message pour demander une réponse d'écho."}
:::

## MTU du chemin et ICMP essentiel

ICMP n'est pas seulement le trafic facultatif de `ping`. Les erreurs IPv4 signalant une fragmentation nécessaire et les messages ICMPv6 Packet Too Big servent à découvrir la MTU du chemin. ICMPv6 assure aussi Neighbor Discovery et les annonces de routeur. Tout bloquer peut donc créer des trous noirs et casser IPv6.

Filtrez selon le type nécessaire, le sens, le débit et la portée. Certains messages peuvent être usurpés ; validez le contexte cité avec les routes locales et les captures.

:::single-choice{#icmp-block-all-risk}
Pourquoi le blocage de tout ICMP peut-il casser un trafic valide ?

::option[Chaque réponse HTTP est transportée dans un Echo Reply.]{#icmp-http-echo explanation="HTTP utilise normalement TCP ou QUIC."}
::option[ICMP stocke tous les mots de passe applicatifs.]{#icmp-passwords explanation="ICMP n'est pas une base d'identifiants."}
::option[ICMP transporte des informations indispensables à la MTU du chemin et au contrôle IPv6.]{#icmp-essential-control .correct explanation="Les supprimer peut empêcher le dimensionnement des paquets ou la découverte des voisins et routeurs."}
:::

## Interpréter le silence

Une absence de réponse peut signifier filtrage, limitation de débit, routage asymétrique, absence de route retour, hôte arrêté ou refus de répondre. Inversement, une erreur ICMP peut provenir d'un équipement intermédiaire.

:::single-choice{#icmp-silence-meaning}
Que prouve à lui seul l'absence d'Echo Reply ?

::option[Que l'application cible est certainement arrêtée.]{#icmp-silence-app-down explanation="Le service peut fonctionner tandis que l'écho est filtré ou ignoré."}
::option[Que le nom de destination a été supprimé du DNS.]{#icmp-silence-dns-deleted explanation="Une sonde vers une adresse numérique peut rester muette indépendamment du DNS."}
::option[Seulement qu'aucune réponse observée n'a résulté de cet échange.]{#icmp-silence-limited .correct explanation="Il faut d'autres preuves sur les routes, le transport, l'application et les captures."}
:::

## Résumé

Vous savez désormais interpréter ICMP comme un indice de contrôle plutôt qu'un verdict binaire.

1. Lire le type et le code dans la bonne famille IP.
2. Reconnaître les rôles d'écho, d'inaccessibilité et de dépassement de temps.
3. Préserver les messages nécessaires à la MTU et à IPv6.
4. Corréler erreurs et silence avec d'autres observations du chemin.
