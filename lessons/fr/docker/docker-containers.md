---
lesson_id: "docker-containers"
course_id: "docker"
lang: "fr"
order_index: 1
title: "Conteneurs"
description: "Découvrez ce qui s’exécute dans un conteneur Docker et comment celui-ci utilise la machine qui héberge Docker."
meta_title: "Conteneurs - Docker"
meta_description: "Découvrez les conteneurs à travers l’exemple d’un petit serveur web et observez ce qui change quand son programme principal démarre ou s’arrête."
meta_keywords: "conteneurs Docker, bases des conteneurs, hôte Docker, processus, serveur web"
---

Un navigateur affiche une page fournie par un serveur web qui tourne dans Docker. Où ce serveur s’exécute-t-il ? Que se passe-t-il si on l’arrête ? Pour le comprendre, partons du programme qui répond au navigateur.

## Un programme dans un conteneur

Un **serveur web** est un programme qui répond aux demandes de pages. Imaginez que votre navigateur et un petit serveur web nommé `web` se trouvent sur la même machine. Docker exécute le serveur dans un **conteneur**, qui donne au programme sa propre vue des fichiers et des autres ressources. Les exemples sont déjà préparés : vous pouvez suivre ce cours sans installer Docker.

:::single-choice{#docker-containers-page-request} Quand le navigateur demande une page, qu’est-ce qui lui envoie son contenu ?

::option[Le serveur web qui tourne dans le conteneur.]{#docker-containers-page-server .correct explanation="Le programme serveur reçoit la requête et renvoie la page."}
::option[Les fichiers qui décrivent le démarrage du conteneur.]{#docker-containers-page-files explanation="Ces fichiers servent à configurer l’environnement. C’est un programme en cours d’exécution qui répond à la requête."}
::option[La liste des conteneurs Docker sur la machine.]{#docker-containers-page-list explanation="Cette liste indique ce que Docker exécute. Elle ne fournit pas la page web."}
:::

## Le conteneur et son hôte

La machine qui exécute les conteneurs est appelée **hôte**. Lorsque Docker exécute des conteneurs Linux sous Linux, les programmes tournent sous forme de processus sur cet hôte Linux. Un **processus** est un programme en cours d’exécution. Même si plusieurs conteneurs partagent le même hôte, chacun accède à un ensemble limité de ressources. Avec Docker Desktop, les conteneurs Linux s’exécutent dans une machine virtuelle Linux gérée par Docker.

:::single-choice{#docker-containers-shared-host} Deux conteneurs Linux s’exécutent sur le même hôte Linux. Qu’est-ce que cela implique ?

::option[Leurs programmes voient forcément les mêmes fichiers.]{#docker-containers-host-shared-files explanation="Chaque conteneur peut avoir sa propre vue des fichiers sur le même hôte."}
::option[Leurs programmes peuvent s’exécuter dans des processus distincts sur cet hôte.]{#docker-containers-host-separate-processes .correct explanation="Un même hôte peut exécuter plusieurs programmes dans des conteneurs indépendants."}
::option[Chaque conteneur doit démarrer une machine Linux distincte.]{#docker-containers-host-separate-machines explanation="Les conteneurs Linux peuvent tourner sous forme de processus sur un même hôte, sans démarrer une machine par conteneur."}
:::

## Partir d’une image

Docker crée un conteneur à partir d’une **image** qui regroupe le programme et les fichiers dont il a besoin. La même image de serveur web peut servir à créer `web` et `demo`. Au démarrage, chaque conteneur exécute le même programme serveur dans un processus distinct. Vous pouvez arrêter l’un ou l’autre séparément.

:::single-choice{#docker-containers-two-from-image} Vous arrêtez demo alors que web est encore en cours d’exécution. Que se passe-t-il pour web ?

::option[Il se met en pause jusqu’au redémarrage de demo.]{#docker-containers-two-paused explanation="Chaque conteneur exécute son propre programme. Dans cet exemple, l’arrêt de demo n’interrompt pas web."}
::option[Il faut le recréer à partir de l’image.]{#docker-containers-two-recreate explanation="Le conteneur web a été créé séparément et peut continuer à tourner."}
::option[Il continue de tourner dans son propre conteneur.]{#docker-containers-two-independent .correct explanation="Les deux conteneurs partent de la même image, mais s’exécutent indépendamment."}
:::

## Vérifier le service avant et après son arrêt

Supposons que le navigateur puisse déjà envoyer des requêtes à `web`. Avant l’arrêt du conteneur, le navigateur reçoit la page. Après l’arrêt, une nouvelle requête n’obtient plus de page de ce serveur. L’image reste disponible pour créer un autre conteneur. Le serveur doit être en cours d’exécution et le navigateur doit pouvoir le joindre. Une autre leçon expliquera comment relier le navigateur à un conteneur.

:::single-choice{#docker-containers-stopped-server} L’image est toujours disponible, mais web est arrêté. Que faut-il pour que web lui-même réponde de nouveau ?

::option[Son programme serveur doit être relancé.]{#docker-containers-stopped-program .correct explanation="L’image fournit les fichiers. Il faut un serveur en cours d’exécution pour traiter les nouvelles requêtes."}
::option[L’image doit changer de nom pour pouvoir fournir des pages.]{#docker-containers-stopped-rename explanation="Renommer l’image ne redémarre pas un serveur arrêté."}
::option[Le navigateur a besoin d’une autre copie de l’image.]{#docker-containers-stopped-browser-image explanation="Le navigateur envoie les requêtes. Le programme serveur s’exécute dans le conteneur."}
:::

![Terminal LabEx affichant une réponse HTTP 200 avant l’arrêt du conteneur et un échec de connexion ensuite](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-containers/server-response.png)

Dans cet exemple LabEx, le conteneur `page-demo` fournit la page. La première requête avec `curl` reçoit une réponse HTTP 200. Après l’arrêt du conteneur, une nouvelle requête échoue. Curl affiche `000` car il n’a reçu aucune réponse HTTP.

## Résumé

Vous savez maintenant expliquer comment un conteneur exécute un programme sur un hôte.

1. Identifier le programme qui répond à une requête du navigateur.
2. Expliquer comment plusieurs conteneurs peuvent partager un hôte.
3. Décrire comment une même image peut servir à créer plusieurs conteneurs.
4. Envoyer une nouvelle requête pour vérifier si un serveur jusque-là joignable répond toujours.
