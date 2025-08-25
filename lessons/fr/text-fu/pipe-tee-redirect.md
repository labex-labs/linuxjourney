---
index: 4
lang: "fr"
title: "pipe et tee"
meta_title: "pipe et tee - Text-Fu"
meta_description: "Apprenez les pipes Linux et la commande tee pour un flux de données efficace en ligne de commande. Comprenez stdout, stdin et la sortie de fichier. Améliorez vos compétences Linux !"
meta_keywords: "pipe Linux, commande tee, tutoriel Linux, stdout, stdin, Linux pour débutants, ligne de commande, guide Linux"
---

## Lesson Content

Passons à la plomberie maintenant, pas vraiment, mais un peu. Essayons une commande :

```bash
ls -la /etc
```

Vous devriez voir une très longue liste d'éléments ; c'est un peu difficile à lire, en fait. Au lieu de rediriger cette sortie vers un fichier, ne serait-il pas agréable de pouvoir simplement voir la sortie dans une autre commande comme `less` ? Eh bien, nous le pouvons !

```bash
ls -la /etc | less
```

L'opérateur de pipe `|`, représenté par une barre verticale, nous permet d'obtenir le `stdout` d'une commande et d'en faire le `stdin` d'un autre processus. Dans ce cas, nous avons pris le `stdout` de `ls -la /etc` et l'avons ensuite _pipé_ vers la commande `less`. La commande pipe est extrêmement utile, et nous continuerons à l'utiliser pour toute l'éternité.

Eh bien, et si je voulais écrire la sortie de ma commande vers deux flux différents ? C'est possible avec la commande `tee` :

```bash
ls | tee peanuts.txt
```

Vous devriez voir la sortie de `ls` sur votre écran, et si vous ouvrez le fichier `peanuts.txt`, vous devriez voir les mêmes informations !

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la redirection d'entrée/sortie et des pipelines :

1. **[Redirection d'entrée et de sortie sous Linux](https://labex.io/fr/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Entraînez-vous à contrôler le flux de données des commandes en manipulant la sortie standard (stdout), l'erreur standard (stderr) et l'entrée standard (stdin) à l'aide d'opérateurs comme `>`, `>>`, `2>`, et la commande `tee`.
2. **[Contrôle de séquence et pipeline](https://labex.io/fr/labs/linux-sequence-control-and-pipeline-17994)** - Apprenez à contrôler les séquences d'exécution des commandes, à utiliser les pipelines et à exploiter de puissants outils de traitement de texte comme `cut`, `grep`, `wc`, `sort` et `uniq`.
3. **[Redirection de flux de données](https://labex.io/fr/labs/linux-data-stream-redirection-17995)** - Apprenez l'art de la redirection de flux Linux, y compris la manipulation des flux d'entrée, de sortie et d'erreur standard, la combinaison des sorties et l'utilisation de `/dev/null`.

Ces laboratoires vous aideront à appliquer les concepts de piping et de redirection dans des scénarios réels et à renforcer votre confiance dans la manipulation des données en ligne de commande.

## Quiz Question

Quelle touche représente l'opérateur pipe ?

## Quiz Answer

|
