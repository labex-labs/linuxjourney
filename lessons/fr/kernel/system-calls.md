---
lesson_id: "system-calls"
course_id: "kernel"
lang: "fr"
order_index: 3
title: "Appels système"
description: "Découvrez comment le code de l'espace utilisateur appelle les services du noyau Linux et comment examiner ces appels sans risque avec `strace`."
meta_title: "Appels système - Noyau"
meta_description: "Explorez les appels système Linux, leur passage entre espace utilisateur et noyau, leur ABI et leur observation avec strace."
meta_keywords: "appel système Linux, appels système, table syscall, mode noyau, mode utilisateur, strace, ABI syscall"
---

Un appel système est une entrée définie dans le noyau par laquelle le code de l'espace utilisateur demande une opération, par exemple ouvrir un fichier, mapper de la mémoire, créer un processus ou envoyer des données réseau. Le noyau valide les arguments, identifiants, états des objets et règles de sécurité avant d'effectuer la demande.

## Bibliothèques et ABI des appels système

Les applications appellent couramment des fonctions de la bibliothèque C plutôt que d'écrire des instructions d'entrée propres à une architecture. Une fonction d'enveloppe prépare les registres et la mémoire conformément à l'ABI des appels système, entre dans le noyau et traduit le résultat selon les conventions du langage.

La relation n'est pas toujours d'une fonction à un appel système :

- une fonction de bibliothèque peut combiner plusieurs appels système ;
- certaines fonctions agissent entièrement dans l'espace utilisateur ;
- une fonction vDSO optimisée peut obtenir certaines données entretenues par le noyau sans transition de mode complète ;
- un appel système peut prendre en charge de nombreuses API de plus haut niveau.

