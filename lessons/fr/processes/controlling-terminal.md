---
index: 2
lang: "fr"
title: "Contrôle du Terminal"
meta_title: "Contrôle du Terminal - Processus"
meta_description: "Explorez le concept de terminal de contrôle sous Linux. Apprenez ce qu'est un TTY, la différence entre TTY et PTS, et comment utiliser la sortie de `ps tty` pour identifier les processus sans terminal de contrôle, comme les démons."
meta_keywords: "terminal de contrôle, ps tty, qu'est-ce que tty, comment utiliser ps, TTY, PTS, terminal Linux, processus démon, processus Linux"
---

## Lesson Content

Lorsque vous inspectez les processus en cours d'exécution, vous remarquerez un champ `TTY` dans la sortie de la commande `ps`. Ce champ est important car il indique le **terminal de contrôle** qui a exécuté la commande. Comprendre ce concept est essentiel pour gérer efficacement les processus.

### Qu'est-ce qu'un TTY

TTY est l'abréviation de "Teletype", qui était historiquement un appareil physique pour interagir avec un ordinateur. Dans les systèmes Linux modernes, un TTY fait référence au terminal qui fournit l'entrée et la sortie standard pour un processus.

Il existe deux principaux types de terminaux que vous rencontrerez : les périphériques terminaux et les périphériques pseudo-terminaux.

### Périphériques Terminaux vs Pseudo-Terminaux

Un véritable périphérique terminal est une console native qui vous permet de taper des commandes et de voir la sortie directement. Vous pouvez en faire l'expérience en basculant vers une console virtuelle. Sur de nombreux systèmes, vous pouvez appuyer sur `Ctrl-Alt-F1` pour accéder à TTY1. Vous verrez une invite de connexion dans un environnement purement textuel, sans interface graphique. C'est un terminal classique. Pour revenir à votre session graphique, vous pouvez généralement utiliser `Ctrl-Alt-F7` (la combinaison de touches exacte peut varier).

A contrario, un pseudo-terminal (PTS) est ce que vous utilisez le plus souvent. Lorsque vous ouvrez une application de terminal dans votre environnement de bureau graphique, vous utilisez un PTS. Ceux-ci émulent un terminal dans une fenêtre. Si vous vérifiez la sortie `ps tty` pour votre shell, vous verrez son TTY listé comme `pts/*`.

### Le Rôle du Terminal de Contrôle

La plupart des processus sont liés à un **terminal de contrôle**. Cela signifie que le cycle de vie du processus est lié à la session de terminal qui l'a démarré. Par exemple, si vous exécutez un programme comme `find` dans votre fenêtre de terminal et que vous fermez ensuite cette fenêtre, le processus `find` sera également terminé.

### Processus Sans Terminal de Contrôle

Certains processus, appelés démons, sont conçus pour s'exécuter en arrière-plan et gérer les services système. Ces processus démarrent souvent lorsque le système démarre et ne s'arrêtent qu'à l'arrêt du système.

Pour éviter qu'ils ne soient terminés accidentellement, les démons ne sont pas attachés à un **terminal de contrôle**. Lorsque vous apprenez **comment utiliser ps** pour examiner ces processus, vous verrez un point d'interrogation (`?`) dans la colonne TTY. Ce `?` signifie que le processus n'a pas de terminal de contrôle et s'exécute indépendamment de toute session utilisateur.

## Exercise

La pratique rend parfait ! Voici un laboratoire pratique pour renforcer votre compréhension des processus Linux et de leur interaction avec les terminaux :

1. **[Gérer et Surveiller les Processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Dans ce laboratoire, vous apprendrez les compétences essentielles pour gérer et surveiller les processus sur un système Linux. Vous explorerez comment interagir avec les processus au premier plan et en arrière-plan, les inspecter avec `ps`, surveiller les ressources avec `top`, ajuster la priorité avec `renice`, et les terminer avec `kill`.

Ce laboratoire vous aidera à appliquer les concepts de gestion des processus dans des scénarios réels et à renforcer votre confiance dans la compréhension du fonctionnement et de l'interaction des processus avec le système.

## Quiz Question

Quelle valeur est donnée à un processus qui n'a pas de terminal de contrôle ?

## Quiz Answer

?
