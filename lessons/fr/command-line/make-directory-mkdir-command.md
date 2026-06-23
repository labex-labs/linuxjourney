---
index: 12
lang: "fr"
title: "mkdir (Créer un répertoire)"
meta_title: "mkdir (Créer un répertoire) - Ligne de commande"
meta_description: "Apprenez la commande Linux mkdir avec des exemples pour créer un répertoire, plusieurs répertoires, des répertoires parents imbriqués et définir les permissions."
meta_keywords: "commande mkdir, linux mkdir, créer répertoire linux, faire répertoire linux, mkdir -p, mkdir -m, créer dossier linux"
---

## Lesson Content

Lorsque vous travaillez avec des fichiers, vous devrez les organiser dans des répertoires. L'outil principal pour cette tâche est la commande `mkdir`, qui signifie make directory (créer un répertoire).

La syntaxe de base est :

```bash
mkdir [OPTIONS] DIRECTORY...
```

### Créer un répertoire unique

L'utilisation la plus basique de `mkdir` est de créer un nouveau répertoire unique. Si le répertoire n'existe pas déjà, cette commande le crée à l'emplacement courant.

```bash
$ mkdir documents
```

### Créer plusieurs répertoires

Vous pouvez aussi créer plusieurs répertoires en une seule fois en listant leurs noms, séparés par des espaces. C'est une manière efficace de configurer rapidement plusieurs dossiers.

```bash
$ mkdir books paintings
```

### Créer des répertoires imbriqués

Parfois, vous devez créer un répertoire ainsi que ses répertoires parents simultanément. L'option `-p` est parfaite pour cela. Elle évite les erreurs si les répertoires parents n'existent pas.

```bash
$ mkdir -p books/hemingway/favorites
```

Cette seule commande crée `books`, `hemingway` et `favorites` s'ils n'existent pas déjà.

### Définir les permissions du répertoire

Utilisez `-m` pour définir les permissions lors de la création d'un répertoire.

```bash
$ mkdir -m 755 public
```

Vous en apprendrez plus sur les permissions plus tard, mais cet exemple crée un répertoire que le propriétaire peut écrire et que les autres peuvent lire et parcourir.

### Options courantes de mkdir

- `-p` : Crée les répertoires parents si nécessaire.
- `-m MODE` : Définit les permissions pour le nouveau répertoire.
- `-v` : Affiche un message pour chaque répertoire créé.

Exemple :

```bash
$ mkdir -pv projects/app/src
mkdir: created directory 'projects'
mkdir: created directory 'projects/app'
mkdir: created directory 'projects/app/src'
```

### Questions fréquentes

**Pourquoi mkdir affiche-t-il "File exists" ?** Un fichier ou répertoire portant ce nom existe déjà. Utilisez `ls` pour l'inspecter.

**Comment créer des répertoires imbriqués ?** Utilisez `mkdir -p parent/child/grandchild`.

**Est-ce que mkdir peut créer des fichiers ?** Non. Utilisez `touch` pour créer des fichiers vides.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la création et gestion des répertoires :

1. **[Commande Linux mkdir : création de répertoire](https://labex.io/fr/labs/linux-linux-mkdir-command-directory-creating-209739)** - Apprenez à utiliser la commande `mkdir` sous Linux pour créer des répertoires, définir des permissions et organiser votre système de fichiers. Ce laboratoire couvre les usages basiques et avancés, y compris la création de répertoires imbriqués.
2. **[Mise en place d'une nouvelle structure de projet](https://labex.io/fr/labs/linux-setting-up-a-new-project-structure-387859)** - Entraînez-vous à gérer les répertoires Linux en créant une structure de projet spécifique et en naviguant à travers elle avec des commandes essentielles comme `mkdir` et `cd`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance pour créer et organiser des répertoires sous Linux.

## Quiz Question

Quelle commande est utilisée pour créer un répertoire ? Veuillez répondre uniquement avec la commande en anglais en minuscules.

## Quiz Answer

mkdir
