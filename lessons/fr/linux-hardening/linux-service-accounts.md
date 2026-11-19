---
lesson_id: "linux-service-accounts"
course_id: "linux-hardening"
lang: "fr"
order_index: 2
title: "Comptes de service"
description: "Apprenez à identifier le compte sous lequel tourne un processus Linux et à comprendre ses droits d’accès."
meta_title: "Comptes de service - Durcissement de Linux"
meta_description: "Apprenez à identifier le compte sous lequel tourne un processus Linux et à comprendre ses droits d’accès."
meta_keywords: "comptes de service, durcissement de Linux, cybersécurité, Linux Journey"
---

Un serveur web démarre sous forme de processus. Linux associe chaque processus à une identité qui contribue à déterminer ce que le programme peut lire ou modifier. Un **compte de service** est une identité réservée à un programme.

## Identifier le compte du processus

Dans un terminal ordinaire, `$$` donne l’identifiant du processus du shell. Utilisez-le pour voir sous quel compte tourne votre propre shell. L’option `-p` sélectionne ce processus et `-o` choisit les colonnes à afficher. Les signes égal suppriment les en-têtes des colonnes.

```bash
$ ps -p "$$" -o user=,comm=
```

Dans un terminal LabEx, le compte peut être `labex`. La colonne de commande indique le programme du shell. Pour un processus de service, les mêmes champs indiquent le compte utilisé, quelle que soit la personne qui l’a lancé.

:::single-choice{#linux-service-accounts-process-user} Quel champ indique le compte associé au processus sélectionné ?

::option[L’identifiant de processus fourni avec -p.]{#linux-service-accounts-process-user-a explanation="L’identifiant sélectionne un processus actif."}
::option[Le nom de la commande dans la dernière colonne.]{#linux-service-accounts-process-user-c explanation="Cette colonne nomme le programme en cours d’exécution."}
::option[Le champ utilisateur affiché par ps.]{#linux-service-accounts-process-user-b .correct explanation="Le champ utilisateur indique l’identité du processus."}
:::

![Sortie de ps montrant le processus du shell LabEx et son compte labex](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-service-accounts/shell-identity.png)

## Choisir un compte dédié

Prenons un service web dont les seules tâches sont de lire des pages et d’écrire dans son propre journal. Vous pouvez donner ces permissions à un compte dédié `site-web`. Les droits plus étendus d’un administrateur permettraient au programme de modifier davantage de choses sur l’hôte que ce dont il a besoin.

:::single-choice{#linux-service-accounts-isolate-service} Quels droits correspondent au travail du service ?

::option[Autoriser site-web à modifier les fichiers de tous les utilisateurs.]{#linux-service-accounts-isolate-service-b explanation="Aucune tâche du service n’exige un accès aussi large."}
::option[Autoriser site-web à lire les pages et à écrire dans son propre journal.]{#linux-service-accounts-isolate-service-a .correct explanation="Ces droits correspondent aux deux tâches indiquées."}
::option[Autoriser site-web à agir en administrateur pour chaque requête.]{#linux-service-accounts-isolate-service-c explanation="La plupart des requêtes ne nécessitent que les droits limités du service."}
:::

## Examiner les services à plusieurs processus

Certains services répartissent leurs tâches entre plusieurs processus. Repérez celui qui traite la requête avant de déterminer quels droits s’y appliquent. Si vous changez le compte d’exécution, vérifiez que le service peut encore lire ses données d’entrée et écrire uniquement là où il en a besoin.

:::single-choice{#linux-service-accounts-verify-identity} Un outil de maintenance indique que le processus superviseur tourne sous root. Comment savoir quel compte traite les requêtes web ?

::option[Examiner l’identité du processus qui traite les requêtes.]{#linux-service-accounts-verify-identity-c .correct explanation="En inspectant le processus concerné, vous associez le compte au travail qu’il effectue."}
::option[Consulter uniquement le nom du fichier de configuration du service.]{#linux-service-accounts-verify-identity-a explanation="Le nom du fichier ne donne pas le compte utilisé par le processus actif."}
::option[Lire le nom de la personne qui a ouvert le terminal.]{#linux-service-accounts-verify-identity-b explanation="L’utilisateur du terminal peut différer du compte sous lequel tourne le service."}
:::

## Résumé

Vous savez maintenant associer un processus Linux à son compte d’exécution.

1. Repérez le compte d’un processus dans la sortie de ps.
2. Choisissez des permissions adaptées au rôle du service.
3. Inspectez le processus pertinent lorsque le service en comporte plusieurs.
