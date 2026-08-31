---
lesson_id: "upstart-jobs"
course_id: "init"
lang: "fr"
order_index: 4
title: "Jobs Upstart"
description: "Découvrez comment examiner et piloter les jobs d'un ancien système Upstart confirmé avec `initctl`."
meta_title: "Jobs Upstart - Init"
meta_description: "Apprenez à gérer les services avec les jobs Upstart et initctl : afficher, démarrer, arrêter et redémarrer sous Linux."
meta_keywords: "jobs Upstart, initctl, Upstart Linux, services Linux, administration système, système init"
---

`initctl` communique avec un démon d'initialisation Upstart actif. Ne l'employez qu'après avoir confirmé que l'espace de noms de PID concerné exécute réellement Upstart ; sur un hôte systemd actuel, servez-vous plutôt des outils natifs de systemd.

## Répertorier les jobs et lire leur état

Affichez les jobs et instances connus :

```bash
$ initctl list
```

Examinez un job :

```bash
$ initctl status networking
networking start/running
```

Upstart indique à la fois un **objectif**, comme `start` ou `stop`, et un **état actuel**, comme `running` ou `waiting`. `stop/waiting` signifie que le job ne s'exécute pas et attend une condition de démarrage ou une demande manuelle ; cela ne signale pas nécessairement une erreur.

