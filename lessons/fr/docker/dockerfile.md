---
lesson_id: "dockerfile"
course_id: "docker"
lang: "fr"
order_index: 7
title: "Dockerfile"
description: "Apprenez comment un Dockerfile assemble une page et une image de base pour créer une image de serveur web réutilisable."
meta_title: "Dockerfile - Docker"
meta_description: "Lisez FROM, COPY et CMD dans un petit Dockerfile et distinguez la construction d’une image du démarrage d’un conteneur."
meta_keywords: "Dockerfile, construction d’image Docker, FROM, COPY, CMD, contexte de construction"
---

Vous avez déjà démarré un conteneur à partir d’une image de serveur web. Pour servir votre propre page, vous pouvez créer une image qui la contient déjà. Un **Dockerfile** est un fichier texte qui précise les étapes de construction de cette image.

## Partir d’une image de base

Une **image de base** fournit les fichiers et les programmes de départ. Le Dockerfile suivant part de l’image Nginx, ajoute une page et définit la commande par défaut du conteneur. Placez le Dockerfile et un fichier nommé `index.html` dans le même dossier d’exercice. Une seule ligne telle que `<h1>Hello from Docker</h1>` suffit pour la page.

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
CMD ["nginx", "-g", "daemon off;"]
```

`FROM nginx:alpine` prend pour point de départ l’image indiquée, qui contient déjà le programme Nginx. Docker s’en sert pour construire la nouvelle image.

:::single-choice{#dockerfile-base-image-purpose} Quelle ligne fournit Nginx avant que votre page ne soit ajoutée ?

::option[`COPY index.html /usr/share/nginx/html/index.html`]{#dockerfile-base-image-copy explanation="COPY ajoute la page et s’appuie sur le serveur fourni par l’image de base."}
::option[`FROM nginx:alpine`]{#dockerfile-base-image-from .correct explanation="FROM sélectionne l’image de départ, qui contient déjà le serveur."}
::option[La ligne qui commence par `CMD`.]{#dockerfile-base-image-cmd explanation="CMD fixe la commande par défaut au démarrage. Le programme du serveur vient de l’image de base."}
:::

## Ajouter un fichier

`COPY` lit `index.html` parmi les fichiers fournis pour la construction. Il copie la page au chemin indiqué à droite, l’emplacement depuis lequel cette version de l’image Nginx sert sa page par défaut. Si vous modifiez ensuite la page locale, reconstruisez l’image pour y inclure la modification.

:::single-choice{#dockerfile-copy-after-edit} Après la construction, vous avez modifié le titre dans le fichier index.html local. Comment inclure cette modification dans une nouvelle image ?

::option[Démarrer un autre conteneur depuis l’image existante.]{#dockerfile-copy-edit-run explanation="Ce conteneur démarrera avec la page déjà incluse dans l’image."}
::option[Changer uniquement le nom du conteneur existant.]{#dockerfile-copy-edit-rename explanation="Le nom d’un conteneur ne change pas les fichiers contenus dans l’image."}
::option[Reconstruire l’image avec la page mise à jour.]{#dockerfile-copy-edit-rebuild .correct explanation="Pendant la construction, COPY lit le fichier local à jour et l’inclut dans la nouvelle image."}
:::

## Définir la commande de démarrage

`CMD` fixe la commande par défaut d’un nouveau conteneur. Dans cet exemple, Nginx reste au premier plan à l’intérieur du conteneur. Avec `docker run -d`, Docker peut tout de même lancer le conteneur en arrière-plan par rapport à votre terminal.

:::single-choice{#dockerfile-cmd-start-time} À quel moment la commande CMD de l’exemple est-elle utilisée ?

::option[Quand un conteneur démarre avec sa commande par défaut.]{#dockerfile-cmd-when-start .correct explanation="Docker utilise la commande par défaut de l’image au démarrage du conteneur."}
::option[Pendant que Docker copie la page dans l’image.]{#dockerfile-cmd-when-copy explanation="COPY ajoute la page lors de la construction. Il ne démarre pas le serveur."}
::option[Quand Docker finit d’écrire l’image.]{#dockerfile-cmd-when-build explanation="La construction enregistre la commande de démarrage pour plus tard."}
:::

## Construire l’image et lancer le conteneur

Lancez la construction depuis le dossier qui contient les deux fichiers. L’option `-t` donne à l’image la référence `journey-web:1`. Le point final indique à Docker d’utiliser le dossier courant comme source des fichiers de construction.

```bash
$ docker build -t journey-web:1 .
$ docker run -d --name custom-web -p 127.0.0.1:8082:80 journey-web:1
```

La deuxième commande démarre un conteneur. Si le port 8082 est libre, ouvrez `http://127.0.0.1:8082` dans le navigateur de l’hôte Docker pour voir votre page.

:::single-choice{#dockerfile-build-versus-run} La construction a réussi, mais vous n’avez pas encore exécuté la deuxième commande. Qu’est-ce qui est prêt ?

::option[L’image existe et peut servir à créer un conteneur.]{#dockerfile-build-ready-image .correct explanation="La construction a produit l’image. La commande suivante démarrera un conteneur à partir de cette image."}
::option[Le conteneur nommé sert déjà votre page.]{#dockerfile-build-ready-container explanation="Le serveur démarre quand vous lancez un conteneur à partir de l’image."}
::option[Docker a déjà publié le port du navigateur pour l’image.]{#dockerfile-build-ready-port explanation="La redirection de port est une option de docker run. La construction ne crée pas cette connexion."}
:::

![Terminal LabEx affichant la construction de l’image, le démarrage du conteneur et la réponse HTML de la page personnalisée](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/dockerfile/build-and-run.png)

La dernière requête récupère la page intégrée dans l’image pendant la construction. Les messages de progression et les identifiants d’images peuvent varier selon l’environnement.

## Résumé

Vous savez maintenant lire un petit Dockerfile et suivre le chemin d’une page locale jusqu’à son serveur en cours d’exécution.

1. Repérer l’image de base dans `FROM`.
2. Décrire où `COPY` lit et écrit un fichier.
3. Reconnaître `CMD` comme la commande par défaut du conteneur.
4. Construire une image, puis en démarrer un conteneur.
