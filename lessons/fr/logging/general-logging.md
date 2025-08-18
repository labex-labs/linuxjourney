---
index: 3
lang: "fr"
title: "Journalisation générale"
meta_title: "Journalisation générale - Logging"
meta_description: "Découvrez les fichiers journaux Linux comme /var/log/messages et syslog. Comprenez leurs différences pour un dépannage efficace du système. Commencez votre parcours Linux !"
meta_keywords: "Journaux Linux, syslog, var/log/messages, dépannage Linux, débutant Linux, guide Linux, journaux système"
---

## Lesson Content

Il existe de nombreux fichiers journaux que vous pouvez consulter sur votre système ; beaucoup d'entre eux se trouvent sous `/var/log`. Nous ne les passerons pas tous en revue, mais nous discuterons de quelques-uns des principaux.

Il existe deux fichiers journaux généraux que vous pouvez consulter pour avoir un aperçu de ce que fait votre système :

### `/var/log/messages`

Ce journal contient tous les messages non critiques et non de débogage, y compris les messages enregistrés pendant le démarrage (dmesg), l'authentification (auth), cron, daemon, etc. Il est très utile pour avoir un aperçu du comportement de votre machine.

### `/var/log/syslog`

Celui-ci enregistre tout sauf les messages d'authentification (auth) ; il est extrêmement utile pour déboguer les erreurs sur votre machine.

Ces deux journaux devraient être plus que suffisants pour résoudre les problèmes de votre système. Cependant, si vous souhaitez simplement consulter un composant de journal spécifique, il existe également des journaux séparés pour ceux-ci.

## Exercise

Look at your `/var/log/messages` and `/var/log/syslog` files and see what the differences are.

## Quiz Question

Quel fichier journal enregistre tout sauf les messages d'authentification (auth) ?

## Quiz Answer

syslog
