---
lesson_id: "user-management-tools"
course_id: "user-management"
lang: "fr"
order_index: 6
title: "Outils de gestion des utilisateurs"
description: "Apprenez à créer, modifier, sécuriser, vérifier et supprimer des comptes locaux avec des options explicites."
meta_title: "Outils de gestion des utilisateurs - Gestion des utilisateurs"
meta_description: "Maîtrisez useradd, usermod, userdel et passwd pour gérer les comptes Linux en sécurité."
meta_keywords: "gestion utilisateurs Linux, useradd, usermod, userdel, passwd, comptes Linux"
---

Les distributions fournissent couramment les outils de la suite shadow, mais leurs valeurs par défaut et leurs enveloppes varient. Avant tout changement, confirmez que le compte n'est pas géré centralement, lisez le manuel local et gardez une voie de récupération.

Les commandes de cette leçon modifient authentification et propriété. Exercez-vous uniquement dans un environnement jetable autorisé, jamais sur un hôte de production.

## Examiner les valeurs par défaut de création

`useradd` crée un compte local à partir des options et réglages du site :

```bash
$ useradd -D
```

`/etc/default/useradd`, `/etc/login.defs` et le contenu squelette peuvent influencer le résultat selon la distribution. Une commande `adduser` de plus haut niveau peut exister, mais son interface n'est pas standard partout.

## Créer explicitement un compte local

Dans un environnement contrôlé :

```bash
$ sudo useradd -m -s /bin/bash -c "Bob Example" bob
```

- `-m` demande la création du répertoire personnel.
- `-s /bin/bash` choisit le shell après vérification de sa présence et de son autorisation.
- `-c` renseigne le commentaire GECOS.

Le compte ne peut généralement pas utiliser un mot de passe local avant sa définition, mais l'état initial dépend des outils et de la politique. Vérifiez plutôt que supposer :

```bash
$ getent passwd bob
$ sudo passwd -S bob
$ id bob
```

