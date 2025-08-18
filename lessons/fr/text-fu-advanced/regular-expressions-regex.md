---
index: 1
lang: "fr"
title: "regex (Expressions Régulières)"
meta_title: "regex (Expressions Régulières) - Text-Fu Avancé"
meta_description: "Apprenez les expressions régulières (regex) pour la correspondance de motifs sous Linux. Comprenez la syntaxe regex comme ^, $, ., et [] pour la manipulation de texte. Améliorez vos compétences grep !"
meta_keywords: "expressions régulières, regex, regex Linux, grep regex, correspondance de motifs, tutoriel regex, commandes Linux, débutant"
---

## Lesson Content

Les expressions régulières sont un outil puissant pour la sélection basée sur des motifs. Elles utilisent des notations spéciales similaires à celles que nous avons déjà rencontrées, comme le joker `*`.

Nous allons passer en revue quelques-unes des expressions régulières les plus courantes ; celles-ci sont presque universelles avec n'importe quel langage de programmation.

Nous utiliserons cette phrase comme chaîne de test :

```plaintext
sally sells seashells
by the seashore
```

### 1. Début d'une ligne avec ^

```plaintext
^by
would match the line "by the seashore"
```

### 2. Fin d'une ligne avec $

```plaintext
seashore$
would match the line "by the seashore"
```

### 3. Correspondance de n'importe quel caractère unique avec

```plaintext
b.
would match by
```

### 4. Notation entre crochets avec [] et ()

Cela peut être un peu délicat. Les crochets nous permettent de spécifier les caractères trouvés à l'intérieur du crochet.

```plaintext
d[iou]g
would match: dig, dog, dug
```

L'ancre précédente `^` lorsqu'elle est utilisée entre crochets signifie tout sauf les caractères à l'intérieur du crochet.

```plaintext
d[^i]g
would match: dog and dug but not dig
```

Les crochets peuvent également utiliser des plages pour augmenter la quantité de caractères que vous souhaitez utiliser.

```plaintext
d[a-c]g
will match patterns like dag, dbg, and dcg
```

Soyez prudent, cependant, car les crochets sont sensibles à la casse :

```plaintext
d[A-C]g
will match dAg, dBg and dCg but not dag, dbg and dcg
```

Et ce sont quelques expressions régulières de base.

## Exercise

Essayez de combiner les expressions régulières avec `grep` et de rechercher dans certains fichiers.

```bash
grep [regular expression here] [file]
```

## Quiz Question

Quelle expression régulière utiliseriez-vous pour faire correspondre un seul caractère ?

## Quiz Answer

.
