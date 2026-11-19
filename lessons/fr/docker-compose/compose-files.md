---
lesson_id: "compose-files"
course_id: "docker-compose"
lang: "fr"
order_index: 1
title: "Fichiers Compose"
description: "Apprenez à repérer les services, les images, les commandes et les ports dans un fichier Compose."
meta_title: "Fichiers Compose - Docker Compose"
meta_description: "Apprenez à repérer les services, les images, les commandes et les ports dans un fichier Compose."
meta_keywords: "fichier Compose, services, Docker Compose, DevOps, Linux Journey"
---

Vous pouvez lancer un serveur web et son outil auxiliaire avec deux commandes distinctes. Un **fichier Compose** regroupe les réglages pour vous permettre de redémarrer les mêmes services par la suite. Ce cours utilise Docker avec le module Compose, qui fournit la commande `docker compose`.

## Définir deux services

Créez un dossier d’exercice nommé `journey-compose` et enregistrez-y l’exemple sous le nom `compose.yaml`. Un **service** décrit comment Compose doit exécuter un conteneur. Ce fichier définit un serveur web et un petit conteneur d’outils, qui reste actif pour les vérifications suivantes.

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "127.0.0.1:8080:80"
  toolbox:
    image: busybox:1.36
    command: ["sleep", "3600"]
```

Utilisez des espaces pour l’indentation. Les clés indentées sous `web` appartiennent à ce service. Le tiret sous `ports` introduit un élément de liste. Les crochets de `command` forment aussi une liste. Elle contient ici le nom du programme et son argument.

:::single-choice{#compose-files-service-images} Quel service utilise l’image BusyBox ?

::option[Le service web.]{#compose-files-service-images-a explanation="L’image indiquée pour web est nginx."}
::option[Le service toolbox.]{#compose-files-service-images-c .correct explanation="Le champ image de toolbox indique busybox:1.36."}
::option[Les deux services.]{#compose-files-service-images-b explanation="Chaque service définit sa propre image."}
:::

## Lire la définition du service web

Le service web publie le port 80 du conteneur sur le port 8080 de l’hôte. Sur la machine qui exécute Docker, une requête vers `http://127.0.0.1:8080` peut atteindre Nginx une fois le service démarré. Le conteneur d’outils ne publie aucun port. Sa commande `sleep` le maintient en cours d’exécution pendant 3 600 secondes pour l’exercice.

:::single-choice{#compose-files-mapping-owner} Quel réglage détermine comment un navigateur sur l’hôte Docker accède à Nginx ?

::option[Le réglage ports sous web.]{#compose-files-mapping-owner-a .correct explanation="Il associe l’adresse et le port de l’hôte au conteneur web."}
::option[L’étiquette de l’image sous toolbox.]{#compose-files-mapping-owner-b explanation="Elle sélectionne l’image du conteneur d’outils."}
::option[L’argument de sleep sous toolbox.]{#compose-files-mapping-owner-c explanation="Cet argument fixe la durée d’exécution du programme."}
:::

## Vérifier la configuration interprétée

Exécutez la commande depuis le dossier qui contient le fichier. Saisissez ce qui se trouve après le symbole d’invite `$`. Compose lit `compose.yaml` et affiche la configuration telle qu’il l’interprète. Repérez les entrées `web` et `toolbox`. Certains réglages abrégés peuvent apparaître sous une forme plus détaillée.

```bash
$ docker compose config
```

:::single-choice{#compose-files-config-scope} La commande affiche deux services sans erreur. Qu’avez-vous vérifié ?

::option[Les deux conteneurs ont démarré.]{#compose-files-config-scope-a explanation="Cette commande lit et affiche les réglages."}
::option[Le navigateur a reçu une réponse valide.]{#compose-files-config-scope-c explanation="Vous pourrez tester une requête après le démarrage du serveur."}
::option[Compose sait lire les deux définitions de service.]{#compose-files-config-scope-b .correct explanation="Vous pouvez examiner la configuration interprétée avant le démarrage."}
:::

## Résumé

Vous savez maintenant repérer les éléments d’un fichier Compose simple.

1. Repérez les noms des services et les références à leurs images dans services.
2. Associez les réglages d’un service au conteneur qu’ils décrivent.
3. Examinez la configuration interprétée avec docker compose config.
