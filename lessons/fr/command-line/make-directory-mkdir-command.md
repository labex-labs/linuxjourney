---
index: 12
lang: "fr"
title: "mkdir (Créer un Répertoire)"
meta_title: "mkdir (Créer un Répertoire) - Ligne de Commande"
meta_description: "Apprenez à utiliser la commande mkdir sous Linux pour créer un nouveau répertoire. Ce guide couvre la commande pour créer un dossier sous Linux, y compris comment créer plusieurs répertoires et des répertoires parents depuis l'invite de commande."
meta_keywords: "créer répertoire linux, commande mkdir linux, créer répertoire linux, commande créer répertoire invite, commande créer dossier linux, mkdir, créer répertoire, linux"
---

## Lesson Content

Lorsque vous travaillez avec des fichiers, vous devrez les organiser dans des répertoires. L'outil principal pour cette tâche est la commande `mkdir`, qui signifie "Make Directory" (Créer un Répertoire). Cette commande vous permet de **créer un répertoire sous Linux** directement depuis votre terminal ou votre **invite de commande**.

### Créer un Répertoire Unique

L'utilisation la plus basique de la **commande mkdir sous Linux** est de créer un seul nouveau répertoire. Si le répertoire n'existe pas déjà, cette commande le créera à votre emplacement actuel. Par exemple, pour créer un répertoire nommé `documents` :

```bash
mkdir documents
```

### Créer Plusieurs Répertoires

Vous pouvez également créer plusieurs répertoires à la fois en listant leurs noms, séparés par des espaces. C'est une manière efficace de configurer plusieurs dossiers rapidement.

```bash
mkdir livres peintures
```

### Créer des Répertoires Imbriqués

Parfois, vous devez créer un répertoire et ses répertoires parents simultanément. L'option `-p` (parent) est parfaite pour cela. Cette fonctionnalité puissante de la **commande pour créer un dossier sous Linux** empêche les erreurs si les répertoires parents n'existent pas. Par exemple, pour créer le répertoire `favoris` à l'intérieur de `hemmingway`, qui est à l'intérieur de `livres` :

```bash
mkdir -p livres/hemmingway/favoris
```

Cette seule commande crée `livres`, `hemmingway` et `favoris` s'ils n'existent pas déjà, démontrant une capacité clé lorsque vous devez **créer un répertoire sous Linux**.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la création et de la gestion des répertoires :

1. **[Commande mkdir Linux : Création de Répertoires](https://labex.io/fr/labs/linux-linux-mkdir-command-directory-creating-209739)** - Apprenez à utiliser la commande `mkdir` sous Linux pour créer des répertoires, définir des permissions et organiser votre système de fichiers. Ce laboratoire couvre l'utilisation de base et avancée, y compris la création de répertoires imbriqués.
2. **[Configuration d'une Nouvelle Structure de Projet](https://labex.io/fr/labs/linux-setting-up-a-new-project-structure-387859)** - Entraînez-vous à gérer les répertoires Linux en créant une structure de projet spécifique et en naviguant à travers elle à l'aide de commandes essentielles comme `mkdir` et `cd`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance dans la création et l'organisation des répertoires sous Linux.

## Quiz Question

Quelle commande est utilisée pour créer un répertoire ? Veuillez répondre en utilisant uniquement la commande anglaise en minuscules.

## Quiz Answer

mkdir
