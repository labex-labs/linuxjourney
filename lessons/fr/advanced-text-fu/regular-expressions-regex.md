---
lesson_id: "regular-expressions-regex"
course_id: "advanced-text-fu"
lang: "fr"
order_index: 1
title: "regex (Expressions Régulières)"
description: "Découvrez comment les ancres, les ensembles de caractères, les répétitions et les variantes de regex contrôlent la recherche de motifs textuels."
meta_title: "Regex (Expressions Régulières) - Maîtrise Avancée du Texte"
meta_description: "Maîtrisez les bases de Linux avec notre guide sur les expressions régulières (regex). Apprenez l'appariement de motifs avec grep, en utilisant des syntaxes comme ^, $, et []. C'est l'une des meilleures façons d'apprendre la manipulation de texte sous Linux et de faire progresser vos compétences."
meta_keywords: "expression régulière linux, regex, bases linux, appariement de motifs, grep, traitement de texte, apprendre linux, tutoriel linux, chemin rapide vers linux avancé"
---

Les expressions régulières, souvent abrégées en **regex**, décrivent des motifs textuels. Des outils comme `grep`, `sed` et `awk` les utilisent, mais la syntaxe prise en charge peut différer : identifiez donc toujours l'outil et la variante de regex employés.

GNU `grep` utilise par défaut les expressions régulières basiques (BRE), et les expressions régulières étendues (ERE) avec `-E`. Cette leçon présente d'abord les constructions communes aux deux variantes, puis quelques ajouts courants des ERE.

Utilisez ce texte dans les exemples :

```text
sally sells seashells
by the seashore
```

## Rechercher du texte littéral

La plupart des caractères ordinaires correspondent à eux-mêmes. Le motif `seashells` sélectionne une ligne qui contient cette suite exacte, où qu'elle se trouve :

```bash
$ grep 'seashells' sample.txt
sally sells seashells
```

Placez les motifs regex entre guillemets simples afin que le shell ne les développe ni ne les découpe avant que l'outil de recherche ne les reçoive. Une regex diffère aussi du développement des noms de chemins par le shell : dans une regex, `*` répète l'élément précédent ; dans un motif glob du shell, `*` est lui-même un joker représentant une suite de caractères d'un chemin.

