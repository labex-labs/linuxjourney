---
index: 10
lang: "fr"
title: "cp (Copier)"
meta_title: "cp (Copier) - Ligne de commande"
meta_description: "Apprenez la commande Linux cp avec des exemples pour copier des fichiers, des répertoires, plusieurs fichiers, des jokers, des sauvegardes et des options comme cp -r, cp -i et cp -p."
meta_keywords: "commande linux cp, commande cp, copier fichiers linux, cp -r, cp -i, cp -p, cp -a, cp -u, copie récursive, jokers linux"
---

## Lesson Content

La commande `cp` est l'outil standard pour copier des fichiers et des répertoires sous Linux. Elle crée une nouvelle copie tout en laissant le fichier original en place. Sa syntaxe de base est :

```bash
cp [OPTIONS] SOURCE DESTINATION
```

Vous pouvez copier un fichier vers un autre fichier, un ou plusieurs fichiers dans un répertoire, ou un arbre de répertoires entier avec la bonne option.

### Copie de fichiers basique

Pour copier un fichier, vous spécifiez le fichier source et le répertoire ou chemin de destination.

```bash
$ cp mycoolfile /home/pete/Documents/cooldocs
```

Dans cet exemple, `mycoolfile` est le fichier source, et `/home/pete/Documents/cooldocs` est le répertoire de destination. Vous pouvez aussi copier un fichier et lui donner un nouveau nom dans la destination.

```bash
$ cp mycoolfile /home/pete/Documents/mycoolfile_backup
```

Si la destination est un répertoire existant, le fichier copié garde son nom d'origine. Si la destination est un nom de fichier, `cp` crée une copie avec ce nouveau nom.

### Copier plusieurs fichiers dans un répertoire

Pour copier plusieurs fichiers dans le même répertoire, listez d'abord toutes les sources et mettez le répertoire de destination en dernier.

```bash
$ cp report.txt notes.txt summary.txt /home/pete/Documents/
```

Le dernier argument doit être un répertoire lorsque vous fournissez plus d'une source.

### Utiliser les jokers pour une copie en masse

Les jokers sont des caractères spéciaux qui vous aident à sélectionner plusieurs fichiers selon des motifs, offrant une grande flexibilité.

- `*` : Correspond à n'importe quelle séquence de caractères.
- `?` : Correspond à un seul caractère.
- `[]` : Correspond à un des caractères entre crochets.

Par exemple, pour copier toutes les images JPEG de votre emplacement actuel vers le répertoire `Pictures` :

```bash
$ cp *.jpg /home/pete/Pictures
```

Vous pouvez prévisualiser les fichiers correspondants avant de copier :

```bash
$ ls *.jpg
beach.jpg  lunch.jpg  profile.jpg
$ cp *.jpg /home/pete/Pictures
```

### Copier des répertoires récursivement

Si vous essayez de copier un répertoire avec `cp` sans option, vous recevrez une erreur. Pour copier un répertoire et tout son contenu, y compris les sous-répertoires, vous devez utiliser l'option `-r` (récursive).

```bash
$ cp -r Pumpkin/ /home/pete/Documents
```

Cette commande copie le répertoire `Pumpkin` et tout ce qu'il contient dans votre répertoire `Documents`.

Vous pouvez aussi voir `-R`, qui a la même fonction récursive sur les systèmes Linux typiques :

```bash
$ cp -R website /home/pete/backups/
```

### Gérer les écrasements de fichiers

Par défaut, `cp` écrase un fichier à la destination s'il porte le même nom. Pour éviter une perte de données accidentelle, utilisez l'option `-i` (interactive), qui demande une confirmation avant d'écraser.

```bash
$ cp -i mycoolfile /home/pete/Pictures
cp: overwrite '/home/pete/Pictures/mycoolfile'? n
```

Inversement, si vous voulez forcer l'écrasement sans demande, utilisez l'option `-f`. Cela est utile dans les scripts où l'interaction utilisateur n'est pas possible.

