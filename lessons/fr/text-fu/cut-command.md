---
lang: "fr"
title: "cut"
description: "Apprenez à utiliser la commande Linux `cut` pour extraire du texte de fichiers. Ce tutoriel convivial pour débutants couvre la découpe par caractères et par champs. Améliorez vos compétences en traitement de texte Linux !"
keywords: "commande cut, traitement de texte Linux, extraire du texte, tutoriel Linux, Linux pour débutants, exemples cut, guide Linux"
---

## Lesson Content

Nous allons apprendre quelques commandes utiles que vous pouvez utiliser pour traiter du texte. Avant de commencer, créons un fichier avec lequel nous allons travailler. Copiez et collez la commande suivante ; une fois cela fait, ajoutez une TAB entre "lazy" et "dog" (maintenez Ctrl-v + TAB).

```bash
echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt
```

La première commande que nous allons apprendre est la commande `cut`. Elle extrait des portions de texte d'un fichier.

Pour extraire le contenu par une liste de caractères :

```bash
cut -c 5 sample.txt
```

Ceci affiche le 5ème caractère de chaque ligne du fichier. Dans ce cas, c'est "q" ; notez que l'espace compte également comme un caractère.

Pour extraire le contenu par un champ, nous devrons faire une petite modification :

```bash
cut -f 2 sample.txt
```

Le drapeau `-f` ou champ coupe le texte en fonction des champs. Par défaut, il utilise les TABs comme délimiteurs, donc tout ce qui est séparé par une TAB est considéré comme un champ. Vous devriez voir "dog" comme votre sortie.

Vous pouvez combiner le drapeau de champ avec le drapeau de délimiteur pour extraire le contenu par un délimiteur personnalisé :

```bash
cut -f 1 -d ";" sample.txt
```

Ceci changera le délimiteur TAB en un délimiteur ";", et puisque nous coupons le premier champ, le résultat devrait être "The quick brown".

## Exercise

Que fait la commande suivante ? Pourquoi ?

```bash
cut -c 5-10 sample.txt
cut -c 5- sample.txt
cut -c -5 sample.txt
```

## Quiz Question

Quelle commande utiliseriez-vous pour obtenir le premier caractère de chaque ligne dans un fichier ?

## Quiz Answer

cut -c 1
