---
index: 4
lang: "fr"
title: "Surveillance du CPU"
meta_title: "Surveillance du CPU - Utilisation des processus"
meta_description: "Apprenez les bases de la surveillance du CPU sous Linux avec la commande uptime. Ce guide pour débutants explique comment interpréter la charge moyenne, comprendre l'utilisation des processus et évaluer les performances du système."
meta_keywords: "commande uptime, surveillance CPU Linux, charge moyenne, performance système, utilisation des processus, tutoriel Linux, guide débutant"
---

## Lesson Content

Une compétence fondamentale dans la gestion d'un système Linux est la compréhension de ses performances. L'une des commandes les plus utiles pour un contrôle rapide de l'état est **uptime**.

```
pete@icebox:~$ uptime
 17:23:35 up 1 day,  5:59,  2 users,  load average: 0.00, 0.02, 0.05
```

Bien que nous ayons déjà vu `uptime`, concentrons-nous sur le champ `load average` (charge moyenne), qui est crucial pour la **surveillance du CPU sous Linux**.

### Comprendre la Charge Moyenne

La charge moyenne fournit un instantané de la charge CPU de votre système. Les trois nombres représentent la charge moyenne du CPU sur les intervalles de 1, 5 et 15 minutes. Mais qu'est-ce que la charge CPU ? C'est le nombre moyen de processus dans la file d'attente d'exécution (run-queue), ce qui signifie qu'ils sont soit activement exécutés par le CPU, soit en attente de leur tour. Cette métrique est un indicateur clé de l'**utilisation des processus** et de la **performance globale du système**.

### Une Analogie Routière

Imaginez un CPU monocœur comme une autoroute à une seule voie.

- Si l'autoroute est à pleine capacité avec un flux constant de voitures, le trafic est à 100 %, ce qui correspond à une charge moyenne de 1,0.
- Si un embouteillage majeur se produit et que les voitures s'accumulent au double de la capacité de l'autoroute, la charge est de 200 %, soit une charge moyenne de 2,0.
- Si l'autoroute est à moitié vide, la charge est de 0,5.
- Idéalement, vous souhaitez une charge moyenne faible, comme une autoroute à 2 heures du matin sans trafic.

Dans cette analogie, les voitures sont les processus attendant d'être traités par le CPU.

### Interpréter la Charge Moyenne sur les Systèmes Modernes

Une charge moyenne de 1,0 ne signifie pas nécessairement que votre système est en difficulté. La plupart des ordinateurs modernes disposent de processeurs multi-cœurs. Si vous avez un processeur quadricœur (4 cœurs), une charge moyenne de 1,0 signifie que seulement 25 % de votre capacité CPU totale est utilisée. Chaque cœur agit comme une voie supplémentaire sur l'autoroute.

Pour interpréter correctement la charge moyenne, vous devez tenir compte du nombre de cœurs CPU. Vous pouvez afficher le nombre de cœurs sur votre système avec la commande `cat /proc/cpuinfo`.

Une règle générale pour une bonne **performance du système** est de maintenir votre charge moyenne inférieure au nombre de cœurs. Si vous constatez que votre machine a constamment une charge moyenne supérieure à son nombre de cœurs, cela pourrait indiquer un goulot d'étranglement de performance, tel qu'un processus incontrôlé ou des ressources matérielles insuffisantes.

## Exercise

Afin d'acquérir une expérience pratique avec la **surveillance du CPU sous Linux** et l'analyse de la **performance du système**, essayez ces laboratoires pratiques. Ils vous aideront à appliquer les concepts de **charge moyenne** et d'**utilisation des processus** dans des scénarios réels.

1. **[Gérer et Surveiller les Processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir et à inspecter les processus, et à surveiller les ressources avec des outils comme `ps` et `top`, ce qui est directement lié à la compréhension de la charge CPU.
2. **[Commande Linux top : Surveillance du Système en Temps Réel](https://labex.io/fr/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Apprenez à utiliser la commande `top` pour la surveillance du système en temps réel, y compris le tri des processus et le filtrage, offrant une analyse plus approfondie de l'activité CPU et des processus.
3. **[Commande Linux free : Surveillance de la Mémoire Système](https://labex.io/fr/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Apprenez à surveiller et à analyser l'utilisation de la mémoire système, qui est souvent un facteur critique parallèlement à la charge CPU dans la performance globale du système.

## Quiz Question

Quelle commande pouvez-vous utiliser pour voir la charge moyenne du système ? Veuillez répondre en anglais, et notez que la commande est sensible à la casse.

## Quiz Answer

uptime
