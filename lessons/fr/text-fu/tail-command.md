---
lang: "fr"
title: "tail"
description: "Apprenez à utiliser la commande `tail` sous Linux pour afficher les fins de fichiers et surveiller les journaux. Découvrez `tail -f` pour des mises à jour en temps réel. Commencez votre parcours Linux !"
keywords: "commande tail, Linux tail, tail -f, afficher les journaux, tutoriel Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

Similaire à la commande `head`, la commande `tail` vous permet de voir les 10 dernières lignes d'un fichier par défaut.

```bash
tail /var/log/syslog
```

Tout comme avec `head`, vous pouvez modifier le nombre de lignes que vous souhaitez voir.

```bash
tail -n 10 /var/log/syslog
```

Une autre excellente option que vous pouvez utiliser est l'indicateur `-f` (follow) ; cela suivra le fichier au fur et à mesure qu'il grandit. Essayez et voyez ce qui se passe.

```bash
tail -f /var/log/syslog
```

Votre fichier `syslog` changera continuellement pendant que vous interagissez avec votre système, et en utilisant `tail -f`, vous pouvez voir tout ce qui est ajouté à ce fichier.

## Exercise

Consultez la page de manuel de `tail` et lisez certaines des autres commandes que nous n'avons pas abordées.

```bash
man tail
```

## Quiz Question

Quel est l'indicateur utilisé pour suivre un fichier dans `tail` ?

## Quiz Answer

-f
