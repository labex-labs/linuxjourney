---
index: 2
lang: "fr"
title: "pwd (Print Working Directory)"
meta_title: "pwd (Print Working Directory) - Ligne de commande"
meta_description: "Apprenez à utiliser la commande 'pwd' sous Linux pour afficher votre répertoire de travail actuel. Comprenez les chemins du système de fichiers Linux et la navigation pour les débutants."
meta_keywords: "commande pwd, répertoire Linux, répertoire actuel, chemin Linux, tutoriel Linux, Linux débutant, guide Linux"
---

## Lesson Content

Tout dans Linux est un fichier. En approfondissant Linux, vous comprendrez cela, mais pour l'instant, gardez cela à l'esprit. Chaque fichier est organisé dans une arborescence de répertoires hiérarchique. Le premier répertoire du système de fichiers est nommé à juste titre le répertoire racine. Le répertoire racine contient de nombreux dossiers et fichiers, qui peuvent stocker d'autres dossiers et fichiers, etc. Voici un exemple de ce à quoi ressemble l'arborescence des répertoires :

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

La navigation dans le système de fichiers, tout comme dans la vie réelle, est utile si vous savez où vous êtes et où vous allez. Pour savoir où vous êtes, vous pouvez utiliser la commande `pwd`. Cette commande signifie "print working directory" (afficher le répertoire de travail) et elle vous indique simplement dans quel répertoire vous vous trouvez. Notez que le chemin part du répertoire racine.

```bash
pwd
```

Où êtes-vous ? Où suis-je ? Essayez.

## Exercise

Pour une pratique concrète de la commande `pwd`, essayez ce laboratoire interactif :

- [Linux pwd Command: Directory Displaying](https://labex.io/fr/labs/linux-linux-pwd-command-directory-displaying-209734)

## Quiz Question

Comment puis-je trouver le répertoire dans lequel je me trouve actuellement ?

## Quiz Answer

pwd