```bash
$ cp -f mycoolfile /home/pete/Pictures
```

Une autre option de sécurité utile est `-n`, qui signifie "ne pas écraser". Elle empêche d'écraser un fichier de destination existant.

```bash
$ cp -n mycoolfile /home/pete/Pictures
```

### Préserver les attributs de fichier avec -p

Lorsque vous copiez un fichier, ses métadonnées, comme la date de modification et la propriété, sont généralement mises à jour. Pour préserver ces attributs originaux, utilisez l'option `-p`.

L'option `cp -p` est particulièrement utile pour les sauvegardes ou lors de la migration de fichiers où la conservation des horodatages est importante.

```bash
$ cp -p mycoolfile /home/pete/backups/
```

Cela copie `mycoolfile` tout en préservant son mode, sa propriété lorsque c'est possible, et ses horodatages.

### Copies d'archives avec -a

L'option `-a` signifie archive. Elle est couramment utilisée pour des copies de répertoires de type sauvegarde car elle préserve de nombreux attributs et copie récursivement.

```bash
$ cp -a project/ project-backup/
```

Pour beaucoup de sauvegardes quotidiennes, `cp -a` est plus pratique que de combiner plusieurs options manuellement.

### Copier uniquement les fichiers plus récents avec -u

L'option `-u` copie uniquement lorsque le fichier source est plus récent que le fichier de destination ou lorsque le fichier de destination n'existe pas.

```bash
$ cp -u *.txt /home/pete/Documents/
```

Cela est utile pour actualiser un dossier sans réécrire les fichiers déjà à jour.

### Options courantes de cp

Voici les options que vous utiliserez le plus souvent :

- `-r` ou `-R` : Copier les répertoires récursivement.
- `-i` : Demander avant d'écraser un fichier.
- `-f` : Forcer l'écrasement en supprimant d'abord la destination si nécessaire.
- `-n` : Ne pas écraser les fichiers existants.
- `-p` : Préserver le mode, la propriété lorsque possible, et les horodatages.
- `-a` : Mode archive, utile pour préserver les arbres de répertoires.
- `-u` : Copier uniquement lorsque la source est plus récente que la destination.
- `-v` : Afficher chaque fichier au fur et à mesure de la copie.

### Questions fréquentes

**Pourquoi cp a-t-il écrasé mon fichier ?** Par défaut, `cp` remplace un fichier de destination portant le même nom. Utilisez `cp -i` pour demander avant ou `cp -n` pour éviter l'écrasement.

**Pourquoi cp ne peut-il pas copier un répertoire ?** Un répertoire nécessite une copie récursive. Utilisez `cp -r source-dir destination-dir`.

**Quelle est la différence entre cp et mv ?** `cp` crée une copie et conserve l'original. `mv` déplace ou renomme l'original.

**Dois-je utiliser cp -r ou cp -a pour les sauvegardes ?** Utilisez `cp -r` pour une copie récursive simple. Utilisez `cp -a` lorsque vous voulez une copie de type sauvegarde qui préserve plus d'attributs de fichier.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la copie de fichiers et de répertoires sous Linux :

1. **[Commande Linux cp : Copier des fichiers](https://labex.io/fr/labs/linux-linux-cp-command-file-copying-209744)** - Pratiquez l'utilisation basique, les options avancées comme la copie récursive, la préservation des attributs, et l'utilisation des jokers pour copier efficacement fichiers et répertoires.
2. **[Organisation des fichiers et répertoires](https://labex.io/fr/labs/linux-organizing-files-and-directories-387877)** - Pratiquez les compétences essentielles de gestion de fichiers Linux en utilisant les commandes `cp`, `mv` et `rm` pour organiser une structure de projet, déplacer des fichiers et nettoyer des répertoires inutiles.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance avec la copie et la gestion des fichiers sous Linux.

## Quiz Question

Quelle option devez-vous spécifier pour copier un répertoire ?

## Quiz Answer

-r
