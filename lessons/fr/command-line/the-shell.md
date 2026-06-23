---
index: 1
lang: "fr"
title: "Le Shell"
meta_title: "Le Shell - Ligne de Commande"
meta_description: "Découvrez ce qu'est le shell Linux, comment fonctionne l'invite Bash, et comment exécuter votre première commande avec des exemples simples pour débutants."
meta_keywords: "shell linux, bash shell, ligne de commande, terminal linux, invite shell, commande echo, commandes linux de base"
---

## Lesson Content

### Qu'est-ce que le Shell Linux

Bienvenue dans votre parcours Linux ! La première étape est de comprendre le shell Linux. Un shell est un programme qui accepte les commandes que vous tapez, demande au système d'exploitation de les exécuter, puis affiche le résultat dans votre terminal.

Si vous avez utilisé une interface graphique, vous êtes habitué à cliquer sur des fenêtres, des menus et des boutons. En ligne de commande, vous tapez des instructions précises à la place. Des applications nommées "Terminal", "Console" ou "Konsole" ouvrent généralement une session shell pour vous.

Le shell est utile car il est rapide, scriptable, et disponible sur presque tous les systèmes Linux. Au fur et à mesure que vous apprendrez plus de commandes, vous pourrez les combiner pour inspecter des fichiers, gérer des répertoires, rechercher du texte, installer des logiciels, et automatiser des tâches répétitives.

### Interagir avec le Shell Bash

Pour ce cours, nous nous concentrerons sur Bash, abréviation de Bourne Again Shell. Bash est l'un des shells Linux les plus courants et constitue une bonne base même si vous utilisez plus tard `zsh`, `fish` ou un autre shell.

Lorsque vous ouvrez un terminal, vous êtes accueilli par l'invite du shell. Son apparence peut varier, mais elle affiche souvent votre nom d'utilisateur, le nom de l'hôte, et le répertoire courant.

```plaintext
pete@icebox:/home/pete $
```

Le symbole `$` indique que le shell est prêt à accepter votre saisie en tant qu'utilisateur normal. Vous ne tapez pas ce symbole lorsque vous entrez des commandes ; il est affiché par le shell. Si vous voyez `#` à la place, vous travaillez généralement en tant qu'utilisateur root, qui a plus de pouvoirs mais aussi plus de risques.

Les commandes suivent souvent ce schéma :

```bash
command options arguments
```

Par exemple, dans `echo Hello World`, `echo` est la commande et `Hello World` est le texte qui lui est passé.

### Votre Première Commande Linux

Commençons par l'une des commandes Linux les plus basiques pour les débutants : `echo`. Cette commande affiche le texte que vous fournissez dans le terminal.

```bash
$ echo Hello World
Hello World
```

Essayez quelques exemples supplémentaires :

```bash
$ echo Linux is fun
Linux is fun
$ echo "Hello from Bash"
Hello from Bash
```

Les guillemets sont utiles lorsque vous voulez que le shell considère plusieurs mots comme un seul morceau de texte.

### Conseils Courants pour les Débutants

- Appuyez sur `Entrée` pour exécuter une commande.
- Utilisez la touche `Flèche Haut` pour rappeler une commande précédente.
- Les commandes et noms de fichiers sont sensibles à la casse sous Linux.
- Les espaces comptent. `echo hello` et `echohello` sont différents.
- Si une commande semble bloquée, `Ctrl-C` l'annule souvent.

### Questions Courantes

**Le shell est-il la même chose que le terminal ?** Pas exactement. Le terminal est la fenêtre ou l'application dans laquelle vous tapez. Le shell est le programme qui s'exécute à l'intérieur.

**Dois-je taper le `$` montré dans les exemples ?** Non. Le `$` est un marqueur d'invite. Tapez seulement la commande qui suit.

**Pourquoi apprendre Bash si d'autres shells existent ?** Bash est largement disponible, bien documenté, et courant dans les tutoriels et scripts.

## Exercise

Nous recommandons d'explorer le [![Shell Learning Path](https://labex.io/_ipx/f_webp&q_100&s_20x20/https://file.labex.io/path/FaVTnI4iqZP0.png)Shell Learning Path](https://labex.io/fr/learn/shell) complet pour pratiquer les compétences et concepts associés.

## Quiz Question

Quelle est la sortie exacte affichée lorsque vous tapez `echo Hello World` ? Veuillez répondre en anglais, en faisant bien attention à la casse et aux espaces.

## Quiz Answer

Hello World
