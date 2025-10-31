---
index: 4
lang: "fr"
title: "Motifs de Recherche Vim"
meta_title: "Motifs de Recherche Vim - Maîtrise Avancée du Texte"
meta_description: "Apprenez à effectuer une recherche Vim avant et arrière en utilisant des motifs. Maîtrisez les techniques de recherche Vim pour trouver rapidement du texte et naviguer entre les résultats avec 'n' et 'N'."
meta_keywords: "Recherche Vim, recherche Vim, commandes Vim, éditeur de texte Linux, tutoriel Vim, guide Vim, motifs de recherche"
---

## Lesson Content

La recherche de texte est une tâche fondamentale dans tout éditeur. Vim fournit des moyens puissants et rapides d'effectuer une `recherche vim` directement en mode normal. Explorons comment utiliser ces modèles de recherche pour améliorer votre flux de travail.

### Recherche Avant

Pour effectuer une `recherche vim` avant standard, appuyez simplement sur la touche `/` en mode normal, suivie de votre terme de recherche. Lorsque vous appuyez sur Entrée, Vim sautera à la première occurrence du terme après votre curseur.

```plaintext
My pretty file is very pretty.

/pretty

This will find the first "pretty" word after the cursor.
```

### Recherche Arrière

De même, vous pouvez rechercher en arrière à partir de la position de votre curseur. Utilisez la touche `?` suivie de votre terme de recherche. Vim trouvera la première occurrence avant votre curseur.

```plaintext
My pretty file is very pretty.

?pretty

This will find the last "pretty" word in the file first.
```

### Navigation dans les Résultats de Recherche

Une fois qu'une recherche est lancée, vous pouvez facilement naviguer à travers toutes les correspondances dans le fichier.

- Appuyez sur `n` pour sauter à la correspondance **suivante** dans la direction de la recherche initiale.
- Appuyez sur `N` pour sauter à la correspondance **précédente**, se déplaçant dans la direction opposée à la recherche initiale.

### Recherche Efficace dans Vim (Vim Lookup)

Les commandes `/` et `?` sont le cœur de toute opération de `recherche vim` (vim lookup). Que vous ayez besoin de trouver le nom d'une fonction spécifique, une variable, ou juste un mot, ce mécanisme de recherche est votre outil principal. Maîtriser ce simple processus de `recherche vim` (vim lookup) est essentiel pour une navigation et une édition efficaces.

## Exercise

Pour appliquer ces concepts, essayez le laboratoire pratique suivant. Il vous aidera à maîtriser les outils essentiels d'édition de texte, y compris les fonctionnalités de recherche.

1. **[Modifier des fichiers texte sous Linux avec Vim et Nano](https://labex.io/fr/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Entraînez-vous à créer, modifier, sauvegarder et naviguer dans des fichiers texte avec Vim et Nano.

## Quiz Question

Quelle touche est utilisée pour lancer une recherche avant dans Vim ?

## Quiz Answer

/
