---
lesson_id: "vim-text-editor"
course_id: "advanced-text-fu"
lang: "fr"
order_index: 3
title: "Vim (Vi Amélioré)"
description: "Découvrez ce qu'est Vim, son lien avec vi et la manière d'ouvrir des fichiers, l'aide et un tutoriel guidé."
meta_title: "Vim (Vi Amélioré) - Maîtrise Avancée du Texte"
meta_description: "Découvrez Vim, l'éditeur de texte puissant et léger connu sous le nom de vi improved. Ce tutoriel présente les bases de Vim, un outil préinstallé sur la plupart des systèmes Linux."
meta_keywords: "Vim, vi amélioré, vim vi amélioré, éditeur de texte Linux, tutoriel Vim, éditeur Vi, vim amélioré, commandes Linux"
---

Vim est un éditeur de texte configurable dont le nom signifie **Vi Improved**, ou « Vi amélioré ». Il conserve le modèle d'édition modal associé à l'éditeur `vi` d'origine et y ajoute notamment l'annulation multiniveau, la prise en charge de la syntaxe, un langage de script et un vaste système d'aide.

## Comprendre le lien entre Vim et vi

`vi` désigne à la fois un éditeur historique et une interface de commande courante. Sur un système Linux, `vi` peut lancer Vim dans un mode axé sur la compatibilité ; sur un autre, il peut lancer une autre implémentation de vi. Ne supposez donc pas que toutes les commandes `vi` proposent toutes les fonctionnalités de Vim.

Vérifiez ce que résout le shell actuel :

```bash
$ command -v vim
/usr/bin/vim
$ command -v vi
/usr/bin/vi
```

Les chemins résolus ne permettent pas à eux seuls de savoir si `vi` et `vim` sont la même implémentation. `type -a vi vim` et les informations de version de l'éditeur peuvent fournir davantage de détails.

