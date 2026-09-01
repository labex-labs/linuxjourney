---
lesson_id: "cat-command"
course_id: "command-line"
lang: "fr"
order_index: 7
title: "cat"
description: "Apprenez à afficher, concaténer et rediriger sans risque le contenu de fichiers avec la commande cat."
meta_title: "cat - Ligne de commande"
meta_description: "Apprenez la commande Linux cat avec des exemples pour afficher des fichiers, concaténer des fichiers, numéroter les lignes, créer des fichiers et utiliser la redirection en toute sécurité."
meta_keywords: "commande linux cat, commande cat, afficher fichier linux, concaténer fichiers, cat -n, cat -b, redirection cat, linux cat"
---

Après avoir appris à identifier les fichiers, l'étape suivante consiste à lire leur contenu. La commande `cat` affiche les fichiers et en réunit le contenu ; son nom est l'abréviation de « concatenate ».

## Afficher le contenu d'un fichier

L'utilisation la plus simple de `cat` affiche directement un fichier dans le terminal :

```bash
$ cat myfile.txt
```

La commande écrit tout le fichier sur la sortie standard. Cette méthode convient aux textes courts, mais un fichier long peut défiler trop rapidement.

:::single-choice{#display-short-file} Quelle commande affiche tout le contenu de `myfile.txt` dans le terminal ?

::option[`file myfile.txt`]{#classify-myfile explanation="`file` indique le type probable du fichier ; elle n'affiche pas tout le texte qu'il contient."}
::option[`touch myfile.txt`]{#update-myfile explanation="`touch` actualise les horodatages ou crée un fichier absent ; elle n'affiche pas son contenu."}
::option[`cat myfile.txt`]{#display-myfile .correct explanation="`cat` lit `myfile.txt` et écrit son contenu sur la sortie standard, ici le terminal."}
:::

## Concaténer des fichiers

Lorsque vous fournissez plusieurs fichiers à `cat`, elle les lit dans l'ordre des opérandes et écrit leurs contenus à la suite :

```bash
$ cat dogfile birdfile
```

`dogfile` est affiché avant `birdfile`. Pour enregistrer la sortie combinée dans un nouveau fichier, redirigez la sortie standard avec `>` :

```bash
$ cat dogfile birdfile > animals
```

Le shell crée `animals` ou le tronque avant de lancer `cat`, puis y envoie la sortie combinée. N'utilisez pas l'un des fichiers d'entrée comme destination : il pourrait être vidé avant sa lecture par `cat`.

:::single-choice{#combine-files-in-order} Quelle commande écrit `part1`, puis `part2`, dans un fichier nouveau ou remplacé nommé `whole` ?

::option[`cat whole > part1 part2`]{#reverse-redirection explanation="Une redirection possède une seule destination, tandis que les autres mots deviennent des opérandes de `cat`. Cette commande n'exprime pas les entrées et la sortie demandées."}
::option[`cat part1 part2 > whole`]{#ordered-inputs .correct explanation="`cat` produit les deux fichiers dans l'ordre indiqué et `>` redirige la sortie combinée vers `whole`."}
::option[`cat part2 part1 > whole`]{#reverse-inputs explanation="Cette commande écrit les mêmes entrées dans `whole`, mais lit `part2` avant `part1`. L'ordre des opérandes détermine celui de la sortie."}
:::

## Écrire l'entrée du terminal dans un fichier

Sans fichier d'entrée, `cat` lit l'entrée standard. Combinez ce comportement avec `>` pour saisir du texte dans le terminal et l'écrire dans un fichier :

```bash
$ cat > newfile.txt
```

Après la commande, tapez le texte voulu. Appuyez sur `Ctrl+D` pour envoyer une fin de fichier et revenir au shell. Attention : si `newfile.txt` existe, `>` tronque son ancien contenu.

Utilisez `>>` pour ajouter la nouvelle saisie au lieu de remplacer le contenu existant :

```bash
$ cat >> notes.txt
```

:::single-choice{#append-terminal-input} Vous voulez saisir du texte supplémentaire à la fin d'un fichier `notes.txt` existant. Quelle commande lance l'opération sans tronquer le fichier ?

::option[`cat > notes.txt`]{#overwrite-notes explanation="Un seul `>` tronque la destination avant d'y rediriger l'entrée. Le texte existant de `notes.txt` serait perdu."}
::option[`cat >> notes.txt`]{#append-notes .correct explanation="L'opérateur `>>` ouvre la destination en ajout ; le texte lu par `cat` est donc placé après le contenu existant."}
::option[`cat notes.txt > notes.txt`]{#same-input-output explanation="Utiliser le même fichier comme entrée et comme destination de `>` peut le tronquer avant sa lecture. Ce n'est pas un ajout sûr."}
:::

## Mettre en forme la sortie

Plusieurs options facilitent l'inspection :

- `-n` : numéroter toutes les lignes de sortie à partir de 1 ;
- `-b` : ne numéroter que les lignes non vides ;
- `-s` : réduire plusieurs lignes vides successives à une seule ;
- `-A` : montrer les caractères non imprimables, les tabulations et fins de ligne.

Exemples :

```bash
$ cat -n script.sh
$ cat -b notes.txt
$ cat -s messy.txt
```

:::single-choice{#number-nonempty-lines} Quelle commande ne numérote que les lignes de sortie non vides de `notes.txt` ?

::option[`cat -b notes.txt`]{#number-nonblank .correct explanation="L'option `-b` numérote les lignes non vides et laisse les lignes vides sans numéro."}
::option[`cat -n notes.txt`]{#number-all-lines explanation="L'option `-n` numérote toutes les lignes, y compris les lignes vides ; elle ne respecte pas la condition demandée."}
::option[`cat -s notes.txt`]{#squeeze-blank-lines explanation="L'option `-s` réduit les suites de lignes vides à une seule, sans ajouter de numéros."}
:::

## Choisir un afficheur pour les fichiers longs

Utilisez `cat` lorsque vous voulez toute la sortie à la fois. Pour un fichier long, `less` est généralement plus pratique : il permet de faire défiler, de rechercher et de quitter sans inonder le terminal.

```bash
$ less /var/log/syslog
```

:::single-choice{#choose-viewer-for-long-file} Quelle commande convient le mieux à la lecture interactive d'un long journal ?

::option[`less /var/log/syslog`]{#page-through-log .correct explanation="`less` permet le défilement, la recherche et une sortie contrôlée ; il convient donc à la lecture interactive de longs fichiers."}
::option[`cat /var/log/syslog`]{#print-entire-log explanation="`cat` écrit tout le journal dans le terminal d'un coup. Un fichier long peut défiler avant que vous ne l'examiniez."}
::option[`touch /var/log/syslog`]{#update-log-time explanation="`touch` change les horodatages et peut exiger des permissions ; cette commande ne sert pas à lire le journal."}
:::

Pour vous exercer à afficher et combiner des contenus, essayez ces laboratoires :

1. **[Commande Linux cat : concaténer des fichiers](https://labex.io/fr/labs/linux-linux-cat-command-file-concatenating-210986)** — Utilisez `cat` pour afficher, concaténer et manipuler des fichiers texte.
2. **[Afficher les journaux et fichiers de configuration Linux](https://labex.io/fr/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** — Entraînez-vous à lire et parcourir efficacement des fichiers texte, notamment les journaux et configurations du système.

## Résumé

Vous savez maintenant utiliser `cat` pour afficher et combiner le contenu de fichiers en choisissant une redirection sûre.

1. Afficher le contenu complet d'un fichier court.
2. Concaténer des fichiers dans l'ordre choisi.
3. Remplacer une destination ou lui ajouter du texte volontairement.
4. Numéroter ou simplifier les lignes de sortie.
5. Choisir `less` lorsqu'une lecture interactive convient mieux.
