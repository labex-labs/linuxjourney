---
index: 18
lang: "fr"
title: "alias"
meta_title: "alias - Ligne de commande"
meta_description: "Apprenez la commande Linux alias avec des exemples pour créer des alias temporaires, enregistrer des alias dans .bashrc, lister les alias et les supprimer avec unalias."
meta_keywords: "commande linux alias, commande alias, alias bash, alias .bashrc, commande unalias, raccourci commande linux, alias shell"
---

## Lesson Content

Taper des commandes longues ou répétitives peut être fastidieux. Un alias est un raccourci shell qui vous permet de définir un nom personnalisé pour une commande ou une séquence de commandes.

### Création d'un alias temporaire

Pour créer un alias temporaire qui dure pour votre session terminal actuelle, il vous suffit de spécifier un nom et de l'assigner à la chaîne de commande.

Par exemple, créez un alias nommé `ll` pour `ls -la` :

```bash
$ alias ll='ls -la'
```

Maintenant, au lieu de taper `ls -la`, vous pouvez simplement taper `ll`, et cela exécutera la même commande. C'est une manière simple mais puissante de personnaliser votre shell.

### Rendre un alias permanent

Un alias temporaire disparaîtra une fois que vous fermerez votre terminal ou redémarrerez votre système. Pour rendre un `alias de commande sous linux` permanent, vous devez l'ajouter au fichier de configuration de votre shell. Pour le shell Bash, ce fichier est généralement `~/.bashrc`.

1. Ouvrez le fichier dans un éditeur de texte : `nano ~/.bashrc`
2. Ajoutez votre définition d'alias dans le fichier, exactement comme vous l'avez tapée dans la ligne de commande :

```bash
alias ll='ls -la'
alias update='sudo apt update && sudo apt upgrade'
```

3. Enregistrez le fichier et quittez l'éditeur.

Pour que les modifications prennent effet, vous devez soit fermer et rouvrir votre terminal, soit demander au shell de recharger le fichier de configuration avec la commande `source` :

```bash
$ source ~/.bashrc
```

Votre alias sera désormais disponible à chaque fois que vous démarrez une nouvelle session Bash.

### Suppression d'un alias

Si vous n'avez plus besoin d'un alias, vous pouvez le supprimer avec la commande `unalias`. Cela le supprimera de votre session en cours.

```bash
$ unalias ll
```

Pour supprimer un alias permanent, vous devez également supprimer sa définition dans votre fichier `~/.bashrc`.

### Lister les alias existants

Exécutez `alias` sans arguments pour lister les alias dans votre shell actuel.

```bash
$ alias
alias ll='ls -la'
alias grep='grep --color=auto'
```

Utilisez `type` pour voir ce qui sera exécuté lorsque vous entrez une commande :

```bash
$ type ll
ll is aliased to 'ls -la'
```

### Exemples d'alias utiles

```bash
$ alias la='ls -la'
$ alias ..='cd ..'
$ alias grep='grep --color=auto'
```

Gardez les alias courts et prévisibles. Évitez de remplacer des commandes destructrices par des comportements surprenants sauf si vous en êtes très sûr.

### Questions fréquentes

**Les alias fonctionnent-ils dans les scripts ?** En général non, pas par défaut. Les scripts doivent utiliser des commandes complètes ou des fonctions.

**Où doivent aller les alias Bash ?** Mettez-les dans `~/.bashrc` pour les sessions Bash interactives.

**Que faire si un alias entre en conflit avec une commande réelle ?** L'alias prend généralement la priorité dans l'utilisation du shell interactif. Utilisez `command nom` ou `\nom` pour contourner un alias.

## Exercise

Bien qu'il n'y ait pas de laboratoires spécifiques pour ce sujet, nous recommandons d'explorer le parcours complet [Linux Learning Path](https://labex.io/fr/learn/linux) pour pratiquer les compétences et concepts Linux associés.

## Quiz Question

Quelle commande est utilisée pour créer un alias ? Veuillez répondre en anglais en minuscules.

## Quiz Answer

alias
