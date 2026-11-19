---
lesson_id: "linux-listening-services"
course_id: "linux-hardening"
lang: "fr"
order_index: 4
title: "Services à l’écoute"
description: "Apprenez à lire une adresse d’écoute sous Linux et à choisir d’où vérifier qu’elle est accessible."
meta_title: "Services à l’écoute - Durcissement de Linux"
meta_description: "Apprenez à lire une adresse d’écoute sous Linux et à choisir d’où vérifier qu’elle est accessible."
meta_keywords: "services à l’écoute, durcissement de Linux, cybersécurité, Linux Journey"
---

Un service peut attendre des connexions sur une adresse et un port précis. Un **socket d’écoute** est un point de communication prêt à recevoir des connexions entrantes. Son adresse donne un indice sur les clients qui peuvent l’atteindre.

## Lister les sockets TCP à l’écoute

Exécutez cette commande en lecture seule sur un hôte Linux d’exercice. Les options demandent à `ss` d’afficher les sockets TCP à l’écoute avec des adresses et des ports numériques.

```bash
$ ss -lnt
```

Lisez la colonne de l’adresse locale. Dans l’exemple ci-dessous, la prévisualisation web utilise `127.0.0.1:8091`. Le port est 8091. L’adresse est celle de la **boucle locale**, qui désigne l’hôte lui-même.

:::single-choice{#linux-listening-services-local-listener} Un navigateur sur le même hôte doit ouvrir la prévisualisation. Quelle adresse doit-il essayer ?

::option[0.0.0.0:8091.]{#linux-listening-services-local-listener-a explanation="Cette notation indique un mode d’écoute. La destination locale est celle affichée dans l’exemple."}
::option[127.0.0.1:8091.]{#linux-listening-services-local-listener-b .correct explanation="Le service écoute sur cette adresse de boucle locale et ce port."}
::option[Le port 80 sur un serveur sans rapport.]{#linux-listening-services-local-listener-c explanation="Le service de l’exemple écoute sur le port 8091 de son propre hôte."}
:::

![Sortie enregistrée de ss dans LabEx, montrant l’écoute sur le port 8091 de la boucle locale](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-listening-services/loopback-listener.png)

## Interpréter une écoute sur toutes les interfaces

L’adresse IPv4 locale `0.0.0.0:8091` signifie que le service écoute sur toutes les interfaces IPv4 de l’hôte. Cela peut inclure une interface joignable depuis un autre ordinateur. La liste des sockets d’écoute décrit ce que le processus accepte localement. Les règles du pare-feu et le routage peuvent limiter l’accès depuis une autre machine.

:::single-choice{#linux-listening-services-all-interfaces} Un service passe de 127.0.0.1 à 0.0.0.0 sur le même port. Qu’est-ce qui a changé ?

::option[Il peut écouter sur davantage d’interfaces IPv4.]{#linux-listening-services-all-interfaces-a .correct explanation="Le réglage élargit l’ensemble des adresses locales sur lesquelles les connexions entrantes sont acceptées."}
::option[Il écoute désormais sur un autre port.]{#linux-listening-services-all-interfaces-b explanation="Le numéro de port est resté identique."}
::option[Il garantit un accès immédiat depuis n’importe quel réseau.]{#linux-listening-services-all-interfaces-c explanation="Les règles réseau et le routage déterminent encore les chemins utilisables."}
:::

## Vérifier le chemin prévu

Un service interne destiné au personnel peut être réservé à un réseau. Vérifiez l’accès depuis ce réseau et, si vous devez confirmer la restriction, effectuez aussi un test depuis un emplacement approuvé à l’extérieur. Vérifiez le socket d’écoute et le chemin d’accès. Une liste locale ne suffit pas à savoir ce qu’un client distant a observé.

:::single-choice{#linux-listening-services-verify-from-client} Un socket écoute sur toutes les interfaces locales. Quel contrôle montre si un poste du personnel peut y accéder ?

::option[Relire le nom d’hôte.]{#linux-listening-services-verify-from-client-a explanation="Le nom d’hôte ne teste pas le chemin réseau."}
::option[Compter les sockets d’écoute.]{#linux-listening-services-verify-from-client-b explanation="Ce décompte n’indique pas si le poste peut se connecter."}
::option[Envoyer une requête autorisée depuis le réseau du personnel.]{#linux-listening-services-verify-from-client-c .correct explanation="Ce contrôle emprunte le chemin prévu."}
:::

Pour vérifier quels services écoutent sur un hôte Linux, commencez par la leçon Audit Listening Services (auditer les services à l’écoute) dans [Sécurité Linux pour le DevSecOps](https://labex.io/courses/linux-security-for-devsecops).

## Résumé

Vous savez maintenant lire une adresse d’écoute avant de décider d’où tester l’accès.

1. Listez les sockets TCP locaux à l’écoute avec une commande en lecture seule.
2. Distinguez la boucle locale de l’écoute sur toutes les interfaces IPv4.
3. Vérifiez la connexion depuis l’emplacement client pertinent.
