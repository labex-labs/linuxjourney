---
lesson_id: "emacs-editing"
course_id: "advanced-text-fu"
lang: "fr"
order_index: 12
title: "Édition Emacs"
description: "Apprenez à déplacer le point, activer une région et utiliser les commandes du kill ring d'Emacs pour modifier du texte."
meta_title: "Édition Emacs - Maîtrise Avancée du Texte"
meta_description: "Maîtrisez les fondamentaux de l'édition Emacs avec ce guide pour débutants. Apprenez les commandes Emacs essentielles pour la navigation, la coupe et le collage de texte dans cet éditeur de texte puissant sous Linux."
meta_keywords: "Emacs, tutoriel Emacs, commandes Emacs, éditeur de texte, éditeur Linux, navigation Emacs, Emacs débutant, guide Emacs"
---

Emacs appelle **point** la position actuelle du curseur. Les commandes de déplacement repositionnent le point ; les commandes d'édition insèrent, suppriment, coupent, copient ou collent du texte autour de lui. Dans la notation ci-dessous, `C-` signifie Contrôle et `M-` signifie Méta, généralement Alt.

## Se déplacer par caractères et lignes

Les touches fléchées et d'autres touches de navigation de la plateforme peuvent fonctionner, mais les commandes de déplacement standard d'Emacs restent disponibles dans les sessions graphiques comme dans les terminaux :

- `C-f` : avancer d'un caractère ;
- `C-b` : reculer d'un caractère ;
- `C-n` : aller à la ligne suivante ;
- `C-p` : aller à la ligne précédente ;
- `C-a` : aller au début de la ligne ;
- `C-e` : aller à la fin de la ligne.

:::single-choice{#emacs-edit-next-line} Quelle touche Emacs déplace le point vers la ligne suivante ?

::option[`C-p`]{#emacs-edit-previous-line explanation="`C-p` va à la ligne précédente, dans le sens opposé."}
::option[`C-n`]{#emacs-edit-next-line-answer .correct explanation="`C-n`, pour « next-line », descend le point à la position correspondante de la ligne d'écran suivante."}
::option[`C-f`]{#emacs-edit-forward-character explanation="`C-f` avance d'un caractère au lieu de passer à la ligne suivante."}
:::

## Se déplacer par mots et limites du tampon

Les commandes Méta parcourent des unités plus grandes :

- `M-f` : avancer d'un mot ;
- `M-b` : reculer d'un mot ;
- `M-<` : aller au début du tampon ;
- `M->` : aller à la fin du tampon.

Sur de nombreux claviers, Alt joue le rôle de Méta. Si cette combinaison n'est pas disponible, appuyer sur `Esc`, puis sur la touche suivante envoie souvent la commande Méta équivalente.

:::single-choice{#emacs-edit-buffer-end} Quelle touche Emacs déplace le point à la fin du tampon ?

::option[`C-e`]{#emacs-edit-line-end explanation="`C-e` va à la fin de la ligne actuelle, pas à celle de tout le tampon."}
::option[`M-<`]{#emacs-edit-buffer-start explanation="`M-<` va au début du tampon."}
::option[`M->`]{#emacs-edit-buffer-end-answer .correct explanation="`M->` déplace le point à la fin du tampon actuel."}
:::

## Définir une région

La **marque** est une position mémorisée dans le tampon. Le texte entre le point et la marque est la **région**. Appuyez sur `C-SPC`, parfois noté `C-space`, pour exécuter `set-mark-command`, puis déplacez le point afin d'étendre la région active.

Dans un terminal, `C-SPC` peut être codé sous la forme `C-@`. Le surlignage dépend des réglages de marque transitoire, mais le point et la marque définissent toujours une région.

:::single-choice{#emacs-edit-set-mark} Quelle touche commence à définir une région en plaçant la marque au point ?

::option[`C-w`]{#emacs-edit-kill-region-before-mark explanation="`C-w` coupe une région déjà définie ; cette commande ne place pas la marque initiale."}
::option[`C-y`]{#emacs-edit-yank-before-mark explanation="`C-y` insère du texte provenant du kill ring et ne commence pas une sélection."}
::option[`C-SPC`]{#emacs-edit-control-space .correct explanation="`set-mark-command` place la marque ; les déplacements modifient ensuite la région comprise entre la marque et le point."}
:::

## Couper ou copier une région

Emacs stocke les textes coupés et copiés dans le **kill ring** :

- `C-w` : couper la région active, en la retirant et en l'ajoutant au kill ring ;
- `M-w` : copier la région active dans le kill ring sans la retirer ;
- `C-k` : couper du point à la fin de la ligne ; des utilisations répétées peuvent inclure le saut de ligne.

La coupe va au-delà d'une suppression ordinaire, car le texte retiré est conservé en vue d'un collage ultérieur.

:::single-choice{#emacs-edit-copy-region} Quelle touche copie la région active dans le kill ring sans la retirer ?

::option[`M-w`]{#emacs-edit-copy-active-region .correct explanation="`kill-ring-save`, associé à `M-w`, copie la région sans la supprimer."}
::option[`C-w`]{#emacs-edit-kill-active-region explanation="`C-w` retire la région tout en l'enregistrant dans le kill ring."}
::option[`C-k`]{#emacs-edit-kill-line explanation="`C-k` coupe le texte vers la fin de la ligne au lieu de copier la région sélectionnée sans la modifier."}
:::

## Coller depuis le kill ring

Utilisez `C-y` pour coller au point l'entrée la plus récente du kill ring. Immédiatement après ce collage, `M-y` remplace le texte inséré par une entrée plus ancienne ; la répétition de `M-y` parcourt les entrées.

```text
C-y
M-y
```

Si une autre commande sans rapport intervient après `C-y`, `M-y` ne dispose plus du même contexte de remplacement de collage.

:::single-choice{#emacs-edit-yank-latest} Quelle touche insère au point l'entrée la plus récente du kill ring ?

::option[`C-y`]{#emacs-edit-yank-answer .correct explanation="`yank`, associé à `C-y`, insère le dernier texte du kill ring dans le tampon actuel."}
::option[`M-y`]{#emacs-edit-yank-pop explanation="`M-y` remplace normalement une entrée qui vient d'être collée par une entrée plus ancienne ; cette commande dépend du collage précédent."}
::option[`C-d`]{#emacs-edit-delete-character explanation="`C-d` supprime le caractère après le point et ne récupère pas de texte du kill ring."}
:::

Exercez-vous dans `*scratch*` ou un fichier jetable : déplacez le point, placez la marque, copiez une région, coupez-en une autre, puis recollez-les. N'enregistrez que si le fichier obtenu mérite d'être conservé.

## Résumé

Vous savez maintenant parcourir et réorganiser du texte dans Emacs avec le point, la marque et le kill ring.

1. Se déplacer par caractères ou lignes avec les commandes Contrôle.
2. Se déplacer par mots ou limites de tampon avec les commandes Méta.
3. Placer la marque avec `C-SPC` pour définir une région.
4. Couper avec `C-w` ou copier avec `M-w`.
5. Coller avec `C-y`, puis parcourir immédiatement les entrées avec `M-y`.
