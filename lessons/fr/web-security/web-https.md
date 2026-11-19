---
lesson_id: "web-https"
course_id: "web-security"
lang: "fr"
order_index: 2
title: "HTTPS"
description: "Apprenez à reconnaître la partie d’une requête web que protège HTTPS."
meta_title: "HTTPS - Sécurité web"
meta_description: "Apprenez à reconnaître la partie d’une requête web que protège HTTPS."
meta_keywords: "HTTPS, sécurité web, cybersécurité, Linux Journey"
---

HTTP définit les messages qu’un navigateur et un serveur échangent. HTTPS fait passer ces mêmes messages par **TLS**, un protocole qui protège la connexion et aide le navigateur à vérifier le serveur.

## Repérer la connexion protégée

Imaginez qu’un navigateur se connecte à `https://site.example`. Une fois la connexion TLS établie, le navigateur et le serveur peuvent échanger des messages HTTP chiffrés. Une personne qui observe cette partie du réseau ne peut pas simplement lire le corps HTTP ni le modifier sans que cela soit détecté.

```text
Browser  ===== HTTPS connection =====  Website server
```

Le navigateur doit tout de même valider l’identité que présente le serveur.

:::single-choice{#web-https-protected-hop} Que protège HTTPS dans cette configuration simple ?

::option[La page après son affichage par le navigateur.]{#web-https-protected-hop-b explanation="Le navigateur lit la page après avoir déchiffré la réponse."}
::option[Toutes les sauvegardes conservées par le site.]{#web-https-protected-hop-c explanation="La protection des sauvegardes relève d’autres mesures."}
::option[Les messages HTTP envoyés sur la connexion protégée.]{#web-https-protected-hop-a .correct explanation="TLS protège les messages en transit entre ses deux extrémités."}
:::

## Examiner un trajet à plusieurs étapes

Un serveur mandataire, ou proxy, peut recevoir la requête d’un navigateur et la transmettre à un autre serveur. Si la connexion TLS se termine au niveau du proxy, celui-ci peut lire la requête avant de la transmettre. La connexion suivante doit bénéficier de sa propre protection. Examinez chaque connexion du trajet.

```text
Browser  === HTTPS ===  Proxy  --- HTTP ---  Internal server
```

Dans ce schéma, la connexion externe utilise TLS. La connexion interne utilise HTTP en clair.

:::single-choice{#web-https-inner-hop} Quelle partie du trajet nécessite une modification distincte pour bénéficier de TLS ?

::option[Du navigateur au proxy.]{#web-https-inner-hop-a explanation="Cette partie utilise déjà HTTPS."}
::option[Du proxy au serveur interne.]{#web-https-inner-hop-b .correct explanation="Cette partie interne utilise HTTP en clair dans le schéma."}
::option[Un onglet du navigateur qui ne demande jamais le site.]{#web-https-inner-hop-c explanation="Aucune connexion de cet onglet n’apparaît dans le schéma."}
:::

## Vérifier aussi les droits d’accès

Une connexion sécurisée et valide aide à vérifier l’identité du serveur et protège les messages en transit. L’application décide toujours quel compte peut lire une page ou modifier un réglage. Une page privée peut bénéficier d’une protection TLS robuste et nécessiter des règles d’accès dans l’application.

:::single-choice{#web-https-access-vs-transport} Que doit vérifier le service avant de renvoyer une page privée du compte ?

::option[Si le compte authentifié est autorisé à lire cette page.]{#web-https-access-vs-transport-c .correct explanation="Les règles d’autorisation de l’application déterminent à quoi le compte a accès."}
::option[Uniquement si TLS est utilisé.]{#web-https-access-vs-transport-a explanation="HTTPS protège l’échange. Le service doit encore décider si le compte a accès à cette ressource."}
::option[Uniquement si le certificat couvre le nom d’hôte demandé.]{#web-https-access-vs-transport-b explanation="Le certificat aide à vérifier l’identité du serveur. L’application contrôle toujours l’accès aux pages privées."}
:::

## Résumé

Vous savez maintenant décrire ce que HTTPS protège sur le trajet d’une requête web.

1. Repérez les extrémités de la connexion TLS.
2. Vérifiez chaque connexion lorsqu’un proxy transmet la requête.
3. Identifiez les contrôles d’accès qui restent du ressort de l’application.
