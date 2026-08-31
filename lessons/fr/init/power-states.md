---
lesson_id: "power-states"
course_id: "init"
lang: "fr"
order_index: 7
title: "États d'alimentation"
description: "Découvrez comment planifier, annuler et vérifier sans risque les opérations d'arrêt et de redémarrage de Linux."
meta_title: "États d'alimentation - Init"
meta_description: "Apprenez à gérer les états d'alimentation Linux avec les commandes shutdown, reboot, halt et poweroff, en toute sécurité."
meta_keywords: "états alimentation Linux, commande shutdown, commande reboot, halt, poweroff Linux, redémarrer Linux, administration système"
---

L'arrêt ou le redémarrage modifie la disponibilité de tout le système. Avant d'agir, confirmez l'hôte cible, obtenez l'autorisation, prévenez les utilisateurs connectés et assurez-vous que les écritures importantes, sauvegardes et tâches de maintenance peuvent se terminer. Sur un système distant, conservez une console ou une voie de récupération indépendante au cas où la machine ne reviendrait pas.

## Mettre hors tension sans risque

Sur une distribution fondée sur systemd, demandez une mise hors tension ordonnée avec :

```bash
$ sudo systemctl poweroff
```

L'interface traditionnelle `shutdown` est également très répandue :

```bash
$ sudo shutdown -h now
```

Un arrêt ordonné demande aux services de s'arrêter, démonte les systèmes de fichiers, puis change l'état d'alimentation de la machine. Ne considérez pas le redémarrage forcé ou l'interrupteur physique comme des raccourcis ordinaires : ils peuvent interrompre les écritures et laisser les données ou services incohérents.

