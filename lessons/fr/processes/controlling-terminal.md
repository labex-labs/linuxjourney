---
lang: "fr"
title: "Contrôler le Terminal"
meta_description: "Apprenez à contrôler les terminaux sous Linux, y compris TTY vs PTS, et comment les processus y sont liés. Comprenez les processus daemon. Commencez votre parcours Linux !"
meta_keywords: "terminal de contrôle, TTY, PTS, terminal Linux, processus daemon, débutant Linux, tutoriel Linux, guide Linux"
---

## Lesson Content

Nous avons discuté de la présence d'un champ TTY dans la sortie de `ps`. Le TTY est le terminal qui a exécuté la commande.

Il existe deux types de terminaux : les **périphériques de terminal** réguliers et les **périphériques de pseudoterminal**. Un périphérique de terminal régulier est un périphérique de terminal natif dans lequel vous pouvez taper et envoyer des sorties à votre système. Cela ressemble à l'application de terminal que vous avez lancée pour accéder à votre shell, mais ce n'est pas le cas.

Nous allons faire une digression pour que vous puissiez voir cela en action. Allez-y et tapez Ctrl-Alt-F1 pour accéder à TTY1 (la première console virtuelle). Vous remarquerez que vous n'avez rien d'autre que le terminal — pas de graphiques, etc. Ceci est considéré comme un périphérique de terminal régulier. Vous pouvez en sortir avec Ctrl-Alt-F7.

Un pseudoterminal est ce avec quoi vous avez l'habitude de travailler. Ils émulent des terminaux avec la fenêtre de terminal du shell et sont désignés par PTS. Si vous regardez `ps` à nouveau, vous verrez votre processus shell sous `pts/*`.

Maintenant, revenons au terminal de contrôle : les processus sont généralement liés à un terminal de contrôle. Par exemple, si vous exécutiez un programme dans votre fenêtre de shell, tel que `find`, et que vous fermiez la fenêtre, votre processus se terminerait également avec elle.

Il existe des processus tels que les processus daemon, qui sont des processus spéciaux qui maintiennent essentiellement le système en marche. Ils démarrent souvent au démarrage du système et sont généralement terminés lorsque le système est arrêté. Ils s'exécutent en arrière-plan, et comme nous ne voulons pas que ces processus spéciaux soient terminés, ils ne sont pas liés à un terminal de contrôle. Dans la sortie de `ps`, le TTY est listé comme un **?**, ce qui signifie qu'il n'a pas de terminal de contrôle.

## Exercise

Regardez la sortie de votre `ps` et listez toutes les valeurs TTY uniques.

## Quiz Question

Quelle valeur est donnée pour un processus qui n'a pas de terminal de contrôle ?

## Quiz Answer

?
