---
lesson_id: "docker-port-mapping"
course_id: "docker"
lang: "fr"
order_index: 5
title: "Publication de ports"
description: "Apprenez à publier un port de conteneur et à déterminer l’adresse à ouvrir dans le navigateur."
meta_title: "Publication de ports - Docker"
meta_description: "Lisez une redirection de port Docker, distinguez le port de l’hôte de celui du conteneur et repérez une requête envoyée au mauvais port."
meta_keywords: "publication de ports Docker, ports publiés, docker run -p, port de l’hôte, port du conteneur"
---

Un serveur web peut tourner dans un conteneur sans être encore accessible à votre navigateur. Un **port** est un numéro qui permet à une machine de transmettre les requêtes réseau entrantes au bon service. Docker peut publier un port sur l’hôte et rediriger ces requêtes vers un port du conteneur.

## Lire une redirection de port

Dans cet exemple, Nginx reçoit les requêtes web sur le port 80 du conteneur. Le conteneur `web` de l’exemple précédent a été créé sans port publié. Donnez un autre nom au nouveau conteneur et utilisez `-p` pour définir la redirection au moment de sa création.

```bash
$ docker run -d --name published-web -p 127.0.0.1:8080:80 nginx:alpine
```

`8080:80` redirige le **port de l’hôte** 8080, auquel se connecte le navigateur, vers le **port du conteneur** 80, où le serveur reçoit la requête. Avec `127.0.0.1`, on lie la redirection à l’adresse de bouclage de l’hôte, celle que la machine utilise pour se joindre elle-même.

Utilisez un environnement d’exercice isolé. Dans les versions de Docker Engine antérieures à 28.0.0, d’autres machines du même segment réseau local peuvent, dans certains cas, accéder aux ports publiés sur localhost. [Publication des ports dans Docker](https://docs.docker.com/engine/network/port-publishing/)

:::single-choice{#docker-port-mapping-request-target} Dans `127.0.0.1:9090:80`, sur quel port un navigateur exécuté sur l’hôte Docker doit-il se connecter ?

::option[Le port 9090 de l’hôte.]{#docker-port-mapping-target-outer .correct explanation="La valeur du milieu indique le port de l’hôte auquel se connecte le navigateur."}
::option[Le port 80 de l’hôte.]{#docker-port-mapping-target-inner explanation="Le port 80 désigne la destination dans le conteneur."}
::option[Le port 9090 du conteneur.]{#docker-port-mapping-target-wrong-side explanation="Dans l’exemple, le serveur reçoit la requête sur le port 80 du conteneur."}
:::

## Tester depuis l’hôte

Ouvrez `http://127.0.0.1:8080` dans le navigateur de la machine sur laquelle Docker a publié le port. Si Docker tourne à distance, saisir `127.0.0.1` dans le navigateur de votre ordinateur portable vous ramène à cet ordinateur. Dans un environnement d’exercice accessible depuis le navigateur, utilisez le mode d’accès indiqué par cet environnement.

:::single-choice{#docker-port-mapping-local-browser} Docker a publié le port 8080 sur une autre machine d’exercice. À quoi correspond `127.0.0.1` si vous saisissez cette adresse sur votre ordinateur portable ?

::option[À l’autre machine d’exercice.]{#docker-port-mapping-local-lab explanation="Cette adresse désigne la machine d’exercice uniquement si vous l’utilisez depuis cette machine."}
::option[Au conteneur web dans Docker.]{#docker-port-mapping-local-container explanation="Le navigateur utilise l’adresse de sa propre machine. La redirection permet de transmettre la requête à un conteneur."}
::option[À votre ordinateur portable.]{#docker-port-mapping-local-laptop .correct explanation="L’adresse de bouclage désigne la machine sur laquelle tourne le navigateur."}
:::

## Voir quels ports Docker a publiés

La colonne `PORTS` de `docker ps` peut afficher la redirection. La flèche va de l’adresse et du port de l’hôte vers le port du conteneur. Le suffixe `/tcp` indique le protocole réseau utilisé.

```text
$ docker ps
STATUS         PORTS                   NAMES
Up 2 minutes   127.0.0.1:8080->80/tcp   published-web
```

Une ligne peut aussi afficher `80/tcp` tout seul. En l’absence d’adresse de l’hôte et de flèche, cette entrée n’affiche aucun port publié sur l’hôte.

![Terminal LabEx avec une redirection du port 8080 de l’hôte vers le port 80 du conteneur et une réponse HTTP 200](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-port-mapping/loopback-mapping.png)

Dans la capture, la liste a été filtrée pour ne garder que `published-web`. La requête avec `curl` part de l’hôte Docker et confirme que l’adresse publiée répond correctement.

:::single-choice{#docker-port-mapping-read-listing} Une ligne affiche `80/tcp` sans flèche. Qu’indique-t-elle ?

::option[Docker a publié le port 80 sur l’hôte.]{#docker-port-mapping-listing-host explanation="Une redirection publiée indiquerait un port de l’hôte et le port du conteneur vers lequel il pointe."}
::option[Un port du conteneur est indiqué, sans port publié sur l’hôte.]{#docker-port-mapping-listing-container .correct explanation="L’entrée nomme le port 80 du conteneur. Elle n’affiche ni adresse de l’hôte ni flèche de redirection."}
::option[Docker a publié le port 8080 sur l’hôte.]{#docker-port-mapping-listing-default explanation="L’entrée ne contient aucun port de l’hôte. Docker n’en déduit pas qu’il faut utiliser 8080."}
:::

## Choisir l’adresse à tester

Si la page ne s’ouvre pas, comparez l’adresse saisie avec le côté gauche de la redirection. L’état `Up` vous dit ce qui tourne. La flèche vous dit où arrivent les requêtes. Une requête depuis le navigateur vérifie si le serveur renvoie réellement la page.

:::single-choice{#docker-port-mapping-correct-misdirected} Depuis l’hôte Docker, vous essayez le port 8080, mais la page ne s’ouvre pas. La ligne affiche `127.0.0.1:8081->80/tcp`. Que devriez-vous essayer ensuite ?

::option[Ouvrir `http://127.0.0.1:80`.]{#docker-port-mapping-misdirected-80 explanation="Le port 80 se trouve du côté du conteneur."}
::option[Ouvrir `http://127.0.0.1:8081`.]{#docker-port-mapping-misdirected-8081 .correct explanation="Utilisez le port publié sur l’hôte, à gauche de la flèche."}
::option[Réessayer `http://127.0.0.1:8080`.]{#docker-port-mapping-misdirected-8080 explanation="Le port de l’hôte affiché est 8081. Une nouvelle requête sur 8080 ne vérifie pas cette redirection."}
:::

## Résumé

Vous savez maintenant lire une redirection de port et choisir la bonne adresse dans le navigateur.

1. Distinguer le port de l’hôte de celui du conteneur.
2. Expliquer à quoi correspond `127.0.0.1`.
3. Repérer un port publié dans la liste des conteneurs.
4. Tester le service en passant par le port publié sur l’hôte.
