---
index: 3
lang: "fr"
title: "stderr (Erreur Standard)"
meta_title: "stderr (Erreur Standard) - Text-Fu"
meta_description: "Apprenez la redirection stderr (erreur standard) sous Linux. Comprenez 2>, 2>&1, &> et /dev/null pour la gestion des erreurs dans Bash. Améliorez vos compétences en ligne de commande Linux !"
meta_keywords: "Linux stderr, erreur standard, redirection 2>, 2>&1, redirection &>, /dev/null, gestion des erreurs Bash, tutoriel Linux, Linux pour débutants"
---

## Lesson Content

Essayons quelque chose d'un peu différent maintenant. Essayons de lister le contenu d'un répertoire qui n'existe pas sur votre système et de rediriger à nouveau la sortie vers le fichier `peanuts.txt`.

```bash
ls /fake/directory > peanuts.txt
```

Ce que vous devriez voir est :

```plaintext
ls: cannot access /fake/directory: No such file or directory
```

Maintenant, vous vous dites probablement, ce message n'aurait-il pas dû être envoyé au fichier ? Il y a en fait un autre flux d'E/S en jeu ici appelé erreur standard (stderr). Par défaut, stderr envoie également sa sortie à l'écran ; c'est un flux complètement différent de stdout. Vous devrez donc rediriger sa sortie d'une manière différente.

Malheureusement, le redirecteur n'est pas aussi simple que d'utiliser `<` ou `>` mais il est assez proche. Nous devrons utiliser des descripteurs de fichier. Un descripteur de fichier est un nombre non négatif utilisé pour accéder à un fichier ou à un flux. Nous approfondirons ce sujet plus tard, mais pour l'instant, sachez que le descripteur de fichier pour stdin, stdout et stderr est respectivement 0, 1 et 2.

Donc, si nous voulons rediriger notre stderr vers le fichier, nous pouvons faire ceci :

```bash
ls /fake/directory 2> peanuts.txt
```

Vous ne devriez voir que les messages stderr dans `peanuts.txt`.

Maintenant, que se passe-t-il si je voulais voir à la fois stderr et stdout dans le fichier `peanuts.txt` ? Il est également possible de le faire avec des descripteurs de fichier :

```bash
ls /fake/directory > peanuts.txt 2>&1
```

Ceci envoie les résultats de `ls /fake/directory` au fichier `peanuts.txt`, puis redirige stderr vers stdout via `2>&1`. L'ordre des opérations est important ici ; `2>&1` envoie stderr vers ce que stdout pointe. Dans ce cas, stdout pointe vers un fichier, donc `2>&1` envoie également stderr vers un fichier. Donc, si vous ouvrez ce fichier `peanuts.txt`, vous devriez voir à la fois stderr et stdout. Dans notre cas, la commande ci-dessus n'affiche que stderr.

Il existe un moyen plus court de rediriger à la fois stdout et stderr vers un fichier :

```bash
ls /fake/directory &> peanuts.txt
```

Maintenant, que se passe-t-il si je ne veux aucune de ces informations inutiles et que je veux me débarrasser complètement des messages stderr ? Eh bien, vous pouvez également rediriger la sortie vers un fichier spécial appelé `/dev/null` et il ignorera toute entrée.

```bash
ls /fake/directory 2> /dev/null
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la redirection d'entrée/sortie :

1. **[Redirection d'entrée et de sortie sous Linux](https://labex.io/fr/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Dans ce laboratoire, vous apprendrez à rediriger l'entrée et la sortie dans le shell Linux. Vous vous entraînerez à contrôler le flux de données des commandes en manipulant la sortie standard (stdout), l'erreur standard (stderr) et l'entrée standard (stdin) à l'aide d'opérateurs comme >, >>, 2> et la commande tee.

Ce laboratoire vous aidera à appliquer les concepts de redirection d'E/S dans des scénarios réels et à renforcer votre confiance dans la gestion des flux de données sous Linux.

## Quiz Question

Quel est le redirecteur pour stderr ?

## Quiz Answer

2>
