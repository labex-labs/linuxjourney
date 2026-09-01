---
lesson_id: "link-layer"
course_id: "network-basics"
lang: "fr"
order_index: 8
title: "Couche liaison"
description: "Découvrez comment les trames Ethernet, la découverte des voisins, les commutateurs et les routeurs livrent les paquets sur une liaison locale."
meta_title: "Couche liaison - Notions de base sur les réseaux"
meta_description: "Explorez les principes de la couche liaison TCP/IP : trames Ethernet, résolution ARP, adresses MAC, commutation et parcours des paquets sur un réseau local."
meta_keywords: "couche liaison, en-tête liaison, ARP, TCP/IP, adresse MAC, notions de réseau, réseau Linux, parcours des paquets, protocole de résolution d’adresses"
---

La couche liaison transporte les paquets de la couche réseau sur un support local ou une liaison virtuelle. Ethernet et le Wi-Fi emploient des méthodes de mise en trame différentes, mais assurent tous deux la livraison locale sous IP.

## Trames Ethernet

Une trame Ethernet contient les adresses MAC de destination et source, un champ EtherType ou de longueur, une charge utile et une séquence de contrôle de trame en fin de trame. La transmission physique utilise également un préambule et un délimiteur de début. La séquence de contrôle détecte les altérations sur la liaison ; elle ne répare pas une trame endommagée et ne la protège pas par cryptographie.

:::single-choice{#link-layer-fcs-purpose} À quoi sert la séquence de contrôle d’une trame Ethernet ?

::option[À détecter l’altération d’une trame sur la liaison.]{#link-layer-detect-corruption .correct explanation="Un récepteur peut abandonner une trame qui échoue au contrôle d’intégrité."}
::option[À chiffrer la charge utile sur tous les sauts routés.]{#link-layer-fcs-encryption explanation="La FCS est un code de détection d’erreurs, et non un mécanisme de chiffrement ou d’authentification."}
::option[À sélectionner une application grâce au port TCP.]{#link-layer-fcs-port explanation="Les ports de transport sont acheminés dans la charge utile IP."}
:::

## Commutateurs et livraison locale

Un commutateur Ethernet apprend sur quels ports apparaissent les adresses MAC source et achemine les trames unicast connues vers le port associé à leur destination. Les diffusions et certains trafics dont la destination est inconnue sont propagés dans le domaine de diffusion. Les VLAN peuvent diviser un même système de commutation en domaines de liaison logiques distincts.

:::single-choice{#link-layer-switch-learning} Quelles informations un commutateur Ethernet apprend-il normalement à partir des trames ?

::option[Les mots de passe applicatifs et les cookies HTTP.]{#link-layer-switch-passwords explanation="Une table d’acheminement élémentaire emploie des adresses de liaison, et non des identifiants applicatifs."}
::option[La table de routage Internet complète de chaque routeur.]{#link-layer-switch-routing-table explanation="La commutation de couche 2 et l’échange de routes globales sont des fonctions différentes."}
::option[Les adresses MAC source associées aux ports du commutateur.]{#link-layer-switch-source .correct explanation="Cet apprentissage construit la table utilisée ensuite pour acheminer les trafics unicast connus."}
:::

## Résoudre l’adresse du prochain saut

Pour IPv4 sur Ethernet, le protocole ARP associe l’adresse IPv4 d’un prochain saut situé sur la liaison à une adresse MAC. L’hôte consulte d’abord son cache de voisins. Si nécessaire, il diffuse une requête ARP, à laquelle répond le propriétaire de l’adresse ou un proxy autorisé.

Pour une destination IP hors liaison, l’hôte résout l’adresse MAC de la passerelle par défaut ou sélectionnée, et non celle de la destination distante. IPv6 emploie la découverte de voisins sur ICMPv6 plutôt qu’ARP.

:::single-choice{#link-layer-remote-destination-mac} Quelle adresse MAC un hôte utilise-t-il pour une destination IPv4 hors liaison ?

::option[L’adresse MAC du routeur choisi comme prochain saut.]{#link-layer-gateway-mac .correct explanation="Le paquet IP reste adressé à l’hôte distant tandis que la trame locale est envoyée au routeur."}
::option[L’adresse MAC du serveur distant à travers tous les routeurs.]{#link-layer-remote-mac explanation="Les adresses MAC identifient les interfaces sur une liaison locale et ne sont pas transportées de bout en bout."}
::option[Une adresse MAC dérivée du port TCP de destination.]{#link-layer-port-mac explanation="Les ports de transport ne déterminent pas les adresses de liaison."}
:::

## Examiner l’état des voisins

Affichez les entrées ARP d’IPv4 et celles de la découverte de voisins d’IPv6 avec :

```bash
$ ip neighbor show
```

Les états tels que `REACHABLE`, `STALE`, `DELAY`, `PROBE` et `FAILED` décrivent le processus de détection d’inaccessibilité des voisins. `STALE` ne signifie pas que la communication est interrompue ; il indique que la confirmation d’accessibilité mise en cache n’est plus récente et peut être vérifiée lors d’une utilisation.

:::single-choice{#link-layer-stale-neighbor} Qu’indique l’état `STALE` d’une entrée de voisin ?

::option[Que le voisin est définitivement bloqué par le pare-feu.]{#link-layer-stale-blocked explanation="Cet état ne décrit pas la politique du pare-feu."}
::option[Que l’adresse MAC a été enregistrée sur disque comme sauvegarde.]{#link-layer-stale-backup explanation="L’état d’un voisin est une information opérationnelle du cache."}
::option[Que l’association mise en cache ne possède pas de confirmation d’accessibilité récente.]{#link-layer-stale-confirmation .correct explanation="La pile peut encore l’utiliser et effectuer une détection d’accessibilité si nécessaire."}
:::

## Encapsulation lors du passage par un routeur

L’émetteur place un paquet IP dans une trame adressée à son prochain saut. Le routeur valide et retire la trame entrante, traite l’en-tête IP, choisit une route de sortie et construit une nouvelle trame pour cette liaison. Le destinataire retire les encapsulations dans l’ordre inverse et livre la charge utile de transport au socket approprié.

:::single-choice{#link-layer-router-reframing} Qu’est-ce qui reste inchangé lors d’un acheminement ordinaire, tandis que la trame Ethernet change au niveau d’un routeur ?

::option[La destination IP, sauf si un équipement intermédiaire tel qu’un dispositif NAT la modifie.]{#link-layer-ip-destination .correct explanation="Les routeurs ordinaires acheminent le trafic vers la destination IP finale tout en remplaçant les trames propres à chaque saut."}
::option[La séquence de contrôle de la trame entrante.]{#link-layer-same-fcs explanation="Une nouvelle trame sortante reçoit sa propre valeur d’intégrité de liaison."}
::option[L’adresse MAC de destination sur chaque liaison.]{#link-layer-same-mac explanation="Chaque liaison emploie l’adresse de liaison appropriée au prochain saut."}
:::

## Résumé

Vous savez maintenant suivre un paquet IP pendant une étape de livraison sur une liaison locale.

1. Identifier les principaux champs d’une trame Ethernet et sa séquence de contrôle d’intégrité.
2. Expliquer comment un commutateur apprend les emplacements d’acheminement locaux.
3. Résoudre un prochain saut IPv4 avec ARP et un voisin IPv6 avec NDP.
4. Interpréter l’état du cache de voisins sans conclure trop vite à une panne.
5. Reconnaître que les routeurs reconstruisent les trames pour chaque liaison sortante.
