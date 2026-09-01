---
lesson_id: "traceroute"
course_id: "troubleshooting"
lang: "fr"
order_index: 3
title: "traceroute"
description: "Découvrez comment traceroute trouve les sauts répondants et comment interpréter silences, délais et variations de chemin."
meta_title: "traceroute - Dépannage"
meta_description: "Maîtrisez traceroute sous Linux pour suivre les routes réseau et comprendre le rôle du TTL dans le diagnostic."
meta_keywords: "traceroute Linux, dépannage réseau, TTL, routage, commandes Linux"
---

`traceroute` envoie des sondes avec des valeurs croissantes de TTL IPv4 ou Hop Limit IPv6. Les routeurs où la valeur expire peuvent renvoyer Time Exceeded et révéler certains points répondants du trajet aller.

## Fonctionnement de la découverte des sauts

Les sondes commencent avec une limite de un, puis l'augmentent. Le premier routeur la décrémente à zéro et peut renvoyer une erreur ICMP. Une limite de deux atteint le deuxième routeur, et ainsi de suite jusqu'à la destination ou la limite maximale.

:::single-choice{#traceroute-expiring-field} Quel champ fait expirer les sondes successives sur des routeurs plus éloignés ?

::option[Le TTL du cache DNS du nom de destination.]{#traceroute-dns-ttl explanation="La durée d'un enregistrement DNS ne contrôle pas les sauts de transfert."}
::option[L'adresse MAC Ethernet source.]{#traceroute-source-mac explanation="Les adresses de liaison ne portent pas de compteur de sauts de bout en bout."}
::option[Le TTL IPv4 ou Hop Limit IPv6.]{#traceroute-hop-field .correct explanation="L'augmentation de ce compteur borné expose les sauts routés qui répondent."}
:::

## Méthodes de sondage

Le traceroute Linux traditionnel envoie souvent des datagrammes UDP vers des ports élevés. La destination peut terminer la découverte avec ICMP Port Unreachable. D'autres options utilisent ICMP Echo ou TCP SYN :

```bash
$ traceroute -n example.com
$ traceroute -I -n example.com
$ traceroute -T -p 443 -n example.com
```

Privilèges et options varient. N'utilisez que des méthodes autorisées et notez-les lorsque vous comparez des résultats.

:::single-choice{#traceroute-default-destination-response} Qu'est-ce qui termine couramment un traceroute UDP Linux traditionnel ?

::option[Une réponse ICMP Port Unreachable de la destination.]{#traceroute-port-unreachable .correct explanation="Les ports UDP élevés sont généralement inutilisés, ce qui permet à la destination de se signaler par cette erreur."}
::option[Une réponse HTTP 200 obligatoire de chaque routeur.]{#traceroute-http-every-router explanation="Les routeurs renvoient des erreurs de contrôle réseau, pas des réponses HTTP."}
::option[Une diffusion Ethernet de la destination sur Internet.]{#traceroute-ethernet-broadcast explanation="Les diffusions de liaison ne franchissent pas les réseaux routés."}
:::

## Interpréter les astérisques

Un astérisque signifie qu'aucune réponse n'a été observée avant l'expiration. Le routeur peut transférer le trafic tout en filtrant ou limitant ses réponses de diagnostic. Si des sauts suivants répondent, le saut silencieux a bien transmis au moins certaines sondes.

:::single-choice{#traceroute-asterisk-meaning} Que prouve `*` pour un saut ?

::option[Que le routeur abandonne définitivement tout trafic de transit.]{#traceroute-star-all-drop explanation="Les réponses ultérieures peuvent démontrer la poursuite du transfert."}
::option[Seulement qu'aucune réponse correspondante n'est arrivée avant l'expiration.]{#traceroute-star-no-response .correct explanation="Filtrage, limitation, perte et problème de route retour peuvent tous produire ce silence."}
::option[Que la destination n'a aucune adresse IP.]{#traceroute-star-no-address explanation="La sonde vise déjà une adresse ; un saut silencieux ne la supprime pas."}
:::

## Délais et variations de chemin

Les temps par saut sont des allers-retours vers des réponses de contrôle, pas la latence ajoutée entre deux lignes. Les routeurs peuvent déprioriser ces réponses. L'équilibrage peut faire varier le chemin, et la résolution de noms ralentir l'affichage ; `-n` évite les recherches inverses.

La route retour de chaque réponse ICMP peut différer du trajet aller. Répétez les tests et corrélez-les avec la mesure applicative avant d'identifier un goulot.

:::single-choice{#traceroute-hop-rtt-limit} Pourquoi ne faut-il pas soustraire les RTT de deux sauts comme latence exacte du lien ?

::option[Parce que traceroute exprime tous les temps en octets.]{#traceroute-times-bytes explanation="Les durées de sonde sont normalement en millisecondes."}
::option[Parce que les réponses peuvent emprunter d'autres retours et subir un traitement de contrôle variable.]{#traceroute-rtt-asymmetry .correct explanation="Ce sont des allers-retours source-saut distincts, pas des mesures unidirectionnelles synchronisées."}
::option[Parce que chaque routeur possède la même horloge que la source.]{#traceroute-router-clock explanation="La mesure ne repose pas sur la synchronisation des horloges distantes."}
:::

## Comparer avec l'application

Un traceroute peut atteindre la destination tandis que le service est bloqué, et un service fonctionner tandis que des routeurs intermédiaires cachent leurs réponses. Testez la même famille, adresse, transport et port que l'application, puis utilisez traceroute comme indice complémentaire.

:::single-choice{#traceroute-service-proof} Un traceroute terminé prouve-t-il la bonne santé d'un service HTTPS ?

::option[Oui, car chaque saut valide le certificat.]{#traceroute-validates-cert explanation="Les routeurs n'effectuent pas la validation TLS du client."}
::option[Non ; le transport, TLS et HTTP exigent leurs propres tests.]{#traceroute-not-app-proof .correct explanation="La découverte du chemin et la santé de l'application relèvent de couches différentes."}
::option[Oui, mais seulement si les noms DNS inverses apparaissent.]{#traceroute-rdns-proof explanation="Les noms n'établissent pas le fonctionnement applicatif."}
:::

## Résumé

Vous savez interpréter traceroute comme une série de sondes à sauts bornés, pas comme un oracle complet.

1. Expliquer la découverte par expiration du TTL ou Hop Limit.
2. Noter la méthode UDP, ICMP ou TCP.
3. Traiter les astérisques comme des réponses absentes, pas des pannes prouvées.
4. Ne pas déduire une latence exacte des RTT adjacents.
5. Corréler le chemin avec l'application réelle.
