---
lesson_id: "history-command"
course_id: "command-line"
lang: "fr"
order_index: 9
title: "history"
description: "Apprenez à consulter, rechercher, réutiliser et gérer l'historique des commandes dans Bash."
meta_title: "history - Ligne de commande"
meta_description: "Apprenez la commande history sous Linux avec des exemples pour afficher l'historique des commandes, relancer des commandes, recherche inversée, suppression d'entrées et nettoyage du terminal."
meta_keywords: "commande linux history, historique bash, history -c, history -d, history -w, Ctrl-R, historique des commandes, commande clear"
---

Les shells interactifs peuvent conserver les commandes saisies. Cette leçon porte sur Bash, dont la commande intégrée `history` affiche et gère cet historique. Les autres shells peuvent employer des raccourcis, fichiers ou réglages différents.

## Afficher l'historique Bash

Exécutez `history` pour afficher la liste actuelle :

```bash
$ history
  101  pwd
  102  ls -la
  103  cat notes.txt
```

Chaque ligne contient un numéro d'historique suivi de la commande.

:::single-choice{#show-command-history}
Quelle commande Bash affiche la liste actuelle et numérotée de l'historique ?

::option[`clear`]{#clear-display explanation="`clear` rafraîchit la zone visible du terminal ; elle n'affiche pas les commandes précédentes."}
::option[`history -w`]{#write-history explanation="`history -w` écrit la liste actuelle dans le fichier d'historique. Elle sert à l'enregistrer, pas à l'afficher."}
::option[`history`]{#show-history .correct explanation="La commande intégrée `history` affiche les commandes de la liste actuelle, normalement avec leur numéro."}
:::

## Réutiliser les commandes précédentes

Bash fournit plusieurs raccourcis pour rappeler ou exécuter immédiatement des commandes :

- **Flèche haut** : rappeler des commandes antérieures pour les examiner ou les modifier ;
- **`!!`** : développer et exécuter la commande la plus récente ;
- **exécution par numéro** : `!102` exécute la commande numéro 102 de l'historique ;
- **exécution par préfixe** : `!cat` exécute la commande la plus récente qui commence par `cat`.

Les développements d'historique qui commencent par `!` peuvent exécuter une commande dès l'appui sur Entrée. En cas de doute, inspectez d'abord la correspondance, surtout avant d'ajouter des privilèges ou d'agir sur des fichiers importants.

:::single-choice{#repeat-most-recent-command}
Quel développement de l'historique Bash répète la dernière commande exécutée ?

::option[`!102`]{#event-number explanation="Ce développement sélectionne la commande portant le numéro 102, qui n'est pas nécessairement la plus récente."}
::option[`!cat`]{#event-prefix explanation="Ce développement choisit la commande la plus récente dont le texte commence par `cat`, pas la dernière commande de n'importe quel type."}
::option[`!!`]{#previous-event .correct explanation="Dans Bash, `!!` se développe en commande précédente et l'exécute après la validation de la ligne."}
:::

## Rechercher interactivement dans l'historique

Appuyez sur `Ctrl+R` pour commencer une recherche incrémentale inversée, puis tapez une partie de la commande recherchée. Appuyez de nouveau sur `Ctrl+R` pour atteindre une correspondance plus ancienne.

Entrée exécute la correspondance affichée. Pour l'examiner ou la modifier d'abord, utilisez une touche fléchée afin de placer la commande sur la ligne d'édition.

:::single-choice{#search-before-executing}
Vous vous souvenez d'une partie d'une ancienne commande Bash et voulez la retrouver interactivement. Quelle touche devez-vous utiliser d'abord ?

::option[`Ctrl+D`]{#end-input explanation="`Ctrl+D` signale une fin d'entrée dans de nombreux contextes et peut fermer un shell inactif ; elle ne lance pas une recherche d'historique."}
::option[`Ctrl+C`]{#cancel-input explanation="`Ctrl+C` interrompt ou annule normalement l'opération actuelle ; elle ne recherche pas dans l'historique."}
::option[`Ctrl+R`]{#reverse-search .correct explanation="`Ctrl+R` commence une recherche incrémentale inversée dans l'historique. Les caractères saisis ensuite affinent la correspondance."}
:::

## Gérer la liste d'historique

La commande intégrée `history` peut modifier ou enregistrer la liste actuelle :

- `history -c` : effacer la liste actuelle en mémoire ;
- `history -w` : écrire la liste actuelle dans le fichier d'historique configuré, généralement `~/.bash_history` ;
- `history -d <position>` : supprimer l'entrée à la position indiquée.

Exemples :

```bash
$ history -d 101
$ history -w
```

Effacer la liste en mémoire ne garantit pas à lui seul la disparition des anciennes commandes de chaque fichier, sauvegarde ou autre shell actif. Le comportement dépend aussi des réglages de Bash et du moment où les sessions lisent ou écrivent leurs fichiers.

:::single-choice{#save-current-history-list}
Quelle commande écrit la liste d'historique Bash actuelle dans le fichier configuré ?

::option[`history -c`]{#clear-current-list explanation="L'option `-c` efface la liste en mémoire ; elle ne demande pas d'enregistrer son contenu actuel."}
::option[`history -d 101`]{#delete-one-entry explanation="L'option `-d` supprime une entrée choisie ; elle n'enregistre pas toute la liste."}
::option[`history -w`]{#write-current-list .correct explanation="L'option `-w` écrit la liste d'historique actuelle dans le fichier configuré."}
:::

## Effacer l'affichage et compléter les noms

Utilisez `clear` pour retrouver une zone visible vide :

```bash
$ clear
```

Cette commande n'efface pas la liste d'historique de Bash. Selon le terminal, l'ancien affichage peut également rester accessible dans l'historique de défilement.

La complétion par Tab évite aussi de tout ressaisir. Commencez une commande ou un nom de fichier ou de répertoire, puis appuyez sur Tab. Bash peut compléter une correspondance sans ambiguïté ou présenter les possibilités s'il en existe plusieurs.

Les lignes de commande pouvant être conservées dans l'historique, n'y placez pas directement de mots de passe, jetons ou autres secrets lorsqu'une méthode de saisie plus sûre existe.

:::single-choice{#distinguish-clear-from-history-clear}
Vous voulez rafraîchir l'affichage du terminal sans supprimer l'historique des commandes en mémoire. Quelle commande faut-il exécuter ?

::option[`clear`]{#clear-visible-area .correct explanation="`clear` rafraîchit la zone visible du terminal tout en laissant intacte la liste d'historique Bash en mémoire."}
::option[`history -c`]{#clear-memory explanation="Cette commande retire les entrées de la liste en mémoire ; elle modifie l'historique au lieu de seulement rafraîchir l'affichage."}
::option[`history -d 1`]{#delete-first-entry explanation="Cette commande demande à Bash de supprimer une entrée choisie ; elle n'efface pas la zone visible du terminal."}
:::

## Résumé

Vous savez maintenant retrouver et réutiliser des commandes Bash tout en gérant l'historique avec discernement.

1. Afficher la liste actuelle et numérotée de l'historique.
2. Rappeler ou développer prudemment une ancienne commande.
3. Rechercher interactivement avec `Ctrl+R`.
4. Supprimer, effacer ou écrire des entrées d'historique.
5. Distinguer l'historique des commandes de l'affichage du terminal.
