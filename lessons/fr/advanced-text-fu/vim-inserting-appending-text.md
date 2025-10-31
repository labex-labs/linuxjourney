---
index: 6
lang: "fr"
title: "Insertion et Ajout de Texte dans Vim"
meta_title: "Insertion et Ajout de Texte dans Vim - Maîtrise Avancée"
meta_description: "Apprenez la différence entre les modes insertion et ajout de Vim. Maîtrisez les commandes comme 'i', 'a' et 'o' pour éditer efficacement le texte, ajouter du contenu et insérer une ligne dans Vim."
meta_keywords: "vim ajouter, ajouter vs insérer vim, vim insertion vs ajout, vim insérer ligne, édition de texte vim, commandes vim, tutoriel vim, mode insertion, mode ajout"
---

## Lesson Content

Dans Vim, vous travaillerez principalement dans deux modes : le mode Normal pour exécuter des commandes et le mode Insertion pour taper du texte. Pour passer du mode Insertion au mode Normal, appuyez simplement sur la touche `Esc`.

Il existe plusieurs commandes pour entrer en mode Insertion, chacune plaçant le curseur à une position de départ différente pour votre saisie de texte.

### Commandes d'Insertion de Base

La manière la plus fondamentale de commencer à taper est avec la commande `i`.

- `i` – **i**nsérer du texte avant la position actuelle du curseur.

Cette commande vous fait passer en mode Insertion, vous permettant de taper directement dans le fichier.

### Vim Append vs Insert (Ajouter vs Insérer)

Un point de comparaison courant est **vim append vs insert** (vim ajouter vs insérer). Bien que les deux entrent en mode Insertion, leurs points de départ diffèrent par rapport au curseur. Comprendre la distinction **vim insert vs append** est essentiel pour un mouvement et une édition efficaces.

- `a` – **a**jouter du texte après la position actuelle du curseur.
- `I` – **I**nsérer du texte au début de la ligne actuelle.
- `A` – **A**jouter du texte à la fin de la ligne actuelle.

Utiliser `a` au lieu de `i` vous fait gagner une frappe (en déplaçant le curseur d'un espace vers la droite avant d'insérer). De même, `A` est un raccourci puissant pour commencer immédiatement à taper à la fin d'une ligne. Maîtriser les commandes **vim append** est une étape importante pour améliorer votre vitesse d'édition.

### Comment Vim Ajouter une Ligne

Lorsque vous avez besoin d'ajouter de nouvelles lignes de texte, vous n'avez pas besoin d'appuyer manuellement sur Entrée à la fin d'une ligne. Vim fournit des commandes dédiées pour ouvrir des lignes et entrer immédiatement en mode Insertion.

- `o` – **o**uvrir une nouvelle ligne sous la ligne actuelle et entrer en mode Insertion.
- `O` – **O**uvrir une nouvelle ligne au-dessus de la ligne actuelle et entrer en mode Insertion.

Ces commandes sont extrêmement utiles lorsque vous devez rapidement **vim add line** (vim ajouter ligne) lors du codage ou de l'écriture.

Astuce : Vous pouvez préfixer ces commandes avec un nombre pour les répéter. Par exemple, taper `3o` en mode Normal ouvrira trois nouvelles lignes vides sous la ligne actuelle et vous placera en mode Insertion sur la première de ces nouvelles lignes.

## Exercise

La pratique est essentielle pour maîtriser Vim. Le laboratoire suivant fournit un environnement pratique pour renforcer votre compréhension des capacités d'édition de texte de Vim.

1. **[Modifier des fichiers texte sous Linux avec Vim et Nano](https://labex.io/fr/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Entraînez-vous à créer des fichiers, à modifier du texte, à sauvegarder des fichiers et à naviguer avec vi/vim et nano. Ce laboratoire vous aidera à maîtriser les compétences fondamentales de l'utilisation des modes Normal et Insertion de Vim.

Appliquer ces concepts dans des scénarios réels vous aidera à gagner en confiance dans l'édition de texte sous Linux en utilisant Vim.

## Quiz Question

Quelle touche entre en mode Insertion avant le curseur ? Veuillez répondre avec une seule lettre anglaise minuscule.

## Quiz Answer

i
