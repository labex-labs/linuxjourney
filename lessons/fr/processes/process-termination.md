---
lesson_id: "process-termination"
course_id: "processes"
lang: "fr"
order_index: 5
title: "Fin des processus"
description: "Découvrez comment l’état de sortie, l’attente, les zombies et le changement de parent achèvent le cycle de vie des processus Linux."
meta_title: "Fin des processus - Processus"
meta_description: "Explorez la fin des processus Linux, l’appel système wait et les différences entre processus zombies et orphelins."
meta_keywords: "fin processus Linux, processus zombie, processus orphelin, zombie ou orphelin, tuer processus enfant Linux, appel système wait, _exit, gestion processus"
---

Un processus peut se terminer en revenant de sa fonction principale, en appelant une interface de sortie ou en étant terminé par un signal. Le noyau libère la plupart de ses ressources, mais la comptabilisation entre parent et enfant se poursuit jusqu’à ce que le parent recueille les informations de fin.

## État de sortie

Un programme qui se termine normalement fournit un état entier. Par convention, l’état `0` signifie la réussite et une valeur non nulle signale une forme d’échec ou un autre résultat. La signification exacte des valeurs non nulles appartient à l’interface du programme.

Dans un shell, examinez l’état du pipeline au premier plan le plus récent avec :

```bash
$ command
$ printf '%s\n' "$?"
```

Les shells exposent une plage d’états encodés limitée et représentent aussi la terminaison par un signal ; cette valeur n’est donc pas un dossier de diagnostic complet. Les programmes doivent documenter leurs propres codes de sortie.

:::single-choice{#process-termination-success-status}
Selon la convention Unix, quel état de sortie normal indique la réussite ?

::option[`1`]{#process-termination-status-one explanation="De nombreux programmes emploient `1` pour un échec général, même si la signification dépend de la commande."}
::option[`0`]{#process-termination-status-zero .correct explanation="Un état normal nul indique conventionnellement une exécution réussie."}
::option[`255`]{#process-termination-status-255 explanation="Cette valeur est non nulle et ne représente pas conventionnellement la réussite."}
:::

## Attendre et récupérer

Le noyau enregistre la manière dont un enfant s’est terminé et avertit son parent. Celui-ci emploie un membre de la famille d’appels système `wait()` pour récupérer ces informations. La collecte de cet enregistrement s’appelle la récupération.

L’attente peut également coordonner l’exécution : un shell attend une commande au premier plan avant d’afficher une nouvelle invite, mais peut différer l’attente d’une tâche en arrière-plan. Un parent de longue durée bien conçu doit récupérer ses enfants sans bloquer le travail sans rapport.

:::single-choice{#process-termination-wait-purpose}
Qu’est-ce qu’une opération d’attente réussie permet au parent de récupérer ?

::option[Les informations de fin de l’enfant.]{#process-termination-wait-status .correct explanation="La famille wait indique comment un enfant s’est arrêté ou terminé et récupère un enfant achevé."}
::option[Une copie de l’ancien espace d’adressage de l’enfant.]{#process-termination-wait-memory explanation="La majeure partie de la mémoire du processus a déjà été libérée et n’est pas rendue au parent par `wait()`."}
::option[La propriété de chaque fichier ouvert par l’enfant.]{#process-termination-wait-files explanation="L’attente ne transfère pas les métadonnées de propriété du système de fichiers."}
:::

## Processus zombies

Après la fin d’un enfant mais avant la récupération de son enregistrement, il apparaît comme un zombie, souvent avec l’état `Z` dans `ps`. Il ne s’exécute plus et ne conserve aucun espace d’adressage ordinaire, mais une entrée minimale de la table des processus et des informations comptables subsistent.

L’envoi d’un signal à un zombie ne peut pas le faire se terminer une seconde fois. Pour corriger une accumulation persistante, diagnostiquez le parent qui n’attend pas, redémarrez-le ou corrigez-le au moyen d’une procédure opérationnelle adaptée, ou permettez le rattachement à un processus qui récupérera le zombie. Un grand nombre de zombies peut épuiser les PID ou la capacité de la table des processus.

:::single-choice{#process-termination-zombie-definition}
Quelle description correspond à un processus zombie ?

::option[Un enfant en cours d’exécution dont le parent s’est déjà terminé.]{#process-termination-zombie-orphan explanation="Cela décrit un enfant orphelin, et non un état zombie."}
::option[Un enfant terminé dont l’enregistrement de fin n’a pas été récupéré.]{#process-termination-zombie-unreaped .correct explanation="Le processus a cessé de s’exécuter, mais le noyau conserve un état minimal pour son parent."}
::option[Un processus qui consomme du processeur dans une boucle non interruptible.]{#process-termination-zombie-cpu explanation="Un zombie n’exécute aucune instruction et ne consomme pas de temps processeur."}
:::

## Orphelins et changement de parent

Si un parent se termine tandis que son enfant continue, le noyau rattache cet enfant à un sous-récupérateur admissible ou au processus init de l’espace de noms de PID concerné. L’enfant peut être en cours d’exécution, en sommeil, arrêté ou devenir ensuite un zombie ; « orphelin » décrit la perte de la relation avec le parent d’origine plutôt qu’un état d’exécution.

Le processus adoptant devient responsable de la collecte de l’état de fin. Les gestionnaires de services et les environnements de conteneurs modernes rendent important de ne pas supposer que le nouveau parent est toujours le PID 1 de l’hôte.

:::single-choice{#process-termination-orphan-definition}
Que se passe-t-il lorsqu’un processus survit à son parent d’origine ?

::option[Il est rattaché à un sous-récupérateur admissible ou au processus init de l’espace de noms.]{#process-termination-orphan-reparented .correct explanation="Le noyau préserve une relation parentale valide en attribuant un processus adoptant."}
::option[Il devient immédiatement un zombie même s’il ne s’est pas terminé.]{#process-termination-orphan-zombie explanation="L’état zombie ne commence qu’après la fin de l’exécution et pendant l’attente de la collecte de l’état."}
::option[Il perd définitivement son PID et continue anonymement.]{#process-termination-orphan-no-pid explanation="Un orphelin actif conserve son identité de processus tandis que sa relation parentale change."}
:::

Utilisez l’atelier [Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864) pour observer les codes de sortie et les états des processus sans perturber une charge de production.

## Résumé

Vous savez maintenant distinguer la fin de l’exécution du nettoyage côté parent.

1. Interpréter zéro comme une réussite conventionnelle et les états non nuls selon la documentation du programme.
2. Employer l’attente pour recueillir les informations de fin d’un enfant.
3. Reconnaître un zombie comme terminé mais non récupéré.
4. Reconnaître un orphelin comme un enfant rattaché à un nouveau parent après la fin de son parent d’origine.
