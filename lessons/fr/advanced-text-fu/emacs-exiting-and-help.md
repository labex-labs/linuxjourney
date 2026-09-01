---
lesson_id: "emacs-exiting-and-help"
course_id: "advanced-text-fu"
lang: "fr"
order_index: 13
title: "Emacs Quitter et Aide"
description: "Apprenez à quitter Emacs sans risque, annuler une commande en cours, consulter l'aide et défaire des modifications."
meta_title: "Emacs Quitter et Aide - Maîtrise Avancée du Texte"
meta_description: "Apprenez les commandes de sortie d'Emacs et comment accéder à l'aide. Comprenez les fonctions de navigation et d'annulation de base d'Emacs dans ce tutoriel convivial pour débutants."
meta_keywords: "Emacs quitter, Emacs aide, Emacs annuler, Emacs tutoriel, éditeur de texte Linux, guide du débutant"
---

Emacs fournit une aide contextuelle sur les touches, les fonctions, les variables et les modes actifs. Lors de la fermeture, il protège également les tampons modifiés associés à des fichiers et vous laisse enregistrer ou refuser chaque écriture.

## Quitter Emacs

Utilisez `C-x C-c`, qui exécute `save-buffers-kill-terminal`, pour demander la fermeture de la session Emacs ou de la connexion au terminal :

```text
C-x C-c
```

Emacs vérifie les tampons modifiés concernés qui sont associés à des fichiers et demande s'il faut les enregistrer. Lisez le nom de chaque tampon et répondez avec discernement. Il peut aussi vous interroger sur les processus actifs. Annulez la fermeture si vous devez examiner le travail avant de décider.

Dans un flux de travail avec `emacsclient` ou un serveur Emacs, le comportement exact du cadre et du serveur peut différer, mais les demandes concernant les tampons modifiés exigent toujours votre attention.

:::single-choice{#emacs-exit-key} Quelle séquence de touches demande une fermeture normale d'Emacs en vérifiant les tampons modifiés ?

::option[`C-x k`]{#emacs-exit-kill-buffer explanation="Cette séquence ferme un tampon sélectionné et ne demande pas la fermeture de la session Emacs."}
::option[`C-g`]{#emacs-exit-keyboard-quit explanation="Cette touche annule une commande ou une demande en cours au lieu de fermer Emacs."}
::option[`C-x C-c`]{#emacs-exit-save-buffers .correct explanation="Cette séquence exécute le flux normal d'enregistrement des tampons et de fermeture, avec des demandes pour le travail non enregistré concerné."}
:::

## Ouvrir le répartiteur de l'aide

Le préfixe d'aide standard est `C-h`. Utilisez `C-h C-h`, qui exécute l'aide sur l'aide, pour afficher les commandes d'assistance disponibles :

```text
C-h C-h
```

La seconde touche choisit le type d'aide recherché.

:::single-choice{#emacs-help-for-help} Quelle séquence de touches explique comment utiliser le système d'aide d'Emacs ?

::option[`C-h C-h`]{#emacs-help-help .correct explanation="Le préfixe d'aide suivi d'un autre `C-h` ouvre l'aide relative au répartiteur de l'aide lui-même."}
::option[`C-x C-h`]{#emacs-help-prefix-list explanation="Ce n'est pas la séquence d'aide sur l'aide présentée ici."}
::option[`C-h t`]{#emacs-help-tutorial-other explanation="Cette séquence ouvre directement le tutoriel au lieu d'expliquer le menu d'aide général."}
:::

## Décrire les touches et l'état de l'éditeur

Parmi les commandes d'aide utiles :

- `C-h k TOUCHE` : décrire la commande exécutée par une séquence de touches ;
- `C-h f FONCTION` : décrire une fonction Emacs Lisp ;
- `C-h v VARIABLE` : décrire une variable Emacs Lisp ;
- `C-h m` : décrire les modes majeur et mineurs actuels ;
- `C-h t` : ouvrir le tutoriel interactif.

Par exemple, saisissez `C-h k C-x C-s` pour afficher la documentation de la touche associée à `save-buffer`.

:::single-choice{#emacs-describe-key} Vous voulez savoir ce que fait `C-x C-s`. Quel préfixe d'aide devez-vous saisir avant cette séquence ?

::option[`C-h k`]{#emacs-describe-key-answer .correct explanation="`describe-key` attend une séquence de touches et explique la commande qui lui est associée."}
::option[`C-h f`]{#emacs-describe-function explanation="Cette séquence demande un nom de fonction au lieu de lire une séquence de touches pour identifier son association."}
::option[`C-h v`]{#emacs-describe-variable explanation="Cette séquence demande un nom de variable et n'examine pas une association de touches."}
:::

## Annuler une commande en attente

Utilisez `C-g`, associé à `keyboard-quit`, lorsque vous êtes bloqué dans une demande, une séquence de touches partiellement saisie, une recherche incrémentale ou toute autre commande que vous souhaitez annuler :

```text
C-g
```

Cette touche n'annule pas les modifications déjà apportées au tampon et ne quitte pas Emacs. Elle interrompt l'interaction actuelle et rend si possible le contrôle à l'édition ordinaire.

:::single-choice{#emacs-cancel-pending-command} Quelle touche annule normalement la demande ou la commande Emacs en cours ?

::option[`C-x C-c`]{#emacs-cancel-exit explanation="Cette séquence lance le flux de fermeture d'Emacs au lieu de simplement annuler la demande actuelle."}
::option[`C-y`]{#emacs-cancel-yank explanation="Cette touche colle du texte provenant du kill ring et n'annule pas une commande."}
::option[`C-g`]{#emacs-keyboard-quit-answer .correct explanation="`keyboard-quit` interrompt l'interaction de commande actuelle et rend le contrôle à Emacs."}
:::

## Annuler des modifications du tampon

Utilisez `C-/`, `C-_` ou `C-x u` pour invoquer l'annulation dans les configurations Emacs courantes :

```text
C-/
```

La répétition des commandes d'annulation remonte les modifications récentes du tampon. Le déplacement seul du curseur ne constitue normalement pas une modification. Les versions et configurations d'Emacs peuvent proposer `undo-redo` et des outils d'historique plus avancés ; utilisez `C-h k` sur vos touches d'annulation et de rétablissement afin de vérifier le comportement local.

:::single-choice{#emacs-undo-change} Quelle séquence de touches est une association standard pour annuler une modification récente du tampon Emacs ?

::option[`C-/`]{#emacs-undo-control-slash .correct explanation="`C-/` est une association standard d'annulation, avec `C-_` et `C-x u` dans les configurations courantes."}
::option[`C-x C-s`]{#emacs-undo-save explanation="Cette séquence enregistre le tampon actuel au lieu de parcourir son historique d'annulation."}
::option[`C-w`]{#emacs-undo-kill explanation="Cette touche coupe la région active et crée une nouvelle modification au lieu d'en annuler une."}
:::

Exercez-vous en ouvrant `*scratch*`, en apportant une modification jetable, en l'annulant, en interrogeant `C-h k` sur une touche inconnue et en annulant une demande du minibuffer avec `C-g`, avant de quitter normalement.

## Résumé

Vous savez maintenant obtenir de l'aide et quitter Emacs sans ignorer le travail non enregistré.

1. Passer par la vérification des tampons modifiés avec `C-x C-c`.
2. Ouvrir l'aide sur l'aide avec `C-h C-h`.
3. Décrire des touches, fonctions, variables ou modes actifs.
4. Annuler une commande en attente avec `C-g`.
5. Annuler les modifications récentes du tampon avec une association locale vérifiée.
