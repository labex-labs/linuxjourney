---
index: 13
lang: "fr"
title: "rm (Supprimer)"
meta_title: "rm (Supprimer) - Ligne de commande"
meta_description: "Apprenez la commande Linux rm avec des exemples sûrs pour supprimer des fichiers, enlever des répertoires, utiliser rm -r, rm -i, et éviter les erreurs avec rm -rf."
meta_keywords: "commande linux rm, commande rm, rm -r, rm -i, rm -f, rm -rf, supprimer fichiers linux, enlever répertoire linux, rmdir"
---

## Lesson Content

Sous Linux, il est courant d'accumuler des fichiers qui ne sont plus nécessaires. Pour les supprimer, vous utilisez la commande `rm` (remove), un utilitaire fondamental pour gérer votre système de fichiers. La syntaxe de base est :

```bash
rm [OPTIONS] FILE...
```

La commande `rm` supprime les entrées de répertoire du système de fichiers. En termes simples, elle supprime des fichiers. Contrairement à de nombreux environnements de bureau, la suppression en ligne de commande ne déplace généralement pas les fichiers dans une corbeille, donc vous devez vérifier votre commande avant d'appuyer sur Entrée.

### Supprimer un fichier unique

Pour supprimer un fichier, passez simplement son nom à `rm`.

```bash
$ rm file1
```

Vous pouvez supprimer plusieurs fichiers à la fois en les listant les uns après les autres.

```bash
$ rm notes.txt old-report.txt draft.md
```

Ceci est utile pour un nettoyage rapide, mais cela signifie aussi qu'une faute de frappe peut supprimer plus que prévu.

### Supprimer des fichiers avec des caractères génériques

Les caractères génériques du shell vous permettent de correspondre à plusieurs fichiers. Par exemple, ceci supprime tous les fichiers `.tmp` dans le répertoire courant :

```bash
$ rm *.tmp
```

Avant d'utiliser `rm` avec un caractère générique, il est plus sûr de prévisualiser la correspondance avec `ls`.

```bash
$ ls *.tmp
cache.tmp  test.tmp
$ rm *.tmp
```

Rappelez-vous que le shell développe `*.tmp` avant que `rm` ne s'exécute. Si le motif correspond à plus de fichiers que prévu, `rm` recevra tous ces fichiers.

### Suppression interactive avec -i

Pour une approche plus sûre, utilisez l'option `-i`. Elle vous demande confirmation avant de supprimer chaque fichier.

```bash
$ rm -i important.txt
rm: remove regular file 'important.txt'? y
```

Utilisez `rm -i` lorsque vous supprimez des fichiers dans un répertoire partagé, nettoyez beaucoup de fichiers, ou apprenez la commande pour la première fois.

### Suppression forcée avec -f

L'option `-f` signifie "force". Elle ignore les fichiers inexistants et ne demande pas de confirmation.

```bash
$ rm -f old-cache.txt
```

Ceci est utile dans les scripts où le nettoyage doit continuer même si un fichier a déjà été supprimé.

```bash
$ rm -f build.log
```

Soyez prudent : `-f` supprime aussi certaines invites de sécurité, ce qui peut masquer des erreurs.

### Supprimer des répertoires avec -r

Par défaut, `rm` ne peut pas supprimer un répertoire.

```bash
$ rm projects
rm: cannot remove 'projects': Is a directory
```

Pour supprimer un répertoire et tout ce qu'il contient, utilisez `-r` ou `-R` pour une suppression récursive.

```bash
$ rm -r old-project
```

La suppression récursive parcourt l'arborescence du répertoire et supprime fichiers, sous-répertoires et leur contenu.

### Les dangers de rm -rf

La commande `rm -rf` combine suppression récursive et suppression forcée.

```bash
$ rm -rf old-project
```

Cette commande peut être appropriée pour supprimer des dossiers générés comme des résultats de compilation, mais elle est dangereuse car elle supprime un arbre entier sans poser de questions. Vérifiez toujours :

- Êtes-vous dans le répertoire que vous pensez ? Utilisez `pwd`.
- Votre caractère générique s'est-il bien développé ? Prévisualisez avec `ls`.
- Le chemin est-il absolu ou relatif ? `/tmp/cache` et `tmp/cache` sont très différents.
- Y a-t-il un espace accidentel ? `rm -rf old-project` et `rm -rf old project` ciblent des chemins différents.

### Utiliser rmdir pour les répertoires vides

Comme alternative plus sûre, supprimez un répertoire vide avec `rmdir`.

```bash
$ rmdir empty-directory
```

La commande `rmdir` ne réussira que si le répertoire est complètement vide, ce qui en fait un choix plus sûr que `rm -r` pour les tâches de nettoyage.

### Options courantes de rm

Voici les options que vous verrez le plus souvent :

- `-i` : Demande confirmation avant chaque suppression.
- `-I` : Demande une fois avant de supprimer plus de trois fichiers ou de supprimer récursivement.
- `-f` : Force la suppression et ignore les fichiers inexistants.
- `-r` ou `-R` : Supprime récursivement les répertoires et leur contenu.
- `-v` : Affiche ce qui a été supprimé.

Par exemple, vous pouvez combiner les options :

```bash
$ rm -rv old-project
removed 'old-project/notes.txt'
removed directory 'old-project'
```

### Questions fréquentes

**Puis-je annuler rm ?** Habituellement, non. Une fois un fichier supprimé avec `rm`, il n'y a pas de commande intégrée pour annuler. Les sauvegardes, le contrôle de version et les outils de récupération de système de fichiers sont la vraie sécurité.

**Pourquoi rm affiche-t-il "Permission denied" ?** Vous n'avez pas la permission de supprimer ce fichier ou de modifier le répertoire qui le contient. Vérifiez la propriété et les permissions avec `ls -l`.

**Pourquoi rm affiche-t-il "No such file or directory" ?** Le fichier n'existe pas à ce chemin, ou vous êtes dans un répertoire différent de celui attendu. Utilisez `pwd` et `ls` pour confirmer.

**Dois-je utiliser sudo avec rm ?** Seulement lorsque vous comprenez parfaitement le chemin que vous supprimez. `sudo rm -r` peut supprimer des fichiers système que votre compte utilisateur normal n'a pas le droit de toucher.

## Exercise

La pratique est essentielle. Voici quelques exercices pratiques pour renforcer votre compréhension de la suppression de fichiers et répertoires sous Linux :

1. **[Commande Linux rm : Suppression de fichiers](https://labex.io/fr/labs/linux-linux-rm-command-file-removing-209741)** - Apprenez à utiliser la commande `rm` pour supprimer fichiers et répertoires, y compris diverses options comme `-r` et `-i`, et exercez-vous à une suppression sûre et efficace.
2. **[Organisation des fichiers et répertoires](https://labex.io/fr/labs/linux-organizing-files-and-directories-387877)** - Pratiquez les compétences essentielles de gestion de fichiers Linux, y compris l'utilisation de la commande `rm` pour nettoyer des répertoires inutiles, dans un défi pratique.

Ces laboratoires vous aideront à appliquer ces concepts dans des scénarios réels et à gagner en confiance avec la commande `linux rm command`.

## Quiz Question

How do you remove a file named `myfile`? Your answer must be in English and use the exact, case-sensitive command.

## Quiz Answer

rm myfile