:::single-choice{#upstart-jobs-stop-waiting}
Que signifie normalement `stop/waiting` dans la sortie d'état d'Upstart ?

::option[Le job s'exécute, mais ne consomme aucun temps processeur.]{#upstart-jobs-running-idle explanation="Un job actif afficherait normalement un objectif start et l'état running."}
::option[L'objectif du job est l'arrêt et aucune instance de processus ne s'exécute.]{#upstart-jobs-stopped-waiting .correct explanation="La définition reste connue tandis qu'Upstart attend une future condition ou commande."}
::option[Tout le système d'exploitation attend sa mise hors tension.]{#upstart-jobs-system-poweroff explanation="Cette paire décrit l'instance du job, pas nécessairement l'état global du système."}
:::

## Démarrer et arrêter un job

Après avoir examiné les dépendances et l'impact :

```bash
$ sudo initctl start NOM_DU_JOB
$ sudo initctl stop NOM_DU_JOB
```

Les jobs peuvent définir plusieurs instances désignées par des variables d'environnement. Dans ce cas, fournissez les variables exactes qu'exige la configuration et incluez-les de façon cohérente lors de l'interrogation ou de l'arrêt d'une instance. Démarrer ou arrêter des jobs de réseau, stockage, authentification ou accès distant peut interrompre la session ; conservez donc une possibilité de récupération par la console.

:::single-choice{#upstart-jobs-start-command}
Quelle commande demande manuellement le démarrage du job `peanuts` ?

::option[`sudo initctl start peanuts`]{#upstart-jobs-start-peanuts .correct explanation="La sous-commande start est suivie du nom du job configuré et des éventuelles variables d'instance requises."}
::option[`sudo initctl peanuts start`]{#upstart-jobs-name-first explanation="La syntaxe d'initctl place la sous-commande avant le nom du job."}
::option[`sudo systemctl initctl peanuts`]{#upstart-jobs-systemctl-mixed explanation="Cette forme mélange incorrectement les interfaces de deux gestionnaires de services distincts."}
:::

## Redémarrage et changements de configuration

Demandez le redémarrage d'un job déjà actif avec :

```bash
$ sudo initctl restart peanuts
```

Dans Upstart, `restart` n'équivaut pas toujours à un nouvel enchaînement `stop` puis `start` après la modification d'un fichier de job : l'ancienne configuration du job en cours d'exécution peut continuer de faire autorité. Validez le fichier `.conf` modifié, demandez à Upstart de recharger la configuration selon la version installée, puis suivez la procédure documentée d'arrêt et de démarrage si la nouvelle configuration doit prendre effet.

Un redémarrage provoque une interruption et peut échouer à rétablir le service. Vérifiez ensuite son véritable point d'accès et ses journaux.

:::single-choice{#upstart-jobs-restart-peanuts}
Quelle commande demande le redémarrage du job Upstart actif `peanuts` ?

::option[`sudo initctl restart peanuts`]{#upstart-jobs-restart-command .correct explanation="La sous-commande restart agit sur le job nommé par l'intermédiaire de l'interface de contrôle Upstart."}
::option[`sudo initctl emit peanuts`]{#upstart-jobs-emit-not-restart explanation="L'émission d'un événement touche tous les jobs dont les conditions correspondent et ne constitue pas une demande directe de redémarrage."}
::option[`sudo service --status-all peanuts`]{#upstart-jobs-status-all explanation="Un affichage des états ne demande aucun redémarrage."}
:::

## Valider la configuration d'un job

Avant d'installer un fichier modifié, employez l'outil de validation fourni par l'ancienne distribution, souvent `init-checkconf`, et examinez les scripts inclus, l'environnement, les réglages d'utilisateur et de groupe, la politique de relance et les expressions d'événements. Rechargez ensuite les définitions au moyen de la méthode `initctl reload-configuration` adaptée à la version.

La validation syntaxique ne prouve ni l'existence des chemins, ni les autorisations d'exécution, ni l'arrivée des événements, ni l'état prêt du processus. Testez dans un environnement permettant la récupération.

:::single-choice{#upstart-jobs-syntax-validation-limit}
Que la validation syntaxique d'un job ne permet-elle pas de prouver ?

::option[Que le service démarrera correctement et deviendra disponible.]{#upstart-jobs-runtime-not-proven .correct explanation="Les chemins, permissions, dépendances et flux d'événements à l'exécution exigent un véritable test contrôlé."}
::option[Que le texte de configuration peut être analysé.]{#upstart-jobs-parse-purpose explanation="L'analyse constitue précisément le principal objectif de la validation syntaxique."}
::option[Qu'un fichier a été fourni au validateur.]{#upstart-jobs-file-supplied explanation="L'outil peut signaler immédiatement l'absence d'une entrée."}
:::

## Émettre des événements avec prudence

Upstart peut émettre un événement nommé :

```bash
$ sudo initctl emit NOM_DE_L_ÉVÉNEMENT
```

Chaque job dont l'expression de démarrage ou d'arrêt correspond peut réagir. Un événement ne s'adresse pas à un seul job, et ses effets peuvent se propager par d'autres événements. Examinez toutes les configurations correspondantes avant d'émettre un événement personnalisé ou système ; ne rejouez pas négligemment les événements centraux du démarrage sur une machine de production.

:::single-choice{#upstart-jobs-emit-scope}
Que peut-il se produire lorsque `initctl emit NOM_DE_L_ÉVÉNEMENT` s'exécute ?

::option[Toutes les expressions de jobs correspondant à l'événement peuvent effectuer une transition.]{#upstart-jobs-event-matches .correct explanation="Les événements sont diffusés dans le modèle de dépendances d'Upstart au lieu d'être envoyés à un seul service nommé."}
::option[Seul un job dont le nom est strictement identique à l'événement peut répondre.]{#upstart-jobs-event-name-only explanation="La correspondance dépend des expressions `start on` et `stop on`, pas de l'égalité avec le nom du job."}
::option[L'événement est conservé pour toujours comme message d'une file durable.]{#upstart-jobs-event-durable explanation="Les événements Upstart sont des notifications de cycle de vie, pas une file de messages durable générale."}
:::

## Résumé

Vous savez maintenant piloter les jobs Upstart avec une portée explicite des états et événements.

1. Lire séparément l'objectif et l'état dans la sortie d'`initctl`.
2. Démarrer et arrêter l'instance exacte après en avoir examiné l'impact.
3. Distinguer le redémarrage du changement de configuration du job.
4. Valider la syntaxe, puis tester la disponibilité à l'exécution.
5. Examiner toutes les correspondances avant d'émettre un événement.
