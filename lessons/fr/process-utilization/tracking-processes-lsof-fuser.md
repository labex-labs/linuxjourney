---
index: 2
lang: "fr"
title: "lsof et fuser"
meta_title: "lsof et fuser - Utilisation des processus"
meta_description: "Explorez les commandes Linux lsof et fuser pour identifier quels processus utilisent des fichiers spécifiques. Apprenez à résoudre les erreurs 'Périphérique ou ressource occupée', comparez fuser et lsof, et utilisez des options comme fuser -k pour gérer efficacement les fichiers ouverts."
meta_keywords: "lsof, fuser, commande fuser, fuser linux, fuser vs lsof, lsof vs fuser, fuser -k linux, fichiers ouverts, gestion des processus, périphérique occupé, commandes Linux"
---

## Lesson Content

Avez-vous déjà essayé de démonter une clé USB et reçu une erreur "Périphérique ou ressource occupé" ? Ce problème courant survient lorsqu'un processus utilise encore un fichier ou un répertoire sur le périphérique. Pour résoudre ce problème, vous devez découvrir quel processus détient la ressource. Deux utilitaires puissants pour cette tâche sont `lsof` et `fuser`.

### Utilisation de lsof pour lister les fichiers ouverts

Sous Linux, presque tout est traité comme un fichier, y compris les disques, les pipes, les sockets réseau et les périphériques. La commande `lsof` (abréviation de "list open files") vous montre une liste détaillée de tous les fichiers ouverts et des processus qui les utilisent.

Pour voir quels processus utilisent le répertoire courant (`.`), vous pouvez exécuter :

```bash
pete@icebox:~$ lsof .
COMMAND    PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
lxsession 1491 pete  cwd    DIR    8,6     4096  131 .
update-no 1796 pete  cwd    DIR    8,6     4096  131 .
nm-applet 1804 pete  cwd    DIR    8,6     4096  131 .
xterm     2205 pete  cwd    DIR    8,6     4096  131 .
bash      2207 pete  cwd    DIR    8,6     4096  131 .
lsof      5914 pete  cwd    DIR    8,6     4096  131 .
```

Le résultat montre la commande (`COMMAND`), l'ID de processus (`PID`) et l'utilisateur (`USER`) associés à chaque fichier ouvert. Avec ces informations, vous pouvez identifier les processus qui vous empêchent de démonter un périphérique.

### La commande fuser

Un autre excellent outil est la commande `fuser` (abréviation de "file user"). Cet utilitaire identifie quels processus utilisent des fichiers, des sockets ou des systèmes de fichiers spécifiques. La commande `linux fuser` est un moyen rapide de voir les PID des processus accédant à une ressource particulière.

L'utilisation de l'option `-v` (verbose) fournit un résultat plus détaillé :

```bash
pete@icebox:~$ fuser -v .
                     USER        PID ACCESS COMMAND
/home/pete:         pete  1491 ..c.. lxsession
                     pete  1796 ..c.. update-notifier
                     pete  1804 ..c.. nm-applet
                     pete  2205 ..c.. xterm
                     pete  2207 ..c.. bash
```

Ici, nous pouvons voir clairement quels processus utilisent notre répertoire courant. La colonne `ACCESS` montre comment le fichier est utilisé (par exemple, `c` pour répertoire courant).

### Terminer les processus avec fuser

Une fonctionnalité clé de la commande `fuser` est sa capacité à terminer les processus qui utilisent une ressource. L'option `fuser -k` envoie un signal `SIGKILL` à chaque processus accédant au fichier ou système de fichiers spécifié. Ceci est particulièrement utile pour démonter un périphérique occupé.

Par exemple, pour tuer tous les processus utilisant un point de montage à `/mnt/usb`, vous exécuteriez :

```bash
sudo fuser -k /mnt/usb
```

L'utilisation de `fuser -k` sous Linux est un moyen rapide et efficace de libérer une ressource.

### fuser vs lsof

Alors, quand faut-il utiliser `fuser` contre `lsof` ?

- **`lsof`** est excellent pour les investigations détaillées. Il fournit des informations exhaustives sur tous les fichiers ouverts, ce qui le rend idéal pour un dépannage complexe.
- **`fuser`** est plus direct. Il est parfait pour identifier rapidement et, si nécessaire, terminer les processus sur un fichier ou un point de montage spécifique. La commande `fuser command` est souvent le choix le plus rapide pour résoudre les erreurs "Périphérique ou ressource occupé".

Les deux outils sont essentiels pour tout utilisateur Linux. Familiarisez-vous avec eux pour gérer efficacement les fichiers et les processus.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des processus et du dépannage des conflits de ressources :

1. **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir avec les processus au premier plan et en arrière-plan, à les inspecter avec `ps`, à surveiller les ressources avec `top` et à les terminer avec `kill`. Ce laboratoire vous aidera à identifier et à gérer les processus qui pourraient conserver des ressources, comme les fichiers sur une clé USB.

Ce laboratoire vous aidera à appliquer ces concepts dans des scénarios réels et à renforcer votre confiance dans l'identification et la gestion des processus système.

## Quiz Question

Quelle commande est utilisée pour lister les fichiers ouverts et les informations sur les processus associés ?

## Quiz Answer

lsof
