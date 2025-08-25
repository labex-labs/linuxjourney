---
index: 7
lang: "fr"
title: "Édition Vim"
meta_title: "Édition Vim - Maîtrise avancée du texte"
meta_description: "Apprenez les bases de l'édition Vim : supprimer, modifier, copier et coller du texte efficacement. Maîtrisez les commandes Vim essentielles pour les débutants et améliorez vos compétences en édition de texte sous Linux."
meta_keywords: "édition Vim, commandes Vim, éditeur de texte Linux, tutoriel Vim, guide Vim, Vim débutant, commande dd, suppression Vim"
---

## Lesson Content

L'édition dans Vim se fait à partir du mode Normal en utilisant des opérateurs et des mouvements. Vous pouvez supprimer, modifier, copier (yank), coller (put) et remplacer du texte efficacement.

- Appuyez sur `Esc` pour vous assurer que vous êtes en mode Normal avant d'utiliser ces commandes.

Suppressions (opérateur `d`):

- `x` – supprime le caractère sous le curseur
- `dw` – supprime du curseur jusqu'au début du mot suivant
- `d$` – supprime du curseur jusqu'à la fin de la ligne
- `dd` – supprime la ligne actuelle
- Les comptes s'appliquent : `3dd` supprime trois lignes ; `2dw` supprime deux mots

Modifications (opérateur `c`, supprime puis entre en mode Insertion):

- `cw` – modifie le mot à partir du curseur
- `c$` – modifie jusqu'à la fin de la ligne
- `cc` – modifie toute la ligne

Copier et Coller (yank/put):

- `yw` – copie le mot
- `yy` – copie la ligne actuelle
- `p` – colle après le curseur ou sous la ligne
- `P` – colle avant le curseur ou au-dessus de la ligne

Remplacer et autres modifications pratiques:

- `r{char}` – remplace le caractère sous le curseur par `{char}`
- `R` – entre en mode Remplacement pour écraser le texte
- `J` – joint la ligne actuelle avec la ligne suivante
- `.` – répète la dernière modification

Combinez les opérateurs avec les mouvements pour plus de puissance : `d}` supprime jusqu'au paragraphe suivant ; `caw` modifie « un mot » (le mot sous le curseur, y compris l'espace environnant).

## Exercise

La pratique rend parfait ! Voici un laboratoire pratique pour renforcer votre compréhension de l'édition de texte dans Vim :

1. **[Modifier des fichiers texte sous Linux avec Vim et Nano](https://labex.io/fr/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Entraînez-vous à créer des fichiers, à éditer du texte, à enregistrer des fichiers et à naviguer avec vi/vim et nano. Ce laboratoire vous aidera à maîtriser les commandes d'édition fondamentales abordées, telles que la suppression, la modification, la copie et le collage de texte.

Ce laboratoire vous aidera à appliquer les concepts dans des scénarios réels et à renforcer votre confiance en l'édition de texte sous Linux.

## Quiz Question

Quelle commande supprime la ligne actuelle dans Vim ?

## Quiz Answer

dd
