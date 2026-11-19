---
lesson_id: "compose-volumes"
course_id: "docker-compose"
lang: "fr"
order_index: 4
title: "Volumes"
description: "Découvrez comment un volume nommé conserve les fichiers après le remplacement d’un conteneur."
meta_title: "Volumes - Docker Compose"
meta_description: "Découvrez comment un volume nommé conserve les fichiers après le remplacement d’un conteneur."
meta_keywords: "volumes nommés, stockage persistant, Docker Compose, DevOps, Linux Journey"
---

Un conteneur peut écrire des fichiers dans sa propre couche accessible en écriture. Lorsque vous supprimez le conteneur, Docker supprime aussi cette couche. Un **volume nommé** est un espace de stockage que Docker gère séparément. Vous pouvez le monter dans un autre conteneur.

## Définir un volume pour l’exercice

Enregistrez cet exemple à part sous le nom `compose.volume.yaml` dans le dossier d’exercice. L’exemple monte l’espace de stockage nommé `notes` au chemin `/data` dans le conteneur d’outils. La section `volumes` en bas du fichier déclare le volume nommé.

```yaml
services:
  toolbox:
    image: busybox:1.36
    volumes:
      - notes:/data
volumes:
  notes:
```

La définition du service précise où monter le volume dans le conteneur. La déclaration de premier niveau indique à Compose de gérer ce volume avec le projet.

:::single-choice{#compose-volumes-attached-path} Quel chemin du conteneur d’outils utilise le volume nommé ?

::option[/notes.]{#compose-volumes-attached-path-b explanation="Notes est le nom du volume. Le chemin de montage dans le conteneur se trouve après les deux-points."}
::option[/data.]{#compose-volumes-attached-path-a .correct explanation="La partie droite de notes:/data indique le chemin dans le conteneur."}
::option[Tous les chemins du conteneur.]{#compose-volumes-attached-path-c explanation="Le volume est monté au seul emplacement indiqué dans la configuration."}
:::

## Écrire puis lire avec deux conteneurs distincts

L’option `-f` sélectionne l’autre fichier, et `-p` lui attribue un nom de projet distinct. La commande `run --rm` crée un conteneur pour un seul lancement et le supprime à la fin. Exécutez les commandes dans le dossier d’exercice isolé. La première écrase le fichier de test `/data/note.txt`.

```bash
$ docker compose -p journey-volume -f compose.volume.yaml run --rm toolbox sh -c 'echo ready > /data/note.txt'
$ docker compose -p journey-volume -f compose.volume.yaml run --rm toolbox cat /data/note.txt
```

Le deuxième conteneur devrait afficher `ready`. Il monte le même volume que le premier.

:::single-choice{#compose-volumes-persistence} Comment le deuxième conteneur peut-il lire le fichier alors que le premier a été supprimé ?

::option[Les deux conteneurs ont monté le même volume nommé.]{#compose-volumes-persistence-b .correct explanation="Le fichier a été écrit dans l’espace de stockage séparé monté sous /data."}
::option[Les deux conteneurs ont conservé la couche accessible en écriture du premier.]{#compose-volumes-persistence-a explanation="Cette couche a été supprimée avec le premier conteneur."}
::option[BusyBox a automatiquement ajouté le fichier à son image.]{#compose-volumes-persistence-c explanation="L’exécution d’un conteneur laisse l’image d’origine intacte."}
:::

![Deux conteneurs d’outils distincts écrivent puis lisent le même fichier dans un volume nommé](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-volumes/persisted-note.png)

## Choisir les données à conserver

Un fichier comme `/tmp/note.txt` se trouve en dehors du répertoire monté. Il reste lié au conteneur, sauf si un autre stockage est monté à cet emplacement. Vérifiez les chemins avant de supposer qu’un fichier sera conservé. Supprimer le volume peut effacer ses données. Une sauvegarde est une copie distincte qui permet de restaurer les données si le volume est perdu.

:::single-choice{#compose-volumes-inside-mount} À quel fichier le prochain conteneur d’outils pourra-t-il accéder via ce volume ?

::option[À /tmp/note.txt, dans la couche accessible en écriture du premier conteneur.]{#compose-volumes-inside-mount-a explanation="Ce chemin se trouve en dehors du point de montage configuré."}
::option[À un fichier stocké dans un volume portant un autre nom.]{#compose-volumes-inside-mount-b explanation="Le nouveau conteneur doit monter cet autre volume pour accéder au fichier."}
::option[À /data/note.txt, écrit par le premier conteneur.]{#compose-volumes-inside-mount-c .correct explanation="Le montage sur /data permet à chaque conteneur d’accéder au même fichier."}
:::

## Résumé

Vous savez maintenant expliquer pourquoi un fichier peut rester disponible après la disparition du conteneur qui l’a écrit.

1. Repérez le nom du volume et le chemin de montage.
2. Vérifiez que le fichier est conservé en le lisant depuis un autre conteneur.
3. Distinguez le remplacement d’un conteneur de la suppression d’un volume.
