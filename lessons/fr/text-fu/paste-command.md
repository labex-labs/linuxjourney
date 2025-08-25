---
index: 7
lang: "fr"
title: "paste"
meta_title: "paste - Text-Fu"
meta_description: "Apprenez à utiliser la commande Linux paste pour fusionner les lignes de fichiers. Découvrez les délimiteurs et combinez des fichiers avec ce tutoriel essentiel sur les commandes Linux."
meta_keywords: "commande Linux paste, tutoriel commande paste, fusionner lignes de fichiers, commandes Linux, Linux débutant, guide Linux"
---

## Lesson Content

La commande `paste` est similaire à la commande `cat` ; elle fusionne les lignes d'un fichier. Créons un nouveau fichier avec le contenu suivant :

```
sample2.txt
The
quick
brown
fox
```

Combinons toutes ces lignes en une seule ligne :

```bash
paste -s sample2.txt
```

Le délimiteur par défaut pour `paste` est TAB, donc maintenant il y a une ligne avec des TABs séparant chaque mot.

Changeons ce délimiteur (`-d`) pour quelque chose d'un peu plus lisible :

```bash
paste -d ' ' -s sample2.txt
```

Maintenant, tout devrait être sur une seule ligne délimitée par des espaces.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du traitement de texte et de la manipulation de données sous Linux :

1. **[Traitement de texte simple](https://labex.io/fr/labs/linux-simple-text-processing-18004)** - Apprenez à utiliser des commandes puissantes comme `tr`, `col`, `join` et `paste` pour manipuler et analyser efficacement les données textuelles.
2. **[Redirection de flux de données](https://labex.io/fr/labs/linux-data-stream-redirection-17995)** - Apprenez l'art de la redirection de flux Linux et comment manipuler les flux d'entrée, de sortie et d'erreur standard, ce qui est fondamental pour comprendre comment des commandes comme `paste` fonctionnent.
3. **[Contrôle de séquence et pipeline](https://labex.io/fr/labs/linux-sequence-control-and-pipeline-17994)** - Apprenez à contrôler les séquences d'exécution des commandes et à utiliser les pipelines, améliorant ainsi votre capacité à combiner `paste` avec d'autres commandes pour des tâches de données complexes.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans le traitement de texte et la gestion des données sous Linux.

## Quiz Question

Quel drapeau utilisez-vous avec `paste` pour que tout tienne sur une seule ligne ?

## Quiz Answer

-s
