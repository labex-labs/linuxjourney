---
lesson_id: "docker-images"
course_id: "docker"
lang: "fr"
order_index: 2
title: "Images"
description: "Apprenez à lire une référence d’image et à vérifier si l’image correspondante est disponible localement."
meta_title: "Images - Docker"
meta_description: "Lisez les noms et les tags des images Docker, découvrez les registres et le téléchargement, puis distinguez les listes d’images et de conteneurs."
meta_keywords: "images Docker, tags d’images, registre d’images, docker pull, docker image ls"
---

Une image Docker regroupe un programme, ses fichiers et ses réglages par défaut. Docker utilise ce paquet pour créer un conteneur. Dans cette leçon, vous allez lire des noms d’images et repérer celles dont Docker dispose déjà.

## Lire le nom et le tag d’une image

Dans `nginx:alpine`, `nginx` est le nom de l’image et `alpine` est le **tag**, une étiquette qui permet de choisir une version ou une variante. Ici, elle désigne la variante basée sur Alpine Linux. Les deux-points séparent le nom du tag. `nginx:alpine` et `nginx:latest` sont deux références distinctes au même nom d’image.

:::single-choice{#docker-images-read-reference} Dans `busybox:1.36`, quelle partie correspond au tag ?

::option[`busybox`]{#docker-images-reference-name explanation="BusyBox est le nom qui précède les deux-points."}
::option[`busybox:1.36`]{#docker-images-reference-whole explanation="La référence complète contient le nom et le tag de l’image."}
::option[`1.36`]{#docker-images-reference-tag .correct explanation="Le texte après les deux-points est le tag qui sert à sélectionner l’image."}
:::

## Choisir un tag

Si vous omettez le tag dans une référence comme `nginx`, Docker utilise `latest`. C’est un nom par convention. La personne qui publie l’image choisit celle que le tag désigne et peut modifier ce choix par la suite. En écrivant `nginx:alpine`, vous indiquez la variante voulue. L’image associée à ce tag peut aussi être mise à jour.

:::single-choice{#docker-images-default-tag} Quelqu’un utilise `nginx` sans tag et suppose que Docker a choisi la version la plus récente. Qu’a réellement sélectionné cette référence ?

::option[L’image désignée par le tag latest.]{#docker-images-default-latest .correct explanation="En l’absence de tag, Docker utilise latest. L’image associée est choisie par la personne qui la publie."}
::option[L’image Nginx publiée le plus récemment.]{#docker-images-default-newest explanation="Docker utilise un tag nommé latest. Il ne classe pas les images par date de publication."}
::option[La plus petite image Nginx disponible.]{#docker-images-default-smallest explanation="La taille ne détermine pas le tag par défaut. Indiquez la variante souhaitée par son nom."}
:::

## Télécharger une image

Un **registre** stocke les images et permet de les télécharger. Pour une référence comme `nginx:alpine`, Docker consulte Docker Hub par défaut. La commande `docker pull` télécharge l’image dans l’environnement Docker auquel vous êtes connecté. On appelle aussi cette opération un **pull**.

```bash
$ docker pull nginx:alpine
```

Si la commande réussit, l’image est disponible dans cet environnement. Vous pourrez démarrer un conteneur dans un second temps. Dans les exemples de terminal, le `$` est l’invite de commande.

:::single-choice{#docker-images-pull-result} Le téléchargement d’une image s’est terminé correctement. Qu’a fait Docker ?

::option[Il a démarré un conteneur qui répond aux requêtes web.]{#docker-images-pull-started explanation="Un conteneur démarre quand vous le lancez. Le téléchargement prépare seulement l’image."}
::option[Il a rendu l’image disponible dans cet environnement.]{#docker-images-pull-available .correct explanation="Vous pouvez maintenant partir de cette image pour créer un conteneur."}
::option[Il a envoyé une copie de l’image au registre.]{#docker-images-pull-uploaded explanation="Le pull transfère l’image du registre vers le stockage local de Docker."}
:::

## Vérifier les images locales

La commande `docker image ls` affiche les images déjà disponibles. Cet exemple ne montre que le nom et le tag. Docker intitule la colonne des noms d’images `REPOSITORY`.

```text
$ docker image ls
REPOSITORY   TAG
nginx        alpine
busybox      1.36
```

La première ligne affiche `nginx:alpine`. Ce tableau indique les images présentes. L’état d’un éventuel conteneur créé à partir de ces images figure dans une autre liste.

![Terminal LabEx affichant docker pull et les colonnes REPOSITORY et TAG de docker image ls](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-images/pull-and-list.png)

Dans cette capture, la liste est filtrée pour n’afficher que les deux références utilisées dans la leçon.

:::single-choice{#docker-images-local-list} Quelle référence est disponible d’après cette sortie ?

::option[`busybox:latest`]{#docker-images-local-busybox-latest explanation="La ligne busybox indique le tag 1.36. L’exemple n’affiche aucune ligne busybox avec le tag latest."}
::option[`busybox:1.36`]{#docker-images-local-busybox .correct explanation="Associez busybox dans la colonne REPOSITORY à 1.36 dans la colonne TAG."}
::option[`nginx:1.36`]{#docker-images-local-nginx-mixed explanation="Prenez le nom et le tag sur une même ligne. Ici, 1.36 appartient à la ligne busybox."}
:::

## Résumé

Vous savez maintenant lire une référence d’image et vérifier si elle figure dans la liste locale.

1. Identifier le nom et le tag d’une image.
2. Expliquer ce qui se passe lorsqu’on omet le tag.
3. Utiliser `docker pull` pour télécharger une image depuis un registre.
4. Lire le nom et le tag dans la sortie de `docker image ls`.
