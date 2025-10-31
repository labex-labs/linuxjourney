---
index: 8
lang: "fr"
title: "less"
meta_title: "less - Ligne de Commande"
meta_description: "Maîtrisez la commande Linux less pour visualiser efficacement les fichiers texte. Ce guide couvre comment utiliser la commande less, naviguer, effectuer une recherche unix less, et comment quitter less."
meta_keywords: "commande less, less commande, quitter less, recherche unix less, linux less, visualiser fichiers texte, naviguer fichiers, ligne de commande linux"
---

## Lesson Content

Lorsque vous consultez des fichiers texte trop volumineux pour tenir sur un seul écran, la `commande less` est un outil inestimable. Comme le dit le vieil adage Unix : « less is more » (moins c'est plus). (C'est un jeu de mots sur le fait qu'il existe également une commande `more` avec une fonctionnalité similaire). L'utilitaire `less` affiche le texte sous forme paginée, vous permettant de naviguer dans un fichier page par page sans charger le fichier entier en mémoire.

### Démarrer avec la commande Less

Pour commencer à visualiser un fichier, utilisez simplement la `commande less` suivie du nom du fichier. Cela ouvrira le fichier dans l'interface `less`.

```bash
less /home/pete/Documents/text1
```

Une fois que vous êtes dans la visionneuse `less`, vos commandes shell standard ne fonctionneront pas. Au lieu de cela, vous utilisez un ensemble spécifique de touches pour naviguer et interagir avec le texte.

### Navigation et Commandes

Vous pouvez utiliser plusieurs touches pour vous déplacer dans le document :

- **Touches fléchées et touches de page** : Utilisez `Page Haut`, `Page Bas`, `Flèche Haut` et `Flèche Bas` pour naviguer ligne par ligne ou page par page.
- **Aller au début** : Appuyez sur `g` pour vous déplacer directement au début du fichier texte.
- **Aller à la fin** : Appuyez sur `G` (Maj + g) pour sauter à la fin du fichier texte.
- **Menu d'aide** : Si vous oubliez les commandes pendant que vous êtes dans `less`, appuyez simplement sur `h` pour afficher un résumé utile.

### Recherche Unix Less

Une fonctionnalité puissante de `less` est sa capacité à rechercher du texte. Pour effectuer une `recherche unix less`, tapez `/` suivi du texte que vous souhaitez trouver, puis appuyez sur Entrée. Cela mettra en surbrillance toutes les occurrences de votre terme de recherche.

- `/terme_recherche` : Recherche vers l'avant de "terme_recherche".
- `?terme_recherche` : Recherche vers l'arrière de "terme_recherche".
- `n` : Passe à l'occurrence suivante du terme de recherche.
- `N` : Passe à l'occurrence précédente.

### Comment quitter Less

Lorsque vous avez terminé de visualiser le fichier, vous devez savoir comment `quitter less` et revenir à votre invite de commande.

- **Quitter** : Appuyez simplement sur `q` pour quitter la visionneuse `less` et revenir à votre shell.

Maîtriser la `commande less` est une compétence fondamentale pour quiconque travaille sur la ligne de commande Linux, rendant l'inspection des fichiers beaucoup plus efficace.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la visualisation et de la navigation des fichiers texte sous Linux :

1. **[Commande Linux less : Pagination de fichiers](https://labex.io/fr/labs/linux-linux-less-command-file-paging-214301)** - Apprenez la commande Linux 'less' pour une visualisation et une navigation efficaces des fichiers texte, y compris la recherche, les numéros de ligne et la correspondance de motifs.
2. **[Commande Linux more : Défilement de fichiers](https://labex.io/fr/labs/linux-linux-more-command-file-scrolling-214299)** - Apprenez la commande Linux 'more' pour une visualisation efficace des fichiers texte, couvrant l'utilisation de base, le démarrage à partir de lignes spécifiques et la personnalisation de l'affichage.
3. **[Visualisation des fichiers journaux et de configuration sous Linux](https://labex.io/fr/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Apprenez les compétences essentielles de la ligne de commande Linux pour visualiser et naviguer efficacement dans les fichiers texte, y compris les journaux système et les fichiers de configuration, à l'aide de commandes telles que `cat`, `more` et `less`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la manipulation et la navigation des fichiers texte.

## Quiz Question

Comment quittez-vous la commande `less` ? Veuillez fournir la touche de caractère unique comme réponse. Note : la réponse est une lettre anglaise sensible à la casse.

## Quiz Answer

q
