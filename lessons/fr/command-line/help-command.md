---
index: 15
lang: "fr"
title: "help"
meta_title: "help - Ligne de commande"
meta_description: "Apprenez à obtenir de l'aide sur la ligne de commande Linux avec l'aide Bash, la sortie --help, les pages man, et la commande type pour les commandes intégrées et externes."
meta_keywords: "commande d'aide linux, aide bash, aide ligne de commande, --help, commande intégrée shell, commande man, commande type"
---

## Lesson Content

Lorsque vous travaillez sur la ligne de commande Linux, vous aurez souvent besoin d'un rappel rapide sur le fonctionnement d'une commande ou les options qu'elle accepte. Linux fournit plusieurs outils d'aide directement dans le terminal.

### La commande 'help' pour les commandes intégrées Bash

Un des outils les plus directs est `help`, une commande intégrée directement dans le shell Bash. Elle est spécialement conçue pour fournir des informations sur d'autres commandes intégrées Bash. Une commande intégrée fait partie du shell lui-même, ce n'est pas un programme séparé. Des exemples incluent `echo`, `cd` et `pwd`.

Pour utiliser `help`, tapez-le suivi du nom de la commande intégrée.

```bash
$ help echo
```

Cela affichera un résumé de la commande `echo`, sa syntaxe, et une liste des options disponibles. C'est la manière la plus rapide d'obtenir de l'aide pour les fonctions spécifiques au shell.

### Le flag --help pour les programmes exécutables

Pour la plupart des autres programmes exécutables qui ne sont pas intégrés au shell, la commande `help` ne fonctionnera pas. À la place, une convention courante est de fournir un flag `--help`. Cette option indique au programme d'afficher un résumé d'utilisation puis de quitter.

```bash
$ ls --help
```

Bien que la plupart des développeurs suivent cette norme, ce n'est pas universel. Essayer `--help` est généralement une bonne première étape pour un programme inconnu.

### Trouver le type de commande

Si vous n'êtes pas sûr qu'une commande soit une commande intégrée Bash ou un programme externe, utilisez `type`.

```bash
$ type cd
cd is a shell builtin
$ type ls
ls is /usr/bin/ls
```

Cela vous aide à choisir entre `help cd`, `ls --help` ou `man ls`.

### Choisir le bon outil d'aide

- Utilisez `help COMMANDE` pour les commandes intégrées Bash telles que `cd`, `echo` et `history`.
- Utilisez `COMMANDE --help` pour un résumé rapide de nombreuses commandes externes.
- Utilisez `man COMMANDE` pour des pages de manuel détaillées.
- Utilisez `whatis COMMANDE` pour une description en une ligne.

### Questions fréquentes

**Pourquoi `help ls` ne fonctionne-t-il pas ?** `ls` est généralement un programme externe, pas une commande intégrée Bash. Essayez `ls --help` ou `man ls`.

**Pourquoi `--help` ne fonctionne-t-il pas pour toutes les commandes ?** C'est une convention, pas une règle stricte.

**Quelle est la manière la plus rapide de vérifier une commande ?** Essayez `COMMANDE --help` pour les commandes externes et `help COMMANDE` pour les commandes intégrées Bash.

## Exercise

Bien qu'il n'y ait pas de laboratoires spécifiques pour ce sujet, nous recommandons d'explorer le parcours complet [Linux Learning Path](https://labex.io/fr/learn/linux) pour pratiquer les compétences et concepts Linux associés.

## Quiz Question

Comment obtenir rapidement de l'aide en ligne de commande pour les commandes intégrées Bash ? (Veuillez fournir le nom de la commande unique en anglais et en minuscules.)

## Quiz Answer

help
