---
lesson_id: "grep-command"
course_id: "text-fu"
lang: "fr"
order_index: 16
title: "grep"
description: "Apprenez à sélectionner des lignes avec des chaînes fixes ou des expressions régulières et à interpréter les résultats."
meta_title: "grep - Text-Fu"
meta_description: "Utilisez grep sous Linux pour rechercher des motifs, compter les lignes et filtrer du texte avec les options essentielles."
meta_keywords: "commande grep, grep -e, grep -c, grep -F, grep -o, recherche texte, expressions régulières"
---

`grep` sélectionne les lignes d'entrée correspondant à un motif. Il recherche des fichiers ou stdin, affiche du contexte, compte des lignes et signale par son code de sortie si une correspondance existe.

## Rechercher des lignes dans un fichier

Fournissez un motif puis un ou plusieurs fichiers :

```bash
$ grep 'fox' sample.txt
```

GNU `grep` interprète par défaut le motif comme une expression régulière basique. Citez les motifs pour empêcher le shell d'interpréter d'abord leurs espaces ou métacaractères.

`-F` demande une chaîne fixe :

```bash
$ grep -F 'price: $5.00' products.txt
```

:::single-choice{#grep-fixed-string} Quelle commande recherche littéralement `price: $5.00` dans `products.txt`, sans syntaxe d'expression régulière ?

::option[`grep -F 'price: $5.00' products.txt`]{#grep-fixed-price .correct explanation="`-F` sélectionne les chaînes fixes et les apostrophes protègent le dollar du shell."}
::option[`grep -E 'price: $5.00' products.txt`]{#grep-extended-price explanation="`-E` active les expressions régulières étendues, où `$` et `.` ont un sens spécial."}
::option[`grep -v 'price: $5.00' products.txt`]{#grep-invert-price explanation="`-v` sélectionne les lignes qui ne correspondent pas et conserve l'interprétation régulière."}
:::

## Choisir la syntaxe du motif

GNU `grep` propose trois modes courants : expressions régulières basiques par défaut, étendues avec `-E`, et chaînes fixes avec `-F`. Les ancres `^` et `$` désignent le début et la fin d'une ligne.

```bash
$ grep -E '\.txt$' filenames.txt
```

La barre oblique inverse rend le point littéral ; un `.` non échappé correspond à n'importe quel caractère.

:::single-choice{#grep-literal-txt-suffix} Quelle expression régulière étendue correspond aux lignes finissant littéralement par `.txt` ?

::option[`'.txt$'`]{#grep-anychar-txt explanation="Le point non échappé correspond à n'importe quel caractère."}
::option[`'\.txt$'`]{#grep-dot-txt-end .correct explanation="`\.` désigne un point littéral et `$` ancre la fin de ligne."}
::option[`'^.txt'`]{#grep-start-anychar-txt explanation="Cette forme ancre le début et conserve un point générique."}
:::

## Fournir les motifs en sécurité

`-e PATTERN` fournit explicitement un motif, notamment lorsqu'il commence par `-` :

```bash
$ grep -e '-v' settings.conf
```

Les guillemets seuls n'empêchent pas l'analyse des options. Répétez `-e` pour plusieurs motifs, ou utilisez `-f patterns.txt` pour en lire un par ligne.

:::single-choice{#grep-hyphen-pattern} Quelle commande recherche le motif `-v` dans `settings.conf` au lieu de l'interpréter comme une option ?

::option[`grep '-v' settings.conf`]{#grep-quoted-v explanation="Les guillemets protègent du shell, mais `grep` peut encore interpréter `-v` comme option."}
::option[`grep -v settings.conf`]{#grep-invert-settings explanation="Cette forme active la correspondance inversée sans fournir le motif voulu."}
::option[`grep -e '-v' settings.conf`]{#grep-explicit-v .correct explanation="`-e` déclare que l'argument suivant est un motif même s'il commence par un tiret."}
:::

## Contrôler la sortie sélectionnée

- `-i` : ignorer la casse.
- `-n` : préfixer les numéros de ligne.
- `-v` : sélectionner les lignes non correspondantes.
- `-c` : compter les lignes sélectionnées par fichier.
- `-o` : afficher uniquement chaque partie correspondante non vide.

```bash
$ grep -ic 'fox' sample.txt
```

`-c` compte des lignes, pas toutes les occurrences dans celles-ci. Pour compter des correspondances non superposées avec GNU `grep`, un pipeline possible est `grep -o PATTERN | wc -l`.

:::single-choice{#grep-count-lines} `data.txt` contient une ligne avec `error error` et deux sans correspondance. Que renvoie `grep -c 'error' data.txt` ?

::option[`2`, car le mot apparaît deux fois sur une ligne.]{#grep-count-occurrences explanation="`-c` compte les lignes sélectionnées, pas les occurrences dans une ligne."}
::option[`1`, car exactement une ligne correspond.]{#grep-count-one-line .correct explanation="La ligne est sélectionnée une fois, même si le motif y apparaît deux fois."}
::option[`3`, car le fichier comporte trois lignes.]{#grep-count-total-lines explanation="Les lignes sans correspondance ne contribuent pas au compte."}
:::

## Filtrer stdin et rechercher dans des répertoires

Sans fichier, `grep` lit stdin :

```bash
$ env | grep '^USER='
```

Utilisez `-r` pour parcourir récursivement les fichiers lisibles d'un répertoire :

```bash
$ grep -r 'listen_port' config/
```

`-r` recherche récursivement dans les fichiers lisibles. Les erreurs d'autorisation vont sur stderr et ne constituent pas une entrée de recherche. Ciblez le chemin et comprenez les droits avant d'élever les privilèges.

:::single-choice{#grep-pipeline-input} Dans `generate-report | grep 'failed'`, quelle entrée `grep` recherche-t-il ?

::option[Un fichier `generate-report` dans le répertoire courant.]{#grep-report-file explanation="La partie gauche est exécutée comme commande, pas transmise comme fichier."}
::option[Le flux stdout produit par `generate-report`.]{#grep-report-stdout .correct explanation="Le tube relie stdout du producteur à stdin de `grep`."}
::option[Le flux stderr produit par `generate-report`.]{#grep-report-stderr explanation="Un tube ordinaire transporte stdout ; stderr reste séparé."}
:::

## Interpréter le code de sortie

Pour une recherche ordinaire, GNU `grep` renvoie `0` si au moins une ligne est sélectionnée, `1` si aucune ne l'est et `2` en cas d'erreur. Un script peut donc distinguer absence de résultat, fichier illisible et motif invalide.

`-q` supprime la sortie normale et s'arrête après la première correspondance. Ne déduisez pas le succès d'un écran vide : mode silencieux, redirection, absence de correspondance et erreur peuvent tous produire peu de stdout, mais leurs états diffèrent.

Pour vous exercer :

1. **[Rechercher du texte avec grep sous Linux](https://labex.io/fr/labs/comptia-search-text-with-grep-in-linux-590841)** - Utilisez numéros de ligne, ancres et expressions régulières.
2. **[Commande Linux grep : rechercher des motifs](https://labex.io/fr/labs/linux-linux-grep-command-pattern-searching-219192)** - Explorez la recherche et les motifs complexes.
3. **[Une aiguille dans une botte de foin](https://labex.io/fr/labs/linux-needle-in-the-haystack-388109)** - Comptez et combinez des critères dans des journaux.

## Résumé

Vous savez rechercher du texte ligne par ligne et distinguer les correspondances des erreurs.

1. Choisir entre motifs basiques, étendus ou fixes.
2. Citer les motifs et employer `-e` devant un tiret.
3. Compter les lignes sélectionnées sans les confondre avec les occurrences.
4. Filtrer stdin ou rechercher récursivement dans un chemin ciblé.
5. Interpréter les codes de correspondance, d'absence et d'erreur.
