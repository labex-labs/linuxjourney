---
lang: "fr"
title: "paste"
meta_description: "Apprenez à utiliser la commande Linux paste pour fusionner les lignes de fichiers. Découvrez les délimiteurs et combinez des fichiers avec ce tutoriel essentiel sur les commandes Linux."
meta_keywords: "commande Linux paste, tutoriel commande paste, fusionner les lignes de fichiers, commandes Linux, Linux pour débutants, guide Linux"
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

Essayez de coller plusieurs fichiers ensemble. Que se passe-t-il ?

## Quiz Question

Quel drapeau utilisez-vous avec `paste` pour que tout tienne sur une seule ligne ?

## Quiz Answer

-s
