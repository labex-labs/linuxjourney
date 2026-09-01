---
lesson_id: "emacs-manipulate-files"
course_id: "advanced-text-fu"
lang: "fr"
order_index: 10
title: "Emacs Manipuler les Fichiers"
description: "Apprenez à ouvrir, enregistrer, renommer, recharger et examiner les tampons associés à des fichiers dans Emacs."
meta_title: "Emacs Manipuler les Fichiers - Text-Fu Avancé"
meta_description: "Apprenez la manipulation de fichiers Emacs : enregistrer, enregistrer sous et ouvrir des fichiers en utilisant les commandes C-x C-s, C-x C-w et C-x C-f. Maîtrisez les opérations essentielles de fichiers Emacs !"
meta_keywords: "Emacs, enregistrer fichier Emacs, ouvrir fichier Emacs, tutoriel Emacs, commandes Linux, Emacs débutant, guide Emacs"
---

Emacs ouvre les fichiers dans des tampons. Une modification change d'abord le tampon ; l'enregistrement écrit son contenu actuel vers le chemin associé. Lisez les messages du minibuffer, car les permissions, des modifications concurrentes sur le disque ou d'autres erreurs peuvent empêcher l'écriture.

## Ouvrir un fichier

Utilisez `C-x C-f`, qui exécute `find-file`, puis saisissez un chemin dans le minibuffer et appuyez sur Entrée :

```text
C-x C-f
```

Emacs ouvre un fichier existant et lisible dans un tampon, ou prépare un nouveau tampon associé au fichier si le chemin est absent. Dans ce second cas, aucun fichier n'existe sur le disque avant la réussite d'un enregistrement.

Vous pouvez utiliser la complétion avec Tab pendant la saisie d'un chemin. L'ouverture d'un répertoire lance normalement Dired, l'éditeur de répertoires d'Emacs, au lieu de traiter ce répertoire comme un fichier texte.

