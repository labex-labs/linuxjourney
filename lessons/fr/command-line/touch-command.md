---
index: 5
lang: "fr"
title: "touch"
meta_title: "touch - Ligne de commande"
meta_description: "Apprenez la commande Linux touch avec des exemples pour créer des fichiers vides, mettre à jour les horodatages, définir des dates, utiliser des fichiers de référence et éviter les écrasements."
meta_keywords: "commande linux touch, commande touch, créer fichier linux, mettre à jour horodatage linux, touch -d, touch -r, touch -c"
---

## Lesson Content

La commande `touch` est un utilitaire standard sur les systèmes d'exploitation de type Unix. Bien que sa fonction principale soit de modifier les horodatages des fichiers, elle est également couramment utilisée pour créer de nouveaux fichiers vides.

La syntaxe de base est :

```bash
touch [OPTIONS] FILE...
```

### Création de nouveaux fichiers

La manière la plus simple de créer un fichier vide est d'utiliser `touch` suivi d'un nom de fichier. Si le fichier n'existe pas, `touch` le crée.

```bash
$ touch mysuperduperfile
```

Après avoir exécuté cette commande, un nouveau fichier vide nommé `mysuperduperfile` apparaîtra dans votre répertoire courant. Vous pouvez créer plusieurs fichiers à la fois en listant leurs noms.

```bash
$ touch file1.txt file2.txt file3.log
```

Cela est utile lors de la mise en place d'une structure de projet ou pour créer des fichiers temporaires avant d'ajouter du contenu.

### Mise à jour des horodatages des fichiers

La fonction originale de `touch` est de mettre à jour les horodatages d'accès et de modification d'un fichier ou d'un répertoire. Si vous utilisez `touch` sur un fichier existant, il met à jour ses horodatages à l'heure actuelle.

Vous pouvez vérifier cela en utilisant `ls -l` pour consulter l'horodatage d'un fichier, en exécutant `touch` dessus, puis en vérifiant à nouveau.

```bash
# Check the original timestamp
$ ls -l mysuperduperfile

# Update the timestamp
$ touch mysuperduperfile

# Check the new timestamp
$ ls -l mysuperduperfile
```

### Contrôle avancé des horodatages

La commande `touch` offre également des options pour une manipulation plus précise des horodatages.

Utilisez un fichier de référence avec `-r` pour copier les horodatages d'un fichier vers un autre.

```bash
$ touch -r file1.txt file2.txt
```

Définissez une date et une heure spécifiques avec `-d` :

```bash
$ touch -d "2026-06-23 12:30:00" mysuperduperfile
```

Utilisez `-c` lorsque vous souhaitez mettre à jour un fichier uniquement s'il existe déjà. Avec `-c`, `touch` ne créera pas un fichier manquant.

```bash
$ touch -c existing-file.txt
```

### Options courantes de touch

- `-a` : Modifier uniquement l'heure d'accès.
- `-m` : Modifier uniquement l'heure de modification.
- `-c` : Ne pas créer le fichier s'il n'existe pas.
- `-d "DATE"` : Utiliser une chaîne de date spécifique.
- `-r FILE` : Utiliser l'horodatage d'un autre fichier comme référence.
- `-t STAMP` : Utiliser un horodatage au format numérique compact.

Par exemple, ceci modifie uniquement l'heure de modification :

```bash
$ touch -m notes.txt
```

### Questions fréquentes

**Est-ce que touch ajoute du texte à un fichier ?** Non. `touch` crée un fichier vide ou met à jour les horodatages. Utilisez un éditeur, `echo` ou `cat` pour ajouter du texte.

**Est-ce que touch écrase un fichier existant ?** Non. Il met à jour les horodatages mais ne remplace pas le contenu du fichier.

**Pourquoi utiliser touch dans les scripts ?** C'est un moyen rapide de s'assurer qu'un fichier existe ou de marquer qu'une tâche a eu lieu à un moment donné.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la création et de la gestion des objets du système de fichiers :

1. **[Commande Linux mkdir : création de répertoire](https://labex.io/fr/labs/linux-linux-mkdir-command-directory-creating-209739)** - Apprenez à utiliser la commande `mkdir` sous Linux pour créer des répertoires, définir des permissions et organiser votre système de fichiers. Cela vous aidera à comprendre le concept plus large de création de nouveaux éléments dans le système de fichiers.
2. **[Mise en place d'une nouvelle structure de projet](https://labex.io/fr/labs/linux-setting-up-a-new-project-structure-387859)** - Entraînez-vous à gérer les répertoires Linux en créant une structure de projet spécifique et en naviguant à travers elle avec des commandes essentielles comme `mkdir` et `cd`.

Ces laboratoires vous aideront à appliquer les concepts de création et d'organisation du système de fichiers dans des scénarios réels et à gagner en confiance avec les commandes Linux.

## Quiz Question

Comment créez-vous un fichier appelé `myfile` ? Veuillez répondre uniquement avec la commande en anglais, en respectant la casse.

## Quiz Answer

touch myfile
