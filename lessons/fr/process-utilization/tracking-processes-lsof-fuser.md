---
index: 2
---
---
lang: "fr"
title: "lsof et fuser"
meta_description: "Apprenez à utiliser les commandes lsof et fuser sous Linux pour identifier les processus utilisant des fichiers. Comprenez les erreurs "Device or Resource Busy" et gérez efficacement les fichiers ouverts."
meta_keywords: "lsof, fuser, commandes Linux, fichiers ouverts, gestion des processus, tutoriel Linux, guide du débutant, périphérique occupé"
---

## Lesson Content

Disons que vous avez branché une clé USB et commencé à travailler sur des fichiers. Une fois terminé, vous avez essayé de démonter le périphérique USB et avez reçu une erreur : "Device or Resource Busy." Comment feriez-vous pour savoir quels fichiers sur la clé USB sont encore utilisés ? Il existe deux outils que vous pouvez utiliser pour cela :

### lsof

N'oubliez pas que les fichiers ne sont pas seulement des fichiers texte, des images, etc. ; ils sont tout sur le système : disques, pipes, sockets réseau, périphériques, etc. Pour voir ce qui est utilisé par un processus, vous pouvez utiliser la commande `lsof` (abréviation de "list open files"). Cela vous montrera une liste de tous les fichiers ouverts et de leurs processus associés.

```bash
pete@icebox:~$ lsof .
COMMAND    PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
lxsession 1491 pete  cwd    DIR    8,6     4096  131 .
update-no 1796 pete  cwd    DIR    8,6     4096  131 .
nm-applet 1804 pete  cwd    DIR    8,6     4096  131 .
indicator 1809 pete  cwd    DIR    8,6     4096  131 .
xterm     2205 pete  cwd    DIR    8,6     4096  131 .
bash      2207 pete  cwd    DIR    8,6     4096  131 .
lsof      5914 pete  cwd    DIR    8,6     4096  131 .
lsof      5915 pete  cwd    DIR    8,6     4096  131 .
```

Maintenant, je peux voir quels processus maintiennent le périphérique/fichier ouvert. Dans notre exemple USB, vous pouvez également tuer ces processus afin de pouvoir démonter ce disque gênant.

### fuser

Une autre façon de suivre un processus est avec la commande `fuser` (abréviation de "file user"). Cela vous montrera des informations sur le processus qui utilise le fichier ou l'utilisateur du fichier.

```bash
pete@icebox:~$ fuser -v .
                     USER        PID ACCESS COMMAND
/home/pete:         pete  1491 ..c.. lxsession
                     pete  1796 ..c.. update-notifier
                     pete  1804 ..c.. nm-applet
                     pete  1809 ..c.. indicator-power
                     pete  2205 ..c.. xterm
                     pete  2207 ..c.. bash
```

Nous pouvons voir quels processus utilisent actuellement notre répertoire `/home/pete`. Les outils `lsof` et `fuser` sont très similaires. Familiarisez-vous avec ces outils et essayez de les utiliser la prochaine fois que vous aurez besoin de suivre un fichier ou un processus.

## Exercise

Lisez les pages de manuel pour `lsof` et `fuser`. Il y a beaucoup d'informations que nous n'avons pas couvertes qui vous permettent d'avoir une plus grande flexibilité avec ces outils.

## Quiz Question

Quelle commande est utilisée pour lister les fichiers ouverts et leurs informations de processus ?

## Quiz Answer

lsof
