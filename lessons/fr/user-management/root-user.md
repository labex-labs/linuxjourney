---
index: 2
lang: "fr"
title: "root"
meta_title: "root - Gestion des Utilisateurs"
meta_description: "Apprenez-en davantage sur l'utilisateur root de Linux, la commande su et le fichier /etc/sudoers. Comprenez l'accès superutilisateur et les permissions sous Linux avec ce guide pour débutants."
meta_keywords: "Linux root, commande su, fichier sudoers, permissions Linux, superutilisateur, tutoriel Linux, guide pour débutants"
---

## Lesson Content

Nous avons examiné une façon d'obtenir un accès superutilisateur en utilisant la commande `sudo`. Vous pouvez également exécuter des commandes en tant que superutilisateur avec la commande `su`. Cette commande va "substituer les utilisateurs" et ouvrir un shell root si aucun nom d'utilisateur n'est spécifié. Vous pouvez utiliser cette commande pour substituer n'importe quel utilisateur tant que vous connaissez le mot de passe.

```bash
su
```

Il y a quelques inconvénients à utiliser cette méthode : il est beaucoup plus facile de faire une erreur critique en exécutant tout en tant que root, vous n'aurez pas d'enregistrements des commandes que vous utilisez pour modifier les configurations du système, etc. En gros, si vous avez besoin d'exécuter des commandes en tant que superutilisateur, contentez-vous de `sudo`.

Maintenant que vous savez quelles commandes exécuter en tant que superutilisateur, la question est de savoir comment vous savez qui a accès pour le faire ? Le système ne permet pas à n'importe qui d'exécuter des commandes en tant que superutilisateur, alors comment sait-il ? Il existe un fichier appelé `/etc/sudoers` ; ce fichier liste les utilisateurs qui peuvent exécuter `sudo`. Vous pouvez modifier ce fichier avec la commande **visudo**.

## Exercise

Ouvrez le fichier `/etc/sudoers` et voyez quelles permissions de superutilisateur les autres utilisateurs de la machine ont.

## Quiz Question

Quel fichier indique les utilisateurs qui ont accès à `sudo` ?

## Quiz Answer

/etc/sudoers
