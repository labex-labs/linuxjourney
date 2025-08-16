---
lang: "fr"
title: "Journalisation du système"
description: "Découvrez la journalisation système Linux, syslog et comment afficher les fichiers journaux dans /var/log. Comprenez rsyslogd et surveillez les événements système avec ce guide pour débutants."
keywords: "Journalisation Linux, syslog, rsyslogd, var log, journaux système, tutoriel Linux, guide du débutant"
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

Ici, nous pouvons voir que le 27 janvier à 07:41:32, notre service cron a exécuté la tâche `cron.weekly`. Vous pouvez consulter tous les messages d'événement que syslog collecte dans le fichier `/var/log/syslog`.

## Exercise

Regardez votre fichier `/var/log/syslog` et voyez ce qui se passe d'autre sur votre machine.

## Quiz Question

Quel est le démon qui gère les journaux sur les systèmes Linux plus récents ?

## Quiz Answer

rsyslogd
