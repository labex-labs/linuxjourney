---
index: 1
lang: "fr"
title: "stdout (Sortie Standard)"
meta_title: "stdout (Sortie Standard) - Text-Fu"
meta_description: "Découvrez stdout de Linux et la redirection d'E/S. Comprenez comment rediriger la sortie de commande vers des fichiers à l'aide des opérateurs > et >>. Commencez votre parcours Linux dès aujourd'hui !"
meta_keywords: "Linux stdout, redirection E/S, commandes Linux, rediriger la sortie, tutoriel Linux, Linux pour débutants, guide Linux, script shell"
---

## Lesson Content

Nous sommes maintenant familiarisés avec de nombreuses commandes et leur sortie, ce qui nous amène à notre prochain sujet : les flux d'E/S (entrée/sortie). Exécutons la commande suivante, et nous discuterons de son fonctionnement.

```bash
echo Hello World > peanuts.txt
```

Que vient-il de se passer ? Eh bien, vérifiez le répertoire où vous avez exécuté cette commande, et, surprise, vous devriez voir un fichier nommé `peanuts.txt`. Regardez à l'intérieur de ce fichier, et vous devriez voir le texte "Hello World". Beaucoup de choses se sont produites en une seule commande, alors décomposons-la.

Tout d'abord, décomposons la première partie :

```bash
echo Hello World
```

Nous savons que cela affiche "Hello World" à l'écran, mais comment ? Les processus utilisent des flux d'E/S pour recevoir des entrées et renvoyer des sorties. Par défaut, la commande `echo` prend l'entrée (standard input ou stdin) du clavier et renvoie la sortie (standard output ou stdout) à l'écran. C'est pourquoi, lorsque vous tapez `echo Hello World` dans votre shell, vous obtenez "Hello World" à l'écran. Cependant, la redirection d'E/S nous permet de modifier ce comportement par défaut, nous offrant une plus grande flexibilité de fichier.

Passons à la partie suivante de la commande :

```bash
>
```

Le `>` est un opérateur de redirection qui nous permet de changer la destination de la sortie standard. Il nous permet d'envoyer la sortie de `echo Hello World` vers un fichier au lieu de l'écran. Si le fichier n'existe pas déjà, il le créera pour nous. Cependant, s'il existe, il le écrasera (vous pouvez ajouter un shell flag pour empêcher cela, selon le shell que vous utilisez).

Et c'est fondamentalement ainsi que fonctionne la redirection stdout !

Eh bien, disons que je ne voulais pas écraser mon `peanuts.txt`. Heureusement, il existe également un opérateur de redirection pour cela : `>>`.

```bash
echo Hello World >> peanuts.txt
```

Cela ajoutera "Hello World" à la fin du fichier `peanuts.txt`. Si le fichier n'existe pas déjà, il le créera pour nous, tout comme le redirecteur `>` !

## Exercise

Essayez quelques commandes :

```bash
ls -l /var/log > myoutput.txt
echo Hello World > rm
> somefile.txt
```

## Quiz Question

Quel redirecteur utilisez-vous pour ajouter une sortie à un fichier ?

## Quiz Answer

> >
