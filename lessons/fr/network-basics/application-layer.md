---
lesson_id: "application-layer"
course_id: "network-basics"
lang: "fr"
order_index: 5
title: "Couche application"
description: "Découvrez comment les protocoles applicatifs définissent les messages, l'état, le nommage et le comportement de sécurité des services."
meta_title: "Couche application - Réseaux"
meta_description: "Explorez la couche application du modèle TCP/IP, les protocoles HTTP, DNS, SSH et SMTP, les rôles client-serveur, ports et TLS."
meta_keywords: "couche application, protocole applicatif, modèle TCP/IP, SMTP, HTTP, DNS, client serveur, TLS"
---

La couche application de TCP/IP contient les protocoles qu'emploient les applications pour demander et fournir des services réseau. Elle couvre de nombreuses fonctions que la terminologie OSI sépare dans les couches application, présentation et session.

## Messages et sémantique des protocoles

Un protocole applicatif définit la manière dont les pairs interprètent les messages et l'état. HTTP définit les requêtes, réponses, méthodes, codes d'état et champs. DNS définit les requêtes et enregistrements de ressources. SMTP définit les commandes et réponses du transfert de courrier.

Tous les protocoles applicatifs n'ajoutent pas un unique « en-tête applicatif » fixe. Certains emploient des champs textuels, d'autres des enregistrements binaires ou plusieurs formats imbriqués, et certains transportent une suite continue de messages sur une même connexion de transport.

:::single-choice{#application-layer-protocol-role} Que définit principalement un protocole applicatif ?

::option[Le sens et les règles d'échange des messages d'un service.]{#application-layer-message-semantics .correct explanation="Les pairs ont besoin d'une syntaxe, d'une sémantique et d'un comportement d'état communs pour interagir."}
::option[La tension de chaque câble Ethernet.]{#application-layer-voltage explanation="La signalisation physique relève des technologies des couches inférieures."}
::option[La route choisie indépendamment par chaque routeur d'Internet.]{#application-layer-router-choice explanation="Les décisions de routage relèvent de la couche réseau."}
:::

## Clients, serveurs et pairs

Un client initie une demande ou une connexion à un service ; un serveur écoute ou l'accepte d'une autre manière. Il s'agit de rôles dans une interaction, pas de catégories permanentes d'appareils. Un même hôte peut être client pour le DNS et serveur pour SSH simultanément, et certains protocoles emploient des rôles pair à pair.

:::single-choice{#application-layer-client-role} Qu'est-ce qui fait d'un programme le client dans un échange demande-réponse typique ?

::option[Il initie une demande vers le service.]{#application-layer-client-initiates .correct explanation="Client et serveur décrivent des rôles d'interaction qu'un même hôte peut remplir simultanément pour différents services."}
::option[Il doit s'exécuter sur un ordinateur portable plutôt que sur un serveur.]{#application-layer-client-laptop explanation="La catégorie du matériel ne détermine pas le rôle dans le protocole."}
::option[Il possède le préfixe IP de destination.]{#application-layer-client-prefix explanation="La propriété du réseau est sans rapport avec l'initiation d'une demande applicative."}
:::

## Noms, ports et sélection des services

Une application peut résoudre le nom d'un service vers une ou plusieurs adresses IP, puis choisir un terminal de transport. Les ports bien connus fournissent des valeurs par défaut, pas la preuve immuable d'un protocole. HTTP emploie couramment le port TCP 80 et HTTPS le port TCP 443, mais tous deux peuvent fonctionner ailleurs. SMTP utilise différents ports et règles pour le relais et la soumission des messages.

:::single-choice{#application-layer-port-limit} Que prouve à lui seul un port TCP 443 ouvert ?

::option[Qu'un processus y a accepté un terminal TCP, mais que son comportement applicatif doit encore être testé.]{#application-layer-port-endpoint .correct explanation="L'échange du protocole et la validation TLS fournissent des preuves plus solides au niveau applicatif."}
::option[Que le service est certainement une application HTTPS correctement configurée.]{#application-layer-port-proves-https explanation="Un numéro de port ne valide ni le comportement du protocole, ni l'identité, ni la santé."}
::option[Que le DNS ne peut pas renvoyer d'adresse IPv6.]{#application-layer-port-dns explanation="Les ports de transport ne limitent pas les familles d'enregistrements DNS."}
:::

## Sécurité et tests de bout en bout

TLS peut ajouter confidentialité, intégrité et identité authentifiée du pair lorsque la validation du certificat et le nom du terminal sont corrects. Il n'autorise pas automatiquement chaque action de l'application. Testez le même nom, la même famille d'adresses, le même port, protocole, les mêmes identifiants et la même demande que le véritable client.

Un diagnostic HTTPS peut par exemple contrôler séparément la résolution, la connexion TCP, le certificat et le nom TLS, la réponse HTTP et le contenu applicatif. La réussite d'une étape réduit le problème sans prouver toutes les suivantes.

:::single-choice{#application-layer-tls-limit} Qu'établit la validation réussie d'un certificat TLS ?

::option[Que chaque utilisateur est autorisé pour toutes les ressources.]{#application-layer-tls-all-users explanation="L'authentification du transport ne remplace pas les règles d'accès de l'application."}
::option[L'identité du pair pour le nom validé et un canal sécurisé authentifié.]{#application-layer-tls-identity .correct explanation="L'autorisation applicative et la justesse du contenu exigent encore leurs propres contrôles."}
::option[Qu'aucun routeur ne pourra jamais perdre un paquet ultérieur.]{#application-layer-tls-routing explanation="TLS ne peut pas garantir la livraison future par le réseau."}
:::

## Résumé

Vous savez maintenant décrire le comportement de la couche application au-delà d'un numéro de port ou d'un nom de programme.

1. Identifier la syntaxe, la sémantique et l'état des protocoles comme des préoccupations applicatives.
2. Considérer client et serveur comme des rôles dans un échange.
3. Employer les ports comme conventions de terminaux plutôt que comme preuves du protocole.
4. Tester le nommage, la sécurité et les réponses applicatives de bout en bout.
