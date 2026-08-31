---
lesson_id: "path-of-a-packet"
course_id: "routing"
lang: "fr"
order_index: 3
title: "Parcours d’un paquet"
description: "Découvrez comment les routes, la découverte des voisins, les trames et les routeurs transportent un paquet IP sur un chemin."
meta_title: "Parcours d’un paquet - Routage"
meta_description: "Explorez le parcours complet d’un paquet sur un réseau local et Internet avec les adresses IP et MAC, ARP et les tables de routage."
meta_keywords: "parcours paquet, communication réseau, ARP, adresse IP, adresse MAC, table routage, passerelle défaut, réseau Linux"
---

Le parcours d’un paquet est une succession de décisions locales. L’hôte source, chaque routeur et la destination appliquent leur propre état de routage, de voisins, de filtrage et de protocole ; aucun terminal ne connaît normalement à l’avance chaque décision interne.

## Envoyer vers une destination sur la liaison

Pour une destination couverte par une route connectée, la source choisit une interface et une adresse IP source. Elle résout ensuite l’adresse de liaison de la destination — avec ARP pour IPv4 sur Ethernet ou la découverte de voisins pour IPv6 — et envoie une trame qui transporte le paquet IP. Un commutateur peut acheminer la trame sans devenir un saut IP.

:::single-choice{#packet-path-switch-hop}
Un commutateur Ethernet ordinaire compte-t-il comme saut de routage IP ?

::option[Non ; il achemine les trames locales sans décrémenter le champ de sauts IP.]{#packet-path-switch-not-hop .correct explanation="Un saut routé se produit lorsqu’un routeur traite et achemine le paquet IP."}
::option[Oui ; chaque commutateur remplace la destination IP.]{#packet-path-switch-replaces-ip explanation="L’acheminement de couche 2 ne réécrit normalement pas les destinations IP."}
::option[Oui ; chaque connecteur de câble constitue également un saut IP.]{#packet-path-cable-hop explanation="Les composants physiques n’effectuent pas de routage IP."}
:::

## Envoyer par une passerelle

Pour une destination hors liaison, la route sélectionnée identifie un routeur de prochain saut. La destination IP reste le terminal distant, tandis que la destination de la trame locale est l’adresse de liaison de la passerelle. Sur sa liaison locale, l’hôte résout la passerelle, et non le serveur distant.

:::single-choice{#packet-path-gateway-mac}
Quelle adresse MAC est utilisée dans la première trame Ethernet envoyée à un serveur hors liaison ?

::option[L’adresse du serveur distant à travers tous les réseaux intermédiaires.]{#packet-path-remote-mac explanation="L’adresse de liaison distante n’a aucune signification sur le réseau local source."}
::option[Une valeur calculée à partir du nom DNS du serveur.]{#packet-path-dns-mac explanation="Les noms DNS n’encodent pas l’adresse MAC du prochain saut local."}
::option[L’adresse de la passerelle locale sélectionnée.]{#packet-path-local-gateway .correct explanation="La trame est livrée au prochain saut tandis que l’en-tête IP vise le terminal final."}
:::

## Traitement par chaque routeur

Un routeur retire l’encapsulation de liaison entrante, valide et traite l’en-tête IP, décrémente le TTL ou la limite de sauts, recherche la destination, applique la politique et crée une nouvelle encapsulation pour la liaison de sortie. En IPv4, le traitement de la somme de contrôle de l’en-tête tient compte de la modification du TTL. Si le champ de sauts atteint zéro, le routeur abandonne le paquet et peut renvoyer un message ICMP de délai dépassé.

:::single-choice{#packet-path-router-change}
Quel champ IP est modifié par chaque saut routé normal ?

::option[Le nom d’utilisateur de l’application.]{#packet-path-username explanation="Les routeurs n’ont pas besoin des données des comptes applicatifs pour l’acheminement élémentaire."}
::option[Le TTL d’IPv4 ou la limite de sauts d’IPv6.]{#packet-path-hop-field .correct explanation="Chaque routeur décrémente ce champ afin de borner les boucles de routage."}
::option[Le port de transport de destination dans tous les cas.]{#packet-path-port explanation="Le routage ordinaire conserve les terminaux de transport ; le NAT constitue une transformation distincte."}
:::

## Tenir compte des équipements intermédiaires et de la MTU

Le routage ordinaire conserve les adresses IP source et destination, mais le NAT peut les réécrire et les tunnels encapsuler le paquet d’origine. Les pare-feu peuvent abandonner le trafic silencieusement ou le rejeter. Les MTU des liaisons diffèrent également ; les routeurs IPv4 peuvent parfois fragmenter les paquets, tandis que les routeurs IPv6 ne fragmentent pas les paquets acheminés et reposent sur la découverte de la MTU du chemin.

:::single-choice{#packet-path-address-change-exception}
Quand les adresses IP de bout en bout peuvent-elles changer sur un chemin ?

::option[Chaque fois qu’un commutateur Ethernet apprend une adresse MAC source.]{#packet-path-switch-learning-ip explanation="L’apprentissage du commutateur affecte une table d’acheminement de liaison, et non les adresses IP des terminaux."}
::option[Lorsqu’une politique NAT traduit les en-têtes du paquet.]{#packet-path-nat-change .correct explanation="La traduction est une fonction d’équipement intermédiaire qui dépasse le routage ordinaire."}
::option[Chaque fois qu’une entrée du cache DNS expire.]{#packet-path-dns-expiry explanation="Les paquets existants contiennent déjà des adresses numériques."}
:::

## Suivre le chemin du retour

La destination effectue sa propre recherche de route pour la réponse. Le retour peut emprunter d’autres routeurs en raison de la politique de routage, de l’équilibrage de charge ou de pannes. Les pare-feu avec état et le NAT doivent tenir compte du flux observé ; l’asymétrie peut donc avoir des conséquences opérationnelles même si IP l’autorise.

:::single-choice{#packet-path-return-symmetry}
Une réponse doit-elle traverser les mêmes routeurs dans l’ordre inverse ?

::option[Oui, car IP enregistre toute la route aller dans chaque paquet.]{#packet-path-records-route explanation="Les paquets IP ordinaires ne transportent pas obligatoirement une route inverse complète."}
::option[Oui, sauf si la source et la destination partagent un nom d’hôte.]{#packet-path-hostname-symmetry explanation="Les noms n’imposent pas la symétrie du chemin."}
::option[Non ; chaque sens est routé indépendamment.]{#packet-path-independent-return .correct explanation="Les politiques et la topologie peuvent produire un chemin asymétrique mais valide."}
:::

## Résumé

Vous savez maintenant suivre l’évolution de l’état de liaison autour d’un paquet IP routé.

1. Résoudre l’hôte final uniquement lorsqu’il se trouve sur la liaison.
2. Encapsuler le trafic hors liaison dans une trame adressée à la passerelle locale sélectionnée.
3. Suivre la recherche de route et le traitement de la limite de sauts à chaque routeur.
4. Tenir compte du NAT, du filtrage, des tunnels et des contraintes de MTU.
5. Considérer le sens du retour comme une route indépendante.
