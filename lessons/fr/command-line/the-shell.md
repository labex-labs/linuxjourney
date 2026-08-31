---
lesson_id: "the-shell"
course_id: "command-line"
lang: "fr"
order_index: 1
title: "Le Shell"
description: "Découvrez ce qu'est le shell Linux et comment les commandes sont exécutées."
meta_title: "Le Shell - Ligne de Commande"
meta_description: "Découvrez ce qu'est le shell Linux, comment fonctionne l'invite Bash, et comment exécuter votre première commande avec des exemples simples pour débutants."
meta_keywords: "shell linux, bash shell, ligne de commande, terminal linux, invite shell, commande echo, commandes linux de base"
---

## Qu'est-ce que le shell Linux ?

Bienvenue dans votre parcours Linux ! La première étape consiste à comprendre le shell. Un shell est un programme qui accepte les commandes saisies, demande au système d'exploitation de les exécuter, puis affiche le résultat dans le terminal.

Si vous avez déjà utilisé une interface graphique, vous avez l'habitude de cliquer sur des fenêtres, des menus et des boutons. En ligne de commande, vous saisissez plutôt des instructions précises. Les applications nommées « Terminal », « Console » ou « Konsole » ouvrent généralement une session shell.

Le terminal est la fenêtre ou l'application dans laquelle vous tapez, tandis que le shell est le programme qui s'exécute à l'intérieur.

Le shell est utile parce qu'il est rapide, scriptable et disponible sur presque tous les systèmes Linux. À mesure que vous apprendrez des commandes, vous pourrez les combiner pour inspecter des fichiers, gérer des répertoires, rechercher du texte, installer des logiciels et automatiser des tâches répétitives.

:::single-choice{#distinguish-shell-and-terminal}
Quelle affirmation décrit correctement la relation entre un terminal et un shell ?

::option[Le terminal fournit la fenêtre, tandis que le shell s'exécute à l'intérieur.]{#shell-runs-in-terminal .correct explanation="Le terminal est l'interface utilisée, et le shell est le programme de traitement des commandes qui s'y exécute."}
::option[Le terminal accepte les commandes, tandis que le shell ne fait qu'afficher leur sortie.]{#terminal-accepts-commands explanation="Cette proposition inverse leurs rôles. Le terminal fournit l'interface, tandis que le shell accepte et exécute les commandes."}
::option[Terminal et shell sont deux noms du même programme.]{#terminal-equals-shell explanation="Ils fonctionnent ensemble, mais ne sont pas le même programme. Un terminal ouvre une session dans laquelle s'exécute un shell."}
:::

## Interagir avec le shell Bash

Dans ce cours, nous nous concentrerons sur Bash, abréviation de Bourne Again Shell. Bash est l'un des shells Linux les plus courants et constitue une bonne base, même si vous utilisez ensuite `zsh`, `fish` ou un autre shell.

À l'ouverture d'un terminal, l'invite du shell vous accueille. Son apparence varie, mais elle indique souvent le nom d'utilisateur, le nom d'hôte et le répertoire actuel.

```plaintext
pete@icebox:/home/pete $
```

Le symbole `$` indique que le shell attend la saisie d'un utilisateur ordinaire. Vous ne tapez pas ce symbole lorsque vous entrez une commande : le shell l'affiche. Si vous voyez plutôt `#`, vous travaillez généralement comme utilisateur root, avec davantage de pouvoir et de risques.

:::single-choice{#interpret-dollar-prompt}
Que signifie le `$` à la fin de l'exemple d'invite ?

::option[Le shell s'exécute avec les privilèges de l'utilisateur root.]{#root-user-ready explanation="Une invite root se termine généralement par `#`, et non par `$`. L'accès root apporte davantage de pouvoir et de risques."}
::option[Le shell attend la saisie d'un utilisateur ordinaire.]{#normal-user-ready .correct explanation="Le `$` marque l'invite d'un utilisateur ordinaire et indique que le shell attend une commande."}
::option[La prochaine commande doit commencer par un signe dollar.]{#type-dollar-first explanation="Le `$` appartient à l'invite. Saisissez la commande qui le suit sans recopier ce symbole."}
:::

Les commandes suivent souvent ce modèle :

```bash
command options arguments
```

Par exemple, dans `echo Hello World`, `echo` est la commande et `Hello World` est le texte qui lui est transmis.

:::single-choice{#identify-command-name}
Dans `echo Hello World`, quelle partie est le nom de la commande ?

::option[`Hello`]{#hello-command explanation="`Hello` vient après le nom de la commande ; il fait donc partie du texte transmis à `echo`."}
::option[`World`]{#world-command explanation="`World` est lui aussi du texte transmis à `echo`, et non le nom de la commande exécutée."}
::option[`echo`]{#echo-command .correct explanation="`echo` nomme le programme que le shell doit exécuter. Les mots qui suivent lui sont transmis comme arguments."}
:::

## Votre première commande Linux

Commençons par l'une des commandes Linux les plus simples pour les débutants : `echo`. Elle réaffiche dans le terminal le texte que vous lui fournissez.

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

Les guillemets sont utiles lorsque vous voulez que le shell traite plusieurs mots comme un seul fragment de texte.

:::single-choice{#group-words-with-quotes}
Quelle commande demande au shell de traiter `Hello from Bash` comme un seul fragment de texte entre guillemets ?

::option[`echo "Hello from Bash"`]{#quoted-words .correct explanation="Les guillemets regroupent les trois mots en un seul argument transmis à `echo`."}
::option[`echo Hello from Bash`]{#unquoted-words explanation="Cette commande affiche visuellement les mêmes mots, mais le shell les traite comme des arguments distincts puisqu'ils ne sont pas entre guillemets."}
::option[`"echo Hello from Bash"`]{#quoted-command explanation="En plaçant toute la ligne entre guillemets, le shell recherche une commande portant ce nom complet au lieu d'exécuter `echo` avec du texte."}
:::

Pour pratiquer ces compétences, explorez le [![Parcours d'apprentissage du shell](https://labex.io/cdn-cgi/image/width=200,height=200,quality=80,format=auto,onerror=redirect/https://file.labex.io/path/FaVTnI4iqZP0.png)parcours d'apprentissage du shell](https://labex.io/fr/learn/shell).

## Conseils courants pour les débutants

- Appuyez sur `Entrée` pour exécuter une commande.
- Utilisez la touche `Flèche haut` pour rappeler une commande précédente.
- Sous Linux, les commandes et noms de fichiers sont sensibles à la casse.
- Les espaces comptent : `echo hello` et `echohello` sont différents.
- Si une commande semble bloquée, `Ctrl-C` permet souvent de l'annuler.

## Résumé

Vous savez maintenant expliquer le rôle d'un shell et interagir avec une invite élémentaire.

1. Distinguer un terminal d'un shell.
2. Identifier une invite de commande.
3. Exécuter une commande simple avec `echo`.
