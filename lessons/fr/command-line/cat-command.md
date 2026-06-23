---
index: 7
lang: "fr"
title: "cat"
meta_title: "cat - Ligne de commande"
meta_description: "Apprenez la commande Linux cat avec des exemples pour afficher des fichiers, concaténer des fichiers, numéroter les lignes, créer des fichiers et utiliser la redirection en toute sécurité."
meta_keywords: "commande linux cat, commande cat, afficher fichier linux, concaténer fichiers, cat -n, cat -b, redirection cat, linux cat"
---

## Lesson Content

Après avoir appris à naviguer dans le système de fichiers, l'étape suivante est de visualiser le contenu des fichiers. Un outil fondamental et polyvalent pour cela est la commande `cat`. Le nom `cat` est l'abréviation de "concatenate" (concaténer), ce qui indique sa capacité à relier des fichiers ensemble.

### Affichage du contenu d'un fichier

L'utilisation la plus basique de la commande `cat` est d'afficher le contenu d'un seul fichier directement dans votre terminal.

```bash
$ cat myfile.txt
```

Cette commande affichera tout le contenu de `myfile.txt` à l'écran. Bien que cela soit parfait pour des fichiers de configuration courts ou des extraits de texte, ce n'est pas idéal pour visualiser de gros fichiers, car le texte défilera très rapidement. Nous aborderons des outils mieux adaptés aux gros fichiers dans une leçon ultérieure.

### Concaténation de fichiers

Fidèle à son nom, `cat` peut combiner, ou concaténer, plusieurs fichiers et afficher leur sortie combinée. Il lit les fichiers dans l'ordre où ils sont fournis et les affiche séquentiellement.

```bash
$ cat dogfile birdfile
```

Cette commande affichera d'abord le contenu de `dogfile`, immédiatement suivi du contenu de `birdfile`.

Pour enregistrer la sortie combinée dans un nouveau fichier, utilisez la redirection :

```bash
$ cat dogfile birdfile > animals
```

### Création de fichiers avec la redirection

Vous pouvez également utiliser `cat` avec l'opérateur de redirection de sortie (`>`) pour créer de nouveaux fichiers. C'est un moyen rapide d'écrire du texte dans un fichier directement depuis votre terminal.

```bash
$ cat > newfile.txt
```

Après avoir exécuté cette commande, vous pouvez taper votre texte. Appuyez sur `Ctrl+D` sur une nouvelle ligne pour enregistrer et quitter. Cela créera `newfile.txt` avec le texte que vous avez saisi. Faites attention, car utiliser `>` sur un fichier existant le remplacera complètement.

Pour ajouter du texte à un fichier au lieu de l'écraser, utilisez `>>`.

```bash
$ cat >> notes.txt
```

### Options courantes de la commande cat

La commande `cat` dispose de plusieurs options pour modifier son comportement.

- `-n` : Numérote toutes les lignes de sortie, en commençant à 1.
- `-b` : Numérote uniquement les lignes non vides.
- `-s` : Compresse plusieurs lignes vides en une seule ligne vide.
- `-A` : Affiche les caractères non imprimables, les tabulations et les fins de ligne.

Exemples :

```bash
$ cat -n script.sh
$ cat -b notes.txt
$ cat -s messy.txt
```

### Quand ne pas utiliser cat

Utilisez `cat` pour les fichiers courts. Pour les fichiers longs, utilisez `less` afin de pouvoir faire défiler, rechercher et quitter sans inonder votre terminal.

```bash
$ less /var/log/syslog
```

### Questions fréquentes

**Que signifie cat ?** Cela signifie concaténer.

**Est-ce que cat peut éditer un fichier ?** Pas de manière interactive. Il peut créer ou écraser des fichiers avec la redirection, mais un éditeur de texte est préférable pour l'édition.

**Quelle est la différence entre > et >> ?** `>` écrase un fichier. `>>` ajoute à la fin d'un fichier.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'affichage du contenu des fichiers :

1. **[Commande Linux cat : concaténation de fichiers](https://labex.io/fr/labs/linux-linux-cat-command-file-concatenating-210986)** - Apprenez la commande `cat` pour afficher, concaténer et manipuler des fichiers texte, améliorant vos compétences en ligne de commande pour une gestion efficace des fichiers texte.
2. **[Visualisation des fichiers journaux et de configuration sous Linux](https://labex.io/fr/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Entraînez-vous à utiliser des commandes comme `cat` pour visualiser et naviguer efficacement dans des fichiers texte, y compris les journaux système et les fichiers de configuration, afin d'extraire des informations critiques.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance pour la visualisation du contenu des fichiers sous Linux.

## Quiz Question

Quelle commande est utilisée pour afficher le contenu d'un fichier en ligne de commande ? (Remarque : votre réponse doit être un seul mot en anglais, en minuscules.)

## Quiz Answer

cat
