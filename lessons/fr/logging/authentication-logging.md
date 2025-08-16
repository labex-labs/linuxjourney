---
lang: "fr"
title: "Journalisation de l'authentification"
description: "Découvrez la journalisation de l'authentification Linux avec /var/log/auth.log. Comprenez les connexions des utilisateurs et dépannez les problèmes d'accès avec ce guide essentiel."
keywords: "authentification Linux, auth.log, journalisation Linux, connexion utilisateur, sécurité Linux, débutant, tutoriel, guide"
---

## Lesson Content

La journalisation de l'authentification peut être très utile si vous rencontrez des problèmes de connexion.

### /var/log/auth.log

Ce fichier contient les journaux d'autorisation du système, tels que les connexions des utilisateurs et les méthodes d'authentification utilisées.

Extrait d'exemple :

```plaintext
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

## Exercise

Effectuez quelques tentatives de connexion échouées, puis une tentative réussie. Ensuite, examinez votre fichier `/var/log/auth.log` pour voir ce qui s'est passé.

## Quiz Question

Quel fichier journal est utilisé pour l'authentification des utilisateurs ?

## Quiz Answer

auth.log
