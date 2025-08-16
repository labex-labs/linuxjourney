---
lang: "fr"
title: "head"
description: "Apprenez à utiliser la commande Linux 'head' pour afficher le début des fichiers. Comprenez les options comme -n pour le nombre de lignes. Tutoriel essentiel sur les commandes Linux."
keywords: "commande head, Linux head, afficher début fichier, tutoriel Linux, commandes Linux, Linux débutant, head -n, guide Linux"
---

## Lesson Content

Disons que nous avons un très long fichier ; en fait, nous en avons beaucoup à choisir. Allez-y et `cat /var/log/syslog`. Vous devriez voir des pages et des pages de texte. Et si je voulais juste voir les deux premières lignes de ce fichier texte ? Eh bien, nous pouvons le faire avec la commande `head`. Par défaut, la commande `head` vous montrera les 10 premières lignes d'un fichier.

```bash
head /var/log/syslog
```

Vous pouvez également modifier le nombre de lignes à votre guise. Disons que je voulais voir les 15 premières lignes à la place.

```bash
head -n 15 /var/log/syslog
```

Le drapeau `-n` signifie "nombre de lignes".

## Exercise

Que fait la commande suivante et pourquoi ?

```bash
had -c 15 /var/log/syslog
```

## Quiz Question

Quel drapeau utiliseriez-vous pour changer le nombre de lignes que vous souhaitez afficher pour la commande `head` ?

## Quiz Answer

-n
