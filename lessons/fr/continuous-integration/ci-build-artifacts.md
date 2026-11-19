---
lesson_id: "ci-build-artifacts"
course_id: "continuous-integration"
lang: "fr"
order_index: 6
title: "Artefacts de build"
description: "Apprenez à relier un fichier produit par la CI à l’exécution et à la révision source correspondantes."
meta_title: "Artefacts de build - Intégration continue"
meta_description: "Apprenez à relier un fichier produit par la CI à l’exécution et à la révision source correspondantes."
meta_keywords: "artefacts de build, révision source, intégration continue, DevOps, Linux Journey"
---

Un **artefact de build** est un fichier, ou un ensemble de fichiers, conservé après une exécution pour être utilisé plus tard. Il peut s’agir d’un rapport de test ou d’une archive du site. Gardez la référence de l’exécution et de la révision avec l’artefact pour que la personne qui le vérifie puisse retrouver les fichiers source dont il provient.

## Empaqueter un dossier de sortie

Utilisez le dossier d’exercice où `dist` contient la page produite. Cet exemple crée une archive compressée, un fichier unique qui contient le contenu du dossier. S’il existe déjà une archive du même nom dans le dossier courant, elle sera écrasée.

```bash
$ tar -czf site.tar.gz -C dist .
$ tar -tzf site.tar.gz
```

Dans la première commande, `-c` crée l’archive, `-z` la compresse et `-f` indique le nom du fichier de sortie. Avec `-C dist .`, tar commence dans `dist`. La deuxième commande utilise `-t` pour lister le contenu de l’archive. Repérez `./index.html` avant de mettre l’archive à disposition.

:::single-choice{#ci-build-artifacts-inspect-archive} Quelle commande permet de vérifier que la page figure dans l’archive ?

::option[Lister son contenu avec tar -tzf site.tar.gz.]{#ci-build-artifacts-inspect-archive-b .correct explanation="La liste indique si index.html figure dans l’archive."}
::option[Créer une nouvelle fois l’archive.]{#ci-build-artifacts-inspect-archive-a explanation="Répéter la création n’affiche pas la liste des fichiers à vérifier."}
::option[Lire le nom du fichier.]{#ci-build-artifacts-inspect-archive-c explanation="Le nom de l’archive ne renseigne pas sur son contenu."}
:::

![Liste produite par tar indiquant que index.html se trouve dans site.tar.gz](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-build-artifacts/archive-contents.png)

## Relier un artefact à une exécution

Un workflow peut téléverser l’archive terminée. La page d’exécution indique la révision utilisée pour le build. Deux artefacts appelés `site.tar.gz` peuvent être différents s’ils proviennent de révisions différentes. Pour choisir le bon téléchargement, regardez à la fois l’exécution et la révision.

:::single-choice{#ci-build-artifacts-choose-run} Les exécutions 41 et 42 contiennent site.tar.gz. Comment identifier le paquet de la révision que vous avez vérifiée ?

::option[Prendre le premier téléchargement nommé site.tar.gz.]{#ci-build-artifacts-choose-run-b explanation="Le nom ne dit pas quels fichiers source ont produit l’artefact."}
::option[Prendre la dernière exécution réussie, quelle que soit la révision.]{#ci-build-artifacts-choose-run-c explanation="Une exécution plus récente peut réussir avec d’autres sources. Recherchez la révision que vous comptez utiliser."}
::option[Choisir l’exécution dont la révision correspond à celle que vous avez vérifiée.]{#ci-build-artifacts-choose-run-a .correct explanation="Plusieurs exécutions peuvent utiliser le même nom de fichier."}
:::

## Distinguer une archive d’une image de conteneur

Une archive du site contient des fichiers que vous pouvez extraire. Une image de conteneur inclut le système de fichiers et les réglages dont Docker se sert pour démarrer un conteneur. Un workflow peut publier une image dans un registre. Si vous comptez lancer cette image, conservez sa référence avec la révision source.

:::single-choice{#ci-build-artifacts-deployable-type} L’étape suivante doit démarrer un conteneur à partir d’un registre. À quel résultat doit-elle faire référence ?

::option[Au rapport de test téléchargé depuis l’exécution.]{#ci-build-artifacts-deployable-type-a explanation="Un rapport décrit les résultats mais ne fournit aucun système de fichiers de conteneur."}
::option[À la référence de l’image de conteneur publiée.]{#ci-build-artifacts-deployable-type-c .correct explanation="Docker peut utiliser la référence pour récupérer l’image préparée."}
::option[Au nom du fichier d’archive du site.]{#ci-build-artifacts-deployable-type-b explanation="L’archive contient les fichiers des pages. Son nom ne désigne pas une image dans un registre."}
:::

## Résumé

Vous savez maintenant reconnaître un artefact de build et retracer son origine.

1. Empaquetez les fichiers produits et vérifiez le contenu de l’archive.
2. Vérifiez quelle exécution et quelle révision source l’ont produit.
3. Choisissez un artefact de fichiers ou une image de conteneur selon les besoins de l’étape suivante.
