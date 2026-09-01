---
lesson_id: "exit-command"
course_id: "command-line"
lang: "fr"
order_index: 19
title: "exit"
description: "Apprenez à quitter le shell actuel et à choisir l'état qu'il renvoie à son appelant."
meta_title: "exit - Ligne de commande"
meta_description: "Apprenez la commande Linux exit, comment fermer une session shell, la différence entre logout et exit, et le fonctionnement des codes de sortie."
meta_keywords: "commande exit, linux exit, commande logout, session shell, sortie terminal, code de sortie, bash exit"
---

Les shells peuvent être imbriqués : un terminal graphique lance un shell, une connexion SSH lance un shell distant, et un shell peut en démarrer un autre. En quitter un rend normalement le contrôle au programme qui a lancé ce shell.

## Quitter le shell actuel

La commande `exit` demande au shell actuel de se terminer :

```bash
$ exit
```

Si ce shell est le processus principal d'un onglet de terminal graphique, l'onglet peut se fermer selon les réglages du terminal. Dans une session SSH, quitter le shell distant vous ramène normalement au shell local. Si vous avez lancé un shell imbriqué, `exit` revient à son shell parent.

:::single-choice{#leave-current-shell} Vous avez lancé Bash depuis un autre shell et voulez maintenant revenir au shell parent. Quelle commande faut-il exécuter dans la session Bash imbriquée ?

::option[`clear`]{#clear-nested explanation="`clear` rafraîchit la zone visible du terminal, mais laisse le shell actuel en fonctionnement."}
::option[`exit`]{#exit-nested .correct explanation="`exit` termine le shell actuel et permet au shell parent de reprendre."}
::option[`history -c`]{#clear-nested-history explanation="Cette commande efface la liste d'historique Bash en mémoire ; elle ne termine pas le shell actuel."}
:::

## Renvoyer un état de terminaison

Un argument numérique facultatif fixe l'état renvoyé à l'appelant du shell :

```bash
$ exit 0
```

Par convention, `0` signifie la réussite, et une valeur différente de zéro représente un échec ou une autre condition définie par le programme. Si Bash ne reçoit aucun argument numérique, il se termine avec l'état de la dernière commande exécutée avant `exit`.

:::single-choice{#return-success-status} Quelle commande termine le shell actuel en signalant explicitement une réussite à son appelant ?

::option[`exit 0`]{#exit-zero .correct explanation="L'état `0` signale conventionnellement une exécution réussie à l'appelant."}
::option[`exit 1`]{#exit-one explanation="Un état différent de zéro indique conventionnellement un échec ou un autre résultat exceptionnel, pas une réussite."}
::option[`logout 0`]{#logout-zero explanation="`logout` de Bash s'adresse aux shells de connexion et n'emploie pas cette forme pour définir l'état demandé."}
:::

:::single-choice{#exit-without-number} Dans Bash, quel état `exit` renvoie-t-elle lorsqu'aucun nombre n'est fourni ?

::option[Elle renvoie toujours l'état de réussite `0`.]{#always-zero explanation="La convention de réussite n'oblige pas un `exit` sans argument à renvoyer zéro ; Bash conserve alors un état antérieur."}
::option[Elle renvoie toujours l'état d'échec `1`.]{#always-one explanation="Bash n'attribue pas l'état d'échec `1` à chaque `exit` sans argument ; la commande précédente détermine la valeur."}
::option[Elle renvoie l'état de terminaison de la commande précédente.]{#last-command-status .correct explanation="Sans argument numérique explicite, Bash se termine avec l'état de la commande la plus récente."}
:::

## Utiliser logout dans un shell de connexion

La commande intégrée `logout` de Bash quitte un shell de connexion :

```bash
$ logout
```

Dans un shell Bash qui n'est pas un shell de connexion, `logout` signale cette situation ; utilisez plutôt `exit`.

:::single-choice{#leave-login-shell} Quelle commande intégrée à Bash est spécialement destinée à quitter un shell de connexion ?

::option[`logout`]{#logout-login .correct explanation="Bash fournit `logout` pour terminer un shell de connexion."}
::option[`unalias`]{#unalias-login explanation="`unalias` supprime des définitions d'alias du shell actuel ; elle ne termine pas la session."}
::option[`source`]{#source-login explanation="`source` lit dans le shell actuel des commandes provenant d'un fichier ; elle ne termine pas ce shell."}
:::

## Utiliser Ctrl+D ou fermer un terminal

À une invite interactive vide, `Ctrl+D` fournit normalement le caractère de fin de fichier du terminal. Bash interprète généralement cette condition comme une demande de fermeture. Il ne s'agit pas d'un signal, et des réglages comme `ignoreeof` de Bash peuvent modifier le comportement.

Fermer une fenêtre de terminal graphique demande à l'application de fermer ses processus et peut affecter les tâches en cours. Préférez un `exit` ordonné lorsque c'est possible et vérifiez le travail actif avant de fermer une session.

## Résumé

Vous savez maintenant quitter le shell actuel et communiquer son état de terminaison.

1. Utiliser `exit` pour rendre le contrôle à l'appelant du shell.
2. Fournir `0` pour la réussite ou un état non nul défini dans les autres cas.
3. Comprendre l'état utilisé par un `exit` sans argument.
4. N'utiliser `logout` que dans un shell de connexion.
5. Reconnaître `Ctrl+D` comme une fin d'entrée plutôt qu'un signal.
