---
lesson_id: "web-sessions-and-cookies"
course_id: "web-security"
lang: "fr"
order_index: 5
title: "Sessions et cookies"
description: "Découvrez comment un cookie rattache les requêtes d’un navigateur à une session web."
meta_title: "Sessions et cookies - Sécurité web"
meta_description: "Découvrez comment un cookie rattache les requêtes d’un navigateur à une session web."
meta_keywords: "sessions et cookies, sécurité web, cybersécurité, Linux Journey"
---

Un navigateur envoie souvent une nouvelle requête après une connexion réussie. Une **session** permet à l’application d’associer ces requêtes au compte connecté. Une méthode courante consiste à conserver un identifiant court dans un cookie du navigateur.

## Suivre un cookie

Ces exemples sont abrégés. La réponse envoie un cookie nommé `session` doté d’un jeton fictif pour l’illustration.

```http
Set-Cookie: session=sample-token; Secure; HttpOnly; SameSite=Lax
```

Le navigateur peut ensuite inclure le cookie dans une requête ultérieure qui respecte ses conditions d’envoi.

```http
Cookie: session=sample-token
```

Le serveur utilise le jeton pour retrouver la session créée auparavant.

:::single-choice{#web-sessions-and-cookies-direction} Quel en-tête renvoie la valeur du cookie dans une requête qui remplit ses conditions d’envoi ?

::option[Set-Cookie.]{#web-sessions-and-cookies-direction-a explanation="Le serveur envoie cet en-tête dans la réponse pour définir le cookie."}
::option[Content-Type.]{#web-sessions-and-cookies-direction-c explanation="Cet en-tête décrit le format du corps du message."}
::option[Cookie.]{#web-sessions-and-cookies-direction-b .correct explanation="Le navigateur inclut cet en-tête de requête lorsque les conditions d’envoi sont remplies."}
:::

## Lire les attributs

`Secure` limite normalement l’envoi du cookie aux connexions HTTPS. `HttpOnly` empêche les scripts de la page de le lire par l’interface habituelle des cookies. `SameSite` détermine quand le navigateur inclut le cookie dans les requêtes lancées depuis un autre site. Chaque réglage concerne un comportement différent du navigateur.

:::single-choice{#web-sessions-and-cookies-secure-attribute} Quel attribut indique au navigateur de limiter l’envoi de ce cookie à HTTPS ?

::option[HttpOnly.]{#web-sessions-and-cookies-secure-attribute-b explanation="Cet attribut limite l’accès au cookie depuis les scripts de la page."}
::option[Secure.]{#web-sessions-and-cookies-secure-attribute-a .correct explanation="Cet attribut s’applique à la protection du transport du cookie."}
::option[Le nom session.]{#web-sessions-and-cookies-secure-attribute-c explanation="Le nom d’un cookie est un libellé choisi par l’application."}
:::

## Mettre fin à une session

Quand un utilisateur se déconnecte, le service peut invalider la session sur le serveur et demander au navigateur de supprimer le cookie enregistré. L’invalidation côté serveur est importante, car le navigateur peut encore conserver brièvement une ancienne valeur. Traitez un vrai jeton de session comme une donnée d’authentification et gardez-le hors des captures d’écran et des journaux partagés.

:::single-choice{#web-sessions-and-cookies-after-sign-out} Que doit-il se passer si un jeton de session invalidé parvient de nouveau au serveur ?

::option[Le serveur doit considérer la requête comme non authentifiée.]{#web-sessions-and-cookies-after-sign-out-c .correct explanation="La session serveur associée à cette valeur n’est plus valide."}
::option[Le serveur doit rétablir automatiquement l’ancienne session.]{#web-sessions-and-cookies-after-sign-out-a explanation="L’ancienne session a pris fin."}
::option[Le serveur doit l’accepter parce que le cookie porte toujours un nom.]{#web-sessions-and-cookies-after-sign-out-b explanation="Le nom du cookie ne rend pas sa valeur valide."}
:::

## Résumé

Vous savez maintenant suivre un cookie de session entre un navigateur et un service.

1. Identifiez l’en-tête qui crée un cookie et celui qui le renvoie.
2. Expliquez le rôle des attributs courants d’un cookie.
3. Décrivez comment l’invalidation côté serveur met fin à une session.
