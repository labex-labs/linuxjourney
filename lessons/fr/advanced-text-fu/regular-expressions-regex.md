---
index: 1
lang: "fr"
title: "regex (Expressions Régulières)"
meta_title: "Regex (Expressions Régulières) - Maîtrise Avancée du Texte"
meta_description: "Maîtrisez les bases de Linux avec notre guide sur les expressions régulières (regex). Apprenez l'appariement de motifs avec grep, en utilisant des syntaxes comme ^, $, et []. C'est l'une des meilleures façons d'apprendre la manipulation de texte sous Linux et de faire progresser vos compétences."
meta_keywords: "expression régulière linux, regex, bases linux, appariement de motifs, grep, traitement de texte, apprendre linux, tutoriel linux, chemin rapide vers linux avancé"
---

## Lesson Content

Les expressions régulières, souvent abrégées en regex, sont un outil puissant pour la sélection de texte basée sur des motifs. Les comprendre est fondamental pour maîtriser la manipulation de texte sous Linux. Bien qu'il existe de nombreuses applications pour apprendre Linux, plonger dans des concepts fondamentaux comme « regular expression linux » est le moyen le plus rapide d'atteindre une maîtrise avancée de Linux. Elles utilisent des notations spéciales, dont certaines sont similaires aux jokers comme `*`.

Explorons quelques-uns des opérateurs regex les plus courants, qui sont presque universels dans les langages de programmation. Nous utiliserons le texte suivant comme exemple :

```plaintext
sally sells seashells
by the seashore
```

### Ancrage au début d'une ligne

Le symbole accent circonflexe `^` correspond au début d'une ligne. Il garantit que votre motif n'apparaît qu'au début.

```plaintext
^by
```

Ce motif correspondrait à la ligne « by the seashore » mais pas à « sally sells seashells ».

### Ancrage à la fin d'une ligne

Le symbole dollar `$` correspond à la fin d'une ligne. C'est le pendant de l'ancre `^`.

```plaintext
seashore$
```

Ce motif correspondrait à la ligne « by the seashore » car elle se termine par « seashore ».

### Correspondance de n'importe quel caractère unique

Le point `.` est un joker qui correspond à n'importe quel caractère unique.

```plaintext
b.
```

Dans notre exemple, cela correspondrait à « by ».

### Utilisation des crochets pour les ensembles de caractères

Les crochets `[]` vous permettent de spécifier un ensemble de caractères à faire correspondre. Cela offre plus de contrôle que le joker `.`.

```plaintext
s[ae]lls
```

Ceci correspondrait à « sells » et correspondrait également à « salls ».

Vous pouvez également utiliser des crochets pour spécifier ce qu'il ne faut _pas_ faire correspondre. Lorsque l'accent circonflexe `^` est le premier caractère à l'intérieur des crochets, il nie l'ensemble, correspondant à tout caractère _sauf_ ceux énumérés.

```plaintext
s[^e]lls
```

Ceci correspondrait à « salls » mais pas à « sells ».

Enfin, les crochets prennent en charge les plages pour définir efficacement un grand ensemble de caractères.

```plaintext
d[a-c]g
```

Ce motif correspondra à « dag », « dbg » et « dcg ». Sachez que les plages sont sensibles à la casse. Par exemple, `[a-c]` ne correspondra pas à `A`, `B` ou `C`.

Apprendre ces opérateurs est l'une des meilleures façons d'acquérir une efficacité en ligne de commande Linux.

## Exercise

Mettez vos connaissances en pratique. Voici quelques laboratoires pratiques pour renforcer votre compréhension des expressions régulières et de la correspondance de motifs :

1.  **[Rechercher du texte avec grep sous Linux](https://labex.io/fr/labs/comptia-search-text-with-grep-in-linux-590841)** - Dans ce laboratoire, vous apprendrez à rechercher du texte dans des fichiers sur un système Linux en utilisant la commande `grep`. Vous effectuerez des recherches de base, afficherez les numéros de ligne, utiliserez des ancres comme `^` et `$` pour correspondre aux positions des lignes, et exploiterez les expressions régulières de base et étendues pour une correspondance de motifs complexe.
2.  **[Traitement de texte et expressions régulières](https://labex.io/fr/labs/linux-text-processing-and-regular-expressions-18003)** - Apprenez les puissants outils de traitement de texte grep, sed et awk. Apprenez à utiliser les expressions régulières pour une manipulation de texte et une correspondance de motifs efficaces sous Linux.
3.  **[Extraction d'e-mails et de nombres](https://labex.io/fr/labs/linux-extracting-mails-and-numbers-17991)** - Dans ce défi, vous apprendrez à utiliser grep et les expressions régulières pour extraire des adresses e-mail et des nombres d'un fichier, démontrant des compétences essentielles en traitement de texte Linux.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance avec les expressions régulières et le traitement de texte.

## Quiz Question

Quelle expression régulière utiliseriez-vous pour correspondre à n'importe quel caractère unique ?

## Quiz Answer

.
