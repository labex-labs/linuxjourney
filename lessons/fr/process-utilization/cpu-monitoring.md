---
lang: "fr"
title: "Surveillance du CPU"
meta_description: "Apprenez la surveillance du CPU avec la commande uptime. Comprenez la moyenne de charge, l'utilisation du CPU et comment interpréter les performances du système pour les débutants Linux."
meta_keywords: "commande uptime, surveillance CPU Linux, moyenne de charge, performances système, tutoriel Linux, guide du débutant"
---

## Lesson Content

Passons en revue une commande utile, **uptime**.

```
pete@icebox:~$ uptime
 17:23:35 up 1 day,  5:59,  2 users,  load average: 0.00, 0.02, 0.05
```

Nous avons parlé de uptime dans la première leçon de ce cours, mais nous n'avons pas abordé le champ load average. Les moyennes de charge sont un bon moyen de voir la charge CPU sur votre système. Ces nombres représentent la charge CPU moyenne sur des intervalles de 1, 5 et 15 minutes. Qu'est-ce que j'entends par charge CPU ? La charge CPU est le nombre moyen de processus qui attendent d'être exécutés par le CPU.

Disons que vous avez un CPU monocœur ; considérez ce cœur comme une seule voie de circulation. S'il y a une heure de pointe sur l'autoroute, cette voie sera très occupée, et le trafic sera à 100 % ou une charge de 1. Maintenant, le trafic est devenu si dense qu'il bloque l'autoroute et rend les routes normales deux fois plus encombrées par les voitures ; nous pouvons dire que votre charge est de 200 % ou une charge de 2. Maintenant, disons que ça se dégage un peu et qu'il n'y a que la moitié moins de voitures sur la voie de l'autoroute ; nous pouvons dire que la charge de la voie est de 0,5. Lorsque le trafic est inexistant et que nous pouvons rentrer chez nous plus rapidement, la charge devrait idéalement être très faible, comme le trafic de 2 heures du matin. Les voitures dans ce cas sont des processus, et ces processus attendent juste de quitter l'autoroute et de rentrer chez eux.

Maintenant, ce n'est pas parce que vous avez une moyenne de charge de 1 que votre ordinateur est lent. La plupart des machines modernes ont de nos jours plusieurs cœurs. Si vous aviez un processeur quad-core (4 cœurs) et que votre moyenne de charge est de 1, cela n'affecte vraiment que 25 % de votre CPU. Considérez chaque cœur comme une voie de circulation. Vous pouvez voir le nombre de cœurs que vous avez sur votre système avec **cat /proc/cpuinfo**.

Lorsque vous observez la moyenne de charge, vous devez prendre en compte le nombre de cœurs. Si vous constatez que votre machine utilise toujours une charge supérieure à la moyenne, il pourrait y avoir un problème.

## Exercise

Check the load average of your system and see what it's doing.

## Quiz Question

Quelle commande pouvez-vous utiliser pour voir la moyenne de charge ?

## Quiz Answer

uptime
