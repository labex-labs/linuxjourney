---
index: 13
lang: "fr"
title: "tr (Traduire)"
meta_title: "tr (Traduire) - Text-Fu"
meta_description: "Maîtrisez la commande Linux tr pour la traduction et la suppression de caractères. Ce guide explique comment trtraduire des caractères, utiliser des options comme linux tr -d pour supprimer des caractères, et fournit des exemples pratiques de manipulation de texte."
meta_keywords: "tr, commande tr, trtraduire, linux tr -d, tr -d linux, traduire caractères, supprimer caractères, traitement de texte, commande Linux"
---

## Lesson Content

La commande `tr`, abréviation de translate (traduire), est un utilitaire en ligne de commande sous Linux qui traduit ou supprime des caractères de l'entrée standard. C'est un outil utile pour la manipulation de texte simple et est souvent utilisé avec des pipes pour traiter la sortie d'autres commandes. La fonctionnalité `trtranslate` est un élément central du traitement de texte.

### Traduction de Caractères de Base

L'utilisation la plus courante de `tr` est de substituer un ensemble de caractères par un autre. Par exemple, vous pouvez facilement traduire tous les caractères minuscules en majuscules.

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

Dans cet exemple, nous avons redirigé la sortie de `echo` vers la commande `tr`. La commande `tr` a ensuite traduit la plage de caractères `a-z` par les caractères correspondants dans la plage `A-Z`.

### Suppression de Caractères avec -d

Une autre fonctionnalité puissante est la capacité de supprimer des caractères spécifiques à l'aide de l'option `-d` (delete/supprimer). Ceci est particulièrement utile pour nettoyer du texte. Par exemple, si vous souhaitez supprimer tous les chiffres d'une chaîne, vous pouvez utiliser `linux tr -d`.

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

Ici, la commande `tr -d` a supprimé chaque caractère de l'ensemble spécifié ('0' à '9') du flux d'entrée. C'est un modèle courant pour les utilisateurs de `tr -d linux`.

### Compression des Caractères Répétés

La commande `tr` peut également "comprimer" les caractères répétés en une seule instance en utilisant l'option `-s` (squeeze/compresser). C'est excellent pour normaliser le texte contenant des espaces superflus.

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

Dans ce cas, `tr -s ' '` a remplacé les séquences de plusieurs espaces par un seul espace, rendant la sortie beaucoup plus propre.

## Exercise

Pour mettre vos connaissances en pratique, essayez le laboratoire pratique suivant. Il vous aidera à renforcer votre compréhension de la traduction de caractères et du traitement de texte.

1.  **[Commande Linux tr : Traduction de Caractères](https://labex.io/fr/labs/linux-linux-tr-command-character-translating-219198)** - Apprenez la commande Linux `tr` pour les transformations au niveau des caractères dans les flux de texte. Vous pratiquerez la traduction de caractères, la suppression de caractères spécifiques, le travail avec des classes de caractères et la compression des caractères répétés.

Ce laboratoire vous aidera à appliquer les concepts de manipulation de texte dans des scénarios réels et à renforcer votre confiance avec la commande `tr`.

## Quiz Question

Quelle commande est utilisée pour traduire des caractères ? (Veuillez répondre uniquement en lettres anglaises minuscules)

## Quiz Answer

tr
