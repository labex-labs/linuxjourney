---
index: 10
lang: "fr"
title: "expand et unexpand"
meta_title: "expand et unexpand - Text-Fu"
meta_description: "Apprenez à convertir les tabulations en espaces avec la commande `expand` et les espaces en tabulations avec `unexpand`. Améliorez le formatage des fichiers texte avec ce tutoriel Linux."
meta_keywords: "commande expand, commande unexpand, tabulations Linux, espaces Linux, formatage de texte, tutoriel Linux, Linux débutant, guide Linux"
---

## Lesson Content

Dans notre leçon sur la commande `cut`, nous avions notre fichier `sample.txt` qui contenait une tabulation. Normalement, les tabulations montreraient une différence notable, mais certains fichiers texte ne le montrent pas assez bien. Avoir des tabulations dans un fichier texte peut ne pas fournir l'espacement désiré. Pour changer vos tabulations en espaces, utilisez la commande `expand`.

```bash
expand sample.txt
```

La commande ci-dessus affichera une sortie avec chaque tabulation convertie en un groupe d'espaces. Pour enregistrer cette sortie dans un fichier, utilisez la redirection de sortie comme indiqué ci-dessous.

```bash
expand sample.txt > result.txt
```

À l'opposé de `expand`, nous pouvons reconvertir chaque groupe d'espaces en une tabulation avec la commande `unexpand` :

```bash
unexpand -a result.txt
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la manipulation de texte et de la redirection sous Linux :

1. **[Redirection de l'entrée et de la sortie sous Linux](https://labex.io/fr/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Entraînez-vous à contrôler le flux de données des commandes en manipulant la sortie standard (stdout), l'erreur standard (stderr) et l'entrée standard (stdin) à l'aide d'opérateurs comme `>` et `>>`.
2. **[Traitement de texte simple](https://labex.io/fr/labs/linux-simple-text-processing-18004)** - Apprenez à utiliser des commandes puissantes comme `tr`, `col`, `join` et `paste` pour manipuler et analyser efficacement les données textuelles, améliorant ainsi vos compétences en ligne de commande pour le traitement des données.
3. **[Traitement de texte et expressions régulières](https://labex.io/fr/labs/linux-text-processing-and-regular-expressions-18003)** - Apprenez les puissants outils de traitement de texte `grep`, `sed` et `awk`, et utilisez les expressions régulières pour une manipulation de texte et une correspondance de motifs efficaces sous Linux.

Ces laboratoires vous aideront à appliquer les concepts de transformation de texte et de manipulation de fichiers dans des scénarios réels et à renforcer votre confiance avec les outils de ligne de commande Linux.

## Quiz Question

Quelle commande est utilisée pour convertir les tabulations en espaces ?

## Quiz Answer

expand
