---
lang: "fr"
title: "join et split"
description: "Apprenez à utiliser les commandes Linux 'join' et 'split' pour la manipulation de fichiers. Comprenez comment combiner des fichiers par des champs communs et diviser efficacement de gros fichiers. Obtenez des exemples pratiques et des conseils."
keywords: "commande Linux join, commande Linux split, manipulation de fichiers, tutoriel Linux, ligne de commande, Linux pour débutants, guide Linux"
---

## Lesson Content

La commande `join` vous permet de joindre plusieurs fichiers ensemble par un champ commun :

Disons que j'avais deux fichiers que je voulais joindre ensemble :

```plaintext
file1.txt
1 John
2 Jane
3 Mary

file2.txt
1 Doe
2 Doe
3 Sue
```

```bash
$ join file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

Voyez-vous comment elle a joint mes fichiers ? Ils sont joints par le premier champ par défaut, et les champs doivent être identiques. S'ils ne le sont pas, vous pouvez les trier. Dans ce cas, les fichiers sont joints via 1, 2, 3.

Comment joindrions-nous les fichiers suivants ?

```plaintext
file1.txt
John 1
Jane 2
Mary 3

file2.txt
1 Doe
2 Doe
3 Sue
```

Pour joindre ce fichier, vous devez spécifier les champs que vous joignez. Dans ce cas, nous voulons le champ 2 sur `file1.txt` et le champ 1 sur `file2.txt`, donc la commande ressemblerait à ceci :

```bash
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

`-1` fait référence à `file1.txt` et `-2` fait référence à `file2.txt`. Plutôt astucieux. Vous pouvez également diviser un fichier en différents fichiers avec la commande `split` :

```bash
split somefile
```

Cela le divisera en différents fichiers. Par défaut, il les divisera une fois qu'ils atteindront une limite de 1000 lignes. Les fichiers sont nommés `x**` par défaut.

## Exercise

Joignez deux fichiers avec un nombre de lignes différent dans chaque fichier. Que se passe-t-il ?

## Quiz Question

Quelle commande utiliseriez-vous pour joindre des fichiers nommés `cat`, `dog`, `cow` ?

## Quiz Answer

join cat dog cow
