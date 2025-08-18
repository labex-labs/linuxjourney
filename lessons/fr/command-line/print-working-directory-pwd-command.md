---
index: 2
lang: "fr"
title: "pwd (Répertoire de travail actuel)"
meta_title: "pwd (Répertoire de travail actuel) - Command Line"
meta_description: "Apprenez à utiliser la commande 'pwd' sous Linux pour afficher votre répertoire de travail actuel. Comprenez les chemins du système de fichiers Linux et la navigation pour les débutants."
meta_keywords: "commande pwd, répertoire Linux, répertoire actuel, chemin Linux, tutoriel Linux, Linux débutant, guide Linux"
---

## Lesson Content

Tout dans Linux est un fichier. Au fur et à mesure que vous approfondirez Linux, vous comprendrez cela, mais pour l'instant, gardez cela à l'esprit. Chaque fichier est organisé dans une arborescence de répertoires hiérarchique. Le premier répertoire du système de fichiers est appelé à juste titre le répertoire racine. Le répertoire racine contient de nombreux dossiers et fichiers, qui peuvent stocker plus de dossiers et de fichiers, etc. Voici un exemple de ce à quoi ressemble l'arborescence des répertoires :

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

La navigation dans le système de fichiers, tout comme dans la vie réelle, est utile si vous savez où vous êtes et où vous allez. Pour savoir où vous êtes, vous pouvez utiliser la commande `pwd`. Cette commande signifie "print working directory" (afficher le répertoire de travail) et elle vous montre simplement dans quel répertoire vous vous trouvez. Notez que le chemin part du répertoire racine.

```bash
pwd
```

Où êtes-vous ? Où suis-je ? Essayez.

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Comment puis-je trouver le répertoire dans lequel vous vous trouvez actuellement ?

## Quiz Answer

pwd
