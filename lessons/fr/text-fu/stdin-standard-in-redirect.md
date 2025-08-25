---
index: 2
lang: "fr"
title: "stdin (entrée standard)"
meta_title: "stdin (entrée standard) - Text-Fu"
meta_description: "Apprenez la redirection stdin (entrée standard) sous Linux. Comprenez comment utiliser l'opérateur '<' avec des fichiers et des commandes. Explorez des exemples pratiques et améliorez vos compétences en ligne de commande Linux."
meta_keywords: "stdin, entrée standard, redirection Linux, opérateur <, tutoriel Linux, ligne de commande, débutant, guide"
---

## Lesson Content

Lors de notre leçon précédente, nous avons appris que nous disposons de différents flux stdout que nous pouvons utiliser, tels qu'un fichier ou l'écran. Eh bien, il existe également différents flux d'entrée standard (stdin) que nous pouvons utiliser. Nous savons que nous avons stdin à partir de périphériques comme le clavier, mais nous pouvons également utiliser des fichiers, la sortie d'autres processus et le terminal. Voyons un exemple.

Utilisons le fichier `peanuts.txt` de la leçon précédente pour cet exemple. Rappelez-vous, il contenait le texte "Hello World".

```bash
cat < peanuts.txt > banana.txt
```

Tout comme nous avions `>` pour la redirection stdout, nous pouvons utiliser `<` pour la redirection stdin.

Normalement, dans la commande `cat`, vous lui envoyez un fichier et ce fichier devient le stdin. Dans ce cas, nous avons redirigé `peanuts.txt` pour qu'il soit notre stdin. Ensuite, la sortie de `cat peanuts.txt`, qui serait "Hello World", est redirigée vers un autre fichier appelé `banana.txt`.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la redirection d'entrée et de sortie sous Linux :

1. **[Redirection d'entrée et de sortie sous Linux](https://labex.io/fr/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Entraînez-vous à contrôler le flux de données des commandes en manipulant la sortie standard (stdout), l'erreur standard (stderr) et l'entrée standard (stdin) à l'aide d'opérateurs comme >, >>, 2> et la commande tee.
2. **[Redirection de flux de données](https://labex.io/fr/labs/linux-data-stream-redirection-17995)** - Apprenez l'art de la redirection de flux Linux. Manipulez les flux d'entrée, de sortie et d'erreur standard, combinez les sorties et utilisez /dev/null pour des opérations de fichiers avancées.
3. **[Contrôle de séquence et pipeline](https://labex.io/fr/labs/linux-sequence-control-and-pipeline-17994)** - Apprenez à contrôler les séquences d'exécution des commandes et à utiliser les pipelines, qui sont fondamentaux pour diriger la sortie d'une commande comme entrée vers une autre.

Ces laboratoires vous aideront à appliquer les concepts de redirection d'entrée et de sortie dans des scénarios réels et à renforcer votre confiance avec le script shell et la manipulation de données.

## Quiz Question

Quel redirecteur utilisez-vous pour rediriger stdin ?

## Quiz Answer

<
