---
index: 5
lang: "fr"
title: "Journalisation de l'authentification"
meta_title: "Journalisation de l'authentification - Journalisation"
meta_description: "Découvrez la journalisation de l'authentification Linux avec /var/log/auth.log. Comprenez les connexions des utilisateurs et dépannez les problèmes d'accès avec ce guide essentiel."
meta_keywords: "Authentification Linux, auth.log, journalisation Linux, connexion utilisateur, sécurité Linux, débutant, tutoriel, guide"
---

## Lesson Content

La journalisation de l'authentification peut être très utile à consulter si vous rencontrez des problèmes de connexion.

### /var/log/auth.log

Ce fichier contient les journaux d'autorisation du système, tels que les connexions des utilisateurs et les méthodes d'authentification utilisées.

Extrait d'exemple :

```plaintext
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'authentification des utilisateurs et de la gestion des comptes :

1. **[Configurer les comptes d'utilisateur et les privilèges Sudo sous Linux](https://labex.io/fr/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Entraînez-vous à appliquer des politiques de mot de passe, à verrouiller/déverrouiller des comptes d'utilisateur, à sécuriser le compte root et à accorder des autorisations administratives, tout cela étant essentiel pour comprendre la sécurité de l'authentification.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion des utilisateurs et de la sécurité sous Linux.

## Quiz Question

Quel fichier journal est utilisé pour l'authentification des utilisateurs ?

## Quiz Answer

auth.log