:::single-choice{#power-states-orderly-poweroff}
Que faut-il faire avant de mettre hors tension un hôte de production distant ?

::option[Déconnecter sa console de gestion avant d'exécuter la commande.]{#power-states-remove-console explanation="Une console de gestion constitue un accès de récupération utile et doit rester disponible."}
::option[Forcer l'arrêt afin que les services ne puissent pas le retarder.]{#power-states-force-first explanation="Une opération forcée peut interrompre des écritures et ne doit pas être la méthode normale."}
::option[Confirmer l'hôte et préserver une voie d'accès pour la récupération.]{#power-states-confirm-and-recover .correct explanation="La confirmation évite d'agir sur le mauvais hôte, tandis que l'accès de récupération aide s'il ne revient pas."}
:::

## Planifier et annuler un arrêt

Accordez aux utilisateurs et aux charges le temps de se préparer en planifiant l'opération. La forme `+m` désigne un nombre de minutes à partir de maintenant :

```bash
$ sudo shutdown -h +4
```

Cette commande planifie un arrêt ou une mise hors tension dans quatre minutes et envoie des avertissements aux utilisateurs connectés. Si la maintenance est reportée, annulez l'arrêt en attente avant son échéance :

```bash
$ sudo shutdown -c
```

Ne supposez pas qu'un avertissement rend l'opération sûre. Vérifiez les sessions actives et les charges propres au système, puis suivez la procédure documentée de drainage du service ou de la grappe lorsqu'elle existe.

:::single-choice{#power-states-four-minute-schedule}
Quelle commande planifie un arrêt dans quatre minutes ?

::option[`sudo shutdown -h +4`]{#power-states-relative-four .correct explanation="L'action `-h` associée à `+4` demande un arrêt dans quatre minutes."}
::option[`sudo shutdown -h 4`]{#power-states-absolute-four explanation="Sans le signe plus, l'argument de temps n'est pas la forme documentée des minutes relatives."}
::option[`sudo shutdown -c +4`]{#power-states-cancel-four explanation="L'option `-c` annule un arrêt en attente au lieu d'en créer un."}
:::

## Redémarrer le système

Employez un redémarrage ordonné lorsque la machine doit s'arrêter puis repartir :

```bash
$ sudo systemctl reboot
```

Parmi les commandes de compatibilité équivalentes courantes :

```bash
$ sudo shutdown -r now
$ sudo reboot
```

Avant le redémarrage, vérifiez que les disques chiffrés, la configuration d'amorçage, le réseau et les services nécessaires peuvent revenir sans la session interactive actuelle. Coordonnez d'abord le basculement ou la migration des charges lorsque d'autres systèmes dépendent de l'hôte.

:::single-choice{#power-states-reboot-action}
Quelle commande demande un redémarrage ordonné immédiat au moyen de `shutdown` ?

::option[`sudo shutdown -c now`]{#power-states-cancel-now explanation="L'option `-c` annule un arrêt en attente."}
::option[`sudo shutdown -r now`]{#power-states-reboot-now .correct explanation="L'option `-r` sélectionne le redémarrage et `now` le planifie immédiatement."}
::option[`sudo shutdown -h now`]{#power-states-halt-now explanation="L'action `-h` arrête ou met hors tension au lieu de redémarrer."}
:::

## Distinguer l'arrêt de la mise hors tension

`halt`, `poweroff` et `reboot` peuvent être des interfaces de compatibilité vers le système d'initialisation, mais leurs états finaux demandés diffèrent. Un arrêt met fin au fonctionnement normal ; selon la plateforme et l'implémentation, l'alimentation peut rester fournie. Une mise hors tension demande en plus au matériel pris en charge de couper l'alimentation. Préférez la commande qui nomme le résultat voulu et consultez le manuel local, car le comportement de compatibilité peut varier.

:::single-choice{#power-states-halt-versus-poweroff}
Pourquoi faut-il distinguer `halt` de `poweroff` ?

::option[Poweroff demande la coupure de l'alimentation, tandis que halt peut la laisser fournie.]{#power-states-power-distinction .correct explanation="L'état matériel final demandé peut différer même si les deux mettent fin au fonctionnement normal."}
::option[Halt redémarre toujours les services après les avoir arrêtés.]{#power-states-halt-restarts explanation="Halt est un état d'arrêt, pas une demande de redémarrage des services."}
::option[Poweroff ne fait que déconnecter l'utilisateur actuel du terminal.]{#power-states-power-logout explanation="Poweroff est une transition d'état à l'échelle du système, pas une déconnexion du shell."}
:::

## Vérifier le résultat

Pour une opération planifiée, confirmez que les utilisateurs ont reçu l'avis et que le travail essentiel est drainé. Après un redémarrage, vérifiez le noyau et l'état de démarrage attendus, les unités en échec, la santé des applications, les montages, l'accessibilité réseau et les journaux récents. Une connexion réussie ne prouve pas à elle seule que tout le service est rétabli.

```bash
$ uptime
$ systemctl --failed
$ journalctl -b -p warning
```

Ces commandes constituent des points de départ ; employez les contrôles de santé propres à la charge réelle.

:::single-choice{#power-states-post-reboot-check}
Quelle preuve démontre le mieux qu'une application redémarrée est disponible ?

::option[L'état du service, les journaux et son contrôle de santé réussissent tous.]{#power-states-health-evidence .correct explanation="Plusieurs contrôles système et applicatifs vérifient la charge plutôt que le seul accès à l'hôte."}
::option[Le voyant d'alimentation du châssis est allumé.]{#power-states-light-on explanation="L'alimentation du matériel n'établit pas la santé de l'application."}
::option[Un administrateur peut se connecter à un shell.]{#power-states-shell-open explanation="L'accès au shell ne prouve qu'une partie de la disponibilité du système."}
:::

## Résumé

Vous savez maintenant changer les états d'alimentation de Linux avec préparation, intention claire et vérification.

1. Confirmer la cible, l'impact, l'autorisation et la voie de récupération.
2. Employer des commandes ordonnées de mise hors tension ou de redémarrage pour les opérations normales.
3. Planifier un arrêt lorsque les utilisateurs et charges ont besoin d'un avertissement.
4. Annuler un arrêt en attente lorsque le plan de maintenance change.
5. Vérifier la santé du système et des applications après le retour de la machine.
