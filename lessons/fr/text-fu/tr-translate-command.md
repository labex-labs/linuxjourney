---
index: 13
lang: "fr"
title: "tr (Traduire)"
meta_title: "tr (Traduire) - Text-Fu"
meta_description: "Apprenez la commande Linux tr avec des exemples pour traduire des caractères, supprimer des caractères, compresser les répétitions, utiliser des classes de caractères et nettoyer du texte."
meta_keywords: "commande linux tr, commande tr, tr -d, tr -s, traduire caractères, supprimer caractères, classes de caractères, traitement texte linux"
---

## Lesson Content

La commande `tr`, abréviation de translate (traduire), est un utilitaire en ligne de commande qui traduit, supprime ou compresse des caractères depuis l'entrée standard. Elle est utile pour des manipulations simples de texte et est souvent utilisée avec des pipes pour traiter la sortie d'autres commandes.

La syntaxe de base est :

```bash
tr [OPTIONS] SET1 [SET2]
```

Contrairement à des outils comme `sed` ou `awk`, `tr` fonctionne caractère par caractère. Il ne comprend pas les mots, les colonnes ou les expressions régulières de la même manière. Cela le rend rapide et simple pour des tâches telles que changer la casse, supprimer des chiffres et normaliser les espaces répétés.

### Traduction de caractères basique

L'utilisation la plus courante de `tr` est de substituer un ensemble de caractères par un autre. Par exemple, vous pouvez facilement traduire tous les caractères minuscules en majuscules.

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

Dans cet exemple, nous avons passé la sortie de `echo` à la commande `tr`. La commande `tr` a alors traduit la plage de caractères `a-z` en les caractères correspondants dans la plage `A-Z`.

Vous pouvez aussi traduire un caractère en un autre :

```bash
$ echo "2026-06-23" | tr '-' '/'
2026/06/23
```

Chaque caractère dans `SET1` correspond au caractère à la même position dans `SET2`.

```bash
$ echo "abc123" | tr 'abc' 'ABC'
ABC123
```

Ici, `a` devient `A`, `b` devient `B` et `c` devient `C`.

### Suppression de caractères avec -d

Une autre fonctionnalité puissante est la capacité de supprimer des caractères spécifiques avec l'option `-d`. Cela est particulièrement utile pour nettoyer du texte. Par exemple, si vous voulez supprimer tous les chiffres d'une chaîne, vous pouvez utiliser :

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

Ici, `tr -d` a supprimé chaque caractère dans l'ensemble spécifié, de `0` à `9`.

Vous pouvez supprimer la ponctuation d'une chaîne en utilisant une classe de caractères :

```bash
$ echo "Hello, world!" | tr -d '[:punct:]'
Hello world
```

Vous pouvez aussi supprimer les caractères de nouvelle ligne pour joindre des lignes ensemble :

```bash
$ printf "one\ntwo\nthree\n" | tr -d '\n'
onetwothree
```

### Compression des caractères répétés

La commande `tr` peut aussi "compresser" les caractères répétés en une seule occurrence avec l'option `-s`. C'est idéal pour normaliser un texte avec des espaces en trop.

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

Dans ce cas, `tr -s ' '` a remplacé les séquences de plusieurs espaces par un seul espace, rendant la sortie beaucoup plus propre.

Vous pouvez aussi compresser les nouvelles lignes répétées :

```bash
$ printf "one\n\n\nTwo\n" | tr -s '\n'
one
Two
```

### Utilisation des classes de caractères

Les classes de caractères rendent les commandes `tr` plus lisibles et portables. Les classes courantes incluent :

- `[:lower:]` : Lettres minuscules.
- `[:upper:]` : Lettres majuscules.
- `[:digit:]` : Chiffres.
- `[:alpha:]` : Lettres.
- `[:alnum:]` : Lettres et chiffres.
- `[:space:]` : Caractères d'espacement.
- `[:punct:]` : Caractères de ponctuation.

Par exemple, convertir du texte en minuscules en majuscules avec des classes de caractères :

```bash
$ echo "linux journey" | tr '[:lower:]' '[:upper:]'
LINUX JOURNEY
```

Supprimez tout sauf les lettres et les chiffres en utilisant `-c` avec `-d`. L'option `-c` signifie complément, ou "tout ce qui n'est pas dans cet ensemble".

```bash
$ echo "user@example.com!" | tr -cd '[:alnum:]'
userexamplecom
```

### Combinaison de suppression et compression

Vous pouvez combiner les options lors du nettoyage de texte. Cet exemple supprime la ponctuation, puis compresse les espaces répétés :

```bash
$ echo "Hello,,,     world!!!" | tr -d '[:punct:]' | tr -s ' '
Hello world
```

Pour une entrée séparée par des tabulations, vous pouvez traduire les tabulations en virgules :

```bash
$ printf "name\tlevel\npete\tbeginner\n" | tr '\t' ','
name,level
pete,beginner
```

### Options courantes de tr

Voici les options que vous utiliserez le plus souvent :

- `-d` : Supprime les caractères dans `SET1`.
- `-s` : Compresse les caractères répétés dans `SET1`.
- `-c` : Utilise le complément de `SET1`.
- `-t` : Tronque `SET1` à la longueur de `SET2` avant de traduire.

### Questions fréquentes

**Pourquoi tr lit-il depuis un pipe ?** `tr` lit depuis l'entrée standard, il est donc couramment utilisé après des commandes comme `echo`, `cat`, `printf` ou d'autres commandes produisant du texte.

**Est-ce que tr remplace des mots ?** Non. `tr` traduit des caractères, pas des mots. Utilisez `sed` lorsque vous devez remplacer des mots entiers ou des motifs.

**Pourquoi ma commande tr a-t-elle changé les caractères un par un ?** C'est ainsi que fonctionne `tr`. Il associe chaque caractère de `SET1` au caractère correspondant dans `SET2`.

**Pourquoi devrais-je mettre entre guillemets des ensembles comme 'a-z' ?** Mettre entre guillemets empêche le shell d'interpréter les caractères spéciaux avant que `tr` ne les reçoive.

## Exercise

Pour mettre vos connaissances en pratique, essayez le laboratoire pratique suivant. Il vous aidera à renforcer votre compréhension de la traduction de caractères et du traitement de texte.

1. **[Commande Linux tr : Traduction de caractères](https://labex.io/fr/labs/linux-linux-tr-command-character-translating-219198)** - Apprenez la commande Linux `tr` pour les transformations au niveau des caractères dans les flux de texte. Vous pratiquerez la traduction de caractères, la suppression de caractères spécifiques, le travail avec les classes de caractères et la compression des caractères répétés.

Ce laboratoire vous aidera à appliquer les concepts de manipulation de texte dans des scénarios réels et à gagner en confiance avec la commande `tr`.

## Quiz Question

Quelle commande est utilisée pour traduire des caractères ? (Veuillez répondre uniquement en lettres minuscules anglaises)

## Quiz Answer

tr
