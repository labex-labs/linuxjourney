---
index: 11
lang: "fr"
title: "mv (Déplacer)"
meta_title: "mv (Déplacer) - Ligne de commande"
meta_description: "Apprenez la commande Linux mv avec des exemples pour déplacer des fichiers, renommer des fichiers et des répertoires, déplacer plusieurs fichiers et éviter les écrasements."
meta_keywords: "commande linux mv, commande mv, déplacer fichiers linux, renommer fichier linux, renommer répertoire linux, mv -i, mv -n, mv -t"
---

## Lesson Content

La commande `mv`, abréviation de "move" (déplacer), est un utilitaire fondamental dans tout environnement Linux. Elle sert principalement à deux choses : renommer des fichiers ou des répertoires et les déplacer vers un autre emplacement.

La syntaxe de base est :

```bash
mv [OPTIONS] SOURCE DESTINATION
```

Contrairement à `cp`, qui crée une copie, `mv` change l'emplacement ou le nom de l'élément original.

### Renommer des fichiers et des répertoires

L'une des utilisations les plus courantes de `mv` est le renommage. La syntaxe est simple : spécifiez l'ancien nom et le nouveau nom.

Pour renommer un fichier :

```bash
$ mv oldfile newfile
```

Cette même logique s'applique pour renommer des répertoires :

```bash
$ mv old_directory_name new_directory_name
```

### Déplacer des fichiers et des répertoires

L'autre fonction principale de la commande `mv` est de déplacer des éléments d'un emplacement à un autre.

Pour déplacer un seul fichier dans un autre répertoire :

```bash
$ mv file2 /home/pete/Documents
```

Vous pouvez aussi déplacer plusieurs fichiers à la fois. Il suffit de lister tous les fichiers sources suivis du répertoire cible :

```bash
$ mv file_1 file_2 somedirectory/
```

Sur les systèmes GNU/Linux, une option utile est `-t`, qui permet de spécifier d'abord le répertoire cible. Cela peut être plus clair lorsqu'on déplace beaucoup de fichiers.

```bash
$ mv -t somedirectory/ file_1 file_2
```

Contrairement à la commande `cp`, vous n'avez pas besoin d'une option récursive pour déplacer un répertoire. `mv` gère les répertoires par défaut.

### Options importantes pour la commande mv

Par défaut, si vous déplacez un fichier vers une destination où un fichier du même nom existe déjà, `mv` l'écrasera sans avertissement. Pour éviter toute perte de données accidentelle, vous pouvez utiliser les options suivantes :

- **-i (interactif)** : C'est une fonction de sécurité cruciale. Elle vous demandera une confirmation avant d'écraser un fichier existant.

  ```bash
  $ mv -i source_file destination_directory
  ```

- **-b (backup)** : Si vous souhaitez écraser un fichier mais garder l'ancienne version, cette option crée une sauvegarde du fichier de destination. La sauvegarde est généralement renommée avec un suffixe tilde (`~`).

  ```bash
  $ mv -b file1 directory_with_file1
  ```

- **-v (verbeux)** : Cette option fait que la commande `mv` affiche ce qu'elle fait, montrant chaque fichier déplacé ou renommé.

  ```bash
  $ mv -v file1 file2 somedirectory/
  ```

Une autre option utile est `-n`, qui signifie "no clobber" (ne pas écraser). Elle empêche d'écraser un fichier de destination existant.

```bash
$ mv -n source_file destination_directory
```

### Exemples courants de mv

Renommer un fichier :

```bash
$ mv draft.txt final.txt
```

Déplacer un répertoire :

```bash
$ mv project /home/pete/Documents/
```

Déplacer tous les fichiers texte dans un dossier :

```bash
$ mv *.txt notes/
```

Prévisualisez les correspondances de caractères génériques avec `ls` avant de déplacer plusieurs fichiers.

### Questions fréquentes

**Est-ce que mv copie les fichiers ?** Non. `mv` déplace ou renomme l'élément original.

**Est-ce que mv peut écraser des fichiers ?** Oui. Utilisez `mv -i` pour demander avant ou `mv -n` pour éviter l'écrasement.

**Ai-je besoin de mv -r pour les répertoires ?** Non. `mv` déplace les répertoires sans `-r`.

## Exercise

La pratique rend parfait ! L'expérience pratique est cruciale pour maîtriser les commandes Linux comme `mv`. Ces labs vous aideront à consolider votre compréhension du déplacement et du renommage de fichiers et de répertoires dans un environnement réel :

1. **[Commande Linux mv : déplacement et renommage de fichiers](https://labex.io/fr/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - Entraînez-vous à utiliser la commande `mv` pour déplacer et renommer des fichiers et des répertoires, en comprenant ses différentes options et comportements.
2. **[Organisation des fichiers et des répertoires](https://labex.io/fr/labs/linux-organizing-files-and-directories-387877)** - Appliquez vos connaissances de `mv` (ainsi que `cp` et `rm`) dans un défi pratique pour organiser une structure de projet, déplacer des fichiers et nettoyer des répertoires.

Ces labs vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance dans la gestion des fichiers et des répertoires avec la commande `mv`.

## Quiz Question

Avec la commande `mv`, comment renommeriez-vous un fichier nommé `cat` en `dog` ? Veuillez fournir la commande complète. Note : La réponse est sensible à la casse et doit être saisie en anglais minuscule.

## Quiz Answer

mv cat dog
