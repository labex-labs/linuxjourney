---
index: 5
lang: "fr"
title: "env (Environnement)"
meta_title: "env (Environnement) - Text-Fu"
meta_description: "Découvrez ce que fait la commande env sous Linux. Ce guide explique comment visualiser et utiliser les variables d'environnement Linux telles que PATH, HOME et USER avec la commande env."
meta_keywords: "env, linux env, env linux, commande env linux, commande env sous linux, que fait env sous linux, variables d'environnement, variable PATH, variables shell"
---

## Lesson Content

Votre système Linux utilise des variables d'environnement pour stocker des informations auxquelles le shell et d'autres processus peuvent accéder. Ces variables contiennent des données utiles concernant votre session utilisateur et la configuration du système.

### Exploration des variables d'environnement de base

Vous pouvez afficher la valeur d'une variable spécifique en faisant précéder son nom du symbole `$` . Par exemple, exécutez la commande suivante :

```bash
echo $HOME
```

Cette commande affichera le chemin de votre répertoire personnel, qui pourrait ressembler à `/home/pete`.

Essayez-en une autre :

```bash
echo $USER
```

Ceci affichera votre nom d'utilisateur actuel. Mais d'où viennent ces informations ? Elles sont stockées dans l'environnement de votre shell.

### Que fait env sous Linux

Pour voir toutes les variables d'environnement actuellement définies pour votre session, vous pouvez utiliser la commande `env`. La `commande linux env` est un outil fondamental pour inspecter la configuration de votre shell.

```bash
env
```

L'exécution de la commande `env` affichera une liste de paires clé-valeur. Voici un bref exemple de ce que vous pourriez voir :

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

Comprendre la `linux env` est crucial pour gérer efficacement votre système.

### L'importance de la variable PATH

L'une des variables les plus importantes dans votre sortie `env linux` est `PATH`. Vous pouvez visualiser son contenu spécifiquement avec :

```bash
echo $PATH
```

Cette commande renvoie une liste de répertoires séparés par des deux-points. Lorsque vous tapez une commande, votre système recherche dans ces répertoires pour trouver le fichier exécutable correspondant.

Imaginez que vous installez manuellement un programme dans un répertoire non standard comme `/opt/coolapp/bin`. Si vous essayez de l'exécuter en tapant `coolcommand`, vous pourriez obtenir une erreur "command not found". Cela se produit parce que le répertoire contenant votre programme n'est pas listé dans la variable `PATH`, le shell ne sait donc pas où le chercher.

Pour corriger cela, vous pouvez modifier la variable `PATH` pour inclure le nouveau répertoire. En ajoutant votre répertoire personnalisé à `PATH`, vous permettez au shell de trouver et d'exécuter vos programmes depuis n'importe où dans le terminal.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des variables d'environnement Linux :

1. **[Gérer l'environnement et la configuration du shell sous Linux](https://labex.io/fr/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - Entraînez-vous à créer et gérer des variables locales et d'environnement, à comprendre l'héritage et à rendre les configurations persistantes en modifiant le fichier `.bashrc`.
2. **[Variables d'environnement sous Linux](https://labex.io/fr/labs/linux-environment-variables-in-linux-385274)** - Apprenez le concept et l'utilisation des variables d'environnement, comment les créer, les modifier et les gérer, ainsi que leur rôle dans la configuration du système.
3. **[Configurer les variables d'environnement Linux](https://labex.io/fr/labs/linux-configure-linux-environment-variables-437861)** - Acquérir une expérience pratique en créant, définissant et gérant des variables d'environnement dans un système Linux.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion de votre environnement shell Linux.

## Quiz Question

Quelle commande affiche toutes vos variables d'environnement actuelles ? (Veuillez répondre en anglais, en utilisant uniquement le nom de la commande en minuscules)

## Quiz Answer

env
