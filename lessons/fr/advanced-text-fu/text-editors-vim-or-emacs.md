---
lesson_id: "text-editors-vim-or-emacs"
course_id: "advanced-text-fu"
lang: "fr"
order_index: 2
title: "Éditeurs de texte"
description: "Apprenez à choisir et à configurer un éditeur de texte en terminal pour l'administration et le développement sous Linux."
meta_title: "Éditeurs de texte - Maîtrise avancée du texte"
meta_description: "Découvrez les éditeurs de texte Linux comme Vim et Emacs. Découvrez leurs utilisations et leur importance pour la navigation système. Commencez votre parcours avec les éditeurs de texte Linux !"
meta_keywords: "éditeurs de texte Linux, Vim, Emacs, commandes Linux, tutoriel Linux, Linux débutant, guide Linux"
---

Les configurations Linux, les scripts, le code source et les journaux sont généralement stockés sous forme de texte brut. Un éditeur en terminal permet de travailler sur ces fichiers depuis un terminal local, une session SSH distante ou un environnement dépourvu de bureau graphique.

## Choisir un éditeur adapté à l'environnement

Aucun éditeur n'est le meilleur pour tout le monde ni pour toutes les tâches. Les éditeurs graphiques, les éditeurs en terminal et les environnements de développement intégrés peuvent tous convenir. Pour travailler en ligne de commande, choisissez un éditeur installé, dont vous savez sortir sans risque et dont vous comprenez le fonctionnement élémentaire.

Ne supposez pas que Vim ou Emacs est installé. Vérifiez la résolution des commandes dans le shell actuel :

```bash
$ command -v vim
/usr/bin/vim
$ command -v emacs
/usr/bin/emacs
```

Une sortie vide accompagnée d'un état différent de zéro signifie que ce nom n'a pas été trouvé par la recherche de commandes actuelle. Les systèmes minimaux peuvent fournir `vi`, tandis que d'autres proposent Nano, voire aucun éditeur interactif.

