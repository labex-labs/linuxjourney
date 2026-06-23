---
index: 9
lang: "fr"
title: "history"
meta_title: "history - Ligne de commande"
meta_description: "Apprenez la commande history sous Linux avec des exemples pour afficher l'historique des commandes, relancer des commandes, recherche inversée, suppression d'entrées et nettoyage du terminal."
meta_keywords: "commande linux history, historique bash, history -c, history -d, history -w, Ctrl-R, historique des commandes, commande clear"
---

## Lesson Content

Votre shell conserve un enregistrement des commandes que vous avez précédemment saisies. Vous pouvez accéder à cette liste lorsque vous souhaitez retrouver et réutiliser une commande sans la retaper. La commande `history` est un outil fondamental dans Bash et de nombreux environnements shell de type Unix.

### Afficher votre historique de commandes

Pour voir la liste des commandes que vous avez utilisées, tapez `history`.

```bash
$ history
  101  pwd
  102  ls -la
  103  cat notes.txt
```

Chaque ligne comporte un numéro d'historique suivi de la commande.

### Relancer des commandes précédentes

Le shell propose plusieurs raccourcis pour faciliter la relance des commandes.

- **Flèche vers le haut** : Vous voulez exécuter la même commande que celle que vous venez de faire ? Il suffit d'appuyer sur la touche flèche vers le haut pour parcourir votre historique vers l'arrière.
- **Le raccourci `!!`** : Pour exécuter à nouveau la commande la plus récente, vous pouvez utiliser `!!`. Par exemple, si vous venez d'exécuter `cat file1`, taper `!!` puis appuyer sur Entrée exécutera à nouveau `cat file1`.
- **Exécuter par numéro** : Utilisez `!102` pour exécuter la commande numéro 102 de votre historique.
- **Exécuter par préfixe** : Utilisez `!cat` pour exécuter la commande la plus récente qui commence par `cat`.

### Rechercher dans votre historique

Un des raccourcis d'historique les plus puissants est `Ctrl-R`. Cela lance une recherche inversée. Après avoir appuyé sur `Ctrl-R`, commencez à taper une partie de la commande que vous cherchez, et le shell affichera la correspondance la plus récente. Vous pouvez appuyer plusieurs fois sur `Ctrl-R` pour parcourir les correspondances plus anciennes. Une fois que vous avez trouvé la commande souhaitée, appuyez simplement sur Entrée pour l'exécuter.

Si vous souhaitez modifier la commande trouvée avant de l'exécuter, appuyez sur la touche flèche droite ou flèche gauche au lieu d'Entrée.

### Gérer la liste d'historique

Au-delà de simplement afficher votre historique, vous pouvez aussi le gérer directement.

- **Effacer la liste d'historique en mémoire** : `history -c` supprime toutes les entrées de la liste d'historique en mémoire.
- **Écrire l'historique dans un fichier** : `history -w` enregistre l'historique de la session courante dans votre fichier d'historique, généralement `~/.bash_history`.
- **Supprimer une entrée spécifique** : `history -d <offset>` supprime une commande par son numéro d'historique.

Exemples :

```bash
$ history -d 101
$ history -w
```

Soyez prudent avec les commandes d'expansion d'historique telles que `!!` et `!102`. Utilisez d'abord `history` pour confirmer ce qui sera exécuté.

### Autres outils utiles du terminal

Au fur et à mesure que votre fenêtre de terminal se remplit, vous pourriez vouloir la nettoyer. Utilisez la commande `clear` pour effacer votre affichage et repartir sur un écran vierge.

```bash
$ clear
```

Une autre fonctionnalité indispensable est la complétion par tabulation. Si vous commencez à taper le début d'une commande, d'un nom de fichier ou d'un répertoire et appuyez sur la touche Tab, le shell tentera de l'autocompléter. S'il y a plusieurs possibilités, il peut vous montrer les options ou ne rien faire. Appuyer une deuxième fois sur Tab affichera souvent toutes les complétions possibles.

### Questions fréquentes

**Où est stocké l'historique Bash ?** Généralement dans `~/.bash_history`, bien que le comportement exact dépende des paramètres du shell.

**L'historique inclut-il chaque commande immédiatement ?** Pas toujours. Certains shells écrivent l'historique à la fermeture de la session sauf configuration contraire.

**L'historique peut-il contenir des données sensibles ?** Oui. Évitez de taper des mots de passe, jetons ou secrets directement dans les commandes.

**Quelle est la différence entre history -c et clear ?** `history -c` efface l'historique des commandes en mémoire. `clear` ne fait qu'effacer l'écran du terminal.

## Exercise

Bien qu'il n'y ait pas de laboratoires spécifiques pour ce sujet, nous recommandons d'explorer le [Parcours d'apprentissage Linux](https://labex.io/fr/learn/linux) complet pour pratiquer les compétences et concepts Linux associés.

## Quiz Question

Quelle est la commande pour nettoyer le terminal ? (Veuillez répondre uniquement en lettres minuscules anglaises)

## Quiz Answer

clear
