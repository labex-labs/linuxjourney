---
lesson_id: "vim-editing"
course_id: "advanced-text-fu"
lang: "fr"
order_index: 7
title: "Édition Vim"
description: "Apprenez comment Vim combine opérateurs, déplacements, registres, collages et annulations pour modifier du texte."
meta_title: "Édition Vim - Maîtrise Avancée du Texte"
meta_description: "Un tutoriel Vim pour débutants sur les commandes d'édition essentielles. Apprenez à supprimer, modifier, copier (yank) et coller du texte dans l'éditeur Vim pour améliorer votre flux de travail Linux."
meta_keywords: "Édition Vim, commandes Vim, éditeur de texte Linux, tutoriel Vim, guide Vim, Vim débutant, commande dd, suppression Vim"
---

Les commandes d'édition de Vim combinent souvent un opérateur avec un déplacement ou un objet textuel. Cette grammaire permet d'appliquer les mêmes actions à un caractère, un mot, une ligne ou une portée plus grande. Appuyez sur `Esc` avant de vous exercer afin de revenir au mode Normal.

## Combiner un opérateur et un déplacement

La forme générale est :

```text
[nombre] opérateur [nombre] déplacement
```

Les opérateurs courants comprennent :

- `d` : supprimer du texte ;
- `c` : modifier du texte, puis passer au mode Insertion ;
- `y` : copier, ou « yanker », du texte.

Par exemple, `dw` supprime sur la portée du déplacement `w`, tandis que `d$` supprime du curseur jusqu'à la fin de la ligne. `2dw` applique la suppression sur deux déplacements de mot.

