---
lesson_id: "deployment-staging"
course_id: "deployment"
lang: "fr"
order_index: 3
title: "Préproduction"
description: "Découvrez ce que vous pouvez vérifier en préproduction et pourquoi le même artefact peut se comporter différemment selon l’environnement."
meta_title: "Préproduction - Déploiement"
meta_description: "Découvrez ce que vous pouvez vérifier en préproduction et pourquoi le même artefact peut se comporter différemment selon l’environnement."
meta_keywords: "préproduction, staging, déploiement, DevOps, Linux Journey"
---

Une release est presque prête. Exécutez l’artefact en **préproduction** (staging), un environnement de test conçu pour ressembler au service que les utilisateurs emploieront. Vous pouvez ainsi vérifier la release avec des réglages réalistes avant de l’exposer au trafic de production.

## Garder le même artefact d’un environnement à l’autre

Utilisez l’image qui a été testée et approuvée. Si vous reconstruisez l’image après un changement de dépendances, vous pourriez obtenir un autre artefact. Notez la référence complète de l’image à chaque déploiement.

```text
Environment  Artifact      Page configuration
staging      site@digest-A Internal preview
production   site@digest-A Public website
```

L’empreinte de l’exemple est symbolique. Les deux environnements utilisent le même artefact avec des réglages différents.

:::single-choice{#deployment-staging-same-artifact} Qu’est-ce qui indique que le même code empaqueté peut passer en production ?

::option[La référence de l’artefact est identique dans les deux fiches de déploiement.]{#deployment-staging-same-artifact-b .correct explanation="La référence exacte rattache les deux environnements au même build."}
::option[Les deux environnements utilisent la même désignation pour un port.]{#deployment-staging-same-artifact-a explanation="Un réglage commun ne suffit pas à identifier l’artefact."}
::option[Les deux environnements ont été déployés le même jour.]{#deployment-staging-same-artifact-c explanation="La date seule ne permet pas de savoir ce qui a été déployé."}
:::

## Choisir des vérifications représentatives

La préproduction doit vous permettre d’exercer les fonctions importantes, comme charger la page et lire des données depuis une dépendance de test. Utilisez des comptes et des données de test autorisés. Une vérification réussie renforce la confiance dans le scénario testé. Les différences de trafic, de données ou de configuration peuvent encore compter après la mise en production.

:::single-choice{#deployment-staging-staging-scope} La page de préproduction se charge avec une base de données de test. Que faut-il encore vérifier après le déploiement réel ?

::option[Que l’artefact n’a plus besoin de numéro de version.]{#deployment-staging-staging-scope-b explanation="La trace de la version reste utile pour la vérification et la remise en service."}
::option[Que toutes les requêtes de production réussiront.]{#deployment-staging-staging-scope-c explanation="Un petit échantillon de test ne renseigne pas sur chaque futur résultat."}
::option[Que le parcours en production fonctionne avec les réglages approuvés.]{#deployment-staging-staging-scope-a .correct explanation="La requête de préproduction n’est pas passée par l’environnement de production."}
:::

## Vérifier la cible avant toute modification

Vérifiez le nom et l’adresse de la cible avant de lancer un déploiement. Ensuite, utilisez cette même adresse pour confirmer la nouvelle version et vérifier les fonctions importantes. Identifiez clairement la préproduction et la production dans vos notes, afin que chaque résultat puisse être rattaché à son environnement.

:::single-choice{#deployment-staging-correct-target} Vous comptez déployer en préproduction, mais la commande indique l’adresse de production. Que faut-il faire en premier ?

::option[Continuer et étiqueter le résultat comme un test de préproduction.]{#deployment-staging-correct-target-a explanation="L’adresse détermine quel service reçoit la modification."}
::option[Vous arrêter et confirmer la cible prévue.]{#deployment-staging-correct-target-c .correct explanation="Vous évitez ainsi de modifier le mauvais environnement."}
::option[Tester depuis un autre navigateur après le déploiement.]{#deployment-staging-correct-target-b explanation="La cible doit être corrigée avant de lancer la modification."}
:::

Pour un exemple pratique de CI/CD, consultez [Déploiement continu en préproduction](https://labex.io/tutorials/cd-deployment-to-staging-636593).

## Résumé

Vous savez maintenant tester un artefact approuvé en préproduction avant de le déployer dans l’environnement suivant.

1. Conservez l’identité de l’artefact d’un environnement à l’autre.
2. Choisissez des vérifications représentatives des actions importantes des utilisateurs.
3. Confirmez l’environnement avant de le modifier.
