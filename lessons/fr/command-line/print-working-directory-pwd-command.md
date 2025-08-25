---
index: 2
lang: "fr"
title: "pwd (Print Working Directory)"
meta_title: "pwd (Print Working Directory) - Ligne de commande"
meta_description: "Apprenez à utiliser la commande 'pwd' sous Linux pour afficher votre répertoire de travail actuel. Comprenez les chemins du système de fichiers Linux et la navigation pour les débutants."
meta_keywords: "commande pwd, répertoire Linux, répertoire actuel, chemin Linux, tutoriel Linux, Linux débutant, guide Linux"
---

## Lesson Content

Tout dans Linux est un fichier. En approfondissant Linux, vous comprendrez cela, mais pour l'instant, gardez cela à l'esprit. Chaque fichier est organisé dans une arborescence de répertoires hiérarchique. Le premier répertoire du système de fichiers est judicieusement nommé le répertoire racine. Le répertoire racine contient de nombreux dossiers et fichiers, qui peuvent stocker plus de dossiers et de fichiers, etc. Voici un exemple de ce à quoi ressemble l'arborescence des répertoires :

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

L'emplacement de ces fichiers et répertoires est appelé chemins. Si vous aviez un dossier nommé `home` avec un dossier à l'intérieur nommé `pete` et un autre dossier dans ce dossier appelé `Movies`, ce chemin ressemblerait à ceci : `/home/pete/Movies`. Plutôt simple, n'est-ce pas ?

La navigation dans le système de fichiers, tout comme dans la vie réelle, est utile si vous savez où vous êtes et où vous allez. Pour voir où vous êtes, vous pouvez utiliser la commande `pwd`. Cette commande signifie "print working directory" (afficher le répertoire de travail) et elle vous montre simplement dans quel répertoire vous vous trouvez. Notez que le chemin part du répertoire racine.

```bash
pwd
```

Où êtes-vous ? Où suis-je ? Essayez.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la navigation dans le système de fichiers Linux et l'identification de votre emplacement actuel :

1. **[Commande Linux pwd : Affichage du répertoire](https://labex.io/fr/labs/linux-linux-pwd-command-directory-displaying-209734)** - Ce laboratoire offre un aperçu ciblé et une utilisation pratique de la commande `pwd`, s'alignant directement avec l'introduction de la leçon sur la recherche de votre répertoire actuel.
2. **[Navigation dans les répertoires Linux](https://labex.io/fr/labs/linux-directory-navigation-387844)** - Mettez à l'épreuve vos compétences de base en ligne de commande Linux en naviguant à travers divers répertoires, consolidant ainsi votre compréhension des chemins et de la structure du système de fichiers.
3. **[Commande Linux cd : Changement de répertoire](https://labex.io/fr/labs/linux-linux-cd-command-directory-changing-209733)** - Apprenez à naviguer efficacement dans votre système de fichiers à l'aide de la commande `cd`, en comprenant les différentes techniques pour changer de répertoire et explorer la structure des fichiers.

Ces laboratoires vous aideront à appliquer les concepts de hiérarchie et de navigation du système de fichiers dans des scénarios réels et à renforcer votre confiance avec les commandes Linux essentielles.

## Quiz Question

Comment puis-je savoir dans quel répertoire je me trouve actuellement ?

## Quiz Answer

pwd
