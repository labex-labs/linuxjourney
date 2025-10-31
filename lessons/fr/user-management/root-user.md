---
index: 2
lang: "fr"
title: "Racine"
meta_title: "Racine - Gestion des utilisateurs"
meta_description: "Explorez le rôle de l'utilisateur root sous Linux. Cette leçon couvre les différences entre su et sudo pour obtenir les privilèges de superutilisateur et explique comment le fichier /etc/sudoers gère l'accès."
meta_keywords: "utilisateur root linux, utilisateur root, su, sudo, sudoers, visudo, superutilisateur, gestion des utilisateurs, permissions linux"
---

## Lesson Content

Sous Linux, certaines tâches administratives nécessitent des privilèges élevés. Ces privilèges appartiennent à un compte spécial connu sous le nom d'**utilisateur root sous Linux**. Bien que vous puissiez vous connecter directement en tant que root, il est souvent plus sûr et plus gérable d'obtenir un accès superutilisateur temporairement.

### La commande `su`

Outre la commande `sudo`, vous pouvez utiliser `su` (substitute user) pour obtenir les privilèges de superutilisateur. Lorsqu'elle est exécutée sans nom d'utilisateur, `su` tente d'ouvrir une nouvelle session shell pour l'**utilisateur root Linux**, vous demandant le mot de passe root.

```bash
su
```

Vous pouvez également utiliser cette commande pour passer à tout autre utilisateur du système, à condition de connaître son mot de passe.

### Risques d'un shell root persistant

L'utilisation de `su` pour ouvrir un shell root présente des inconvénients majeurs. Opérer continuellement en tant qu'utilisateur root augmente le risque de commettre une erreur critique modifiant le système. De plus, les actions effectuées dans un shell root ne sont pas enregistrées sous votre compte utilisateur personnel, ce qui rend difficile l'audit des modifications du système. Pour ces raisons, la meilleure pratique consiste à utiliser `sudo` pour les commandes individuelles nécessitant un accès superutilisateur.

### Le fichier `sudoers`

Alors, comment le système détermine-t-il qui est autorisé à utiliser `sudo` ? L'accès est contrôlé par un fichier de configuration situé à `/etc/sudoers`. Ce fichier répertorie les utilisateurs et les groupes qui sont autorisés à exécuter des commandes en tant que superutilisateur.

Pour modifier ce fichier en toute sécurité, vous devez toujours utiliser la commande `visudo`. Cet utilitaire ouvre le fichier `sudoers` dans un éditeur de texte et effectue une vérification de syntaxe avant d'enregistrer, ce qui aide à prévenir les erreurs de configuration qui pourraient vous priver de l'accès administratif.

## Exercise

Mettez vos connaissances en pratique. Le laboratoire pratique suivant vous aidera à renforcer votre compréhension de l'accès et des privilèges de superutilisateur :

1. **[Configurer les comptes utilisateurs et les privilèges Sudo sous Linux](https://labex.io/fr/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Entraînez-vous à appliquer les politiques de mots de passe, à verrouiller et déverrouiller les comptes utilisateurs, à sécuriser le compte root et à accorder des autorisations administratives, ce qui est directement lié à la gestion de l'accès superutilisateur.

Ce laboratoire vous aidera à appliquer les concepts dans des scénarios réels et à gagner en confiance dans la gestion des privilèges utilisateurs et de l'accès superutilisateur.

## Quiz Question

Quel fichier répertorie les utilisateurs et les groupes ayant des privilèges `sudo` ? Veuillez fournir le chemin complet. (Note : Votre réponse doit être en anglais et sensible à la casse).

## Quiz Answer

/etc/sudoers
