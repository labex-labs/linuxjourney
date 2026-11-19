---
lesson_id: "web-access-logs"
course_id: "web-security"
lang: "fr"
order_index: 7
title: "Journaux d’accès web"
description: "Apprenez à utiliser les journaux d’accès HTTP pour savoir ce qu’un service a renvoyé sans exposer de données d’authentification."
meta_title: "Journaux d’accès web - Sécurité web"
meta_description: "Apprenez à utiliser les journaux d’accès HTTP pour savoir ce qu’un service a renvoyé sans exposer de données d’authentification."
meta_keywords: "journaux d’accès web, sécurité web, cybersécurité, Linux Journey"
---

Un serveur web peut consigner une entrée dans son **journal d’accès** pour chaque requête. L’entrée peut contenir une heure, un chemin, un code de réponse et un identifiant de requête. Utilisez seulement les champs nécessaires à votre enquête.

## Lire le résultat de la requête

Cet extrait simulé utilise des champs nommés. Les deux requêtes visent des chemins différents.

```text
t=09:18:01Z request=r31 method=GET path=/health status=200
t=09:18:04Z request=r32 method=GET path=/staff status=403
```

Un code `403` indique que le service a refusé la requête. Vérifiez le chemin exact et l’identifiant de la requête avant de rapprocher la réponse d’une autre entrée.

:::single-choice{#web-access-logs-log-result} Quelle requête suivre pour examiner le refus ?

::option[r31 sur /health.]{#web-access-logs-log-result-a explanation="Cette ligne indique un contrôle d’état réussi."}
::option[r32 sur /staff.]{#web-access-logs-log-result-b .correct explanation="Son statut est 403, le refus de cet extrait."}
::option[Les deux, comme s’il s’agissait de la même requête.]{#web-access-logs-log-result-c explanation="Les identifiants et les chemins les distinguent."}
:::

## Chercher la décision d’accès

Le journal d’accès indique ce que le serveur a renvoyé. Il peut omettre le motif d’une décision d’accès. Si l’application consigne aussi ses décisions d’autorisation, cherchez le même identifiant de requête à la même heure. Vous pourrez ainsi déterminer quelle règle s’est appliquée dans cet exemple.

:::single-choice{#web-access-logs-refusal-reason} La ligne du journal indique 403. Quelle autre entrée expliquerait le mieux pourquoi ?

::option[La décision d’autorisation de l’application pour r32.]{#web-access-logs-refusal-reason-a .correct explanation="L’entrée correspondante peut indiquer la règle appliquée."}
::option[Une réponse de succès d’un autre site.]{#web-access-logs-refusal-reason-b explanation="Elle est sans rapport avec ce refus."}
::option[Une requête antérieure vers le chemin du contrôle d’état.]{#web-access-logs-refusal-reason-c explanation="Elle consigne une autre opération et un autre résultat."}
:::

## Éviter de journaliser les données d’authentification

Évitez de consigner les valeurs qui permettraient à quelqu’un d’utiliser la session d’une autre personne, comme un cookie de session complet ou un jeton d’autorisation. Un identifiant de requête et un statut de réponse permettent déjà de diagnostiquer le problème. Lorsque vous partagez un extrait, retirez les champs sensibles et gardez uniquement les détails nécessaires à l’enquête.

:::single-choice{#web-access-logs-safe-fields} Quelles données peuvent aider à suivre la requête refusée sans copier de donnée d’authentification ?

::option[Le cookie de session complet et le mot de passe du compte.]{#web-access-logs-safe-fields-a explanation="Les deux valeurs sont sensibles et doivent rester hors des journaux partagés."}
::option[Le jeton d’autorisation et un chemin public.]{#web-access-logs-safe-fields-b explanation="Le chemin peut être utile. Le jeton est une donnée d’authentification confidentielle."}
::option[L’identifiant de la requête et le statut de sa réponse.]{#web-access-logs-safe-fields-c .correct explanation="Ces deux champs permettent de retrouver les entrées pertinentes sans révéler de valeur de session."}
:::

## Partager un extrait ciblé

Supposons qu’une personne ait besoin de contexte pour examiner un refus. Gardez l’heure, l’identifiant, la méthode, le chemin expurgé et le statut si ces champs suffisent. Certains chemins comportent des valeurs privées dans leurs paramètres de requête. Vérifiez l’extrait avant de le transmettre.

:::single-choice{#web-access-logs-final-application} Quel extrait convient le mieux à cet examen ?

::option[La requête complète et tous ses en-têtes par défaut.]{#web-access-logs-final-application-b explanation="Une requête peut contenir des données d’authentification ou des données personnelles superflues."}
::option[Uniquement le code de statut, sans aucun identifiant.]{#web-access-logs-final-application-c explanation="Le code seul peut être difficile à rapprocher de la décision d’accès correspondante."}
::option[Un chemin expurgé avec l’heure, l’identifiant de la requête et le statut de réponse.]{#web-access-logs-final-application-a .correct explanation="Ces champs suffisent à relier les entrées sans partager de valeur de session."}
:::

## Résumé

Vous savez maintenant lire un journal d’accès simple et conserver le contexte utile en toute sécurité.

1. Associez l’identifiant de la requête, son chemin et la réponse.
2. Consultez la décision d’autorisation correspondante si vous devez connaître le motif.
3. Écartez les données d’authentification des journaux collectés et partagés.
