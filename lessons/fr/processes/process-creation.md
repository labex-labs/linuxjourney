---
index: 4
lang: "fr"
title: "Création de Processus"
meta_title: "Création de Processus - Processus"
meta_description: "Explorez les fondamentaux de la création de processus sous Linux. Ce guide couvre les appels système fork et execve, les relations parent/enfant (PID et PPID), et le rôle du processus init. Apprenez à créer un processus sous Linux et comprenez les concepts clés de la création de processus dans le système d'exploitation."
meta_keywords: "création de processus linux, création processus linux, créer un processus linux, création processus système d'exploitation, création de processus, fork, execve, PID, PPID, processus init, processus Linux"
---

## Lesson Content

Cette leçon explore les concepts fondamentaux de la manière dont les nouveaux processus sont démarrés sur un système Linux. Comprendre ce mécanisme donne un aperçu du fonctionnement interne du système d'exploitation.

### Le Modèle Fork et Exec

Le mécanisme principal pour la **création de processus sous Linux** implique qu'un processus existant se clone à l'aide de l'appel système `fork`. L'appel `fork` crée un processus enfant presque identique. Ce nouveau processus enfant reçoit son propre identifiant de processus (PID) unique, tandis que le processus d'origine devient son parent, identifié par un identifiant de processus parent (**PPID**).

Après le fork, le processus enfant peut soit continuer à exécuter le même programme que son parent, soit, plus couramment, utiliser l'appel système `execve` pour charger et exécuter un nouveau programme. L'appel `execve` remplace effectivement l'espace mémoire du processus par celui du nouveau programme, permettant à une tâche différente de commencer. Ce modèle en deux étapes "fork-exec" est une pierre angulaire de la manière dont vous **créez un processus sous Linux**.

### Observation des Relations Parent-Enfant

Nous pouvons observer cette relation parent-enfant en action en utilisant la commande `ps` :

```bash
ps l
```

L'option `l` fournit une vue au "format long", montrant plus de détails sur les processus en cours d'exécution. Vous verrez une colonne intitulée **PPID**, qui signifie Parent Process ID (Identifiant du Processus Parent). Regardez le processus de votre shell actuel (par exemple, `bash`). Lorsque vous exécutez la commande `ps l`, vous remarquerez que le **PID** de votre processus shell correspond au **PPID** du processus `ps l`. C'est parce que votre shell s'est forké pour créer le processus `ps`.

### Le Processus Init

Si chaque processus est l'enfant d'un autre, il doit y avoir un ancêtre original. C'est le processus `init`. Lorsque le système démarre, le noyau crée `init` comme tout premier processus de l'espace utilisateur, lui attribuant un PID de 1. Le processus `init` est le parent ultime de tous les autres processus et s'exécute avec les privilèges root pour gérer le système. Il ne peut pas être terminé tant que le système n'est pas éteint et est responsable du lancement de nombreux services qui maintiennent le système en fonctionnement.

## Exercise

La pratique rend parfait ! Voici un laboratoire pratique pour renforcer votre compréhension des processus Linux et de leur gestion :

- **[Gérer et Surveiller les Processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Dans ce laboratoire, vous apprendrez les compétences essentielles pour gérer et surveiller les processus sur un système Linux. Vous explorerez comment interagir avec les processus au premier plan et en arrière-plan, les inspecter avec `ps`, surveiller les ressources avec `top`, ajuster la priorité avec `renice` et les terminer avec `kill`.

Ce laboratoire vous aidera à appliquer les concepts d'identifiants de processus, d'identifiants de processus parent et de surveillance des processus dans un scénario réel et à renforcer votre confiance dans la gestion des processus.

## Quiz Question

Quel appel système crée un nouveau processus ? (Veuillez répondre en un seul mot anglais en minuscules.)

## Quiz Answer

fork
