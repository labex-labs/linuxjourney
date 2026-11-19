---
lesson_id: "web-http-requests-responses"
course_id: "web-security"
lang: "fr"
order_index: 1
title: "Requêtes et réponses HTTP"
description: "Apprenez à lire la méthode, le chemin, le statut et le type de contenu d’un échange HTTP."
meta_title: "Requêtes et réponses HTTP - Sécurité web"
meta_description: "Apprenez à lire la méthode, le chemin, le statut et le type de contenu d’un échange HTTP."
meta_keywords: "requêtes et réponses HTTP, sécurité web, cybersécurité, Linux Journey"
---

Un navigateur ou un autre client adresse une **requête HTTP** à un serveur web pour lui demander quelque chose. Le serveur renvoie une **réponse HTTP**. En lisant les deux messages, vous pouvez voir ce que le client a demandé et ce que le serveur a renvoyé.

## Lire la requête

Voici une courte requête HTTP/1.1. `GET` est la méthode, qui décrit l’action demandée par le client. `/health` est le chemin. L’en-tête `Host` indique à quel site web le client s’adresse.

```http
GET /health HTTP/1.1
Host: site.example
```

Un **en-tête** est une valeur nommée qui fournit des informations sur le message. La méthode et le chemin figurent sur la première ligne de la requête.

:::single-choice{#web-http-requests-responses-request-path} Qu’est-ce que ce client demande au serveur de récupérer ?

::option[Un fichier nommé HTTP/1.1.]{#web-http-requests-responses-request-path-b explanation="Ce champ indique la version du protocole."}
::option[La ressource à l’adresse /health.]{#web-http-requests-responses-request-path-a .correct explanation="Le chemin figure après GET sur la première ligne."}
::option[Une ressource à l’adresse /site.example.]{#web-http-requests-responses-request-path-c explanation="L’en-tête Host indique le site web. Le chemin figure sur la première ligne."}
:::

## Lire une réponse

Dans un dossier d’exercice vide, créez une page et démarrez un serveur HTTP Python sur la boucle locale. La redirection écrit la page. Laissez le serveur tourner dans ce terminal jusqu’à la fin de la requête, puis arrêtez-le avec Ctrl+C.

```bash
$ mkdir web-demo
$ printf '%s\n' ready > web-demo/health.txt
$ python3 -m http.server 8094 --bind 127.0.0.1 --directory web-demo
```

Depuis un deuxième terminal sur la même machine, exécutez `curl -i`. Cette option affiche les en-têtes de la réponse avant son contenu.

```bash
$ curl -i http://127.0.0.1:8094/health.txt
```

La première ligne d’une réponse contient un **code de statut**. Un code `200` signale que cette requête a réussi. Une ligne vide sépare les en-têtes du corps. `Content-Type` indique au client comment interpréter le corps, par exemple comme du texte brut.

:::single-choice{#web-http-requests-responses-response-parts} Quelle partie aide le client à déterminer comment afficher le contenu ?

::option[L’en-tête Content-Type de la réponse.]{#web-http-requests-responses-response-parts-b .correct explanation="Il décrit le type du corps de la réponse."}
::option[Le nom d’hôte de la requête d’origine.]{#web-http-requests-responses-response-parts-a explanation="Il nomme le site contacté par le client."}
::option[Le chemin seul.]{#web-http-requests-responses-response-parts-c explanation="Le chemin identifie la ressource sans préciser le format renvoyé."}
:::

![Réponse HTTP enregistrée dans LabEx avec le statut 200, un type de contenu texte et le corps ready](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/web-security/web-http-requests-responses/http-response.png)

## Comparer deux résultats

Une réponse `404` indique que le serveur n’a pas trouvé la ressource demandée ou ne révèle pas son existence. Un site peut renvoyer 200 sur un chemin et 404 sur un autre. Utilisez la méthode et le chemin exacts pour comparer les résultats.

:::single-choice{#web-http-requests-responses-health-scope} Une requête vers /health reçoit 200. Que pouvez-vous en conclure sur /welcome ?

::option[/welcome a également renvoyé 200.]{#web-http-requests-responses-health-scope-a explanation="L’exemple a vérifié un autre chemin."}
::option[L’hôte n’a pas pu être contacté.]{#web-http-requests-responses-health-scope-b explanation="Le contrôle d’état a reçu une réponse."}
::option[Il faut demander /welcome pour connaître son résultat.]{#web-http-requests-responses-health-scope-c .correct explanation="Les deux chemins peuvent se comporter différemment."}
:::

Pour vous entraîner à vérifier les en-têtes de réponse et la connexion, essayez [Tester la connexion à un serveur avec curl sous Linux](https://labex.io/tutorials/linux-how-to-test-server-connectivity-with-curl-in-linux-415082).

## Résumé

Vous savez maintenant lire les principales parties d’un échange HTTP simple.

1. Repérez la méthode, le chemin et l’hôte dans une requête.
2. Lisez le statut et le type de contenu dans la réponse.
3. Décrivez le résultat de la requête exacte qui a été envoyée.
