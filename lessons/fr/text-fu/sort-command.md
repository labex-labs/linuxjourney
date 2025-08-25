---
index: 12
lang: "fr"
title: "sort"
meta_title: "sort - Maîtrise du texte"
meta_description: "Apprenez à utiliser la commande Linux sort pour trier des fichiers texte. Découvrez des options comme le tri inversé et numérique. Améliorez vos compétences en ligne de commande Linux !"
meta_keywords: "commande Linux sort, sort -r, sort -n, tutoriel Linux, ligne de commande, Linux débutant, guide sort"
---

## Lesson Content

La commande `sort` est utile pour trier les lignes.

```plaintext
file1.txt
dog
cow
cat
elephant
bird

$ sort file1.txt
bird
cat
cow
dog
elephant
```

Vous pouvez également effectuer un tri inversé :

```bash
$ sort -r file1.txt
elephant
dog
cow
cat
bird
```

Et aussi trier par valeur numérique :

```bash
$ sort -n file1.txt
bird
cat
cow
elephant
dog
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la commande `sort` et du traitement de texte :

1. **[Commande Linux sort : Tri de texte](https://labex.io/fr/labs/linux-linux-sort-command-text-sorting-219196)** - Ce laboratoire offre une introduction directe à la commande `sort`, vous permettant de pratiquer le tri de lignes de fichiers texte de différentes manières, y compris par ordre croissant et décroissant.
2. **[Comptage et tri de mots](https://labex.io/fr/labs/linux-word-count-and-sorting-388125)** - Dans ce défi, vous appliquerez vos connaissances du tri et du comptage de mots pour analyser des données textuelles, vous aidant à trouver des motifs fréquents et à trier les données efficacement.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la manipulation et le tri de texte sous Linux.

## Quiz Question

Quel drapeau utilisez-vous pour effectuer un tri inversé ?

## Quiz Answer

-r
