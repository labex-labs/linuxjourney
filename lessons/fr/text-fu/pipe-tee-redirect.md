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

Try the following commands:

```bash
ls | tee peanuts.txt banan.txt
```

## Quiz Question

Quelle touche représente l'opérateur de pipe ?

## Quiz Answer

|