:::single-choice{#user-tools-create-home} Quelle option de `useradd` demande explicitement la création du répertoire personnel ?

::option[`-M`]{#user-tools-no-home-option explanation="`-M` demande explicitement de ne pas créer le répertoire sur les implémentations courantes."}
::option[`-s`]{#user-tools-shell-option explanation="`-s` choisit le shell de connexion."}
::option[`-m`]{#user-tools-home-option .correct explanation="`-m` demande la création et le peuplement du répertoire selon les réglages locaux."}
:::

## Définir ou changer un mot de passe

```bash
$ passwd
```

Un administrateur autorisé peut définir le mot de passe d'un autre compte avec :

```bash
$ sudo passwd bob
```

Un utilisateur change son propre mot de passe avec la première commande ; un administrateur autorisé change celui de `bob` avec la seconde. Saisissez les secrets uniquement dans l'invite protégée, jamais dans les arguments, l'historique, des notes ou un chat. PAM peut refuser les mots de passe faibles ou réutilisés ; les comptes d'annuaire peuvent exiger un autre outil.

:::single-choice{#user-tools-change-own-password} Quelle commande permet normalement à l'utilisateur courant de changer son mot de passe dans une invite interactive ?

::option[`useradd`]{#user-tools-add-not-password explanation="`useradd` crée un compte ; ce n'est pas l'outil interactif ordinaire de changement."}
::option[`userdel`]{#user-tools-delete-not-password explanation="`userdel` supprime un compte local."}
::option[`passwd`]{#user-tools-passwd-self .correct explanation="Sans nom, `passwd` agit sur le mot de passe local de l'appelant selon PAM."}
:::

## Modifier les propriétés et groupes

```bash
$ sudo usermod -s /bin/zsh bob
$ sudo usermod -d /srv/home/bob -m bob
$ sudo usermod -aG developers bob
```

Avant un déplacement de répertoire, vérifiez destination, propriété, espace, processus, montages et services. Pour les groupes supplémentaires, `-aG` ajoute à la liste ; `-G` sans `-a` la remplace et peut supprimer des accès. Les changements concernent normalement les nouvelles sessions, pas les processus déjà actifs.

:::single-choice{#user-tools-append-group} Quelle commande ajoute `bob` au groupe supplémentaire `developers` sans remplacer ses autres appartenances ?

::option[`usermod -G developers bob`]{#user-tools-replace-groups explanation="Sans `-a`, `-G` remplace la liste et peut supprimer les groupes existants."}
::option[`usermod -aG developers bob`]{#user-tools-append-groups .correct explanation="`-a` ajoute le groupe désigné par `-G` en préservant les autres."}
::option[`groupdel developers bob`]{#user-tools-delete-group explanation="`groupdel` supprime une définition de groupe et n'ajoute aucun membre."}
:::

## Verrouiller un mot de passe local

Un administrateur peut verrouiller le hachage avec `passwd -l USER`, inspecter avec `passwd -S USER` et déverrouiller avec `passwd -u USER` après analyse de la raison et du hachage restant.

Ce verrou ne bloque pas nécessairement clés SSH, jetons, tâches planifiées, processus actifs ou authentification propre à un service. Pour désactiver complètement un compte, définissez les menaces et coordonnez expiration, shell, services, clés et sessions.

:::single-choice{#user-tools-password-lock-scope} Que verrouille principalement `passwd -l bob` ?

::option[Toutes les voies possibles d'authentification et d'exécution.]{#user-tools-lock-everything explanation="Clés, jetons, tâches, services et sessions peuvent exiger d'autres contrôles."}
::option[Tous les fichiers appartenant à l'UID de Bob.]{#user-tools-lock-files explanation="L'état du mot de passe ne change ni la propriété ni l'accès aux données."}
::option[Le hachage Unix local utilisé par l'authentification par mot de passe.]{#user-tools-lock-local-password .correct explanation="La commande préfixe ou désactive ce hachage afin d'empêcher sa vérification normale."}
:::

## Supprimer délibérément un compte local

`userdel bob` retire normalement les enregistrements mais laisse le répertoire personnel. `userdel -r bob` tente aussi de supprimer celui-ci et la boîte locale : c'est destructeur.

Avant toute suppression :

1. Confirmez le compte avec `getent passwd bob` et `id bob`.
2. Repérez processus, tâches, services, clés et accès délégués.
3. Inventoriez les fichiers appartenant à l'UID sur les systèmes visés.
4. Décidez du transfert, archivage, maintien ou effacement sûr des données.
5. Évitez la réattribution de l'UID tant que des fichiers orphelins subsistent.

`userdel -r` ne garantit pas la suppression des fichiers hors du répertoire et de la boîte configurés. Il peut rester propriétés numériques, autorisations de bases, identités applicatives et comptes distants.

:::single-choice{#user-tools-userdel-r-scope} Que demande couramment `userdel -r bob` en plus de `userdel bob` ?

::option[Tous les fichiers de l'UID sur tous les systèmes montés.]{#user-tools-delete-all-owned explanation="L'outil ne découvre ni n'efface universellement tous les fichiers appartenant à l'UID."}
::option[Tous les comptes distants également nommés `bob`.]{#user-tools-delete-remote explanation="`userdel` agit sur les bases locales applicables."}
::option[Le répertoire personnel et la boîte locale de Bob, en plus des enregistrements.]{#user-tools-delete-home-mail .correct explanation="L'option cible ces emplacements configurés, pas tout objet possédé ailleurs."}
:::

Pour vous exercer :

1. **[Gérer les comptes Linux avec useradd, usermod et userdel](https://labex.io/fr/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Pratiquez tout le cycle de vie des comptes.
2. **[Gérer les groupes Linux](https://labex.io/fr/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Ajoutez, modifiez et supprimez des groupes.
3. **[Configurer les comptes et privilèges sudo](https://labex.io/fr/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Sécurisez les comptes et droits administratifs.

## Résumé

Vous savez gérer les comptes locaux avec une portée explicite et des vérifications.

1. Examiner les valeurs par défaut de `useradd`.
2. Demander explicitement répertoire, shell et métadonnées.
3. Changer les mots de passe uniquement par une invite protégée.
4. Ajouter des groupes sans remplacer la liste existante.
5. Inventorier les dépendances avant une suppression destructive.
