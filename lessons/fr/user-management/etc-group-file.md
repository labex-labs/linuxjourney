---
index: 5
lang: "fr"
title: "/etc/group"
meta_title: "/etc/group - Gestion des utilisateurs"
meta_description: "Explorez le fichier /etc/group sous Linux pour comprendre la gestion des groupes. Apprenez à visualiser les données des groupes avec cat /etc/group, et comprenez la structure incluant le GID et les listes d'utilisateurs. Ce guide couvre l'essentiel du fichier etc group linux."
meta_keywords: "/etc/group, /etc/group linux, fichier /etc/group sous linux, cat /etc/group, etc group linux, gestion des groupes, GID, permissions Linux, groupes Linux"
---

## Lesson Content

Sous Linux, la gestion des permissions pour plusieurs utilisateurs est simplifiée grâce à l'utilisation de groupes. Le fichier central pour cela est `/etc/group`, qui définit les groupes sur le système et leurs membres.

### Qu'est-ce que le fichier /etc/group ?

Le fichier `/etc/group` sous Linux est un fichier texte simple qui contient la liste de tous les groupes d'utilisateurs. Chaque groupe peut se voir attribuer des permissions spécifiques sur les fichiers et les répertoires, permettant aux administrateurs de gérer efficacement les droits d'accès pour plusieurs utilisateurs à la fois. Comprendre ce fichier est crucial pour une gestion appropriée des utilisateurs et des permissions dans tout environnement `etc group linux`.

### Affichage des informations de groupe

Pour inspecter le contenu de ce fichier, vous pouvez utiliser une commande simple. L'exécution de `cat /etc/group` dans votre terminal affichera toutes les définitions de groupe sur votre système.

```bash
$ cat /etc/group

root:*:0:pete
```

### Structure du fichier /etc/group

Similaire au fichier `/etc/passwd`, chaque ligne du fichier `/etc/group` représente un seul groupe et contient quatre champs séparés par des deux-points (`:`).

1. **Nom du groupe** : Le nom unique du groupe.
2. **Mot de passe du groupe** : Ce champ est une fonctionnalité héritée et est rarement utilisé. Les systèmes modernes utilisent des outils comme `sudo` pour les privilèges élevés au lieu des mots de passe de groupe. Vous verrez généralement un espace réservé comme un astérisque (`*`) ou un 'x'.
3. **Identifiant de groupe (GID)** : Un identifiant numérique unique pour le groupe. Le système utilise souvent le GID en interne au lieu du nom du groupe.
4. **Liste des utilisateurs** : Une liste séparée par des virgules des noms d'utilisateur qui sont membres de ce groupe.

Dans l'exemple `root:*:0:pete`, le nom du groupe est `root`, il n'y a pas de mot de passe, le GID est `0`, et l'utilisateur `pete` en est membre.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des utilisateurs et des groupes sous Linux :

1. **[Gérer les comptes utilisateurs Linux avec useradd, usermod et userdel](https://labex.io/fr/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Entraînez-vous au cycle de vie complet de l'administration des utilisateurs, de la création et de la sécurisation des nouveaux comptes à leur modification et suppression.
2. **[Gérer les groupes Linux avec groupadd, usermod et groupdel](https://labex.io/fr/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Acquérir une expérience pratique avec les utilitaires de ligne de commande essentiels pour l'administration des groupes, y compris `groupadd`, `usermod` et `groupdel`.
3. **[Ajouter un nouvel utilisateur et un nouveau groupe](https://labex.io/fr/labs/linux-add-new-user-and-group-17987)** - Simulez l'ajout de nouveaux membres d'équipe à un environnement serveur en créant de nouveaux comptes utilisateurs, en configurant des groupes personnalisés et en gérant les appartenances aux groupes.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion des utilisateurs et des groupes sous Linux.

## Quiz Question

Quel est le GID de root ?

## Quiz Answer

0
