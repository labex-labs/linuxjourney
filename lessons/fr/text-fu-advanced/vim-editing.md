---
index: 7
lang: "fr"
title: "Édition Vim"
meta_title: "Édition Vim - Text-Fu Avancé"
meta_description: "Apprenez les bases de l'édition Vim : supprimer, modifier, copier et coller du texte efficacement. Maîtrisez les commandes Vim essentielles pour les débutants et améliorez vos compétences en édition de texte sous Linux."
meta_keywords: "édition Vim, commandes Vim, éditeur de texte Linux, tutoriel Vim, guide Vim, Vim pour débutants, commande dd, suppression Vim"
---

## Lesson Content

L'édition dans Vim se fait à partir du mode Normal en utilisant des opérateurs et des mouvements. Vous pouvez supprimer, modifier, copier (yank), coller (put) et remplacer du texte efficacement.

- Appuyez sur `Esc` pour vous assurer d'être en mode Normal avant d'utiliser ces commandes.

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

Yank et Put (copier/coller):

- `yw` – copie le mot
- `yy` – copie la ligne actuelle
- `p` – colle (paste) après le curseur ou sous la ligne
- `P` – colle (paste) avant le curseur ou au-dessus de la ligne

Remplacer et autres modifications pratiques:

- `r{char}` – remplace le caractère sous le curseur par `{char}`
- `R` – entre en mode Remplacement pour écraser le texte
- `J` – joint la ligne actuelle avec la ligne suivante
- `.` – répète la dernière modification

Combinez les opérateurs avec les mouvements pour plus de puissance : `d}` supprime jusqu'au paragraphe suivant ; `caw` modifie « un mot » (mot sous le curseur, y compris l'espace environnant).

## Exercise

Ouvrez un fichier avec `vim [file]` et essayez : `dw`, `cw`, `yy` puis `p`, `dd`, `J`, et `.` pour répéter une modification.

## Quiz Question

Quelle commande supprime la ligne actuelle dans Vim ?

## Quiz Answer

dd
