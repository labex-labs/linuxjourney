---
lesson_id: "stdin-standard-in-redirect"
course_id: "text-fu"
lang: "fr"
order_index: 2
title: "stdin (entrée standard)"
description: "Découvrez comment les programmes lisent l'entrée standard et comment Bash relie ce flux à un fichier."
meta_title: "stdin (entrée standard) - Text-Fu"
meta_description: "Maîtrisez l'entrée standard stdin, le descripteur 0 et la redirection avec l'opérateur <."
meta_keywords: "stdin, entrée standard, rediriger stdin, Linux, ligne de commande, flux d'entrée"
---

L'entrée standard, abrégée **stdin**, est le flux qu'un programme lit normalement pour recevoir des données. Dans un terminal interactif, le shell la relie généralement à votre saisie.

## Entrée standard et descripteur de fichier 0

Par convention, les trois flux standard utilisent ces descripteurs :

- `0` : entrée standard (`stdin`)
- `1` : sortie standard (`stdout`)
- `2` : erreur standard (`stderr`)

Un programme choisit comment employer ces flux. Une commande conçue pour lire stdin attend souvent une saisie au terminal si aucun fichier ni autre source n'est fourni.

:::single-choice{#stdin-descriptor-number} Quel descripteur représente conventionnellement l'entrée standard ?

::option[`0`]{#stdin-fd-zero .correct explanation="L'entrée standard correspond conventionnellement au descripteur 0."}
::option[`1`]{#stdin-fd-one explanation="Le descripteur 1 désigne la sortie standard."}
::option[`2`]{#stdin-fd-two explanation="Le descripteur 2 désigne l'erreur standard."}
:::

## Rediriger un fichier vers stdin

L'opérateur `<` demande à Bash d'ouvrir un fichier en lecture et de le relier à stdin :

```bash
$ cat < peanuts.txt
Hello World
```

Le shell traite `< peanuts.txt` ; `cat` lit simplement le descripteur 0. Le chemin ne lui est pas transmis comme opérande. Si le fichier n'existe pas ou ne peut être ouvert, le shell signale l'erreur et ne lance pas la commande avec cette entrée.

:::single-choice{#stdin-from-file} Quelle commande fait lire `names.txt` à `sort` sur son entrée standard ?

::option[`sort < names.txt`]{#sort-stdin-file .correct explanation="Bash ouvre `names.txt` et le relie au descripteur 0 de `sort`."}
::option[`sort > names.txt`]{#stdout-to-names explanation="`>` redirige stdout et peut tronquer le fichier ; il ne fournit pas l'entrée."}
::option[`sort names.txt >`]{#incomplete-sort-output explanation="Cette redirection de sortie est incomplète."}
:::

## Opérande de fichier ou redirection d'entrée

Certaines commandes acceptent soit un nom de fichier, soit stdin, avec parfois une légère différence :

```bash
$ wc -l peanuts.txt
1 peanuts.txt
$ wc -l < peanuts.txt
1
```

Les deux formes comptent les mêmes lignes. Dans la première, `wc` connaît le nom reçu en argument. Dans la seconde, il ne reçoit qu'un flux et n'a aucun nom à afficher.

:::single-choice{#stdin-not-command-argument} Pourquoi `wc -l < peanuts.txt` omet-il normalement `peanuts.txt` dans sa sortie ?

::option[`wc` supprime le nom après le comptage.]{#stdin-delete-name explanation="La commande ne renomme ni ne supprime le fichier."}
::option[L'opérateur `<` masque chaque mot affiché.]{#stdin-hide-words explanation="La redirection d'entrée ne filtre pas stdout."}
::option[Bash fournit le fichier sur stdin plutôt que comme argument.]{#stdin-no-filename .correct explanation="Le shell relie le fichier au descripteur 0 ; `wc` ne reçoit donc pas son chemin comme opérande."}
:::

## Combiner les redirections d'entrée et de sortie

Une même ligne peut rediriger plusieurs flux :

```bash
$ cat < peanuts.txt > banana.txt
```

Le shell réalise deux connexions indépendantes :

1. `< peanuts.txt` ouvre `peanuts.txt` comme stdin de `cat`.
2. `> banana.txt` crée ou tronque `banana.txt` et le relie à stdout.

`cat` lit stdin et écrit sur stdout ; `banana.txt` reçoit donc le contenu source. Pour une copie ordinaire, `cp peanuts.txt banana.txt` exprime mieux l'intention ; cet exemple illustre les flux.

:::single-choice{#stdin-and-stdout-files} Dans `cat < input.txt > output.txt`, quel fichier fournit stdin et lequel reçoit stdout ?

::option[`output.txt` fournit stdin et `input.txt` reçoit stdout.]{#stdin-output-stdout-input explanation="Cela inverse le sens des opérateurs."}
::option[`input.txt` fournit stdin et `output.txt` reçoit stdout.]{#stdin-input-stdout-output .correct explanation="`<` ouvre `input.txt` pour le descripteur 0 et `>` ouvre `output.txt` pour le descripteur 1."}
::option[Les deux fournissent stdin et stdout reste au terminal.]{#both-stdin explanation="Les opérateurs touchent deux flux différents ; `>` redirige stdout."}
:::

Pour vous exercer :

1. **[Rediriger les entrées et sorties sous Linux](https://labex.io/fr/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Manipulez stdout, stderr et stdin avec les opérateurs de redirection.
2. **[Redirection des flux de données](https://labex.io/fr/labs/linux-data-stream-redirection-17995)** - Combinez les flux standard et utilisez `/dev/null`.

## Résumé

Vous savez maintenant relier l'entrée standard d'une commande à un fichier.

1. Reconnaître stdin comme le descripteur 0.
2. Rediriger un fichier lisible avec `<`.
3. Distinguer un opérande d'une entrée redirigée.
4. Combiner volontairement les redirections stdin et stdout.
