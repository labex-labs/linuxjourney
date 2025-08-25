---
index: 6
lang: "fr"
title: "cut"
meta_title: "cut - Maîtrise du texte"
meta_description: "Apprenez à utiliser la commande Linux `cut` pour extraire du texte de fichiers. Ce tutoriel convivial pour débutants couvre le découpage de caractères et de champs. Améliorez vos compétences en traitement de texte Linux !"
meta_keywords: "commande cut, traitement de texte Linux, extraire du texte, tutoriel Linux, Linux pour débutants, exemples cut, guide Linux"
---

## Lesson Content

Nous allons apprendre quelques commandes utiles que vous pouvez utiliser pour traiter du texte. Avant de commencer, créons un fichier avec lequel nous allons travailler. Copiez et collez la commande suivante ; une fois que vous l'avez fait, ajoutez une TABULATION entre "lazy" et "dog" (maintenez Ctrl-v + TAB).

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

Le drapeau `-f` ou champ coupe le texte en fonction des champs. Par défaut, il utilise les tabulations comme délimiteurs, donc tout ce qui est séparé par une tabulation est considéré comme un champ. Vous devriez voir "dog" comme votre sortie.

Vous pouvez combiner le drapeau de champ avec le drapeau de délimiteur pour extraire le contenu par un délimiteur personnalisé :

```bash
cut -f 1 -d ";" sample.txt
```

Ceci changera le délimiteur TAB en un délimiteur ";", et puisque nous coupons le premier champ, le résultat devrait être "The quick brown".

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du traitement de texte avec `cut` et d'autres commandes connexes :

1. **[Commande Linux cut : Découpage de texte](https://labex.io/fr/labs/linux-linux-cut-command-text-cutting-219187)** - Ce laboratoire offre une introduction directe et pratique à la commande `cut`, vous permettant de vous entraîner à extraire des colonnes ou des champs spécifiques de fichiers texte, comme discuté dans la leçon.
2. **[Traitement de texte simple](https://labex.io/fr/labs/linux-simple-text-processing-18004)** - Développez vos compétences en manipulation de texte en utilisant des commandes puissantes comme `tr`, `col`, `join` et `paste` pour traiter et analyser efficacement les données textuelles.
3. **[Contrôle de séquence et pipeline](https://labex.io/fr/labs/linux-sequence-control-and-pipeline-17994)** - Améliorez votre efficacité en ligne de commande en apprenant à contrôler les séquences d'exécution des commandes, à utiliser les pipelines et à exploiter des outils puissants de traitement de texte comme `cut`, `grep`, `wc`, `sort` et `uniq`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans le traitement de texte sous Linux.

## Quiz Question

Quelle commande utiliseriez-vous pour obtenir le premier caractère de chaque ligne d'un fichier ?

## Quiz Answer

cut -c 1
