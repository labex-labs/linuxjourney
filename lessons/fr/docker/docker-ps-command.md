---
lesson_id: "docker-ps-command"
course_id: "docker"
lang: "fr"
order_index: 4
title: "docker ps"
description: "Apprenez à lister les conteneurs Docker et à distinguer ceux qui tournent de ceux qui se sont arrêtés."
meta_title: "docker ps - Docker"
meta_description: "Lisez la sortie de docker ps, retrouvez les conteneurs arrêtés avec docker ps -a et interprétez leurs noms et leurs codes de sortie."
meta_keywords: "docker ps, liste de conteneurs Docker, conteneurs arrêtés, docker ps -a, état du conteneur, code de sortie"
---

Le serveur web que vous avez démarré dans Docker tourne-t-il toujours ? Vérifiez avec `docker ps`. Une image Docker contient le programme et les fichiers dont il a besoin. Un conteneur est une instance créée à partir de cette image. La commande affiche la liste des conteneurs au moment où vous l’exécutez.

## Lister les conteneurs qui tournent

Par défaut, `docker ps` liste les conteneurs en cours d’exécution. Les exemples montrent quelques colonnes d’un environnement Docker préparé. Vous pouvez les lire sans installer Docker. Dans le terminal, tapez la commande qui suit l’invite `$`.

```text
$ docker ps
IMAGE         STATUS         NAMES
nginx:alpine  Up 4 minutes   web
nginx:alpine  Up 30 seconds  demo
```

Si Docker n’affiche que les en-têtes de colonnes, la liste des conteneurs en cours d’exécution est vide. L’environnement peut encore contenir des conteneurs arrêtés.

