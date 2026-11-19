---
lesson_id: "linux-ssh-access"
course_id: "linux-hardening"
lang: "fr"
order_index: 6
title: "Accès SSH"
description: "Apprenez à distinguer l’identité du serveur SSH, l’authentification de l’utilisateur et les règles de connexion."
meta_title: "Accès SSH - Durcissement de Linux"
meta_description: "Apprenez à distinguer l’identité du serveur SSH, l’authentification de l’utilisateur et les règles de connexion."
meta_keywords: "accès SSH, durcissement de Linux, cybersécurité, Linux Journey"
---

Quand vous utilisez SSH pour la maintenance, chaque extrémité de la connexion effectue une vérification. Votre client doit savoir quel serveur il a joint. Le serveur doit vérifier si le compte a le droit de se connecter.

## Vérifier l’identité du serveur

Un serveur SSH présente une **clé d’hôte**. Le client peut la comparer à l’identité connue de cet hôte. Si la clé change de façon inattendue, vérifiez la nouvelle clé auprès d’une source indépendante approuvée, comme l’inventaire des hôtes de l’équipe ou une personne chargée de la maintenance jointe par un canal de confiance.

:::single-choice{#linux-ssh-access-unexpected-key} Votre client signale que la clé d’hôte du serveur a changé. Quelle vérification effectuer d’abord ?

::option[Confirmer la nouvelle clé d’hôte attendue auprès d’une source de confiance.]{#linux-ssh-access-unexpected-key-b .correct explanation="Vous vérifiez ainsi l’identité avant de vous fier à la connexion."}
::option[Essayer plusieurs noms d’utilisateur jusqu’à ce que l’un fonctionne.]{#linux-ssh-access-unexpected-key-a explanation="Un nom d’utilisateur ne vérifie pas l’identité du serveur."}
::option[Supprimer toutes les clés d’hôte enregistrées et continuer.]{#linux-ssh-access-unexpected-key-c explanation="Vous perdriez les identités connues avant d’avoir expliqué le changement."}
:::

## Vérifier l’accès de l’utilisateur

Une clé d’utilisateur peut prouver qu’un client est autorisé à utiliser un compte. La clé d’hôte sert, elle, à vérifier l’identité du serveur. La politique du serveur peut limiter les comptes et les méthodes d’authentification qu’il accepte. Dans cet exemple d’exercice, `ops` se connecte avec une authentification par clé.

:::single-choice{#linux-ssh-access-distinguish-keys} Quelle identité est vérifiée quand le serveur contrôle la clé d’utilisateur d’ops ?

::option[Le nom de la page web publique.]{#linux-ssh-access-distinguish-keys-b explanation="Le contenu web est indépendant de l’authentification SSH."}
::option[L’identité du serveur lui-même.]{#linux-ssh-access-distinguish-keys-c explanation="Le client utilise la clé d’hôte pour cette vérification."}
::option[Celle du client qui tente de se connecter sous ops.]{#linux-ssh-access-distinguish-keys-a .correct explanation="L’authentification de l’utilisateur concerne le compte que le client essaie d’utiliser."}
:::

## Conserver un accès de maintenance

Avant toute modification approuvée de la politique SSH, mettez-vous d’accord sur les comptes et la méthode d’accès attendus. Utilisez une connexion de test distincte et gardez l’accès de secours établi jusqu’à ce que la connexion prévue réussisse. Une session déjà ouverte peut rester active après un changement qui bloque les nouvelles connexions.

:::single-choice{#linux-ssh-access-test-new-login} Une session reste ouverte après la modification d’une règle. Qu’est-ce qui confirme qu’une personne chargée de la maintenance peut encore se connecter ?

::option[Une simple réponse à un ping.]{#linux-ssh-access-test-new-login-a explanation="Une réponse réseau ne démontre pas la réussite de l’authentification SSH."}
::option[Une nouvelle session SSH autorisée avec le compte et la méthode prévus.]{#linux-ssh-access-test-new-login-c .correct explanation="Vous testez directement les règles qui s’appliqueront aux prochaines connexions."}
::option[L’ancienne session reste ouverte sans activité.]{#linux-ssh-access-test-new-login-b explanation="Elle a été authentifiée avant la modification."}
:::

## Résumé

Vous savez maintenant vérifier les principales identités et règles qui régissent l’accès de maintenance par SSH.

1. Vérifiez l’identité du serveur à l’aide de sa clé d’hôte.
2. Distinguez ce contrôle de l’authentification de l’utilisateur.
3. Vérifiez qu’une nouvelle connexion autorisée fonctionne après un changement.
