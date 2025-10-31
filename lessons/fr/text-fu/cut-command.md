---
index: 6
lang: "fr"
title: "couper"
meta_title: "couper - Text-Fu"
meta_description: "Apprenez à utiliser la commande Linux `cut` pour extraire des sections spécifiques de texte des fichiers. Ce guide couvre la découpe par caractère et par champ (`cut f`), y compris comment couper f avec des délimiteurs personnalisés. Parfait pour maîtriser le traitement de texte sous Linux."
meta_keywords: "commande cut, traitement de texte Linux, extraire texte, cut f, comment couper f, tutoriel Linux, exemples cut, guide Linux, découpe par champ"
---

## Lesson Content

Nous allons apprendre quelques commandes utiles pour le traitement de texte. Avant de commencer, créons un fichier pour travailler. Copiez et collez la commande suivante. Après avoir collé, vous devrez ajouter un caractère TAB littéral entre "lazy" et "dog" (vous pouvez souvent le faire en appuyant sur Ctrl-v puis TAB).

```bash
echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt
```

La première commande que nous allons explorer est `cut`, qui extrait des portions de texte d'un fichier.

### Découpage par Caractère

Vous pouvez extraire du contenu basé sur la position des caractères en utilisant l'indicateur `-c`.

```bash
cut -c 5 sample.txt
```

Cette commande affiche le 5ème caractère de chaque ligne du fichier. Dans notre cas, le résultat est "q". Notez que les espaces comptent également comme des caractères.

### Découpage par Champ avec cut f

Une fonctionnalité plus puissante est le découpage par champs. La syntaxe `cut f`, utilisant l'indicateur `-f`, vous permet d'extraire du texte basé sur la position du champ. Par défaut, `cut` utilise le caractère TAB comme délimiteur, ce qui signifie que tout ce qui est séparé par un TAB est considéré comme un champ distinct.

Voyons comment découper f basé sur les champs :

```bash
cut -f 2 sample.txt
```

Puisque nous avons inséré une TAB entre "lazy" et "dog", cette commande traite "dog" comme le deuxième champ. Votre résultat devrait être "dog".

### Utilisation de Délimiteurs Personnalisés

Vous pouvez également combiner l'indicateur de champ avec l'indicateur de délimiteur (`-d`) pour spécifier un délimiteur personnalisé. Ceci est utile lorsque vous travaillez avec des fichiers qui utilisent des caractères comme des virgules ou des points-virgules pour séparer les données.

```bash
cut -f 1 -d ";" sample.txt
```

Cette commande change le délimiteur de TAB à point-virgule (";"). Puisque nous découpons le premier champ (`-f 1`), le résultat sera "The quick brown".

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du traitement de texte avec `cut` et d'autres commandes associées :

1. **[Commande Linux cut : Découpage de Texte](https://labex.io/fr/labs/linux-linux-cut-command-text-cutting-219187)** - Ce laboratoire offre une introduction directe et pratique à la commande `cut`, vous permettant de vous exercer à extraire des colonnes ou des champs spécifiques à partir de fichiers texte, comme discuté dans la leçon.
2. **[Traitement de Texte Simple](https://labex.io/fr/labs/linux-simple-text-processing-18004)** - Développez vos compétences en manipulation de texte en utilisant des commandes puissantes comme `tr`, `col`, `join` et `paste` pour traiter et analyser efficacement les données textuelles.
3. **[Contrôle de Séquence et Pipeline](https://labex.io/fr/labs/linux-sequence-control-and-pipeline-17994)** - Améliorez votre efficacité en ligne de commande en apprenant à contrôler les séquences d'exécution des commandes, à utiliser les pipelines et à exploiter des outils de traitement de texte puissants comme `cut`, `grep`, `wc`, `sort` et `uniq`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance avec le traitement de texte sous Linux.

## Quiz Question

Quelle commande utiliseriez-vous pour obtenir le premier caractère de chaque ligne d'un fichier ?

## Quiz Answer

cut -c 1
