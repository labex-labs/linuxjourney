---
index: 5
lang: "fr"
title: "env (Environnement)"
meta_title: "env (Environnement) - Text-Fu"
meta_description: "Découvrez les variables d'environnement Linux avec la commande 'env'. Comprenez les variables PATH, HOME et USER. Obtenez un guide pour débutants sur la gestion de votre environnement Linux."
meta_keywords: "commande env, variables d'environnement Linux, variable PATH, tutoriel Linux, Linux pour débutants, variables shell, guide Linux"
---

## Lesson Content

Exécutez la commande suivante :

```bash
echo $HOME
```

Vous devriez voir le chemin de votre répertoire personnel ; le mien ressemble à /home/pete.

Qu'en est-il de cette commande ?

```bash
echo $USER
```

Vous devriez voir votre nom d'utilisateur !

D'où vient cette information ? Elle provient de vos variables d'environnement. Vous pouvez les visualiser en tapant :

```bash
env
```

Ceci affiche une grande quantité d'informations sur les variables d'environnement que vous avez actuellement définies. Ces variables contiennent des informations utiles que le shell et d'autres processus peuvent utiliser.

Voici un court exemple :

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

Une variable particulièrement importante est la variable PATH. Vous pouvez accéder à ces variables en plaçant un `$` devant le nom de la variable, comme ceci :

```bash
$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
```

Ceci renvoie une liste de chemins séparés par un deux-points que votre système recherche lorsqu'il exécute une commande. Supposons que vous téléchargiez et installiez manuellement un paquet depuis Internet et que vous le placiez dans un répertoire non standard, et que vous vouliez exécuter cette commande. Vous tapez `$ coolcommand`, et l'invite dit "command not found". Eh bien, c'est absurde ; vous regardez le binaire dans un dossier et savez qu'il existe. Ce qui se passe, c'est que la variable `$PATH` ne vérifie pas ce répertoire pour ce binaire, donc elle génère une erreur.

Supposons que vous ayez des tonnes de binaires que vous vouliez exécuter à partir de ce répertoire ; vous pouvez simplement modifier la variable PATH pour inclure ce répertoire dans votre variable d'environnement PATH.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des variables d'environnement Linux :

1. **[Gérer l'environnement et la configuration du shell sous Linux](https://labex.io/fr/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - Entraînez-vous à créer et gérer des variables locales et d'environnement, à comprendre l'héritage et à rendre les configurations persistantes en modifiant le fichier `.bashrc`.
2. **[Variables d'environnement sous Linux](https://labex.io/fr/labs/linux-environment-variables-in-linux-385274)** - Apprenez le concept et l'utilisation des variables d'environnement, comment les créer, les modifier et les gérer, ainsi que leur rôle dans la configuration du système.
3. **[Configurer les variables d'environnement Linux](https://labex.io/fr/labs/linux-configure-linux-environment-variables-437861)** - Acquérez une expérience pratique de la création, de la définition et de la gestion des variables d'environnement dans un système Linux.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion de votre environnement de shell Linux.

## Quiz Question

Comment visualisez-vous vos variables d'environnement ?

## Quiz Answer

env
