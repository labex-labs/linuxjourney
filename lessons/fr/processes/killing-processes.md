---
lesson_id: "killing-processes"
course_id: "processes"
lang: "fr"
order_index: 7
title: "kill (terminer)"
description: "Découvrez comment identifier un processus et lui envoyer un signal approprié avec `kill` selon une escalade sûre."
meta_title: "kill (terminer) - Processus"
meta_description: "Maîtrisez la commande kill sous Linux pour gérer et terminer les processus avec SIGTERM, SIGKILL, SIGHUP et une procédure sûre."
meta_keywords: "commande kill, kill SIGTERM, kill SIGHUP, kill -0 Linux, kill ou terminate, kill -15 Linux, SIGTERM, SIGKILL, gestion processus"
---

La commande `kill` envoie un signal à un processus ou à un groupe de processus. Son nom est historique : le signal demandé peut terminer, arrêter, reprendre ou déclencher une action définie par l’application. Confirmez toujours précisément la cible et comprenez le comportement documenté du programme envers le signal avant de l’envoyer.

## Demander une terminaison ordonnée

Avec un PID seul, `kill` envoie `SIGTERM` par défaut :

```bash
$ kill 12445
```

Préférez le nom symbolique lorsque vous précisez explicitement un signal :

```bash
$ kill -TERM 12445
```

L’action par défaut de `SIGTERM` est la terminaison, mais un programme peut l’intercepter ou l’ignorer. Un service bien conçu peut employer un gestionnaire pour cesser d’accepter du travail, enregistrer l’état approprié et libérer les ressources de l’application. Il s’agit d’une possibilité, pas d’une garantie de nettoyage immédiat ou réussi.

:::single-choice{#killing-processes-default-signal}
Quel signal `kill PID` demande-t-il par défaut ?

::option[`SIGKILL`]{#killing-processes-default-kill explanation="Le signal forcé impossible à intercepter doit être choisi explicitement."}
::option[`SIGTERM`]{#killing-processes-default-term .correct explanation="Sans autre opérande de signal, `kill` envoie la demande standard de terminaison."}
::option[`SIGSTOP`]{#killing-processes-default-stop explanation="L’arrêt d’un processus n’est pas l’action demandée par défaut par `kill`."}
:::

## Vérifier la cible

Les PID peuvent être réutilisés ; un PID périmé peut donc désigner ultérieurement un autre processus. Examinez la cible active immédiatement avant d’agir :

```bash
$ ps -p 12445 -o pid,ppid,user,lstart,stat,cmd
```

Vérifiez son utilisateur, son heure de démarrage, sa commande, son parent, son gestionnaire de service et son rôle opérationnel. Si un gestionnaire de services contrôle le processus, employez si possible sa commande d’arrêt ou de rechargement afin qu’il conserve un état correct et n’effectue pas immédiatement un redémarrage de l’enfant.

Vous pouvez envoyer des signaux aux processus que vous possédez, sous réserve des règles d’identifiants. L’envoi d’un signal au processus d’un autre utilisateur nécessite généralement les privilèges appropriés. N’employez pas de commande large fondée sur un nom avant d’avoir examiné chaque correspondance.

:::single-choice{#killing-processes-pid-reuse}
Pourquoi faut-il examiner un PID immédiatement avant de lui envoyer un signal ?

::option[Le PID change chaque fois que le processus lit un fichier.]{#killing-processes-pid-read explanation="Un processus actif conserve normalement le même PID pendant toute sa durée de vie."}
::option[Le noyau peut réutiliser un PID après la fin du processus précédent.]{#killing-processes-pid-reused .correct explanation="Un PID numérique mémorisé peut désigner ultérieurement un autre processus actif."}
::option[`kill` accepte les noms de commandes, mais pas les identifiants numériques.]{#killing-processes-no-numeric explanation="Un PID numérique est l’opérande cible ordinaire de `kill`."}
:::

## Vérifier la permission avec le signal zéro

Le signal numéro zéro effectue les contrôles d’erreurs sans délivrer de véritable signal :

```bash
$ kill -0 12445
```

Une réussite signifie qu’un processus possédant ce PID existe et que l’appelant est autorisé à lui envoyer un signal à cet instant. Un échec est ambigu : le processus peut ne pas exister ou l’appelant manquer de permission. Examinez l’erreur et l’état de sortie au lieu de traduire chaque échec par « ne s’exécute pas ». Ce contrôle n’est qu’instantané et ne supprime pas une éventuelle concurrence liée à la réutilisation ultérieure du PID.

:::single-choice{#killing-processes-signal-zero}
Qu’établit la réussite de `kill -0 PID` à cet instant ?

::option[Le processus a terminé tout son nettoyage et s’est arrêté.]{#killing-processes-zero-exited explanation="La réussite indique une cible active à laquelle un signal peut être envoyé, et non une terminaison achevée."}
::option[Le processus conservera définitivement ce PID.]{#killing-processes-zero-permanent explanation="Le contrôle est instantané et les PID peuvent être réutilisés après la fin."}
::option[Le processus existe et l’appelant peut lui envoyer un signal.]{#killing-processes-zero-permitted .correct explanation="Le signal zéro contrôle l’existence de la cible et l’autorisation sans délivrer un signal ordinaire."}
:::

## N’escalader que si nécessaire

Si une cible autorisée ne se termine pas après `SIGTERM`, accordez-lui un délai adapté à la charge et recherchez-en la cause. Si une terminaison forcée se justifie ensuite, envoyez :

```bash
$ kill -KILL 12445
```

`SIGKILL` ne peut être ni intercepté, ni ignoré, ni bloqué ; le programme ne peut donc effectuer aucun nettoyage applicatif. Il peut laisser des transactions incomplètes, un état temporaire ou du travail de récupération à d’autres composants. Employez-le comme escalade, et non comme première étape habituelle.

Les autres signaux n’ont de sens que selon le contrat du programme destinataire. `SIGHUP` demande souvent un rechargement de la configuration, mais certains programmes conservent son comportement par défaut de terminaison. `SIGSTOP` suspend sans nettoyage et `SIGCONT` reprend un processus arrêté.

:::single-choice{#killing-processes-kill-tradeoff}
Quel est le principal inconvénient opérationnel de `SIGKILL` ?

::option[Il ne peut être traité que par le propriétaire du processus.]{#killing-processes-kill-owner-handler explanation="Aucun processus cible ne peut installer de gestionnaire pour `SIGKILL`."}
::option[Il suspend le processus sans jamais le terminer.]{#killing-processes-kill-pauses explanation="`SIGSTOP` suspend ; `SIGKILL` termine."}
::option[Il ne laisse aucune possibilité de nettoyage applicatif au programme.]{#killing-processes-kill-no-cleanup .correct explanation="Le noyau impose la terminaison sans appeler de gestionnaire de signal dans l’espace utilisateur."}
:::

Entraînez-vous à choisir les signaux uniquement sur des processus que vous avez lancés dans un environnement isolé. L’atelier [Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864) fournit une procédure contrôlée pour l’examen et la terminaison.

## Résumé

Vous savez maintenant envoyer des signaux aux processus avec une procédure délibérée et vérifiable.

1. Confirmer la cible active et son superviseur avant d’agir.
2. Employer `SIGTERM` comme demande normale de terminaison.
3. Interpréter le signal zéro comme un contrôle instantané d’existence et de permission.
4. Réserver `SIGKILL` à une escalade justifiée après investigation.
