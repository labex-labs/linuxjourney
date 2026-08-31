---
lesson_id: "proc-filesystem"
course_id: "processes"
lang: "fr"
order_index: 10
title: "Système de fichiers /proc"
description: "Découvrez comment Linux expose les informations actives des processus et du noyau par le système de fichiers virtuel `/proc`."
meta_title: "Système de fichiers /proc - Processus"
meta_description: "Découvrez le système de fichiers virtuel /proc de Linux, qui fournit une vue du noyau et des processus en cours d’exécution."
meta_keywords: "système fichiers /proc, proc Linux, informations processus, détails proc Linux, tableau système, processus Linux, informations noyau"
---

Linux monte couramment `procfs` sur `/proc`. Ce système de fichiers virtuel présente les interfaces produites par le noyau sous forme de fichiers et de répertoires ; son contenu n’est pas constitué de fichiers persistants ordinaires enregistrés sur disque. Il expose l’état des processus ainsi que certaines informations du noyau à l’échelle du système.

## Trouver les répertoires des processus

Affichez le montage et les entrées de premier niveau avec :

```bash
$ findmnt /proc
$ ls /proc
```

Les noms de répertoires numériques correspondent aux identifiants de processus visibles dans l’espace de noms de PID de l’appelant. Par exemple, `/proc/12345` représente le PID 12345 à l’instant où il existe. `/proc/self` est un lien symbolique qui se résout vers le propre répertoire du processus observateur, et `/proc/thread-self` identifie le thread actuel.

La visibilité et l’accès dépendent des identifiants, des espaces de noms, de la politique de sécurité et des options de montage de procfs telles que `hidepid`. Un processus peut se terminer entre la liste d’un répertoire et l’ouverture de l’un de ses fichiers ; cette disparition est une condition de concurrence normale que les outils d’examen doivent gérer.

