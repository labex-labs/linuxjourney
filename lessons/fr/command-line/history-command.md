---
index: 9
lang: "fr"
title: "historique"
meta_title: "historique - Ligne de commande"
meta_description: "Maîtrisez la commande history sous Linux pour rappeler et gérer efficacement votre activité sur la ligne de commande. Apprenez à visualiser l'historique, à utiliser des raccourcis comme Ctrl-R, et à gérer votre historique avec des options telles que history -c et history -d."
meta_keywords: "historique linux, history -c linux, history -d linux, history -w linux, commande history unix, historique bash, ligne de commande, Ctrl-R, effacer commande"
---

## Lesson Content

Votre shell conserve un enregistrement des commandes que vous avez précédemment saisies. Vous pouvez accéder à cette liste, ce qui est incroyablement utile lorsque vous souhaitez retrouver et réutiliser une commande sans avoir à la retaper. La commande `history` est un outil fondamental dans la plupart des environnements Unix et Linux.

### Afficher l'historique de vos commandes

Pour voir la liste des commandes que vous avez utilisées, tapez simplement la commande `history`. Cette fonctionnalité fournit un journal détaillé de votre activité, ce qui facilite le suivi de votre `history in linux`.

```bash
history
```

### Réexécuter les commandes précédentes

Le shell fournit plusieurs raccourcis pour faciliter la réexécution des commandes.

- **Flèche Haut** : Vous voulez exécuter la même commande que vous venez de faire ? Appuyez simplement sur la flèche haut pour parcourir l'historique à l'envers.
- **Le raccourci `!!`** : Pour réexécuter la commande la plus récente, vous pouvez utiliser `!!`. Par exemple, si vous venez d'exécuter `cat file1`, taper `!!` et appuyer sur Entrée exécutera à nouveau `cat file1`.

### Rechercher dans votre historique

L'un des raccourcis d'historique les plus puissants est `Ctrl-R`. Cela lance une recherche inversée. Après avoir appuyé sur `Ctrl-R`, commencez à taper n'importe quelle partie de la commande que vous recherchez, et le shell affichera la correspondance la plus récente. Vous pouvez appuyer sur `Ctrl-R` de manière répétée pour parcourir les correspondances plus anciennes. Une fois que vous avez trouvé la commande souhaitée, appuyez simplement sur Entrée pour l'exécuter.

### Gérer la liste d'historique

Au-delà de la simple visualisation de votre historique, vous pouvez également le gérer directement.

- **Effacer l'historique** : Si vous souhaitez effacer l'historique des commandes pour votre session actuelle, vous pouvez utiliser la commande `history -c linux`. Cela supprime toutes les entrées de la liste d'historique en mémoire.
- **Écrire dans un fichier** : Pour sauvegarder l'historique de la session en cours dans votre fichier d'historique (généralement `~/.bash_history`), vous pouvez utiliser `history -w linux`. Ceci est utile pour conserver les commandes avant de fermer une session.
- **Supprimer une entrée spécifique** : Vous pouvez supprimer une seule commande de votre historique en utilisant `history -d <offset>`. Le décalage est le numéro affiché à côté de la commande dans la sortie `history`. Par exemple, `history -d 101` supprimerait la 101e entrée. C'est une fonction clé de `history -d linux`.

### Autres outils de terminal utiles

À mesure que votre fenêtre de terminal se remplit, vous voudrez peut-être la nettoyer. Utilisez la commande `clear` pour effacer votre affichage et commencer avec un écran vierge.

```bash
clear
```

Une autre fonctionnalité indispensable est la complétion par tabulation. Si vous commencez à taper le début d'une commande, d'un nom de fichier ou d'un répertoire et que vous appuyez sur la touche Tab, le shell tentera de le compléter automatiquement. S'il y a plusieurs possibilités, il pourra vous montrer les options ou ne rien faire. Appuyer sur Tab une seconde fois listera souvent toutes les complétions possibles.

## Exercise

Bien qu'il n'y ait pas de laboratoires spécifiques pour ce sujet, nous vous recommandons d'explorer le [Parcours d'apprentissage Linux](https://labex.io/fr/learn/linux) complet pour pratiquer les compétences et concepts Linux associés.

## Quiz Question

Quelle est la commande pour effacer le terminal ? (Veuillez répondre uniquement en lettres anglaises minuscules)

## Quiz Answer

clear
