---
lang: "fr"
title: "Modèles de recherche Vim"
meta_description: "Apprenez les modèles de recherche Vim : recherche avant (/) et arrière (?). Naviguez dans les résultats avec 'n' et 'N'. Améliorez vos compétences Vim dès aujourd'hui !"
meta_keywords: "recherche Vim, commandes Vim, éditeur de texte Linux, tutoriel Vim, guide Vim, Vim pour débutants"
---

## Lesson Content

Pour rechercher une expression, il suffit de taper la touche `/` puis votre terme de recherche lorsque vous êtes dans une session Vim. Une fois que vous avez appuyé sur Entrée, vous pouvez appuyer sur `n` pour avancer ou sur `N` pour reculer dans vos résultats de recherche.

```plaintext
My pretty file is very pretty.

/pretty

will find the pretty words in the text file.
```

La commande de recherche `?` recherchera le fichier texte à l'envers. Ainsi, dans l'exemple précédent, le dernier "pretty" apparaîtrait en premier.

```plaintext
My pretty file is very pretty.

?pretty

will find the pretty words in the text file.
```

## Exercise

Jouez avec la touche de recherche. Ouvrez un fichier texte dans Vim avec : `vim [textfile]` et commencez à chercher !

## Quiz Question

Quelle touche est utilisée pour rechercher dans Vim ?

## Quiz Answer

/
