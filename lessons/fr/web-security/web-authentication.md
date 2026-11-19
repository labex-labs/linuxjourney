---
lesson_id: "web-authentication"
course_id: "web-security"
lang: "fr"
order_index: 4
title: "Authentification"
description: "Découvrez comment un service web vérifie une identité et quelles preuves apportent deux facteurs différents."
meta_title: "Authentification - Sécurité web"
meta_description: "Découvrez comment un service web vérifie une identité et quelles preuves apportent deux facteurs différents."
meta_keywords: "authentification, sécurité web, cybersécurité, Linux Journey"
---

L’**authentification** est l’étape qui vérifie l’identité déclarée par un utilisateur. Un formulaire de connexion peut demander un nom de compte et un mot de passe. Le nom indique l’identité revendiquée. Le mot de passe fournit une preuve que le service peut vérifier.

## Repérer l’identité déclarée

Imaginez qu’un utilisateur saisisse le nom de compte `alex`. Toute personne qui connaît ce nom peut le saisir. Le service vérifie la preuve fournie à l’aide des informations et des règles applicables à ce compte.

:::single-choice{#web-authentication-username-claim} Quelle donnée indique le compte auquel l’utilisateur essaie d’accéder ?

::option[Le résultat de la vérification du mot de passe.]{#web-authentication-username-claim-a explanation="C’est un élément qui sert à accepter ou à rejeter l’identité déclarée."}
::option[Le nom du compte.]{#web-authentication-username-claim-b .correct explanation="Il indique au service quelle identité vérifier."}
::option[Le format de la réponse de la page d’accueil.]{#web-authentication-username-claim-c explanation="Le type de contenu est indépendant de l’identité utilisée pour se connecter."}
:::

## Comparer les facteurs d’authentification

Un **facteur** est une catégorie de preuve. Le mot de passe est une chose que l’utilisateur connaît. Une clé de sécurité enregistrée fournit une preuve fondée sur quelque chose qu’il possède. Un mot de passe et une clé enregistrée distincte donnent deux types de preuves.

:::single-choice{#web-authentication-independent-factors} Quel exemple combine connaissance et possession ?

::option[Un mot de passe et une clé de sécurité enregistrée.]{#web-authentication-independent-factors-a .correct explanation="Le premier vérifie ce que l’utilisateur connaît, la seconde vérifie qu’il dispose de la clé."}
::option[Un mot de passe et un deuxième mot de passe mémorisé.]{#web-authentication-independent-factors-b explanation="Ce sont deux exemples de choses que l’utilisateur connaît."}
::option[Un nom d’utilisateur et un titre de page.]{#web-authentication-independent-factors-c explanation="Ces libellés fournissent peu d’éléments pour vérifier une identité."}
:::

## Comprendre ce que confirme l’authentification

Après avoir vérifié la preuve, le service peut laisser l’utilisateur ouvrir une session. Une vérification réussie établit quel compte est connecté. Les actions permises à ce compte restent à déterminer. Le service applique ses règles d’accès lorsqu’il reçoit des requêtes visant des ressources précises.

:::single-choice{#web-authentication-auth-limit} Un compte s’est connecté avec succès et demande une page d’administration. Que doit-il se passer ensuite ?

::option[Tous les comptes connectés doivent recevoir automatiquement la page.]{#web-authentication-auth-limit-a explanation="Le compte doit encore détenir l’autorisation exigée par la page."}
::option[Le titre d’origine de la page doit déterminer l’accès.]{#web-authentication-auth-limit-b explanation="Un titre ne porte aucun droit utilisateur."}
::option[L’application doit vérifier l’accès du compte à cette ressource.]{#web-authentication-auth-limit-c .correct explanation="La vérification d’identité et l’accès à la ressource répondent à deux questions distinctes."}
:::

## Résumé

Vous savez maintenant expliquer ce qu’établit une décision d’authentification.

1. Distinguez l’identité déclarée de la preuve apportée.
2. Reconnaissez deux catégories différentes de facteurs d’authentification.
3. Appuyez-vous sur les règles d’autorisation du service pour décider de l’accès à une ressource.
