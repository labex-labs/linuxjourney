---
lesson_id: "netstat"
course_id: "troubleshooting"
lang: "fr"
order_index: 4
title: "netstat"
description: "Apprenez à inspecter les sockets, écouteurs, files et états TCP Linux avec ss."
meta_title: "netstat - Dépannage"
meta_description: "Analysez connexions, ports et sockets Linux avec ss et comprenez SYN-SENT, CLOSE-WAIT et TIME-WAIT."
meta_keywords: "netstat Linux, ss, sockets, CLOSE-WAIT, SYN-SENT, connexions réseau"
---

L'ancien outil `netstat` affiche sockets, routes et statistiques d'interfaces. Sur Linux moderne, `ss` est préféré pour inspecter efficacement l'état des sockets du noyau et reste maintenu avec iproute2.

## Lister les sockets en écoute

Affichez numériquement les écouteurs TCP et UDP, avec leurs processus lorsque les droits le permettent :

```bash
$ sudo ss -lntup
```

`-l` choisit les écouteurs, `-n` évite la résolution, `-t` et `-u` choisissent TCP et UDP, et `-p` demande le processus. UDP étant sans connexion, ses sockets liées n'ont pas l'état `LISTEN` de la négociation TCP.

:::single-choice{#netstat-ss-numeric}
Pourquoi employer `-n` lors d'un dépannage de sockets ?

::option[Pour créer un nouvel espace de noms réseau.]{#netstat-new-namespace explanation="Cette option contrôle la résolution des noms dans la sortie."}
::option[Pour empêcher les recherches de noms d'adresses et de ports.]{#netstat-numeric-output .correct explanation="La sortie numérique évite de confondre un nom conventionnel avec l'identité réellement observée."}
::option[Pour fermer toutes les sockets qui n'écoutent pas.]{#netstat-close-sockets explanation="L'inspection ne termine aucune socket."}
:::

## Ports, extrémités et services

Une extrémité locale combine adresse, protocole de transport et port. Une connexion TCP se distingue par protocole, adresses et ports source et destination. `/etc/services` associe des noms conventionnels à des numéros, sans prouver quel processus possède un port ni quel protocole applicatif il parle.

:::single-choice{#netstat-services-file-limit}
Qu'établit une entrée `/etc/services` telle que `https 443/tcp` ?

::option[Qu'un serveur HTTPS sain écoute actuellement.]{#netstat-healthy-listener explanation="Une base statique ne prouve pas l'état d'exécution."}
::option[L'association conventionnelle entre ce nom de service et ce port.]{#netstat-conventional-name .correct explanation="La propriété de la socket et le protocole réel exigent une inspection et des tests."}
::option[Que tout trafic du port 443 est correctement chiffré.]{#netstat-all-encrypted explanation="Un numéro de port ne valide pas TLS."}
:::

## Lire les états TCP

- `SYN-SENT` : l'extrémité locale a demandé une connexion et attend la suite.
- `ESTAB` : la connexion TCP est établie.
- `CLOSE-WAIT` : le pair a fermé son sens d'envoi, mais l'application locale n'a pas fermé sa socket.
- `TIME-WAIT` : l'extrémité ayant fermé activement attend l'expiration des segments retardés.

Une population importante ou croissante de `CLOSE-WAIT` pointe souvent vers le nettoyage de l'application locale. `TIME-WAIT` est normal ; sa quantité et son impact déterminent s'il pose problème.

:::single-choice{#netstat-close-wait-owner}
Quel côté doit encore fermer une socket en `CLOSE-WAIT` ?

::option[Tous les routeurs d'Internet.]{#netstat-all-routers-close explanation="Les routeurs ne possèdent pas la socket d'extrémité."}
::option[Le serveur DNS faisant autorité.]{#netstat-dns-close explanation="Le DNS est sans rapport avec la fermeture TCP locale."}
::option[L'application locale.]{#netstat-local-close .correct explanation="TCP a reçu le FIN du pair et attend que le processus local ferme son côté."}
:::

## Interpréter les files

Le sens de `Recv-Q` et `Send-Q` dépend de l'état et du protocole. Sur TCP établi, elles peuvent indiquer des données en attente de lecture applicative ou d'acquittement. Sur un écouteur, elles décrivent plutôt l'arriéré des connexions.

Un instantané ne prouve ni fuite ni goulot. Échantillonnez dans le temps et corrélez avec processus, latence, retransmissions et limites de ressources.

:::single-choice{#netstat-queue-snapshot}
Pourquoi un seul instantané avec une grande file ne suffit-il pas au diagnostic ?

::option[Linux ne stocke jamais de données dans les files de sockets.]{#netstat-no-queues explanation="Le réseau du noyau repose sur des files d'envoi et de réception."}
::option[Chaque valeur de file est une permission de fichier.]{#netstat-queue-permission explanation="Ces champs décrivent l'état réseau."}
::option[L'impact exige l'état, la tendance et le contexte de charge.]{#netstat-queue-context .correct explanation="Une pointe transitoire diffère d'un goulot durable dans l'application ou le réseau."}
:::

## Filtrer l'enquête

```bash
$ ss -tn state established
$ ss -ltn 'sport = :443'
```

Limitez la sortie au protocole, à l'état, à l'extrémité ou au processus concernés. Un écouteur prouve la disponibilité locale du transport, pas l'accessibilité distante ni la santé de l'application. Poursuivez avec des tests de route, pare-feu, paquets, TLS et application.

:::single-choice{#netstat-listener-limit}
Qu'est-ce qu'un écouteur TCP sur le port 443 ne prouve pas ?

::option[Qu'une socket locale a réussi les opérations bind et listen.]{#netstat-listen-local explanation="C'est précisément l'état local affiché."}
::option[Que des clients distants peuvent terminer une requête HTTPS valide.]{#netstat-not-remote-proof .correct explanation="Le chemin, la politique, TLS et l'application restent à tester."}
::option[Que TCP possède un champ de port numérique.]{#netstat-port-field explanation="La sortie de l'écouteur en contient directement un."}
:::

## Résumé

Vous savez utiliser `ss` pour inspecter les sockets sans confondre ports et applications.

1. Lister numériquement les écouteurs avec leurs processus.
2. Distinguer les noms conventionnels de la propriété réelle.
3. Lire les états de fermeture depuis l'extrémité locale.
4. Échantillonner les files avec le contexte de charge.
5. Vérifier l'application distante au-delà de l'écouteur local.
