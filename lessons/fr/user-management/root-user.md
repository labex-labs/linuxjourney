---
index: 2
lang: "fr"
title: "root"
meta_title: "root - Gestion des utilisateurs"
meta_description: "Apprenez-en davantage sur l'utilisateur root de Linux, la commande su et le fichier /etc/sudoers. Comprenez l'accès et les autorisations du superutilisateur sous Linux avec ce guide pour débutants."
meta_keywords: "Linux root, commande su, fichier sudoers, permissions Linux, superutilisateur, tutoriel Linux, guide du débutant"
---

## Lesson Content

Nous avons examiné une façon d'obtenir un accès superutilisateur en utilisant la commande `sudo`. Vous pouvez également exécuter des commandes en tant que superutilisateur avec la commande `su`. Cette commande va « substituer les utilisateurs » et ouvrir un shell root si aucun nom d'utilisateur n'est spécifié. Vous pouvez utiliser cette commande pour vous substituer à n'importe quel utilisateur tant que vous connaissez le mot de passe.

```bash
su
```

Il y a des inconvénients à utiliser cette méthode : il est beaucoup plus facile de faire une erreur critique en exécutant tout en tant que root, vous n'aurez pas d'enregistrements des commandes que vous utilisez pour modifier les configurations du système, etc. En gros, si vous avez besoin d'exécuter des commandes en tant que superutilisateur, contentez-vous de `sudo`.

Maintenant que vous savez quelles commandes exécuter en tant que superutilisateur, la question est de savoir comment vous savez qui a accès pour le faire ? Le système ne permet pas à n'importe quel quidam d'exécuter des commandes en tant que superutilisateur, alors comment le sait-il ? Il existe un fichier appelé le fichier `/etc/sudoers` ; ce fichier liste les utilisateurs qui peuvent exécuter `sudo`. Vous pouvez modifier ce fichier avec la commande **visudo**.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'accès et des privilèges du superutilisateur :

1. **[Configurer les comptes d'utilisateur et les privilèges Sudo sous Linux](https://labex.io/fr/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Entraînez-vous à appliquer des politiques de mot de passe, à verrouiller et déverrouiller des comptes d'utilisateur, à sécuriser le compte root et à accorder des autorisations administratives, directement liées à la gestion de l'accès superutilisateur.

Ce laboratoire vous aidera à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion des privilèges d'utilisateur et de l'accès superutilisateur.

## Quiz Question

Quel fichier indique les utilisateurs qui ont accès à `sudo` ?

## Quiz Answer

/etc/sudoers
