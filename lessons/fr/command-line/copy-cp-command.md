---
lesson_id: "copy-cp-command"
course_id: "command-line"
lang: "fr"
order_index: 10
title: "cp (Copier)"
description: "Apprenez à copier des fichiers et des arborescences tout en contrôlant les écrasements et les attributs conservés."
meta_title: "cp (Copier) - Ligne de commande"
meta_description: "Apprenez la commande Linux cp avec des exemples pour copier des fichiers, des répertoires, plusieurs fichiers, des jokers, des sauvegardes et des options comme cp -r, cp -i et cp -p."
meta_keywords: "commande linux cp, commande cp, copier fichiers linux, cp -r, cp -i, cp -p, cp -a, cp -u, copie récursive, jokers linux"
---

La commande `cp` copie des fichiers et répertoires en laissant la source en place. Sa syntaxe élémentaire est :

```bash
cp [OPTIONS] SOURCE DESTINATION
```

Vous pouvez copier un fichier vers un autre chemin, plusieurs fichiers dans un répertoire ou toute une arborescence de manière récursive.

## Copier un fichier

Placez d'abord la source, puis la destination :

```bash
$ cp mycoolfile /home/pete/Documents/cooldocs
```

Si `/home/pete/Documents/cooldocs` est un répertoire existant, la copie y est créée sous le nom `mycoolfile`. Vous pouvez aussi fournir un nouveau nom de destination :

```bash
$ cp mycoolfile /home/pete/Documents/mycoolfile_backup
```

Dans le second exemple, les données copiées prennent le nom `mycoolfile_backup`.

