---
index: 2
lang: "fr"
title: "syslog"
meta_title: "syslog - Journalisation"
meta_description: "Apprenez tout sur syslog et rsyslog sous Linux, comment gérer les journaux système et utiliser la commande logger. Commencez avec ce tutoriel convivial pour débutants !"
meta_keywords: "syslog, rsyslog, journaux Linux, commande logger, /var/log/syslog, tutoriel Linux, Linux débutant, journalisation système"
---

## Lesson Content

Le service syslog gère et envoie les journaux au système de journalisation. Rsyslog est une version avancée de syslog ; la plupart des distributions Linux devraient utiliser cette nouvelle version. Le résultat de tous les journaux collectés par le service syslog se trouve dans `/var/log/syslog` (tous les messages, à l'exception des messages d'authentification).

Pour savoir quels fichiers sont maintenus par notre système de journalisation, consultez les fichiers de configuration dans `/etc/rsyslog.d` :

```plaintext
pete@icebox:~$ less /etc/rsyslog.d/50-default.conf
# First some standard log files.  Log by facility.
#
auth,authpriv.*                 /var/log/auth.log
*.*;auth,authpriv.none          -/var/log/syslog
#cron.*                         /var/log/cron.log
#daemon.*                       -/var/log/daemon.log
kern.*                          -/var/log/kern.log
#lpr.*                          -/var/log/lpr.log
mail.*                          -/var/log/mail.log
#user.*                         -/var/log/user.log
```

Ces règles pour les fichiers journaux sont désignées par le sélecteur dans la colonne de gauche et l'action dans la colonne de droite. L'action nous indique où envoyer les informations du journal : vers un fichier, la console, etc. N'oubliez pas que toutes les applications et tous les services n'utilisent pas rsyslog pour gérer leurs journaux. Par conséquent, si vous souhaitez savoir spécifiquement ce qui est enregistré, vous devrez regarder à l'intérieur de ce répertoire.

Voyons maintenant la journalisation en action ; vous pouvez envoyer manuellement un journal avec la commande `logger` :

```bash
logger -s Hello
```

Maintenant, regardez dans votre `/var/log/syslog`, et vous devriez voir cette entrée dans vos journaux.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la journalisation Linux et de la visualisation des fichiers :

1. **[Visualisation des fichiers journaux et de configuration sous Linux](https://labex.io/fr/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Entraînez-vous aux compétences essentielles de la ligne de commande Linux pour visualiser et naviguer efficacement dans les fichiers texte, y compris les journaux système et les fichiers de configuration.
2. **[Commande Linux tail : Affichage de la fin du fichier](https://labex.io/fr/labs/linux-linux-tail-command-file-end-display-214303)** - Apprenez la commande Linux `tail` pour visualiser et surveiller la fin des fichiers texte, ce qui est particulièrement utile pour l'analyse des journaux en temps réel.
3. **[Rechercher du texte avec grep sous Linux](https://labex.io/fr/labs/comptia-search-text-with-grep-in-linux-590841)** - Apprenez à rechercher des modèles de texte spécifiques dans les fichiers, une compétence inestimable pour passer au crible les entrées de journal afin de trouver des informations critiques.

Ces laboratoires vous aideront à appliquer les concepts de gestion des journaux et d'inspection des fichiers dans des scénarios réels et à renforcer votre confiance dans l'administration système Linux.

## Quiz Question

Quelle commande pouvez-vous utiliser pour enregistrer manuellement un message ?

## Quiz Answer

logger
