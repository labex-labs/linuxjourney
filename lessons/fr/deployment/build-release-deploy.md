---
lesson_id: "build-release-deploy"
course_id: "deployment"
lang: "fr"
order_index: 1
title: "Build, release et déploiement"
description: "Apprenez à suivre une révision source à travers les traces de son build, de sa validation et de son déploiement."
meta_title: "Build, release et déploiement - Déploiement"
meta_description: "Apprenez à suivre une révision source à travers les traces de son build, de sa validation et de son déploiement."
meta_keywords: "build, release, déploiement, DevOps, Linux Journey"
---

Un collègue dit que la version 2 est prête. Les fichiers ont peut-être été produits, la version a peut-être été approuvée, ou les visiteurs y ont déjà accès. Consultez les traces de chaque opération pour savoir où en est la version.

## Identifier le build

Un build produit un résultat à partir d’une révision source précise. Dans cet exemple, un petit site web est empaqueté sous forme d’image de conteneur et stocké dans un registre d’images. Notez le commit source à côté de la référence de l’image produite.

```text
Build 81
Source commit: 3ab4501
Image: registry.example/journey/site:2
Result: succeeded
```

Cette trace indique ce qui a été produit. Le site peut encore servir une version antérieure.

:::single-choice{#build-release-deploy-build-record} Quelle trace relie l’image empaquetée à la révision source ?

::option[Un favori dans le navigateur.]{#build-release-deploy-build-record-b explanation="Un favori indique une adresse sans préciser comment les fichiers ont été produits."}
::option[Le build 81.]{#build-release-deploy-build-record-a .correct explanation="Il indique le commit source et l’image qui en résulte."}
::option[Le nom de la branche locale la plus récente.]{#build-release-deploy-build-record-c explanation="Une branche peut changer de commit, son nom ne suffit donc pas à identifier ce build."}
:::

## Lire la validation d’une version

Une **release** désigne une version approuvée pour la distribution. Par exemple, une fiche de release peut autoriser l’image exacte du build 81 pour la préproduction. Après validation, vous pouvez ainsi désigner le même artefact sans en produire une nouvelle copie.

:::single-choice{#build-release-deploy-release-record} La release 2 est approuvée pour la préproduction. Qu’est-ce que cela établit ?

::option[L’artefact enregistré est approuvé pour cet usage.]{#build-release-deploy-release-record-b .correct explanation="La fiche précise quel artefact est autorisé en préproduction."}
::option[Tous les environnements servent déjà la version 2.]{#build-release-deploy-release-record-a explanation="L’approbation autorise le déploiement. Pour connaître la version en service, il faut consulter une autre trace."}
::option[La version 2 reçoit plus de requêtes.]{#build-release-deploy-release-record-c explanation="Une fiche de release ne mesure pas le trafic."}
:::

## Trouver la version déployée

Un **déploiement** place une version précise dans un environnement et y lance ou met à jour l’application. Un environnement, comme la préproduction ou la production, dispose de ses propres réglages et ressources. Une requête réussie vers un point d’accès indiquant la version peut vous aider à vérifier quelle version répond.

```text
Staging version response: 2
Production version response: 1
```

Ici, la nouvelle version répond en préproduction, tandis que la production répond encore avec la version 1.

:::single-choice{#build-release-deploy-running-version} Une personne souhaite vérifier que la version 2 est en service en production. Quelle observation l’aiderait directement ?

::option[Une deuxième réponse de préproduction indiquant la version 2.]{#build-release-deploy-running-version-a explanation="Cette requête vérifie toujours la préproduction."}
::option[Le message d’approbation de la release.]{#build-release-deploy-running-version-b explanation="L’approbation ne teste pas le service en cours d’exécution."}
::option[Une réponse de l’adresse de production indiquant la version.]{#build-release-deploy-running-version-c .correct explanation="Cette requête vérifie l’environnement concerné."}
:::

## Résumé

Vous savez maintenant distinguer les traces des différentes étapes d’une mise en service.

1. Reliez le résultat d’un build à sa source.
2. Identifiez l’artefact approuvé pour une release.
3. Confirmez quelle version répond dans l’environnement visé.
