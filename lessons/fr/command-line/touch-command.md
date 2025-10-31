---
index: 5
lang: "fr"
title: "touch"
meta_title: "touch - Ligne de commande"
meta_description: "Apprenez à utiliser la commande linux touch pour créer des fichiers et gérer les horodatages. Ce guide couvre la commande touch sous linux, y compris les options comme linux touch -r et touch -d."
meta_keywords: "linux touch, commande touch linux, bash touch, touch -d linux, linux touch -r, créer des fichiers, mettre à jour les horodatages, gestion de fichiers, commandes linux"
---

## Lesson Content

La commande `touch` est un utilitaire standard sur les systèmes d'exploitation de type Unix. Bien que son objectif principal soit de modifier les horodatages des fichiers, elle est également couramment utilisée pour créer de nouveaux fichiers vides. Explorons comment fonctionne la commande `linux touch`.

### Création de nouveaux fichiers

La manière la plus simple de créer un fichier vide est d'utiliser la commande `touch` suivie d'un nom de fichier. Si le fichier n'existe pas, `touch` le créera pour vous. Il s'agit d'une opération fondamentale de `bash touch` pour le scripting et les tâches quotidiennes.

```bash
touch mysuperduperfile
```

Après avoir exécuté cette commande, un nouveau fichier vide nommé `mysuperduperfile` apparaîtra dans votre répertoire courant. Vous pouvez créer plusieurs fichiers à la fois en listant leurs noms.

```bash
touch file1.txt file2.txt file3.log
```

### Mise à jour des horodatages des fichiers

La fonction originale de la `commande touch sous linux` est de mettre à jour les horodatages d'accès et de modification d'un fichier ou d'un répertoire. Si vous utilisez `touch` sur un fichier existant, il mettra à jour ses horodatages à l'heure actuelle.

Vous pouvez le vérifier en utilisant `ls -l` pour vérifier l'horodatage d'un fichier, en exécutant `touch` dessus, puis en vérifiant à nouveau.

```bash
# Vérifier l'horodatage original
ls -l mysuperduperfile

# Mettre à jour l'horodatage
touch mysuperduperfile

# Vérifier le nouvel horodatage
ls -l mysuperduperfile
```

### Contrôle avancé des horodatages

La commande `linux touch` fournit également des options pour une manipulation plus précise des horodatages.

#### Utilisation d'un fichier de référence

L'option `linux touch -r` vous permet de définir l'horodatage d'un fichier pour qu'il corresponde à celui d'un autre fichier (un fichier de référence). Ceci est utile pour synchroniser les horodatages entre fichiers connexes.

```bash
# Définir l'horodatage de file2.txt pour qu'il corresponde à celui de file1.txt
touch -r file1.txt file2.txt
```

#### Définition d'une date spécifique

Avec l'option `touch -d`, vous pouvez définir l'horodatage d'un fichier à une date et une heure spécifiques. La fonctionnalité `touch -d linux` accepte divers formats de chaîne pour la date.

```bash
# Définir l'horodatage à une date et heure spécifiques
touch -d "2023-01-01 12:30:00" mysuperduperfile
```

Maîtriser `touch` est une excellente étape pour apprendre à gérer efficacement votre système de fichiers depuis la ligne de commande.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la création et de la gestion des objets du système de fichiers :

1. **[Commande Linux mkdir : Création de répertoires](https://labex.io/fr/labs/linux-linux-mkdir-command-directory-creating-209739)** - Apprenez à utiliser la commande `mkdir` sous Linux pour créer des répertoires, définir des permissions et organiser votre système de fichiers. Cela vous aidera à comprendre le concept plus large de création de nouveaux éléments dans le système de fichiers.
2. **[Configuration d'une nouvelle structure de projet](https://labex.io/fr/labs/linux-setting-up-a-new-project-structure-387859)** - Entraînez-vous à gérer les répertoires Linux en créant une structure de projet spécifique et en y naviguant à l'aide de commandes essentielles comme `mkdir` et `cd`.

Ces laboratoires vous aideront à appliquer les concepts de création et d'organisation du système de fichiers dans des scénarios réels et à renforcer votre confiance avec les commandes Linux.

## Quiz Question

Comment créez-vous un fichier nommé `myfile` ? Veuillez répondre en utilisant uniquement la commande anglaise, en faisant attention à la casse.

## Quiz Answer

touch myfile
