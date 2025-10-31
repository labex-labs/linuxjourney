---
index: 18
lang: "fr"
title: "alias"
meta_title: "alias - Ligne de commande"
meta_description: "Apprenez à créer et gérer un alias de commande sous Linux pour optimiser votre flux de travail. Ce guide couvre la création d'alias temporaires et permanents via la commande alias et le fichier .bashrc."
meta_keywords: "alias linux, commande alias linux, alias de commande linux, alias commande bash, bash alias, commande unalias, .bashrc, ligne de commande, tutoriel Linux"
---

## Lesson Content

Taper des commandes longues ou répétitives peut être fastidieux. Heureusement, vous pouvez créer un raccourci, ou un **alias Linux**, pour rendre votre expérience de ligne de commande plus efficace. La commande `alias` vous permet de définir un nom personnalisé pour n'importe quelle commande ou séquence de commandes.

### Création d'un alias temporaire

Pour créer un alias temporaire qui dure pour votre session de terminal actuelle, il vous suffit de spécifier un nom et de l'affecter à la chaîne de commande.

Par exemple, pour créer un alias nommé `ll` pour la commande `ls -la`, vous utiliseriez la syntaxe `alias command linux` comme suit :

```bash
alias ll='ls -la'
```

Maintenant, au lieu de taper `ls -la`, vous pouvez simplement taper `ll`, et cela exécutera la même commande. C'est une manière simple mais puissante de personnaliser votre shell.

### Rendre un alias permanent

Un alias temporaire disparaîtra une fois que vous fermerez votre terminal ou redémarrerez votre système. Pour rendre un **command alias in linux** permanent, vous devez l'ajouter au fichier de configuration de votre shell. Pour le shell Bash, ce fichier est généralement `~/.bashrc`.

1. Ouvrez le fichier dans un éditeur de texte : `nano ~/.bashrc`
2. Ajoutez votre définition d'alias au fichier, exactement comme vous l'avez tapée sur la ligne de commande :

```bash
alias ll='ls -la'
alias update='sudo apt update && sudo apt upgrade'
```

3. Enregistrez le fichier et quittez l'éditeur.

Pour que les modifications prennent effet, vous devez soit fermer et rouvrir votre terminal, soit indiquer au shell de recharger le fichier de configuration en utilisant la commande `source` :

```bash
source ~/.bashrc
```

Votre **linux command alias** sera désormais disponible chaque fois que vous ouvrirez une nouvelle session de terminal.

### Suppression d'un alias

Si vous n'avez plus besoin d'un alias, vous pouvez le supprimer avec la commande `unalias`. Cela le supprimera de votre session actuelle.

```bash
unalias ll
```

Pour supprimer un alias permanent, vous devez également supprimer sa définition de votre fichier `~/.bashrc`.

## Exercise

Bien qu'il n'y ait pas de laboratoires spécifiques pour ce sujet, nous vous recommandons d'explorer le [Parcours d'apprentissage Linux](https://labex.io/fr/learn/linux) complet pour pratiquer les compétences et concepts Linux connexes.

## Quiz Question

Quelle commande est utilisée pour créer un alias ? Veuillez répondre en anglais minuscule.

## Quiz Answer

alias
