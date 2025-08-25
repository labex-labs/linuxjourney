---
index: 1
lang: "fr"
title: "Suivi des processus : top"
meta_title: "Suivi des processus : top - Utilisation des processus"
meta_description: "Apprenez à utiliser la commande Linux `top` pour surveiller les ressources système et suivre les processus. Comprenez les détails du CPU, de la mémoire et des processus pour l'analyse des performances."
meta_keywords: "commande Linux top, surveiller les processus, utilisation du système, performances Linux, débutant, tutoriel, guide"
---

## Lesson Content

Dans ce cours, nous allons voir comment lire et analyser l'utilisation des ressources sur votre système. Cette leçon présente d'excellents outils à utiliser lorsque vous avez besoin de suivre ce qu'un processus est en train de faire.

### top

Nous avons déjà parlé de `top`, mais nous allons approfondir les détails de ce qu'il affiche réellement. Rappelez-vous, `top` est l'outil que nous avons utilisé pour obtenir une vue en temps réel de l'utilisation du système par nos processus :

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

Passons en revue la signification de cette sortie. Vous n'avez pas besoin de la mémoriser, mais revenez-y lorsque vous avez besoin d'une référence.

### 1ère ligne : C'est la même information que vous verriez si vous exécutiez la commande `uptime` (plus à venir)

Les champs sont de gauche à droite :

1. Heure actuelle
2. Durée d'exécution du système
3. Nombre d'utilisateurs actuellement connectés
4. Charge moyenne du système (plus à venir)

### 2ème ligne : Tâches en cours d'exécution, en veille, arrêtées et zombies

### 3ème ligne : Informations CPU

1. `us` : temps CPU utilisateur - Pourcentage du temps CPU passé à exécuter les processus des utilisateurs qui ne sont pas "niced".
2. `sy` : temps CPU système - Pourcentage du temps CPU passé à exécuter le noyau et les processus du noyau.
3. `ni` : temps CPU nice - Pourcentage du temps CPU passé à exécuter les processus "niced".
4. `id` : temps d'inactivité CPU - Pourcentage du temps CPU passé en inactivité.
5. `wa` : attente I/O - Pourcentage du temps CPU passé à attendre les I/O. Si cette valeur est faible, le problème n'est probablement pas lié au disque ou au réseau.
6. `hi` : interruptions matérielles - Pourcentage du temps CPU passé à servir les interruptions matérielles.
7. `si` : interruptions logicielles - Pourcentage du temps CPU passé à servir les interruptions logicielles.
8. `st` : temps volé - Si vous exécutez des machines virtuelles, c'est le pourcentage du temps CPU qui vous a été volé pour d'autres tâches.

### 4ème et 5ème ligne : Utilisation de la mémoire et utilisation du swap

### Liste des processus actuellement utilisés

1. `PID` : ID du processus
2. `USER` : utilisateur propriétaire du processus
3. `PR` : Priorité du processus
4. `NI` : La valeur nice
5. `VIRT` : Mémoire virtuelle utilisée par le processus
6. `RES` : Mémoire physique utilisée par le processus
7. `SHR` : Mémoire partagée du processus
8. `S` : Indique l'état du processus : `S`=veille, `R`=en cours d'exécution, `Z`=zombie, `D`=ininterrompable, `T`=arrêté
9. `%CPU` : pourcentage de CPU utilisé par ce processus
10. `%MEM` : pourcentage de RAM utilisé par ce processus
11. `TIME+` : temps total d'activité de ce processus
12. `COMMAND` : nom du processus

Vous pouvez également spécifier un ID de processus si vous souhaitez simplement suivre certains processus :

```bash
top -p 1
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'utilisation des ressources Linux et de la gestion des processus :

1. **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir avec, inspecter, surveiller et terminer des processus dans un environnement Linux réel.
2. **[Commande Linux top : Surveillance du système en temps réel](https://labex.io/fr/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Apprenez à utiliser la commande `top` pour surveiller l'utilisation du CPU, la mémoire et les processus en cours d'exécution en temps réel.
3. **[Commande Linux free : Surveillance de la mémoire système](https://labex.io/fr/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Apprenez à utiliser la commande `free` pour surveiller et analyser l'utilisation de la mémoire système.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance en matière de surveillance du système et de gestion des processus.

## Quiz Question

Quelle commande affiche la même sortie que la première ligne de `top` ?

## Quiz Answer

uptime
