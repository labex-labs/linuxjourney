---
index: 12
lang: "fr"
title: "sort"
meta_title: "sort - Text-Fu"
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

La véritable puissance de `sort` réside dans sa capacité à être combinée avec d'autres commandes. Essayez la commande suivante et voyez ce qui se passe :

```bash
ls /etc | sort -rn
```

## Quiz Question

Quel drapeau utilisez-vous pour effectuer un tri inversé ?

## Quiz Answer

-r
