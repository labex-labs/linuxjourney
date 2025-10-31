---
index: 8
lang: "fr"
title: "head"
meta_title: "head - Text-Fu"
meta_description: "Un guide Linux pour débutants sur l'utilisation de la commande head pour afficher le début d'un fichier. Apprenez à utiliser l'option head -n pour contrôler le nombre de lignes, une compétence essentielle pour tout tutoriel Linux."
meta_keywords: "commande head, Linux head, afficher début fichier, tutoriel Linux, commandes Linux, Linux débutant, head -n, guide Linux, fichiers texte, ligne de commande"
---

## Lesson Content

Sous Linux, vous devez souvent inspecter le contenu de fichiers très volumineux, tels que les journaux système. Par exemple, si vous exécutez `cat /var/log/syslog`, vous verrez défiler des pages de texte, ce qui rend difficile d'avoir un aperçu rapide. Alors, que faire si vous voulez seulement **visualiser le début d'un fichier** ? La commande `head` est l'outil parfait pour cette tâche.

### Comportement par défaut de la commande head

Par défaut, la commande `head` affiche les 10 premières lignes de tout fichier donné. C'est une partie fondamentale de notre **guide Linux pour débutants** sur la manipulation de texte. Pour la voir en action, fournissez simplement un nom de fichier comme argument :

```bash
head /var/log/syslog
```

Cette commande affichera les 10 premières lignes de `/var/log/syslog`, vous permettant de vérifier rapidement le contenu initial du fichier sans l'ouvrir dans un éditeur.

### Personnalisation du nombre de lignes

La commande **Linux head** est flexible. Vous pouvez facilement modifier le nombre de lignes affichées à l'aide de l'indicateur `-n`, qui signifie "nombre de lignes". Par exemple, si vous souhaitez voir les 15 premières lignes d'un fichier, vous utiliseriez l'option `head -n` comme suit :

```bash
head -n 15 /var/log/syslog
```

Cela fait de `head` l'une des **commandes Linux** les plus utiles pour inspecter rapidement les en-têtes de fichiers ou les entrées de journaux.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la visualisation du début des fichiers et de la manipulation générale des fichiers texte :

1. **[Commande Linux head : Affichage du début de fichier](https://labex.io/fr/labs/linux-linux-head-command-file-beginning-display-214302)** - Ce laboratoire vous guidera dans l'utilisation de la commande `head` pour afficher les lignes initiales des fichiers texte, y compris la modification du nombre de lignes.
2. **[Visualisation des fichiers journaux et de configuration sous Linux](https://labex.io/fr/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Entraînez-vous aux compétences essentielles de la ligne de commande Linux pour visualiser et naviguer efficacement dans les fichiers texte, y compris les journaux système et les fichiers de configuration, qui nécessitent souvent des commandes comme `head`.
3. **[Détection rapide des menaces](https://labex.io/fr/labs/linux-rapid-threat-detection-387930)** - Appliquez vos connaissances de `head` (et `tail`) pour extraire et analyser rapidement les entrées de journaux récentes, simulant une analyse de cybersécurité réelle.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la visualisation et l'analyse des fichiers texte sous Linux.

## Quiz Question

Quel indicateur utiliseriez-vous avec la commande `head` pour modifier le nombre de lignes que vous souhaitez visualiser ? Veuillez répondre en utilisant uniquement l'indicateur anglais, en faisant attention à la casse.

## Quiz Answer

-n
