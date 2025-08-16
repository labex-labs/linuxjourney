---
title: "tr (Traduire)"
description: "Apprenez à utiliser la commande Linux 'tr' pour traduire et supprimer des caractères. Comprenez la traduction de caractères avec des exemples et des exercices. Commencez votre parcours Linux !"
keywords: "commande tr, Linux tr, traduire des caractères, supprimer des caractères, tutoriel Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

La commande `tr` (translate) vous permet de traduire un ensemble de caractères en un autre ensemble de caractères. Essayons un exemple de traduction de tous les caractères minuscules en caractères majuscules.

```bash
$ tr a-z A-Z
hello
HELLO
```

Comme vous pouvez le voir, nous avons transformé les plages de `a-z` en `A-Z`, et tout le texte que nous tapons en minuscules est converti en majuscules.

## Exercise

Essayez la commande suivante. Que se passe-t-il ?

```bash
$ tr -d ello
hello
```

## Quiz Question

Quelle commande est utilisée pour traduire des caractères ?

## Quiz Answer

tr
