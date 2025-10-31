---
index: 5
lang: "fr"
title: "Terminaison de Processus"
meta_title: "Terminaison de Processus - Processus"
meta_description: "Explorez la terminaison des processus Linux, l'appel système wait, et les différences clés dans le débat processus zombie vs orphelin. Apprenez à gérer les états des processus enfants Linux pour un système stable."
meta_keywords: "Terminaison processus Linux, processus zombie, processus orphelin, zombie vs orphelin, tuer processus enfant linux, appel système wait, _exit, gestion des processus"
---

## Lesson Content

### Le Processus de Terminaison

Une fois qu'un processus est créé, comment se termine-t-il ? La terminaison d'un processus est une partie essentielle du cycle de vie du processus, garantissant que les ressources système sont gérées efficacement.

Un processus se termine généralement en appelant l'appel système `_exit`. Cette action signale au noyau que le processus est terminé et que ses ressources, telles que la mémoire et les descripteurs de fichiers, peuvent être récupérées. Lors de la sortie, le processus fournit un statut de terminaison au noyau, qui est une valeur entière. Par convention, un statut de 0 indique une exécution réussie, tandis qu'une valeur non nulle signale une erreur.

Cependant, appeler `_exit` n'efface pas immédiatement le processus. Le processus parent doit accuser réception de la terminaison de son enfant en utilisant l'appel système `wait`. Cet appel permet au parent de récupérer le statut de terminaison de l'enfant. Ce mécanisme en deux étapes est essentiel pour un nettoyage correct du processus. Une autre façon de `linux kill child process` (tuer un processus enfant sous Linux) est d'utiliser des signaux, un sujet que nous explorerons dans une leçon ultérieure.

### Processus Orphelins

Que se passe-t-il si un processus parent se termine avant son enfant ? L'enfant devient un processus "orphelin". Puisque son parent d'origine ne peut plus appeler `wait`, le noyau intervient. Le processus orphelin est immédiatement adopté par un processus système spécial, généralement `init` (ID de processus 1), qui est considéré comme l'ancêtre de tous les processus. Le processus `init` assume alors le rôle de parent, appelant périodiquement `wait` pour collecter le statut de terminaison de tous ses enfants adoptés, leur permettant de se terminer proprement.

### Processus Zombies

Un scénario différent se produit lorsqu'un processus enfant se termine, mais que son parent n'a pas encore appelé `wait`. Dans cet état, l'enfant devient un processus "zombie". Le noyau libère la plupart des ressources du zombie, mais il conserve une entrée dans la table des processus. Cette entrée contient l'ID du processus et le statut de terminaison, attendant que le parent le récupère.

Les processus zombies sont déjà morts, ils ne consomment donc pas de temps CPU. Vous ne pouvez pas les tuer avec des signaux car ils ne sont pas en cours d'exécution. Le processus par lequel le parent appelle `wait` pour nettoyer un zombie est appelé "récolte" (reaping). Si le processus parent se termine également, `init` adoptera et récoltera le zombie.

### Processus Zombie vs Orphelin

Comprendre la différence entre un `zombie vs orphan process` (processus zombie contre processus orphelin) est essentiel pour diagnostiquer les problèmes liés aux processus.

- Un **processus orphelin** est un processus actif, en cours d'exécution, dont le parent est décédé. Il est adopté par `init` et continue de s'exécuter jusqu'à sa fin.
- Un **processus zombie** est un processus mort qui a terminé son exécution mais qui possède toujours une entrée dans la table des processus. Il attend que son processus parent lise son statut de sortie.

En bref, un orphelin est vivant mais sans parent, tandis qu'un zombie est mort mais pas encore entièrement récolté par son parent.

## Exercise

Pour appliquer ces concepts, essayez le laboratoire pratique suivant :

1. **[Gérer et Surveiller les Processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir avec les processus de premier plan et d'arrière-plan, à les inspecter avec `ps`, à surveiller les ressources avec `top`, à ajuster la priorité avec `renice`, et à les terminer avec `kill`. Ce laboratoire offre une expérience pratique du cycle de vie des processus, y compris comment les terminer et observer leurs états.

## Quiz Question

Quel est le statut de terminaison le plus courant pour un processus qui réussit ?

## Quiz Answer

0
