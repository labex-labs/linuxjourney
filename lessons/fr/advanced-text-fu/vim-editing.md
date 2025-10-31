---
index: 7
lang: "fr"
title: "Édition Vim"
meta_title: "Édition Vim - Maîtrise Avancée du Texte"
meta_description: "Un tutoriel Vim pour débutants sur les commandes d'édition essentielles. Apprenez à supprimer, modifier, copier (yank) et coller du texte dans l'éditeur Vim pour améliorer votre flux de travail Linux."
meta_keywords: "Édition Vim, commandes Vim, éditeur de texte Linux, tutoriel Vim, guide Vim, Vim débutant, commande dd, suppression Vim"
---

## Lesson Content

L'édition de texte dans Vim est une fonctionnalité puissante qui repose sur la combinaison d'opérateurs et de mouvements depuis le mode Normal. Cette approche vous permet de supprimer, modifier, copier (yank) et coller (put) efficacement du texte. Avant d'exécuter toute commande, appuyez sur `Esc` pour vous assurer d'être en mode Normal.

### Comprendre les Opérateurs et les Mouvements de Vim

Le cœur de l'édition Vim est la formule : `opérateur + mouvement`. Un opérateur est une action (comme `d` pour supprimer), et un mouvement est un déplacement (comme `w` pour mot). Par exemple, `dw` combine l'opérateur de suppression avec le mouvement mot pour supprimer un mot. Vous pouvez également utiliser des compteurs pour répéter une action, comme `2dw` pour supprimer deux mots.

### Supprimer du Texte dans Vim

L'opérateur de suppression est `d`. C'est l'une des commandes Vim les plus courantes pour la manipulation de texte.

- `x` – Supprime le caractère directement sous le curseur.
- `dw` – Supprime du curseur jusqu'au début du mot suivant.
- `d$` – Supprime du curseur jusqu'à la fin de la ligne actuelle.
- `dd` – La commande `dd` supprime la ligne entière actuelle.
- `3dd` – Supprime trois lignes, en commençant par la ligne actuelle.

### Modifier du Texte

L'opérateur de modification, `c`, fonctionne de manière similaire à la suppression mais vous place en mode Insertion après avoir effectué l'action. Ceci est utile pour remplacer du texte.

- `cw` – Modifie le texte du curseur jusqu'à la fin du mot.
- `c$` – Modifie le texte du curseur jusqu'à la fin de la ligne.
- `cc` – Modifie la ligne entière actuelle.

### Copier et Coller dans Vim

Dans Vim, copier s'appelle "yanking" (opérateur `y`), et coller s'appelle "putting".

- `yw` – Yank (copie) un mot.
- `yy` – Yank la ligne entière actuelle.
- `p` – Put (colle) le texte yanké après le curseur ou sur la ligne inférieure.
- `P` – Put le texte avant le curseur ou sur la ligne supérieure.

### Autres Commandes d'Édition Utiles

Ce guide Vim ne serait pas complet sans quelques autres commandes pratiques.

- `r{char}` – Remplace le caractère unique sous le curseur par le caractère spécifié.
- `R` – Entre en mode Remplacement, vous permettant d'écraser du texte en continu jusqu'à ce que vous appuyiez sur `Esc`.
- `J` – Joint la ligne actuelle avec la suivante.
- `.` – Répète la dernière modification que vous avez effectuée, une commande très puissante et efficace.

La combinaison d'opérateurs avec différents mouvements débloque tout le potentiel de cet éditeur de texte Linux. Par exemple, `d}` supprime jusqu'au paragraphe suivant, et `caw` modifie "un mot" (le mot sous le curseur y compris tout espace environnant).

## Exercise

Pour mettre vos connaissances en pratique, nous vous recommandons le laboratoire pratique suivant. Il vous aidera à maîtriser les commandes d'édition fondamentales abordées dans ce tutoriel Vim.

1. **[Modifier des fichiers texte sous Linux avec Vim et Nano](https://labex.io/fr/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Entraînez-vous à créer des fichiers, à modifier du texte, à sauvegarder des fichiers et à naviguer avec vi/vim et nano. Ce laboratoire vous aidera à appliquer des concepts tels que la suppression, la modification, le yanking et le putting de texte dans des scénarios réels.

## Quiz Question

Which command deletes the current line in Vim? (Please answer in English, paying attention to case sensitivity).

## Quiz Answer

dd
