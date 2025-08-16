---
lang: "fr"
title: "/etc/shadow"
description: "Découvrez le fichier /etc/shadow sous Linux, ses champs et comment il sécurise les mots de passe des utilisateurs. Comprenez l'authentification Linux pour les débutants."
keywords: "/etc/shadow, sécurité Linux, authentification utilisateur, gestion des mots de passe, tutoriel Linux, guide du débutant"
---

## Lesson Content

Le fichier `/etc/shadow` est utilisé pour stocker des informations sur l'authentification des utilisateurs. Il nécessite des permissions de lecture de superutilisateur.

```bash
$ sudo cat /etc/shadow

root:MyEPTEa$6Nonsense:15000:0:99999:7:::
```

Vous remarquerez qu'il ressemble beaucoup au contenu de `/etc/passwd`; cependant, dans le champ du mot de passe, vous verrez un mot de passe chiffré. Les champs sont séparés par des deux-points comme suit :

1. Nom d'utilisateur
2. Mot de passe chiffré
3. Date du dernier changement de mot de passe - exprimée en nombre de jours depuis le 1er janvier 1970. Si la valeur est 0, cela signifie que l'utilisateur doit changer son mot de passe lors de sa prochaine connexion.
4. Âge minimum du mot de passe - Nombre de jours qu'un utilisateur devra attendre avant de pouvoir changer à nouveau son mot de passe.
5. Âge maximum du mot de passe - Nombre maximal de jours avant qu'un utilisateur ne doive changer son mot de passe.
6. Période d'avertissement du mot de passe - Nombre de jours avant l'expiration d'un mot de passe.
7. Période d'inactivité du mot de passe - Nombre de jours après l'expiration d'un mot de passe pour autoriser la connexion avec ce mot de passe.
8. Date d'expiration du compte - Date à laquelle un utilisateur ne pourra plus se connecter.
9. Champ réservé pour une utilisation future.

Dans la plupart des distributions actuelles, l'authentification des utilisateurs ne repose pas uniquement sur le fichier `/etc/shadow`; d'autres mécanismes sont en place, tels que PAM (Pluggable Authentication Modules), qui remplacent l'authentification.

## Exercise

Jetez un œil au fichier `/etc/shadow`.

## Quiz Question

Pas de questions, passez votre chemin !

## Quiz Answer
