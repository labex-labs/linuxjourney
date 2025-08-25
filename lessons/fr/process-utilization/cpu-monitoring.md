---
index: 4
lang: "fr"
title: "Surveillance CPU"
meta_title: "Surveillance CPU - Utilisation des processus"
meta_description: "Apprenez la surveillance du CPU avec la commande uptime. Comprenez la charge moyenne, l'utilisation du CPU et comment interpréter les performances du système pour les débutants Linux."
meta_keywords: "commande uptime, surveillance CPU Linux, charge moyenne, performances système, tutoriel Linux, guide du débutant"
---

## Lesson Content

Passons en revue une commande utile, **uptime**.

```
pete@icebox:~$ uptime
 17:23:35 up 1 day,  5:59,  2 users,  load average: 0.00, 0.02, 0.05
```

Nous avons parlé d'uptime dans la première leçon de ce cours, mais nous n'avons pas encore abordé le champ de la charge moyenne (load average). Les charges moyennes sont un bon moyen de voir la charge CPU sur votre système. Ces nombres représentent la charge CPU moyenne sur des intervalles de 1, 5 et 15 minutes. Qu'est-ce que j'entends par charge CPU ? La charge CPU est le nombre moyen de processus qui attendent d'être exécutés par le CPU.

Disons que vous avez un CPU monocœur ; imaginez ce cœur comme une seule voie de circulation. S'il est l'heure de pointe sur l'autoroute, cette voie va être très occupée, et le trafic sera à 100 % ou une charge de 1. Maintenant, le trafic est devenu si mauvais qu'il bloque l'autoroute et rend les routes normales deux fois plus encombrées ; nous pouvons dire que votre charge est de 200 % ou une charge de 2. Maintenant, disons que ça se dégage un peu et qu'il n'y a que la moitié moins de voitures sur la voie de l'autoroute ; nous pouvons dire que la charge de la voie est de 0,5. Lorsque le trafic est inexistant et que nous pouvons rentrer chez nous plus rapidement, la charge devrait idéalement être très faible, comme le trafic de 2 heures du matin. Les voitures dans ce cas sont des processus, et ces processus attendent juste de quitter l'autoroute et de rentrer chez eux.

Maintenant, ce n'est pas parce que vous avez une charge moyenne de 1 que votre ordinateur est lent. La plupart des machines modernes ont de nos jours plusieurs cœurs. Si vous aviez un processeur quad-core (4 cœurs) et que votre charge moyenne est de 1, cela n'affecte vraiment que 25 % de votre CPU. Considérez chaque cœur comme une voie de circulation. Vous pouvez voir le nombre de cœurs que vous avez sur votre système avec **cat /proc/cpuinfo**.

Lorsque vous observez la charge moyenne, vous devez prendre en compte le nombre de cœurs. Si vous constatez que votre machine utilise toujours une charge supérieure à la moyenne, il pourrait y avoir un problème.

## Exercise

C'est en forgeant qu'on devient forgeron ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la surveillance des performances du système Linux et de la charge CPU :

1. **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir avec et à inspecter les processus, et à surveiller les ressources avec des outils comme `ps` et `top`, ce qui est directement lié à la compréhension de la charge CPU.
2. **[Commande Linux top : Surveillance du système en temps réel](https://labex.io/fr/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Apprenez à utiliser la commande `top` pour la surveillance du système en temps réel, y compris le tri et le filtrage des processus, offrant une plongée plus profonde dans l'activité du CPU et des processus.
3. **[Commande Linux free : Surveillance de la mémoire système](https://labex.io/fr/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Apprenez à surveiller et à analyser l'utilisation de la mémoire système, qui est souvent un facteur critique, en plus de la charge CPU, pour la performance globale du système.

Ces laboratoires vous aideront à appliquer les concepts de surveillance du système et de gestion des ressources dans des scénarios réels et à renforcer votre confiance dans l'analyse des performances du système.

## Quiz Question

Quelle commande pouvez-vous utiliser pour voir la charge moyenne ?

## Quiz Answer

uptime
