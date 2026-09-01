---
lesson_id: "vim-navigation"
course_id: "advanced-text-fu"
lang: "fr"
order_index: 5
title: "Navigation Vim"
description: "Apprenez à vous déplacer par caractères, mots, lignes et positions de fichier dans le mode Normal de Vim."
meta_title: "Navigation Vim - Maîtrise Avancée du Texte"
meta_description: "Apprenez les bases de la navigation Vim en utilisant les touches h, j, k, l. Comprenez les mouvements essentiels de Vim pour les débutants et améliorez vos compétences en ligne de commande Linux."
meta_keywords: "Navigation Vim, Tutoriel Vim, Vim Linux, Mouvement Vim, Bases Vim, Vim débutant, Éditeur de texte Linux, Guide Vim"
---

Vim fournit des déplacements au clavier utilisables dans un terminal sans souris. Certaines configurations acceptent aussi la souris, mais la maîtrise des déplacements permet de les combiner avec les commandes d'édition.

Appuyez sur `Esc` avant de vous exercer afin de revenir au mode Normal.

## Se déplacer par caractères et lignes d'écran

Les déplacements fondamentaux du mode Normal sont :

- `h` : un caractère vers la gauche ;
- `j` : une ligne d'écran vers le bas ;
- `k` : une ligne d'écran vers le haut ;
- `l` : un caractère vers la droite.

Les touches fléchées produisent généralement des déplacements similaires, mais `h`, `j`, `k` et `l` gardent les mains près des autres commandes. Sur une ligne repliée à l'écran, `j` et `k` se déplacent normalement selon les lignes du fichier ; `gj` et `gk` suivent les lignes affichées.

:::single-choice{#vim-navigation-down} En mode Normal, quelle touche descend le curseur d'une ligne ?

::option[`k`]{#vim-nav-k-up explanation="Le déplacement `k` remonte d'une ligne."}
::option[`l`]{#vim-nav-l-right explanation="Le déplacement `l` avance d'un caractère vers la droite."}
::option[`j`]{#vim-nav-j-down .correct explanation="En mode Normal, le déplacement `j` descend d'une ligne."}
:::

## Préfixer les déplacements par un nombre

Saisissez un nombre positif avant de nombreux déplacements pour les répéter. Par exemple :

```text
5j
3l
```

`5j` descend de cinq lignes, tandis que `3l` avance si possible de trois caractères vers la droite. Les nombres se combinent aussi avec les commandes de déplacement par mots et d'édition.

:::single-choice{#vim-navigation-count} Quel est l'effet de `4k` en mode Normal ?

::option[Descendre si possible de quatre lignes.]{#vim-nav-four-down explanation="Le déplacement vers le bas utilise `j` ; `k` va dans le sens opposé."}
::option[Remonter si possible de quatre lignes.]{#vim-nav-four-up .correct explanation="Le nombre `4` répète quatre fois le déplacement `k` vers le haut."}
::option[Supprimer quatre lignes au-dessus du curseur.]{#vim-nav-delete-four explanation="Un déplacement seul change la position du curseur. La suppression nécessiterait un opérateur comme `d`."}
:::

## Se déplacer par mots

Parmi les déplacements utiles par mots :

- `w` : aller au début du mot suivant ;
- `b` : aller au début du mot actuel ou précédent ;
- `e` : aller à la fin du mot actuel ou suivant.

Les majuscules `W`, `B` et `E` utilisent des WORDS délimités par des espaces et traitent donc la ponctuation autrement. Préfixez le déplacement par un nombre pour parcourir plusieurs mots, par exemple `3w`.

:::single-choice{#vim-navigation-next-words} Quelle commande du mode Normal avance jusqu'au début de la troisième position de mot suivante ?

::option[`3w`]{#vim-nav-three-words .correct explanation="Le nombre applique trois fois le déplacement vers le mot suivant."}
::option[`w3`]{#vim-nav-word-three explanation="Dans cette forme de commande, le nombre précède le déplacement ; placé après, `3` n'exprime pas le mouvement demandé."}
::option[`3b`]{#vim-nav-three-back explanation="Le déplacement `b` va vers les débuts de mots antérieurs plutôt que vers l'avant."}
:::

## Se déplacer dans une ligne

Ces déplacements ciblent des positions de la ligne actuelle :

- `0` : aller à la colonne zéro ;
- `^` : aller au premier caractère non blanc ;
- `$` : aller à la fin de la ligne.

La différence entre `0` et `^` est importante sur les lignes indentées.

:::single-choice{#vim-navigation-first-nonblank} Quel déplacement va au premier caractère non blanc d'une ligne indentée ?

::option[`0`]{#vim-nav-column-zero explanation="Zéro va à la première colonne, qui peut contenir un espace d'indentation."}
::option[`$`]{#vim-nav-line-end explanation="Le déplacement dollar cible la fin de la ligne."}
::option[`^`]{#vim-nav-first-nonblank .correct explanation="L'accent circonflexe ignore les blancs initiaux et se place sur le premier caractère non blanc."}
:::

## Parcourir le fichier

Utilisez ces commandes du mode Normal pour effectuer de plus grands sauts :

- `gg` : aller à la première ligne ;
- `G` : aller à la dernière ligne ;
- `42G` : aller à la ligne 42 ;
- `Ctrl+F` : avancer d'environ un écran ;
- `Ctrl+B` : reculer d'environ un écran.

La commande `:42`, suivie d'Entrée, permet également d'aller à la ligne 42.

:::single-choice{#vim-navigation-file-end} Quelle commande du mode Normal va à la dernière ligne du tampon ?

::option[`gg`]{#vim-nav-first-line explanation="Le `gg` minuscule va à la première ligne, pas à la dernière."}
::option[`$`]{#vim-nav-current-line-end explanation="Le déplacement dollar va à la fin de la ligne actuelle, pas à celle du fichier."}
::option[`G`]{#vim-nav-last-line .correct explanation="Sans nombre, le `G` majuscule saute à la dernière ligne."}
:::

Pour pratiquer la navigation au clavier dans un fichier jetable, essayez ce laboratoire :

1. **[Modifier des fichiers texte sous Linux avec Vim et Nano](https://labex.io/fr/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** — Entraînez-vous à créer, modifier et enregistrer des fichiers, ainsi qu'à naviguer avec Vim et Nano dans un véritable environnement Linux.

## Résumé

Vous savez maintenant parcourir un tampon Vim à plusieurs échelles utiles.

1. Se déplacer par caractères ou lignes avec `h`, `j`, `k` et `l`.
2. Répéter un déplacement avec un préfixe numérique.
3. Parcourir les limites de mots avec `w`, `b` et `e`.
4. Cibler le début, le premier texte ou la fin d'une ligne.
5. Atteindre une position du fichier avec `gg`, `G` ou un numéro de ligne.
