---
lesson_id: "emacs-text-editor"
course_id: "advanced-text-fu"
lang: "fr"
order_index: 9
title: "Emacs"
description: "Apprenez à démarrer Emacs, à lire sa notation de touches et à distinguer tampons, fenêtres et cadres."
meta_title: "Emacs - Maîtrise avancée du texte"
meta_description: "Apprenez Emacs, un éditeur de texte puissant et extensible pour Linux. Comprenez les tampons Emacs et l'utilisation de base. Commencez votre voyage Emacs dès aujourd'hui !"
meta_keywords: "Emacs, éditeur de texte Linux, tutoriel Emacs, tampons Emacs, commandes Linux, débutant, guide"
---

GNU Emacs est un éditeur de texte extensible dont le comportement peut être personnalisé avec Emacs Lisp. Il prend en charge l'édition de texte brut, les modes de programmation, la gestion des fichiers et des tampons, ainsi que de nombreux paquets facultatifs. Vous pouvez apprendre ses commandes d'édition essentielles sans adopter toutes ses extensions.

## Vérifier et démarrer Emacs

Ne supposez pas qu'Emacs est installé. Vérifiez comment le shell résout sa commande :

```bash
$ command -v emacs
/usr/bin/emacs
```

Démarrez Emacs avec sa sélection d'affichage normale :

```bash
$ emacs
```

Dans une session graphique, cette commande peut créer un cadre graphique. Utilisez `-nw`, abréviation de « no window system », si Emacs doit rester dans le terminal actuel :

```bash
$ emacs -nw
```

