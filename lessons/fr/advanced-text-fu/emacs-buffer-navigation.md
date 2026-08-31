---
lesson_id: "emacs-buffer-navigation"
course_id: "advanced-text-fu"
lang: "fr"
order_index: 11
title: "Navigation dans les Tampons Emacs"
description: "Apprenez à changer et fermer des tampons Emacs, ainsi qu'à diviser, sélectionner et fermer les fenêtres d'affichage."
meta_title: "Navigation Tampons Emacs - Maîtrise Avancée du Texte"
meta_description: "Guide complet sur la navigation dans les tampons Emacs. Apprenez à basculer efficacement entre les tampons, diviser les fenêtres et gérer votre flux de travail avec les commandes Emacs essentielles. Maîtrisez la commande switch buffer d'Emacs et améliorez vos compétences en édition de texte."
meta_keywords: "navigation emacs, emacs switch buffer, gestion tampons emacs, commandes emacs, C-x b, C-x k, C-x 2, éditeur de texte, linux"
---

Un tampon Emacs contient du texte ou un état de l'éditeur, tandis qu'une fenêtre affiche un tampon. Un tampon peut exister sans être visible, et plusieurs fenêtres peuvent afficher le même tampon. La gestion de l'un de ces objets n'entraîne pas automatiquement celle de l'autre.

## Changer de tampon

Utilisez `C-x b`, qui exécute `switch-to-buffer`, pour sélectionner par son nom le tampon affiché dans la fenêtre actuelle :

```text
C-x b
```

Le minibuffer propose la complétion des noms existants. La saisie d'un nouveau nom peut créer un tampon sans fichier portant ce nom ; elle n'ouvre pas un chemin de fichier.

Par défaut, `C-x Droite` exécute `next-buffer` et `C-x Gauche` exécute `previous-buffer`, ce qui fait défiler les tampons dans la fenêtre sélectionnée.

:::single-choice{#emacs-switch-buffer-key}
Quelle séquence de touches demande le nom du tampon à afficher dans la fenêtre actuelle ?

::option[`C-x C-f`]{#emacs-buffer-find-file explanation="Cette séquence demande un chemin et ouvre ce fichier, ce qui diffère du choix d'un tampon existant par son nom."}
::option[`C-x b`]{#emacs-switch-buffer .correct explanation="`switch-to-buffer` lit un nom de tampon et affiche celui-ci dans la fenêtre sélectionnée."}
::option[`C-x k`]{#emacs-buffer-kill explanation="Cette séquence demande quel tampon fermer au lieu d'en afficher un dans la fenêtre sélectionnée."}
:::

## Diviser la fenêtre sélectionnée

Utilisez `C-x 2` pour diviser la fenêtre sélectionnée en une fenêtre supérieure et une fenêtre inférieure :

```text
C-x 2
```

Utilisez `C-x 3` pour la diviser en fenêtres gauche et droite :

```text
C-x 3
```

La nouvelle fenêtre affiche initialement un tampon, souvent le même. Vous pouvez changer indépendamment le tampon de chaque fenêtre.

:::single-choice{#emacs-split-side-by-side}
Quelle séquence de touches divise la fenêtre Emacs sélectionnée en fenêtres gauche et droite ?

::option[`C-x 1`]{#emacs-window-one explanation="Cette séquence supprime les autres fenêtres et fait de la fenêtre sélectionnée la seule de son cadre."}
::option[`C-x 2`]{#emacs-window-below explanation="Cette séquence crée des fenêtres supérieure et inférieure, et non une division côte à côte."}
::option[`C-x 3`]{#emacs-window-right .correct explanation="`split-window-right`, associé à `C-x 3`, crée des fenêtres gauche et droite."}
:::

## Sélectionner et fermer des fenêtres

Utilisez `C-x o`, qui exécute `other-window`, pour sélectionner la fenêtre suivante :

```text
C-x o
```

Utilisez les commandes suivantes pour retirer des affichages de fenêtres :

- `C-x 0` : supprimer la fenêtre sélectionnée ;
- `C-x 1` : supprimer les autres fenêtres du cadre actuel.

La suppression d'une fenêtre laisse normalement en vie le tampon qu'elle affichait. Vous pourrez donc le réafficher dans une autre fenêtre.

:::single-choice{#emacs-select-other-window}
Quelle séquence de touches déplace le point et le focus clavier vers une autre fenêtre Emacs ?

::option[`C-x 0`]{#emacs-delete-selected-window explanation="Cette séquence supprime la fenêtre sélectionnée au lieu de déplacer le focus vers une autre."}
::option[`C-x o`]{#emacs-other-window .correct explanation="`other-window` sélectionne à tour de rôle une autre fenêtre du cadre."}
::option[`C-x b`]{#emacs-switch-in-window explanation="Cette séquence change le tampon affiché par la fenêtre actuelle, pas la fenêtre sélectionnée."}
:::

:::single-choice{#emacs-keep-one-window}
Quelle séquence de touches conserve la fenêtre sélectionnée et supprime les autres fenêtres de son cadre ?

::option[`C-x 1`]{#emacs-delete-other-windows .correct explanation="`delete-other-windows` fait de la fenêtre sélectionnée la seule fenêtre du cadre."}
::option[`C-x 0`]{#emacs-delete-current-window explanation="Cette séquence supprime la fenêtre sélectionnée elle-même au lieu de la conserver."}
::option[`C-x 2`]{#emacs-add-lower-window explanation="Cette séquence ajoute une fenêtre au lieu de réduire le cadre à une seule."}
:::

## Fermer un tampon

Utilisez `C-x k`, qui exécute `kill-buffer`, pour demander quel tampon retirer d'Emacs :

```text
C-x k
```

Le tampon actuel est proposé par défaut. Si un tampon associé à un fichier contient des changements non enregistrés, Emacs affiche un avertissement avant de le fermer. Lisez la demande : fermer un tampon modifié peut faire perdre des changements.

Fermer un tampon diffère de supprimer une fenêtre. Emacs remplace un tampon fermé dans toutes les fenêtres qui l'affichaient, tandis que la suppression d'une fenêtre peut laisser son tampon intact.

:::single-choice{#emacs-kill-buffer-key}
Quelle séquence de touches demande quel tampon Emacs fermer ?

::option[`C-x 0`]{#emacs-kill-window-only explanation="Cette séquence supprime l'affichage d'une fenêtre, mais laisse normalement le tampon en vie."}
::option[`C-x k`]{#emacs-kill-buffer-answer .correct explanation="`kill-buffer` retire le tampon choisi d'Emacs après toute confirmation requise concernant ses modifications."}
::option[`C-x b`]{#emacs-kill-switch explanation="Cette séquence affiche un tampon nommé dans la fenêtre actuelle et ne le ferme pas."}
:::

Exercez-vous avec `*scratch*` et des tampons jetables. Avant de fermer un tampon associé à un fichier, vérifiez si son indicateur de modification signale un travail non enregistré.

## Résumé

Vous savez maintenant gérer ce qu'Emacs stocke et ce que chaque fenêtre affiche.

1. Changer le tampon de la fenêtre sélectionnée avec `C-x b`.
2. Diviser vers le bas avec `C-x 2` ou vers la droite avec `C-x 3`.
3. Sélectionner une autre fenêtre avec `C-x o`.
4. Retirer des fenêtres avec `C-x 0` ou `C-x 1`.
5. Fermer un tampon avec `C-x k` seulement après avoir examiné les changements non enregistrés.
