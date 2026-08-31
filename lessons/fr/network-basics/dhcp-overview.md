---
lesson_id: "dhcp-overview"
course_id: "network-basics"
lang: "fr"
order_index: 9
title: "Présentation de DHCP"
description: "Découvrez comment DHCPv4 loue des adresses et des options réseau par la découverte, la sélection et le renouvellement."
meta_title: "Présentation de DHCP - Notions de base sur les réseaux"
meta_description: "Découvrez les principes de DHCP : attribution d’adresses IP, échange DORA en quatre étapes, baux, renouvellement et rôle du protocole dans un réseau Linux."
meta_keywords: "DHCP, protocole de configuration dynamique des hôtes, couche DHCP, adresse IP, réseau Linux, processus DHCP, DORA, configuration réseau"
---

Le protocole DHCP fournit aux clients une configuration réseau sous forme de bail. Avec DHCPv4, celle-ci peut comprendre une adresse IPv4, un masque de sous-réseau, des routeurs par défaut, des serveurs DNS, une durée de bail et d’autres options choisies selon la politique locale.

## Clients, serveurs et relais

Un serveur DHCP gère des étendues ou des pools d’adresses ainsi que l’état des baux. Il n’a pas besoin de se trouver sur chaque segment physique : un relais DHCP peut transmettre les échanges entre les clients d’un sous-réseau et un serveur centralisé. Un réseau reposant uniquement sur une configuration statique peut ne proposer aucun service DHCP.

DHCP est un protocole de la couche application transporté par UDP. Les serveurs DHCPv4 utilisent normalement le port UDP 67 et les clients le port 68.

