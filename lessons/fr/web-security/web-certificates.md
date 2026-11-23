---
lesson_id: "web-certificates"
course_id: "web-security"
lang: "fr"
order_index: 3
title: "Certificats"
description: "Apprenez à vérifier le nom, les dates de validité et l’émetteur d’un certificat TLS."
meta_title: "Certificats - Sécurité web"
meta_description: "Apprenez à vérifier le nom, les dates de validité et l’émetteur d’un certificat TLS."
meta_keywords: "certificats, sécurité web, cybersécurité, Linux Journey"
---

Un navigateur a besoin de preuves qu’il a bien joint le site indiqué dans l’URL. Un **certificat** TLS contient une identité et une clé publique. Le navigateur vérifie plusieurs propriétés avant de faire confiance à cette identité.

## Examiner les noms

Ouvrez la page du [certificat public d’exercice](https://github.com/labex-labs/linuxjourney/blob/master/examples/web-security/site-cert.pem) sur GitHub et enregistrez le fichier sous le nom `site-cert.pem`. C’est un exemple pédagogique autosigné. Utilisez OpenSSL pour afficher l’émetteur, les dates de validité et les autres noms du sujet. L’option `-noout` masque le certificat encodé.

```bash
$ openssl x509 -in site-cert.pem -noout -issuer -dates -ext subjectAltName
```

La section des **noms alternatifs du sujet** répertorie les noms DNS couverts par l’exemple. Cherchez `DNS:site.example`. Un navigateur compare le nom de son URL aux noms du certificat.

:::single-choice{#web-certificates-wrong-name} Le seul nom indiqué est site.example. Quelle URL correspond à ce nom ?

::option[`https://site.example/`.]{#web-certificates-wrong-name-b .correct explanation="Le nom DNS du certificat correspond à l’hôte de l’URL."}
::option[`https://other.example/`.]{#web-certificates-wrong-name-a explanation="Le certificat d’exercice indique un autre nom."}
::option[`https://preview.site.example/`.]{#web-certificates-wrong-name-c explanation="Un sous-domaine constitue un nom distinct, sauf si le certificat le couvre."}
:::

![Sortie enregistrée d’OpenSSL montrant l’émetteur du certificat d’exercice, ses dates de validité et le nom DNS site.example](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/web-security/web-certificates/dns-name-and-validity.png)

## Vérifier les dates

Les champs `notBefore` et `notAfter` indiquent la période pendant laquelle le certificat peut être utilisé. Comparez ces dates à l’heure de votre test. Un problème d’horloge peut aussi fausser le contrôle. Pour vérifier un certificat, il faut examiner d’autres éléments que les dates.

:::single-choice{#web-certificates-validity-period} L’heure actuelle est postérieure à notAfter. Que devez-vous examiner ?

::option[Si le bon nom DNS figure dans le certificat.]{#web-certificates-validity-period-b explanation="Le nom compte pour vérifier l’identité. Même si le nom correspond, un certificat expiré est hors de sa période de validité."}
::option[Si le mot de passe d’un utilisateur a changé.]{#web-certificates-validity-period-c explanation="La connexion à l’application est indépendante de la validité du certificat."}
::option[Si le certificat a expiré et doit être renouvelé.]{#web-certificates-validity-period-a .correct explanation="Le serveur présente un certificat hors de la période de validité indiquée."}
:::

## Vérifier la confiance

L’**émetteur** désigne la personne ou l’organisme qui a signé le certificat. Les navigateurs vérifient normalement les signatures le long d’une chaîne qui remonte à une autorité de confiance. OpenSSL affiche le nom de l’émetteur dans un champ que vous pouvez consulter. La vérification de la chaîne est une opération distincte. Un certificat d’exercice peut être destiné uniquement à un environnement d’entraînement.

:::single-choice{#web-certificates-trust-check} Le nom et les dates correspondent, mais le navigateur ne fait pas confiance au signataire. Que manque-t-il encore ?

::option[Une deuxième copie de la date du certificat.]{#web-certificates-trust-check-a explanation="Des dates concordantes n’établissent pas qui garantit l’identité."}
::option[Une chaîne valide jusqu’à une autorité de confiance pour cette connexion.]{#web-certificates-trust-check-c .correct explanation="Le navigateur a besoin d’une chaîne de confiance, d’un nom correspondant et de dates valides."}
::option[Un autre nom d’utilisateur sur le site.]{#web-certificates-trust-check-b explanation="La décision de confiance précède l’authentification habituelle dans l’application."}
:::

## Résumé

Vous savez maintenant effectuer trois vérifications utiles sur un certificat.

1. Vérifiez que l’hôte de l’URL correspond à un nom couvert.
2. Comparez la date et l’heure actuelles à la période de validité du certificat.
3. Vérifiez séparément la chaîne de confiance.
