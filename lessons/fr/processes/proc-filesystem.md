---
index: 10
lang: "fr"
title: "Système de fichiers /proc"
meta_title: "Système de fichiers /proc - Processus"
meta_description: "Découvrez le système de fichiers /proc de Linux, un répertoire virtuel offrant une vue de type tableau de bord sur le noyau et les processus en cours d'exécution. Apprenez à accéder à des détails de processus supplémentaires au-delà des commandes standard."
meta_keywords: "système de fichiers /proc, linux proc, informations processus, extras linux proc, tableau de bord système, processus Linux, informations noyau"
---

## Lesson Content

Sous Linux, un principe fondamental est que tout est traité comme un fichier. Ce concept s'étend aux processus en cours d'exécution, dont les informations sont stockées dynamiquement dans un système de fichiers virtuel spécial connu sous le nom de `/proc`.

### Exploration du répertoire /proc

Le système de fichiers `/proc` n'est pas un vrai système de fichiers sur votre disque dur ; il est créé en mémoire par le noyau. Il offre une fenêtre sur les structures de données internes du noyau et l'état du système.

Pour voir son contenu, vous pouvez lister les fichiers et les répertoires qu'il contient :

```bash
ls /proc
```

Vous verrez de nombreux répertoires numérotés. Chaque numéro correspond à l'ID de processus (PID) d'un processus en cours d'exécution. Vous trouverez également d'autres fichiers comme `cpuinfo` et `meminfo` qui fournissent des informations sur le matériel système.

### Accès aux informations spécifiques d'un processus

Si vous identifiez un PID à l'aide d'une commande comme `ps`, vous pouvez trouver son répertoire correspondant dans `/proc` pour obtenir des informations plus détaillées. Par exemple, pour inspecter un processus avec le PID 12345, vous pouvez consulter son fichier status :

```bash
cat /proc/12345/status
```

Cette commande affichera des informations détaillées sur le processus, y compris son état (par exemple, dormant, en cours d'exécution), l'utilisation de la mémoire et l'identifiant utilisateur. Le répertoire `/proc` offre la vue directe du noyau sur le processus, fournissant beaucoup plus de données que les outils standards.

### Un tableau de bord des données système

Pensez au système de fichiers `/proc` comme à la source de données brutes pour de nombreux outils de surveillance système. Des utilitaires comme `top`, `ps` et `htop` lisent depuis `/proc` pour présenter l'information dans un format convivial. Il contient une mine de détails **supplémentaires** que ces outils pourraient ne pas afficher par défaut.

En accédant directement aux fichiers dans `/proc`, vous pouvez recueillir des métriques spécifiques pour créer des scripts personnalisés ou un **tableau de bord** de surveillance adapté à vos besoins. C'est une interface puissante pour observer et comprendre le fonctionnement interne de votre système Linux.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des processus Linux et de la surveillance du système :

1.  **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Dans ce laboratoire, vous apprendrez les compétences essentielles pour gérer et surveiller les processus sur un système Linux. Vous explorerez comment interagir avec les processus au premier plan et en arrière-plan, les inspecter avec `ps`, surveiller les ressources avec `top`, ajuster la priorité avec `renice` et les terminer avec `kill`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion des processus et l'observation du système.

## Quiz Question

What virtual filesystem stores process information? Please answer in English, paying attention to case sensitivity.

## Quiz Answer

/proc
