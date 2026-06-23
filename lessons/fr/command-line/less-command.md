---
index: 8
lang: "fr"
title: "less"
meta_title: "less - Ligne de commande"
meta_description: "Apprenez la commande Linux less avec des exemples pour visualiser de gros fichiers, défiler, rechercher, aller à une ligne, suivre les logs et quitter less."
meta_keywords: "commande less, linux less, voir gros fichier linux, rechercher dans less, quitter less, less -N, less +F, visualiseur texte linux"
---

## Lesson Content

Lorsque vous visualisez des fichiers texte trop volumineux pour tenir sur un seul écran, la commande `less` est un outil précieux. Comme le dit le vieil adage Unix, « less is more ». C’est un jeu de mots faisant référence à la commande `more` qui offre une fonctionnalité similaire.

L’utilitaire `less` affiche le texte en mode paginé, vous permettant de naviguer dans un fichier sans saturer votre terminal.

### Premiers pas avec la commande Less

Pour commencer à visualiser un fichier, utilisez `less` suivi du nom du fichier.

```bash
$ less /home/pete/Documents/text1
```

Une fois dans le visualiseur `less`, vos commandes shell habituelles ne fonctionnent plus. À la place, vous utilisez un ensemble spécifique de touches pour naviguer et interagir avec le texte.

### Navigation et contrôles

Vous pouvez utiliser plusieurs touches pour vous déplacer dans le document :

- **Flèches et touches Page** : Utilisez `Page Up`, `Page Down`, `Up` et `Down` pour naviguer ligne par ligne ou page par page.
- **Aller au début** : Appuyez sur `g` pour aller directement au début du fichier texte.
- **Aller à la fin** : Appuyez sur `G` (Maj + g) pour sauter à la fin du fichier texte.
- **Déplacer d’une demi-page** : Appuyez sur `u` pour monter et `d` pour descendre.
- **Menu d’aide** : Si vous oubliez les commandes dans `less`, appuyez simplement sur `h` pour afficher un résumé utile.

### Recherche dans Less

Une fonctionnalité puissante de `less` est sa capacité à rechercher du texte. Tapez `/` suivi du texte à trouver, puis appuyez sur Entrée.

- `/terme_de_recherche` : Recherche vers l’avant du terme "terme_de_recherche".
- `?terme_de_recherche` : Recherche vers l’arrière du terme "terme_de_recherche".
- `n` : Passe à l’occurrence suivante du terme recherché.
- `N` : Passe à l’occurrence précédente.

### Comment quitter Less

Lorsque vous avez fini de visualiser le fichier, vous devez savoir comment `quitter less` et revenir à votre invite de commande.

- **Quitter** : Appuyez simplement sur `q` pour quitter le visualiseur `less` et revenir à votre shell.

### Options utiles de less

Vous pouvez lancer `less` avec des options :

```bash
$ less -N file.txt
$ less +G file.txt
$ less +F /var/log/syslog
```

- `-N` : Affiche les numéros de ligne.
- `+G` : Ouvre à la fin du fichier.
- `+F` : Suit le contenu ajouté en temps réel, similaire à `tail -f`.

Lorsque vous suivez un fichier avec `+F`, appuyez sur `Ctrl-C` pour arrêter le suivi et revenir à la navigation normale, puis appuyez sur `q` pour quitter.

### Questions fréquentes

**Less est-il meilleur que cat ?** Utilisez `cat` pour les fichiers courts et `less` pour les fichiers longs ou ceux que vous devez rechercher.

**Comment faire une recherche insensible à la casse ?** Lancez `less` avec `-i`, ou tapez les recherches normalement lorsque le motif ne contient pas de majuscules sur de nombreux systèmes.

**Less peut-il ouvrir la sortie d’une commande ?** Oui. Poussez la sortie dans `less`, par exemple `dmesg | less`.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la visualisation et de la navigation dans les fichiers texte sous Linux :

1. **[Commande Linux less : Pagination de fichiers](https://labex.io/fr/labs/linux-linux-less-command-file-paging-214301)** - Apprenez la commande Linux 'less' pour une visualisation et une navigation efficaces dans les fichiers texte, incluant la recherche, les numéros de ligne et la correspondance de motifs.
2. **[Commande Linux more : Défilement de fichiers](https://labex.io/fr/labs/linux-linux-more-command-file-scrolling-214299)** - Apprenez la commande Linux 'more' pour une visualisation efficace des fichiers texte, couvrant l’utilisation de base, le démarrage à partir de lignes spécifiques et la personnalisation de l’affichage.
3. **[Visualisation des fichiers journaux et de configuration sous Linux](https://labex.io/fr/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Apprenez les compétences essentielles en ligne de commande Linux pour visualiser et naviguer efficacement dans les fichiers texte, y compris les journaux système et les fichiers de configuration, en utilisant des commandes comme `cat`, `more` et `less`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance dans la manipulation et la navigation des fichiers texte.

## Quiz Question

Comment quittez-vous la commande `less` ? Veuillez fournir la touche unique comme réponse. Note : la réponse est une lettre anglaise sensible à la casse.

## Quiz Answer

q
