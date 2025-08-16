---
title: "uniq (Unique)"
description: "Apprenez à utiliser la commande Linux `uniq` pour supprimer les lignes en double des fichiers texte. Découvrez des options comme -c, -u, -d, et combinez-les avec `sort` pour un nettoyage efficace des données."
keywords: "commande uniq, uniq Linux, supprimer les doublons, sort uniq, tutoriel Linux, traitement de texte, Linux pour débutants, guide Linux"
---

## Lesson Content

La commande `uniq` (unique) est un autre outil utile pour l'analyse de texte.

Disons que vous aviez un fichier avec beaucoup de doublons :

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

Obtenons le compte du nombre d'occurrences d'une ligne :

```bash
$ uniq -c reading.txt
2 book
2 paper
2 article
1 magazine
```

Obtenons juste les valeurs uniques :

```bash
$ uniq -u reading.txt
magazine
```

Obtenons juste les valeurs en double :

```bash
$ uniq -d reading.txt
book
paper
article
```

**Note** : `uniq` ne détecte pas les lignes en double à moins qu'elles ne soient adjacentes. Par exemple :

Disons que vous aviez un fichier avec des doublons qui ne sont pas adjacents :

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

Quel résultat obtiendriez-vous si vous essayiez `uniq -uc` ?

## Quiz Question

Quelle commande utiliseriez-vous pour supprimer les doublons dans un fichier ?

## Quiz Answer

uniq
