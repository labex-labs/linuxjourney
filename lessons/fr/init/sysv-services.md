---
lesson_id: "sysv-services"
course_id: "init"
lang: "fr"
order_index: 2
title: "Service System V"
description: "Découvrez comment examiner et piloter les anciens scripts de services SysV au moyen de l'enveloppe prise en charge par le système actif."
meta_title: "Service System V - Init"
meta_description: "Apprenez à gérer les services traditionnels System V sous Linux avec la commande service : afficher, démarrer, arrêter et redémarrer."
meta_keywords: "System V, SysV init, services Linux, commande service, démarrer service, arrêter service, redémarrer service"
---

Les services SysV sont généralement représentés par des scripts exécutables sous `/etc/init.d/`. Selon son implémentation et les conventions de la distribution, un script accepte des actions comme `start`, `stop`, `restart` ou `status`. La commande `service` fournit une enveloppe qui exécute un script nommé dans un environnement plus contrôlé.

## Découvrir les services et leurs actions

Commencez par répertorier les noms des scripts :

```bash
$ ls -1 /etc/init.d/
```

Certaines implémentations proposent :

```bash
$ service --status-all
```

Ses marqueurs entre crochets et états de fin sont propres à l'enveloppe, et un script peut signaler un état inconnu. Pour un service précis, examinez l'aide du script ou sa documentation au lieu de supposer que chaque action existe.

:::single-choice{#sysv-services-wrapper-purpose} Qu'enveloppe couramment la commande `service` ?

::option[Un éditeur de partitions exécuté sur chaque fichier de service.]{#sysv-services-partition-editor explanation="Le contrôle des services est sans rapport avec le partitionnement du stockage."}
::option[Un appel système du noyau ajouté dynamiquement par le script.]{#sysv-services-new-syscall explanation="Les scripts init sont des programmes de contrôle des processus dans l'espace utilisateur."}
::option[Un script init nommé et l'une des actions qu'il prend en charge.]{#sysv-services-script-action .correct explanation="L'enveloppe trouve un ancien script de service et l'appelle dans un environnement normalisé."}
:::

## Démarrer et arrêter

Sur un véritable hôte géré par SysV, les formes suivantes sont courantes :

```bash
$ sudo service NOM_DU_SERVICE start
$ sudo service NOM_DU_SERVICE stop
```

Ne remplacez le paramètre fictif qu'après avoir identifié le service, ses dépendants, son état actuel et l'impact opérationnel. Arrêter le réseau, l'accès distant, le stockage ou l'authentification depuis une session distante peut vous exclure du système ou corrompre un travail actif.

La forme directe `/etc/init.d/NOM_DU_SERVICE ACTION` peut exister, mais sur un hôte dont le gestionnaire actif fournit une compatibilité, employez la commande tournée vers ce gestionnaire afin qu'il puisse suivre l'état et les dépendances.

:::single-choice{#sysv-services-stop-peanut} Quelle commande demande l'arrêt du service SysV `peanut` ?

::option[`sudo service stop peanut`]{#sysv-services-stop-first explanation="L'ordre conventionnel des opérandes place le nom du service avant l'action."}
::option[`sudo stop --partition peanut`]{#sysv-services-partition-stop explanation="Cette syntaxe n'est pas celle de l'enveloppe des services SysV."}
::option[`sudo service peanut stop`]{#sysv-services-peanut-stop .correct explanation="L'enveloppe reçoit le nom du service, puis l'action d'arrêt demandée."}
:::

## Rechargement, redémarrage et état

`restart` arrête normalement le service puis le démarre, ce qui provoque une interruption. `reload` peut demander au service de relire sa configuration sans redémarrage complet, mais seulement si le script et le démon le prennent en charge. Certains scripts proposent `force-reload`, avec un comportement de repli défini par la distribution.

Validez la configuration avant tout rechargement ou redémarrage, conservez une deuxième connexion d'administration pour les changements d'accès distant et vérifiez ensuite le véritable point d'accès et les journaux du service, pas seulement un état « running ».

```bash
$ sudo service NOM_DU_SERVICE status
$ sudo service NOM_DU_SERVICE reload
```

:::single-choice{#sysv-services-reload-versus-restart} Pourquoi ne faut-il pas supposer que `reload` équivaut à `restart` ?

::option[Reload arrête toujours tout le système d'exploitation.]{#sysv-services-reload-shutdown explanation="Ce n'est pas le sens normal d'une action de rechargement d'un service."}
::option[Restart se contente d'afficher la configuration sans modifier l'état du processus.]{#sysv-services-restart-readonly explanation="Restart arrête et redémarre généralement le service."}
::option[Reload est propre au service et peut relire sa configuration sans arrêter le processus.]{#sysv-services-reload-specific .correct explanation="La prise en charge et la sémantique appartiennent au script et au démon, tandis que restart provoque normalement une interruption du cycle de vie."}
:::

## Contrôle à l'exécution et activation au démarrage

Démarrer un service maintenant ne l'active pas forcément pour les futurs niveaux d'exécution. L'activation au démarrage est représentée par les liens de niveaux et gérée avec des outils propres à la distribution, comme `update-rc.d`, `chkconfig` ou les générateurs de compatibilité du gestionnaire de services.

Ne créez pas manuellement les liens `S` et `K` tant que vous ne comprenez pas les métadonnées de dépendances et l'outil de gestion de la distribution ; ces liens peuvent être écrasés ou mal ordonnés.

:::single-choice{#sysv-services-start-versus-enable} `service SERVICE start` active-t-il nécessairement le service lors des futurs démarrages ?

::option[Oui ; chaque action start crée automatiquement tous les liens de niveaux.]{#sysv-services-start-links explanation="L'enveloppe ne modifie pas universellement l'activation persistante."}
::option[Non ; l'état d'exécution et l'activation dans les niveaux sont distincts.]{#sysv-services-runtime-separate .correct explanation="Les liens de démarrage ou les règles du gestionnaire déterminent l'activation future indépendamment du lancement actuel du processus."}
::option[Oui ; le PID actif est stocké définitivement dans le secteur de démarrage.]{#sysv-services-pid-boot-sector explanation="Les PID sont des identifiants d'exécution, pas des métadonnées d'activation au démarrage."}
:::

## Résumé

Vous savez maintenant piloter un ancien service sans confondre le contrôle d'exécution et les règles de démarrage.

1. Découvrir le script réel et les actions qu'il prend en charge.
2. Placer le nom du service avant l'action dans la syntaxe de l'enveloppe.
3. Valider et vérifier le comportement du rechargement ou du redémarrage.
4. Gérer l'activation dans les futurs niveaux au moyen des outils de la distribution.
