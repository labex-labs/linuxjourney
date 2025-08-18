---
index: 8
lang: "fr"
title: "less"
meta_title: "less - Command Line"
meta_description: "Apprenez à utiliser la commande Linux 'less' pour une visualisation et une navigation efficaces des fichiers texte. Maîtrisez la pagination, la recherche et la sortie avec ce guide convivial pour débutants."
meta_keywords: "commande less, Linux less, visualiser fichiers texte, naviguer fichiers, tutoriel Linux, Linux débutant, guide Linux"
---

## Lesson Content

Si vous visualisez des fichiers texte plus volumineux qu'une simple sortie, `less` est plus. (Il existe en fait une commande appelée `more` qui fait quelque chose de similaire, c'est donc ironique.) Le texte est affiché de manière paginée, vous pouvez donc naviguer dans un fichier texte page par page.

Allez-y et examinez le contenu d'un fichier avec `less`. Une fois que vous êtes dans la commande `less`, vous pouvez utiliser d'autres commandes clavier pour naviguer dans le fichier.

```bash
less /home/pete/Documents/text1
```

Utilisez les commandes suivantes pour naviguer dans `less` :

- `q` - Utilisé pour quitter `less` et revenir à votre shell.
- `Page up`, `Page down`, `Up` et `Down` - Naviguez à l'aide des touches fléchées et des touches de page.
- `g` - Se déplace au début du fichier texte.
- `G` - Se déplace à la fin du fichier texte.
- `/search` - Vous pouvez rechercher un texte spécifique dans le document texte. Faites précéder les mots que vous souhaitez rechercher de `/`.
- `h` - Si vous avez besoin d'un peu d'aide sur la façon d'utiliser `less` pendant que vous êtes dans `less`, utilisez help.

## Exercise

Exécutez `less` sur un fichier, puis parcourez le fichier page par page. Essayez de rechercher un mot spécifique. Naviguez rapidement au début ou à la fin du fichier.

## Quiz Question

Comment quittez-vous une commande `less` ?

## Quiz Answer

q
