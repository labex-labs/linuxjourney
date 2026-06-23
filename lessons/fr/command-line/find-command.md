---
index: 14
lang: "fr"
title: "find"
meta_title: "find - Ligne de commande"
meta_description: "Apprenez la commande Linux find avec des exemples pour rechercher par nom, type, taille, date de modification et exécuter des actions sur les fichiers correspondants."
meta_keywords: "commande linux find, commande find, trouver fichiers linux, find par nom, find par type, find par taille, find mtime, find exec"
---

## Lesson Content

Avec d'innombrables fichiers sur un système, il peut être difficile de localiser un fichier spécifique. La commande `find` recherche dans les arbres de répertoires en utilisant des critères tels que le nom, le type, la taille et la date de modification.

### Utilisation de la commande find

La syntaxe de base est :

```bash
find [PATH] [EXPRESSION]
```

Vous spécifiez le répertoire dans lequel chercher et les critères de ce que vous recherchez.

Par exemple, pour rechercher un fichier nommé `puppies.jpg` dans le répertoire `/home` et tous ses sous-répertoires, vous utiliseriez :

```bash
$ find /home -name puppies.jpg
```

Les recherches sont récursives par défaut, donc `find /home` regarde à l'intérieur de `/home` et de ses sous-répertoires.

### Recherche par nom et type

Une des utilisations les plus courantes de `find` est la recherche par nom de fichier. L'option `-name` correspond aux noms exactement ou selon des motifs de style shell.

```bash
$ find . -name "*.txt"
```

Vous pouvez aussi spécifier le type d'élément que vous recherchez. L'option `-type` est utilisée à cet effet. Par exemple, si vous voulez trouver un répertoire au lieu d'un fichier, vous pouvez utiliser `d`.

```bash
$ find /home -type d -name MyFolder
```

Dans cette commande, nous définissons le type à `d` pour répertoire et cherchons un élément nommé `MyFolder`. Pour rechercher spécifiquement des fichiers réguliers, vous utiliseriez `-type f`.

### Recherche par taille et date

Vous pouvez rechercher par taille de fichier :

```bash
$ find . -type f -size +10M
$ find . -type f -size -1k
```

La première commande trouve les fichiers plus grands que 10 mégaoctets. La seconde trouve les fichiers plus petits que 1 kilo-octet.

Vous pouvez aussi rechercher par date de modification :

```bash
$ find . -type f -mtime -7
$ find . -type f -mtime +30
```

`-mtime -7` signifie modifié dans les 7 derniers jours. `-mtime +30` signifie modifié il y a plus de 30 jours.

### Exécuter des actions sur les résultats

Par défaut, `find` affiche les chemins correspondants. Vous pouvez ajouter des actions telles que `-print`, `-delete` ou `-exec`.

Afficher explicitement les correspondances :

```bash
$ find . -name "*.log" -print
```

Exécuter `ls -l` sur chaque correspondance :

```bash
$ find . -name "*.log" -exec ls -l {} \;
```

Le placeholder `{}` est remplacé par chaque chemin correspondant. Le point-virgule échappé marque la fin de la commande.

Soyez prudent avec les actions destructrices comme `-delete`. Exécutez d'abord la même recherche sans `-delete` pour confirmer les correspondances.

### Options courantes de find

- `-name PATTERN` : Correspondance par nom de fichier.
- `-iname PATTERN` : Correspondance par nom de fichier, sans tenir compte de la casse.
- `-type f` : Correspond aux fichiers réguliers.
- `-type d` : Correspond aux répertoires.
- `-size +10M` : Correspond aux fichiers plus grands que 10 mégaoctets.
- `-mtime -7` : Correspond aux fichiers modifiés dans les 7 derniers jours.
- `-maxdepth N` : Limite la profondeur de recherche de `find`.

### Questions fréquentes

**Pourquoi find affiche-t-il "Permission denied" ?** Votre utilisateur ne peut pas lire certains répertoires. Cherchez dans un chemin plus restreint ou utilisez les privilèges appropriés.

**Pourquoi devrais-je mettre les motifs comme "*.txt" entre guillemets ?** Les guillemets empêchent le shell d'expanser le caractère générique avant que `find` ne le reçoive.

**find est-il récursif ?** Oui. Il recherche dans les sous-répertoires par défaut.

## Exercise

La pratique est la clé pour maîtriser la commande `find` sous Linux. Ces laboratoires pratiques vous aideront à renforcer votre compréhension de la recherche de fichiers et de répertoires :

1. **[Commande Linux find : Recherche de fichiers](https://labex.io/fr/labs/linux-linux-find-command-file-searching-219191)** - Ce laboratoire offre une introduction à la commande `find`, un outil polyvalent pour rechercher et localiser des fichiers et répertoires selon divers critères. Vous pratiquerez l'utilisation de `find` pour localiser des fichiers spécifiques.
2. **[Découvrir les ressources système critiques](https://labex.io/fr/labs/linux-discover-critical-system-resources-388032)** - Apprenez les commandes Linux essentielles pour localiser fichiers et exécutables, y compris `find`. Vous pratiquerez la navigation efficace dans le système de fichiers et la découverte des ressources système critiques.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance dans l'utilisation efficace de la commande `find`.

## Quiz Question

Quelle option devez-vous spécifier pour la commande `find` afin de rechercher par nom ? Veuillez répondre en utilisant uniquement l'option en anglais, en respectant le format requis (par exemple, -option).

## Quiz Answer

-name
