---
lesson_id: "sudo-events"
course_id: "security-logs"
lang: "fr"
order_index: 3
title: "Événements sudo"
description: "Apprenez à reconnaître quel compte a demandé une commande, sous quel compte elle devait s’exécuter et si elle a été autorisée."
meta_title: "Événements sudo - Journaux de sécurité"
meta_description: "Lisez les journaux sudo en distinguant le compte demandeur, le compte cible, la commande et la décision d’autorisation."
meta_keywords: "événements sudo, journaux sudo, autorisation sudo, compte cible, droits Linux"
---

Une personne peut ouvrir une session avec un compte ordinaire, puis avoir besoin de droits supplémentaires pour une tâche. Sur un système qui utilise `sudo`, elle peut demander à exécuter une commande sous un autre compte. L’entrée de journal peut indiquer quels droits ont été demandés et quelle décision le système a prise.

## Repérer les deux comptes

Les entrées simulées utilisent `account` pour le compte qui fait la demande et `target` pour celui sous lequel la commande doit s’exécuter. Le compte `root` dispose des droits d’administration. Une demande `sudo` peut aussi désigner un autre compte cible, comme `backup`.

```text
t=09:15:10Z source=sudo host=web-01 account=alex target=root
command=systemctl status nginx decision=allowed session=42
```

La deuxième ligne complète l’entrée. Ici, `alex` a demandé d’exécuter la commande en tant que `root`.

:::single-choice{#sudo-events-account-target} Dans une entrée qui indique `account=sam target=backup`, qui a demandé l’exécution de la commande et sous quel compte ?

::option[Backup a demandé de l’exécuter en tant que sam.]{#sudo-events-target-swapped explanation="Account indique le compte demandeur. Target donne l’identité sous laquelle la commande doit s’exécuter."}
::option[Sam a demandé de l’exécuter en tant que backup.]{#sudo-events-target-backup .correct explanation="Account est le compte demandeur. Target est le compte que la commande utiliserait."}
::option[Sam a demandé de l’exécuter en tant que root.]{#sudo-events-target-root explanation="Root est un compte cible possible. Cette entrée indique backup."}
:::

## Lire la commande demandée

Le champ `command` indique la commande qui fait l’objet de la demande. Dans l’exemple, `systemctl status nginx` demande l’état actuel du service web Nginx. Une autre entrée pourrait montrer `systemctl restart nginx`, une demande pour arrêter et redémarrer le service. Les deux commandes concernent le même service et demandent des actions différentes.

:::single-choice{#sudo-events-command-scope} Quelle demande vise à changer l’état du service web ?

::option[`systemctl restart nginx`]{#sudo-events-command-restart .correct explanation="Restart demande d’arrêter puis de redémarrer le service. Cette opération peut changer son état."}
::option[`systemctl status nginx`]{#sudo-events-command-status explanation="Status demande l’état du service sans demander de redémarrage."}
::option[Les deux demandes, car elles mentionnent nginx.]{#sudo-events-command-both explanation="Le nom de service est le même. Le verbe de la commande indique l’action demandée."}
:::

## Lire la décision

La **politique d’accès** est l’ensemble des règles que `sudo` applique pour décider si une demande est autorisée. Dans les exemples, `decision=allowed` indique que la politique a permis la demande. `decision=denied` indique que `sudo` l’a refusée.

```text
t=09:16:00Z source=sudo host=web-01 account=alex target=root
command=systemctl restart nginx decision=denied session=42
```

Une décision favorable renseigne sur le droit d’exécuter la commande. Pour connaître le résultat de la commande, cherchez l’entrée correspondante si le système en fournit une.

![Terminal LabEx avec des entrées sudo simulées montrant une consultation d’état autorisée et un redémarrage refusé](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/sudo-events/sudo-decisions.png)

Comparez les commandes demandées et les décisions dans ces deux entrées simulées.

:::single-choice{#sudo-events-denied-request} Qu’indique le deuxième exemple au sujet de la demande de redémarrage ?

::option[Sudo a refusé la demande de redémarrage.]{#sudo-events-denied-refused .correct explanation="La commande indique l’action demandée. Denied indique que l’autorisation a été refusée."}
::option[Le service a redémarré avec succès.]{#sudo-events-denied-success explanation="L’entrée montre un refus et ne confirme aucun redémarrage réussi."}
::option[La demande d’état précédente a également été refusée.]{#sudo-events-denied-earlier explanation="Chaque décision s’applique à sa propre demande. La première entrée indique allowed."}
:::

## Garder le compte de connexion en vue

Les deux exemples indiquent que `alex` a fait la demande et contiennent `session=42`. Ce nombre désigne la session, c’est-à-dire la période d’activité qui suit la connexion. Il aide à retrouver les entrées d’authentification autour de cet événement. Le compte cible de chaque exemple se rapporte à une commande précise. Lisez les champs du demandeur et du compte cible ensemble.

:::single-choice{#sudo-events-session-interpretation} Quel résumé correspond au premier exemple ?

::option[Root s’est connecté directement et a ouvert la session 42.]{#sudo-events-session-root-login explanation="C’est une entrée sudo. Le champ du compte cible ne décrit pas une autre connexion."}
::option[Alex a demandé les droits de root pour toutes les commandes de la session.]{#sudo-events-session-all-commands explanation="L’entrée nomme une commande. Elle ne s’étend pas à toutes celles de la session."}
::option[Alex a demandé d’exécuter une commande précise en tant que root dans la session 42.]{#sudo-events-session-one-command .correct explanation="Le compte demandeur, le compte cible, la commande et la session appuient cette affirmation."}
:::

## Résumé

Vous savez maintenant lire un journal sudo et distinguer l’autorisation du résultat de la commande.

1. Identifier le compte demandeur et le compte cible.
2. Utiliser le champ de commande pour décrire la demande précise.
3. Distinguer une demande autorisée d’une demande refusée.
4. Tenir compte de la session pour décrire la demande.