:::single-choice{#proc-filesystem-numeric-directory}
Que représente normalement le répertoire numérique `/proc/12345` ?

::option[Le bloc de disque numéro 12345.]{#proc-filesystem-disk-block explanation="`/proc` est une interface virtuelle du noyau, et non un répertoire de blocs bruts du disque."}
::option[Le processus actuellement visible dont le PID vaut 12345.]{#proc-filesystem-pid-directory .correct explanation="Les données procfs propres à un processus sont regroupées sous un répertoire portant le PID visible."}
::option[Le compte utilisateur dont l’UID vaut 12345.]{#proc-filesystem-user-directory explanation="Les répertoires numériques de processus au premier niveau sont indexés par PID, et non par UID."}
:::

## Lire les informations d’un processus

Examinez le fichier d’état d’un processus lorsque les permissions le permettent :

```bash
$ less /proc/12345/status
```

Il contient des champs tels que le nom du processus, son état, ses identifiants, ses compteurs mémoire, ses capacités et ses masques de signaux. Parmi les autres entrées utiles figurent :

- `/proc/12345/cmdline` : arguments de la ligne de commande séparés par des octets nuls ;
- `/proc/12345/environ` : entrées de l’environnement, soumises au contrôle d’accès et potentiellement sensibles ;
- `/proc/12345/fd/` : liens symboliques représentant les descripteurs de fichiers ouverts ;
- `/proc/12345/maps` : mappages mémoire actuels ;
- `/proc/12345/cwd` : lien symbolique vers le répertoire de travail actuel.

Considérez-les comme des observations évolutives. Les champs peuvent varier selon la version du noyau, un processus peut changer d’état pendant la lecture de plusieurs fichiers, et certains compteurs possèdent des subtilités que leur seul nom ne révèle pas.

:::single-choice{#proc-filesystem-status-file}
Quel chemin contient un résumé lisible et organisé en champs pour le PID 12345 ?

::option[`/proc/status/12345`]{#proc-filesystem-status-reversed explanation="Les fichiers propres au processus se trouvent dans le répertoire nommé par le PID, et non sous un répertoire `status` de premier niveau."}
::option[`/proc/12345/status`]{#proc-filesystem-process-status .correct explanation="L’interface `status` du processus présente ses identifiants, son état, sa mémoire, ses signaux et ses champs d’identification."}
::option[`/proc/cpuinfo/12345`]{#proc-filesystem-cpuinfo-pid explanation="`/proc/cpuinfo` est une interface à l’échelle du système et non un répertoire de fichiers d’état par PID."}
:::

## Lire les interfaces à l’échelle du système

Toutes les entrées de `/proc` n’appartiennent pas à un processus. Citons notamment :

- `/proc/cpuinfo` pour les informations sur le processeur indiquées par le noyau ;
- `/proc/meminfo` pour les compteurs de mémoire du système ;
- `/proc/mounts` pour la vue des montages du processus actuel ;
- `/proc/loadavg` pour la charge moyenne et les informations sur les tâches exécutables ;
- `/proc/sys/` pour les paramètres du noyau à l’exécution.

Certains fichiers, surtout sous `/proc/sys`, sont des interfaces de configuration accessibles en écriture. N’y écrivez pas simplement parce qu’ils ressemblent à des fichiers ordinaires. Comprenez le paramètre, sa portée, son mécanisme de persistance et le retour en arrière avant d’apporter une modification système autorisée.

:::single-choice{#proc-filesystem-system-interface}
Quelle entrée fournit des compteurs mémoire à l’échelle du système plutôt que l’état d’un processus ?

::option[`/proc/self/status`]{#proc-filesystem-self-status explanation="Ce chemin se résout vers l’état propre au processus observateur."}
::option[`/proc/meminfo`]{#proc-filesystem-memory-info .correct explanation="`meminfo` contient les statistiques de mémoire du système indiquées par le noyau."}
::option[`/proc/1/fd`]{#proc-filesystem-one-fd explanation="Ce répertoire représente les descripteurs de fichiers du PID 1, sous réserve des contrôles d’accès."}
:::

## Employer `/proc` par l’intermédiaire d’outils

Les implémentations Linux d’outils tels que `ps`, `top` et `free` obtiennent une grande partie de leurs données depuis procfs et d’autres interfaces du noyau, puis les étiquettent, les calculent et les mettent en forme. Préférez ces outils pour le travail courant lorsqu’ils fournissent le champ nécessaire ; ne lisez directement `/proc` pour des détails précis ou des scripts qu’après avoir étudié la documentation de l’interface.

Les lecteurs directs doivent analyser correctement les formats, tolérer les processus disparus, protéger les sorties sensibles et ne pas supposer qu’une lecture constitue un instantané atomique du système.

:::single-choice{#proc-filesystem-live-data}
Pourquoi `/proc/PID` peut-il disparaître entre deux commandes d’examen ?

::option[Chaque fichier procfs est automatiquement renommé une fois par seconde.]{#proc-filesystem-renamed explanation="Il n’existe aucune règle de renommage périodique de toutes les entrées procfs."}
::option[La lecture de `status` supprime le répertoire du processus.]{#proc-filesystem-read-delete explanation="L’examen de l’état se fait en lecture seule et ne termine ni ne supprime le processus."}
::option[Le processus peut se terminer pendant son observation.]{#proc-filesystem-process-exit .correct explanation="Procfs reflète l’état actif ; le noyau retire donc le répertoire d’un processus après sa disparition."}
:::

## Résumé

Vous savez maintenant employer procfs comme une interface active et soumise au contrôle d’accès du noyau.

1. Associer les répertoires numériques de `/proc` aux PID visibles.
2. Lire certains fichiers de processus tout en tenant compte des conditions de concurrence et de leur sensibilité.
3. Distinguer les répertoires de processus des interfaces à l’échelle du système.
4. Préférer les outils et formats documentés pour les examens courants fiables.