:::single-choice{#emacs-terminal-start} Quelle commande démarre Emacs dans le terminal actuel plutôt qu'avec un système de fenêtres graphique ?

::option[`emacs -w`]{#emacs-window-option explanation="Ce n'est pas la forme documentée ici pour désactiver le système de fenêtres."}
::option[`emacs -nw`]{#emacs-no-window .correct explanation="L'option `-nw` demande à Emacs de ne pas utiliser de système de fenêtres graphique et de fonctionner dans le terminal."}
::option[`command -v emacs`]{#emacs-check-only explanation="Cette commande vérifie la résolution du nom, mais ne démarre pas l'éditeur."}
:::

## Ouvrir un fichier

Fournissez un chemin pour ouvrir un fichier au démarrage d'Emacs :

```bash
$ emacs notes.txt
```

Si le fichier existe, Emacs le lit dans un tampon. S'il est absent, Emacs crée un nouveau tampon associé à ce chemin ; le fichier ne sera créé qu'après un enregistrement réussi. Les permissions du système de fichiers déterminent toujours si l'écriture peut aboutir.

:::single-choice{#emacs-open-file-buffer} Que fait normalement `emacs notes.txt` si `notes.txt` n'existe pas encore ?

::option[Il ouvre un nouveau tampon associé à ce chemin.]{#emacs-new-file-buffer .correct explanation="Le tampon peut contenir le nouveau texte de `notes.txt`, tandis que la création réelle du fichier attend l'enregistrement."}
::option[Il crée le fichier sur le disque avant de démarrer l'éditeur.]{#emacs-immediate-file explanation="Emacs peut associer un nouveau tampon au chemin sans créer le fichier sur le disque avant la réussite d'un enregistrement."}
::option[Il refuse de démarrer, car chaque fichier ouvert doit exister.]{#emacs-refuse-new-file explanation="Emacs permet de composer de nouveaux fichiers dans des tampons associés à des chemins absents."}
:::

## Comprendre les tampons, les fenêtres et les cadres

Emacs utilise des objets liés mais distincts :

- un **tampon** contient du texte ou un autre état de l'éditeur ; le contenu d'un fichier ouvert réside dans un tampon ;
- une **fenêtre** est une zone d'un cadre Emacs qui affiche un tampon ;
- un **cadre** est un affichage Emacs de premier niveau, graphique ou dans un terminal.

Plusieurs tampons peuvent exister sans être visibles, et deux fenêtres peuvent afficher le même tampon. Fermer une fenêtre ne détruit pas nécessairement son tampon et ne supprime aucun fichier.

:::single-choice{#emacs-buffer-definition} Qu'est-ce qu'un tampon Emacs ?

::option[Un cadre d'application graphique de premier niveau.]{#emacs-buffer-frame explanation="Le cadre est l'objet d'affichage de premier niveau ; le tampon contient le contenu ou l'état de l'éditeur."}
::option[Un objet qui contient du texte modifiable ou un autre état de l'éditeur.]{#emacs-buffer-content .correct explanation="Le contenu des fichiers ouverts et de nombreuses vues sans fichier résident dans des tampons Emacs."}
::option[Un fichier d'historique du shell contenant les commandes précédentes.]{#emacs-buffer-history explanation="L'historique du shell est distinct du stockage des tampons Emacs."}
:::

## Lire la notation des touches d'Emacs

La documentation d'Emacs emploie une notation compacte :

- `C-x` signifie maintenir Contrôle et appuyer sur `x` ;
- `M-x` signifie maintenir Méta et appuyer sur `x` ; Alt joue généralement le rôle de Méta dans les terminaux et bureaux modernes ;
- `C-x C-f` est une séquence : appuyez sur Contrôle+x, puis sur Contrôle+f.

Le terminal utilisé peut intercepter ou réaffecter certaines touches. `Esc` suivi d'une touche peut souvent remplacer une combinaison avec Méta.

:::single-choice{#emacs-key-sequence-notation} Comment saisit-on la séquence Emacs notée `C-x C-f` ?

::option[Maintenir Contrôle pour `x`, puis maintenir Contrôle pour `f`.]{#emacs-control-x-f .correct explanation="Chaque préfixe `C-` s'applique à la touche qui le suit, et les deux combinaisons sont saisies l'une après l'autre."}
::option[Saisir les caractères littéraux `C-x C-f` dans le tampon.]{#emacs-literal-key-text explanation="Cette notation décrit des événements de touches de contrôle, pas du texte à insérer."}
::option[Maintenir simultanément Contrôle, `x` et `f` en une seule combinaison.]{#emacs-simultaneous-x-f explanation="La notation contient deux combinaisons successives et non une seule combinaison de trois touches."}
:::

## Démarrer le tutoriel intégré

Dans Emacs, saisissez `C-h t` pour ouvrir le tutoriel interactif. Il enseigne les déplacements, l'insertion, l'enregistrement et la fermeture dans un tampon d'exercice sûr. `C-h` est le préfixe de l'aide ; `C-h C-h` affiche une aide sur l'utilisation de l'aide.

Si Emacs affiche un menu ou un tampon d'accueil, le tutoriel reste un point de départ mieux structuré que l'expérimentation sur un fichier important.

:::single-choice{#emacs-open-tutorial} Quelle séquence de touches Emacs ouvre le tutoriel intégré ?

::option[`C-x C-s`]{#emacs-save-buffer explanation="Cette séquence enregistre le tampon actuel ; elle n'ouvre pas le tutoriel."}
::option[`C-x C-c`]{#emacs-exit-sequence explanation="Cette séquence commence à quitter Emacs au lieu de lancer une leçon."}
::option[`C-h t`]{#emacs-help-tutorial .correct explanation="Le préfixe d'aide `C-h`, suivi de `t`, démarre le tutoriel d'Emacs."}
:::

## Résumé

Vous savez maintenant démarrer Emacs et interpréter les concepts fondamentaux de son interface.

1. Vérifier si la commande `emacs` est disponible.
2. Choisir le fonctionnement graphique ou en terminal avec `-nw`.
3. Ouvrir un chemin existant ou nouveau dans un tampon.
4. Distinguer les tampons, les fenêtres et les cadres.
5. Lire la notation des touches et ouvrir le tutoriel intégré.
