---
lesson_id: "vim-search-patterns"
course_id: "advanced-text-fu"
lang: "fr"
order_index: 4
title: "Motifs de Recherche Vim"
description: "Apprenez à rechercher vers l'avant ou l'arrière dans Vim, puis à répéter, affiner ou effacer les correspondances."
meta_title: "Motifs de Recherche Vim - Maîtrise Avancée du Texte"
meta_description: "Apprenez à effectuer une recherche Vim avant et arrière en utilisant des motifs. Maîtrisez les techniques de recherche Vim pour trouver rapidement du texte et naviguer entre les résultats avec 'n' et 'N'."
meta_keywords: "Recherche Vim, recherche Vim, commandes Vim, éditeur de texte Linux, tutoriel Vim, guide Vim, motifs de recherche"
---

Vim effectue ses recherches à partir de la position actuelle du curseur en utilisant des motifs. Commencez en mode Normal, lancez une recherche vers l'avant ou l'arrière, puis parcourez les correspondances sans ressaisir le motif.

## Rechercher vers l'avant

En mode Normal, tapez `/`, saisissez un motif, puis appuyez sur Entrée. Vim se place sur la prochaine correspondance après le curseur :

```vim
/pretty
```

Les recherches suivent la syntaxe des expressions régulières de Vim ; des caractères comme `.`, `*`, `[` et `\` peuvent donc avoir un sens spécial. Ajoutez `\V` au début lorsque tout le reste du motif doit être traité de façon « très non magique », ou échappez volontairement les caractères spéciaux.

:::single-choice{#vim-search-forward-key} Depuis le mode Normal, quelle commande lance une recherche vers l'avant de `pretty` ?

::option[`?pretty` suivi d'Entrée]{#vim-backward-pretty explanation="Le point d'interrogation lance une recherche vers l'arrière depuis la position actuelle du curseur."}
::option[`/pretty` suivi d'Entrée]{#vim-forward-pretty .correct explanation="La barre oblique lance une recherche vers l'avant et Entrée soumet le motif."}
::option[`:pretty` suivi d'Entrée]{#vim-command-pretty explanation="Les deux-points ouvrent le mode Ligne de commande pour une commande Ex ; `pretty` ne lance pas ainsi une recherche."}
:::

## Rechercher vers l'arrière

Tapez `?`, saisissez un motif, puis appuyez sur Entrée pour atteindre la correspondance précédente avant le curseur :

```vim
?pretty
```

Cela ne signifie pas nécessairement « la dernière correspondance du fichier ». Le résultat dépend de la position actuelle du curseur. Avec l'option `wrapscan` activée par défaut, la recherche peut reprendre à l'autre extrémité du fichier ; `:set nowrapscan` désactive ce bouclage.

:::single-choice{#vim-search-backward-key} Quel préfixe de recherche du mode Normal parcourt le texte antérieur au curseur ?

::option[`/`]{#vim-slash-forward explanation="La barre oblique recherche vers l'avant depuis le curseur, pas dans le texte qui le précède."}
::option[`?`]{#vim-question-backward .correct explanation="Le point d'interrogation lance une recherche de motif vers l'arrière depuis la position actuelle du curseur."}
::option[`:`]{#vim-colon-command explanation="Les deux-points ouvrent une ligne de commande Ex ; ils ne préfixent pas une recherche vers l'arrière."}
:::

## Répéter une recherche

Après l'un ou l'autre type de recherche :

- appuyez sur `n` pour répéter dans le sens initial ;
- appuyez sur `N` pour répéter dans le sens opposé.

Ainsi, après `/pretty`, `n` avance et `N` recule. Après `?pretty`, `n` recule et `N` avance.

:::single-choice{#vim-repeat-backward-search} Après avoir exécuté `?error`, quelle touche répète la recherche dans le même sens, vers l'arrière ?

::option[`n`]{#vim-same-question-search .correct explanation="Le `n` minuscule répète la dernière recherche dans son sens initial, qui est ici celui de l'arrière."}
::option[`N`]{#vim-opposite-question-search explanation="Le `N` majuscule inverse le sens initial ; après une recherche avec `?`, il avancerait donc."}
::option[`/`]{#vim-new-forward-search explanation="La barre oblique attend un motif pour une nouvelle recherche vers l'avant au lieu de répéter la précédente."}
:::

## Rechercher le mot sous le curseur

En mode Normal, placez le curseur sur un mot, puis utilisez :

- `*` pour rechercher ce mot entier vers l'avant ;
- `#` pour rechercher ce mot entier vers l'arrière.

Ces commandes définissent le dernier motif de recherche ; `n` et `N` peuvent donc poursuivre à partir de celui-ci.

:::single-choice{#vim-current-word-forward} Quelle touche du mode Normal recherche vers l'avant le mot entier sous le curseur ?

::option[`#`]{#vim-hash-current-word explanation="Le dièse recherche vers l'arrière le mot situé sous le curseur."}
::option[`*`]{#vim-star-current-word .correct explanation="L'astérisque construit un motif de mot entier à partir du mot sous le curseur et le recherche vers l'avant."}
::option[`n`]{#vim-repeat-current-pattern explanation="La touche `n` répète une recherche existante ; elle ne crée pas d'abord un motif à partir du mot actuel."}
:::

## Contrôler la casse et le surlignage

Des options de Vim peuvent modifier la gestion de la casse :

- `:set ignorecase` rend les recherches insensibles à la casse ;
- avec `ignorecase`, `:set smartcase` rétablit la sensibilité dès que le motif contient une majuscule ;
- `\c` dans un motif force cette recherche à ignorer la casse ;
- `\C` force cette recherche à respecter la casse.

Par exemple, `/\cerror` correspond à `error`, `Error` et `ERROR`, quelles que soient les options de casse actuelles.

Lorsque le surlignage des recherches est actif, `:nohlsearch` efface les surlignages visibles sans supprimer le motif. La recherche ou répétition suivante pourra de nouveau surligner les correspondances.

:::single-choice{#vim-force-case-insensitive} Quel motif force une recherche de `error` à ignorer la casse, indépendamment des options actuelles ?

::option[`/\Cerror`]{#vim-pattern-match-case explanation="Le `\C` majuscule impose une correspondance sensible à la casse, soit le comportement opposé."}
::option[`/:error`]{#vim-pattern-colon-error explanation="Dans ce motif, les deux-points sont un caractère littéral et ne règlent pas la gestion de la casse."}
::option[`/\cerror`]{#vim-pattern-ignore-case .correct explanation="L'élément `\c` rend cette recherche insensible à la casse ; toutes les variantes de capitalisation peuvent donc correspondre."}
:::

Pour pratiquer la navigation et la recherche de Vim dans un fichier contrôlé, essayez ce laboratoire :

1. **[Modifier des fichiers texte sous Linux avec Vim et Nano](https://labex.io/fr/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** — Entraînez-vous à créer, modifier et enregistrer des fichiers texte, ainsi qu'à y naviguer avec Vim et Nano.

## Résumé

Vous savez maintenant rechercher dans un tampon Vim et parcourir les correspondances de façon prévisible.

1. Lancer une recherche vers l'avant avec `/` et vers l'arrière avec `?`.
2. Répéter dans le même sens avec `n` ou dans le sens opposé avec `N`.
3. Rechercher le mot entier sous le curseur avec `*` ou `#`.
4. Contrôler la casse pour un motif ou à l'aide d'options.
5. Effacer les surlignages sans perdre le motif actuel.
