---
lesson_id: "deployment-rollbacks"
course_id: "deployment"
lang: "fr"
order_index: 5
title: "Retours arrière"
description: "Apprenez à choisir une version éprouvée et à déterminer si un retour arrière de l’application suffit."
meta_title: "Retours arrière - Déploiement"
meta_description: "Apprenez à choisir une version éprouvée et à déterminer si un retour arrière de l’application suffit."
meta_keywords: "retour arrière, rollback, compatibilité des données, déploiement, DevOps, Linux Journey"
---

Un **retour arrière** (rollback) rétablit une version précédente dont le bon fonctionnement a été vérifié. Appuyez-vous sur l’historique des déploiements pour choisir cette version. Avant de revenir en arrière, vérifiez si la release a aussi modifié des données ou des réglages partagés.

## Choisir une version précédente

Dans cet exemple, une requête échoue après le déploiement d’une nouvelle version. La dernière version vérifiée était la version 2. Les libellés ci-dessous représentent les empreintes complètes d’image qui figureraient dans une vraie fiche.

```text
08:50  version 2  digest-B  homepage and version check passed
09:10  version 3  digest-C  homepage check failed
```

La version 2 est un bon point de départ si elle fonctionne encore avec l’environnement actuel. Utilisez la référence d’artefact enregistrée pour la retrouver.

:::single-choice{#deployment-rollbacks-previous-version} Quelle image examineriez-vous en premier pour un retour arrière ?

::option[L’image la plus récente dans le cache de l’hôte.]{#deployment-rollbacks-previous-version-a explanation="L’ordre du cache ne permet pas d’identifier une version qui fonctionnait."}
::option[Digest-C, parce que c’est le déploiement le plus récent.]{#deployment-rollbacks-previous-version-c explanation="La fiche associe cet artefact à la vérification qui a échoué."}
::option[Digest-B, qui avait passé les vérifications pertinentes.]{#deployment-rollbacks-previous-version-b .correct explanation="La fiche relie cet artefact à la dernière version vérifiée."}
:::

## Vérifier la compatibilité des données

Une mise à jour d’application peut aussi modifier une base de données ou une autre ressource partagée. Démarrer une image plus ancienne laisse ces ressources dans leur état actuel. Vérifiez si l’ancienne application sait toujours lire les données. S’il faut restaurer les données, suivez le plan de reprise de l’équipe et tenez compte des modifications depuis la sauvegarde.

:::single-choice{#deployment-rollbacks-external-state} La version 3 a changé le format d’une base de données. Que faut-il vérifier avant de démarrer la version 2 avec cette base ?

::option[Si la version 2 avait passé l’ancienne vérification de la page d’accueil.]{#deployment-rollbacks-external-state-b explanation="Ce résultat fait de la version 2 une candidate. Il ne dit rien sur le format actuel de la base."}
::option[Si la version 2 prend en charge le format actuel.]{#deployment-rollbacks-external-state-a .correct explanation="Changer l’image de l’application ne remet pas les données partagées dans leur état précédent."}
::option[Si le nom de la base figure dans les notes de version.]{#deployment-rollbacks-external-state-c explanation="Il faut savoir si l’ancien code est capable d’utiliser les données actuelles."}
:::

## Confirmer le résultat

Après le retour arrière, vérifiez la version en cours d’exécution et répétez la vérification qui avait échoué du point de vue des utilisateurs. Examinez de nouveau les dépendances importantes. Notez l’heure, la version rétablie et les résultats pour que l’on puisse distinguer l’échec initial du rétablissement.

:::single-choice{#deployment-rollbacks-rollback-proof} La commande de retour arrière a terminé. Quels deux résultats indiquent que le service est rétabli ?

::option[Le point d’accès indique la version 2 et la vérification qui avait échoué réussit désormais.]{#deployment-rollbacks-rollback-proof-c .correct explanation="Vous confirmez ainsi la version attendue et le comportement qui avait été affecté."}
::option[Deux téléchargements d’image ont réussi.]{#deployment-rollbacks-rollback-proof-a explanation="Les téléchargements préparent les fichiers sans tester le service en cours d’exécution."}
::option[Une ancienne capture montre la version 2.]{#deployment-rollbacks-rollback-proof-b explanation="Cette capture montre un état passé."}
:::

## Résumé

Vous savez maintenant vous appuyer sur les vérifications pour préparer un retour arrière.

1. Choisissez une version qui a déjà fait ses preuves.
2. Vérifiez la compatibilité avec les données et les réglages partagés.
3. Vérifiez la version rétablie et le comportement observé par les utilisateurs.
