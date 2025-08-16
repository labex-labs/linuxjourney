---
lang: "fr"
title: "Terminaison de processus"
description: "Découvrez la terminaison des processus Linux, y compris les processus orphelins et zombies. Comprenez les appels système _exit et wait pour une gestion efficace des processus."
keywords: "terminaison de processus Linux, processus zombies, processus orphelins, appel système wait, _exit, tutoriel Linux, Linux pour débutants"
---

## Lesson Content

Maintenant que nous savons ce qui se passe lorsqu'un processus est créé, que se passe-t-il lorsque nous n'en avons plus besoin ? Soyez prévenu, parfois Linux peut devenir un peu sombre...

Un processus peut se terminer en utilisant l'appel système `_exit`. Cela libérera les ressources que ce processus utilisait pour une nouvelle allocation. Ainsi, lorsqu'un processus est prêt à se terminer, il informe le kernel de la raison de sa terminaison avec ce qu'on appelle un statut de terminaison. Le plus souvent, un statut de 0 signifie que le processus a réussi. Cependant, ce n'est pas suffisant pour terminer complètement un processus. Le processus parent doit accuser réception de la terminaison du processus enfant en utilisant l'appel système `wait`, et ce que cela fait, c'est qu'il vérifie le statut de terminaison du processus enfant. Je sais que c'est macabre d'y penser, mais l'appel `wait` est une nécessité ; après tout, quel parent ne voudrait pas savoir comment son enfant est mort ?

Il existe une autre façon de terminer un processus, et cela implique l'utilisation de signaux, dont nous discuterons bientôt.

### Orphan Processes

Lorsqu'un processus parent meurt avant un processus enfant, le kernel sait qu'il ne recevra pas d'appel `wait`, alors il rend ces processus « orphelins » et les place sous la garde de `init` (rappelez-vous, la mère de tous les processus). `init` effectuera finalement l'appel système `wait` pour ces orphelins afin qu'ils puissent mourir.

### Zombie Processes

Que se passe-t-il lorsqu'un enfant se termine et que le processus parent n'a pas encore appelé `wait` ? Nous voulons toujours pouvoir voir comment un processus enfant s'est terminé, donc même si le processus enfant est terminé, le kernel transforme le processus enfant en un processus zombie. Les ressources utilisées par le processus enfant sont toujours libérées pour d'autres processus ; cependant, il y a toujours une entrée dans la table des processus pour ce zombie. Les processus zombies ne peuvent pas non plus être tués, car ils sont techniquement « morts », vous ne pouvez donc pas utiliser de signaux pour les tuer. Finalement, si le processus parent appelle l'appel système `wait`, le zombie disparaîtra ; c'est ce qu'on appelle le « reaping ». Si le parent n'effectue pas d'appel `wait`, `init` adoptera le zombie et effectuera automatiquement `wait` et supprimera le zombie. Il peut être mauvais d'avoir trop de processus zombies, car ils occupent de l'espace dans la table des processus ; si elle se remplit, cela empêchera d'autres processus de s'exécuter.

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Quel est le statut de terminaison le plus courant pour un processus qui réussit ?

## Quiz Answer

0
