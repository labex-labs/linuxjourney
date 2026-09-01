---
lesson_id: "vim-inserting-appending-text"
course_id: "advanced-text-fu"
lang: "fr"
order_index: 6
title: "Insertion et Ajout de Texte dans Vim"
description: "Apprenez à passer en mode Insertion avant, après, au-dessus ou au-dessous de la position actuelle dans Vim."
meta_title: "Insertion et Ajout de Texte dans Vim - Maîtrise Avancée"
meta_description: "Apprenez la différence entre les modes insertion et ajout de Vim. Maîtrisez les commandes comme 'i', 'a' et 'o' pour éditer efficacement le texte, ajouter du contenu et insérer une ligne dans Vim."
meta_keywords: "vim ajouter, ajouter vs insérer vim, vim insertion vs ajout, vim insérer ligne, édition de texte vim, commandes vim, tutoriel vim, mode insertion, mode ajout"
---

En mode Normal, Vim interprète les touches comme des commandes. Le mode Insertion ajoute le texte saisi au tampon. Plusieurs commandes du mode Normal passent au mode Insertion à des positions différentes, ce qui permet de commencer à écrire sans déplacement séparé.

Appuyez sur `Esc` pour quitter le mode Insertion et revenir au mode Normal. Si vous ignorez quel mode est actif, `Esc` rétablit sans risque le mode Normal, même si cette touche peut annuler une opération en attente.

:::single-choice{#vim-insert-return-normal} Quelle touche permet normalement de revenir du mode Insertion au mode Normal ?

::option[`Esc`]{#vim-insert-escape .correct explanation="Échap termine l'insertion actuelle et ramène Vim au mode Normal."}
::option[`Entrée`]{#vim-insert-enter explanation="Entrée insère un saut de ligne tout en restant en mode Insertion."}
::option[`Tab`]{#vim-insert-tab explanation="Tab insère une indentation ou déclenche une complétion configurée ; il ne quitte normalement pas le mode Insertion."}
:::

## Insérer avant ou après le curseur

Depuis le mode Normal :

- `i` : passer au mode Insertion avant le curseur ;
- `a` : passer au mode Insertion après le curseur.

Par exemple, si le curseur se trouve sur `b` dans `abc`, `i` commence avant `b`, tandis que `a` commence après. Les deux commandes changent de mode ; le texte tapé ensuite réalise l'insertion.

:::single-choice{#vim-insert-before-cursor} Quelle touche du mode Normal passe en mode Insertion juste avant le curseur ?

::option[`a`]{#vim-insert-a-after explanation="Le `a` minuscule ajoute après le curseur au lieu d'insérer avant lui."}
::option[`o`]{#vim-insert-o-below explanation="Le `o` minuscule ouvre une nouvelle ligne sous la ligne actuelle avant de passer au mode Insertion."}
::option[`i`]{#vim-insert-i-before .correct explanation="Le `i` minuscule commence l'insertion à la position actuelle, avant le caractère sous le curseur."}
:::

## Insérer aux limites de la ligne

Les commandes en majuscule ciblent des positions significatives de la ligne actuelle :

- `I` : passer au mode Insertion avant le premier caractère non blanc ;
- `A` : passer au mode Insertion à la fin de la ligne.

Sur une ligne indentée, `I` ignore l'indentation et commence avant le premier texte non blanc. Utilisez `0i` si vous devez précisément insérer à la colonne zéro.

:::single-choice{#vim-insert-first-nonblank} Quelle commande du mode Normal commence l'insertion avant le premier caractère non blanc de la ligne actuelle ?

::option[`i`]{#vim-insert-lower-i explanation="Le `i` minuscule utilise la position actuelle du curseur sans cibler d'abord le premier texte de la ligne."}
::option[`A`]{#vim-insert-capital-a explanation="Le `A` majuscule commence l'insertion à la fin de la ligne actuelle."}
::option[`I`]{#vim-insert-capital-i .correct explanation="Le `I` majuscule va au premier caractère non blanc et passe en mode Insertion avant lui."}
:::

:::single-choice{#vim-append-line-end} Quelle commande du mode Normal va à la fin de la ligne actuelle et passe en mode Insertion ?

::option[`A`]{#vim-append-capital-a .correct explanation="Le `A` majuscule combine un saut en fin de ligne et le passage au mode Insertion."}
::option[`$`]{#vim-move-line-end explanation="Le déplacement dollar atteint la fin de ligne, mais reste en mode Normal."}
::option[`a`]{#vim-append-one-position explanation="Le `a` minuscule commence après le curseur actuel sans sauter jusqu'à la fin de ligne."}
:::

## Ouvrir une nouvelle ligne

Depuis le mode Normal :

- `o` : ouvrir une nouvelle ligne sous la ligne actuelle et passer au mode Insertion ;
- `O` : ouvrir une nouvelle ligne au-dessus de la ligne actuelle et passer au mode Insertion.

Vim applique l'indentation selon les réglages actifs et les règles du type de fichier. Un nombre peut répéter l'ouverture de ligne, mais apprenez d'abord la forme simple afin de prévoir la position résultante du curseur.

:::single-choice{#vim-open-line-above} Quelle commande du mode Normal ouvre une nouvelle ligne au-dessus de la ligne actuelle et passe au mode Insertion ?

::option[`o`]{#vim-open-lower-o explanation="Le `o` minuscule ouvre une ligne sous la ligne actuelle."}
::option[`O`]{#vim-open-upper-o .correct explanation="Le `O` majuscule ouvre une nouvelle ligne au-dessus et y commence l'insertion."}
::option[`A`]{#vim-open-upper-a explanation="Le `A` majuscule ajoute à la fin de la ligne existante et n'en ouvre pas une nouvelle au-dessus."}
:::

Pour vous exercer à passer du mode Normal au mode Insertion, essayez ce laboratoire :

1. **[Modifier des fichiers texte sous Linux avec Vim et Nano](https://labex.io/fr/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** — Entraînez-vous à créer, modifier et enregistrer des fichiers, ainsi qu'à naviguer avec vi/vim et nano. Vous maîtriserez ainsi les bases des modes Normal et Insertion de Vim.

## Résumé

Vous savez maintenant passer au mode Insertion à l'endroit où le nouveau texte doit apparaître.

1. Revenir au mode Normal avec `Esc`.
2. Insérer avant ou après le curseur avec `i` ou `a`.
3. Insérer avant le premier texte ou à la fin de la ligne avec `I` ou `A`.
4. Ouvrir une ligne au-dessous avec `o`.
5. Ouvrir une ligne au-dessus avec `O`.
