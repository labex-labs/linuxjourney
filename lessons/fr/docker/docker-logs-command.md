---
lesson_id: "docker-logs-command"
course_id: "docker"
lang: "fr"
order_index: 6
title: "docker logs"
description: "Apprenez à lire la sortie recueillie pour un conteneur et à l’utiliser pour orienter le diagnostic."
meta_title: "docker logs - Docker"
meta_description: "Consultez les journaux des conteneurs en cours d’exécution ou arrêtés, ciblez la sortie récente et distinguez une erreur du programme de l’état du conteneur."
meta_keywords: "docker logs, journaux de conteneurs, dépannage Docker, erreurs de démarrage, dernières lignes"
---

Un conteneur nommé `preview` s’est arrêté. La liste des conteneurs affiche son état et son code de sortie. Pour savoir ce que le programme a signalé, consultez la sortie que Docker a recueillie pour ce conteneur.

## Choisir un conteneur

Indiquez le nom du conteneur à `docker logs`. La commande peut lire une sortie conservée même si le conteneur est arrêté, pourvu qu’il existe encore. Dans cet exemple, une tâche courte a tenté de lire un fichier à l’emplacement `/site/title.txt` avant de s’arrêter.

```text
$ docker logs preview
cat: can't open '/site/title.txt': No such file or directory
```

Ici, `cat` est le programme qui a tenté de lire le fichier. Le message indique le chemin que le programme n’a pas trouvé dans le conteneur.

:::single-choice{#docker-logs-command-read-exited} Preview et report utilisent la même image. Quelle commande lit la sortie de preview ?

::option[`docker logs report`]{#docker-logs-command-exited-report explanation="Le nom sélectionne le conteneur. Report désigne une autre exécution."}
::option[`docker logs busybox:1.36`]{#docker-logs-command-exited-image explanation="Il s’agit de la référence de l’image. Les journaux appartiennent à un conteneur créé à partir de cette image."}
::option[`docker logs preview`]{#docker-logs-command-exited-preview .correct explanation="La commande indique le nom du conteneur dont vous voulez lire la sortie."}
:::

## Lire le message dans son contexte

Les journaux contiennent les messages écrits par le programme. Un message de démarrage peut vous dire que le programme a commencé à écouter les requêtes. Une erreur peut indiquer l’opération qu’il n’a pas pu terminer. L’exemple signale un chemin introuvable dans `preview`. Vérifiez si le fichier devait se trouver exactement à cet emplacement. Le message vous indique par où commencer.

:::single-choice{#docker-logs-command-error-boundary} Que permet d’affirmer le message sur le fichier manquant ?

::option[Le fichier est absent de tous les dossiers de l’hôte.]{#docker-logs-command-error-host-path explanation="Le programme a cherché un chemin dans le conteneur. Son message ne décrit pas les fichiers de tout l’hôte."}
::option[Le programme n’a pas trouvé le fichier indiqué dans preview.]{#docker-logs-command-error-container-path .correct explanation="La sortie décrit le résultat de la recherche du programme qui s’est exécuté dans preview."}
::option[Le navigateur de l’hôte a utilisé un port qui n’était pas publié.]{#docker-logs-command-error-network explanation="Le message concerne une recherche de fichier. Le port du navigateur n’est pas indiqué."}
:::

## Regarder la sortie récente

Lorsqu’un conteneur produit beaucoup de lignes, utilisez `--tail` suivi d’un nombre. Docker renvoie au maximum ce nombre de lignes en partant de la fin de la sortie. Commencez avec quelques lignes, puis affichez-en davantage si le premier message d’erreur se trouve plus haut.

```bash
$ docker logs --tail 5 web
```

![Terminal LabEx affichant l’erreur de fichier manquant dans preview et les cinq dernières lignes de web](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-logs-command/preview-and-tail.png)

Ces deux commandes consultent des conteneurs différents. Dans l’exemple LabEx, `preview` signale le fichier manquant et `web` indique que Nginx a démarré.

:::single-choice{#docker-logs-command-tail-choice} Vous voulez seulement les deux dernières lignes disponibles de web. Quelle commande convient ?

::option[`docker logs --tail 2 web`]{#docker-logs-command-tail-two .correct explanation="Tail 2 demande au plus deux lignes à la fin de la sortie du conteneur."}
::option[`docker logs --tail 5 web`]{#docker-logs-command-tail-five explanation="Cette commande demande au plus cinq lignes et peut donc en afficher plus de deux."}
::option[`docker logs web`]{#docker-logs-command-tail-unlimited explanation="En l’absence de limite, Docker peut afficher toutes les lignes disponibles."}
:::

## Que faire quand la sortie est vide ?

Docker ne peut afficher que la sortie qu’il a recueillie. Une commande peut s’exécuter sans rien afficher. Un programme peut aussi écrire ses messages dans un fichier dont Docker ne recueille pas le contenu. Si `docker logs` réussit sans rien afficher, utilisez `docker ps -a` pour consulter l’état du conteneur. Une sortie vide seule ne permet pas de déterminer cet état.

:::single-choice{#docker-logs-command-empty-result} La tâche cleanup n’a pas de journal. Comment savoir si elle continue de tourner ou si elle s’est arrêtée ?

::option[Demander plus de lignes à Docker pour cleanup.]{#docker-logs-command-empty-more-lines explanation="Changer le nombre de lignes ne révèle pas si un programme sans sortie s’est arrêté."}
::option[Chercher l’image utilisée pour démarrer cleanup.]{#docker-logs-command-empty-image explanation="L’image désigne les fichiers et réglages de départ. L’état se lit dans la liste des conteneurs."}
::option[Lire l’état de cleanup dans la liste complète des conteneurs.]{#docker-logs-command-empty-container-state .correct explanation="La liste complète inclut les conteneurs qui tournent et ceux qui existent encore après leur arrêt."}
:::

## Résumé

Vous savez maintenant utiliser la sortie d’un conteneur pour décider quoi vérifier ensuite.

1. Lire la sortie recueillie pour un conteneur par son nom, même s’il est arrêté.
2. Utiliser un message du programme pour localiser le problème qu’il signale.
3. Limiter la sortie avec `--tail`.
4. Effectuer une autre vérification si les journaux laissent une question ouverte.