:::single-choice{#emacs-find-file-key} Quelle séquence de touches Emacs demande un chemin puis l'ouvre ?

::option[`C-x C-s`]{#emacs-file-save explanation="Cette séquence enregistre le tampon actuel associé à un fichier et ne demande pas d'ouvrir un autre chemin."}
::option[`C-x C-c`]{#emacs-file-exit explanation="Cette séquence commence à quitter Emacs au lieu d'ouvrir un fichier."}
::option[`C-x C-f`]{#emacs-find-file .correct explanation="Cette séquence exécute `find-file` et demande dans le minibuffer le chemin à ouvrir."}
:::

:::single-choice{#emacs-find-missing-file} Lorsque `C-x C-f` ouvre un chemin inexistant, quand le fichier est-il normalement créé sur le disque ?

::option[Seulement après l'enregistrement réussi du nouveau tampon.]{#emacs-file-created-on-save .correct explanation="Le tampon peut contenir des modifications avant l'existence du fichier ; l'enregistrement réalise sa création."}
::option[Immédiatement après la saisie du chemin.]{#emacs-file-created-immediately explanation="Emacs crée d'abord un tampon associé au nouveau chemin ; la création sur le disque est différée."}
::option[Seulement après la fermeture d'Emacs.]{#emacs-file-created-on-exit explanation="Quitter peut provoquer une demande d'enregistrement, mais la création dépend d'un enregistrement réussi et pas nécessairement de la fermeture."}
:::

## Enregistrer le tampon actuel

Utilisez `C-x C-s`, qui exécute `save-buffer`, pour enregistrer le tampon actuel associé à un fichier :

```text
C-x C-s
```

Si le tampon n'a pas de nom de fichier associé, Emacs en demande un. Une écriture réussie efface l'indicateur de modification du tampon ; en cas d'échec, les données non enregistrées restent dans le tampon et une erreur est signalée.

:::single-choice{#emacs-save-current-buffer} Quelle séquence de touches enregistre le tampon actuel associé à un fichier ?

::option[`C-x C-s`]{#emacs-save-buffer-key .correct explanation="`C-x C-s` exécute `save-buffer` pour le tampon actuel."}
::option[`C-x C-w`]{#emacs-write-file-key explanation="Cette séquence demande un autre nom de fichier et change le fichier ouvert par le tampon."}
::option[`C-x s`]{#emacs-save-some-key explanation="Cette séquence examine plusieurs tampons associés à des fichiers et demande lesquels enregistrer au lieu de ne cibler que le tampon actuel."}
:::

## Écrire sous un autre nom

Utilisez `C-x C-w`, qui exécute `write-file`, pour demander un chemin, y écrire le tampon et faire en sorte que celui-ci ouvre désormais le nouveau fichier :

```text
C-x C-w
```

Il s'agit du comportement « Enregistrer sous » d'Emacs. Il diffère de la simple écriture d'une copie séparée tout en continuant à ouvrir le chemin d'origine.

:::single-choice{#emacs-write-file-as} Quelle séquence de touches réalise l'opération habituelle « Enregistrer sous » pour le tampon actuel ?

::option[`C-x C-f`]{#emacs-find-file-other explanation="Cette séquence ouvre un fichier, éventuellement dans un autre tampon ; elle n'enregistre pas le tampon actuel sous un nouveau nom."}
::option[`C-x k`]{#emacs-write-as-kill-buffer explanation="Cette séquence demande de fermer un tampon et peut interroger sur les modifications non enregistrées ; elle n'enregistre pas sous un nouveau nom."}
::option[`C-x C-w`]{#emacs-write-file-answer .correct explanation="`write-file` écrit vers le chemin choisi et fait en sorte que le tampon ouvre ce fichier."}
:::

## Examiner plusieurs tampons modifiés

Utilisez `C-x s`, qui exécute `save-some-buffers`, pour examiner les tampons modifiés associés à des fichiers :

```text
C-x s
```

Emacs demande normalement s'il faut enregistrer chaque tampon modifié concerné. Lisez son nom et répondez avec discernement : ce n'est pas un raccourci qui enregistre tout sans confirmation.

:::single-choice{#emacs-save-some-buffers} Que fait normalement `C-x s` ?

::option[Il demande quels tampons modifiés associés à des fichiers doivent être enregistrés.]{#emacs-prompt-save-some .correct explanation="`save-some-buffers` examine les tampons modifiés concernés et demande lesquels doivent être écrits."}
::option[Il enregistre silencieusement tous les tampons sans afficher leurs noms.]{#emacs-silent-save-all explanation="La commande interactive normale pose des questions au lieu d'écrire tous les tampons sans condition."}
::option[Il ferme tous les tampons après avoir enregistré le tampon actuel.]{#emacs-close-all-buffers explanation="La commande porte sur l'enregistrement de plusieurs tampons et ne les ferme normalement pas."}
:::

## Recharger depuis le disque

Si un fichier a changé sur le disque et que vous souhaitez volontairement abandonner le contenu actuel du tampon, exécutez `M-x revert-buffer` et examinez la demande de confirmation. Le rechargement peut détruire les modifications non enregistrées du tampon ; ne l'utilisez qu'après avoir décidé quelle source doit l'emporter.

Avant de décider, vous pouvez enregistrer une copie séparée ou employer le contrôle de version et des outils de comparaison. Une opération de rechargement n'est pas anodine lorsque le tampon a été modifié.

## Résumé

Vous savez maintenant gérer les tampons associés à des fichiers sans confondre ouverture et écriture.

1. Ouvrir un chemin avec `C-x C-f`.
2. Ne créer un fichier absent qu'à l'enregistrement de son tampon.
3. Enregistrer le tampon actuel avec `C-x C-s`.
4. L'enregistrer sous un nouveau nom ouvert avec `C-x C-w`.
5. Examiner plusieurs tampons modifiés avec `C-x s`.
