---
lesson_id: "root-user"
course_id: "user-management"
lang: "fr"
order_index: 2
title: "root"
description: "Découvrez comment su, sudo et la politique sudoers donnent un accès contrôlé aux identités privilégiées."
meta_title: "root - Gestion des utilisateurs"
meta_description: "Comprenez le rôle de root, les différences entre su et sudo et la gestion sûre de la politique sudoers."
meta_keywords: "root Linux, su, sudo, sudoers, visudo, superutilisateur"
---

Le compte traditionnellement nommé `root` possède l'UID 0 et une large autorité dans son contexte de sécurité. Travaillez normalement sans privilèges et ne les élevez que pour un objectif administratif précis et compris.

## Ouvrir un shell comme un autre utilisateur avec su

`su`, pour substitute user, lance un shell ou une commande avec l'identité d'un autre compte. Sans nom, la cible est root :

```bash
$ su
```

PAM et la politique locale contrôlent l'authentification. Le système peut demander le mot de passe cible, restreindre `su` ou garder le mot de passe root verrouillé.

Un simple `su` préserve davantage l'environnement courant. `su - USER`, ou `su --login USER`, initialise un shell de connexion plus proche d'une nouvelle session cible :

```bash
$ su - operator
```

Quittez ce sous-shell lorsque le travail est terminé.

:::single-choice{#root-su-login-shell} Quelle commande demande un shell de connexion comme `operator` ?

::option[`su - operator`]{#root-su-login-operator .correct explanation="Le tiret demande le comportement de connexion et un environnement orienté vers `operator`."}
::option[`su operator`]{#root-su-preserve-environment explanation="Cette forme change l'identité sans demander l'initialisation complète de connexion."}
::option[`sudo -l operator`]{#root-sudo-list-operator explanation="`sudo -l` liste les commandes permises ; il ne lance pas ce shell."}
:::

## Exécuter une commande précise avec sudo

`sudo COMMAND` demande l'autorisation d'exécuter une commande comme cible, souvent root. `-u USER` choisit une autre cible :

```bash
$ sudo -u postgres id
```

La politique contrôle l'appelant, l'hôte, la cible, la commande et d'autres conditions. L'authentification peut utiliser le mot de passe de l'appelant, un autre mécanisme ou aucune invite. Préférez une commande administrative étroitement définie à un shell privilégié durable.

:::single-choice{#root-sudo-target-user} Que demande `sudo -u postgres id` ?

::option[Renommer définitivement le compte courant en `postgres`.]{#root-sudo-rename explanation="`sudo` exécute une commande avec les attributs cibles sans renommer de compte."}
::option[Exécuter `id` avec `postgres` comme cible, sous réserve de la politique.]{#root-sudo-postgres-id .correct explanation="`-u` choisit l'identité cible et sudoers décide si la demande est permise."}
::option[Lister les utilisateurs dont l'UID dépasse celui de l'appelant.]{#root-sudo-list-uids explanation="`id` décrit les attributs de son processus ; cette syntaxe n'énumère pas les comptes."}
:::

## Éviter les shells privilégiés persistants

`su -`, `sudo -s` ou `sudo -i` peuvent créer un shell privilégié. Toute commande ultérieure conserve alors un fort impact jusqu'à la sortie : erreurs de chemin, scripts non examinés et développements du shell deviennent plus dangereux.

La journalisation dépend de la configuration. L'enregistrement du lancement d'un shell ne fournit pas automatiquement l'historique complet de toutes les commandes saisies ; historique shell, audit système et enregistrement d'E/S sudo sont distincts.

:::single-choice{#root-persistent-shell-risk} Pourquoi un shell root durable est-il plus risqué que l'élévation d'une commande comprise ?

::option[Il supprime automatiquement chaque commande de tous les audits.]{#root-shell-no-audit explanation="La journalisation varie ; tous les enregistrements ne sont pas automatiquement effacés."}
::option[Il interdit les chemins comportant plusieurs composants.]{#root-shell-path-limit explanation="Les privilèges n'imposent pas cette restriction."}
::option[Les commandes suivantes gardent un impact élevé jusqu'à la fermeture du shell.]{#root-shell-elevated-scope .correct explanation="La fenêtre privilégiée augmente le risque qu'une faute ou une commande non fiable modifie des ressources protégées."}
:::

## Examiner les autorisations sudo

```bash
$ sudo -l
```

Examinez les chemins de commandes, utilisateurs cibles permis et restrictions d'arguments. Une règle large ne constitue pas une permission pour un travail sans rapport.

:::single-choice{#root-list-sudo-rules} Quelle commande liste les privilèges sudo de l'utilisateur appelant ?

::option[`sudo -i`]{#root-sudo-login explanation="Cette forme demande un shell cible de type connexion et peut étendre les privilèges."}
::option[`sudo -l`]{#root-sudo-list .correct explanation="L'option `-l` demande à sudo de lister les commandes autorisées par la politique."}
::option[`su -l`]{#root-su-login-default explanation="Cette forme concerne le shell de connexion de `su`, pas les autorisations sudo."}
:::

## Modifier sûrement la politique sudoers

La politique par défaut lit souvent `/etc/sudoers` et des fichiers de `/etc/sudoers.d/`. Utilisez `visudo`, qui verrouille et valide la syntaxe :

```bash
$ sudo visudo
```

Pour un fichier complémentaire, indiquez son chemin exact :

```bash
$ sudo visudo -f /etc/sudoers.d/application-admins
```

N'utilisez ni redirection ordinaire ni flux d'édition non validé. Une erreur de syntaxe ou de permissions peut supprimer l'accès administratif. Gardez une voie de récupération vérifiée lors d'un changement distant.

:::single-choice{#root-edit-sudoers-safely} Quel outil faut-il employer pour modifier et vérifier la politique sudoers principale ?

::option[`cat`]{#root-cat-sudoers explanation="`cat` n'édite, ne verrouille ni ne valide la syntaxe."}
::option[`visudo`]{#root-visudo .correct explanation="`visudo` fournit le verrouillage et la validation conçus pour sudoers."}
::option[`echo` avec `>`]{#root-echo-sudoers explanation="La redirection peut tronquer immédiatement la politique sans validation."}
:::

Pour vous exercer :

1. **[Configurer les comptes et privilèges sudo sous Linux](https://labex.io/fr/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Sécurisez root et accordez des droits administratifs.

## Résumé

Vous savez distinguer changement d'identité et délégation contrôlée de commandes.

1. Employer `su - USER` seulement pour un shell de connexion cible.
2. Demander une cible sudo avec `-u USER`.
3. Réduire le temps passé dans un shell privilégié.
4. Examiner les règles avec `sudo -l`.
5. Modifier sudoers uniquement avec `visudo`.
