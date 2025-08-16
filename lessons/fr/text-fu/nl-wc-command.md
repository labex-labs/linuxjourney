---
title: "wc et nl"
description: "Apprenez les commandes Linux wc et nl. Comprenez le comptage de mots, la numérotation de lignes et l'analyse de fichiers. Améliorez vos compétences en ligne de commande Linux dès aujourd'hui !"
keywords: "commande wc, commande nl, comptage de mots Linux, numéros de ligne Linux, analyse de fichiers, tutoriel Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

La commande `wc` (word count) affiche le nombre total de mots dans un fichier.

```bash
$ wc /etc/passwd
 96     265    5925 /etc/passwd
```

Elle affiche respectivement le nombre de lignes, le nombre de mots et le nombre d'octets.

Pour voir uniquement le compte d'un certain champ, utilisez respectivement les options `-l`, `-w` ou `-c`.

```bash
$ wc -l /etc/passwd
96
```

Une autre commande que vous pouvez utiliser pour vérifier le nombre de lignes dans un fichier est la commande `nl` (number lines).

```plaintext
file1.txt
i
like
turtles
```

```bash
$ nl file1.txt
1. i
2. like
3. turtles
```

## Exercise

Comment obtiendriez-vous le nombre total de lignes en utilisant la commande `nl` sans parcourir toute la sortie ? Indice : Utilisez certaines des autres commandes que vous avez apprises dans ce cours.

## Quiz Question

Quelle commande utiliseriez-vous pour obtenir le nombre total de mots dans un fichier et seulement les mots ?

## Quiz Answer

wc -w
