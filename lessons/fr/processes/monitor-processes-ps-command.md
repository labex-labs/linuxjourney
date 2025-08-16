---
lang: "fr"
title: "ps (Processus)"
description: "Découvrez la commande Linux 'ps' pour visualiser les processus en cours d'exécution et comprendre les ID de processus (PID). Obtenez un guide pour débutants sur la gestion des processus."
keywords: "commande ps, processus Linux, ID de processus, PID, tutoriel Linux, débutant, guide, commande top"
---

## Lesson Content

Les processus sont les programmes qui s'exécutent sur votre machine. Ils sont gérés par le noyau, et chaque processus a un ID qui lui est associé, appelé **ID de processus (PID)**. Ce PID est attribué dans l'ordre de création des processus.

Allez-y et exécutez la commande `ps` pour voir une liste des processus en cours d'exécution :

```plaintext
$ ps

PID        TTY     STAT   TIME          CMD
41230    pts/4    Ss        00:00:00     bash
51224    pts/4    R+        00:00:00     ps
```

Ceci vous donne un aperçu rapide des processus actuels :

- PID : ID du processus
- TTY : Terminal de contrôle associé au processus (nous y reviendrons plus en détail plus tard)
- STAT : Code d'état du processus
- TIME : Temps total d'utilisation du CPU
- CMD : Nom de l'exécutable/de la commande

Si vous consultez la page de manuel de `ps`, vous verrez qu'il existe de nombreuses options de commande que vous pouvez passer. Elles varieront en fonction des options que vous souhaitez utiliser — BSD, GNU ou Unix. À mon avis, le style BSD est plus populaire, nous allons donc l'utiliser. Si vous êtes curieux, la différence entre les styles réside dans le nombre de tirets que vous utilisez et les drapeaux.

```bash
ps aux
```

Le **a** affiche tous les processus en cours d'exécution, y compris ceux exécutés par d'autres utilisateurs. Le **u** affiche plus de détails sur les processus. Et enfin, le **x** liste tous les processus qui n'ont pas de TTY associé. Ces programmes afficheront un `?` dans le champ TTY ; ils sont les plus courants dans les processus démon qui se lancent dans le cadre du démarrage du système.

Vous remarquerez que vous voyez beaucoup plus de champs maintenant. Pas besoin de tous les mémoriser ; dans un cours ultérieur sur les processus avancés, nous reviendrons sur certains d'entre eux :

- USER : L'utilisateur effectif (celui dont nous utilisons l'accès)
- PID : ID du processus
- %CPU : Temps CPU utilisé divisé par le temps d'exécution du processus
- %MEM : Ratio de la taille de l'ensemble résident du processus par rapport à la mémoire physique de la machine
- VSZ : Utilisation de la mémoire virtuelle de l'ensemble du processus
- RSS : Taille de l'ensemble résident, la mémoire physique non paginée qu'une tâche a utilisée
- TTY : Terminal de contrôle associé au processus
- STAT : Code d'état du processus
- START : Heure de début du processus
- TIME : Temps total d'utilisation du CPU
- COMMAND : Nom de l'exécutable/de la commande

La commande `ps` peut être un peu désordonnée à regarder. Pour l'instant, les champs que nous examinerons le plus sont PID, STAT et COMMAND.

Une autre commande très utile est la commande **top**. `top` vous donne des informations en temps réel sur les processus en cours d'exécution sur votre système au lieu d'un instantané. Par défaut, vous obtiendrez un rafraîchissement toutes les 10 secondes. `top` est un outil extrêmement utile pour voir quels processus consomment beaucoup de vos ressources.

```bash
top
```

## Exercise

Utilisez la commande `ps` avec différents drapeaux et voyez comment la sortie change.

## Quiz Question

Quel drapeau `ps` est utilisé pour afficher des informations détaillées sur les processus ?

## Quiz Answer

u
