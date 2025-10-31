---
index: 7
lang: "fr"
title: "kill (Terminer)"
meta_title: "kill (Terminer) - Processus"
meta_description: "Maîtrisez la commande Linux kill pour gérer et terminer les processus. Ce guide couvre les différences entre kill et terminer, et explique les signaux comme kill sigterm (SIGTERM), SIGKILL et kill sighup (SIGHUP)."
meta_keywords: "commande kill, kill sigterm, kill sighup, linux kill -0, kill vs terminer, kill -15 linux, SIGTERM, SIGKILL, gestion des processus, terminer processus"
---

## Lesson Content

Sous Linux, vous pouvez gérer les processus en leur envoyant des signaux. La commande principale pour cela est `kill`, qui, malgré son nom, peut envoyer divers signaux, pas seulement ceux qui terminent un processus.

### Terminaison par défaut avec kill sigterm

Lorsque vous utilisez la commande `kill` avec uniquement un ID de processus (PID), elle envoie un signal `TERM` par défaut. C'est la manière standard et propre de demander à un programme de se terminer.

```bash
kill 12445
```

Le signal `kill sigterm` (également connu sous le nom de `SIGTERM` ou signal 15) demande au processus de s'arrêter proprement. Cela donne au processus une chance de sauvegarder sa progression et de libérer les ressources correctement. Vous pouvez également utiliser explicitement le numéro de signal, rendant `kill -15 12445` équivalent à la commande ci-dessus. Cela répond à la requête courante `kill -15 linux`.

### Forcer la terminaison avec SIGKILL

Parfois, un processus devient inactif et ne réagit pas au signal `SIGTERM`. Dans ces cas, vous pouvez le forcer à s'arrêter en utilisant le signal `KILL`.

```bash
kill -9 12445
```

Le signal `SIGKILL` (signal 9) termine le processus immédiatement, sans lui donner la possibilité de faire le ménage. C'est une différence clé dans le débat `kill vs terminate` ; `SIGKILL` est une terminaison inconditionnelle, tandis que `SIGTERM` est une demande polie.

### Comprendre les autres signaux courants

Bien que `SIGTERM` et `SIGKILL` soient les plus courants, d'autres signaux sont également utiles pour la gestion des processus.

- **SIGHUP** : Le signal `kill sighup` (Hangup, signal 1) est traditionnellement envoyé à un processus lorsque son terminal de contrôle est fermé. Il peut être utilisé pour indiquer aux processus démons de recharger leurs fichiers de configuration.
- **SIGINT** : Le signal d'interruption (signal 2) est envoyé lorsque vous appuyez sur `Ctrl-C`. Il demande au processus d'interrompre son opération en cours.
- **SIGSTOP** : Ce signal (signal 19) met un processus en pause sans le terminer. Le processus peut être repris plus tard avec le signal `SIGCONT`.

### Vérifier l'existence du processus avec kill -0

Un cas d'utilisation spécial est `linux kill -0`. Cette commande n'envoie pas réellement de signal mais vérifie si un processus avec le PID spécifié existe et si vous avez l'autorisation de lui envoyer un signal.

```bash
kill -0 12445
```

Si la commande s'exécute avec succès (code de sortie 0), le processus existe. Si elle échoue, le processus n'existe pas ou vous n'avez pas les autorisations nécessaires.

## Exercise

Pour appliquer ce que vous avez appris, essayez ce laboratoire pratique pour renforcer votre compréhension de la gestion et de la terminaison des processus :

1.  **[Gérer et Surveiller les Processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Dans ce laboratoire, vous apprendrez les compétences essentielles pour gérer et surveiller les processus sur un système Linux. Vous explorerez comment interagir avec les processus au premier plan et en arrière-plan, les inspecter avec `ps`, surveiller les ressources avec `top`, ajuster la priorité avec `renice`, et les terminer avec `kill`.

Ce laboratoire vous aidera à appliquer les concepts de contrôle et de terminaison des processus dans des scénarios réels et à gagner en confiance dans la gestion des processus Linux.

## Quiz Question

Quel est le nom du signal pour la commande `kill` par défaut ? Veuillez répondre en anglais. Notez que la réponse est sensible à la casse.

## Quiz Answer

SIGTERM
