---
index: 3
lang: "fr"
title: "stderr (Erreur Standard)"
meta_title: "stderr (Erreur Standard) - Text-Fu"
meta_description: "Apprenez à gérer l'erreur standard sous Linux. Ce guide couvre la redirection stderr, le descripteur de fichier stderr (2), et comment rediriger stderr vers un fichier ou /dev/null en utilisant 2>, 2>&1, et &>."
meta_keywords: "stderr, erreur standard linux, descripteur de fichier stderr, fichier stderr, erreur standard linux, rediriger stderr, 2>, 2>&1, &>, /dev/null, gestion des erreurs bash"
---

## Lesson Content

Explorons ce qui se passe lorsqu'une commande génère une erreur. Essayez de lister le contenu d'un répertoire qui n'existe pas et redirigez la sortie vers un fichier nommé `peanuts.txt`.

```bash
ls /fake/directory > peanuts.txt
```

Au lieu d'une invite propre, vous verrez un message d'erreur sur votre écran :

```plaintext
ls: cannot access /fake/directory: No such file or directory
```

Vous vous demandez peut-être pourquoi ce message n'a pas été envoyé au fichier. C'est parce qu'un autre flux d'E/S est en jeu : **l'erreur standard**, ou **stderr**.

### Qu'est-ce que l'erreur standard (Standard Error) sous Linux ?

Sous Linux, `stderr` est un flux de sortie par défaut utilisé par les programmes pour envoyer des messages d'erreur et des diagnostics. Il est complètement séparé du flux de sortie standard (`stdout`), qui est utilisé pour la sortie normale du programme. Par défaut, `stdout` et `stderr` envoient leur sortie à l'écran de votre terminal, c'est pourquoi vous voyez le message d'erreur directement.

Pour contrôler `stderr`, vous avez besoin d'une méthode de redirection différente.

### Comprendre les descripteurs de fichiers

Pour gérer les flux d'E/S comme `stdin`, `stdout` et `stderr`, le système utilise des descripteurs de fichiers. Un **descripteur de fichier** est un nombre entier non négatif que le noyau utilise pour identifier un fichier ou un flux ouvert. Les descripteurs de fichiers par défaut sont :

- `0` : stdin (entrée standard)
- `1` : stdout (sortie standard)
- `2` : stderr (erreur standard)

Le nombre `2` est le **descripteur de fichier stderr** dédié, et nous pouvons l'utiliser pour contrôler où vont les messages d'erreur.

### Rediriger stderr vers un fichier

Pour rediriger `stderr` vers un fichier, vous utilisez le descripteur de fichier `2` suivi de l'opérateur `>`. Cette commande enverra tous les messages d'erreur dans le **fichier stderr** spécifié.

```bash
ls /fake/directory 2> peanuts.txt
```

Maintenant, votre terminal sera silencieux et le message d'erreur se trouvera dans `peanuts.txt`.

### Combiner stdout et stderr

Et si vous souhaitez capturer à la fois la sortie normale et les messages d'erreur dans le même fichier ? Vous pouvez y parvenir en redirigeant les deux flux.

```bash
ls /fake/directory /etc/passwd > peanuts.txt 2>&1
```

Décortiquons cela :

1.  `> peanuts.txt` redirige `stdout` (descripteur de fichier 1) vers le fichier `peanuts.txt`.
2.  `2>&1` redirige `stderr` (descripteur de fichier 2) vers le même emplacement que celui vers lequel `stdout` (descripteur de fichier 1) pointe actuellement.

L'ordre est important. `2>&1` envoie `stderr` vers la destination actuelle de `stdout`. Dans ce cas, `stdout` pointe vers un fichier, donc `stderr` est également envoyé vers ce fichier.

Une manière plus moderne et plus courte de rediriger à la fois `stdout` et `stderr` est d'utiliser `&>`.

```bash
ls /fake/directory /etc/passwd &> peanuts.txt
```

### Jeter les messages d'erreur

Parfois, vous voudrez peut-être exécuter une commande et ignorer complètement tout message d'erreur potentiel. Pour ce faire, vous pouvez rediriger `stderr` vers un fichier spécial appelé `/dev/null`, qui supprime toutes les données qui y sont écrites.

```bash
ls /fake/directory 2> /dev/null
```

Cette commande s'exécutera, et toute sortie d'erreur provenant de `stderr` sera envoyée à `/dev/null` et supprimée, laissant votre écran propre.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la redirection d'entrée/sortie :

1. **[Redirection de l'entrée et de la sortie sous Linux](https://labex.io/fr/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Dans ce laboratoire, vous apprendrez à rediriger l'entrée et la sortie dans le shell Linux. Vous vous entraînerez à contrôler le flux de données des commandes en manipulant la sortie standard (stdout), l'erreur standard (stderr) et l'entrée standard (stdin) à l'aide d'opérateurs tels que >, >>, 2> et la commande tee.

Ce laboratoire vous aidera à appliquer les concepts de redirection d'E/S dans des scénarios réels et à renforcer votre confiance dans la gestion des flux de données sous Linux.

## Quiz Question

Quel est l'opérateur utilisé pour rediriger le flux `stderr` ? Veuillez fournir l'opérateur exact dans votre réponse.

## Quiz Answer

2>
