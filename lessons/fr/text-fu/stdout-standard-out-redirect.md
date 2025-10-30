---
index: 1
lang: "fr"
title: "stdout (Sortie Standard)"
meta_title: "stdout (Sortie Standard) - Text-Fu"
meta_description: "Commencez votre apprentissage de Linux en maîtrisant la sortie standard (stdout) et la redirection d'E/S. Cette leçon explique comment rediriger la sortie des commandes vers des fichiers en utilisant les opérateurs > et >>, une compétence fondamentale pour tout utilisateur Linux."
meta_keywords: "Linux, apprendre Linux, stdout, redirection E/S, sortie standard, rediriger sortie, bash, script shell, commandes Linux, tutoriel Linux"
---

## Lesson Content

Alors que vous continuez à apprendre Linux, vous avez vu comment les commandes produisent des sorties. Cela nous amène au sujet important des flux E/S (entrée/sortie), en particulier la sortie standard ou **stdout**. Explorons ce concept en exécutant la commande suivante :

```bash
echo Bonjour Monde > cacahuetes.txt
```

Après avoir exécuté ceci, vous trouverez un nouveau fichier nommé `cacahuetes.txt` dans votre répertoire actuel. Si vous consultez son contenu, vous verrez le texte "Bonjour Monde". Décortiquons ce qui s'est passé.

### Comprendre la Sortie Standard (stdout)

Premièrement, considérons la commande sans le caractère spécial :

```bash
echo Bonjour Monde
```

Par défaut, de nombreuses commandes envoient leurs résultats à la **stdout**, qui est l'écran de votre terminal. C'est pourquoi `echo Bonjour Monde` affiche le texte directement dans votre shell. Les processus utilisent des flux E/S pour recevoir des entrées (entrée standard ou stdin) et envoyer des sorties. La redirection E/S nous permet de modifier ce comportement par défaut, nous donnant un plus grand contrôle sur nos données.

### Rediriger stdout avec >

Le caractère `>` est un opérateur de redirection. Il intercepte les données se dirigeant vers la **stdout** et les envoie vers une nouvelle destination.

```bash
>
```

Dans notre exemple, il envoie la sortie de `echo Bonjour Monde` vers un fichier au lieu de l'écran. Si le fichier n'existe pas, il sera créé. **Attention**, car si le fichier existe déjà, cet opérateur écrasera complètement son contenu.

### Ajouter stdout avec >>

Et si vous souhaitez ajouter à un fichier sans effacer son contenu ? Pour cela, nous utilisons l'opérateur `>>`.

```bash
echo Bonjour Monde >> cacahuetes.txt
```

Cet opérateur ajoute la sortie à la fin du fichier spécifié. Si le fichier n'existe pas déjà, il sera créé, tout comme l'opérateur `>` . Maîtriser la redirection de la **stdout** est une étape fondamentale dans votre parcours Linux.

## Exercise

Pour consolider votre compréhension de la redirection E/S, essayez ce laboratoire pratique :

1.  **[Redirection de l'entrée et de la sortie sous Linux](https://labex.io/fr/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Entraînez-vous à contrôler le flux de données des commandes en manipulant la sortie standard (stdout), l'erreur standard (stderr) et l'entrée standard (stdin) à l'aide d'opérateurs tels que `>`, `>>`, `2>` et la commande `tee`.

Ce laboratoire vous aidera à appliquer ces concepts dans des scénarios réels et à gagner en confiance avec la redirection E/S.

## Quiz Question

Quel redireceteur utilisez-vous pour ajouter la sortie à un fichier ?

## Quiz Answer

`>>`