:::single-choice{#vim-name-origin} Que signifie le nom Vim ?

::option[Visual Input Manager]{#vim-visual-input explanation="Ce développement n'est pas à l'origine du nom de l'éditeur."}
::option[Virtual Interface Mode]{#vim-virtual-interface explanation="Vim utilise bien des modes, mais cette expression n'est pas la signification de son nom."}
::option[Vi Improved]{#vim-vi-improved .correct explanation="Vim est né comme un éditeur amélioré compatible avec vi, ce que rappelle son nom."}
:::

:::single-choice{#vim-check-command} Quelle commande vérifie si Bash peut actuellement résoudre le nom `vim` ?

::option[`vim --create`]{#vim-create-option explanation="Cette option ne vérifie pas la résolution par le shell et ne sert ni à installer ni à découvrir Vim."}
::option[`command -v vim`]{#vim-command-resolution .correct explanation="Cette commande intégrée au shell indique la commande qui serait employée pour ce nom, si elle est disponible."}
::option[`file ~/.vimrc`]{#vim-file-vimrc explanation="Cette commande examine un éventuel fichier de configuration, sans déterminer si l'exécutable Vim est disponible."}
:::

## Ouvrir Vim et des fichiers

Démarrez Vim avec un tampon sans nom :

```bash
$ vim
```

Fournissez un chemin pour modifier ce fichier :

```bash
$ vim filename.txt
```

Si `filename.txt` existe et est lisible, Vim charge son contenu dans un tampon. Si le chemin n'existe pas, Vim ouvre un nouveau tampon associé à ce nom ; aucun fichier n'est créé tant que vous n'avez pas enregistré le tampon avec succès.

Vim ne contourne pas les permissions du système de fichiers. Ouvrir un fichier ne garantit donc pas que votre compte pourra enregistrer les modifications à cet emplacement.

:::single-choice{#vim-open-missing-path} Que se passe-t-il normalement lorsque `vim draft.txt` indique un chemin qui n'existe pas encore ?

::option[Vim ouvre un nouveau tampon et ne crée le fichier que lors de son enregistrement.]{#vim-new-buffer .correct explanation="Le chemin est mémorisé pour le tampon, mais la création sur le disque attend un enregistrement réussi."}
::option[Vim crée un fichier vide sur le disque avant d'ouvrir son interface.]{#vim-immediate-create explanation="Le nouveau tampon est associé au chemin, mais le fichier n'est créé qu'après une écriture réussie."}
::option[Vim refuse de démarrer, car chaque chemin doit déjà exister.]{#vim-refuse-missing explanation="Vim peut ouvrir un nouveau tampon pour un chemin absent afin de vous laisser composer un nouveau fichier."}
:::

## Utiliser les ressources d'apprentissage intégrées

Si l'installation de Vim comprend `vimtutor`, lancez-le depuis le shell pour suivre une leçon interactive :

```bash
$ vimtutor
```

Dans Vim, passez en mode Normal avec `Esc`, tapez `:help`, puis appuyez sur Entrée pour ouvrir l'aide. Vous pouvez préciser un sujet après la commande :

```vim
:help user-manual
:help :write
```

Les étiquettes de l'aide sont précises ; la ponctuation peut donc compter. Utilisez `Ctrl+]` sur un lien de l'aide pour le suivre et `Ctrl+T` pour revenir.

:::single-choice{#vim-guided-tutorial} Quelle commande du shell lance le tutoriel guidé de Vim lorsqu'il est installé ?

::option[`vim --quiz`]{#vim-quiz-option explanation="Cette option n'est pas l'interface standard du tutoriel guidé de Vim."}
::option[`vimtutor`]{#vim-tutor-command .correct explanation="`vimtutor` ouvre une copie du tutoriel interactif conçu pour un apprentissage pratique sans risque."}
::option[`help vim`]{#vim-shell-help explanation="La commande `help` de Bash documente ses commandes intégrées ; elle ne lance pas le tutoriel interactif de Vim."}
:::

## S'exercer avec un fichier jetable

Commencez par un fichier placé dans un répertoire qui vous appartient :

```bash
$ printf 'alpha\nbeta\n' > vim-practice.txt
$ vim vim-practice.txt
```

Les leçons suivantes présentent la recherche, la navigation, l'insertion, la modification et l'enregistrement. Tant que vous ne savez pas quitter sans risque, retenez que `Esc` ramène au mode Normal et que `:q!`, suivi d'Entrée, abandonne les modifications non enregistrées de la fenêtre actuelle. N'utilisez cette commande que si vous souhaitez réellement perdre ces changements.

:::single-choice{#vim-abandon-practice-changes} Dans un fichier d'essai jetable, quelle commande Vim ferme la fenêtre actuelle en abandonnant ses modifications non enregistrées ?

::option[`:w`]{#vim-write-only explanation="`:w` écrit le tampon, mais ne ferme pas la fenêtre actuelle."}
::option[`:wq`]{#vim-write-quit explanation="`:wq` enregistre les modifications avant de quitter ; elle ne les abandonne donc pas."}
::option[`:q!`]{#vim-quit-force .correct explanation="Le `!` demande à Vim d'ignorer l'avertissement concernant le tampon modifié et de quitter sans écrire ces changements."}
:::

Pour vous exercer à ouvrir, modifier et enregistrer des fichiers avec Vim, essayez ce laboratoire :

1. **[Modifier des fichiers texte sous Linux avec Vim et Nano](https://labex.io/fr/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** — Entraînez-vous à créer, modifier et enregistrer des fichiers, ainsi qu'à naviguer avec Vim et Nano dans un véritable environnement Linux.

## Résumé

Vous savez maintenant identifier Vim, ouvrir un tampon et trouver des ressources d'apprentissage sûres.

1. Expliquer le lien entre Vim et vi sans présumer de l'implémentation.
2. Vérifier si la commande `vim` est disponible.
3. Ouvrir un fichier existant ou un nouveau tampon nommé.
4. Lancer `vimtutor` ou ouvrir l'aide intégrée à Vim.
5. N'abandonner les modifications d'un exercice que volontairement.
