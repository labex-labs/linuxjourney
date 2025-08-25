---
index: 8
lang: "fr"
title: "less"
meta_title: "less - Ligne de commande"
meta_description: "Apprenez à utiliser la commande Linux 'less' pour une visualisation et une navigation efficaces des fichiers texte. Maîtrisez la pagination, la recherche et la sortie avec ce guide convivial pour débutants."
meta_keywords: "commande less, Linux less, visualiser fichiers texte, naviguer fichiers, tutoriel Linux, Linux débutant, guide Linux"
---

## Lesson Content

Si vous visualisez des fichiers texte plus grands qu'une simple sortie, `less` est plus. (Il existe en fait une commande appelée `more` qui fait quelque chose de similaire, ce qui est ironique.) Le texte est affiché de manière paginée, vous pouvez donc naviguer dans un fichier texte page par page.

Allez-y et examinez le contenu d'un fichier avec `less`. Une fois que vous êtes dans la commande `less`, vous pouvez utiliser d'autres commandes clavier pour naviguer dans le fichier.

```bash
less /home/pete/Documents/text1
```

Utilisez les commandes suivantes pour naviguer dans `less` :

- `q` - Utilisé pour quitter `less` et revenir à votre shell.
- `Page up`, `Page down`, `Up` et `Down` - Naviguez à l'aide des touches fléchées et des touches de page.
- `g` - Se déplace au début du fichier texte.
- `G` - Se déplace à la fin du fichier texte.
- `/search` - Vous pouvez rechercher un texte spécifique à l'intérieur du document texte. Faites précéder les mots que vous souhaitez rechercher de `/`.
- `h` - Si vous avez besoin d'un peu d'aide sur l'utilisation de `less` pendant que vous êtes dans `less`, utilisez l'aide.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la visualisation et de la navigation dans les fichiers texte sous Linux :

1. **[Commande Linux less : Pagination de fichiers](https://labex.io/fr/labs/linux-linux-less-command-file-paging-214301)** - Apprenez la commande Linux 'less' pour une visualisation et une navigation efficaces des fichiers texte, y compris la recherche, les numéros de ligne et la correspondance de motifs.
2. **[Commande Linux more : Défilement de fichiers](https://labex.io/fr/labs/linux-linux-more-command-file-scrolling-214299)** - Apprenez la commande Linux 'more' pour une visualisation efficace des fichiers texte, couvrant l'utilisation de base, le démarrage à partir de lignes spécifiques et la personnalisation de l'affichage.
3. **[Visualisation des fichiers journaux et de configuration sous Linux](https://labex.io/fr/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Apprenez les compétences essentielles de la ligne de commande Linux pour visualiser et naviguer efficacement dans les fichiers texte, y compris les journaux système et les fichiers de configuration, à l'aide de commandes comme `cat`, `more` et `less`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la manipulation et la navigation des fichiers texte.

## Quiz Question

Comment quittez-vous une commande `less` ?

## Quiz Answer

q
