---
lesson_id: "tcp-ip-model"
course_id: "network-basics"
lang: "fr"
order_index: 3
title: "Modèle TCP/IP"
description: "Découvrez comment les couches application, transport, Internet et liaison coopèrent dans le modèle TCP/IP."
meta_title: "Modèle TCP/IP - Réseaux"
meta_description: "Explorez les couches fondamentales du modèle TCP/IP : application, transport, Internet et liaison, ainsi que leur coopération."
meta_keywords: "modèle TCP/IP, couches TCP IP, réseau TCP/IP, TCP, IP, couches réseau, réseau Linux"
---

Le modèle TCP/IP organise en couches fonctionnelles les protocoles employés par les hôtes Internet. Une forme courante à quatre couches comprend Application, Transport, Internet et Liaison. Certains modèles pédagogiques séparent le support physique de la couche liaison et présentent donc cinq couches.

## Couche application

Les protocoles applicatifs définissent les messages et comportements de services comme HTTP, DNS, SSH et SMTP. Cette couche comprend également de nombreuses responsabilités de représentation et de session que le modèle OSI décrit séparément.

:::single-choice{#tcpip-http-layer} Dans quelle couche TCP/IP classe-t-on normalement HTTP ?

::option[Internet.]{#tcpip-http-internet explanation="La couche Internet traite l'adressage IP et la transmission des paquets."}
::option[Liaison.]{#tcpip-http-link explanation="La couche liaison transporte le trafic sur un support local."}
::option[Application.]{#tcpip-http-application .correct explanation="HTTP définit la sémantique des requêtes et réponses applicatives."}
:::

## Couche transport

Les protocoles de transport fournissent la communication entre les terminaux applicatifs. TCP offre un flux d'octets fiable et ordonné avec contrôle de congestion et de flux. UDP fournit des datagrammes indépendants sans les garanties de connexion, d'ordre ou de retransmission de TCP. Les numéros de ports aident à identifier les terminaux de transport, mais un port seul ne prouve pas l'application à l'écoute.

:::single-choice{#tcpip-udp-property} Quelle propriété appartient à UDP plutôt qu'à TCP ?

::option[Des datagrammes indépendants sans garantie intégrée de retransmission.]{#tcpip-udp-datagrams .correct explanation="Les applications qui emploient UDP choisissent si elles ajoutent une fiabilité et de quelle manière."}
::option[La livraison garantie et ordonnée d'un flux d'octets unique.]{#tcpip-udp-ordered explanation="Il s'agit d'une propriété du service TCP, sous réserve d'une connexion réussie."}
::option[Le routage des paquets entre différents réseaux IP.]{#tcpip-udp-routing explanation="Le routage entre réseaux est une fonction de la couche Internet."}
:::

## Couche Internet

Internet Protocol transporte des paquets avec des adresses IP source et destination. Les routeurs examinent les informations de routage et diminuent la limite de sauts en transmettant les paquets vers leur destination. ICMP communique les informations de contrôle et d'erreur nécessaires au fonctionnement d'IP. La livraison reste au mieux ; les couches supérieures ou les applications prennent en charge toute récupération nécessaire.

:::single-choice{#tcpip-router-layer} Quelle couche fournit l'adresse IP de destination employée par les routeurs ?

::option[Internet.]{#tcpip-router-internet .correct explanation="L'en-tête IP contient la destination de la couche réseau employée pour la transmission routée."}
::option[Application.]{#tcpip-router-application explanation="Les messages applicatifs sont transportés dans les données des protocoles inférieurs."}
::option[Liaison.]{#tcpip-router-link explanation="Les adresses de liaison sélectionnent la destination de la trame au prochain saut local."}
:::

## Couche liaison et encapsulation

La couche liaison envoie un paquet IP sur une liaison locale au moyen d'Ethernet, du Wi-Fi, d'un protocole point à point ou d'une autre technologie. Lorsque les données applicatives descendent dans la pile, chaque couche ajoute les informations nécessaires à sa portée. Chez le destinataire, les couches valident et retirent leur encapsulation avant de livrer les données vers le haut.

Les en-têtes de liaison changent normalement à chaque saut routé ; les conversations de transport et d'application sont de bout en bout, sauf si un équipement intermédiaire les termine ou les transforme.

:::single-choice{#tcpip-link-scope} Quelle est la portée normale d'une trame de la couche liaison ?

::option[Une liaison ou un saut local.]{#tcpip-one-link .correct explanation="Un routeur retire l'encapsulation entrante et en crée une nouvelle pour la liaison suivante."}
::option[Chaque session applicative de tout Internet.]{#tcpip-global-frame explanation="Les trames ne restent pas inchangées à travers les réseaux routés."}
::option[Uniquement la mémoire du processus source.]{#tcpip-process-memory explanation="Les trames sont transmises sur une liaison réseau."}
:::

## Résumé

Vous savez maintenant situer les fonctions Internet courantes dans le modèle TCP/IP.

1. Associer les protocoles de services à la couche application.
2. Distinguer les flux TCP des datagrammes UDP.
3. Placer l'adressage IP et le routage dans la couche Internet.
4. Considérer l'encapsulation de liaison comme propre au saut local.
