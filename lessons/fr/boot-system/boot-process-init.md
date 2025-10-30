---
index: 5
lang: "fr"
title: "Processus de démarrage : Init"
meta_title: "Processus de démarrage : Init - Démarrer le système"
meta_description: "Découvrez les systèmes init de Linux : System V, Upstart et systemd. Comprenez leurs rôles dans le processus de démarrage et comment ils gèrent les services. Commencez votre parcours Linux !"
meta_keywords: "Linux init, systemd, System V init, Upstart, processus de démarrage Linux, tutoriel Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

Nous avons abordé init dans les leçons précédentes et savons que c'est le premier processus qui est démarré, et qu'il démarre tous les autres services essentiels de notre système. Mais comment ?

Il existe en fait trois implémentations majeures d'init sous Linux :

### System V init (sysv)

C'est le système init traditionnel. Il démarre et arrête séquentiellement les processus en fonction des scripts de démarrage. L'état de la machine est indiqué par des niveaux d'exécution (runlevels) ; chaque niveau d'exécution démarre ou arrête une machine d'une manière différente.

### Upstart

C'est l'init que vous trouverez sur les anciennes installations d'Ubuntu. Upstart utilise l'idée de tâches (jobs) et d'événements et fonctionne en démarrant des tâches qui effectuent certaines actions en réponse à des événements.

### Systemd

C'est le nouveau standard pour init ; il est orienté objectif. En gros, vous avez un objectif que vous voulez atteindre, et systemd essaie de satisfaire les dépendances de l'objectif pour le compléter.

Nous avons un cours entier sur les systèmes Init où nous approfondirons chacun de ces systèmes.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des processus Linux et de la façon dont le système les gère :

1. **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir avec les processus de premier plan et d'arrière-plan, à les inspecter avec `ps`, à surveiller les ressources avec `top`, et à les terminer avec `kill`. Ce laboratoire vous aidera à comprendre le cycle de vie et le contrôle des processus, qui sont fondamentaux pour le fonctionnement d'`init`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion des processus Linux.

## Quiz Question

Quel est le nouveau standard pour init ?

## Quiz Answer

systemd
