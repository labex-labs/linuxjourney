---
lesson_id: "alias-command"
course_id: "command-line"
lang: "fr"
order_index: 18
title: "alias"
description: "Apprenez à créer, inspecter, conserver, contourner et supprimer des alias de commandes dans Bash."
meta_title: "alias - Ligne de commande"
meta_description: "Apprenez la commande Linux alias avec des exemples pour créer des alias temporaires, enregistrer des alias dans .bashrc, lister les alias et les supprimer avec unalias."
meta_keywords: "commande linux alias, commande alias, alias bash, alias .bashrc, commande unalias, raccourci commande linux, alias shell"
---

Un alias demande à un shell interactif de remplacer le premier mot d'une commande par une autre chaîne avant d'exécuter la ligne. Il peut raccourcir une commande fréquente ou fournir un ensemble d'options préféré.

## Créer un alias dans le shell actuel

Dans Bash, définissez un alias avec `alias NAME='REPLACEMENT'`, sans espace autour du signe égal :

```bash
$ alias ll='ls -la'
```

Après cette définition, `ll` utilisé comme commande se développe en `ls -la`. Les guillemets maintiennent le remplacement groupé pendant la définition.

Les alias conviennent aux substitutions simples de préfixes de commandes. Employez une fonction shell si vous devez traiter les arguments de manière plus structurée.

:::single-choice{#define-ll-alias} Quelle commande Bash définit `ll` comme alias de `ls -la` dans le shell actuel ?

::option[`alias ll = 'ls -la'`]{#alias-spaces explanation="Les espaces autour de `=` divisent la définition en mots distincts ; Bash ne reçoit donc pas une affectation d'alias valide."}
::option[`alias ll='ls -la'`]{#alias-ll .correct explanation="Cette commande emploie la forme requise `NAME=REPLACEMENT` et cite le remplacement qui contient un espace."}
::option[`unalias ll='ls -la'`]{#unalias-definition explanation="`unalias` supprime des noms d'alias existants ; elle ne crée pas de remplacement."}
:::

## Charger un alias dans les futures sessions Bash

Un alias défini à l'invite appartient au shell actuel et disparaît à sa fermeture. Les sessions Bash interactives sans connexion lisent normalement `~/.bashrc` ; ce fichier est donc l'emplacement habituel des alias personnels :

```bash
alias ll='ls -la'
```

Après avoir modifié le fichier, démarrez une nouvelle session Bash interactive ou rechargez-le dans le shell actuel :

```bash
$ source ~/.bashrc
```

Le démarrage dépend du shell, du mode de connexion et de la distribution. Un utilisateur de Zsh emploiera normalement la configuration de Zsh plutôt que le `.bashrc` de Bash.

:::single-choice{#persist-bash-alias} Où faut-il normalement définir un alias personnel pour que les futures sessions Bash interactives sans connexion le chargent ?

::option[Dans le fichier `~/.bashrc` de l'utilisateur.]{#bashrc-alias .correct explanation="Bash interactif sans connexion lit normalement `~/.bashrc`, qui est donc l'emplacement conventionnel des alias personnels."}
::option[Dans le fichier exécutable utilisé par la commande associée.]{#edit-executable explanation="Modifier un exécutable installé n'a aucun rapport avec le développement des alias et peut endommager des fichiers gérés par le système."}
::option[Dans l'historique de défilement du terminal actuel.]{#terminal-scrollback explanation="L'historique de défilement ne fait qu'enregistrer le texte affiché ; Bash ne l'exécute pas comme configuration de démarrage."}
:::

## Inspecter les alias et la résolution des noms

Exécutez `alias` sans argument pour lister les alias du shell actuel :

```bash
$ alias
alias ll='ls -la'
alias grep='grep --color=auto'
```

Utilisez `type NAME` pour examiner comment Bash résout un nom :

```bash
$ type ll
ll is aliased to 'ls -la'
```

:::single-choice{#inspect-command-alias} Quelle commande indique si Bash résout actuellement `ll` comme alias, fonction, commande intégrée ou exécutable ?

::option[`file ll`]{#file-ll explanation="`file` classe un chemin du système de fichiers. Un alias réside dans l'état du shell et ne correspond pas nécessairement à un fichier `ll`."}
::option[`type ll`]{#type-ll .correct explanation="La commande intégrée `type` indique comment la session Bash actuelle résout le nom `ll`."}
::option[`whatis ll`]{#whatis-ll explanation="`whatis` interroge les descriptions des pages de manuel ; les alias personnels n'ont normalement aucune entrée dans cette base."}
:::

## Contourner et supprimer un alias

Pour contourner un alias sur une ligne, préfixez le nom par une barre oblique inverse ou placez-le après la commande intégrée `command` de Bash :

```bash
$ \ls
$ command ls
```

Cette méthode permet d'obtenir le comportement normal de la commande sous-jacente. Gardez des alias courts et prévisibles, et ne dissimulez pas de comportement surprenant ou destructeur derrière un nom familier.

:::single-choice{#bypass-ls-alias} La session Bash actuelle possède un alias `ls`. Quelle commande le contourne pour une seule invocation ?

::option[`alias ls`]{#show-ls-alias explanation="Cette commande affiche la définition de l'alias `ls` sans invoquer la commande sous-jacente."}
::option[`command ls`]{#command-ls .correct explanation="Puisque `command` est le premier mot, Bash ne développe pas le `ls` suivant comme alias et applique la résolution normale."}
::option[`source ls`]{#source-ls explanation="`source` lit un fichier comme code shell dans la session actuelle ; ce n'est pas une méthode sûre ou adaptée pour contourner un alias."}
:::

Supprimez un alias du shell actuel avec `unalias` :

```bash
$ unalias ll
```

Si sa définition reste dans `~/.bashrc`, un futur shell pourra le recréer. Retirez ou modifiez également cette ligne de configuration pour supprimer l'alias durablement.

:::single-choice{#remove-current-alias} Quelle commande supprime l'alias `ll` de la session Bash actuelle ?

::option[`unalias ll`]{#unalias-ll .correct explanation="`unalias` retire l'alias nommé de la table d'alias du shell actuel."}
::option[`alias ll=''`]{#empty-ll explanation="Cette commande remplace l'alias par un développement vide au lieu de supprimer sa définition."}
::option[`command ll`]{#command-ll explanation="`command` peut contourner le développement d'un alias sur cette ligne, mais ne le supprime pas de l'état du shell."}
:::

## Résumé

Vous savez maintenant personnaliser Bash avec des alias simples et inspectables.

1. Définir un alias temporaire avec des guillemets corrects.
2. Charger les alias personnels depuis `~/.bashrc` dans les futures sessions.
3. Inspecter les alias et la résolution des commandes.
4. Contourner un alias pour une invocation.
5. Supprimer les définitions active et enregistrée si nécessaire.
