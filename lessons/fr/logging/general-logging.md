---
index: 3
lang: "fr"
title: "Journalisation générale"
meta_title: "Journalisation générale - Journalisation"
meta_description: "Découvrez les fichiers journaux Linux comme /var/log/messages et syslog. Comprenez leurs différences pour un dépannage efficace du système. Commencez votre parcours Linux !"
meta_keywords: "journaux Linux, syslog, var/log/messages, dépannage Linux, débutant Linux, guide Linux, journaux système"
---

## Lesson Content

Il existe de nombreux fichiers journaux que vous pouvez consulter sur votre système ; beaucoup des plus importants se trouvent sous `/var/log`. Nous ne les passerons pas tous en revue, mais nous en discuterons quelques-uns des principaux.

Il existe deux fichiers journaux généraux que vous pouvez consulter pour avoir un aperçu de ce que fait votre système :

### `/var/log/messages`

Ce journal contient tous les messages non critiques et non de débogage, y compris les messages enregistrés pendant le démarrage (dmesg), l'authentification (auth), cron, les démons (daemon), etc. Il est très utile pour avoir un aperçu du comportement de votre machine.

### `/var/log/syslog`

Ceci enregistre tout sauf les messages d'authentification ; c'est extrêmement utile pour déboguer les erreurs sur votre machine.

Ces deux journaux devraient être plus que suffisants pour résoudre les problèmes de votre système. Cependant, si vous souhaitez simplement afficher un composant de journal spécifique, il existe également des journaux séparés pour ceux-ci.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la visualisation et de l'analyse des fichiers journaux :

1. **[Commande Linux tail : Affichage de la fin du fichier](https://labex.io/fr/labs/linux-linux-tail-command-file-end-display-214303)** - Apprenez la commande Linux `tail` pour visualiser et surveiller la fin des fichiers texte, essentielle pour l'analyse des journaux.
2. **[Commande Linux head : Affichage du début du fichier](https://labex.io/fr/labs/linux-linux-head-command-file-beginning-display-214302)** - Explorez la commande `head` pour afficher les premières lignes des fichiers texte, utile pour vérifier rapidement les en-têtes de journaux.
3. **[Détection rapide des menaces](https://labex.io/fr/labs/linux-rapid-threat-detection-387930)** - Pratiquez les compétences essentielles de la ligne de commande Linux pour l'analyse de cybersécurité, en utilisant `tail` et `head` pour extraire et analyser rapidement les entrées de journal récentes.

Ces laboratoires vous aideront à appliquer les concepts de visualisation de fichiers journaux dans des scénarios réels et à renforcer votre confiance dans la surveillance du système.

## Quiz Question

Quel fichier journal enregistre tout sauf les messages d'authentification ?

## Quiz Answer

syslog
