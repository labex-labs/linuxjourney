---
index: 14
lang: "fr"
title: "uniq (Unique)"
meta_title: "uniq (Unique) - Text-Fu"
meta_description: "Apprenez à utiliser la commande Linux `uniq` pour supprimer les lignes en double des fichiers texte. Découvrez des options comme -c, -u, -d, et combinez-la avec `sort` pour un nettoyage efficace des données."
meta_keywords: "commande uniq, Linux uniq, supprimer les doublons, sort uniq, tutoriel Linux, traitement de texte, Linux pour débutants, guide Linux"
---

## Lesson Content

La commande `uniq` (unique) est un autre outil utile pour l'analyse de texte.

Supposons que vous ayez un fichier avec beaucoup de doublons :

```plaintext
reading.txt
book
book
paper
paper
article
article
magazine
```

Et que vous vouliez supprimer les doublons ; eh bien, vous pouvez utiliser la commande `uniq` :

```bash
$ uniq reading.txt
book
paper
article
magazine
```

Obtenons le nombre d'occurrences d'une ligne :

```bash
$ uniq -c reading.txt
2 book
2 paper
2 article
1 magazine
```

Obtenons uniquement les valeurs uniques :

```bash
$ uniq -u reading.txt
magazine
```

Obtenons uniquement les valeurs en double :

```bash
$ uniq -d reading.txt
book
paper
article
```

**Note** : `uniq` ne détecte pas les lignes en double à moins qu'elles ne soient adjacentes. Par exemple :

Supposons que vous ayez un fichier avec des doublons qui ne sont pas adjacents :

```plaintext
reading.txt
book
paper
book
paper
article
magazine
article
```

```bash
$ uniq reading.txt
reading.txt
book
paper
book
paper
article
magazine
article
```

Le résultat renvoyé par `uniq` contiendra toutes les entrées, contrairement au tout premier exemple.

Pour surmonter cette limitation de `uniq`, nous pouvons utiliser `sort` en combinaison avec `uniq` :

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du traitement de texte avec `uniq` et `sort` :

1. **[Commande Linux uniq : Filtrage des doublons](https://labex.io/fr/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - Apprenez à utiliser la commande Linux `uniq` en combinaison avec `sort` pour identifier, filtrer et analyser les lignes en double dans les fichiers texte.
2. **[Commande Linux sort : Tri de texte](https://labex.io/fr/labs/linux-linux-sort-command-text-sorting-219196)** - Entraînez-vous à utiliser la commande `sort` pour organiser les lignes de fichiers texte, une étape cruciale avant d'utiliser `uniq` efficacement.
3. **[Comptage de mots et tri](https://labex.io/fr/labs/linux-word-count-and-sorting-388125)** - Apprenez les outils essentiels de traitement de texte Linux `wc` (word count) et `sort` dans ce défi pratique. Apprenez à compter les lignes, les mots et les caractères, à trouver des motifs fréquents et à trier les données efficacement pour diverses tâches d'analyse de texte.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans le traitement de texte et la manipulation de données sous Linux.

## Quiz Question

Quelle commande utiliseriez-vous pour supprimer les doublons dans un fichier ?

## Quiz Answer

uniq
