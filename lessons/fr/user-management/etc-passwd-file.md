---
index: 3
lang: "fr"
title: "/etc/passwd"
meta_title: "/etc/passwd - Gestion des utilisateurs"
meta_description: "Apprenez-en davantage sur le fichier /etc/passwd sous Linux, comprenez les champs d'informations utilisateur et le fonctionnement des UID. Explorez ce fichier de configuration essentiel."
meta_keywords: "/etc/passwd, utilisateurs Linux, ID utilisateur, UID, tutoriel Linux, débutant, guide, commandes Linux"
---

## Lesson Content

N'oubliez pas que les noms d'utilisateur ne sont pas réellement des identifiants pour les utilisateurs. Le système utilise un identifiant d'utilisateur (UID) pour identifier un utilisateur. Pour savoir quels utilisateurs sont mappés à quel identifiant, consultez le fichier `/etc/passwd`.

```bash
cat /etc/passwd
```

Ce fichier vous montre une liste d'utilisateurs et des informations détaillées à leur sujet. Par exemple, la première ligne de ce fichier ressemble très probablement à ceci :

```plaintext
root:x:0:0:root:/root:/bin/bash
```

Chaque ligne affiche les informations d'un utilisateur ; le plus souvent, vous verrez l'utilisateur root comme première ligne. Il y a de nombreux champs séparés par des deux-points qui vous donnent des informations supplémentaires sur l'utilisateur. Examinons-les tous :

1. **Nom d'utilisateur**
2. **Mot de passe de l'utilisateur** - Le mot de passe n'est pas réellement stocké dans ce fichier ; il est généralement stocké dans le fichier `/etc/shadow`. Nous discuterons davantage de `/etc/shadow` dans la prochaine leçon, mais pour l'instant, sachez qu'il contient les mots de passe chiffrés des utilisateurs. Vous pouvez voir de nombreux symboles différents dans ce champ : si vous voyez un "x", cela signifie que le mot de passe est stocké dans le fichier `/etc/shadow` ; un "*" signifie que l'utilisateur n'a pas d'accès de connexion ; et s'il y a un champ vide, cela signifie que l'utilisateur n'a pas de mot de passe.
3. **L'identifiant de l'utilisateur** - Comme vous pouvez le voir, root a l'UID de 0.
4. **L'identifiant du groupe**
5. **Champ GECOS** - Ceci est utilisé pour laisser des commentaires généraux sur l'utilisateur ou le compte, tels que son nom réel ou son numéro de téléphone. Il est délimité par des virgules.
6. **Répertoire personnel de l'utilisateur**
7. **Shell de l'utilisateur** - Vous verrez probablement de nombreux utilisateurs utiliser bash par défaut pour leur shell.

Normalement, dans la page de configuration d'un utilisateur, vous vous attendriez à ne voir que des utilisateurs humains. Cependant, vous remarquerez que `/etc/passwd` contient d'autres utilisateurs. N'oubliez pas que les utilisateurs ne sont réellement sur le système que pour exécuter des processus avec des permissions différentes. Parfois, nous voulons exécuter des processus avec des permissions prédéterminées. Par exemple, l'utilisateur `daemon` est utilisé pour les processus démon.

Il convient également de noter que vous pouvez modifier le fichier `/etc/passwd` à la main si vous souhaitez ajouter des utilisateurs et modifier des informations avec l'outil `vipw`. Cependant, des choses comme celles-ci sont mieux laissées aux outils que nous discuterons dans une leçon ultérieure, tels que `useradd` et `userdel`.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des comptes d'utilisateurs Linux et de leur gestion :

1. **[Gérer les comptes d'utilisateurs Linux avec useradd, usermod et userdel](https://labex.io/fr/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Pratiquez le cycle de vie complet de l'administration des utilisateurs, de la création et de la sécurisation de nouveaux comptes à leur modification et suppression.
2. **[Gérer les groupes Linux avec groupadd, usermod et groupdel](https://labex.io/fr/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Acquérez une expérience pratique avec les utilitaires de ligne de commande essentiels pour l'administration des groupes, y compris la création de nouveaux groupes et la modification des appartenances des utilisateurs.
3. **[Configurer les comptes d'utilisateurs et les privilèges Sudo sous Linux](https://labex.io/fr/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Apprenez les techniques essentielles pour gérer les comptes d'utilisateurs et les privilèges sudo afin d'améliorer la sécurité d'un système Linux.

Ces laboratoires vous aideront à appliquer les concepts d'identifiants d'utilisateur et de gestion de compte dans des scénarios réels et à renforcer votre confiance dans l'administration des utilisateurs Linux.

## Quiz Question

Si un utilisateur n'a pas d'accès de connexion, comment cela est-il indiqué dans `/etc/passwd` ?

## Quiz Answer

-
