---
index: 11
lang: "fr"
title: "join et split"
meta_title: "join et split - Text-Fu"
meta_description: "Apprenez à utiliser les commandes Linux 'join' et 'split' pour la manipulation de fichiers. Comprenez comment combiner des fichiers par des champs communs et diviser efficacement de gros fichiers. Obtenez des exemples pratiques et des conseils."
meta_keywords: "commande Linux join, commande Linux split, manipulation de fichiers, tutoriel Linux, ligne de commande, Linux pour débutants, guide Linux"
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

Voyez-vous comment cela a joint mes fichiers ? Ils sont joints par le premier champ par défaut, et les champs doivent être identiques. S'ils ne le sont pas, vous pouvez les trier. Dans ce cas, les fichiers sont joints via 1, 2, 3.

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

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la jonction et de la manipulation de fichiers texte :

1. **[Commande Linux join : Jonction de fichiers](https://labex.io/fr/labs/linux-linux-join-command-file-joining-219193)** - Ce laboratoire offre une introduction directe et pratique à la commande `join`, vous permettant de vous entraîner à fusionner des lignes de deux fichiers texte triés basés sur un champ commun, comme discuté dans la leçon.
2. **[Traitement des données des employés](https://labex.io/fr/labs/linux-processing-employees-data-388132)** - Appliquez vos connaissances de `join` et d'autres puissants utilitaires de ligne de commande Linux comme `awk` pour combiner et traiter des données provenant de plusieurs sources, simulant un scénario d'analyse de données réel.
3. **[Contrôle de séquence et pipeline](https://labex.io/fr/labs/linux-sequence-control-and-pipeline-17994)** - Améliorez votre efficacité en ligne de commande et vos compétences en manipulation de données en apprenant à contrôler les séquences d'exécution des commandes, à utiliser les pipelines et à exploiter de puissants outils de traitement de texte, ce qui complète les capacités de combinaison de données de `join`.

Ces laboratoires vous aideront à appliquer les concepts de manipulation de fichiers texte et de combinaison de données dans des scénarios réels et à renforcer votre confiance avec les outils de ligne de commande Linux.

## Quiz Question

Quelle commande utiliseriez-vous pour joindre des fichiers nommés `cat`, `dog`, `cow` ?

## Quiz Answer

join cat dog cow
