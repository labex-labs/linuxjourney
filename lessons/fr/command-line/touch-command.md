---
lesson_id: "touch-command"
course_id: "command-line"
lang: "fr"
order_index: 5
title: "touch"
description: "Apprenez à créer des fichiers vides et à gérer leurs horodatages avec la commande touch."
meta_title: "touch - Ligne de commande"
meta_description: "Apprenez la commande Linux touch avec des exemples pour créer des fichiers vides, mettre à jour les horodatages, définir des dates, utiliser des fichiers de référence et éviter les écrasements."
meta_keywords: "commande linux touch, commande touch, créer fichier linux, mettre à jour horodatage linux, touch -d, touch -r, touch -c"
---

La commande `touch` modifie les horodatages des fichiers. Elle sert aussi couramment à créer un ou plusieurs fichiers vides.

Sa syntaxe élémentaire est :

```bash
touch [OPTIONS] FILE...
```

## Créer des fichiers vides

Si le fichier indiqué n'existe pas, `touch` le crée vide :

```bash
$ touch mysuperduperfile
```

Vous pouvez créer plusieurs fichiers en une seule commande en énumérant leurs noms :

```bash
$ touch file1.txt file2.txt file3.log
```

Cette méthode est pratique pour créer des espaces réservés, mais `touch` n'ajoute aucun texte. Pour produire un fichier non vide, utilisez un éditeur ou une autre commande conçue pour écrire du contenu.

:::single-choice{#create-several-empty-files} Quelle commande crée trois fichiers vides nommés `one`, `two` et `three` s'ils n'existent pas déjà ?

::option[`touch "one two three"`]{#touch-one-spaced explanation="Les guillemets produisent un seul nom de fichier contenant des espaces. Cette commande ne désigne donc qu'un fichier."}
::option[`mkdir one two three`]{#mkdir-three explanation="`mkdir` crée des répertoires et non des fichiers ordinaires vides. Utilisez `touch` pour les fichiers demandés."}
::option[`touch one two three`]{#touch-three .correct explanation="`touch` accepte plusieurs fichiers comme opérandes et crée chacun de ceux qui manquent sans ajouter de contenu."}
:::

## Mettre à jour les horodatages

Les fichiers possèdent plusieurs horodatages. Par défaut, l'exécution de `touch` sur un fichier existant règle son heure d'accès et son heure de modification sur l'heure actuelle, sans changer son contenu.

Comparez l'heure de modification affichée avant et après la commande :

```bash
$ ls -l mysuperduperfile
$ touch mysuperduperfile
$ ls -l mysuperduperfile
```

La sortie de `ls -l` affiche normalement l'heure de modification, pas l'heure d'accès.

:::single-choice{#touch-existing-file} Que se passe-t-il avec `touch report.txt` si `report.txt` existe déjà ?

::option[Ses horodatages sont actualisés sans remplacer son contenu.]{#timestamps-only .correct explanation="Par défaut, `touch` met à jour les heures d'accès et de modification d'un fichier existant sans écraser ses données."}
::option[Son contenu est supprimé et le fichier devient vide.]{#contents-deleted explanation="La création d'un fichier vide ne concerne que les chemins absents. Un fichier existant conserve son contenu lorsque `touch` actualise ses horodatages."}
::option[La commande échoue parce que le nom de fichier est déjà utilisé.]{#existing-error explanation="`touch` est conçue pour agir sur des fichiers existants comme sur des fichiers absents. Un nom existant n'est pas en soi une erreur."}
:::

## Choisir l'horodatage à modifier

Utilisez `-a` pour ne changer que l'heure d'accès, ou `-m` pour ne changer que l'heure de modification :

```bash
$ touch -a notes.txt
$ touch -m notes.txt
```

:::single-choice{#change-modification-time-only} Quelle commande ne met à jour que l'heure de modification de `notes.txt` ?

::option[`touch -a notes.txt`]{#access-only explanation="L'option `-a` ne change que l'heure d'accès, pas l'heure de modification demandée."}
::option[`touch -m notes.txt`]{#modification-only .correct explanation="L'option `-m` limite le changement à l'heure de modification et laisse l'heure d'accès intacte."}
::option[`touch -c notes.txt`]{#no-create explanation="L'option `-c` contrôle la création d'un fichier absent ; elle ne limite pas la mise à jour à un horodatage."}
:::

## Définir ou copier une heure

L'option `-d` accepte une date au lieu d'utiliser l'heure actuelle :

```bash
$ touch -d "2026-06-23 12:30:00" mysuperduperfile
```

Pour donner à un fichier les mêmes heures d'accès et de modification qu'à un fichier de référence, utilisez `-r` :

```bash
$ touch -r file1.txt file2.txt
```

Ici, `file1.txt` fournit les horodatages et `file2.txt` est modifié. L'option `-t` permet aussi de fournir une heure sous une forme numérique compacte.

:::single-choice{#copy-reference-timestamps} Quelle commande copie les horodatages de `source.txt` vers `target.txt` ?

::option[`touch -r source.txt target.txt`]{#reference-source .correct explanation="Avec `-r`, l'opérande suivant est le fichier de référence et le dernier est celui dont les horodatages sont mis à jour."}
::option[`touch -r target.txt source.txt`]{#reference-target explanation="Cette commande inverse le rôle des fichiers : elle prendrait `target.txt` comme référence et modifierait `source.txt`."}
::option[`touch -d source.txt target.txt`]{#date-source explanation="L'option `-d` attend une date et non le nom d'un fichier de référence. Utilisez `-r` pour copier des horodatages."}
:::

## Éviter la création d'un fichier

Normalement, `touch` crée le fichier si le chemin indiqué n'existe pas. Ajoutez `-c` lorsque vous ne voulez mettre à jour qu'un fichier existant :

```bash
$ touch -c existing-file.txt
```

Si `existing-file.txt` est absent, cette commande ne le crée pas. Ce comportement est utile dans les scripts qui doivent actualiser un horodatage sans introduire de nouveau fichier.

:::single-choice{#update-without-creating} Quelle commande actualise `status.log` s'il existe, sans le créer s'il est absent ?

::option[`touch -a status.log`]{#touch-access explanation="L'option `-a` choisit l'heure d'accès, mais un fichier absent peut toujours être créé. Elle ne garantit pas l'absence de création."}
::option[`touch -m status.log`]{#touch-modification explanation="L'option `-m` choisit l'heure de modification, mais n'empêche pas la création d'un fichier absent. Utilisez `-c`."}
::option[`touch -c status.log`]{#touch-no-create .correct explanation="L'option `-c` empêche la création d'un fichier absent tout en permettant la mise à jour des horodatages d'un fichier existant."}
:::

## Résumé

Vous savez maintenant utiliser `touch` pour créer des fichiers vides et contrôler leurs horodatages.

1. Créer un ou plusieurs fichiers vides.
2. Actualiser les horodatages sans changer le contenu.
3. Choisir l'heure d'accès ou l'heure de modification.
4. Définir une heure précise ou copier les horodatages d'un fichier de référence.
5. Empêcher la création d'un fichier absent.
