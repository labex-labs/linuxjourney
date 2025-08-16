---
lang: "fr"
title: "expand et unexpand"
description: "Apprenez à convertir les tabulations en espaces avec la commande `expand` et les espaces en tabulations avec `unexpand`. Améliorez le formatage des fichiers texte avec ce tutoriel Linux."
keywords: "commande expand, commande unexpand, tabulations Linux, espaces Linux, formatage de texte, tutoriel Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

Dans notre leçon sur la commande `cut`, nous avions notre fichier `sample.txt` qui contenait une tabulation. Normalement, les tabulations afficheraient une différence notable, mais certains fichiers texte ne la montrent pas assez bien. Avoir des tabulations dans un fichier texte peut ne pas fournir l'espacement désiré. Pour changer vos tabulations en espaces, utilisez la commande `expand`.

```bash
expand sample.txt
```

La commande ci-dessus affichera la sortie avec chaque tabulation convertie en un groupe d'espaces. Pour enregistrer cette sortie dans un fichier, utilisez la redirection de sortie comme indiqué ci-dessous.

```bash
expand sample.txt > result.txt
```

À l'opposé de `expand`, nous pouvons reconvertir chaque groupe d'espaces en une tabulation avec la commande `unexpand`:

```bash
unexpand -a result.txt
```

## Exercise

Que se passe-t-il si vous tapez simplement `expand` sans entrée de fichier ?

## Quiz Question

Quelle commande est utilisée pour convertir les tabulations en espaces ?

## Quiz Answer

expand
