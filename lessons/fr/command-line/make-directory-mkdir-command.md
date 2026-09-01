---
lesson_id: "make-directory-mkdir-command"
course_id: "command-line"
lang: "fr"
order_index: 12
title: "mkdir (Créer un répertoire)"
description: "Apprenez à créer des répertoires uniques, multiples ou imbriqués avec les options de mkdir."
meta_title: "mkdir (Créer un répertoire) - Ligne de commande"
meta_description: "Apprenez la commande Linux mkdir avec des exemples pour créer un répertoire, plusieurs répertoires, des répertoires parents imbriqués et définir les permissions."
meta_keywords: "commande mkdir, linux mkdir, créer répertoire linux, faire répertoire linux, mkdir -p, mkdir -m, créer dossier linux"
---

La commande `mkdir`, abréviation de « make directory », crée des répertoires pour organiser des fichiers et d'autres répertoires.

Sa syntaxe élémentaire est :

```bash
mkdir [OPTIONS] DIRECTORY...
```

## Créer un répertoire

Fournissez un chemin pour créer un répertoire. Cet exemple crée `documents` dans le répertoire de travail actuel :

```bash
$ mkdir documents
```

Si une entrée nommée `documents` existe déjà, `mkdir` signale une erreur au lieu de la remplacer. Utilisez `ls -ld documents` pour examiner l'entrée existante.

:::single-choice{#create-one-directory} Quelle commande crée un répertoire nommé `documents` dans le répertoire de travail actuel ?

::option[`mkdir documents`]{#mkdir-documents .correct explanation="`mkdir` crée le répertoire demandé au chemin relatif `documents`."}
::option[`touch documents`]{#touch-documents explanation="`touch` crée un fichier ordinaire vide lorsque le chemin manque ; elle ne crée pas de répertoire."}
::option[`cd documents`]{#cd-documents explanation="`cd` tente d'ouvrir un répertoire existant ; elle ne crée pas un répertoire absent."}
:::

## Créer plusieurs répertoires

Énumérez plusieurs chemins pour créer plusieurs répertoires en une commande :

```bash
$ mkdir books paintings
```

:::single-choice{#create-separate-directories} Quelle commande crée deux répertoires frères nommés `books` et `paintings` ?

::option[`mkdir books/paintings`]{#nested-paintings explanation="Ce chemin décrit `paintings` à l'intérieur de `books`, pas deux répertoires frères. Il échoue aussi si `books` est absent."}
::option[`mkdir "books paintings"`]{#spaced-directory explanation="Les guillemets réunissent les mots en un chemin ; cette commande demande donc un seul répertoire dont le nom contient un espace."}
::option[`mkdir books paintings`]{#two-directories .correct explanation="Deux opérandes distincts demandent à `mkdir` de créer `books` et `paintings` comme deux répertoires."}
:::

## Créer les répertoires parents manquants

Sans option, `mkdir books/hemingway/favorites` échoue si un répertoire intermédiaire manque. Ajoutez `-p` pour créer les parents absents le long du chemin :

```bash
$ mkdir -p books/hemingway/favorites
```

Cette commande crée les parties manquantes. Elle ne signale pas non plus d'erreur pour la seule raison que le répertoire final existe déjà, même si d'autres erreurs, comme des permissions insuffisantes, restent possibles.

:::single-choice{#create-nested-path} Aucune partie de `projects/app/src` n'existe encore. Quelle commande crée le chemin complet ?

::option[`mkdir -p projects/app/src`]{#mkdir-parents .correct explanation="L'option `-p` crée chaque répertoire parent manquant avant le répertoire final."}
::option[`mkdir projects/app/src`]{#mkdir-no-parents explanation="Sans `-p`, `mkdir` ne peut pas créer `src` lorsque les répertoires intermédiaires n'existent pas."}
::option[`mkdir -m projects/app/src`]{#mkdir-mode-missing explanation="L'option `-m` exige un mode et ne demande pas la création des parents manquants."}
:::

## Définir le mode initial

Utilisez `-m MODE` pour préciser les permissions d'un nouveau répertoire :

```bash
$ mkdir -m 755 public
```

Vous étudierez les modes de permission plus tard. Ici, le mode `755` donne au propriétaire les permissions de lecture, d'écriture et de traversée, tandis que le groupe et les autres reçoivent celles de lecture et de traversée.

Ajoutez `-v` pour afficher un message à chaque création :

```bash
$ mkdir -pv projects/app/src
mkdir: created directory 'projects'
mkdir: created directory 'projects/app'
mkdir: created directory 'projects/app/src'
```

:::single-choice{#set-directory-mode} Quelle commande crée `public` avec le mode de permission `755` ?

::option[`mkdir -p 755 public`]{#parents-755 explanation="L'option `-p` traite les mots restants comme des chemins de répertoires ; elle ne définit donc pas `755` comme mode."}
::option[`mkdir -v 755 public`]{#verbose-755 explanation="L'option `-v` affiche les messages de création ; elle n'interprète pas `755` comme un mode."}
::option[`mkdir -m 755 public`]{#mode-public .correct explanation="L'option `-m` reçoit le mode demandé et `public` est le chemin du répertoire à créer."}
:::

Pour vous exercer, essayez les laboratoires **[Commande Linux mkdir : créer des répertoires](https://labex.io/fr/labs/linux-linux-mkdir-command-directory-creating-209739)** et **[Créer la structure d'un nouveau projet](https://labex.io/fr/labs/linux-setting-up-a-new-project-structure-387859)**.

## Résumé

Vous savez maintenant créer des structures de répertoires avec des noms, parents et modes choisis.

1. Créer un ou plusieurs répertoires avec une seule commande.
2. Reconnaître une erreur provoquée par un chemin existant.
3. Construire les répertoires parents manquants avec `-p`.
4. Définir le mode d'un nouveau répertoire avec `-m`.
