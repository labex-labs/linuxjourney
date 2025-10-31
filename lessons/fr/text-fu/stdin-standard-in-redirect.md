---
index: 2
lang: "fr"
title: "stdin (Entrée Standard)"
meta_title: "stdin (Entrée Standard) - Text-Fu"
meta_description: "Maîtrisez les opérations de la ligne de commande Linux en apprenant à rediriger stdin (entrée standard). Ce guide couvre la relation entre stdin et stdout, l'utilisation de l'opérateur '<', et des exemples pratiques comme 'cat stdin' pour gérer efficacement les flux de données."
meta_keywords: "stdin, entree standard, rediriger stdin, cat stdin, stdin et stdout, entrée standard, redirection Linux, ligne de commande, flux d'entrée"
---

## Lesson Content

Lors de notre leçon précédente, nous avons appris à rediriger le flux de sortie standard (stdout). De même, nous pouvons également gérer le flux d'entrée standard (`stdin`). Par défaut, un programme reçoit son `stdin` du clavier, mais nous pouvons également utiliser des fichiers ou la sortie d'autres processus comme source d'entrée.

### Comprendre stdin et stdout

Chaque processus en ligne de commande sous Linux fonctionne avec au moins deux flux de données fondamentaux : l'entrée standard (`stdin`) et la sortie standard (`stdout`). Un programme lit les données depuis `stdin` et écrit ses résultats sur `stdout`. Comprendre comment contrôler à la fois `stdin et stdout` est crucial pour un travail efficace en ligne de commande.

### Comment rediriger stdin

Tout comme nous utilisons `>` pour la redirection de stdout, nous utilisons l'opérateur `<` pour `rediriger stdin`. Cette fonctionnalité puissante vous permet d'indiquer à une commande de lire son entrée à partir d'un fichier au lieu d'attendre que vous la tapiez au clavier. C'est un concept fondamental de la redirection d'entrée.

### Exemple pratique avec cat stdin

Revenons au fichier `peanuts.txt` de la leçon précédente, qui contient le texte "Hello World". Considérez la commande suivante :

```bash
cat < peanuts.txt > banana.txt
```

Voici une explication de ce qui se passe :

1. La partie `< peanuts.txt` indique au shell de `rediriger stdin` pour la commande `cat`, lui faisant lire depuis `peanuts.txt` au lieu du clavier.
2. La commande `cat` traite son entrée. Dans ce cas, utiliser `cat stdin` signifie qu'elle lit le contenu de `peanuts.txt`.
3. La partie `> banana.txt` redirige la sortie standard de `cat` vers un nouveau fichier nommé `banana.txt`.

En fin de compte, le contenu de `peanuts.txt` est copié dans `banana.txt`. Cet exemple démontre efficacement comment gérer à la fois `stdin et stdout` dans une seule commande efficace.

## Exercise

Pour consolider votre compréhension, essayez ces exercices pratiques axés sur la redirection d'entrée et de sortie sous Linux :

1. **[Redirection d'entrée et de sortie sous Linux](https://labex.io/fr/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Entraînez-vous à contrôler le flux de données des commandes en manipulant la sortie standard (stdout), l'erreur standard (stderr) et l'entrée standard (stdin) à l'aide d'opérateurs tels que >, >>, 2> et de la commande tee.
2. **[Redirection de flux de données](https://labex.io/fr/labs/linux-data-stream-redirection-17995)** - Apprenez l'art de la redirection de flux sous Linux. Manipulez les flux d'entrée, de sortie et d'erreur standard, combinez les sorties et utilisez /dev/null pour des opérations de fichiers avancées.
3. **[Contrôle de séquence et pipeline sous Linux](https://labex.io/fr/labs/linux-sequence-control-and-pipeline-17994)** - Apprenez à contrôler les séquences d'exécution des commandes et à utiliser les pipelines, fondamentaux pour diriger la sortie d'une commande comme entrée d'une autre.

Ces laboratoires vous aideront à appliquer les concepts de redirection d'entrée et de sortie dans des scénarios réels et à renforcer votre confiance dans le scripting shell et la manipulation de données.

## Quiz Question

Quel opérateur est utilisé pour rediriger stdin ? Veuillez répondre uniquement avec le symbole requis.

## Quiz Answer

<
