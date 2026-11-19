---
lesson_id: "compose-services"
course_id: "docker-compose"
lang: "fr"
order_index: 2
title: "Services Compose"
description: "Apprenez à démarrer des services Compose et à vérifier l’état de leurs conteneurs."
meta_title: "Services Compose - Docker Compose"
meta_description: "Apprenez à démarrer des services Compose et à vérifier l’état de leurs conteneurs."
meta_keywords: "services Compose, état des conteneurs, Docker Compose, DevOps, Linux Journey"
---

Reprenez le fichier `compose.yaml` de la leçon précédente, avec `web` et `toolbox`. Les deux services appartiennent au même **projet** Compose, c’est-à-dire à l’ensemble des ressources gérées avec cette configuration. Exécutez les commandes depuis le dossier d’exercice.

## Démarrer le projet

Si le port 8080 est déjà utilisé, choisissez un port libre sur l’hôte dans `compose.yaml`. Par exemple, le conteneur `published-web` du cours Docker occupe le port 8080 tant qu’il tourne. Vous pouvez le laisser en marche et utiliser la correspondance `127.0.0.1:8081:80` dans Compose si le port 8081 est libre. Conservez le port 80 côté conteneur et utilisez le port choisi côté hôte pour les prochaines requêtes depuis le navigateur.

Utilisez `docker compose up -d` pour démarrer les services en arrière-plan. Compose crée les ressources dont le projet a besoin et utilise les réglages des services pour créer ou mettre à jour les conteneurs.

```bash
$ docker compose up -d
```

:::single-choice{#compose-services-project-start} Vous exécutez up -d depuis le dossier d’exercice. Qu’est-ce qui détermine les éléments démarrés ?

::option[Toutes les images disponibles sur l’hôte Docker.]{#compose-services-project-start-a explanation="L’hôte peut contenir des images qui n’ont aucun rapport avec ce projet."}
::option[Tous les conteneurs qui sont arrêtés.]{#compose-services-project-start-c explanation="Compose travaille sur le projet que vous lui demandez de démarrer."}
::option[Les services du fichier Compose sélectionné.]{#compose-services-project-start-b .correct explanation="Dans cet exemple, Compose applique les définitions de web et de toolbox."}
:::

## Lire la liste des services

Utilisez `docker compose ps` pour examiner ce projet. La colonne des services affiche leurs noms dans le fichier YAML. Docker donne aussi un nom à chaque conteneur, qui peut inclure le nom du projet.

```bash
$ docker compose ps
```

Repérez `web` et `toolbox` et regardez leur état. Un conteneur en cours d’exécution indique que le programme tourne au moment de la vérification. Faites une requête dans le navigateur pour vérifier séparément la réponse du serveur web.

:::single-choice{#compose-services-compose-list} Compose indique que web est en cours d’exécution. Comment vérifier directement qu’il renvoie la page attendue ?

::option[Compter les services affichés par config.]{#compose-services-compose-list-b explanation="Le nombre de services ne renseigne pas sur la réponse du serveur web."}
::option[Faire une requête à l’adresse web publiée.]{#compose-services-compose-list-a .correct explanation="La requête permet de voir la page réellement servie."}
::option[Regarder le nom d’un autre conteneur.]{#compose-services-compose-list-c explanation="Le nom identifie un conteneur sans vérifier la réponse du service."}
:::

![État de Compose indiquant que web et toolbox tournent et que le port 8080 est publié côté hôte](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-services/project-status.png)

La capture d’écran utilise le port initial de l’hôte, 8080. Si vous avez choisi un autre port, recherchez son numéro du côté hôte de la correspondance.

## Examiner un service arrêté

Le conteneur d’outils est temporaire. Si le délai d’attente se termine ou si vous l’arrêtez, ajoutez `-a` pour inclure les conteneurs arrêtés dans la liste Compose. La commande ci-dessous arrête le conteneur d’outils de ce projet d’exercice et laisse le service web tourner. Redémarrez le conteneur d’outils quand vous souhaitez poursuivre le cours.

```bash
$ docker compose stop toolbox
$ docker compose ps -a
$ docker compose start toolbox
```

:::single-choice{#compose-services-stopped-service} Où chercher toolbox après l’avoir arrêté ?

::option[Dans la sortie de docker compose ps -a pour ce projet.]{#compose-services-stopped-service-c .correct explanation="Cette option inclut aussi les conteneurs arrêtés du projet."}
::option[Uniquement dans la liste des images.]{#compose-services-stopped-service-a explanation="Même si son programme est arrêté, le conteneur reste disponible pour inspection."}
::option[Dans la liste des conteneurs d’un autre projet.]{#compose-services-stopped-service-b explanation="Toolbox appartient à ce projet."}
:::

Pour pratiquer encore les conteneurs et Compose, consultez les [exercices sur les commandes Docker](https://labex.io/courses/docker-command-labs).

## Résumé

Vous savez maintenant démarrer et examiner un groupe de services à partir d’un fichier Compose.

1. Démarrez les services du projet sélectionné.
2. Repérez le nom du service et son état actuel.
3. Incluez les services arrêtés lorsque vous examinez le projet.
