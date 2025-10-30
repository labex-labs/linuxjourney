---
index: 1
lang: "fr"
title: "ps (Processus)"
meta_title: "ps (Processus) - Processus"
meta_description: "Explorez la commande Linux ps avec notre guide complet. Apprenez à utiliser la commande ps -ef sous Linux et d'autres options pour visualiser les processus en cours, comprendre les PID et gérer les tâches système. Un excellent départ pour votre voyage Linux."
meta_keywords: "commande ps, ps -ef linux, commande ps -ef, linux ps -ef, ps -e linux, processus Linux, identifiant de processus, PID, commande top, voyage linux"
---

## Lesson Content

### Comprendre les Processus Linux

Les processus sont les programmes en cours d'exécution sur votre machine. Le noyau Linux les gère, et chaque processus se voit attribuer un numéro unique appelé **identifiant de processus (PID)**. Les PID sont généralement attribués séquentiellement à mesure que de nouveaux processus sont créés.

### Utilisation de Base de la Commande ps

Pour avoir un aperçu de vos processus actifs, exécutez simplement la commande `ps`. Cela fournit un instantané rapide des processus associés à votre session de terminal actuelle.

```plaintext
$ ps

PID        TTY     STAT   TIME          CMD
41230    pts/4    Ss        00:00:00     bash
51224    pts/4    R+        00:00:00     ps
```

Ce résultat montre quelques détails clés :

- **PID** : L'identifiant de processus unique.
- **TTY** : Le terminal de contrôle pour le processus.
- **STAT** : L'état actuel du processus.
- **TIME** : Le temps total CPU utilisé par le processus.
- **CMD** : La commande qui a démarré le processus.

### Explorer ps avec les Options de Style BSD

La commande `ps` est très polyvalente, avec de nombreuses options qui relèvent de différents styles de syntaxe (BSD, System V, GNU). Le style BSD, qui n'utilise pas de tiret pour les options, est assez courant. Une combinaison populaire est `ps aux` :

```bash
ps aux
```

Voici ce que signifient ces options :

- **a** : Affiche tous les processus pour tous les utilisateurs.
- **u** : Fournit un format détaillé, orienté utilisateur.
- **x** : Inclut les processus non attachés à un terminal. Ceux-ci incluent souvent des démons système qui démarrent au démarrage et affichent un `?` dans la colonne TTY.

Cette commande donne un résultat beaucoup plus riche avec des colonnes supplémentaires telles que `USER`, `%CPU`, `%MEM`, `VSZ` et `RSS`. Pour l'instant, nous nous concentrerons sur PID, STAT et COMMAND.

### Utilisation de la Commande ps -ef sous Linux

Une autre syntaxe extrêmement populaire est le style System V. Vous verrez fréquemment la **commande ps -ef** utilisée par les administrateurs système. C'est un moyen puissant d'obtenir une image complète de tout ce qui s'exécute sur votre système.

```bash
ps -ef
```

La commande **ps -ef linux** fournit une liste complète de tous les processus.

- **-e** : Sélectionne chaque processus du système.
- **-f** : Affiche une liste au "format complet", qui comprend des détails tels que UID, PPID (Parent Process ID), C (utilisation CPU) et STIME (heure de début).

De nombreux utilisateurs préfèrent `ps -ef` à `ps aux` pour sa vue hiérarchique claire et ses informations détaillées. Lors du dépannage sur un système Linux, l'exécution de **linux ps -ef** est souvent l'une des premières étapes pour diagnostiquer les problèmes. Une variation plus simple, `ps -e linux`, listera également tous les processus mais dans un format moins détaillé.

### Surveillance en Temps Réel avec top

Alors que `ps` vous donne un instantané, la commande `top` fournit une vue dynamique et en temps réel des processus sur votre système. C'est un excellent outil pour identifier les processus qui consomment le plus de CPU ou de mémoire. Par défaut, l'affichage est actualisé toutes les quelques secondes.

```bash
top
```

## Exercise

La pratique est essentielle pour maîtriser les commandes Linux. Les laboratoires pratiques suivants vous aideront à renforcer votre compréhension de la surveillance et de la gestion des processus :

1. **[Gérer et Surveiller les Processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous aux compétences essentielles pour gérer et surveiller les processus sur un système Linux, y compris l'interaction avec les processus de premier plan/arrière-plan, l'inspection avec `ps`, la surveillance avec `top` et la terminaison avec `kill`.
2. **[Commande Linux top : Surveillance du Système en Temps Réel](https://labex.io/fr/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Apprenez à utiliser la commande Linux `top` pour la surveillance du système en temps réel, y compris le tri des processus, l'ajustement des intervalles de mise à jour et le filtrage par utilisateur.

Ces laboratoires vous aideront à appliquer les concepts d'identification et de surveillance des processus dans des scénarios réels, renforçant ainsi votre confiance en tant qu'administrateur système Linux.

## Quiz Question

Quel indicateur `ps`, lorsqu'il est utilisé avec les indicateurs `a` et `x`, est utilisé pour afficher des informations détaillées et orientées utilisateur sur les processus ? Veuillez répondre avec une seule lettre anglaise minuscule.

## Quiz Answer

u
