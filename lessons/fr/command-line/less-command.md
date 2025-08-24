---
index: 8
lang: "fr"
title: "less"
meta_title: "less - Ligne de commande"
meta_description: "Apprenez à utiliser la commande Linux 'less' pour une visualisation et une navigation efficaces des fichiers texte. Maîtrisez la pagination, la recherche et la sortie avec ce guide convivial pour débutants."
meta_keywords: "commande less, Linux less, afficher fichiers texte, naviguer fichiers, tutoriel Linux, Linux débutant, guide Linux"
---

## Lesson Content

Si vous visualisez des fichiers texte plus volumineux qu'une simple sortie, `less` est plus. (Il existe en fait une commande appelée `more` qui fait quelque chose de similaire, ce qui est ironique.) Le texte est affiché de manière paginée, vous pouvez donc naviguer dans un fichier texte page par page.

Allez-y et examinez le contenu d'un fichier avec `less`. Une fois que vous êtes dans la commande `less`, vous pouvez utiliser d'autres commandes clavier pour naviguer dans le fichier.

```bash
less /home/pete/Documents/text1
```

Utilisez les commandes suivantes pour naviguer dans `less` :

- `q` - Utilisé pour quitter `less` et revenir à votre shell.
- `Page up`, `Page down`, `Up` et `Down` - Naviguez à l'aide des touches fléchées et des touches de page.
- `g` - Se déplace au début du fichier texte.
- `G` - Se déplace à la fin du fichier texte.
- `/search` - Vous pouvez rechercher un texte spécifique dans le document texte. Faites précéder les mots que vous souhaitez rechercher par `/`.
- `h` - Si vous avez besoin d'un peu d'aide sur l'utilisation de `less` pendant que vous êtes dans `less`, utilisez l'aide.

## Exercise

Exécutez `less` sur un fichier, puis faites défiler le fichier vers le haut et vers le bas. Essayez de rechercher un mot spécifique. Naviguez rapidement au début ou à la fin du fichier.

Pour une pratique concrète de la commande `less`, essayez ce laboratoire interactif :

- [Linux less Command: File Paging](https://labex.io/fr/labs/linux-linux-less-command-file-paging-214301)

## Quiz Question

Comment quittez-vous une commande `less` ?

## Quiz Answer

q
