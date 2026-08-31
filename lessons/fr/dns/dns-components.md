---
lesson_id: "dns-components"
course_id: "dns"
lang: "fr"
order_index: 2
title: "Composants DNS"
description: "Découvrez comment les résolveurs récursifs, serveurs faisant autorité, zones et enregistrements se partagent les responsabilités DNS."
meta_title: "Composants DNS - DNS"
meta_description: "Découvrez les composants DNS : serveurs de noms, fichiers de zone et enregistrements de ressources. Comprenez comment fonctionne le DNS pour les débutants. Commencez votre parcours de mise en réseau Linux !"
meta_keywords: "composants DNS, serveur de noms, fichier de zone, enregistrements de ressources, tutoriel DNS, mise en réseau Linux, guide du débutant"
---

Le DNS sépare la récursion tournée vers le client de la publication faisant autorité. Comprendre cette frontière évite de prendre une réponse mise en cache pour le propriétaire d'une zone.

## Résolveurs stub et récursifs

Un résolveur stub dans une application ou un système d'exploitation envoie ses requêtes au résolveur récursif configuré. Celui-ci renvoie une réponse finale, une erreur ou le résultat d'un renvoi après avoir utilisé son cache et, si nécessaire, des requêtes itératives. Sa réponse ne porte l'indicateur de réponse faisant autorité que si le serveur répondant possède cette autorité ; la récursion seule ne la confère pas.

:::single-choice{#dns-components-recursive-role}
Que fait un résolveur récursif pour un client stub ?

::option[Il obtient un résultat DNS final grâce au cache et à d'autres serveurs de noms.]{#dns-components-recursive-result .correct explanation="Le client délègue au service récursif les différentes étapes de la recherche."}
::option[Il remplace chaque routeur réseau sur le chemin des paquets.]{#dns-components-replaces-router explanation="La résolution de noms et l'acheminement IP sont distincts."}
::option[Il devient l'autorité de chaque enregistrement qu'il met en cache.]{#dns-components-cache-authority explanation="Les données en cache conservent l'autorité de leur source ; le résolveur n'est pas propriétaire de la zone."}
:::

## Serveurs de noms faisant autorité

Un serveur faisant autorité répond depuis les données des zones dont il a la charge. Une zone doit posséder plusieurs serveurs d'autorité, avec des données synchronisées et des risques de panne indépendants. Un serveur exclusivement d'autorité n'a pas besoin d'effectuer la récursion pour des clients arbitraires.

:::single-choice{#dns-components-authoritative-role}
Qu'est-ce qui rend un serveur faisant autorité pour une zone ?

::option[Il a déjà interrogé cette zone par un résolveur public.]{#dns-components-once-queried explanation="Une requête ou une mise en cache ne confère aucune autorité."}
::option[Il sert les données de la zone selon la délégation et la configuration pertinentes.]{#dns-components-serves-zone .correct explanation="L'autorité provient de la délégation DNS et de la zone chargée sur le serveur, pas d'une copie mise en cache."}
::option[Il répond le plus vite à un ping.]{#dns-components-fastest-ping explanation="Le temps de réponse ICMP ne définit pas l'autorité DNS."}
:::

## Zones et stockage des zones

Une zone est une portion de l'espace de noms servie administrativement. Elle commence à son sommet et peut déléguer des zones enfants. Ses données peuvent résider dans un fichier texte, être générées depuis une base de données, chargées par une API ou synthétisées par un logiciel ; un « fichier de zone » physique n'est pas obligatoire.

Le sommet possède normalement un enregistrement SOA et un ensemble NS. Les données de délégation du parent identifient les serveurs de l'enfant, parfois avec des enregistrements d'adresse glue nécessaires pour joindre les noms de serveurs qui appartiennent à la zone déléguée.

:::single-choice{#dns-components-zone-meaning}
Qu'est-ce qu'une zone DNS ?

::option[Une portion de l'espace de noms servie administrativement.]{#dns-components-admin-portion .correct explanation="Elle peut contenir des enregistrements et délégations quel que soit le système de stockage."}
::option[Un unique fichier texte obligatoire sur chaque client.]{#dns-components-client-file explanation="Les implémentations d'autorité peuvent employer plusieurs formes de stockage, et les clients ne détiennent pas toutes les zones."}
::option[Un domaine de diffusion Ethernet identifié par un VLAN.]{#dns-components-vlan explanation="Les zones DNS et les segments de couche liaison sont des concepts indépendants."}
:::

## Champs des enregistrements de ressources

Un enregistrement possède un nom de propriétaire, un TTL, une classe, un type et des RDATA propres au type. Par exemple :

```text
www.example.com.  300  IN  A  192.0.2.25
```

Le propriétaire est `www.example.com.`, le TTL 300 secondes, la classe Internet, le type une adresse IPv4 et les RDATA l'adresse. Les règles d'omission de champs et de noms relatifs des fichiers de zone exigent une gestion attentive de l'origine.

:::single-choice{#dns-components-mx-type}
Quel type d'enregistrement publie les préférences et noms d'hôtes des échangeurs de courrier ?

::option[`A`]{#dns-components-a explanation="Un enregistrement A stocke une adresse IPv4."}
::option[`NS`]{#dns-components-ns explanation="Les enregistrements NS identifient les serveurs de noms faisant autorité."}
::option[`MX`]{#dns-components-mx .correct explanation="Les RDATA MX comprennent une préférence et le nom d'un échangeur de courrier."}
:::

## TTL et cache négatif

Les enregistrements positifs emploient des TTL pour limiter leur réutilisation en cache. Les réponses négatives, comme la preuve d'un nom inexistant, peuvent aussi être mises en cache selon des règles issues du SOA. Réduire un TTL peu avant un changement planifié ne touche que les enregistrements récupérés après que les caches ont vu la nouvelle valeur ; ceux déjà mis en cache avec l'ancien TTL subsistent jusqu'à leur expiration.

:::single-choice{#dns-components-lower-ttl-timing}
Pourquoi réduire un TTL DNS bien avant un changement d'adresse prévu ?

::option[Le TTL modifie le MTU Ethernet du serveur.]{#dns-components-ttl-mtu explanation="La durée du cache et la taille des paquets sur le lien n'ont aucun rapport."}
::option[Un TTL faible garantit que la nouvelle application fonctionne.]{#dns-components-ttl-health explanation="Il agit sur le cache, pas sur la correction du service."}
::option[Les caches existants doivent avoir le temps d'expirer les données apprises avec l'ancien TTL plus long.]{#dns-components-old-cache-expiry .correct explanation="Modifier les données d'autorité ne peut pas raccourcir rétroactivement la durée restante d'un enregistrement déjà en cache."}
:::

## Résumé

Vous savez maintenant séparer la récursion DNS, l'autorité, la gestion de l'espace de noms et les données en cache.

1. Identifier les rôles des résolveurs stub et récursifs.
2. Définir l'autorité par le service délégué d'une zone.
3. Voir une zone comme une responsabilité sur l'espace de noms et non comme un fichier obligatoire.
4. Lire les champs propriétaire, TTL, classe, type et RDATA.
5. Planifier les durées de cache avant les changements DNS.
