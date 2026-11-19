---
lesson_id: "network-monitoring-dns-logs"
course_id: "network-monitoring"
lang: "fr"
order_index: 3
title: "Journaux DNS"
description: "Apprenez à distinguer une question DNS, sa réponse et une connexion ultérieure de l’application."
meta_title: "Journaux DNS - Supervision réseau"
meta_description: "Apprenez à distinguer une question DNS, sa réponse et une connexion ultérieure de l’application."
meta_keywords: "journaux DNS, supervision réseau, cybersécurité, Linux Journey"
---

Avant de se connecter à un service par son nom, un client peut demander une adresse au DNS. Un résolveur peut enregistrer la question et son résultat. Un **résolveur** recherche les noms pour le compte des clients.

## Identifier la question

Une entrée du journal DNS peut contenir l’heure, l’adresse du client, le nom et le type d’enregistrement demandé. Une requête de type `A` demande une adresse IPv4.

```text
09:21:00Z client=192.0.2.10 query=site.example type=A result=NOERROR answer=192.0.2.20
09:21:03Z client=192.0.2.10 query=preview.example type=A result=NXDOMAIN
```

Le premier résultat contient une adresse pour `site.example`. Le second indique que le DNS n’a trouvé aucun nom correspondant à `preview.example` lors de cette recherche.

:::single-choice{#network-monitoring-dns-logs-lookup-name} Quelle ligne a renvoyé une adresse IPv4 pour le nom demandé ?

::option[La résolution de site.example.]{#network-monitoring-dns-logs-lookup-name-a .correct explanation="Cette ligne contient une réponse avec une adresse IPv4."}
::option[La résolution de preview.example.]{#network-monitoring-dns-logs-lookup-name-b explanation="NXDOMAIN indique que le nom demandé n’existe pas dans les données consultées pour cette résolution."}
::option[Les deux lignes, car elles ont le même client.]{#network-monitoring-dns-logs-lookup-name-c explanation="Le client est le même et les résultats diffèrent."}
:::

## Lire le résultat

`NOERROR` signifie que l’échange DNS n’a signalé aucune erreur de protocole. Vérifiez aussi le champ de réponse. Une réponse peut porter le code `NOERROR` sans contenir d’enregistrement d’adresse du type demandé. Un échec peut également apparaître sous une autre forme, par exemple un dépassement de délai enregistré par le client.

:::single-choice{#network-monitoring-dns-logs-no-answer} Une ligne du journal DNS indique NOERROR, mais ne contient aucune réponse avec une adresse. Que faut-il rapporter ?

::option[Le client a forcément reçu une adresse IPv4.]{#network-monitoring-dns-logs-no-answer-a explanation="Le champ de réponse indique les adresses renvoyées dans cet exemple."}
::option[Le site a forcément refusé une connexion du navigateur.]{#network-monitoring-dns-logs-no-answer-c explanation="Cette ligne consigne un résultat DNS et ne décrit aucune requête du navigateur."}
::option[L’échange s’est terminé sans erreur de protocole et cette ligne ne fournit aucune adresse.]{#network-monitoring-dns-logs-no-answer-b .correct explanation="Le résultat et la réponse renseignent sur deux aspects différents."}
:::

## Vérifier séparément la connexion

Un client peut résoudre un nom puis choisir d’établir une connexion. Pour le vérifier, cherchez une entrée de connexion ou de flux correspondante. Comparez l’adresse de destination et l’heure. Les résultats DNS peuvent être en cache. Des connexions peuvent donc avoir lieu sans nouvelle résolution dans les journaux disponibles.

:::single-choice{#network-monitoring-dns-logs-dns-vs-flow} Quel élément montrerait le mieux que le client s’est ensuite connecté à l’adresse renvoyée ?

::option[Une autre vue de la réponse DNS seule.]{#network-monitoring-dns-logs-dns-vs-flow-a explanation="La réponse indique une adresse que le client peut utiliser."}
::option[Une entrée de connexion ou de flux correspondante qui indique la destination.]{#network-monitoring-dns-logs-dns-vs-flow-c .correct explanation="Cette entrée décrit le trafic ultérieur indépendamment de la résolution."}
::option[Une deuxième résolution DNS du même client.]{#network-monitoring-dns-logs-dns-vs-flow-b explanation="Une autre résolution confirme que le client a répété la recherche. La connexion ultérieure de l’application reste à vérifier."}
:::

## Résumé

Vous savez maintenant lire un journal DNS et distinguer la résolution de l’activité réseau ultérieure.

1. Repérez le client, la question et le type d’enregistrement demandé.
2. Interprétez ensemble le résultat et la réponse.
3. Cherchez une entrée distincte pour une connexion ultérieure.
