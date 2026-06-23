---
index: 2
lang: "fr"
title: "pwd (Afficher le répertoire de travail)"
meta_title: "pwd (Afficher le répertoire de travail) - Ligne de commande"
meta_description: "Apprenez la commande Linux pwd, ce que signifie afficher le répertoire de travail, et comment les chemins absolus montrent votre emplacement actuel dans le système de fichiers."
meta_keywords: "commande pwd, linux pwd, afficher répertoire de travail, répertoire courant linux, chemin absolu, système de fichiers linux, arbre des répertoires"
---

## Lesson Content

Sous Linux, les fichiers et répertoires sont organisés en une hiérarchie appelée système de fichiers. Avant de pouvoir vous déplacer en toute confiance, vous devez savoir où vous vous trouvez. La commande `pwd` répond à cette question en affichant votre répertoire de travail actuel.

### L'arborescence des répertoires sous Linux

L'ensemble du système de fichiers commence à partir d'un seul répertoire de niveau supérieur appelé répertoire racine, représenté par une barre oblique (`/`). À partir de la racine, l'arborescence des répertoires se ramifie en sous-répertoires, qui peuvent contenir des fichiers et d'autres sous-répertoires.

Voici un exemple simplifié de ce à quoi cette structure ressemble :

```plaintext
/
|-- bin
|   |-- file1
|   |-- file2
|-- etc
|   |-- file3
|   `-- directory1
|       |-- file4
|       `-- file5
|-- home
|-- var
```

### Comprendre les chemins de fichiers

L'emplacement de n'importe quel fichier ou répertoire est décrit par son chemin. Un chemin est une séquence de répertoires qui mène d'un point de départ à une destination spécifique.

Par exemple, si vous avez un dossier nommé `pete` dans `/home`, et un dossier `Movies` à l'intérieur de `pete`, le chemin complet est :

```plaintext
/home/pete/Movies
```

Un chemin qui commence par `/` est un chemin absolu car il commence au répertoire racine. Un chemin tel que `Movies` est relatif car il dépend de votre emplacement actuel.

### Quelle est la signification complète de PWD sous Linux ?

La signification complète de `pwd` est "print working directory" (afficher le répertoire de travail). Votre répertoire de travail est le répertoire où votre shell se trouve actuellement. Les commandes qui utilisent des chemins relatifs partent de cet emplacement.

### Utiliser la commande pwd

Pour connaître votre répertoire actuel, tapez `pwd` puis appuyez sur Entrée.

```bash
$ pwd
/home/pete
```

La sortie est un chemin absolu. Dans cet exemple, le shell se trouve actuellement dans le répertoire personnel de l'utilisateur `pete`.

### Pourquoi pwd est utile

Utilisez `pwd` lorsque :

- Vous suivez des instructions et devez confirmer votre emplacement.
- Une commande a échoué parce qu'un chemin de fichier était incorrect.
- Vous avez navigué à travers plusieurs répertoires et avez perdu la trace de votre position.
- Vous souhaitez copier le chemin du répertoire actuel dans une autre commande.

Par exemple :

```bash
$ pwd
/home/pete/projects
$ ls
app.py  README.md
```

Cela vous indique que `app.py` et `README.md` se trouvent dans `/home/pete/projects`.

### Questions courantes

**Est-ce que pwd modifie quelque chose ?** Non. `pwd` affiche uniquement des informations.

**Pourquoi la sortie est-elle différente sur mon système ?** Votre nom d'utilisateur, répertoire personnel et emplacement actuel peuvent être différents.

**Quelle est la différence entre pwd et cd ?** `pwd` montre où vous êtes. `cd` change votre emplacement.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la navigation dans le système de fichiers Linux et l'identification de votre emplacement actuel :

1. **[Commande Linux pwd : affichage du répertoire](https://labex.io/fr/labs/linux-linux-pwd-command-directory-displaying-209734)** - Ce laboratoire offre un aperçu ciblé et une utilisation pratique de la commande `pwd`, en lien direct avec l'introduction de la leçon sur la localisation de votre répertoire actuel.
2. **[Navigation dans les répertoires Linux](https://labex.io/fr/labs/linux-directory-navigation-387844)** - Mettez vos compétences de base en ligne de commande Linux à l'épreuve en naviguant à travers divers répertoires, consolidant votre compréhension des chemins et de la structure du système de fichiers.
3. **[Commande Linux cd : changement de répertoire](https://labex.io/fr/labs/linux-linux-cd-command-directory-changing-209733)** - Apprenez à naviguer efficacement dans votre système de fichiers en utilisant la commande `cd`, en comprenant différentes techniques pour changer de répertoire et explorer la structure des fichiers.

Ces laboratoires vous aideront à appliquer les concepts de hiérarchie et de navigation dans le système de fichiers dans des scénarios réels et à gagner en confiance avec les commandes Linux essentielles.

## Quiz Question

Quelle commande est utilisée pour trouver le répertoire dans lequel vous vous trouvez actuellement ? (Veuillez répondre en anglais, en utilisant uniquement le nom de la commande en minuscules.)

## Quiz Answer

pwd
