---
index: 15
lang: "fr"
title: "wc et nl"
meta_title: "wc et nl - Text-Fu"
meta_description: "Maîtrisez les commandes wc et nl dans ce tutoriel Linux. Apprenez à effectuer un décompte de mots Linux, à ajouter des numéros de ligne aux fichiers et à effectuer une analyse de fichiers de base. Un guide parfait pour les débutants souhaitant améliorer leurs compétences en ligne de commande."
meta_keywords: "commande wc, commande nl, décompte mots Linux, compter mots fichier Linux, numéros de ligne Linux, commande nl Linux, analyse fichiers, traitement texte Linux, ligne de commande Linux, tutoriel Linux débutants"
---

## Lesson Content

Sous Linux, l'analyse des fichiers texte est une tâche courante. Deux utilitaires fondamentaux pour cela sont `wc` et `nl`, qui vous aident respectivement à compter le contenu et à numéroter les lignes.

### Compter avec la commande wc

La commande `wc` (word count, compte de mots) est un outil puissant pour l'analyse de fichiers de base. Lorsqu'elle est exécutée sur un fichier, elle fournit un résumé de son contenu.

```bash
$ wc /etc/passwd
 96     265    5925 /etc/passwd
```

Le résultat affiche trois nombres suivis du nom du fichier. De gauche à droite, ces nombres représentent :

1.  Le nombre de lignes.
2.  Le nombre de mots (le compte de mots Linux).
3.  Le nombre d'octets.

### Obtenir des comptes spécifiques

Souvent, vous n'avez besoin que d'une seule information. Vous pouvez utiliser des options pour afficher un compte spécifique au lieu des trois.

- `-l` : Affiche uniquement le nombre de lignes.
- `-w` : Affiche uniquement le nombre de mots.
- `-c` : Affiche uniquement le nombre d'octets.

Par exemple, pour voir uniquement le nombre de lignes dans le fichier `/etc/passwd`, vous utiliseriez :

```bash
$ wc -l /etc/passwd
96
```

### Numéroter les lignes avec la commande nl

Une autre commande utile pour inspecter les fichiers est `nl` (number lines, numéroter les lignes). Comme son nom l'indique, elle lit un fichier et affiche son contenu avec des numéros de ligne ajoutés au début de chaque ligne. Ceci est particulièrement utile pour examiner des scripts ou des fichiers de configuration.

Considérez un fichier nommé `file1.txt` avec le contenu suivant :

```plaintext
i
like
turtles
```

En utilisant la commande `nl`, vous pouvez facilement ajouter des numéros de ligne Linux :

```bash
$ nl file1.txt
     1	i
     2	like
     3	turtles
```

Les commandes `wc` et `nl` sont toutes deux essentielles pour le traitement de texte quotidien sur la ligne de commande Linux.

## Exercise

Pour maîtriser ces commandes, la pratique est essentielle. Essayez ces exercices pour consolider vos compétences en comptage de texte et en numérotation de lignes sous Linux :

1.  **[Commande wc Linux : Comptage de texte](https://labex.io/fr/labs/linux-linux-wc-command-text-counting-219200)** - Entraînez-vous à compter les mots, les lignes et les caractères dans les fichiers texte en utilisant la commande `wc`.
2.  **[Commande nl Linux : Numérotation des lignes](https://labex.io/fr/labs/linux-linux-nl-command-line-numbering-210988)** - Apprenez à numéroter les lignes dans les fichiers texte avec la commande `nl`.
3.  **[Comptage de mots et tri](https://labex.io/fr/labs/linux-word-count-and-sorting-388125)** - Appliquez vos connaissances de `wc` pour compter les lignes, les mots et les caractères, et combinez-les avec le tri pour des tâches d'analyse de texte pratiques.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans le traitement de texte sous Linux.

## Quiz Question

Quelle commande et quelle option utiliseriez-vous pour afficher uniquement le nombre total de mots d'un fichier ? Veuillez répondre en utilisant uniquement la commande et son option en anglais. La réponse est sensible à la casse.

## Quiz Answer

wc -w