:::single-choice{#system-calls-library-wrapper}
Que fait une enveloppe d'appel système typique de libc ?

::option[Elle prépare les arguments de l'ABI, entre dans le noyau et traduit le résultat.]{#system-calls-wrapper-role .correct explanation="L'enveloppe masque les conventions d'appel propres à l'architecture derrière une interface de bibliothèque ordinaire."}
::option[Elle donne à l'application un accès illimité à la mémoire du noyau.]{#system-calls-wrapper-unrestricted explanation="L'entrée dans le noyau reste contrôlée et valide la demande."}
::option[Elle recompile le noyau à chaque appel de la fonction.]{#system-calls-wrapper-compile explanation="Un appel à l'exécution emploie le noyau déjà actif."}
:::

## Entrer dans le noyau et en revenir

L'enveloppe place un numéro d'appel système et ses arguments dans des emplacements définis par l'architecture, puis exécute une instruction d'entrée comme `syscall` sur x86-64 ou `svc` sur AArch64. Le processeur passe à un point d'entrée privilégié configuré et le noyau distribue la demande.

Après l'opération, le noyau renvoie une valeur ou l'indication d'une erreur. Les enveloppes de la bibliothèque C renvoient couramment `-1` et définissent la variable locale au thread `errno` en cas d'erreur. Les autres langages et environnements exposent différents types d'erreurs.

Décrire chaque entrée comme une « interruption logicielle » manque de précision sur les architectures actuelles ; les exceptions, instructions rapides d'appel système et appels superviseur mettent en œuvre des transitions contrôlées apparentées, mais différentes.

:::single-choice{#system-calls-entry-result}
Qui valide les arguments et l'autorisation d'un appel système ?

::option[L'invite du shell avant le démarrage du processus.]{#system-calls-shell-validates explanation="Un processus peut effectuer des appels système sans shell et les contrôles du noyau restent nécessaires."}
::option[L'implémentation du service demandé dans le noyau.]{#system-calls-kernel-validates .correct explanation="Le gestionnaire privilégié vérifie les pointeurs, l'état des objets, les identifiants et les règles avant d'agir."}
::option[La table de partitions du disque.]{#system-calls-partition-validates explanation="Les métadonnées d'organisation du stockage n'autorisent pas les services arbitraires du noyau."}
:::

## Numéros et compatibilité

Les numéros d'appels système et conventions d'appel sont propres à l'architecture. Un même appel symbolique peut posséder un numéro ou une organisation des structures différents dans une autre ABI. Les versions du noyau peuvent ajouter des appels, tandis que les ABI stables de l'espace utilisateur cherchent à préserver les comportements existants.

Un processus non privilégié ne peut pas insérer arbitrairement de nouveaux gestionnaires dans la table des appels du noyau actif. Étendre l'interface exige du code dans le noyau et une conception soigneuse de l'ABI. Des fonctions comme seccomp peuvent filtrer les appels autorisés à un processus, mais ne créent pas de nouvelles implémentations dans le noyau.

:::single-choice{#system-calls-number-portability}
Pourquoi une application doit-elle éviter de coder en dur les numéros d'appels système d'une autre architecture ?

::option[Les numéros et conventions d'appel sont propres à l'ABI.]{#system-calls-abi-specific .correct explanation="Un numéro qui désigne une opération sur une architecture peut en identifier une autre ou être absent ailleurs."}
::option[Les appels système sont nommés depuis le répertoire de travail actuel.]{#system-calls-directory-names explanation="Les chemins ne définissent pas l'ABI de numérotation des appels système."}
::option[Chaque processus reçoit une table aléatoire à son démarrage.]{#system-calls-random-table explanation="L'ABI du noyau actif est stable pour une architecture, pas aléatoire pour chaque processus."}
:::

## Traçage avec `strace`

Tracez une commande simple et enregistrez sa sortie séparément :

```bash
$ strace -o trace.log -- ls
```

Suivez les processus enfants lorsque vous y êtes autorisé avec `-f`, ou limitez la sortie au moyen d'une expression comme :

```bash
$ strace -f -e trace=%file -o trace.log -- command
```

`strace` peut révéler des chemins, arguments, données issues de l'environnement, adresses réseau, fragments du contenu des fichiers et identifiants incorrectement passés comme arguments. Conservez les traces avec des permissions restrictives et supprimez-les selon les règles relatives aux données d'incident.

:::single-choice{#system-calls-strace-purpose}
Qu'observe principalement `strace` ?

::option[Uniquement les lignes du code source exécutées dans l'application.]{#system-calls-strace-source-lines explanation="Le traçage au niveau du code source exige un débogueur ou une instrumentation avec des symboles."}
::option[Les appels système et signaux à la frontière entre utilisateur et noyau.]{#system-calls-strace-boundary .correct explanation="Il indique les demandes, arguments, résultats et événements de signaux des processus tracés."}
::option[La tension physique de chaque cœur du processeur.]{#system-calls-strace-voltage explanation="La télémétrie matérielle ne relève pas du traçage des appels système."}
:::

## Interpréter prudemment les traces

Le traçage modifie le déroulement temporel et peut imposer un surcoût important. Un appel qui échoue peut être une sonde attendue et l'erreur finale visible peut découler d'une opération antérieure ou d'une règle de l'application. Décodez les descripteurs de fichiers, suivez les relations entre processus et rapprochez les résultats des journaux applicatifs.

Les permissions et règles de sécurité ptrace limitent les processus qu'il est possible de tracer. Ne vous attachez pas au processus d'un autre utilisateur ou à un processus de production sans autorisation ; la suspension et les changements temporels peuvent modifier le comportement du service.

:::single-choice{#system-calls-strace-failure}
L'échec d'un seul appel système dans une trace signifie-t-il nécessairement que l'application est cassée ?

::option[Oui ; toute valeur de retour non nulle arrête immédiatement Linux.]{#system-calls-nonzero-terminates explanation="Les applications traitent couramment les erreurs d'appels système sans défaillance du système."}
::option[Non ; les programmes sondent souvent plusieurs possibilités et traitent des erreurs attendues.]{#system-calls-expected-failure .correct explanation="Interprétez le retour dans le contexte du flux de contrôle et de l'application plutôt qu'isolément."}
::option[Oui ; le noyau ne renvoie jamais d'erreurs attendues.]{#system-calls-no-expected-errors explanation="Les erreurs comme les chemins absents ou les opérations non prises en charge sont des résultats normaux de l'API."}
:::

## Résumé

Vous savez maintenant suivre un appel système depuis l'API de bibliothèque jusqu'au travail validé du noyau.

1. Distinguer les fonctions de haut niveau de l'ABI des appels système.
2. Relier les instructions d'entrée de l'architecture à la distribution contrôlée dans le noyau.
3. Considérer les numéros et structures d'appels comme propres à l'architecture.
4. Employer des sorties `strace` filtrées tout en protégeant les données sensibles.
5. Interpréter les échecs et le surcoût du traçage dans le contexte de l'application.
