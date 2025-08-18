---
lang: "fr"
title: "kill (Terminer)"
meta_title: "kill (Terminer) - Processus"
meta_description: "Apprenez à utiliser la commande Linux 'kill' pour terminer les processus. Comprenez SIGTERM, SIGKILL et d'autres signaux pour la gestion des processus. Commencez à apprendre maintenant !"
meta_keywords: "commande kill, processus Linux, SIGTERM, SIGKILL, tutoriel Linux, débutant, gestion des processus, guide Linux"
---

## Lesson Content

Vous pouvez envoyer des signaux qui terminent les processus ; une telle commande est nommée à juste titre la commande `kill`.

```bash
kill 12445
```

Le `12445` est le PID du processus que vous souhaitez tuer. Par défaut, il envoie un signal `TERM`. Le signal `SIGTERM` est envoyé à un processus pour demander sa terminaison, lui permettant de libérer proprement ses ressources et de sauvegarder son état.

Vous pouvez également spécifier un signal avec la commande `kill` :

```bash
kill -9 12445
```

Ceci exécutera le signal `SIGKILL` et tuera le processus.

### Differences between SIGHUP, SIGINT, SIGTERM, SIGKILL, SIGSTOP?

Ces signaux semblent tous raisonnablement similaires, mais ils ont leurs différences.

- SIGHUP - Hangup, envoyé à un processus lorsque le terminal de contrôle est fermé. Par exemple, si vous fermiez une fenêtre de terminal qui avait un processus en cours d'exécution, vous recevriez un signal `SIGHUP`. Donc, en gros, vous avez été raccroché.
- SIGINT - Est un signal d'interruption, vous pouvez donc utiliser Ctrl-C, et le système essaiera de tuer le processus gracieusement.
- SIGTERM - Tue le processus, mais lui permet de faire un peu de nettoyage d'abord.
- SIGKILL - Tue le processus, le tue avec le feu, ne fait aucun nettoyage.
- SIGSTOP - Arrête/suspend un processus.

## Exercise

Terminez des processus en utilisant différents signaux.

## Quiz Question

Quel est le nom du signal pour la commande `kill` par défaut ?

## Quiz Answer

SIGTERM
