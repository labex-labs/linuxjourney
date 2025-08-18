---
lang: "fr"
title: "/etc/passwd"
meta_title: "/etc/passwd - Gestion des Utilisateurs"
meta_description: "Découvrez le fichier /etc/passwd sous Linux, comprenez les champs d'informations utilisateur et le fonctionnement des UID. Explorez ce fichier de configuration essentiel."
meta_keywords: "/etc/passwd, utilisateurs Linux, ID utilisateur, UID, tutoriel Linux, débutant, guide, commandes Linux"
---

## Lesson Content

Rappelez-vous que les noms d'utilisateur ne sont pas vraiment des identifications pour les utilisateurs. Le système utilise un ID utilisateur (UID) pour identifier un utilisateur. Pour savoir quels utilisateurs sont mappés à quel ID, consultez le fichier `/etc/passwd`.

```bash
cat /etc/passwd
```

Ce fichier vous montre une liste d'utilisateurs et des informations détaillées à leur sujet. Par exemple, la première ligne de ce fichier ressemble très probablement à ceci :

```plaintext
root:x:0:0:root:/root:/bin/bash
```

Chaque ligne affiche les informations d'un utilisateur ; le plus souvent, vous verrez l'utilisateur root comme première ligne. Il y a de nombreux champs séparés par des deux-points qui vous donnent des informations supplémentaires sur l'utilisateur. Examinons-les tous :

1. **Nom d'utilisateur**
2. **Mot de passe de l'utilisateur** - Le mot de passe n'est pas réellement stocké dans ce fichier ; il est généralement stocké dans le fichier `/etc/shadow`. Nous discuterons davantage de `/etc/shadow` dans la prochaine leçon, mais pour l'instant, sachez qu'il contient les mots de passe chiffrés des utilisateurs. Vous pouvez voir de nombreux symboles différents dans ce champ : si vous voyez un "x", cela signifie que le mot de passe est stocké dans le fichier `/etc/shadow` ; un "\*" signifie que l'utilisateur n'a pas d'accès de connexion ; et s'il y a un champ vide, cela signifie que l'utilisateur n'a pas de mot de passe.
3. **L'ID utilisateur** - Comme vous pouvez le voir, root a l'UID de 0.
4. **L'ID de groupe**
5. **Champ GECOS** - Ceci est utilisé pour laisser des commentaires généraux sur l'utilisateur ou le compte, tels que son nom réel ou son numéro de téléphone. Il est délimité par des virgules.
6. **Répertoire personnel de l'utilisateur**
7. **Shell de l'utilisateur** - Vous verrez probablement de nombreux utilisateurs par défaut utiliser bash comme shell.

Normalement, dans la page de paramètres d'un utilisateur, vous vous attendriez à ne voir que des utilisateurs humains. Cependant, vous remarquerez que `/etc/passwd` contient d'autres utilisateurs. Rappelez-vous que les utilisateurs ne sont réellement sur le système que pour exécuter des processus avec des permissions différentes. Parfois, nous voulons exécuter des processus avec des permissions prédéterminées. Par exemple, l'utilisateur `daemon` est utilisé pour les processus daemon.

Il convient également de noter que vous pouvez modifier le fichier `/etc/passwd` à la main si vous souhaitez ajouter des utilisateurs et modifier des informations avec l'outil `vipw`. Cependant, des choses comme celles-ci sont mieux laissées aux outils que nous discuterons dans une leçon ultérieure, tels que `useradd` et `userdel`.

## Exercise

Regardez votre fichier `/etc/passwd`, examinez certains des utilisateurs et notez l'accès qu'ils ont.

## Quiz Question

Si un utilisateur n'a pas d'accès de connexion, comment cela est-il indiqué dans `/etc/passwd` ?

## Quiz Answer

-
