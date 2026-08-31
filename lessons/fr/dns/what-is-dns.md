---
lesson_id: "what-is-dns"
course_id: "dns"
lang: "fr"
order_index: 1
title: "Qu'est-ce que le DNS ?"
description: "Découvrez comment le DNS organise et résout des noms distribués et des enregistrements de ressources typés."
meta_title: "Qu'est-ce que le DNS ? - DNS"
meta_description: "Si vous souhaitez apprendre le réseau sous Linux, comprendre le DNS est crucial. Ce guide explique ce qu'est le système de noms de domaine (DNS), comment il traduit les noms de domaine en adresses IP, et pourquoi il est l'annuaire essentiel d'Internet. Un point de départ parfait pour quiconque souhaite apprendre Linux."
meta_keywords: "DNS, Système de noms de domaine, Adresse IP, Apprendre Linux, Linux apprendre, Nom d'hôte, Réseau Linux, Débutant, Tutoriel, Guide, Labex Linux"
---

Le système de noms de domaine est une base de données distribuée et hiérarchique, ainsi qu'un protocole de requêtes. Il permet aux clients d'obtenir des informations typées associées à des noms, notamment des adresses, le routage du courrier, des serveurs faisant autorité, des données de services et des enregistrements de vérification.

## Noms et enregistrements de ressources

Le DNS fait davantage que traduire un nom d'hôte en une adresse IP. Un enregistrement `A` contient une adresse IPv4, `AAAA` une adresse IPv6, `MX` des données de routage du courrier et `NS` les noms des serveurs faisant autorité ; bien d'autres types transportent d'autres données. Un même nom peut avoir plusieurs enregistrements, voire aucun enregistrement d'adresse.

:::single-choice{#dns-purpose-beyond-address}
Pourquoi le DNS est-il plus qu'une liste de correspondances entre noms d'hôtes et adresses ?

::option[Il attribue définitivement des adresses MAC à chaque trame Ethernet.]{#dns-mac-frames explanation="La découverte des voisins de la couche liaison n'utilise pas ainsi le DNS."}
::option[Il stocke des enregistrements typés pour plusieurs formes de services et de délégation.]{#dns-typed-records .correct explanation="Les enregistrements d'adresse, courrier, autorité, alias et politiques possèdent des sémantiques distinctes."}
::option[Il garantit le bon fonctionnement de chaque application nommée.]{#dns-health-guarantee explanation="Les données DNS peuvent être résolues même si le service de destination est indisponible."}
:::

## Noms hiérarchiques

Un nom de domaine pleinement qualifié désigne un chemin dans l'arbre DNS. Dans `www.example.com.`, le point final représente la racine, `com` se trouve dessous, `example` sous `com`, et `www` est un nom de ce domaine. Les interfaces utilisateur omettent souvent le point final, mais celui-ci permet de distinguer les noms absolus des noms relatifs à un contexte local dans une configuration.

:::single-choice{#dns-trailing-dot}
Que représente le point final de `www.example.com.` ?

::option[La racine DNS et un nom absolu.]{#dns-root-dot .correct explanation="Le point termine le chemin complet entre le nœud nommé et la racine."}
::option[Un joker pour tous les domaines de premier niveau.]{#dns-dot-wildcard explanation="Un joker utilise une étiquette comme `*`, pas le terminateur de la racine."}
::option[Une instruction demandant uniquement IPv4.]{#dns-dot-ipv4 explanation="Le type d'enregistrement détermine la famille d'adresses demandée."}
:::

## Autorité distribuée

L'autorité DNS est déléguée vers le bas de la hiérarchie. Les serveurs racine dirigent les résolveurs vers les serveurs des domaines de premier niveau, qui les orientent vers les serveurs faisant autorité pour les zones déléguées. Les organisations gèrent ainsi leurs propres données d'autorité sans qu'un serveur central stocke tout l'espace de noms mondial.

:::single-choice{#dns-authoritative-data}
Qui fournit les données définitives d'une zone DNS déléguée ?

::option[N'importe quel navigateur ayant déjà visité le site.]{#dns-browser-authority explanation="Le cache d'un navigateur ne fait pas autorité pour la zone."}
::option[Les serveurs de noms configurés comme faisant autorité pour la zone.]{#dns-authoritative-servers .correct explanation="La délégation désigne les serveurs chargés de répondre avec autorité."}
::option[Chaque routeur qui transporte un paquet vers l'adresse.]{#dns-router-authority explanation="L'acheminement des paquets et l'autorité DNS sont des rôles distincts."}
:::

## Résolution et cache

Le résolveur stub d'un hôte envoie généralement une requête à un résolveur récursif. Celui-ci répond depuis un cache encore valide ou interroge la hiérarchie pour le client. Le TTL des enregistrements limite normalement leur durée de réutilisation en cache, ce qui améliore le passage à l'échelle, mais retarde la visibilité des changements jusqu'au rafraîchissement.

La réussite du DNS ne prouve pas le bon fonctionnement de la route, du transport, de TLS ou de l'application. Un échec peut aussi survenir avant toute requête externe, car `/etc/hosts`, les suffixes de recherche, les caches locaux et la politique du service de noms influencent le résolveur du système.

:::single-choice{#dns-cache-ttl-role}
Que contrôle principalement le TTL d'un enregistrement DNS ?

::option[Le nombre de routeurs qu'un paquet IP peut traverser.]{#dns-ip-hop-limit explanation="Le TTL IP ou Hop Limit est un champ d'un autre protocole."}
::option[La durée pendant laquelle l'application doit rester fonctionnelle.]{#dns-app-health-time explanation="La mise en cache DNS ne garantit pas la disponibilité du service."}
::option[La durée pendant laquelle un résolveur peut normalement conserver l'enregistrement en cache.]{#dns-cache-lifetime .correct explanation="Une durée de cache plus courte ou plus longue influe sur la charge des requêtes et la propagation des changements."}
:::

## Résumé

Vous savez maintenant décrire le DNS comme un système de données typées, mises en cache et hiérarchiques.

1. Distinguer les types d'enregistrements DNS selon leur fonction.
2. Lire un nom pleinement qualifié en partant de la racine.
3. Identifier la délégation et la responsabilité faisant autorité.
4. Séparer la résolution de noms de la connectivité applicative.
