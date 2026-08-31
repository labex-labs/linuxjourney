---
lesson_id: "remove-rm-command"
course_id: "command-line"
lang: "fr"
order_index: 13
title: "rm (Supprimer)"
description: "Apprenez à supprimer des fichiers et répertoires en vérifiant les cibles et en choisissant des options rm plus sûres."
meta_title: "rm (Supprimer) - Ligne de commande"
meta_description: "Apprenez la commande Linux rm avec des exemples sûrs pour supprimer des fichiers, enlever des répertoires, utiliser rm -r, rm -i, et éviter les erreurs avec rm -rf."
meta_keywords: "commande linux rm, commande rm, rm -r, rm -i, rm -f, rm -rf, supprimer fichiers linux, enlever répertoire linux, rmdir"
---

La commande `rm` supprime des entrées du système de fichiers. Une suppression en ligne de commande n'envoie normalement rien dans la corbeille du bureau et `rm` ne possède pas d'annulation intégrée : confirmez donc chaque cible avant l'exécution.

Sa syntaxe élémentaire est :

```bash
rm [OPTIONS] FILE...
```

## Supprimer des fichiers

Fournissez un ou plusieurs chemins de fichiers à `rm` :

```bash
$ rm file1
```

```bash
$ rm notes.txt old-report.txt draft.md
```

Vérifiez l'orthographe et l'emplacement avant d'appuyer sur Entrée. Une sauvegarde ou une copie sous contrôle de version offre une récupération plus fiable que les outils de restauration du système de fichiers après la suppression.

