---
index: 2
lang: "fr"
title: "Contrôle du terminal"
meta_title: "Contrôle du terminal - Processus"
meta_description: "Apprenez à contrôler les terminaux sous Linux, y compris TTY vs PTS, et comment les processus y sont liés. Comprenez les processus démons. Commencez votre parcours Linux !"
meta_keywords: "terminal de contrôle, TTY, PTS, terminal Linux, processus démons, débutant Linux, tutoriel Linux, guide Linux"
---

## Lesson Content

Nous avons discuté de l'existence d'un champ TTY dans la sortie de `ps`. Le TTY est le terminal qui a exécuté la commande.

Il existe deux types de terminaux : les **terminaux physiques** et les **terminaux virtuels**. Un terminal physique est un périphérique de terminal natif dans lequel vous pouvez taper et envoyer des sorties à votre système. Cela ressemble à l'application de terminal que vous avez lancée pour accéder à votre shell, mais ce n'est pas le cas.

Nous allons faire une digression pour que vous puissiez voir cela en action. Allez-y et tapez Ctrl-Alt-F1 pour accéder à TTY1 (la première console virtuelle). Vous remarquerez que vous n'avez rien d'autre que le terminal — pas de graphiques, etc. Ceci est considéré comme un terminal physique. Vous pouvez en sortir avec Ctrl-Alt-F7.

Un terminal virtuel est ce avec quoi vous avez l'habitude de travailler. Ils émulent des terminaux avec la fenêtre de terminal shell et sont désignés par PTS. Si vous regardez `ps` à nouveau, vous verrez votre processus shell sous `pts/*`.

Maintenant, revenons au terminal de contrôle : les processus sont généralement liés à un terminal de contrôle. Par exemple, si vous exécutiez un programme dans votre fenêtre de shell, tel que `find`, et que vous fermiez la fenêtre, votre processus se terminerait également avec elle.

Il existe des processus tels que les processus démons, qui sont des processus spéciaux qui maintiennent essentiellement le système en marche. Ils démarrent souvent au démarrage du système et sont généralement terminés lorsque le système est arrêté. Ils s'exécutent en arrière-plan, et comme nous ne voulons pas que ces processus spéciaux soient terminés, ils ne sont pas liés à un terminal de contrôle. Dans la sortie de `ps`, le TTY est listé comme un **?**, ce qui signifie qu'il n'a pas de terminal de contrôle.

## Exercise

La pratique rend parfait ! Voici un laboratoire pratique pour renforcer votre compréhension des processus Linux et de leur interaction avec les terminaux :

1. **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Dans ce laboratoire, vous apprendrez les compétences essentielles pour gérer et surveiller les processus sur un système Linux. Vous explorerez comment interagir avec les processus de premier plan et d'arrière-plan, les inspecter avec `ps`, surveiller les ressources avec `top`, ajuster la priorité avec `renice`, et les terminer avec `kill`.

Ce laboratoire vous aidera à appliquer les concepts de gestion des processus dans des scénarios réels et à renforcer votre confiance dans la compréhension du fonctionnement des processus et de leur interaction avec le système.

## Quiz Question

Quelle valeur est donnée pour un processus qui n'a pas de terminal de contrôle ?

## Quiz Answer

?
