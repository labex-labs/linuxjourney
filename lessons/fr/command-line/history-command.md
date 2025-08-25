---
index: 9
lang: "fr"
title: "history"
meta_title: "history - Ligne de commande"
meta_description: "Apprenez à utiliser la commande Linux history, le raccourci !! et Ctrl-R pour un rappel efficace des commandes. Améliorez votre productivité dans le terminal avec ces astuces essentielles !"
meta_keywords: "historique Linux, historique bash, Ctrl-R, commande clear, tutoriel Linux, ligne de commande, guide du débutant"
---

## Lesson Content

Dans votre shell, il y a un historique des commandes que vous avez précédemment saisies. Vous pouvez en fait parcourir ces commandes. C'est très utile lorsque vous voulez trouver et exécuter une commande que vous avez utilisée précédemment sans avoir à la retaper.

```bash
history
```

Vous voulez exécuter la même commande que vous avez utilisée précédemment ? Appuyez simplement sur la flèche vers le haut.

Vous voulez exécuter la commande précédente sans la retaper ? Utilisez `!!`. Si vous avez tapé `cat file1` et que vous voulez l'exécuter à nouveau, vous pouvez simplement taper `!!` et cela exécutera la dernière commande que vous avez lancée.

Un autre raccourci d'historique est `Ctrl-R`. C'est la commande de recherche inversée. Si vous appuyez sur `Ctrl-R` et commencez à taper des parties de la commande que vous voulez, elle vous montrera les correspondances. Vous pouvez naviguer à travers elles en appuyant à nouveau sur la touche `Ctrl-R`. Une fois que vous avez trouvé la commande que vous voulez utiliser à nouveau, appuyez simplement sur la touche Entrée.

Notre terminal est un peu encombré, n'est-ce pas ? Faisons un petit nettoyage. Utilisez la commande `clear` pour effacer votre affichage.

```bash
clear
```

Voilà, ça a l'air mieux, n'est-ce pas ?

Pendant que nous parlons de choses utiles, l'une des fonctionnalités les plus utiles dans n'importe quel environnement de ligne de commande est la complétion par tabulation. Si vous commencez à taper le début d'une commande, d'un fichier, d'un répertoire, etc., et que vous appuyez sur la touche Tab, cela complétera automatiquement en fonction de ce qu'il trouve dans le répertoire où vous cherchez, tant que vous n'avez pas d'autres fichiers qui commencent par ces lettres. Par exemple, si vous essayiez d'exécuter la commande `chrome`, vous pouvez taper `chr` et appuyer sur Tab, et cela complétera en `chrome`.

## Exercise

Bien qu'il n'y ait pas de laboratoires spécifiques pour ce sujet, nous vous recommandons d'explorer le [Parcours d'apprentissage Linux](https://labex.io/fr/learn/linux) complet pour pratiquer les compétences et concepts Linux connexes.

## Quiz Question

Quelle est la commande pour effacer le terminal ?

## Quiz Answer

clear
