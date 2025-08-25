---
index: 1
lang: "fr"
title: "regex (Expressions régulières)"
meta_title: "regex (Expressions régulières) - Maîtrise avancée du texte"
meta_description: "Apprenez les expressions régulières (regex) pour la correspondance de motifs sous Linux. Comprenez la syntaxe regex comme ^, $, . et [] pour la manipulation de texte. Améliorez vos compétences grep !"
meta_keywords: "expressions régulières, regex, regex Linux, grep regex, correspondance de motifs, tutoriel regex, commandes Linux, débutant"
---

## Lesson Content

Les expressions régulières sont un outil puissant pour la sélection basée sur des motifs. Elles utilisent des notations spéciales similaires à celles que nous avons déjà rencontrées, comme le caractère générique `*`.

Nous allons passer en revue quelques-unes des expressions régulières les plus courantes ; elles sont presque universelles dans tous les langages de programmation.

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

L'ancre précédente `^` utilisée entre crochets signifie tout sauf les caractères à l'intérieur du crochet.

```plaintext
d[^i]g
would match: dog and dug but not dig
```

Les crochets peuvent également utiliser des plages pour augmenter le nombre de caractères que vous souhaitez utiliser.

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

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des expressions régulières et de la correspondance de motifs :

1. **[Rechercher du texte avec grep sous Linux](https://labex.io/fr/labs/comptia-search-text-with-grep-in-linux-590841)** - Dans ce laboratoire, vous apprendrez à rechercher du texte dans des fichiers sur un système Linux en utilisant la commande `grep`. Vous effectuerez des recherches de base, afficherez les numéros de ligne, utiliserez des ancres comme `^` et `$` pour faire correspondre les positions de ligne, et exploiterez les expressions régulières de base et étendues pour une correspondance de motifs complexe.
2. **[Traitement de texte et expressions régulières](https://labex.io/fr/labs/linux-text-processing-and-regular-expressions-18003)** - Apprenez les puissants outils de traitement de texte grep, sed et awk. Apprenez à utiliser les expressions régulières pour une manipulation de texte et une correspondance de motifs efficaces sous Linux.
3. **[Extraction de mails et de numéros](https://labex.io/fr/labs/linux-extracting-mails-and-numbers-17991)** - Dans ce défi, vous apprendrez à utiliser grep et les expressions régulières pour extraire des adresses e-mail et des numéros d'un fichier, démontrant ainsi des compétences essentielles en traitement de texte Linux.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance avec les expressions régulières et le traitement de texte.

## Quiz Question

Quelle expression régulière utiliseriez-vous pour faire correspondre un seul caractère ?

## Quiz Answer

.
