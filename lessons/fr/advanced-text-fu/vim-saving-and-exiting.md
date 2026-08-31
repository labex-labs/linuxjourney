---
lesson_id: "vim-saving-and-exiting"
course_id: "advanced-text-fu"
lang: "fr"
order_index: 8
title: "Sauvegarder et Quitter Vim"
description: "Apprenez à écrire, quitter, enregistrer sous un autre nom ou abandonner volontairement les modifications d'un tampon Vim."
meta_title: "Sauvegarder et Quitter Vim - Maîtrise Avancée du Texte"
meta_description: "Apprenez à sauvegarder dans l'éditeur Vim avec des commandes comme :w. Maîtrisez la sauvegarde et la fermeture avec :wq ou ZZ. Ce guide couvre les commandes essentielles linux wq et vi write and quit pour une gestion efficace des fichiers dans Vim."
meta_keywords: "vim comment sauvegarder, linux wq, vi écrire et quitter, vim comment sauvegarder et quitter, comment sauvegarder dans l'éditeur vim, sauvegarder fichier vim, quitter vim, commandes vim"
---

L'écriture et la fermeture sont deux opérations distinctes dans Vim. Avant de saisir une commande Ex, appuyez sur `Esc` pour revenir au mode Normal, tapez `:`, saisissez la commande, puis appuyez sur Entrée. Lisez le message d'état ou d'erreur de Vim avant de considérer qu'une écriture a réussi.

## Écrire le tampon actuel

Utilisez `:w` pour écrire le tampon actuel dans le fichier qui lui est associé sans fermer la fenêtre :

```vim
:w
```

Une écriture peut échouer si le tampon n'a pas de nom, si le répertoire n'est pas accessible en écriture, si le système de fichiers est plein ou si une autre condition l'empêche. Consultez le message affiché par Vim.

`:w copy.txt` écrit le tampon actuel vers un autre chemin tout en conservant son nom existant. Utilisez `:saveas copy.txt` si le tampon doit adopter le nouveau chemin.

