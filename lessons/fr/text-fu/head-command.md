---
index: 8
lang: "fr"
title: "head"
meta_title: "head - Text-Fu"
meta_description: "Apprenez à utiliser la commande Linux 'head' pour afficher le début des fichiers. Comprenez les options comme -n pour le nombre de lignes. Tutoriel essentiel sur les commandes Linux."
meta_keywords: "commande head, Linux head, afficher début fichier, tutoriel Linux, commandes Linux, Linux débutant, head -n, guide Linux"
---

## Lesson Content

Disons que nous avons un fichier très long ; en fait, nous en avons beaucoup à choisir. Allez-y et `cat /var/log/syslog`. Vous devriez voir des pages et des pages de texte. Et si je voulais juste voir les deux premières lignes de ce fichier texte ? Eh bien, nous pouvons le faire avec la commande `head`. Par défaut, la commande `head` vous montrera les 10 premières lignes d'un fichier.

```bash
head /var/log/syslog
```

Vous pouvez également modifier le nombre de lignes à votre guise. Disons que je voulais voir les 15 premières lignes à la place.

```bash
head -n 15 /var/log/syslog
```

Le drapeau `-n` signifie "nombre de lignes".

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'affichage du début des fichiers et de la manipulation générale des fichiers texte :

1. **[Commande Linux head : Affichage du début du fichier](https://labex.io/fr/labs/linux-linux-head-command-file-beginning-display-214302)** - Ce laboratoire vous guidera dans l'utilisation de la commande `head` pour afficher les lignes initiales des fichiers texte, y compris la modification du nombre de lignes.
2. **[Affichage des fichiers journaux et de configuration sous Linux](https://labex.io/fr/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Pratiquez les compétences essentielles de la ligne de commande Linux pour visualiser et naviguer efficacement dans les fichiers texte, y compris les journaux système et les fichiers de configuration, qui nécessitent souvent des commandes comme `head`.
3. **[Détection rapide des menaces](https://labex.io/fr/labs/linux-rapid-threat-detection-387930)** - Appliquez vos connaissances de `head` (et `tail`) pour extraire et analyser rapidement les entrées de journal récentes, simulant une analyse de cybersécurité réelle.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la visualisation et l'analyse de fichiers texte sous Linux.

## Quiz Question

Quel drapeau utiliseriez-vous pour modifier le nombre de lignes que vous souhaitez afficher pour la commande `head` ?

## Quiz Answer

-n
