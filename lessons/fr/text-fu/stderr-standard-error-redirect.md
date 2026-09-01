---
lesson_id: "stderr-standard-error-redirect"
course_id: "text-fu"
lang: "fr"
order_index: 3
title: "stderr (erreur standard)"
description: "Apprenez à rediriger l'erreur standard séparément ou à la réunir avec la sortie standard dans Bash."
meta_title: "stderr (erreur standard) - Text-Fu"
meta_description: "Gérez stderr sous Linux avec le descripteur 2 et les redirections 2>, 2>&1, &> et /dev/null."
meta_keywords: "stderr, erreur standard Linux, descripteur 2, redirection stderr, 2>, 2>&1, &>, /dev/null"
---

Les programmes écrivent normalement leurs résultats sur la sortie standard et leurs diagnostics sur un flux séparé nommé erreur standard, ou **stderr**. Cette séparation permet d'enregistrer les données utiles sans y mêler les erreurs.

## Séparer la sortie ordinaire des erreurs

```bash
$ ls /fake/directory > peanuts.txt
ls: cannot access '/fake/directory': No such file or directory
```

`>` ne redirige que stdout. Le diagnostic va sur stderr, toujours relié au terminal. Le shell crée ou tronque néanmoins `peanuts.txt` pour stdout.

Les descripteurs standard sont `0` pour stdin, `1` pour stdout et `2` pour stderr.

:::single-choice{#stderr-not-in-stdout-file} Pourquoi l'erreur de `ls /missing > results.txt` reste-t-elle normalement au terminal ?

::option[`>` redirige stdout, tandis que le diagnostic va sur stderr.]{#stderr-separate-stream .correct explanation="Un simple `>` ne modifie que le descripteur 1 ; le descripteur 2 conserve le terminal."}
::option[`ls` attend la fermeture du fichier avant toute erreur.]{#stderr-waits-for-close explanation="Il ne s'agit pas de temporisation, mais de flux distincts."}
::option[`results.txt` ne peut pas contenir de diagnostics.]{#stderr-file-capability explanation="Un fichier ordinaire peut recevoir les deux flux ; stderr n'a simplement pas été redirigé."}
:::

## Rediriger stderr avec 2>

Placez le descripteur `2` devant `>` :

```bash
$ ls /fake/directory 2> errors.txt
```

Le shell crée ou tronque `errors.txt` et le relie au descripteur 2. Stdout reste inchangé. Utilisez `2>>` pour ajouter les erreurs.

:::single-choice{#stderr-to-error-file} Quelle commande remplace `errors.log` par les diagnostics de `find /restricted` tout en laissant stdout inchangé ?

::option[`find /restricted > errors.log`]{#stdout-errors-log explanation="`>` redirige le descripteur 1, donc les résultats ordinaires."}
::option[`find /restricted < errors.log`]{#stdin-errors-log explanation="`<` fournit le fichier comme entrée standard."}
::option[`find /restricted 2> errors.log`]{#stderr-errors-log .correct explanation="Le `2` sélectionne stderr et `>` crée ou tronque sa destination."}
:::

## Réunir stdout et stderr

Redirigez d'abord stdout, puis dupliquez stderr vers sa destination actuelle :

```bash
$ ls /fake/directory /etc/passwd > combined.txt 2>&1
```

Les redirections sont traitées de gauche à droite : stdout va d'abord dans le fichier, puis stderr rejoint cette destination. Dans l'ordre inverse :

```bash
$ ls /fake/directory /etc/passwd 2>&1 > regular.txt
```

stderr copie d'abord l'ancienne destination de stdout, le terminal, puis seul stdout va dans `regular.txt`.

:::single-choice{#stderr-combine-order} Quelle redirection Bash envoie stdout et stderr de `command` vers `all.log` ?

::option[`command 2>&1 > all.log`]{#stderr-before-stdout explanation="Stderr rejoint d'abord l'ancienne destination de stdout ; les flux restent séparés."}
::option[`command 2> all.log > /dev/null`]{#stderr-file-stdout-null explanation="Stderr va dans le fichier, mais stdout est jeté."}
::option[`command > all.log 2>&1`]{#stdout-then-stderr .correct explanation="Stdout va d'abord dans le fichier, puis stderr duplique cette destination."}
:::

Bash propose aussi `&>` pour remplacer un fichier avec les deux flux et `&>>` pour les ajouter.

```bash
$ ls /fake/directory /etc/passwd &> combined.txt
```

:::single-choice{#stderr-bash-short-form} Quelle commande Bash ajoute stdout et stderr de `build` à `build.log` ?

::option[`build &> build.log`]{#replace-both-build explanation="`&>` remplace le fichier existant."}
::option[`build 2>> build.log`]{#append-errors-build explanation="Cette forme n'ajoute que stderr."}
::option[`build &>> build.log`]{#append-both-build .correct explanation="Dans Bash, `&>>` ajoute les descripteurs 1 et 2 à la même destination."}
:::

## Écarter volontairement un flux

`/dev/null` est un périphérique spécial qui jette les données reçues :

```bash
$ ls /fake/directory 2> /dev/null
```

Cela ne rend pas la commande réussie et ne change pas son code de sortie ; seul le diagnostic est masqué. Pendant un dépannage, conservez stderr plutôt que de perdre l'information utile.

:::single-choice{#stderr-dev-null-effect} Que change `check-data 2> /dev/null` ?

::option[Elle jette stdout et transforme toute erreur en réussite.]{#discard-stdout-success explanation="Le descripteur 2 est stderr et la redirection ne modifie pas le code de sortie."}
::option[Elle jette stderr sans imposer un code de réussite.]{#discard-stderr-only .correct explanation="Seule la destination des diagnostics change ; le programme détermine toujours son état final."}
::option[Elle enregistre stderr dans un fichier caché.]{#save-dev-null explanation="`/dev/null` jette les données ; elles ne sont pas récupérables."}
:::

Pour vous exercer :

1. **[Rediriger les entrées et sorties sous Linux](https://labex.io/fr/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Manipulez stdout, stderr et stdin avec `>`, `>>`, `2>` et `tee`.

## Résumé

Vous savez désormais séparer les diagnostics ou les réunir avec la sortie ordinaire.

1. Reconnaître stderr comme le descripteur 2.
2. Remplacer ou compléter un journal avec `2>` ou `2>>`.
3. Appliquer les redirections de gauche à droite.
4. Réunir les deux sorties avec une syntaxe choisie.
5. Ne jeter les diagnostics que lorsque leur perte est acceptable.
