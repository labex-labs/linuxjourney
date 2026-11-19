---
lesson_id: "ci-builds-and-tests"
course_id: "continuous-integration"
lang: "fr"
order_index: 4
title: "Builds et tests"
description: "Apprenez à distinguer la préparation, le build et les tests avec une petite vérification locale."
meta_title: "Builds et tests - Intégration continue"
meta_description: "Apprenez à distinguer la préparation, le build et les tests avec une petite vérification locale."
meta_keywords: "builds, tests, code de sortie, intégration continue, DevOps, Linux Journey"
---

Il est plus facile d’interpréter un échec quand chaque phase a une tâche précise. La **préparation** fournit les fichiers d’entrée et les outils. Le **build** produit un résultat. Un **test** vérifie si les fichiers source ou le résultat satisfont une condition.

## Préparer le fichier d’entrée

Écrivez une page d’exemple dans un dossier d’exercice vide. La redirection écrase `index.html` si le fichier existe déjà. Utilisez donc un dossier neuf.

```bash
$ printf '%s\n' '<h1>Welcome</h1>' > index.html
```

Dans un job de CI, le checkout fournirait la page. Certains projets installent aussi des dépendances, c’est-à-dire les bibliothèques ou outils nécessaires au build ou aux tests.

:::single-choice{#ci-builds-and-tests-prepare-input} La page est introuvable avant même que la commande essaie de la copier. Quelle phase faut-il examiner en premier ?

::option[Le téléchargement de l’artefact dans un job ultérieur.]{#ci-builds-and-tests-prepare-input-a explanation="Le fichier d’entrée est nécessaire avant de pouvoir produire le résultat."}
::option[La préparation.]{#ci-builds-and-tests-prepare-input-b .correct explanation="Le fichier d’entrée aurait dû être fourni dans ce job."}
::option[Le temps de réponse en production.]{#ci-builds-and-tests-prepare-input-c explanation="Le problème concerne les fichiers sur le runner."}
:::

## Produire les fichiers de sortie

Copiez la page dans le dossier qui contiendra le site prêt à servir.

```bash
$ mkdir -p dist
$ cp index.html dist/index.html
```

L’option `-p` permet à `mkdir` de réussir même si le dossier existe déjà. La copie crée un fichier distinct dans le dossier de sortie. Les tests suivants peuvent examiner ce fichier.

:::single-choice{#ci-builds-and-tests-build-product} Quel fichier est prêt à être empaqueté une fois la copie réussie ?

::option[dist/index.html.]{#ci-builds-and-tests-build-product-a .correct explanation="Le build a déposé une copie dans le répertoire de sortie."}
::option[Une page déployée sur le site public.]{#ci-builds-and-tests-build-product-b explanation="Copier un fichier local ne démarre aucun service."}
::option[Un enregistrement de l’état du workflow.]{#ci-builds-and-tests-build-product-c explanation="Le build produit ici une page. Le runner suit l’état de la vérification séparément."}
:::

## Tester la page

Lancez ce contrôle juste après le build. L’option `-F` recherche du texte littéral et `-q` évite l’affichage des lignes qui correspondent. Le shell stocke le code de sortie de la dernière commande dans `$?`. Zéro indique que le texte a été trouvé. Un indique qu’aucune ligne ne correspond.

```bash
$ grep -Fq '<h1>Welcome</h1>' dist/index.html
$ echo "$?"
```

Vous devriez obtenir `0`. Le test a recherché le texte exact dans le fichier produit. Il n’a évalué ni les couleurs, ni l’affichage dans un navigateur, ni le temps de réponse.

:::single-choice{#ci-builds-and-tests-test-scope} Le test réussit. Que pouvez-vous en conclure ?

::option[La page est accessible depuis Internet.]{#ci-builds-and-tests-test-scope-a explanation="Le contrôle a lu un fichier de sortie local."}
::option[La page s’affiche dans tous les navigateurs pris en charge.]{#ci-builds-and-tests-test-scope-b explanation="Ce test n’a utilisé aucun navigateur."}
::option[Le fichier produit contient le texte attendu du titre.]{#ci-builds-and-tests-test-scope-c .correct explanation="C’est la condition que vérifie la commande grep."}
:::

![Vérification locale du titre dans LabEx, avec un code de sortie égal à zéro](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-builds-and-tests/heading-check.png)

## Résumé

Vous savez maintenant ce que démontre chaque phase d’une petite vérification de CI.

1. Préparez les fichiers nécessaires avant de lancer le build.
2. Repérez le fichier que produit le build.
3. Interprétez le code de sortie et identifiez exactement ce que le test vérifie.
