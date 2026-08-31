---
lesson_id: "move-mv-command"
course_id: "command-line"
lang: "fr"
order_index: 11
title: "mv (Déplacer)"
description: "Apprenez à renommer et déplacer des fichiers ou répertoires sans provoquer d'écrasements involontaires."
meta_title: "mv (Déplacer) - Ligne de commande"
meta_description: "Apprenez la commande Linux mv avec des exemples pour déplacer des fichiers, renommer des fichiers et des répertoires, déplacer plusieurs fichiers et éviter les écrasements."
meta_keywords: "commande linux mv, commande mv, déplacer fichiers linux, renommer fichier linux, renommer répertoire linux, mv -i, mv -n, mv -t"
---

La commande `mv` renomme un fichier ou un répertoire, ou le déplace vers un autre emplacement. Contrairement à `cp`, elle ne laisse pas le chemin d'origine en place après un déplacement réussi.

Sa syntaxe élémentaire est :

```bash
mv [OPTIONS] SOURCE DESTINATION
```

## Renommer des fichiers et des répertoires

Pour renommer un élément, placez son chemin actuel en premier et son nouveau chemin en second.

Pour un fichier :

```bash
$ mv oldfile newfile
```

Le même ordre renomme un répertoire :

```bash
$ mv old_directory_name new_directory_name
```

:::single-choice{#rename-file-with-mv}
Quelle commande renomme `cat` en `dog` dans le répertoire actuel ?

::option[`mv cat dog`]{#rename-cat .correct explanation="`mv` traite `cat` comme le chemin source et `dog` comme son nouveau chemin de destination."}
::option[`mv dog cat`]{#rename-dog explanation="L'ordre des opérandes est inversé ; cette commande tenterait de renommer un `dog` existant en `cat`."}
::option[`cp cat dog`]{#copy-cat explanation="`cp` créerait une copie nommée `dog` tout en conservant `cat` ; elle n'effectuerait pas le renommage demandé."}
:::

## Déplacer des éléments vers un répertoire

Lorsque le dernier opérande est un répertoire existant, `mv` y place la source :

```bash
$ mv file2 /home/pete/Documents
```

Pour déplacer plusieurs sources, énumérez-les puis placez le répertoire cible en dernier :

```bash
$ mv file_1 file_2 somedirectory/
```

GNU `mv` fournit aussi `-t` pour placer le répertoire cible avant les sources :

```bash
$ mv -t somedirectory/ file_1 file_2
```

Contrairement à `cp`, `mv` ne nécessite pas d'option récursive pour un répertoire.

:::single-choice{#move-multiple-files}
Quelle commande déplace `file_1` et `file_2` dans le répertoire existant `archive/` ?

::option[`mv archive/ file_1 file_2`]{#target-first-without-option explanation="Sans l'option GNU `-t`, un déplacement à plusieurs sources attend le répertoire cible en dernier. Cet ordre n'est pas la forme standard."}
::option[`mv -r file_1 file_2 archive/`]{#recursive-move explanation="`mv` n'utilise pas `-r` pour déplacer des fichiers ou répertoires ; la forme normale à plusieurs sources suffit."}
::option[`mv file_1 file_2 archive/`]{#target-last .correct explanation="Avec plusieurs sources, le répertoire cible existant est le dernier opérande et reçoit les deux fichiers."}
:::

## Contrôler les destinations existantes

Par défaut, `mv` peut remplacer une destination existante. Inspectez les chemins source et destination, puis choisissez si nécessaire une politique d'écrasement :

- `-i` : demander une confirmation avant de remplacer une destination ;

  ```bash
  $ mv -i source_file destination_directory
  ```

- `-n` : ne pas écraser une destination existante ;

  ```bash
  $ mv -n source_file destination_directory
  ```

- `-b` : sous GNU/Linux, sauvegarder une destination qui serait remplacée ; le suffixe par défaut est généralement `~` ;

  ```bash
  $ mv -b file1 directory_with_file1
  ```

- `-v` : afficher chaque déplacement à mesure qu'il se produit.

```bash
$ mv -v file1 file2 somedirectory/
```

:::single-choice{#move-without-overwriting}
Quelle commande déplace `draft.txt` dans `finished/` uniquement si elle n'écrase pas une destination existante ?

::option[`mv -i draft.txt finished/`]{#interactive-draft explanation="`-i` demande quoi faire lorsqu'une destination existe ; un écrasement reste possible si l'utilisateur le confirme."}
::option[`mv -b draft.txt finished/`]{#backup-draft explanation="`-b` permet le remplacement en conservant une sauvegarde de l'ancienne destination ; elle n'empêche pas l'écrasement."}
::option[`mv -n draft.txt finished/`]{#no-clobber-draft .correct explanation="`-n` ignore un déplacement qui écraserait une destination existante."}
:::

## Déplacer des répertoires et des correspondances de jokers

Un répertoire se déplace sans `-r` :

```bash
$ mv project /home/pete/Documents/
```

Les jokers du shell peuvent sélectionner plusieurs sources :

```bash
$ ls *.txt
$ mv *.txt notes/
```

Prévisualiser les correspondances avec `ls` permet de repérer un motif trop large avant de changer plusieurs chemins.

:::single-choice{#move-directory-without-recursion}
Quelle commande déplace le répertoire `project/` dans `/srv/archive/` ?

::option[`mv -r project/ /srv/archive/`]{#recursive-project explanation="`mv` n'a pas besoin de `-r` et ne l'utilise pas dans ce but. Les répertoires sont gérés par le déplacement ordinaire."}
::option[`mv project/ /srv/archive/`]{#move-project .correct explanation="La syntaxe ordinaire de `mv` déplace un répertoire vers une cible existante sans option récursive."}
::option[`cp project/ /srv/archive/`]{#copy-project explanation="Un simple `cp` ne déplace pas le répertoire et nécessiterait une option récursive pour le copier ; l'original resterait aussi en place."}
:::

:::single-choice{#preview-text-file-move}
Vous prévoyez d'exécuter `mv *.txt notes/`. Quelle commande prévisualise les chemins sélectionnés par le même joker ?

::option[`ls '*.txt'`]{#literal-text-pattern explanation="Les guillemets empêchent le shell de développer `*` ; cette commande cherche donc un nom littéral avec un astérisque."}
::option[`ls *.txt`]{#list-text-matches .correct explanation="Le shell développe `*.txt` pour `ls` comme pour `mv`, ce qui permet d'examiner d'abord les noms non cachés sélectionnés."}
::option[`mv -v *.txt notes/`]{#verbose-text-move explanation="Le mode détaillé rapporte les déplacements pendant leur exécution ; il réalise l'opération au lieu de fournir une prévisualisation en lecture seule."}
:::

Pour vous exercer, essayez les laboratoires **[Commande Linux mv : déplacer et renommer](https://labex.io/fr/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** et **[Organiser des fichiers et répertoires](https://labex.io/fr/labs/linux-organizing-files-and-directories-387877)**.

## Résumé

Vous savez maintenant renommer et déplacer des fichiers ou répertoires tout en protégeant les destinations existantes.

1. Placer la source avant son nouveau chemin.
2. Placer le répertoire cible après plusieurs sources.
3. Demander, ignorer ou sauvegarder avant de remplacer une destination.
4. Déplacer des répertoires sans option récursive.
5. Prévisualiser les jokers avant un déplacement en masse.
