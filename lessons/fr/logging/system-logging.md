---
index: 1
lang: "fr"
title: "Journalisation du système"
meta_title: "Journalisation du système - Journalisation"
meta_description: "Apprenez la journalisation du système Linux, syslog et comment afficher les fichiers journaux dans /var/log. Comprenez rsyslogd et surveillez les événements système avec ce guide pour débutants."
meta_keywords: "journalisation Linux, syslog, rsyslogd, var log, journaux système, tutoriel Linux, guide du débutant"
---

## Lesson Content

Les services, le noyau, les démons, etc., de votre système sont constamment en activité. Ces données sont en fait envoyées pour être sauvegardées sur votre système sous forme de journaux (logs). Cela nous permet d'avoir un journal lisible par l'homme des événements qui se produisent sur notre système. Ces données sont généralement conservées dans le répertoire `/var` ; le répertoire `/var` est l'endroit où nous conservons nos données variables, telles que les journaux !

Comment ces messages sont-ils reçus sur votre système ? Il existe un service appelé syslog qui envoie ces informations au journaliseur système.

Syslog contient en fait de nombreux composants. L'un des plus importants est un démon en cours d'exécution appelé `syslogd` (les distributions Linux plus récentes utilisent `rsyslogd`), qui attend que des messages d'événement se produisent et filtre ceux qu'il souhaite connaître. Selon ce qu'il est censé faire avec ce message, il l'enverra à un fichier, à votre console, ou n'en fera rien.

On pourrait penser que ce journaliseur système est l'endroit centralisé pour gérer les journaux, mais malheureusement, ce n'est pas le cas. Vous verrez de nombreuses applications qui écrivent leurs propres règles de journalisation et génèrent différents fichiers journaux. Cependant, en général, le format des journaux doit inclure un horodatage et les détails de l'événement.

Voici un exemple de ligne de syslog :

```plaintext
pete@icebox:~$ less /var/log/syslog
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
```

Ici, nous pouvons voir qu'au 27 janvier à 07:41:32, notre service cron a exécuté la tâche `cron.weekly`. Vous pouvez consulter tous les messages d'événement que syslog collecte dans le fichier `/var/log/syslog`.

## Exercise

C'est en forgeant qu'on devient forgeron ! Voici quelques ateliers pratiques pour renforcer votre compréhension des journaux Linux et de la visualisation de fichiers :

1. **[Affichage des fichiers journaux et de configuration sous Linux](https://labex.io/fr/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Apprenez les compétences essentielles de la ligne de commande Linux pour visualiser et naviguer efficacement dans les fichiers texte, y compris les journaux système et les fichiers de configuration. Entraînez-vous à utiliser des commandes comme `cat`, `more` et `less` pour extraire des informations critiques de divers types de fichiers.
2. **[Commande Linux tail : Affichage de la fin du fichier](https://labex.io/fr/labs/linux-linux-tail-command-file-end-display-214303)** - Apprenez la commande Linux `tail` pour visualiser et surveiller la fin des fichiers texte. Ceci est particulièrement utile pour l'analyse des journaux en temps réel.
3. **[Rechercher du texte avec grep sous Linux](https://labex.io/fr/labs/comptia-search-text-with-grep-in-linux-590841)** - Dans ce laboratoire, vous apprendrez à rechercher du texte dans des fichiers sur un système Linux à l'aide de la commande `grep`. C'est inestimable pour trouver des entrées spécifiques dans de grands fichiers journaux.

Ces laboratoires vous aideront à appliquer les concepts de gestion et d'analyse des fichiers journaux dans des scénarios réels et à renforcer votre confiance dans la surveillance des systèmes Linux.

## Quiz Question

Quel est le démon qui gère les journaux sur les systèmes Linux plus récents ?

## Quiz Answer

rsyslogd
