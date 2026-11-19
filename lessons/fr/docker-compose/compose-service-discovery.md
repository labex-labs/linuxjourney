---
lesson_id: "compose-service-discovery"
course_id: "docker-compose"
lang: "fr"
order_index: 3
title: "Découverte de services"
description: "Découvrez comment les services Compose se joignent par leur nom et comment l’hôte y accède par un port publié."
meta_title: "Découverte de services - Docker Compose"
meta_description: "Découvrez comment les services Compose se joignent par leur nom et comment l’hôte y accède par un port publié."
meta_keywords: "découverte de services, réseau Compose, ports publiés, Docker Compose, DevOps, Linux Journey"
---

Un navigateur sur l’hôte Docker atteint le service web à son adresse publiée. Un autre conteneur du projet emprunte un chemin différent. En général, Compose relie tous les services d’un projet à un réseau commun sur lequel chacun est joignable par son nom.

## Demander la page depuis le conteneur d’outils

Revenez dans le dossier d’exercice qui contient `compose.yaml`. Si le conteneur d’outils s’est arrêté depuis la dernière leçon, redémarrez-le avec `docker compose start toolbox`. Lorsque les deux services tournent, utilisez `docker compose exec` pour exécuter une commande dans le conteneur d’outils existant. La commande `wget` de BusyBox demande une page. L’option `-q` masque les messages de progression, et `-O -` écrit le contenu de la page dans le terminal.

```bash
$ docker compose exec -T toolbox wget -q -O - http://web:80/
```

L’option `-T` désactive l’attribution d’un terminal interactif. L’URL indique le nom du service web et son port dans le conteneur. Si la requête aboutit, le code HTML de la page Nginx s’affiche.

:::single-choice{#compose-service-discovery-sibling-url} Quelle adresse un autre service du même réseau Compose doit-il utiliser pour atteindre le conteneur web ?

::option[http://web:80/]{#compose-service-discovery-sibling-url-c .correct explanation="Sur le réseau commun, web désigne le bon service, qui écoute sur le port 80."}
::option[http://127.0.0.1:8080/]{#compose-service-discovery-sibling-url-a explanation="Depuis cet autre service, l’adresse de bouclage renvoie à son propre environnement réseau."}
::option[http://web:8080/]{#compose-service-discovery-sibling-url-b explanation="Dans cet exemple, le serveur web écoute sur le port 80 à l’intérieur du réseau."}
:::

![Code HTML renvoyé dans le conteneur d’outils après une requête utilisant le nom du service web](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-service-discovery/internal-request.png)

## Choisir une adresse depuis l’hôte

Sur l’hôte Docker, ouvrez `http://127.0.0.1:8080/` si vous avez conservé la correspondance d’origine. Si vous avez modifié le port de l’hôte dans la leçon précédente, utilisez ce port dans le navigateur. Le conteneur d’outils utilise toujours `http://web:80/`, car il se connecte au sein du réseau Compose, où le nom de service `web` est disponible.

:::single-choice{#compose-service-discovery-host-url} Vous passez au port 8081 côté hôte. Quelle adresse de l’exemple doit changer elle aussi ?

::option[L’URL que le conteneur d’outils utilise pour joindre web sur le port 80.]{#compose-service-discovery-host-url-b explanation="Cette connexion atteint toujours directement le port du conteneur web."}
::option[Les deux adresses de l’exemple.]{#compose-service-discovery-host-url-c explanation="Seul le port côté hôte a changé."}
::option[L’adresse utilisée par le navigateur sur l’hôte.]{#compose-service-discovery-host-url-a .correct explanation="Le navigateur passe par le nouveau port publié sur l’hôte."}
:::

## Conserver un nom de service stable

Lorsqu’un conteneur est remplacé, son adresse réseau peut changer. Son nom de service Compose reste le même. Un client peut résoudre à nouveau ce nom et se reconnecter. Une connexion ouverte vers le conteneur remplacé peut se couper.

:::single-choice{#compose-service-discovery-replacement} Le conteneur web a été recréé et possède une adresse différente. Que peut utiliser le conteneur d’outils pour la prochaine requête ?

::option[L’ancienne adresse copiée depuis le conteneur.]{#compose-service-discovery-replacement-a explanation="Le nouveau conteneur peut recevoir une autre adresse réseau."}
::option[Le même nom de service web et le même port de conteneur.]{#compose-service-discovery-replacement-b .correct explanation="Le nom peut désigner le conteneur actuel sur le réseau du projet."}
::option[Le nom du conteneur d’outils lui-même.]{#compose-service-discovery-replacement-c explanation="Cet autre nom désigne le service qui envoie la requête."}
:::

## Résumé

Vous savez maintenant choisir une adresse en fonction de l’origine de la requête.

1. Sur le réseau du projet, utilisez le nom du service et le port du conteneur.
2. Dans le navigateur sur l’hôte, utilisez l’adresse publiée.
3. Résolvez à nouveau le nom du service après un remplacement de conteneur.
