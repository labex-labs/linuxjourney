---
index: 1
lang: "fr"
title: "stdout (Sortie Standard)"
meta_title: "stdout (Sortie Standard) - Text-Fu"
meta_description: "Découvrez stdout et la redirection d'E/S sous Linux. Comprenez comment rediriger la sortie des commandes vers des fichiers à l'aide des opérateurs > et >>. Commencez votre parcours Linux dès aujourd'hui !"
meta_keywords: "Linux stdout, redirection E/S, commandes Linux, rediriger sortie, tutoriel Linux, Linux débutant, guide Linux, script shell"
---

## Lesson Content

Nous sommes maintenant familiarisés avec de nombreuses commandes et leur sortie, ce qui nous amène à notre prochain sujet : les flux d'E/S (entrée/sortie). Exécutons la commande suivante, et nous discuterons de son fonctionnement.

```bash
echo Hello World > peanuts.txt
```

Que s'est-il passé ? Eh bien, vérifiez le répertoire où vous avez exécuté cette commande, et, ô surprise, vous devriez voir un fichier nommé `peanuts.txt`. Regardez à l'intérieur de ce fichier, et vous devriez voir le texte "Hello World". Beaucoup de choses se sont passées en une seule commande, alors décomposons-la.

Tout d'abord, décomposons la première partie :

```bash
echo Hello World
```

Nous savons que cela affiche "Hello World" à l'écran, mais comment ? Les processus utilisent les flux d'E/S pour recevoir des entrées et renvoyer des sorties. Par défaut, la commande `echo` prend l'entrée (entrée standard ou stdin) du clavier et renvoie la sortie (sortie standard ou stdout) à l'écran. C'est pourquoi, lorsque vous tapez `echo Hello World` dans votre shell, vous obtenez "Hello World" à l'écran. Cependant, la redirection d'E/S nous permet de modifier ce comportement par défaut, nous offrant une plus grande flexibilité de fichier.

Passons à la partie suivante de la commande :

```bash
>
```

Le `>` est un opérateur de redirection qui nous permet de changer la destination de la sortie standard. Il nous permet d'envoyer la sortie de `echo Hello World` vers un fichier au lieu de l'écran. Si le fichier n'existe pas déjà, il le créera pour nous. Cependant, s'il existe, il l'écrasera (vous pouvez ajouter un drapeau de shell pour empêcher cela, selon le shell que vous utilisez).

Et c'est fondamentalement ainsi que fonctionne la redirection de stdout !

Eh bien, disons que je ne voulais pas écraser mon `peanuts.txt`. Heureusement, il existe également un opérateur de redirection pour cela : `>>`.

```bash
echo Hello World >> peanuts.txt
```

Cela ajoutera "Hello World" à la fin du fichier `peanuts.txt`. Si le fichier n'existe pas déjà, il le créera pour nous, tout comme le redirecteur `>` !

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la redirection d'E/S :

1. **[Redirection de l'entrée et de la sortie sous Linux](https://labex.io/fr/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Entraînez-vous à contrôler le flux de données des commandes en manipulant la sortie standard (stdout), l'erreur standard (stderr) et l'entrée standard (stdin) à l'aide d'opérateurs comme `>`, `>>`, `2>`, et la commande `tee`.

Ce laboratoire vous aidera à appliquer les concepts dans des scénarios réels et à renforcer votre confiance avec la redirection d'E/S.

## Quiz Question

Quel redirecteur utilisez-vous pour ajouter une sortie à un fichier ?

## Quiz Answer

>>