:::single-choice{#regex-versus-shell-star} Quel est le rôle de `*` dans une expression régulière telle que `ab*` ?

::option[Il correspond à n'importe quel fichier du répertoire courant.]{#regex-shell-glob explanation="Cela décrit le développement des chemins par le shell dans une commande, et non le sens de `*` dans une regex."}
::option[Il répète le `b` précédent zéro ou plusieurs fois.]{#regex-repeat-b .correct explanation="Un quantificateur regex s'applique à l'élément qui le précède immédiatement : `ab*` correspond donc à `a`, `ab`, `abb`, etc."}
::option[Il répète exactement deux fois la chaîne complète `ab`.]{#regex-repeat-ab-twice explanation="L'astérisque ne porte que sur l'élément précédent et autorise zéro ou plusieurs répétitions, pas exactement deux répétitions de toute la chaîne."}
:::

## Ancrer une correspondance

En dehors d'une expression entre crochets, `^` placé au début d'un motif ancre la correspondance au début de la ligne :

```plaintext
^by
```

L'ancre `$` impose une correspondance à la fin de la ligne :

```plaintext
seashore$
```

Combinez les deux ancres lorsque la ligne entière doit correspondre au motif :

```text
^by the seashore$
```

:::single-choice{#regex-complete-line} Quel motif correspond uniquement à une ligne dont le texte complet est `by the seashore` ?

::option[`^by the seashore$`]{#regex-anchored-line .correct explanation="L'accent circonflexe impose le début de la ligne, tandis que le signe dollar impose que la correspondance se termine avec elle."}
::option[`by the seashore`]{#regex-unanchored-line explanation="Sans ancres, cette suite peut apparaître au milieu d'une ligne plus longue, avec du texte avant ou après."}
::option[`$by the seashore^`]{#regex-reversed-anchors explanation="Dans le motif recherché, l'ancre de fin ne peut pas précéder le texte et l'ancre de début ne peut pas le suivre."}
:::

## Rechercher un caractère

Dans le mode habituel où le traitement se fait ligne par ligne, le point correspond à un caractère :

```plaintext
b.
```

Ce motif correspond à `by`, mais aussi à `ba` ou `b7`. Il ne correspond pas à un `b` isolé, car un caractère est requis après celui-ci. Pour rechercher un point littéral, échappez-le sous la forme `\.` ou placez-le dans une expression entre crochets adaptée.

:::single-choice{#regex-dot-character} Quelle chaîne ne correspond pas au motif de ligne complète `^b.$` ?

::option[`by`]{#regex-dot-by explanation="Le point correspond à `y` ; cette ligne de deux caractères satisfait donc le motif."}
::option[`b`]{#regex-dot-b .correct explanation="Le point exige un caractère après `b`, mais cette chaîne se termine immédiatement."}
::option[`b7`]{#regex-dot-b7 explanation="Le point correspond au chiffre `7` ; cette ligne de deux caractères satisfait donc le motif."}
:::

## Utiliser les expressions entre crochets

Une expression entre crochets correspond à un caractère parmi un ensemble donné :

```plaintext
s[ae]lls
```

À cette position, le motif correspond à `sells` ou à `salls`.

Lorsque `^` est le premier caractère après `[`, il inverse l'ensemble :

```plaintext
s[^e]lls
```

Ce motif correspond à `salls`, mais pas à `sells`, car le caractère qui suit le premier `s` ne peut pas être `e`.

:::single-choice{#regex-negated-bracket} À quoi correspond `[^e]` ?

::option[À exactement un caractère autre que `e`.]{#regex-not-e .correct explanation="Un accent circonflexe placé en tête entre crochets prend le complément de l'ensemble indiqué, mais l'expression consomme toujours un seul caractère."}
::option[Au début d'une ligne suivi de `e`.]{#regex-caret-e-anchor explanation="Au début d'une expression entre crochets, l'accent circonflexe inverse l'ensemble au lieu d'ancrer la ligne."}
::option[À zéro ou plusieurs occurrences de la lettre `e`.]{#regex-repeat-e explanation="Une répétition nécessiterait un quantificateur comme `*` ; cette expression correspond à un caractère qui n'est pas `e`."}
:::

Les plages permettent de décrire les caractères situés entre deux bornes :

```plaintext
d[a-c]g
```

Ce motif peut correspondre à `dag`, `dbg` ou `dcg`. Le comportement des plages peut dépendre de l'ordre de classement de la locale. Les classes de caractères comme `[[:lower:]]`, `[[:upper:]]` et `[[:digit:]]` expriment souvent l'intention plus clairement.

## Répéter et combiner des motifs

En BRE comme en ERE, `*` signifie zéro ou plusieurs répétitions de l'élément précédent :

```text
seashells*
```

Ce motif correspond à `seashell` suivi de zéro ou plusieurs caractères `s` supplémentaires. En mode ERE avec `grep -E`, les opérateurs courants comprennent :

- `+` : une ou plusieurs répétitions ;
- `?` : zéro ou une répétition ;
- `|` : soit l'expression de gauche, soit celle de droite ;
- `(...)` : le regroupement d'expressions.

Par exemple :

```bash
$ grep -E '^(cat|dog)s?$' animals.txt
```

Cette commande sélectionne les lignes complètes égales à `cat`, `cats`, `dog` ou `dogs`. En mode BRE, ces opérateurs suivent d'autres règles d'échappement : ne recopiez donc pas un motif d'une variante à l'autre sans les vérifier.

:::single-choice{#regex-extended-alternation} Quelle commande active la syntaxe regex étendue pour le motif `^(cat|dog)s?$` ?

::option[`grep -F '^(cat|dog)s?$' animals.txt`]{#regex-fixed-animals explanation="`-F` traite tous les opérateurs regex comme du texte littéral ; le regroupement, l'alternative et la répétition facultative sont donc désactivés."}
::option[`grep -E '^(cat|dog)s?$' animals.txt`]{#regex-extended-animals .correct explanation="`-E` sélectionne les expressions régulières étendues et active ici le regroupement, l'alternative et le `s` facultatif."}
::option[`grep '^(cat|dog)s?$' animals.txt`]{#regex-basic-animals explanation="Par défaut, grep utilise les BRE, où ces caractères non échappés de regroupement et d'alternative n'ont pas le sens ERE attendu."}
:::

Pour vous exercer à sélectionner du texte avec les outils Linux, essayez ces laboratoires pratiques :

1. **[Rechercher du texte avec grep sous Linux](https://labex.io/fr/labs/comptia-search-text-with-grep-in-linux-590841)** — Apprenez à rechercher du texte dans des fichiers avec `grep`, à afficher les numéros de ligne, à employer les ancres `^` et `$`, ainsi qu'à exploiter les expressions régulières basiques et étendues.
2. **[Traitement de texte et expressions régulières](https://labex.io/fr/labs/linux-text-processing-and-regular-expressions-18003)** — Découvrez les puissants outils `grep`, `sed` et `awk`, puis utilisez les expressions régulières pour manipuler et rechercher efficacement du texte sous Linux.
3. **[Extraction d'e-mails et de nombres](https://labex.io/fr/labs/linux-extracting-mails-and-numbers-17991)** — Utilisez `grep` et les expressions régulières pour extraire des adresses e-mail et des nombres d'un fichier.

## Résumé

Vous savez maintenant lire et construire des expressions régulières fondamentales appliquées ligne par ligne.

1. Distinguer les opérateurs regex des jokers de chemins du shell.
2. Ancrer une correspondance au début ou à la fin d'une ligne.
3. Rechercher un caractère avec un point ou une expression entre crochets.
4. Inverser un ensemble et utiliser des classes de caractères adaptées à la locale.
5. Choisir délibérément la syntaxe BRE ou ERE.