:::single-choice{#docker-ps-running-list} Après `docker ps`, Docker n’affiche que les en-têtes de colonnes. Que pouvez-vous en déduire ?

::option[Aucune image n’est disponible pour démarrer un conteneur.]{#docker-ps-running-list-images explanation="La commande liste des conteneurs. Des images peuvent être disponibles même quand aucun conteneur ne tourne."}
::option[La liste ne contient aucun conteneur en cours d’exécution.]{#docker-ps-running-list-empty .correct explanation="La liste par défaut affiche les conteneurs qui tournent. Il peut rester des conteneurs arrêtés."}
::option[Il n’y a aucun conteneur arrêté à inspecter.]{#docker-ps-running-list-stopped explanation="Les conteneurs arrêtés ne figurent pas dans la sélection par défaut. Ce résultat ne dit pas s’il y en a."}
:::

## Lire les noms et les états

Commencez par chercher le conteneur dans la colonne `NAMES`. Les deux lignes affichent la même image, `nginx:alpine`, dans la colonne `IMAGE`. Repérez `web` à droite, puis lisez `STATUS` sur la même ligne. `Up 4 minutes` signifie que ce conteneur tourne depuis environ quatre minutes.

:::single-choice{#docker-ps-name-column} Quelle ligne correspond à un conteneur qui tourne depuis une trentaine de secondes ?

::option[La ligne nommée `demo`.]{#docker-ps-name-demo .correct explanation="Repérez Up 30 seconds sous STATUS, puis suivez la ligne jusqu’à demo sous NAMES."}
::option[La ligne nommée `web`.]{#docker-ps-name-web explanation="La ligne de web indique Up 4 minutes. Les deux conteneurs utilisent la même image, mais ont démarré à des moments différents."}
::option[Les deux lignes portant l’image `nginx:alpine`.]{#docker-ps-name-image-reference explanation="Chaque ligne a son propre état. Une image commune n’implique pas une heure de démarrage commune."}
:::

## Inclure les conteneurs arrêtés

Si un conteneur attendu ne figure pas dans la liste, essayez `docker ps -a`. L’option `-a` est la forme courte de `--all`. Elle inclut les conteneurs qui se sont arrêtés mais existent encore. L’exemple présente aussi une tâche préparée nommée `preview`.

```text
$ docker ps -a
IMAGE         STATUS                         NAMES
nginx:alpine  Up 4 minutes                   web
nginx:alpine  Up 30 seconds                  demo
busybox:1.36  Exited (0) 2 minutes ago       report
busybox:1.36  Exited (1) About a minute ago  preview
```

Un conteneur exécute un programme principal, par exemple un serveur web ou un script. `Exited` signifie que ce programme s’est arrêté. Le nombre entre parenthèses est son **code de sortie**, le résultat indiqué en fin d’exécution. Zéro indique généralement une réussite et une autre valeur signale le plus souvent une erreur. La tâche `report` affiche `Exited (0)`, ce qui est normal pour une tâche terminée avec succès.

![Terminal LabEx montrant des conteneurs en cours d’exécution et arrêtés, report avec le code de sortie 0 et preview avec le code 1](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-ps-command/running-and-exited.png)

La capture LabEx n’affiche que les noms et les états des quatre conteneurs de l’exemple. Les durées varient selon le moment où la commande est exécutée.

:::single-choice{#docker-ps-exit-code-reading} Sur quelle ligne chercheriez-vous une erreur, d’après le code de sortie ?

::option[`report`, parce que la tâche est terminée.]{#docker-ps-exit-code-report explanation="Une tâche courte peut s’arrêter normalement une fois terminée. Un code de sortie nul indique en général un succès."}
::option[`demo`, parce que ce conteneur est le dernier à avoir démarré.]{#docker-ps-exit-code-demo explanation="Up indique depuis combien de temps le programme tourne. Cette ligne ne donne aucun code de sortie."}
::option[`preview`, parce que la tâche s’est terminée avec le code 1.]{#docker-ps-exit-code-preview .correct explanation="Preview affiche Exited (1). Cela justifie de chercher une erreur, même si cet état n’en donne pas la cause."}
:::

## Choisir la prochaine vérification

Le code de sortie vous aide à savoir quoi regarder. Pour vérifier si `preview` a écrit un message d’erreur, donnez son nom à `docker logs`. La commande affiche la sortie que Docker a recueillie pour ce conteneur.

```bash
$ docker logs preview
```

Si un serveur web tourne, vous pouvez aussi vérifier qu’un visiteur arrive à ouvrir sa page. Ouvrez-la depuis la machine qui doit y accéder. `Up` décrit l’état du programme dans le conteneur. Une requête réussie du navigateur confirme que la page est accessible depuis la machine de test.

:::single-choice{#docker-ps-check-visitor-access} La page s’ouvre sur la machine qui exécute Docker. Une autre personne doit l’ouvrir depuis son poste. Quel test vous permettra de savoir si elle y accède ?

::option[Ouvrir la page depuis le poste de cette personne.]{#docker-ps-next-check-visitor-browser .correct explanation="Cette requête emprunte la connexion qu’elle utilisera réellement."}
::option[Relancer `docker ps` sur la machine qui exécute Docker.]{#docker-ps-next-check-status-again explanation="La liste peut confirmer que web tourne encore. Pour vérifier l’accès depuis l’autre poste, il faut y lancer une requête."}
::option[Ouvrir de nouveau la page sur la machine qui exécute Docker.]{#docker-ps-next-check-host-browser explanation="Cela répète le test depuis la première machine. La connexion de l’autre poste peut fonctionner différemment."}
:::

## Résumé

Vous savez maintenant utiliser la liste des conteneurs pour en trouver un, lire son état et choisir quoi vérifier ensuite.

1. Utiliser `docker ps` pour lister les conteneurs qui tournent.
2. Retrouver un conteneur par son nom et lire son état.
3. Utiliser `docker ps -a` pour inclure les conteneurs arrêtés.
4. Consulter les journaux ou envoyer une requête avec le navigateur quand l’état ne suffit pas.