:::single-choice{#editors-check-availability} Quelle commande vérifie si le shell actuel peut résoudre un exécutable nommé `vim` ?

::option[`vim --install`]{#editors-vim-install explanation="Vim n'utilise pas cette commande comme vérification d'installation portable, et l'installation des paquets dépend de la distribution."}
::option[`file ~/.vimrc`]{#editors-file-vimrc explanation="Cette commande identifie le type d'un fichier de configuration s'il existe ; elle ne détermine pas si `vim` peut être résolu."}
::option[`command -v vim`]{#editors-command-v-vim .correct explanation="Cette commande intégrée au shell vérifie la résolution d'une commande et affiche sa forme résolue lorsqu'elle est disponible."}
:::

## Comprendre le modèle de Vim

Vim est un éditeur modal. Une même touche peut avoir un sens différent selon le mode actif :

- le mode Normal interprète les touches comme des commandes de navigation et d'édition ;
- le mode Insertion insère le texte saisi ;
- le mode Ligne de commande accepte des commandes comme l'enregistrement ou la fermeture.

Avec de la pratique, ce modèle rend les modifications répétitives au clavier efficaces, mais les nouveaux utilisateurs doivent surveiller le mode actif. Les leçons suivantes présentent les opérations de Vim une par une.

:::single-choice{#editors-vim-modal-meaning} Que signifie le fait que Vim soit modal ?

::option[Chaque fichier s'ouvre dans une fenêtre graphique distincte.]{#editors-vim-windows explanation="Les fenêtres et les tampons sont des concepts différents. Le caractère modal concerne la variation du rôle des touches selon l'état de l'éditeur."}
::option[Vim ne peut modifier qu'un seul type de fichier texte à la fois.]{#editors-vim-file-type explanation="Vim prend en charge de nombreux types de fichiers. Le terme modal décrit son modèle d'interaction, pas une restriction sur les fichiers."}
::option[Les touches effectuent des actions différentes selon le mode actif.]{#editors-vim-modes .correct explanation="Par exemple, une touche peut lancer une commande en mode Normal, mais insérer du texte en mode Insertion."}
:::

## Comprendre le modèle d'Emacs

Emacs emploie généralement des combinaisons de touches et des commandes nommées au sein d'un environnement extensible. Les fichiers sont ouverts dans des tampons, et les modes majeurs et mineurs adaptent le comportement à différents contenus et travaux. Emacs peut fonctionner dans un terminal ou dans une fenêtre graphique.

Vim et Emacs vont tous deux bien au-delà de l'édition élémentaire grâce à leur configuration et à leurs extensions. Commencez par ouvrir, modifier, enregistrer et fermer un fichier texte brut avant d'ajouter des personnalisations.

:::single-choice{#editors-emacs-buffer} Dans la terminologie d'Emacs, où se trouve normalement le texte modifiable d'un fichier ouvert ?

::option[Dans un tampon.]{#editors-emacs-buffer-answer .correct explanation="Emacs ouvre un fichier dans un tampon, qui contient le texte affiché ou modifié."}
::option[Dans la table d'alias du shell.]{#editors-emacs-alias-table explanation="Les alias appartiennent à la résolution des commandes du shell et ne stockent pas le texte de l'éditeur."}
::option[Uniquement dans l'historique d'affichage du terminal.]{#editors-emacs-scrollback explanation="L'historique du terminal conserve la sortie affichée, tandis qu'Emacs gère le texte modifiable dans des tampons."}
:::

## Définir un éditeur préféré

De nombreux programmes en ligne de commande consultent `VISUAL` ou `EDITOR` lorsqu'ils doivent lancer un éditeur. Par exemple, choisissez Vim pour les commandes exécutées depuis la session Bash actuelle et ses processus enfants :

```bash
$ export VISUAL=vim
$ export EDITOR="$VISUAL"
```

Ces variables expriment une préférence ; elles n'installent pas le programme. Indiquez une commande qui existe réellement et n'ajoutez ces exportations au fichier de démarrage approprié du shell qu'après les avoir testées.

:::single-choice{#editors-editor-variable} Quel est l'effet de `export EDITOR=vim` ?

::option[Il indique aux futurs processus enfants que `vim` est l'éditeur préféré.]{#editors-export-preference .correct explanation="L'exportation place cette préférence dans l'environnement hérité par les commandes lancées depuis le shell actuel."}
::option[Il installe Vim pour tous les utilisateurs du système.]{#editors-install-vim explanation="L'affectation d'une variable d'environnement n'installe aucun paquet et ne modifie pas le système des autres utilisateurs."}
::option[Il impose les raccourcis de Vim à tous les programmes.]{#editors-global-bindings explanation="Les programmes peuvent consulter la variable pour lancer un éditeur, mais elle ne remplace pas leur propre modèle d'interaction."}
:::

## S'exercer sans risquer des fichiers importants

Apprenez sur un fichier jetable situé dans un répertoire qui vous appartient :

```bash
$ printf 'first line\nsecond line\n' > editor-practice.txt
$ vim editor-practice.txt
```

Évitez de commencer avec une configuration système ou les données d'un autre utilisateur. Sauvegardez tout fichier important avant de le modifier, apprenez à enregistrer et à quitter, puis contrôlez le résultat avec une commande en lecture seule comme `cat` ou `diff`.

:::single-choice{#editors-first-practice-file} Quel fichier est le plus sûr pour découvrir un éditeur inconnu ?

::option[Un fichier de démarrage critique ouvert en tant que root.]{#editors-boot-file explanation="Une modification accidentelle pourrait empêcher un démarrage normal, et les privilèges élevés aggravent les conséquences d'une erreur."}
::option[Un fichier texte jetable dans un répertoire qui vous appartient.]{#editors-disposable-file .correct explanation="Un fichier d'essai limite les conséquences d'une modification accidentelle pendant l'apprentissage de la navigation, de l'enregistrement et de la fermeture."}
::option[Un fichier de production partagé dépourvu de sauvegarde.]{#editors-production-file explanation="S'exercer sans contrôle sur des données partagées peut perturber d'autres personnes et ne laisse aucun moyen simple de revenir en arrière."}
:::

Pour vous exercer à ouvrir, modifier et enregistrer des fichiers texte dans un terminal, essayez ce laboratoire :

1. **[Modifier des fichiers texte sous Linux avec Vim et Nano](https://labex.io/fr/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** — Entraînez-vous à créer et modifier des fichiers, à les enregistrer et à naviguer avec vi/vim et nano, des compétences essentielles pour tout utilisateur Linux.

## Résumé

Vous savez maintenant choisir un éditeur en terminal et préparer une méthode d'apprentissage sans risque.

1. Vérifier si une commande d'éditeur est disponible.
2. Reconnaître le modèle d'interaction modal de Vim.
3. Comprendre les tampons et les modes extensibles d'Emacs.
4. Définir une préférence d'éditeur sans la confondre avec une installation.
5. S'exercer sur du texte jetable avant de modifier des fichiers importants.
