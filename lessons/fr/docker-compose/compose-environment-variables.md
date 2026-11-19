---
lesson_id: "compose-environment-variables"
course_id: "docker-compose"
lang: "fr"
order_index: 5
title: "Variables d’environnement"
description: "Apprenez à distinguer une valeur insérée dans un fichier Compose d’une valeur transmise à un conteneur."
meta_title: "Variables d’environnement - Docker Compose"
meta_description: "Apprenez à distinguer une valeur insérée dans un fichier Compose d’une valeur transmise à un conteneur."
meta_keywords: "variables d’environnement, interpolation, Docker Compose, DevOps, Linux Journey"
---

Une variable d’environnement est une valeur nommée qu’un programme peut lire. Compose peut s’en servir de deux façons : pour insérer une valeur à la lecture du fichier et pour transmettre une valeur à un programme dans un conteneur.

## Insérer une valeur dans le fichier

Enregistrez cet exemple sous le nom `compose.env.yaml` dans le dossier d’exercice. L’expression `${PAGE_MODE:-demo}` indique d’utiliser la valeur de `PAGE_MODE` si la variable est définie et non vide. Sinon, Compose utilise `demo`.

```yaml
services:
  toolbox:
    image: busybox:1.36
    environment:
      PAGE_MODE: "${PAGE_MODE:-demo}"
```

Compose résout l’expression avant de créer le conteneur. C’est ce qu’on appelle l’**interpolation**. Vous pourrez rencontrer la même technique dans d’autres fichiers pour choisir un port de l’hôte ou une étiquette d’image.

:::single-choice{#compose-environment-variables-interpolate-default} Si PAGE_MODE n’est pas définie, quelle valeur apparaît dans la configuration affichée ?

::option[L’expression telle qu’elle est écrite dans le fichier.]{#compose-environment-variables-interpolate-default-a explanation="Compose résout l’expression lorsqu’il lit le fichier."}
::option[Un nom de conteneur généré automatiquement.]{#compose-environment-variables-interpolate-default-c explanation="Le nom du conteneur et la valeur d’environnement sont deux réglages distincts."}
::option[Demo, la valeur après l’opérateur de valeur par défaut.]{#compose-environment-variables-interpolate-default-b .correct explanation="L’expression indique demo comme valeur de repli."}
:::

## Afficher la valeur retenue

Une affectation placée avant une commande définit la variable pour cette seule exécution. Utilisez cette syntaxe pour voir l’effet d’une autre valeur. La commande `config` affiche les réglages après interpolation sans créer de conteneur.

```bash
$ PAGE_MODE=review docker compose -p journey-env -f compose.env.yaml config
```

Repérez `PAGE_MODE: review` dans l’environnement du service. La valeur `review` sert à l’exercice. Évitez d’inclure des secrets dans les exemples de configuration ou dans les sorties affichées.

:::single-choice{#compose-environment-variables-config-scope} La configuration affichée contient review. Que s’est-il passé jusqu’ici ?

::option[Un service a déjà démarré avec cette valeur.]{#compose-environment-variables-config-scope-b explanation="Afficher la configuration et démarrer un conteneur sont deux opérations distinctes."}
::option[Compose a inséré la valeur en lisant la configuration.]{#compose-environment-variables-config-scope-a .correct explanation="La commande config montre les réglages après interpolation, avant tout démarrage."}
::option[Tous les conteneurs existants utilisent maintenant cette valeur.]{#compose-environment-variables-config-scope-c explanation="Cette exécution ne modifie pas les conteneurs en cours d’exécution."}
:::

## Transmettre une valeur au conteneur

La section `environment` transmet la valeur retenue à un nouveau conteneur. Utilisez `printenv` pour afficher cette valeur depuis le conteneur créé pour l’occasion.

```bash
$ PAGE_MODE=review docker compose -p journey-env -f compose.env.yaml run --rm toolbox printenv PAGE_MODE
```

Vous devriez obtenir `review`. L’interpolation a déterminé la valeur et l’entrée d’environnement l’a transmise au conteneur. Une variable qui sert uniquement à choisir un port de l’hôte ne devient pas automatiquement une variable d’environnement du programme.

:::single-choice{#compose-environment-variables-actual-value} Que faire pour vérifier la valeur reçue par le programme dans le conteneur d’outils ?

::option[Afficher PAGE_MODE depuis le conteneur.]{#compose-environment-variables-actual-value-c .correct explanation="L’environnement du programme permet de constater la valeur qu’il a réellement reçue."}
::option[Lire uniquement la valeur par défaut dans le fichier initial.]{#compose-environment-variables-actual-value-a explanation="Une autre valeur peut remplacer celle du fichier."}
::option[Chercher l’adresse IP du conteneur d’outils.]{#compose-environment-variables-actual-value-b explanation="L’adresse ne renseigne pas sur les réglages du programme."}
:::

## Résumé

Vous savez maintenant distinguer les deux usages des variables d’environnement.

1. Lisez une expression avec une valeur par défaut dans un fichier Compose.
2. Vérifiez la configuration après interpolation, avant de démarrer un conteneur.
3. Vérifiez une valeur dans l’environnement du programme en cours d’exécution.
