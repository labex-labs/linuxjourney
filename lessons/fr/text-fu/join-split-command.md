---
index: 11
lang: "fr"
title: "Joindre et diviser"
meta_title: "Joindre et diviser - Text-Fu"
meta_description: "Maîtrisez l'utilisation des commandes Linux join et split. Apprenez à joindre efficacement des fichiers en fonction de champs communs et à diviser de grands fichiers en parties plus petites. Ce guide couvre la commande à utiliser pour joindre des fichiers nommés chat, chien, vache et d'autres exemples pratiques."
meta_keywords: "joindre fichiers linux, quelle commande utiliser pour joindre des fichiers, commande join linux, commande split linux, manipulation de fichiers, ligne de commande, traitement de texte"
---

## Lesson Content

Sous Linux, la gestion et la manipulation des fichiers texte sont des tâches courantes. Deux utilitaires puissants pour cela sont `join` et `split`. La commande `join` fusionne les lignes de deux fichiers en se basant sur un champ commun, tandis que `split` divise un fichier volumineux en morceaux plus petits et plus faciles à gérer.

### Joindre des fichiers par un champ commun

La commande `join` est un outil fondamental lorsque vous avez besoin de **linux join files** (joindre des fichiers Linux). Par défaut, elle combine les lignes de deux fichiers triés en fonction d'un premier champ identique.

Par exemple, imaginez que vous avez deux fichiers que vous souhaitez fusionner :

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

En utilisant la commande `join`, vous pouvez les combiner facilement :

```bash
$ join file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

Comme vous pouvez le constater, les fichiers ont été joints en utilisant le premier champ commun (1, 2, 3). Pour que `join` fonctionne correctement, les champs de jointure dans les deux fichiers doivent être triés.

### Spécifier différents champs de jointure

Et si le champ commun n'est pas la première colonne ? Vous pouvez indiquer à `join` quels champs utiliser. Considérez ces fichiers :

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

Ici, nous devons joindre sur le deuxième champ de `file1.txt` et le premier champ de `file2.txt`. La commande serait :

```bash
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

L'option `-1 2` spécifie le champ 2 du premier fichier, et `-2 1` spécifie le champ 1 du second fichier.

### Diviser les fichiers volumineux

La commande `split` fait l'inverse de `join` ; elle divise un fichier volumineux en fichiers plus petits.

```bash
$ split somefile
```

Par défaut, cette commande divise `somefile` en nouveaux fichiers dès qu'une limite de 1000 lignes est atteinte. Les fichiers de sortie sont nommés `xaa`, `xab`, et ainsi de suite. Vous pouvez personnaliser ce comportement, par exemple, en spécifiant un nombre de lignes différent avec l'option `-l` ou en divisant par taille de fichier avec l'option `-b`.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la jointure et de la manipulation des fichiers texte :

1. **[Commande Linux join : Jointure de fichiers](https://labex.io/fr/labs/linux-linux-join-command-file-joining-219193)** - Ce laboratoire offre une introduction directe et pratique à la commande `join`, vous permettant de vous entraîner à fusionner des lignes de deux fichiers texte triés en fonction d'un champ commun, comme discuté dans la leçon.
2. **[Traitement des données des employés](https://labex.io/fr/labs/linux-processing-employees-data-388132)** - Appliquez vos connaissances de `join` et d'autres utilitaires puissants de la ligne de commande Linux comme `awk` pour combiner et traiter des données provenant de sources multiples, simulant un scénario d'analyse de données du monde réel.
3. **[Contrôle de séquence et Pipeline](https://labex.io/fr/labs/linux-sequence-control-and-pipeline-17994)** - Améliorez votre efficacité en ligne de commande et vos compétences en manipulation de données en apprenant à contrôler les séquences d'exécution des commandes, à utiliser les pipelines et à exploiter de puissants outils de traitement de texte, ce qui complète les capacités de combinaison de données de `join`.

Ces laboratoires vous aideront à appliquer les concepts de manipulation de fichiers texte et de combinaison de données dans des scénarios réels et à gagner en confiance avec les outils en ligne de commande Linux.

## Quiz Question

Quelle commande utiliseriez-vous pour joindre les fichiers nommés `cat`, `dog`, `cow` ? Veuillez fournir la commande complète en anglais. La commande et les noms de fichiers doivent être en minuscules.

## Quiz Answer

join cat dog cow