:::single-choice{#vim-save-without-quit}
Quelle commande Vim écrit le tampon actuel dans son fichier associé sans quitter ?

::option[`:q`]{#vim-save-q explanation="`:q` demande la fermeture et n'écrit pas un tampon modifié."}
::option[`:w`]{#vim-save-w .correct explanation="La commande `:write` enregistre le tampon actuel et laisse la fenêtre d'édition ouverte."}
::option[`:q!`]{#vim-save-q-force explanation="`:q!` abandonne les modifications non enregistrées et quitte ; cette commande ne les sauvegarde pas."}
:::

## Quitter un tampon non modifié

Utilisez `:q` pour fermer la fenêtre actuelle lorsqu'aucune modification non enregistrée du tampon ne sera perdue :

```vim
:q
```

Si le tampon actuel est modifié et que ses changements seraient perdus, Vim refuse normalement et affiche un avertissement. Cette protection vous laisse la possibilité d'écrire ou de reconsidérer l'opération.

:::single-choice{#vim-quit-clean-buffer}
Quelle commande ferme la fenêtre Vim actuelle lorsqu'aucune modification non enregistrée ne risque d'être perdue ?

::option[`:w`]{#vim-quit-w explanation="Cette commande écrit le tampon, mais laisse la fenêtre actuelle ouverte."}
::option[`:q`]{#vim-quit-q .correct explanation="La commande de fermeture ordinaire ferme la fenêtre lorsque les protections de Vim concernant les tampons modifiés l'autorisent."}
::option[`u`]{#vim-quit-u explanation="En mode Normal, `u` annule une modification et ne ferme pas la fenêtre de l'éditeur."}
:::

## Abandonner les modifications non enregistrées

N'utilisez `:q!` que si vous souhaitez réellement fermer la fenêtre actuelle et abandonner les changements qui empêcheraient autrement sa fermeture :

```vim
:q!
```

Le point d'exclamation ignore l'avertissement relatif aux modifications non enregistrées. Celles-ci ne sont pas écrites ; vérifiez donc qu'elles sont bien jetables avant d'appuyer sur Entrée.

:::single-choice{#vim-quit-discard-changes}
Le tampon actuel contient des changements que vous ne souhaitez volontairement pas enregistrer. Quelle commande ferme la fenêtre en les abandonnant ?

::option[`:q`]{#vim-discard-plain-q explanation="`:q` seul refuse normalement de fermer si l'opération ferait perdre les modifications du tampon."}
::option[`:wq`]{#vim-discard-wq explanation="`:wq` écrit les changements avant de quitter, soit l'inverse de leur abandon."}
::option[`:q!`]{#vim-discard-q-force .correct explanation="Le point d'exclamation ignore l'avertissement de modification et ferme sans écrire les changements."}
:::

## Écrire et quitter ensemble

Utilisez `:wq` lorsque le tampon doit être écrit, puis la fenêtre actuelle fermée après une écriture réussie :

```vim
:wq
```

Si l'écriture échoue, Vim ne termine pas la fermeture demandée. Corrigez l'erreur au lieu de supposer que les données ont atteint le disque.

:::single-choice{#vim-write-and-quit}
Quelle commande écrit le tampon actuel, puis ferme la fenêtre si l'écriture réussit ?

::option[`:wq`]{#vim-save-wq .correct explanation="Cette commande combine l'écriture et la fermeture ; cette dernière dépend de la réussite de l'écriture."}
::option[`:q!`]{#vim-save-force-quit explanation="Cette commande quitte en abandonnant les changements au lieu de les écrire."}
::option[`:w copy.txt`]{#vim-save-copy explanation="Cette commande écrit vers un autre chemin, mais garde la fenêtre d'édition ouverte."}
:::

## Utiliser :x et ZZ

`:x` n'écrit le tampon que s'il est modifié, puis quitte. En mode Normal, `ZZ` en majuscules réalise la même opération :

```vim
:x
```

```text
ZZ
```

Ce comportement diffère légèrement de `:wq`, qui demande une écriture même si le tampon n'a pas changé. `ZQ` en majuscules est la commande du mode Normal qui quitte sans écrire, comme `:q!`.

:::single-choice{#vim-write-if-modified-quit}
Quelle commande du mode Normal n'écrit que si le tampon est modifié, puis quitte ?

::option[`ZZ`]{#vim-save-zz .correct explanation="`ZZ` en majuscules produit le comportement « écrire si modifié, puis quitter » de `:x`."}
::option[`zz`]{#vim-center-screen explanation="`zz` en minuscules recentre la ligne actuelle dans la fenêtre ; cette commande n'enregistre pas et ne quitte pas."}
::option[`ZQ`]{#vim-quit-zq explanation="`ZQ` en majuscules quitte sans écrire ; les changements non enregistrés sont donc abandonnés."}
:::

Avec plusieurs fenêtres ou tampons, une commande peut ne fermer que la fenêtre actuelle. Des commandes comme `:qa`, `:wqa` et `:qa!` agissent sur toutes les fenêtres, mais examinez chaque tampon modifié avant d'utiliser une commande forcée globale.

Pour vous exercer à écrire et quitter avec un fichier jetable, essayez ce laboratoire :

1. **[Modifier des fichiers texte sous Linux avec Vim et Nano](https://labex.io/fr/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** — Entraînez-vous à créer, modifier et enregistrer des fichiers, ainsi qu'à naviguer avec Vim et Nano, notamment pour maîtriser l'enregistrement et la fermeture.

## Résumé

Vous savez maintenant choisir la commande de sortie de Vim adaptée au sort voulu pour les données non enregistrées.

1. Écrire sans quitter avec `:w`.
2. Quitter sans risque avec `:q` lorsqu'aucune modification ne sera perdue.
3. Abandonner volontairement les changements avec `:q!`.
4. Écrire et quitter avec `:wq`.
5. Utiliser `:x` ou `ZZ` pour n'écrire que si le tampon est modifié.
