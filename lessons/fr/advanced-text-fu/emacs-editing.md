---
index: 12
lang: "fr"
title: "Édition Emacs"
meta_title: "Édition Emacs - Maîtrise Avancée du Texte"
meta_description: "Maîtrisez les fondamentaux de l'édition Emacs avec ce guide pour débutants. Apprenez les commandes Emacs essentielles pour la navigation, la coupe et le collage de texte dans cet éditeur de texte puissant sous Linux."
meta_keywords: "Emacs, tutoriel Emacs, commandes Emacs, éditeur de texte, éditeur Linux, navigation Emacs, Emacs débutant, guide Emacs"
---

## Lesson Content

Emacs est un éditeur de texte puissant et extensible largement utilisé sur Linux et autres systèmes de type Unix. Ce guide Emacs pour débutants vous présentera quelques commandes d'édition fondamentales. Dans la terminologie Emacs, `C-` fait référence à la touche `Ctrl`, et `M-` fait référence à la touche `Meta`, qui est généralement la touche `Alt`.

### Navigation de Texte Emacs

Bien que les touches de navigation standard comme Début, Fin et les flèches fonctionnent comme prévu, Emacs offre des commandes plus efficaces pour se déplacer dans votre texte, que Emacs conserve dans un "buffer". Maîtriser la navigation Emacs est une étape clé pour devenir compétent.

Voici quelques commandes Emacs essentielles pour déplacer le curseur :

```
C-flèche haut : monter d'un paragraphe
C-flèche bas : descendre d'un paragraphe
C-flèche gauche : reculer d'un mot
C-flèche droite : avancer d'un mot
M-> : aller à la fin du buffer
```

### Couper et Coller

Dans Emacs, couper s'appelle "killing" (tuer) et coller s'appelle "yanking" (tirer). Pour effectuer ces actions, vous devez d'abord sélectionner une région de texte.

Pour commencer à sélectionner du texte, déplacez votre curseur au début de la région souhaitée et appuyez sur `C-espace`. Cela définit la "marque". Ensuite, utilisez n'importe quelle commande de navigation pour déplacer le curseur à la fin de la région que vous souhaitez sélectionner. La zone entre la marque et votre position actuelle du curseur sera mise en surbrillance.

Une fois que vous avez sélectionné une région, vous pouvez utiliser les commandes suivantes :

```
C-w : tuer (couper) la région sélectionnée
C-y : tirer (coller) le dernier texte tué
```

Ces commandes de base constituent le fondement de l'édition dans l'éditeur de texte Emacs.

## Exercise

La meilleure façon d'apprendre les commandes Emacs est par la pratique. Ouvrez un nouveau fichier texte en utilisant `emacs my_practice_file.txt` et essayez les commandes de navigation, de sélection, de coupe et de collage abordées dans cette leçon. Familiarisez-vous avec le déplacement dans le buffer et la manipulation du texte.

## Quiz Question

Comment vous déplacez-vous à la fin du buffer ? Veuillez répondre en utilisant uniquement le format de combinaison de touches montré dans la leçon (par exemple, C-w). La réponse est sensible à la casse.

## Quiz Answer

M->