:::single-choice{#remove-one-file}
Après avoir confirmé la cible, quelle commande supprime le fichier `old-report.txt` ?

::option[`rm old-report.txt`]{#rm-report .correct explanation="`rm` supprime l'entrée de fichier indiquée. L'opération ne place normalement pas le fichier dans une corbeille."}
::option[`rmdir old-report.txt`]{#rmdir-report explanation="`rmdir` agit sur les répertoires vides, pas sur les fichiers ordinaires ; elle ne convient pas à cette cible."}
::option[`mv old-report.txt`]{#mv-report explanation="`mv` exige une destination et change un chemin au lieu de le supprimer. Cette commande incomplète ne réalise pas la suppression."}
:::

## Prévisualiser les cibles d'un joker

Le shell peut développer un joker en plusieurs opérandes. Par exemple, `*.tmp` sélectionne les noms non cachés correspondants du répertoire actuel :

```bash
$ rm *.tmp
```

Avant toute suppression, prévisualisez le même motif non cité avec `ls` :

```bash
$ ls *.tmp
cache.tmp  test.tmp
$ rm *.tmp
```

Le shell développe le motif avant le lancement de `rm`. Si la prévisualisation contient un fichier inattendu, corrigez le motif au lieu de poursuivre.

:::single-choice{#preview-removal-pattern}
Vous prévoyez de supprimer `*.tmp`. Quelle commande affiche d'abord, sans les supprimer, les chemins non cachés sélectionnés ?

::option[`rm -v *.tmp`]{#verbose-remove explanation="Le mode détaillé rapporte les suppressions à mesure qu'elles se produisent ; il supprime toujours les fichiers et n'est pas une prévisualisation en lecture seule."}
::option[`ls '*.tmp'`]{#quoted-pattern explanation="Les guillemets empêchent le développement du joker ; cette commande cherche donc un nom littéral contenant `*`."}
::option[`ls *.tmp`]{#list-temp-matches .correct explanation="Le shell développe `*.tmp` pour `ls`, ce qui permet d'examiner le même ensemble de correspondances non cachées avant la suppression."}
:::

## Demander une confirmation

L'option `-i` interroge avant chaque suppression :

```bash
$ rm -i important.txt
rm: remove regular file 'important.txt'? y
```

Avec GNU `rm`, `-I` est une protection moins intrusive : elle demande une confirmation unique si la commande doit supprimer plus de trois fichiers ou agir récursivement.

:::single-choice{#confirm-each-removal}
Quelle commande demande une confirmation avant de supprimer chaque fichier nommé ?

::option[`rm -i important.txt`]{#interactive-important .correct explanation="L'option `-i` demande confirmation avant chaque suppression, ce qui permet de refuser l'opération."}
::option[`rm -f important.txt`]{#force-important explanation="L'option `-f` supprime les demandes et ignore une cible absente ; elle retire la confirmation au lieu de l'ajouter."}
::option[`rm -v important.txt`]{#verbose-important explanation="L'option `-v` rapporte ce qui a été supprimé, mais ne demande pas d'autorisation préalable."}
:::

## Ignorer les fichiers absents avec -f

L'option `-f` ignore les opérandes absents et supprime les demandes :

```bash
$ rm -f old-cache.txt
```

Dans un script de nettoyage, elle peut rendre l'opération idempotente si un fichier généré est peut-être déjà absent. Comme elle désactive les confirmations, n'ajoutez pas `-f` uniquement pour faire taire une erreur que vous n'avez pas comprise.

## Supprimer des répertoires

`rm` sans option ne supprime pas un répertoire :

```bash
$ rm projects
rm: cannot remove 'projects': Is a directory
```

N'utilisez `-r` ou `-R` que pour supprimer volontairement une arborescence et tout son contenu :

```bash
$ rm -r old-project
```

Pour un répertoire vide, `rmdir` est une solution plus limitée :

```bash
$ rmdir empty-directory
```

`rmdir` échoue si le répertoire n'est pas vide, ce qui protège son contenu d'une suppression récursive.

:::single-choice{#remove-empty-directory-only}
Quelle commande supprime `old-cache/` uniquement si ce répertoire est vide ?

::option[`rm -r old-cache/`]{#recursive-cache explanation="`rm` récursif supprime le répertoire et son contenu ; il n'impose pas que le répertoire soit vide."}
::option[`rmdir old-cache/`]{#rmdir-cache .correct explanation="`rmdir` ne réussit que pour un répertoire vide et ne supprime donc pas récursivement les fichiers qu'il contient."}
::option[`rm -f old-cache/`]{#force-cache explanation="L'option `-f` ne permet pas à `rm` ordinaire de supprimer un répertoire et supprime des protections au lieu de vérifier qu'il est vide."}
:::

## Vérifier une suppression récursive

Une suppression récursive peut effacer une arborescence entière. Avec `-f`, elle supprime aussi les demandes ; `rm -rf` exige donc une validation particulièrement rigoureuse de la cible. Avant toute suppression récursive, vérifiez :

- votre emplacement avec `pwd` ;
- le chemin de premier niveau voulu avec `ls -ld -- TARGET` ;
- toute correspondance de joker avec une prévisualisation en lecture seule ;
- si le chemin est absolu ou relatif : `/tmp/cache` et `tmp/cache` diffèrent fortement ;
- l'absence d'espace accidentel : `rm -rf old-project` et `rm -rf old project` ciblent des chemins différents.

Placez `--` avant une cible susceptible de commencer par un tiret afin qu'elle ne soit pas interprétée comme une option :

```bash
$ rm -- -old-name
```

N'utilisez pas automatiquement `sudo` lorsque `rm` signale un problème de permission. Vérifiez d'abord la cible et pourquoi votre compte ne peut pas modifier son répertoire parent. Une suppression récursive avec privilèges peut endommager le système ou les données d'autres utilisateurs.

`-v` demande à `rm` de rapporter chaque suppression réussie :

```bash
$ rm -rv old-project
removed 'old-project/notes.txt'
removed directory 'old-project'
```

:::single-choice{#remove-nonempty-tree}
Après avoir vérifié toute la cible, quelle commande supprime `old-project/` et tout son contenu tout en conservant les demandes normales ?

::option[`rm old-project/`]{#plain-rm-project explanation="`rm` sans option ne descend pas dans un répertoire et ne peut pas supprimer une arborescence non vide."}
::option[`rm -r old-project/`]{#recursive-old-project .correct explanation="L'option `-r` supprime récursivement l'arborescence. Contrairement à `-rf`, cette forme n'ajoute pas `-f` pour supprimer les demandes."}
::option[`rmdir old-project/`]{#rmdir-project explanation="`rmdir` exige un répertoire vide et échoue si le projet contient encore des entrées."}
:::

Pour vous exercer dans un environnement contrôlé, essayez **[Commande Linux rm : supprimer des fichiers](https://labex.io/fr/labs/linux-linux-rm-command-file-removing-209741)** et **[Organiser des fichiers et répertoires](https://labex.io/fr/labs/linux-organizing-files-and-directories-387877)**.

## Résumé

Vous savez maintenant supprimer des entrées du système de fichiers en considérant chaque cible comme irréversible.

1. Confirmer les chemins avant leur suppression.
2. Prévisualiser le développement des jokers avec une commande en lecture seule.
3. Demander une confirmation avec `-i` ou `-I`.
4. Préférer `rmdir` lorsque le répertoire doit être vide.
5. Valider toute la cible avant une suppression récursive.
