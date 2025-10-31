---
index: 15
lang: "fr"
title: "aide"
meta_title: "aide - Ligne de commande"
meta_description: "Découvrez comment utiliser la commande d'aide Linux pour une assistance rapide dans votre terminal. Ce tutoriel Bash explique comment obtenir de l'aide pour les commandes shell intégrées et utiliser l'indicateur --help pour d'autres programmes Linux."
meta_keywords: "commande aide Linux, aide Bash, aide ligne de commande, commandes Linux, Linux débutant, tutoriel Linux, tutoriel Bash, shell intégré, assistance ligne de commande"
---

## Lesson Content

Lorsque vous travaillez sur la ligne de commande Linux, vous aurez souvent besoin d'un rappel rapide sur le fonctionnement d'une commande ou sur les options qu'elle accepte. Heureusement, Linux fournit d'excellents outils d'aide en ligne de commande directement dans le terminal.

### La commande 'help' pour les commandes intégrées de Bash

L'un des outils les plus directs est `help`, une commande intégrée directement dans le shell Bash. Elle est spécifiquement conçue pour fournir des informations sur les autres commandes intégrées de Bash. Une commande intégrée fait partie du shell lui-même, et non d'un programme séparé. Des exemples incluent `echo`, `cd` et `pwd`.

Pour utiliser la **commande d'aide Linux**, tapez simplement `help` suivi du nom de la commande intégrée.

```bash
help echo
```

Ceci affichera un résumé de la commande `echo`, sa syntaxe et une liste des options disponibles. C'est le moyen le plus rapide d'obtenir de l'aide pour les fonctions spécifiques au shell.

### Le drapeau --help pour les programmes exécutables

Pour la plupart des autres programmes exécutables qui ne sont pas intégrés au shell, la commande `help` ne fonctionnera pas. Au lieu de cela, une convention courante consiste à fournir un drapeau `--help`. Cette option indique au programme d'afficher un résumé d'utilisation, puis de se terminer.

```bash
ls --help
```

Bien que la plupart des développeurs adhèrent à cette norme, elle n'est pas universelle. Cependant, essayer le drapeau `--help` est généralement la meilleure première étape pour trouver de l'aide pour un programme inconnu. C'est une compétence fondamentale pour quiconque apprend les **commandes Linux**.

## Exercise

Bien qu'il n'y ait pas de laboratoires spécifiques pour ce sujet, nous vous recommandons d'explorer le [Parcours d'apprentissage Linux](https://labex.io/fr/learn/linux) complet pour pratiquer les compétences et concepts Linux associés.

## Quiz Question

Comment obtenir une aide rapide en ligne de commande pour les commandes intégrées de Bash ? (Veuillez fournir le nom de la commande unique en anglais et en minuscules.)

## Quiz Answer

help
