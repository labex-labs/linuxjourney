---
index: 1
lang: "fr"
title: "Suivi des processus : top"
meta_title: "Suivi des processus : top - Utilisation du processus"
meta_description: "Découvrez la meilleure façon d'apprendre Linux en maîtrisant la commande `top`. Ce guide explique comment surveiller les ressources système, suivre les processus et comprendre les métriques comme VIRT et RES. Une partie essentielle pour comprendre le fonctionnement de Linux."
meta_keywords: "commande top Linux, surveiller les processus, utilisation système, fonctionnement linux, linux top virt res, meilleure façon d'apprendre linux, performance linux, gestion des processus, formation linux gratuite en ligne avec certificat"
---

## Lesson Content

Comprendre comment lire et analyser l'utilisation des ressources est une compétence essentielle pour tout utilisateur Linux. Beaucoup considèrent que maîtriser les outils en ligne de commande est la **meilleure façon d'apprendre Linux** depuis les bases, car ils offrent un aperçu approfondi de **comment fonctionne Linux**. Cette leçon présente `top`, un utilitaire puissant pour suivre en temps réel ce que font vos processus.

### Comprendre la commande top

Nous avons brièvement mentionné `top` auparavant, mais nous allons maintenant examiner les détails de ce qu'il affiche. La commande `top` vous donne une vue dynamique et en temps réel des processus et de l'utilisation du système sur votre machine.

```plaintext
top - 18:06:26 up 6 days,  4:07,  2 users,  load average: 0.92, 0.62, 0.59
Tasks: 389 total,   1 running, 387 sleeping,   0 stopped,   1 zombie
%Cpu(s):  1.8 us,  0.4 sy,  0.0 ni, 97.6 id,  0.1 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem:  32870888 total, 27467976 used,  5402912 free,   518808 buffers
KiB Swap: 33480700 total,    39892 used, 33440808 free. 19454152 cached Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
 6675 patty    20   0 1731472 520960  30876 S   8.3  1.6 160:24.79 chrome
 6926 patty    20   0  935888 163456  25576 S   4.3  0.5   5:28.13 chrome
```

Examinons ce que signifie cette sortie. Vous n'avez pas besoin de la mémoriser, mais vous pouvez utiliser cette leçon comme référence.

### Résumé du système

Les premières lignes fournissent un résumé de haut niveau de l'état du système.

- **1ère ligne** : Il s'agit des mêmes informations que vous verriez si vous exécutiez la commande `uptime`. Elle indique l'heure actuelle, le temps de fonctionnement du système, le nombre d'utilisateurs connectés et la charge moyenne du système sur les 1, 5 et 15 dernières minutes.
- **2ème ligne** : Un résumé de toutes les tâches (processus), classées comme en cours d'exécution, en veille, arrêtées ou zombies.

### Ventilation de l'utilisation du CPU

La troisième ligne détaille l'utilisation du CPU.

- `us` : Pourcentage du temps CPU passé à exécuter des processus utilisateur qui ne sont pas "nicés".
- `sy` : Pourcentage du temps CPU passé à exécuter le noyau et ses processus.
- `ni` : Pourcentage du temps CPU passé à exécuter des processus utilisateur "nicés" (priorité basse).
- `id` : Pourcentage du temps CPU inactif.
- `wa` : Pourcentage du temps CPU passé à attendre que les opérations d'E/S se terminent. Une valeur élevée peut indiquer un goulot d'étranglement du disque ou du réseau.
- `hi` : Pourcentage du temps CPU passé à gérer les interruptions matérielles.
- `si` : Pourcentage du temps CPU passé à gérer les interruptions logicielles.
- `st` : Temps de vol (Steal time). Dans les environnements virtualisés, c'est le pourcentage de temps CPU qu'un CPU virtuel attend un CPU réel, pendant que l'hyperviseur sert un autre processeur virtuel.

### Informations sur la mémoire et le Swap

Les quatrième et cinquième lignes montrent respectivement l'utilisation de la mémoire et de l'espace swap. Cela inclut les montants total, utilisé et libre.

### La liste des processus

Le corps principal de `top` est une liste des processus les plus gourmands en ressources.

- `PID` : L'identifiant unique du processus.
- `USER` : L'utilisateur propriétaire du processus.
- `PR` : La priorité de planification du processus.
- `NI` : La valeur "nice", qui affecte sa priorité.
- `VIRT` : Mémoire virtuelle utilisée par le processus. C'est la quantité totale de mémoire à laquelle le processus peut accéder.
- `RES` : Mémoire Résidente utilisée par le processus. C'est la mémoire physique non paginée qu'une tâche utilise. Comprendre la différence entre **linux top virt res** est essentiel pour l'analyse de la mémoire.
- `SHR` : Mémoire Partagée utilisée par le processus.
- `S` : L'état du processus : `S`=veille, `R`=en cours d'exécution, `Z`=zombie, `D`=veille non interrompue, `T`=arrêté.
- `%CPU` : Le pourcentage de temps CPU utilisé par ce processus depuis la dernière mise à jour.
- `%MEM` : Le pourcentage de RAM physique utilisée par ce processus.
- `TIME+` : Le temps CPU total que le processus a utilisé depuis son démarrage.
- `COMMAND` : Le nom de la commande ou la ligne de commande qui a démarré le processus.

Vous pouvez également surveiller un processus spécifique par son ID, ce qui est utile pour un dépannage ciblé :

```bash
top -p 1
```

## Exercise

La pratique est essentielle pour la maîtrise. Ces laboratoires pratiques sont parmi les **meilleures ressources pour apprendre Linux** la gestion des processus, offrant un environnement pratique pour appliquer ce que vous avez appris.

1.  **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir, inspecter, surveiller et terminer des processus dans un environnement Linux réel.
2.  **[Commande Linux top : Surveillance du système en temps réel](https://labex.io/fr/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Apprenez à utiliser la commande `top` pour surveiller l'utilisation du CPU, la mémoire et les processus en cours d'exécution en temps réel.
3.  **[Commande Linux free : Surveillance de la mémoire système](https://labex.io/fr/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Apprenez à utiliser la commande `free` pour surveiller et analyser l'utilisation de la mémoire système.

## Quiz Question

Quelle commande affiche la même sortie que la première ligne de `top` ? Veuillez répondre en utilisant uniquement le nom de la commande en anglais minuscule.

## Quiz Answer

uptime
