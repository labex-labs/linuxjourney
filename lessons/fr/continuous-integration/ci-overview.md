---
lesson_id: "ci-overview"
course_id: "continuous-integration"
lang: "fr"
order_index: 1
title: "Intégration continue"
description: "Découvrez comment l’intégration continue vérifie les petites modifications avant leur intégration à une branche partagée."
meta_title: "Intégration continue - Intégration continue"
meta_description: "Découvrez comment l’intégration continue vérifie les petites modifications avant leur intégration à une branche partagée."
meta_keywords: "intégration continue, CI, DevOps, Linux Journey"
---

Une modification de la page d’accueil peut s’afficher correctement chez vous et poser problème dans un autre navigateur. L’**intégration continue**, ou CI, consiste à intégrer fréquemment les changements et à soumettre des versions précises à des vérifications reproductibles.

## Associer une modification à une vérification

Une révision identifie la version des fichiers à vérifier. Lorsqu’une modification touche `index.html`, la CI peut vérifier cette version et indiquer si elle remplit une condition précise. Pour ce site, la vérification pourrait rechercher le titre attendu. L’équipe peut ensuite consulter ce résultat avant de décider de fusionner les changements.

:::single-choice{#ci-overview-revision-result} Une vérification a réussi lundi. Mardi, un nouveau commit modifie la page. Que prouve le résultat de lundi ?

::option[Que les deux révisions satisfont le contrôle.]{#ci-overview-revision-result-b explanation="Il faut un résultat propre au nouveau commit."}
::option[Que la révision de lundi a passé ce contrôle.]{#ci-overview-revision-result-a .correct explanation="Le résultat concerne la révision sur laquelle le contrôle a été exécuté."}
::option[Que les visiteurs peuvent consulter la nouvelle page.]{#ci-overview-revision-result-c explanation="Un contrôle des fichiers source ne donne aucune indication sur un déploiement en cours."}
:::

## Lire un résultat d’échec

Supposons que la vérification signale l’absence du titre attendu. Cela donne à l’auteur un point de départ précis. Lisez la condition attendue et le résultat avant de modifier la page. Il peut s’agir d’une erreur dans le fichier, ou d’un changement de comportement voulu qui exige d’adapter la vérification.

:::single-choice{#ci-overview-failed-action} Que faut-il examiner en premier si la vérification du titre échoue ?

::option[Le titre attendu et le fichier de la révision vérifiée.]{#ci-overview-failed-action-b .correct explanation="Leur comparaison permet de comprendre d’où vient cet écart précis."}
::option[D’abord l’artefact de l’exécution précédente qui a réussi.]{#ci-overview-failed-action-a explanation="Cet artefact correspond à un résultat plus ancien. La vérification qui a échoué et le fichier concerné sont plus directement utiles."}
::option[Les réglages réseau des visiteurs.]{#ci-overview-failed-action-c explanation="La vérification lit un fichier sans envoyer de requête depuis un navigateur."}
:::

## Distinguer vérification et mise à disposition

Un pipeline peut contrôler les fichiers, produire un résultat et le transmettre à une étape de déploiement. Un **build** prépare ce que les étapes suivantes utiliseront, par exemple un dossier de fichiers prêts à être servis. Un **déploiement** installe ou lance une version dans un environnement. Votre premier workflow de CI vérifiera une page avant de la transmettre.

:::single-choice{#ci-overview-output-vs-live} Les tests sont passés et une archive du site a été produite. Comment savoir si les visiteurs peuvent consulter cette version ?

::option[Avec une deuxième copie du journal de vérification.]{#ci-overview-output-vs-live-a explanation="Le journal décrit les vérifications et le build."}
::option[En constatant que l’archive existe.]{#ci-overview-output-vs-live-b explanation="Une archive peut exister sans être servie par le site."}
::option[Avec une trace du déploiement et une requête réussie vers la page attendue.]{#ci-overview-output-vs-live-c .correct explanation="Ces deux éléments relient la version produite à une réponse de l’environnement cible."}
:::

## Résumé

Vous savez maintenant à quel moment intervient la CI dans le parcours d’une modification.

1. Associez chaque résultat de vérification à une révision précise.
2. Partez de la vérification en échec pour choisir ce qu’il faut examiner.
3. Distinguez la vérification, le build et le déploiement.
