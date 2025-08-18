---
lang: "fr"
title: "stdin (Entrée Standard)"
meta_title: "stdin (Entrée Standard) - Text-Fu"
meta_description: "Apprenez la redirection stdin (entrée standard) sous Linux. Comprenez comment utiliser l'opérateur '<' avec les fichiers et les commandes. Explorez des exemples pratiques et améliorez vos compétences en ligne de commande Linux."
meta_keywords: "stdin, entrée standard, redirection Linux, opérateur <, tutoriel Linux, ligne de commande, débutant, guide"
---

## Lesson Content

Dans notre leçon précédente, nous avons appris que nous disposons de différents flux stdout que nous pouvons utiliser, tels qu'un fichier ou l'écran. Eh bien, il existe également différents flux d'entrée standard (stdin) que nous pouvons utiliser. Nous savons que nous avons stdin à partir de périphériques comme le clavier, mais nous pouvons également utiliser des fichiers, la sortie d'autres processus et le terminal. Voyons un exemple.

Utilisons le fichier `peanuts.txt` de la leçon précédente pour cet exemple. Rappelez-vous, il contenait le texte "Hello World".

```bash
cat < peanuts.txt > banana.txt
```

Tout comme nous avions `>` pour la redirection stdout, nous pouvons utiliser `<` pour la redirection stdin.

Normalement, dans la commande `cat`, vous lui envoyez un fichier et ce fichier devient le stdin. Dans ce cas, nous avons redirigé `peanuts.txt` pour qu'il soit notre stdin. Ensuite, la sortie de `cat peanuts.txt`, qui serait "Hello World", est redirigée vers un autre fichier appelé `banana.txt`.

## Exercise

Essayez quelques commandes :

```bash
echo < peanuts.txt > banana.txt
ls < peanuts.txt > banana.txt
pwd < peanuts.txt > banana.txt
```

## Quiz Question

Quel redirecteur utilisez-vous pour rediriger stdin ?

## Quiz Answer

<
