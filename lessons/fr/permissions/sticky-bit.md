---
index: 8
lang: "fr"
title: "Le Bit Collant"
meta_title: "Le Bit Collant - Permissions"
meta_description: "Explorez l'utilité du bit collant dans les permissions de fichiers Linux et Unix. Apprenez comment le bit collant protège les fichiers dans les répertoires partagés comme /tmp et comment le définir avec chmod."
meta_keywords: "bit collant, bit collant linux, permissions fichiers unix bit collant, chmod +t, répertoire /tmp, permissions fichiers, sécurité linux"
---

## Lesson Content

Au-delà des permissions standard de lecture, d'écriture et d'exécution, Linux offre des permissions spéciales pour un contrôle d'accès avancé. La dernière de ces permissions spéciales que nous aborderons est le **bit collant** (sticky bit).

### Qu'est-ce que le Bit Collant ?

Le bit collant est un paramètre de permission qui peut être appliqué à un répertoire. Lorsqu'un répertoire a le bit collant défini, les fichiers qu'il contient ne peuvent être ni supprimés ni renommés que par le propriétaire du fichier, le propriétaire du répertoire ou l'utilisateur root. Ceci est particulièrement utile pour les répertoires partagés où plusieurs utilisateurs doivent créer et gérer leurs propres fichiers sans interférer avec les autres. Ce concept est une partie essentielle de la gestion des **permissions de fichiers Unix bit collant**.

### Un Exemple Pratique : Le Répertoire /tmp

Un cas d'utilisation courant pour le **bit collant sous Linux** est le répertoire `/tmp`, qui est un emplacement accessible en écriture par tous pour les fichiers temporaires. Examinons ses permissions :

```bash
$ ls -ld /tmp
drwxrwxrwt 17 root root 4096 Dec 15 11:45 /tmp
```

Remarquez le `t` à la fin de la chaîne de permissions (`rwxrwxrwt`). Ce `t` indique que le bit collant est défini. Grâce à cela, bien que tout utilisateur puisse créer des fichiers dans `/tmp`, il ne peut pas supprimer ou déplacer les fichiers créés par d'autres utilisateurs. Cela empêche un utilisateur de perturber le travail d'un autre dans cet espace partagé.

### Comment Définir le Bit Collant

Vous pouvez définir le bit collant à l'aide de la commande `chmod` de deux manières : mode symbolique ou mode octal (numérique).

Pour ajouter le bit collant en mode symbolique :

```bash
chmod +t mon_repertoire_partage
```

Pour définir les permissions en mode octal, vous préfixez un `1` au code de permission standard à trois chiffres. La représentation numérique du bit collant est **1**.

```bash
# Ceci définit les permissions à rwxr-xr-x avec le bit collant
chmod 1755 mon_repertoire_partage
```

Comprendre le bit collant est essentiel pour gérer efficacement les environnements multi-utilisateurs et sécuriser les répertoires partagés.

## Exercise

Pour consolider votre compréhension des permissions de fichiers, y compris les permissions spéciales comme le bit collant, essayez ces laboratoires pratiques. Ils vous aideront à voir comment ces concepts s'appliquent dans des scénarios réels.

1. **[Groupes d'Utilisateurs Linux et Permissions de Fichiers](https://labex.io/fr/labs/linux-linux-user-group-and-file-permissions-18002)** - Entraînez-vous à créer des utilisateurs et des groupes, et à manipuler la propriété et les permissions des fichiers. Ce laboratoire fournit une base pour comprendre le fonctionnement des permissions spéciales.
2. **[Supprimer et Déplacer des Fichiers](https://labex.io/fr/labs/linux-delete-and-move-files-7777)** - Apprenez à supprimer et déplacer des fichiers, et voyez comment les permissions, y compris le bit collant sur un répertoire, peuvent restreindre ces actions.
3. **[Trouver un Fichier](https://labex.io/fr/labs/linux-find-a-file-17993)** - Entraînez-vous à localiser des fichiers et à définir des contrôles d'accès, renforçant l'importance des permissions de fichiers dans la gestion de l'accès et de la modification des fichiers.

## Quiz Question

Dans un affichage détaillé du répertoire (ls -l), quel caractère unique dans la chaîne de permissions représente que le bit collant est défini ? Veuillez répondre avec une seule lettre minuscule anglaise.

## Quiz Answer

t
