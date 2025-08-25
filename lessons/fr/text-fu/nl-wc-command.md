---
index: 15
lang: "fr"
title: "wc et nl"
meta_title: "wc et nl - Text-Fu"
meta_description: "Apprenez les commandes Linux wc et nl. Comprenez le comptage de mots, la numérotation de lignes et l'analyse de fichiers. Améliorez vos compétences en ligne de commande Linux dès aujourd'hui !"
meta_keywords: "commande wc, commande nl, comptage de mots Linux, numéros de ligne Linux, analyse de fichiers, tutoriel Linux, Linux pour débutants, guide Linux"
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

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du comptage de texte et de la numérotation de lignes sous Linux :

1. **[Commande Linux wc : Comptage de texte](https://labex.io/fr/labs/linux-linux-wc-command-text-counting-219200)** - Entraînez-vous à compter les mots, les lignes et les caractères dans les fichiers texte à l'aide de la commande `wc`.
2. **[Commande Linux nl : Numérotation de lignes](https://labex.io/fr/labs/linux-linux-nl-command-line-numbering-210988)** - Apprenez à numéroter les lignes dans les fichiers texte avec la commande `nl`.
3. **[Comptage de mots et tri](https://labex.io/fr/labs/linux-word-count-and-sorting-388125)** - Appliquez vos connaissances de `wc` pour compter les lignes, les mots et les caractères, et combinez-les avec le tri pour des tâches pratiques d'analyse de texte.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans le traitement de texte sous Linux.

## Quiz Question

Quelle commande utiliseriez-vous pour obtenir le nombre total de mots dans un fichier et seulement les mots ?

## Quiz Answer

wc -w
