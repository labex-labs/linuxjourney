---
index: 10
lang: "fr"
title: "Agrandir et réduire"
meta_title: "Agrandir et réduire - Text-Fu"
meta_description: "Maîtrisez le formatage de texte sous Linux avec notre guide sur les commandes expand et unexpand. Apprenez à convertir les tabulations en espaces et les espaces en tabulations pour une mise en page de fichiers cohérente."
meta_keywords: "commande expand, commande unexpand, tabulations Linux, espaces Linux, formatage de texte, tutoriel Linux, Linux débutant, guide Linux"
---

## Lesson Content

Un espacement incohérent peut rendre les fichiers texte difficiles à lire. Bien que les tabulations soient destinées à créer une indentation uniforme, leur largeur d'affichage peut varier selon les éditeurs et les systèmes. Cela peut perturber le formatage et l'alignement du texte. Heureusement, Linux fournit des outils simples pour gérer cela en convertissant les tabulations en espaces et vice-versa. Ce guide Linux pour débutants vous expliquera le processus.

### Conversion des tabulations en espaces avec la commande expand

Lorsque vous avez besoin d'assurer un espacement cohérent, vous pouvez convertir les tabulations en un nombre standard d'espaces à l'aide de la commande `expand`. Cette commande lit un fichier et remplace chaque caractère de tabulation par un ensemble de caractères d'espacement, affichant le résultat sur la sortie standard.

```bash
expand sample.txt
```

Par défaut, la commande `expand` convertit chaque tabulation en 8 espaces. Cet utilitaire simple est un outil puissant pour améliorer le formatage du texte.

### Sauvegarde du résultat converti

La commande `expand` n'affiche que le texte converti dans votre terminal. Pour enregistrer les modifications, vous devez rediriger la sortie vers un nouveau fichier.

```bash
expand sample.txt > result.txt
```

Cette commande prend la sortie de `expand sample.txt` et l'écrit dans `result.txt`, vous donnant un nouveau fichier avec des espaces au lieu de tabulations.

### Conversion des espaces en tabulations avec la commande unexpand

L'opération inverse, la conversion des espaces en tabulations, est gérée par la commande `unexpand`. Cela peut être utile pour réduire la taille du fichier ou pour respecter les normes de codage qui exigent des tabulations.

```bash
unexpand -a result.txt
```

Par défaut, `unexpand` ne convertit que les espaces en début de chaque ligne. L'option `-a` indique à la commande `unexpand` de convertir toutes les occurrences de 8 espaces en une tabulation, et pas seulement celles situées au début d'une ligne, offrant ainsi un contrôle plus complet sur vos espaces et tabulations Linux.

## Exercise

Pour maîtriser la manipulation de texte et la redirection sous Linux, la pratique est essentielle. Les laboratoires pratiques suivants vous aideront à renforcer votre compréhension :

1. **[Redirection de l'entrée et de la sortie sous Linux](https://labex.io/fr/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Entraînez-vous à contrôler le flux de données des commandes en manipulant la sortie standard (stdout), l'erreur standard (stderr) et l'entrée standard (stdin) à l'aide d'opérateurs tels que `>` et `>>`.
2. **[Traitement de texte simple sous Linux](https://labex.io/fr/labs/linux-simple-text-processing-18004)** - Apprenez à utiliser des commandes puissantes comme `tr`, `col`, `join` et `paste` pour manipuler et analyser efficacement les données textuelles, améliorant ainsi vos compétences en ligne de commande pour le traitement des données.
3. **[Traitement de texte et expressions régulières sous Linux](https://labex.io/fr/labs/linux-text-processing-and-regular-expressions-18003)** - Découvrez les puissants outils de traitement de texte `grep`, `sed` et `awk`, et utilisez les expressions régulières pour une manipulation de texte et une recherche de motifs efficaces sous Linux.

Terminer ces laboratoires vous aidera à appliquer les concepts de transformation de texte et de manipulation de fichiers dans des scénarios réels, renforçant votre confiance avec les outils essentiels de la ligne de commande Linux.

## Quiz Question

Quelle commande est utilisée pour convertir les tabulations en espaces ? (Veuillez répondre en utilisant le nom de la commande anglaise en minuscules.)

## Quiz Answer

expand
