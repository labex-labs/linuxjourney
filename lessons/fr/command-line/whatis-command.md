---
index: 17
lang: "fr"
title: "whatis"
meta_title: "whatis - Ligne de commande"
meta_description: "Apprenez la commande Linux whatis avec des exemples pour obtenir des descriptions de commandes en une ligne à partir des pages man et comprendre plusieurs sections du manuel."
meta_keywords: "commande whatis, linux whatis, description commande linux, résumé page man, aide ligne de commande, apropos"
---

## Lesson Content

En explorant la ligne de commande Linux, vous rencontrerez un grand nombre de commandes. Il est naturel d'oublier ce que fait une commande spécifique. Heureusement, il existe un utilitaire simple pour vous aider.

### Qu'est-ce que la commande whatis

La commande `whatis` affiche une description concise, en une ligne, d'une commande directement extraite de sa page de manuel. C'est un moyen rapide d'obtenir un rappel de la fonction principale d'une commande sans lire toute la page man.

### Comment utiliser la commande whatis

Utiliser `whatis` est simple. Tapez `whatis` suivi de la commande dont vous voulez connaître la description.

```bash
$ whatis cat
cat (1)              - concatenate files and print on the standard output
```

### Comprendre la sortie

La description fournie par `whatis` provient de la section `NAME` de la page de manuel de la commande. Si un nom possède plusieurs pages de manuel dans différentes sections, `whatis` peut afficher plusieurs lignes.

```bash
$ whatis passwd
passwd (1)           - change user password
passwd (5)           - the password file
```

Le nombre entre parenthèses correspond à la section de la page man.

### Whatis vs Man vs Apropos

- `whatis ls` : Affiche une description en une ligne pour un nom de commande exact.
- `man ls` : Ouvre la page de manuel complète.
- `apropos mot-clé` : Recherche dans les descriptions des pages man un mot-clé.

Par exemple :

```bash
$ apropos password
```

Utilisez `whatis` lorsque vous connaissez le nom de la commande mais avez oublié ce qu'elle fait.

### Questions fréquentes

**Pourquoi whatis affiche-t-il "nothing appropriate" ?** La commande peut ne pas avoir de page man installée, ou la base de données man peut nécessiter une mise à jour.

**Est-ce que whatis affiche les options de la commande ?** Non. Utilisez `man COMMAND` ou `COMMAND --help` pour les options.

**whatis est-il identique à which ?** Non. `whatis` décrit une commande. `which` montre le chemin de l'exécutable.

## Exercise

La pratique rend parfait ! Bien qu'il n'y ait pas de laboratoire spécifique pour la commande `whatis`, comprendre comment trouver des informations sur les commandes et les fichiers est crucial. Voici quelques laboratoires pratiques pour renforcer votre compréhension de la localisation des commandes et fichiers sous Linux :

1. **[Commande Linux which : localisation de commande](https://labex.io/fr/labs/linux-linux-which-command-command-locating-215210)** - Entraînez-vous à utiliser la commande `which` pour localiser les fichiers exécutables et comprendre la priorité des commandes dans le PATH de votre système.
2. **[Commande Linux whereis : recherche de fichiers et commandes](https://labex.io/fr/labs/linux-linux-whereis-command-file-and-command-finding-215211)** - Apprenez à utiliser `whereis` pour trouver le binaire, la source et les pages de manuel des commandes, approfondissant votre compréhension de la structure des commandes.
3. **[Découvrez les ressources système critiques](https://labex.io/fr/labs/linux-discover-critical-system-resources-388032)** - Ce défi combine `which`, `whereis` et `find` pour vous aider à naviguer efficacement dans le système de fichiers et découvrir des ressources système importantes.

Ces laboratoires vous aideront à appliquer les concepts de découverte de commandes et fichiers dans des scénarios réels et à gagner en confiance avec les utilitaires Linux essentiels.

## Quiz Question

Quelle commande pouvez-vous utiliser pour voir une petite description d'une commande ? Veuillez répondre en anglais, en faisant attention aux minuscules.

## Quiz Answer

whatis