:::single-choice{#copy-file-under-new-name} Quelle commande copie `draft.txt` vers un fichier nommé `final.txt` tout en conservant `draft.txt` ?

::option[`mv draft.txt final.txt`]{#move-draft explanation="`mv` renomme ou déplace le chemin original ; elle ne laisse pas la copie source demandée en place."}
::option[`cp final.txt draft.txt`]{#copy-reversed explanation="La source et la destination sont inversées. Cette commande copierait `final.txt` vers `draft.txt`."}
::option[`cp draft.txt final.txt`]{#copy-draft .correct explanation="`cp` lit `draft.txt` et crée ou remplace `final.txt`, tandis que la source reste disponible."}
:::

## Copier plusieurs fichiers dans un répertoire

Énumérez toutes les sources, puis placez le répertoire de destination en dernier :

```bash
$ cp report.txt notes.txt summary.txt /home/pete/Documents/
```

Lorsque vous fournissez plusieurs sources, le dernier argument doit être un répertoire.

:::single-choice{#copy-multiple-files} Quelle commande copie `a.txt` et `b.txt` dans le répertoire existant `archive/` ?

::option[`cp archive/ a.txt b.txt`]{#destination-first explanation="Dans cette forme de `cp`, le répertoire de destination doit se trouver à la fin. Le placer en premier change l'interprétation des opérandes."}
::option[`cp a.txt b.txt archive/`]{#destination-last .correct explanation="Avec plusieurs sources, `cp` traite le dernier répertoire existant comme destination de tous les fichiers qui le précèdent."}
::option[`cp a.txt archive/ b.txt`]{#destination-middle explanation="Toutes les sources doivent précéder la destination ; le répertoire existant doit être le dernier opérande."}
:::

## Sélectionner des fichiers avec des jokers

Le shell peut développer des motifs jokers en plusieurs chemins sources :

- `*` correspond à n'importe quelle suite de caractères ;
- `?` correspond à un caractère quelconque ;
- `[]` correspond à l'un des caractères entre crochets.

Par exemple, copiez les noms qui se terminent par `.jpg` du répertoire actuel vers `Pictures` :

```bash
$ cp *.jpg /home/pete/Pictures
```

Prévisualisez les correspondances avant une copie en masse, surtout si la destination contient des données importantes :

```bash
$ ls *.jpg
beach.jpg  lunch.jpg  profile.jpg
$ cp *.jpg /home/pete/Pictures
```

:::single-choice{#preview-copy-pattern} Avant de copier `*.jpg`, quelle commande montre les noms non cachés auxquels le motif correspond actuellement ?

::option[`cp *.jpg`]{#copy-no-destination explanation="Si plusieurs noms correspondent, cette commande tente une copie sans destination claire ; elle ne constitue pas une prévisualisation."}
::option[`ls *.jpg`]{#list-jpg-matches .correct explanation="Le shell développe le même motif pour `ls`, ce qui permet d'examiner les noms correspondants avant de les copier."}
::option[`file '*.jpg'`]{#quoted-jpg-pattern explanation="Les guillemets empêchent le développement du joker ; `file` reçoit les caractères littéraux `*.jpg` et ne prévisualise pas les correspondances normales."}
:::

## Copier des arborescences

La copie d'un répertoire et de tout son contenu doit être récursive. Utilisez `-r` ou `-R` :

```bash
$ cp -r Pumpkin/ /home/pete/Documents
```

Cette commande copie `Pumpkin` et ses descendants dans `Documents`.

`-R` en majuscule demande également une copie récursive :

```bash
$ cp -R website /home/pete/backups/
```

Le mode archive, `-a`, convient aux copies de type sauvegarde. Il copie récursivement tout en conservant les liens et de nombreux attributs :

```bash
$ cp -a project/ project-backup/
```

:::single-choice{#archive-directory-tree} Vous voulez une copie récursive de type sauvegarde de `project/`, avec conservation des liens et de nombreux attributs. Quelle commande convient ?

::option[`cp -p project/ project-backup/`]{#preserve-directory-only explanation="`-p` conserve certains attributs, mais ne rend pas à elle seule la copie d'un répertoire récursive."}
::option[`cp -u project/ project-backup/`]{#update-directory-only explanation="`-u` contrôle les copies selon l'état de la destination, mais n'active pas à elle seule la récursivité."}
::option[`cp -a project/ project-backup/`]{#archive-project .correct explanation="Le mode archive inclut la copie récursive et conserve les liens ainsi qu'un large ensemble d'attributs."}
:::

## Contrôler les écrasements

Par défaut, `cp` peut remplacer un fichier de destination existant. Utilisez `-i` pour demander une confirmation avant l'écrasement :

```bash
$ cp -i mycoolfile /home/pete/Pictures
cp: overwrite '/home/pete/Pictures/mycoolfile'? n
```

Utilisez `-n` lorsqu'une destination existante ne doit pas être écrasée :

```bash
$ cp -n mycoolfile /home/pete/Pictures
```

Avec GNU `cp`, `-f` demande de tenter de supprimer une destination existante si elle ne peut pas être ouverte en écriture, puis de recommencer la copie. Cette option ne remplace pas une vérification attentive des cibles. Des alias peuvent aussi ajouter des options comme `-i` ; examinez une demande inattendue au lieu de supposer une configuration précise.

:::single-choice{#skip-existing-destination} Quelle commande copie `report.txt` dans `backup/`, mais ignore une destination existante portant le même nom ?

::option[`cp -n report.txt backup/`]{#no-clobber-report .correct explanation="L'option `-n` empêche `cp` d'écraser un fichier de destination existant."}
::option[`cp -i report.txt backup/`]{#interactive-report explanation="`-i` demande une confirmation ; le résultat dépend donc de la réponse et n'ignore pas automatiquement chaque destination existante."}
::option[`cp -f report.txt backup/`]{#force-report explanation="`-f` peut aider à remplacer une destination impossible à ouvrir initialement ; elle ne produit pas un comportement sans écrasement."}
:::

## Conserver ou actualiser des fichiers

`-p` conserve le mode, la propriété lorsque les permissions l'autorisent, et les horodatages de la source :

```bash
$ cp -p mycoolfile /home/pete/backups/
```

`-u` ne copie la source que si la destination manque ou si la source est plus récente :

```bash
$ cp -u *.txt /home/pete/Documents/
```

Autres options courantes :

- `-f` : forcer l'écrasement en supprimant d'abord la destination si nécessaire ;
- `-v` : afficher chaque fichier à mesure de sa copie.

Pour vous exercer, essayez les laboratoires **[Commande Linux cp : copier des fichiers](https://labex.io/fr/labs/linux-linux-cp-command-file-copying-209744)** et **[Organiser des fichiers et répertoires](https://labex.io/fr/labs/linux-organizing-files-and-directories-387877)**.

## Résumé

Vous savez maintenant copier des fichiers et des arborescences tout en contrôlant le traitement des destinations.

1. Placer les sources avant la destination.
2. Prévisualiser les correspondances des jokers avant une copie en masse.
3. Copier les arborescences récursivement ou en mode archive.
4. Confirmer, ignorer ou remplacer volontairement les destinations existantes.
5. Conserver les attributs ou ne copier que les sources plus récentes.
