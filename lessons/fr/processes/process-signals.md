---
lesson_id: "process-signals"
course_id: "processes"
lang: "fr"
order_index: 6
title: "Signaux"
description: "Découvrez comment Linux produit, bloque, délivre et traite les signaux pour contrôler les processus et notifier des événements."
meta_title: "Signaux - Processus"
meta_description: "Explorez les signaux Linux pour la gestion des processus, notamment SIGTERM, SIGKILL et SIGINT, ainsi que leurs actions et leur traitement."
meta_keywords: "signaux Linux, signaux processus Linux, signal 15 Linux, code signal système, SIGKILL, SIGTERM, SIGINT, gestion processus"
---

Un signal est une notification asynchrone délivrée à un processus ou à un thread particulier. Les signaux signalent des événements et demandent des actions, mais ne transportent que peu d’informations par rapport aux mécanismes de communication interprocessus orientés données.

## Origine des signaux

Les signaux peuvent provenir de plusieurs sources :

- un terminal peut produire `SIGINT` pour `Ctrl-C` ou `SIGTSTP` pour `Ctrl-Z` et l’adresser au groupe de processus au premier plan ;
- le noyau peut produire un signal synchrone tel que `SIGSEGV` lorsqu’un thread effectue une référence mémoire invalide ;
- un processus peut envoyer un signal autorisé à un autre processus ou groupe de processus ;
- les minuteurs, les changements d’état des enfants et les raccrochages des terminaux peuvent produire d’autres signaux.

L’émetteur doit posséder les permissions appropriées, généralement fondées sur les identifiants ou les capacités. Les signaux sont donc une interface de contrôle médiée par le noyau, et non des messages sans restriction entre utilisateurs arbitraires.

:::single-choice{#process-signals-ctrl-c}
Quel signal un terminal produit-il normalement pour `Ctrl-C` ?

::option[`SIGTSTP`]{#process-signals-ctrl-c-tstp explanation="`SIGTSTP` est normalement associé au caractère de suspension du terminal tel que `Ctrl-Z`."}
::option[`SIGCONT`]{#process-signals-ctrl-c-cont explanation="`SIGCONT` reprend un processus arrêté au lieu de représenter une interruption au clavier."}
::option[`SIGINT`]{#process-signals-ctrl-c-int .correct explanation="Le caractère d’interruption du terminal produit normalement `SIGINT` pour le groupe de processus au premier plan."}
:::

## Dispositions et actions par défaut

La plupart des signaux possèdent une disposition à l’échelle du processus qui choisit l’une de trois réponses :

- effectuer l’action par défaut définie pour le signal ;
- ignorer le signal ;
- appeler un gestionnaire installé par l’utilisateur.

Les actions par défaut diffèrent : un signal peut terminer, terminer et créer un fichier core, arrêter, reprendre ou être ignoré. L’interception de `SIGTERM` peut permettre à un programme de commencer un arrêt ordonné, mais le gestionnaire doit respecter des règles strictes de sûreté asynchrone et le programme peut encore retarder ou refuser de se terminer.

Les noms de signaux sont plus portables et lisibles que leurs numéros. Même si les architectures Linux courantes emploient le numéro 15 pour `SIGTERM`, ne supposez pas que tous les numéros, hormis ceux garantis par la norme concernée, soient identiques partout. Employez `kill -l` pour examiner l’association locale.

:::single-choice{#process-signals-term-behavior}
Pourquoi un processus peut-il répondre proprement à `SIGTERM` ?

::option[Il peut installer un gestionnaire pour ce signal.]{#process-signals-term-handler .correct explanation="Contrairement à `SIGKILL`, `SIGTERM` peut être intercepté afin que le programme lance sa propre logique d’arrêt."}
::option[Le noyau enregistre toujours automatiquement chaque document ouvert.]{#process-signals-term-kernel-save explanation="Le nettoyage de l’application dépend de son code ; le noyau ne comprend pas et n’enregistre pas un état documentaire arbitraire."}
::option[`SIGTERM` ne peut pas provoquer de terminaison par défaut.]{#process-signals-term-no-default explanation="Son action par défaut est la terminaison lorsque le processus n’a pas modifié sa disposition."}
:::

## Signaux bloqués et en attente

Les threads possèdent des masques de signaux capables de bloquer temporairement la délivrance de certains signaux. Un signal bloqué qui a été produit reste en attente jusqu’à ce qu’il puisse être délivré, sous réserve des règles propres aux signaux standards et temps réel. Plusieurs signaux standards du même type peuvent fusionner plutôt que d’être mis en file une fois par occurrence.

Dans un processus multithread, un signal adressé au processus peut être délivré à un thread admissible qui ne le bloque pas ; un signal adressé à un thread vise celui qui est désigné. Une conception correcte des signaux exige donc davantage que de vérifier si « le processus l’a bloqué ».

:::single-choice{#process-signals-blocked-state}
Que se passe-t-il normalement lorsqu’un signal pouvant être bloqué est produit tandis que sa cible le bloque ?

::option[Il reste en attente jusqu’à ce que sa délivrance devienne possible.]{#process-signals-pending .correct explanation="Le blocage retarde le traitement ; le signal en attente peut être délivré après son déblocage."}
::option[Il est automatiquement converti en `SIGKILL`.]{#process-signals-convert-kill explanation="Le noyau ne transforme pas un signal ordinaire bloqué en signal impossible à intercepter."}
::option[Il modifie l’identifiant utilisateur du processus cible.]{#process-signals-change-uid explanation="Les masques de signaux influencent la délivrance et ne modifient pas les identifiants des processus."}
:::

## Signaux qui ne peuvent pas être traités

`SIGKILL` termine un processus et `SIGSTOP` l’arrête. Aucun des deux ne peut être intercepté, ignoré ou bloqué. Cela garantit au noyau le contrôle ultime, mais signifie aussi que `SIGKILL` ne laisse aucune possibilité de nettoyage à l’application.

Même `SIGKILL` peut ne pas faire disparaître immédiatement une tâche du point de vue d’un observateur. Une tâche peut attendre dans une opération non interruptible du noyau, puis son parent doit encore récupérer son état après sa terminaison.

:::single-choice{#process-signals-uncatchable-pair}
Quelle paire ne peut être ni interceptée, ni ignorée, ni bloquée ?

::option[`SIGKILL` et `SIGSTOP`]{#process-signals-kill-stop .correct explanation="Le noyau réserve ces deux signaux afin qu’un processus ne puisse pas annuler ou retarder leurs actions fondamentales."}
::option[`SIGINT` et `SIGTERM`]{#process-signals-int-term explanation="Tous deux peuvent posséder un gestionnaire installé par l’utilisateur et être bloqués."}
::option[`SIGHUP` et `SIGCONT`]{#process-signals-hup-cont explanation="Ces signaux possèdent une sémantique particulière, mais ne constituent pas la paire impossible à intercepter."}
:::

## Résumé

Vous savez maintenant expliquer les grandes étapes et les contraintes du traitement des signaux Linux.

1. Identifier les signaux produits par le terminal, le noyau et les processus.
2. Distinguer les actions par défaut, les signaux ignorés et les gestionnaires.
3. Relier le blocage à la délivrance en attente et aux masques des threads.
4. Se souvenir que `SIGKILL` et `SIGSTOP` ne peuvent pas être traités ni bloqués.
