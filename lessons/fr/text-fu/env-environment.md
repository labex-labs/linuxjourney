---
lesson_id: "env-environment"
course_id: "text-fu"
lang: "fr"
order_index: 5
title: "env (environnement)"
description: "Découvrez comment Bash développe, exporte, inspecte et remplace temporairement des variables d'environnement."
meta_title: "env (environnement) - Text-Fu"
meta_description: "Découvrez la commande env et les variables d'environnement Linux comme PATH, HOME et USER."
meta_keywords: "env, commande env Linux, variables d'environnement, PATH, HOME, USER, variables shell"
---

Chaque processus possède un environnement : un ensemble de chaînes nom-valeur hérité de son parent. Les shells transmettent ainsi aux programmes des réglages comme la langue ou les chemins de recherche des exécutables.

## Développer la valeur des variables dans Bash

Bash remplace `$NAME` ou `${NAME}` par sa valeur avant d'exécuter une commande. Citez le développement pour préserver la valeur en un seul argument :

```bash
$ printf '%s\n' "$HOME"
/home/pete
```

Variables courantes :

- `HOME` : chemin du répertoire personnel.
- `USER` : nom d'utilisateur fourni par l'environnement de connexion sur de nombreux systèmes.
- `PWD` : répertoire de travail du shell.
- `PATH` : répertoires où rechercher les commandes.

Les valeurs dépendent du processus courant. Une variable absente devient une chaîne vide, sauf mode shell plus strict.

:::single-choice{#env-print-home-value} Quelle commande Bash affiche `HOME` tout en préservant sa valeur comme un seul argument ?

::option[`printf '%s\n' '$HOME'`]{#env-literal-home explanation="Les apostrophes empêchent le développement et affichent littéralement `$HOME`."}
::option[`printf '%s\n' "$HOME"`]{#env-quoted-home .correct explanation="Bash développe `$HOME` entre guillemets et `printf` reçoit toute la valeur comme un argument."}
::option[`printf '%s\n' HOME`]{#env-name-home explanation="Sans dollar, `HOME` est du texte ordinaire."}
:::

## Inspecter l'environnement courant

Sans opérande, `env` affiche l'environnement hérité :

```bash
$ env
```

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

L'environnement peut contenir identifiants, jetons ou chemins internes. Relisez et masquez sa sortie avant de la publier.

:::single-choice{#env-list-exported-values} Quelle commande affiche l'environnement visible par un nouveau processus ?

::option[`env`]{#env-print-all .correct explanation="Sans commande ni affectation, `env` affiche les noms et valeurs reçus."}
::option[`alias`]{#env-alias-list explanation="`alias` liste l'état interne des alias du shell."}
::option[`history`]{#env-history-list explanation="`history` affiche les commandes mémorisées."}
:::

## Trouver les commandes grâce à PATH

`PATH` est une liste de répertoires séparés par des deux-points, consultée quand une commande ne contient aucune barre oblique :

```bash
$ printf '%s\n' "$PATH"
```

L'ordre compte. `type -a NAME` montre comment le shell résout un nom. Pour ajouter un répertoire en tête tout en gardant le chemin existant :

```bash
$ export PATH="/opt/coolapp/bin:$PATH"
```

Ne remplacez pas accidentellement tout `PATH` et n'ajoutez pas de répertoire non fiable accessible en écriture.

:::single-choice{#env-prepend-path-directory} Quelle commande ajoute `/opt/coolapp/bin` avant le `PATH` existant pour Bash et ses futurs enfants ?

::option[`export PATH="/opt/coolapp/bin"`]{#env-replace-path explanation="Cette forme supprime tous les répertoires existants."}
::option[`export PATH="/opt/coolapp/bin:$PATH"`]{#env-export-path .correct explanation="Elle place le nouveau répertoire en tête, conserve l'ancienne valeur et exporte le résultat."}
::option[`PATH='$PATH:/opt/coolapp/bin'`]{#env-literal-path explanation="Les apostrophes gardent littéralement `$PATH` et l'affectation n'est pas exportée."}
:::

## Exporter une variable vers les processus enfants

Les variables Bash ne font pas automatiquement partie de l'environnement des enfants. Utilisez `export` :

```bash
$ export TEST=test
```

Le shell courant possède désormais la variable `TEST`, et ses futures commandes en héritent :

```bash
$ printenv TEST
test
```

Les futures commandes héritent de `TEST=test`, mais un enfant ne peut pas modifier ainsi l'environnement de son parent. L'affectation dure jusqu'à `unset` ou la fin du shell et n'est pas globale au système.

:::single-choice{#env-export-inheritance} Quel est l'effet principal de `export TEST=test` dans Bash ?

::option[Écrire `TEST` dans la configuration de tous les utilisateurs.]{#env-system-wide explanation="L'affectation ne concerne que le shell courant et ses enfants."}
::option[Marquer `TEST=test` pour l'héritage par les futurs enfants.]{#env-child-inheritance .correct explanation="`export` ajoute la variable à l'environnement transmis aux commandes lancées."}
::option[Modifier l'environnement des processus déjà actifs.]{#env-existing-processes explanation="Les processus existants gardent leur propre environnement."}
:::

## Définir une valeur pour une seule commande

Placez les affectations avant la commande :

```bash
$ LANG=C sort names.txt
```

La commande `env` offre une forme explicite équivalente :

```bash
$ env LANG=C sort names.txt
```

La valeur de `LANG` dans le shell courant ne change pas durablement. `env -i COMMAND` démarre avec un environnement initialement vide ; beaucoup de programmes dépendent toutefois de variables, utilisez-le avec discernement.

:::single-choice{#env-one-command-value} Quelle commande exécute `sort names.txt` avec `LANG=C` sans modifier durablement le shell courant ?

::option[`env LANG=C sort names.txt`]{#env-lang-sort .correct explanation="`env` ajoute la valeur à l'environnement de la commande, tandis que le parent conserve la sienne."}
::option[`export LANG=C; sort names.txt`]{#env-export-lang explanation="Cette forme laisse `LANG` modifiée dans le shell après `sort`."}
::option[`env -i sort names.txt`]{#env-empty-sort explanation="Cette forme vide l'environnement sans définir `LANG=C`."}
:::

## Charger des valeurs personnelles dans les sessions futures

Pour recréer une variable exportée dans les futures sessions Bash interactives, placez l'instruction dans le fichier réellement lu, souvent `~/.bashrc` :

```bash
export TEST=test
```

Zsh utilise souvent `~/.zshrc` et Fish une autre syntaxe. Les shells de connexion ou non interactifs peuvent lire d'autres fichiers : identifiez le shell et le type de session.

Pour vous exercer :

1. **[Gérer l'environnement et la configuration du shell sous Linux](https://labex.io/fr/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - Gérez variables locales, héritage et persistance dans `.bashrc`.
2. **[Variables d'environnement sous Linux](https://labex.io/fr/labs/linux-environment-variables-in-linux-385274)** - Créez et modifiez des variables d'environnement.

## Résumé

Vous savez désormais inspecter et contrôler l'environnement transmis par Bash.

1. Développer les valeurs avec des guillemets adaptés.
2. Examiner les valeurs exportées sans révéler de secrets.
3. Préserver et ordonner les répertoires de `PATH`.
4. Exporter une variable vers les futurs enfants.
5. Remplacer une valeur pour une seule commande.
