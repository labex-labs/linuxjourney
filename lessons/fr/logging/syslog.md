---
lang: "fr"
title: "syslog"
meta_description: "Découvrez syslog et rsyslog sous Linux, comment gérer les journaux système et utiliser la commande logger. Démarrez avec ce tutoriel convivial pour débutants !"
meta_keywords: "syslog, rsyslog, journaux Linux, commande logger, /var/log/syslog, tutoriel Linux, Linux débutant, journalisation système"
---

## Lesson Content

Le service syslog gère et envoie les journaux au consignateur système. Rsyslog est une version avancée de syslog ; la plupart des distributions Linux devraient utiliser cette nouvelle version. La sortie de tous les journaux collectés par le service syslog se trouve dans `/var/log/syslog` (chaque message, à l'exception des messages d'authentification).

Pour savoir quels fichiers sont gérés par notre consignateur système, consultez les fichiers de configuration dans `/etc/rsyslog.d` :

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

Ces règles pour les fichiers journaux sont désignées par le sélecteur dans la colonne de gauche et l'action dans la colonne de droite. L'action nous indique où envoyer les informations de journalisation : vers un fichier, la console, etc. N'oubliez pas que toutes les applications et services n'utilisent pas rsyslog pour gérer leurs journaux, donc si vous voulez savoir spécifiquement ce qui est enregistré, vous devrez regarder à l'intérieur de ce répertoire.

Voyons la journalisation en action ; vous pouvez envoyer manuellement un journal avec la commande `logger` :

```bash
logger -s Hello
```

Maintenant, regardez à l'intérieur de votre `/var/log/syslog`, et vous devriez voir cette entrée dans vos journaux !

## Exercise

Regardez votre fichier de configuration `/etc/rsyslog.d` et voyez ce qui est d'autre enregistré via le consignateur système.

## Quiz Question

Quelle commande pouvez-vous utiliser pour enregistrer manuellement un message ?

## Quiz Answer

logger