:::single-choice{#dhcp-relay-purpose}
Que permet un relais DHCP ?

::option[Que chaque client choisisse une adresse sans aucune politique.]{#dhcp-client-any-address explanation="Le serveur continue d’appliquer les règles relatives aux étendues et aux baux."}
::option[Que les clients d’un autre sous-réseau atteignent un serveur DHCP centralisé.]{#dhcp-central-server .correct explanation="Le relais transmet les échanges DHCP au-delà d’une frontière de routage et identifie le réseau du client."}
::option[Que les commutateurs Ethernet remplacent tous les routeurs IP.]{#dhcp-switch-router explanation="Le relais DHCP ne supprime pas les frontières entre les réseaux routés."}
:::

## Échange DHCPv4 initial

Le processus initial courant est désigné par l’acronyme DORA :

1. `DHCPDISCOVER` : un client recherche les serveurs disponibles.
2. `DHCPOFFER` : un serveur propose une adresse et des options.
3. `DHCPREQUEST` : le client sélectionne et demande un bail proposé.
4. `DHCPACK` : le serveur sélectionné confirme le bail et les options.

Les détails de la diffusion et de l’unicast varient selon l’état du client, l’utilisation d’un relais et les capacités du serveur. Une offre ne constitue pas encore un bail final utilisable ; l’accusé de réception achève l’échange de sélection normal.

:::single-choice{#dhcp-dora-order}
Quel est l’ordre initial normal de DHCPv4 ?

::option[OFFER, DISCOVER, ACK, REQUEST.]{#dhcp-wrong-order-one explanation="Un client effectue une découverte avant que le serveur ne fasse une offre, puis formule une demande avant l’accusé de réception."}
::option[DISCOVER, OFFER, REQUEST, ACK.]{#dhcp-correct-order .correct explanation="Cette séquence recherche, propose, sélectionne puis confirme."}
::option[REQUEST, ACK, DISCOVER, OFFER.]{#dhcp-wrong-order-two explanation="Un nouveau client doit normalement effectuer une découverte et recevoir une offre avant de sélectionner un bail."}
:::

## Renouvellement d’un bail

Un bail expire s’il n’est pas renouvelé. Un client commence normalement le renouvellement avant l’expiration, souvent en contactant d’abord directement le serveur d’origine. Si le renouvellement échoue, il élargit ensuite sa tentative de réattribution. Les temporisations exactes sont fournies ou calculées conformément au protocole.

L’affichage d’une adresse attribuée dynamiquement ne prouve pas que son bail durera indéfiniment. Lors du diagnostic d’un changement, relevez le bail actif, sa durée de vie, le serveur et les options.

:::single-choice{#dhcp-lease-expiration}
Que devient un bail d’adresse DHCP s’il n’est pas renouvelé avec succès ?

::option[Il devient une adresse MAC matérielle permanente.]{#dhcp-lease-mac explanation="Un bail IP ne modifie pas l’identité de la couche liaison."}
::option[Il finit par expirer, et le client doit cesser de le considérer comme valide.]{#dhcp-lease-expires .correct explanation="Le principe du bail permet de récupérer ou de modifier les adresses et les options conformément à la politique du serveur."}
::option[Il transforme le client en serveur racine DNS faisant autorité.]{#dhcp-lease-dns-root explanation="Un bail DHCP n’accorde aucune autorité DNS."}
:::

## Examiner le résultat

Une fois le client configuré par DHCP, vérifiez tous les éléments requis plutôt que la seule adresse :

```bash
$ ip address show
$ ip route show
$ resolvectl status
```

La commande du résolveur varie selon le système. Examinez également les données de bail et les journaux du gestionnaire de réseau actif. Des adresses en double peuvent encore apparaître à cause de serveurs non autorisés, d’attributions statiques au sein d’un pool, d’un état périmé ou d’une configuration manuelle ; DHCP réduit les erreurs, mais ne peut empêcher à lui seul tous les conflits.

:::single-choice{#dhcp-result-verification}
Que faut-il vérifier après l’acceptation d’un bail DHCP ?

::option[Uniquement le nom affiché de l’interface.]{#dhcp-interface-name-only explanation="Le nom d’une interface ne renseigne ni sur l’adressage, ni sur le routage, ni sur la résolution."}
::option[Uniquement si le clavier répond.]{#dhcp-keyboard explanation="La saisie au clavier est sans rapport avec la configuration d’un bail réseau."}
::option[L’adresse, les routes, le DNS et les détails du bail.]{#dhcp-check-complete-state .correct explanation="Une configuration utilisable dépend de plusieurs options et de leur état effectivement appliqué au système."}
:::

## DHCPv6 et configuration IPv6

Les hôtes IPv6 peuvent employer l’autoconfiguration sans état, DHCPv6, une configuration statique ou une combinaison de ces méthodes. DHCPv6 n’utilise pas l’échange DORA d’IPv4, et les informations sur le routeur par défaut proviennent normalement des annonces de routeur IPv6 plutôt que de DHCPv6.

:::single-choice{#dhcp-ipv6-default-router}
Où un hôte IPv6 obtient-il normalement les informations relatives à son routeur par défaut ?

::option[Dans les annonces de routeur IPv6.]{#dhcp-router-advertisement .correct explanation="DHCPv6 peut fournir d’autres paramètres, mais les routeurs s’annoncent au moyen de la découverte de voisins."}
::option[Dans la séquence de contrôle d’une trame Ethernet.]{#dhcp-ipv6-fcs explanation="La FCS détecte les altérations sur la liaison et ne contient aucune configuration de routeur."}
::option[Uniquement dans un message DHCPACK IPv4.]{#dhcp-ipv4-ack explanation="Les messages DHCP d’IPv4 ne configurent pas le routage IPv6."}
:::

## Résumé

Vous savez maintenant expliquer comment DHCPv4 loue et renouvelle la configuration réseau d’un hôte.

1. Distinguer les serveurs DHCP des relais et des sous-réseaux clients.
2. Suivre l’échange DISCOVER, OFFER, REQUEST et ACK.
3. Considérer les adresses et les options comme un état de bail limité dans le temps.
4. Vérifier ensemble l’adresse, les routes, le DNS et les métadonnées du bail.
5. Distinguer le comportement de DHCPv4 de l’autoconfiguration IPv6.
