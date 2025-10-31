---
index: 9
lang: "fr"
title: "queue"
meta_title: "tail - Outils Texte"
meta_description: "Guide Linux pour débutants sur la commande tail. Apprenez à utiliser tail sous Linux pour afficher la fin des fichiers et surveiller les logs en temps réel avec l'option puissante tail -f."
meta_keywords: "commande tail, Linux tail, tail -f, visualiser logs, surveiller logs, tutoriel Linux, Linux débutant, guide Linux, surveillance fichiers"
---

## Lesson Content

La commande `tail` est un utilitaire fondamental pour quiconque apprend Linux. Comme son nom l'indique, elle permet de visualiser la "queue" ou la fin d'un fichier. Ceci est particulièrement utile pour vérifier les entrées les plus récentes dans les fichiers qui changent rapidement, tels que les journaux système.

### Visualiser la fin d'un fichier

Par défaut, la commande `tail` affiche les 10 dernières lignes d'un fichier spécifié. Elle fonctionne comme le complément de la commande `head`.

```bash
tail /var/log/syslog
```

Tout comme avec `head`, vous pouvez personnaliser le nombre de lignes que vous souhaitez afficher en utilisant l'option `-n`. Par exemple, pour voir les 20 dernières lignes, vous utiliseriez la commande suivante :

```bash
tail -n 20 /var/log/syslog
```

Cette flexibilité fait de la commande `tail Linux` un outil essentiel pour inspecter rapidement les fins de fichiers sans ouvrir le fichier entier.

### Surveillance de fichiers en temps réel avec tail -f

L'une des fonctionnalités les plus puissantes de la commande `tail` est sa capacité à surveiller les fichiers en temps réel. Ceci est réalisé avec l'indicateur `-f` (follow/suivre). Lorsque vous utilisez `tail -f`, la commande ne se termine pas après avoir affiché les dernières lignes. Au lieu de cela, elle attend que de nouvelles données soient ajoutées au fichier et les imprime à l'écran au fur et à mesure de leur arrivée.

```bash
tail -f /var/log/syslog
```

Essayez d'exécuter cette commande. Au fur et à mesure que vous continuez à utiliser votre système, vous verrez de nouvelles lignes apparaître dans votre terminal. Cela fait de `tail -f` un outil indispensable pour les administrateurs système et les développeurs qui ont besoin de `visualiser les journaux` et de surveiller la sortie des applications au fur et à mesure qu'elles se produisent.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la commande `tail` et de ses applications :

1. **[Commande tail Linux : Affichage de la fin de fichier](https://labex.io/fr/labs/linux-linux-tail-command-file-end-display-214303)** - Apprenez la commande `tail` Linux pour visualiser et surveiller la fin des fichiers texte, y compris l'option `-f` pour les mises à jour en temps réel.
2. **[Visualisation des fichiers journaux et de configuration sous Linux](https://labex.io/fr/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Entraînez-vous à utiliser `tail` (avec `cat` et `more`) pour visualiser et naviguer efficacement dans les fichiers journaux et de configuration, ce qui est crucial pour la surveillance du système.
3. **[Détection rapide des menaces](https://labex.io/fr/labs/linux-rapid-threat-detection-387930)** - Appliquez vos connaissances de `tail` pour extraire et analyser rapidement les entrées de journal récentes, simulant une détection rapide des menaces dans un contexte de cybersécurité.

Ces laboratoires vous aideront à appliquer les concepts de visualisation et de surveillance du contenu des fichiers dans des scénarios réels et à gagner en confiance avec la commande `tail`.

## Quiz Question

Quel est l'indicateur utilisé pour suivre un fichier dans `tail` ? (Veuillez répondre en anglais, en faisant attention à la casse)

## Quiz Answer

-f
