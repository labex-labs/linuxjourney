---
index: 14
lang: "fr"
title: "uniq (Unique)"
meta_title: "uniq (Unique) - Text-Fu"
meta_description: "Explorez la commande uniq sous Linux pour filtrer et supprimer les lignes adjacentes dupliquées dans un texte. Apprenez à utiliser l'outil uniq linux avec des options comme -c, -u, -d et combinez-le avec sort pour un traitement de texte puissant."
meta_keywords: "commande uniq, uniq Linux, uniq linux, supprimer doublons, sort uniq, traitement texte, nettoyage données, tutoriel Linux"
---

## Lesson Content

La commande `uniq` (unique) est un outil essentiel pour le traitement de texte sous Linux. Elle vous aide à filtrer et à gérer les lignes dupliquées dans un fichier texte, mais il est important de comprendre son fonctionnement pour l'utiliser efficacement.

### Suppression de base des doublons

La fonction principale de la commande `uniq` est de supprimer les lignes adjacentes dupliquées. Imaginez que vous avez un fichier nommé `reading.txt` avec le contenu suivant :

```plaintext
book
book
paper
paper
article
article
magazine
```

Pour supprimer les lignes répétées, vous pouvez exécuter la commande `uniq` :

```bash
$ uniq reading.txt
book
paper
article
magazine
```

Comme vous pouvez le constater, `uniq` affiche une version du fichier sans les lignes adjacentes dupliquées.

### Options de filtrage avancées

La commande `uniq` fournit également plusieurs options pour une analyse plus détaillée.

Pour compter les occurrences de chaque ligne, utilisez l'indicateur `-c` (count) :

```bash
$ uniq -c reading.txt
      2 book
      2 paper
      2 article
      1 magazine
```

Pour afficher uniquement les lignes qui ne sont pas répétées (c'est-à-dire qui sont uniques), utilisez l'indicateur `-u` (unique) :

```bash
$ uniq -u reading.txt
magazine
```

Inversement, pour afficher uniquement les lignes qui sont dupliquées, utilisez l'indicateur `-d` (duplicated) :

```bash
$ uniq -d reading.txt
book
paper
article
```

### L'importance du tri

Un détail critique concernant la commande **uniq linux** est qu'elle ne détecte les lignes dupliquées que si elles sont directement adjacentes les unes aux autres. Si les doublons sont dispersés dans le fichier, `uniq` ne les identifiera pas.

Considérez cette version de `reading.txt` où les doublons ne sont pas adjacents :

```plaintext
book
paper
book
paper
article
magazine
article
```

L'exécution de `uniq` sur ce fichier produira un résultat surprenant :

```bash
$ uniq reading.txt
book
paper
book
paper
article
magazine
article
```

Aucune ligne n'a été supprimée car aucune ligne identique n'était côte à côte. Pour résoudre ce problème, vous devez d'abord trier le contenu du fichier. En acheminant la sortie de `sort` vers `uniq`, vous vous assurez que toutes les lignes identiques deviennent adjacentes, permettant à `uniq` de fonctionner correctement. Cette combinaison est un modèle puissant et courant dans le scripting shell.

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

Cette commande trie d'abord les lignes par ordre alphabétique, puis `uniq` filtre les doublons, vous donnant une liste claire des entrées uniques.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du traitement de texte avec `uniq` et `sort` :

1. **[Commande Linux uniq : Filtrage des doublons](https://labex.io/fr/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - Apprenez à utiliser la commande Linux `uniq` en combinaison avec `sort` pour identifier, filtrer et analyser les lignes dupliquées dans les fichiers texte.
2. **[Commande Linux sort : Tri de texte](https://labex.io/fr/labs/linux-linux-sort-command-text-sorting-219196)** - Entraînez-vous à utiliser la commande `sort` pour organiser les lignes des fichiers texte, une étape cruciale avant d'utiliser `uniq` efficacement.
3. **[Comptage de mots et tri](https://labex.io/fr/labs/linux-word-count-and-sorting-388125)** - Découvrez les outils essentiels de traitement de texte Linux `wc` (compte de mots) et `sort` dans ce défi pratique. Apprenez à compter les lignes, les mots et les caractères, à trouver les modèles fréquents et à trier les données efficacement pour diverses tâches d'analyse de texte.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans le traitement de texte et la manipulation de données sous Linux.

## Quiz Question

Quelle commande utiliseriez-vous pour supprimer les lignes dupliquées adjacentes dans un fichier ? Veuillez répondre en utilisant uniquement le nom de la commande en minuscules anglaises.

## Quiz Answer

uniq
