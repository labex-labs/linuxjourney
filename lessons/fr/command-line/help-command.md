---
lesson_id: "help-command"
course_id: "command-line"
lang: "fr"
order_index: 15
title: "help"
description: "Apprenez à choisir l'aide intégrée, la sortie d'utilisation d'un programme ou sa page de manuel."
meta_title: "help - Ligne de commande"
meta_description: "Apprenez à obtenir de l'aide sur la ligne de commande Linux avec l'aide Bash, la sortie --help, les pages man, et la commande type pour les commandes intégrées et externes."
meta_keywords: "commande d'aide linux, aide bash, aide ligne de commande, --help, commande intégrée shell, commande man, commande type"
---

Vous n'avez pas besoin de mémoriser toutes les options. Bash et de nombreux programmes installés peuvent expliquer leur syntaxe directement dans le terminal, mais la source appropriée dépend du type de commande.

## Obtenir de l'aide sur les commandes intégrées à Bash

Bash fournit sa commande intégrée `help` pour les commandes mises en œuvre par le shell lui-même, comme `cd`, `history` et `type`.

Fournissez le nom de la commande comme argument :

```bash
$ help echo
```

La sortie décrit sa syntaxe et son comportement. Sans argument, `help` liste les commandes intégrées pour lesquelles Bash possède une aide.

:::single-choice{#help-for-bash-cd}
Quelle commande affiche l'entrée d'aide de Bash pour sa commande intégrée `cd` ?

::option[`cd --help`]{#cd-help-option explanation="Certaines commandes intégrées reconnaissent des options, mais l'interface de documentation dédiée de Bash est `help` suivie du nom."}
::option[`help cd`]{#help-cd .correct explanation="La commande intégrée `help` de Bash recherche la documentation de la commande intégrée nommée, ici `cd`."}
::option[`type cd`]{#type-cd explanation="`type` explique comment Bash résout le nom `cd` ; elle identifie la commande sans afficher toute son entrée d'aide."}
:::

## Demander le résumé d'utilisation d'un programme

De nombreux programmes externes acceptent par convention `--help` et affichent un résumé :

```bash
$ ls --help
```

Cette convention est fréquente, mais pas universelle. Lisez la sortie et l'état de terminaison au lieu de supposer que tous les programmes prennent en charge la même option.

:::single-choice{#quick-ls-usage}
Quelle commande affiche généralement un résumé rapide fourni par le programme externe `ls` ?

::option[`help ls`]{#bash-help-ls explanation="`help` documente les commandes intégrées au shell. Sur un système typique, elle ne fournit pas la page d'utilisation du programme externe `ls`."}
::option[`ls --help`]{#ls-help .correct explanation="GNU `ls` suit la convention courante `--help` et affiche son utilisation ainsi que ses options."}
::option[`type --help ls`]{#type-help-ls explanation="Cette commande interroge la gestion des options de `type`, pas celle de `ls`."}
:::

## Découvrir comment Bash résout un nom

Utilisez `type` pour savoir si Bash résout un nom comme commande intégrée, alias, fonction, mot-clé ou fichier exécutable :

```bash
$ type cd
cd is a shell builtin
$ type ls
ls is /usr/bin/ls
```

Le résultat exact dépend des alias, fonctions, programmes installés et de `PATH`. Utilisez `type -a NAME` pour afficher toutes les résolutions connues plutôt que la première seulement.

:::single-choice{#identify-command-resolution}
Vous ignorez si `deploy` est un alias, une fonction, une commande intégrée ou un exécutable. Quelle commande Bash vérifie sa résolution ?

::option[`type deploy`]{#type-deploy .correct explanation="La commande intégrée `type` indique comment Bash interprète ce nom dans l'environnement actuel du shell."}
::option[`help deploy`]{#help-deploy explanation="`help` recherche la documentation des commandes intégrées à Bash ; elle n'identifie généralement pas les alias, fonctions et fichiers externes."}
::option[`deploy --help`]{#deploy-help explanation="Cette commande tente d'exécuter le programme et dépend de sa prise en charge de l'option ; elle n'explique pas d'abord comment Bash a résolu le nom."}
:::

## Choisir le niveau de détail

- Utilisez `help COMMAND` pour une commande intégrée à Bash.
- Utilisez `COMMAND --help` pour obtenir un résumé rapide de nombreux programmes externes.
- Utilisez `man COMMAND` pour une page de manuel installée et plus détaillée.
- Utilisez `whatis COMMAND` pour une description en une ligne.

Les leçons suivantes étudient plus précisément les pages de manuel et les descriptions brèves.

:::single-choice{#choose-detailed-manual}
Vous avez besoin de la documentation détaillée de la commande externe `ls`, pas seulement d'un résumé. Quelle commande faut-il essayer ?

::option[`man ls`]{#man-ls .correct explanation="`man ls` ouvre la page de manuel installée, qui décrit normalement plus complètement la syntaxe, les options et le comportement."}
::option[`whatis ls`]{#whatis-ls explanation="`whatis` affiche des descriptions concises de pages de manuel ; elle ne fournit pas la documentation détaillée demandée."}
::option[`type ls`]{#type-ls explanation="`type` indique comment Bash résout `ls` ; elle n'affiche pas le manuel détaillé du programme."}
:::

## Résumé

Vous savez maintenant choisir une source d'aide en fonction de la manière dont Bash résout une commande.

1. Utiliser `help` pour les commandes intégrées à Bash.
2. Essayer `--help` pour le résumé d'utilisation d'un programme.
3. Examiner la résolution d'un nom avec `type`.
4. Ouvrir une documentation détaillée avec `man`.