:::single-choice{#vim-edit-operator-motion}
En mode Normal, quel est l'effet de `d$` ?

::option[Supprimer tout le fichier à partir du curseur.]{#vim-edit-delete-file-end explanation="Le déplacement dollar cible la fin de la ligne actuelle, pas celle de tout le tampon."}
::option[Supprimer du curseur jusqu'à la fin de la ligne.]{#vim-edit-delete-line-end .correct explanation="L'opérateur `d` s'applique au déplacement `$` qui mène à la fin de la ligne."}
::option[Aller à la fin de la ligne sans modifier le texte.]{#vim-edit-move-line-end explanation="`$` seul effectue un déplacement, mais le `d` qui le précède supprime la plage parcourue."}
:::

## Modifier des caractères et des lignes

Certaines commandes constituent des raccourcis pratiques :

- `x` : supprimer le caractère sous le curseur ;
- `dd` : supprimer toute la ligne actuelle ;
- `3dd` : supprimer trois lignes à partir de la ligne actuelle ;
- `cc` : modifier la ligne actuelle et passer au mode Insertion ;
- `r{caractère}` : remplacer le caractère sous le curseur par `{caractère}` ;
- `R` : passer au mode Remplacement jusqu'à l'appui sur `Esc`.

La répétition d'un opérateur, comme dans `dd`, le fait agir ligne par ligne. Un nombre étend le nombre de lignes concernées.

:::single-choice{#vim-edit-delete-three-lines}
Quelle commande du mode Normal supprime la ligne actuelle et les deux suivantes ?

::option[`dd3`]{#vim-edit-dd-three explanation="Dans cette forme de commande, le nombre se place avant l'opérateur doublé."}
::option[`3x`]{#vim-edit-three-x explanation="Cette commande supprime trois caractères à partir du curseur, pas trois lignes complètes."}
::option[`3dd`]{#vim-edit-three-dd .correct explanation="Le nombre s'applique à la commande ligne par ligne `dd` et supprime trois lignes à partir de la ligne actuelle."}
:::

## Modifier du texte et passer au mode Insertion

L'opérateur `c` retire le texte sélectionné et passe au mode Insertion afin que vous puissiez saisir son remplacement :

- `ce` : modifier jusqu'à la fin du mot ;
- `c$` : modifier jusqu'à la fin de la ligne ;
- `cc` : modifier toute la ligne actuelle ;
- `ciw` : modifier le mot intérieur sous le curseur ;
- `caw` : modifier l'objet textuel « un mot », y compris l'espacement alentour tel que Vim le définit.

Le comportement de `cw` présente un cas particulier historique et ressemble souvent à `ce`. Les objets textuels comme `iw` peuvent rendre la limite visée plus claire.

:::single-choice{#vim-edit-change-inner-word}
Quelle commande du mode Normal remplace le mot intérieur sous le curseur en le supprimant puis en passant au mode Insertion ?

::option[`diw`]{#vim-edit-delete-inner-word explanation="Cette commande supprime le mot intérieur, mais reste en mode Normal au lieu de commencer le texte de remplacement."}
::option[`yiw`]{#vim-edit-yank-inner-word explanation="Cette commande copie le mot intérieur sans modifier le tampon ni passer au mode Insertion."}
::option[`ciw`]{#vim-edit-change-inner-word-answer .correct explanation="L'opérateur `c` modifie l'objet textuel `iw`, puis passe au mode Insertion."}
:::

## Copier et coller du texte

Vim appelle la copie **yank** et le collage **put** :

- `yw` : copier sur la portée d'un déplacement de mot ;
- `yy` : copier la ligne actuelle ;
- `p` : coller après le curseur pour du texte caractère par caractère, ou sous la ligne actuelle pour du texte ligne par ligne ;
- `P` : coller avant le curseur ou au-dessus de la ligne actuelle.

Les suppressions et modifications stockent aussi le texte dans des registres. Un `p` ultérieur peut donc coller le dernier texte supprimé plutôt qu'une copie plus ancienne. Les registres nommés permettent de conserver un texte précis ; commencez toutefois par surveiller ce qu'a stocké la dernière opération.

:::single-choice{#vim-edit-yank-put-line}
Après avoir copié la ligne actuelle avec `yy`, quelle commande la colle sous la ligne actuelle ?

::option[`p`]{#vim-edit-put-below .correct explanation="Pour du texte copié ligne par ligne, le `p` minuscule place la ligne mémorisée sous la ligne actuelle."}
::option[`P`]{#vim-edit-put-above explanation="Le `P` majuscule place le texte ligne par ligne au-dessus de la ligne actuelle."}
::option[`u`]{#vim-edit-undo-not-put explanation="Le `u` minuscule annule une modification ; il ne colle pas la ligne copiée."}
:::

## Annuler, rétablir et répéter

En mode Normal :

- `u` : annuler la dernière modification ;
- `Ctrl+R` : rétablir une modification annulée ;
- `.` : répéter si possible la dernière modification à l'emplacement actuel ;
- `J` : joindre la ligne actuelle à la suivante.

L'historique d'annulation concerne les modifications du tampon, pas les simples déplacements du curseur. Créez des points d'enregistrement et contrôlez vos changements au lieu de dépendre d'un historique illimité ou permanent.

:::single-choice{#vim-edit-redo-change}
Quelle commande du mode Normal rétablit une modification qui vient d'être annulée ?

::option[`Ctrl+U`]{#vim-edit-control-u explanation="En mode Normal, `Ctrl+U` remonte d'environ un demi-écran ; ce n'est pas la commande de rétablissement."}
::option[`.`]{#vim-edit-dot-repeat explanation="Le point répète la dernière modification comme une nouvelle action au lieu d'avancer dans l'historique d'annulation."}
::option[`Ctrl+R`]{#vim-edit-control-r .correct explanation="En mode Normal, Vim utilise `Ctrl+R` pour avancer dans l'historique d'annulation."}
:::

Pour pratiquer les opérateurs, les déplacements et la récupération sur du texte jetable, essayez ce laboratoire :

1. **[Modifier des fichiers texte sous Linux avec Vim et Nano](https://labex.io/fr/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** — Entraînez-vous à créer, modifier et enregistrer des fichiers, ainsi qu'à naviguer avec vi/vim et nano, puis appliquez la suppression, la modification, la copie et le collage à des situations réelles.

## Résumé

Vous savez maintenant composer des modifications Vim et corriger des erreurs en mode Normal.

1. Combiner des opérateurs avec des déplacements, des objets textuels et des nombres.
2. Supprimer des caractères ou des lignes complètes à la portée choisie.
3. Modifier du texte et passer au mode Insertion pour le remplacer.
4. Copier et coller du texte caractère par caractère ou ligne par ligne.
5. Annuler, rétablir ou répéter volontairement des modifications.
