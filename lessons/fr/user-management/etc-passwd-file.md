---
index: 3
lang: "fr"
title: "/etc/passwd"
meta_title: "/etc/passwd - Gestion des utilisateurs"
meta_description: "Guide complet sur le fichier /etc/passwd sous Linux. Apprenez à interpréter les champs de données utilisateur, comprendre les UID, et voyez des exemples comme root:x:0:0:root:/root:/bin/bash."
meta_keywords: "/etc/passwd, /etc/passwd sous linux, root:x:0:0:root:/root:/bin/bash, identifiant utilisateur, UID, gestion des utilisateurs, tutoriel Linux"
---

## Lesson Content

Sous Linux, les noms d'utilisateur sont des étiquettes lisibles par l'homme, mais le système identifie les utilisateurs avec un identifiant d'utilisateur (UID) unique. La correspondance entre les noms d'utilisateur et les UID est stockée dans le fichier `/etc/passwd`, un composant essentiel pour la gestion des utilisateurs.

Pour visualiser son contenu, vous pouvez utiliser une commande simple :

```bash
cat /etc/passwd
```

Ce fichier affiche une liste de tous les utilisateurs du système et des informations détaillées à leur sujet. Chaque ligne représente un seul compte utilisateur.

### Décortiquer les champs de /etc/passwd

Une ligne typique de ce fichier, souvent la toute première, ressemble à ceci :

```plaintext
root:x:0:0:root:/root:/bin/bash
```

Cette entrée pour l'utilisateur `root` contient sept champs séparés par des deux-points (`:`). Comprendre la structure de `/etc/passwd` sous Linux est essentiel pour gérer les utilisateurs. Décomposons chaque champ :

1. **Nom d'utilisateur** : Le nom de connexion de l'utilisateur (par exemple, `root`).
2. **Mot de passe** : Un espace réservé pour le mot de passe chiffré de l'utilisateur. Le mot de passe réel n'est pas stocké ici pour des raisons de sécurité.
    - Un `x` indique que le mot de passe chiffré se trouve dans le fichier `/etc/shadow`.
    - Un `*` (astérisque) signifie que le compte est verrouillé et ne peut pas être utilisé pour la connexion.
    - Un champ vide signifie que l'utilisateur n'a pas de mot de passe.
3. **Identifiant d'utilisateur (UID)** : L'identifiant numérique unique de l'utilisateur. L'utilisateur `root` a toujours un UID de `0`.
4. **Identifiant de groupe (GID)** : L'identifiant numérique du groupe principal de l'utilisateur.
5. **Champ GECOS** : Un champ de commentaire qui contient traditionnellement des informations supplémentaires telles que le nom complet de l'utilisateur, le numéro de téléphone ou le lieu de bureau. Il est délimité par des virgules.
6. **Répertoire personnel** : Le chemin absolu vers le répertoire personnel de l'utilisateur (par exemple, `/root`).
7. **Shell par défaut** : L'interpréteur de commandes par défaut de l'utilisateur, qui est exécuté lors de la connexion (par exemple, `/bin/bash`).

### Utilisateurs système et comptes spéciaux

Lorsque vous inspectez le fichier `/etc/passwd`, vous remarquerez de nombreux comptes qui n'appartiennent pas à des utilisateurs humains. Ce sont des comptes système utilisés pour exécuter des services ou des processus spécifiques avec des autorisations limitées, améliorant ainsi la sécurité du système. Par exemple, l'utilisateur `daemon` est utilisé pour exécuter des processus de démon en arrière-plan.

### Modification du fichier /etc/passwd

Bien que vous puissiez techniquement modifier le fichier `/etc/passwd` directement à l'aide d'un éditeur de texte ou de la commande `vipw`, cela est fortement déconseillé. Les modifications manuelles peuvent facilement introduire des erreurs de syntaxe, vous bloquant potentiellement hors du système ou provoquant une instabilité.

Il est toujours plus sûr et plus fiable d'utiliser des utilitaires de ligne de commande dédiés tels que `useradd`, `usermod` et `userdel` pour gérer les comptes utilisateurs. Ces outils sont conçus pour modifier le fichier correctement et gérer toutes les configurations associées.

## Exercise

Pour consolider vos connaissances, essayez ces laboratoires pratiques. Ils vous aideront à appliquer les concepts d'identifiants d'utilisateur et de gestion de compte dans des scénarios réels et à renforcer votre confiance dans l'administration des utilisateurs Linux.

1. **[Gérer les comptes utilisateurs Linux avec useradd, usermod et userdel](https://labex.io/fr/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Entraînez-vous au cycle complet de l'administration des utilisateurs, de la création et de la sécurisation des nouveaux comptes à leur modification et suppression.
2. **[Gérer les groupes Linux avec groupadd, usermod et groupdel](https://labex.io/fr/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Acquérir une expérience pratique avec les utilitaires de ligne de commande essentiels pour l'administration des groupes, y compris la création de nouveaux groupes et la modification des appartenances des utilisateurs.
3. **[Configurer les comptes utilisateurs et les privilèges Sudo sous Linux](https://labex.io/fr/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Apprenez les techniques essentielles pour gérer les comptes utilisateurs et les privilèges sudo afin d'améliorer la sécurité d'un système Linux.

## Quiz Question

Si un compte utilisateur est verrouillé et ne peut pas être utilisé pour la connexion, comment cela est-il indiqué dans le champ mot de passe du fichier /etc/passwd ? Veuillez répondre en utilisant uniquement le caractère requis.

## Quiz Answer

`*`
