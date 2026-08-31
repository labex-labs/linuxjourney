---
lesson_id: "whatis-command"
course_id: "command-line"
lang: "fr"
order_index: 17
title: "whatis"
description: "Apprenez à obtenir de brèves descriptions de pages de manuel et à interpréter leurs numéros de section."
meta_title: "whatis - Ligne de commande"
meta_description: "Apprenez la commande Linux whatis avec des exemples pour obtenir des descriptions de commandes en une ligne à partir des pages man et comprendre plusieurs sections du manuel."
meta_keywords: "commande whatis, linux whatis, description commande linux, résumé page man, aide ligne de commande, apropos"
---

Lorsque vous reconnaissez le nom d'une commande, mais avez oublié son rôle, `whatis` fournit un bref rappel provenant de la base des pages de manuel.

## Rechercher un nom exact

Fournissez un ou plusieurs noms de sujets exacts à `whatis`. Chaque résultat provient de la section `NAME` d'une page de manuel installée :

```bash
$ whatis cat
cat (1)              - concatenate files and print on the standard output
```

La sortie est une description et non une liste d'options ou d'exemples. Utilisez `man cat` ou `cat --help` pour davantage de détails.

:::single-choice{#describe-known-command}
Vous connaissez le nom `cat` et voulez sa description de manuel en une ligne. Quelle commande faut-il exécuter ?

::option[`man cat`]{#manual-cat explanation="`man cat` ouvre toute la page de manuel et fournit plus que le bref rappel demandé."}
::option[`apropos cat`]{#apropos-cat explanation="`apropos` recherche un mot-clé dans les descriptions et peut renvoyer de nombreux sujets ; elle est plus large qu'une recherche par nom exact."}
::option[`whatis cat`]{#whatis-cat .correct explanation="`whatis` recherche le nom de sujet exact et affiche sa description concise issue de la base des manuels."}
:::

## Lire les numéros de section

Si un sujet possède des pages dans plusieurs sections, `whatis` peut afficher plusieurs résultats :

```bash
$ whatis passwd
passwd (1)           - change user password
passwd (5)           - the password file
```

Le nombre entre parenthèses est la section du manuel. Ici, `passwd(1)` décrit la commande utilisateur et `passwd(5)` un format de fichier. Ouvrez l'une d'elles avec `man 1 passwd` ou `man 5 passwd`.

:::single-choice{#interpret-whatis-section}
Dans la sortie `passwd (5) - the password file`, que désigne `(5)` ?

::option[La cinquième option acceptée par la commande `passwd`.]{#fifth-option explanation="Ce nombre n'est pas une position d'option ; les options sont documentées à l'intérieur de la page choisie."}
::option[La section du manuel qui contient la page du format de fichier.]{#section-five .correct explanation="La section 5 est consacrée aux formats et conventions de fichiers ; `passwd(5)` désigne cette section."}
::option[Cinq pages de manuel qui partagent le nom `passwd`.]{#five-pages explanation="Plusieurs résultats peuvent exister, mais la valeur entre parenthèses indique une section et non un nombre de pages."}
:::

## Choisir entre whatis, man et apropos

- `whatis NAME` : afficher les descriptions concises d'un nom exact de sujet ;
- `man NAME` : ouvrir une page de manuel complète ;
- `apropos KEYWORD` : rechercher un mot-clé dans les noms et descriptions des pages.

Par exemple :

```bash
$ apropos password
```

Utilisez `apropos` lorsque vous connaissez la tâche, mais pas le nom de la commande. Utilisez `whatis` lorsque vous connaissez déjà ce nom.

:::single-choice{#search-by-purpose}
Vous ignorez le nom de la commande, mais voulez rechercher le mot-clé `password` dans les descriptions des manuels. Quelle commande convient ?

::option[`apropos password`]{#apropos-password .correct explanation="`apropos` recherche le mot-clé dans les noms et descriptions des pages, ce qui aide à découvrir les sujets pertinents."}
::option[`whatis password`]{#exact-password explanation="`whatis` cherche un sujet exact nommé `password` ; elle n'est pas l'interface générale de recherche par mot-clé."}
::option[`man password`]{#manual-password explanation="`man` tente d'ouvrir une page portant ce nom ; elle ne réalise pas la recherche de descriptions demandée."}
:::

## Lorsqu'aucune description n'apparaît

Si `whatis` ne trouve rien d'approprié, le sujet peut ne pas posséder de page installée ou la base peut être obsolète. Ce résultat ne prouve pas qu'aucun exécutable, alias, fonction ou commande intégrée de ce nom n'existe. Utilisez `type NAME` pour savoir comment Bash le résout, puis choisissez la source d'aide appropriée.

:::single-choice{#whatis-versus-type}
`whatis deploy` ne trouve aucune description. Quelle commande vérifie si Bash résout `deploy` comme alias, fonction, commande intégrée ou exécutable ?

::option[`whatis -r deploy`]{#whatis-regex-deploy explanation="Modifier la requête de la base manuelle ne montre pas tous les alias, fonctions, commandes intégrées et résolutions de chemins de Bash."}
::option[`man 5 deploy`]{#manual-five-deploy explanation="Cette commande tente d'ouvrir une page de section 5 ; elle ne détermine pas comment Bash résout le nom."}
::option[`type deploy`]{#resolve-deploy .correct explanation="La commande `type` de Bash indique comment le shell actuel résout un nom, indépendamment de l'existence d'une description manuelle."}
:::

## Résumé

Vous savez maintenant récupérer et interpréter les descriptions concises de la base des manuels.

1. Rechercher un sujet exact avec `whatis`.
2. Lire la section du manuel entre parenthèses.
3. Utiliser `man` pour la page complète.
4. Utiliser `apropos` lorsque vous connaissez un mot-clé plutôt qu'un nom.
