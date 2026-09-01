---
lesson_id: "dns-process"
course_id: "dns"
lang: "fr"
order_index: 3
title: "Processus DNS"
description: "Découvrez comment les résolveurs stub et récursif utilisent cache, renvois, glue et autorité pour répondre à une requête DNS."
meta_title: "Processus DNS - DNS"
meta_description: "Explorez le processus de résolution DNS étape par étape, des serveurs racine au serveur DNS faisant autorité. Comprenez comment un serveur Linux trouve un domaine, un concept crucial pour les environnements de production et l'hébergement de domaines."
meta_keywords: "processus DNS, recherche DNS, résolution de domaine, dns linux, serveur de production, hébergement de domaine, serveur dns, TLD, serveurs racine, dns faisant autorité"
---

Une application ordinaire interroge le résolveur stub du système d'exploitation, lequel consulte la politique locale du service de noms et envoie une requête récursive au résolveur configuré. Ce dernier ne parcourt la hiérarchie que si son cache valide ne répond pas déjà.

## Commencer par la politique locale et le cache

Le résolveur du système peut consulter `/etc/hosts`, le DNS et d'autres sources dans l'ordre configuré. Les suffixes de recherche peuvent transformer un nom court en plusieurs noms candidats. Le résolveur récursif vérifie ensuite ses caches positif et négatif avant d'envoyer du trafic en amont.

:::single-choice{#dns-process-cache-first} Pourquoi un résolveur récursif peut-il ne contacter aucun serveur faisant autorité pour une requête ?

::option[Le DNS exige que chaque requête échoue d'abord localement.]{#dns-process-requires-failure explanation="Un résolveur peut répondre immédiatement depuis son cache."}
::option[Il possède une réponse en cache encore valide.]{#dns-process-valid-cache .correct explanation="La mise en cache évite de répéter le parcours hiérarchique jusqu'à l'expiration de l'enregistrement."}
::option[Les serveurs faisant autorité n'acceptent que des trames Ethernet de clients.]{#dns-process-authoritative-ethernet explanation="Le DNS fonctionne sur des transports IP à travers des réseaux routés."}
:::

## Interroger un serveur racine

En cas d'absence en cache, le résolveur récursif peut interroger un serveur racine. La racine DNS comporte 13 identités de serveurs nommées de A à M, servies par de nombreuses instances physiques grâce à l'anycast et d'autres techniques résilientes. La réponse renvoie normalement le résolveur vers les serveurs du domaine de premier niveau pertinent au lieu de fournir l'adresse finale.

:::single-choice{#dns-process-root-response} Que renvoie normalement un serveur racine pour une recherche non mise en cache de `www.example.com` ?

::option[Un renvoi vers les serveurs du domaine de premier niveau `com`.]{#dns-process-root-referral .correct explanation="La hiérarchie délègue les responsabilités au lieu de stocker chaque enregistrement d'hôte final à la racine."}
::option[La page Web hébergée sur `www.example.com`.]{#dns-process-root-webpage explanation="Le DNS renvoie des enregistrements de ressources et non du contenu applicatif."}
::option[L'adresse MAC Ethernet de la destination.]{#dns-process-root-mac explanation="Les adresses MAC se résolvent sur les liens locaux, pas dans la hiérarchie DNS."}
:::

## Suivre les renvois du TLD et des serveurs d'autorité

Le résolveur interroge un serveur faisant autorité pour `com`, qui renvoie les serveurs délégués de `example.com`. Le renvoi peut inclure des enregistrements d'adresse glue lorsqu'ils sont nécessaires pour joindre un serveur dont le nom se trouve dans l'enfant délégué. Le résolveur interroge ensuite un serveur d'autorité pour l'enregistrement demandé.

:::single-choice{#dns-process-glue-purpose} Quel problème les données glue du DNS contribuent-elles à résoudre ?

::option[Le chiffrement des données HTTP après la résolution DNS.]{#dns-process-glue-http explanation="TLS ou d'autres mécanismes applicatifs assurent le chiffrement du contenu."}
::option[Le choix du port de commutateur Ethernet le plus rapide.]{#dns-process-glue-switch explanation="Les données glue sont des adresses de délégation, pas une politique de transfert sur le lien."}
::option[La connexion à un serveur dans la zone enfant sans résolution circulaire.]{#dns-process-glue-reachability .correct explanation="Le parent fournit l'adresse nécessaire pour joindre un serveur dont le nom appartient à la zone déléguée."}
:::

## Suivre les alias et les types d'enregistrements

Une réponse peut contenir un alias CNAME qui nécessite la recherche d'un autre nom, ou des enregistrements propres à l'application qui entraînent d'autres requêtes. Une demande `A` ne renvoie que les adresses IPv4 et les données liées à leur chaîne ; une requête `AAAA` distincte obtient les adresses IPv6. La réponse finale porte un état comme `NOERROR`, `NXDOMAIN` ou `SERVFAIL`, chacun ayant un sens différent.

:::single-choice{#dns-process-nxdomain-meaning} Que signale `NXDOMAIN` ?

::option[Le nom de domaine interrogé n'existe pas selon une réponse faisant autorité.]{#dns-process-name-does-not-exist .correct explanation="Ce cas diffère d'un nom existant qui ne possède simplement pas le type d'enregistrement demandé."}
::option[Le nom existe et possède toujours un enregistrement A vide.]{#dns-process-empty-a explanation="Un nom existant sans les données demandées produit normalement une réponse sans données, pas NXDOMAIN."}
::option[Le résolveur a atteint la taille maximale d'une trame Ethernet.]{#dns-process-frame-size explanation="Cet état concerne l'existence du nom."}
:::

## Validation, cache et utilisation par l'application

Un résolveur récursif validant peut utiliser les signatures DNSSEC et la chaîne de confiance pour vérifier un déni authentifié ou l'intégrité d'un enregistrement. DNSSEC ne chiffre pas les requêtes et ne prouve pas que l'application à l'adresse renvoyée est digne de confiance.

Le résolveur met les résultats en cache selon les règles de TTL et les renvoie au stub. L'application choisit ensuite une adresse et tente ses propres protocoles réseau et de sécurité.

:::single-choice{#dns-process-dnssec-limit} Que ne fournit pas la validation DNSSEC ?

::option[L'intégrité et l'authentification de l'origine des données DNS signées.]{#dns-process-dnssec-does-integrity explanation="Il s'agit d'objectifs fondamentaux de DNSSEC."}
::option[Le déni authentifié de données inexistantes signées.]{#dns-process-authenticated-denial explanation="Les mécanismes de déni signé peuvent fournir cette validation."}
::option[La confidentialité de la requête et de la réponse DNS.]{#dns-process-no-confidentiality .correct explanation="Le chiffrement exige un transport DNS protégé distinct, comme DoT ou DoH."}
:::

## Résumé

Vous savez maintenant suivre une résolution DNS récursive depuis la politique locale jusqu'à la réponse finale mise en cache.

1. Vérifier d'abord les sources locales et le cache du résolveur.
2. Suivre les renvois de la racine et du domaine de premier niveau.
3. Utiliser les données glue pour joindre les serveurs délégués.
4. Distinguer les alias, les réponses sans données et les noms inexistants.
5. Séparer l'intégrité DNSSEC de la confidentialité du transport.
