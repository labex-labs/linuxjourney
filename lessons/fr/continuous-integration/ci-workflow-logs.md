---
lesson_id: "ci-workflow-logs"
course_id: "continuous-integration"
lang: "fr"
order_index: 5
title: "Journaux de workflow"
description: "Apprenez à repérer l’étape en échec dans un workflow et à interpréter le premier message qui aide au diagnostic."
meta_title: "Journaux de workflow - Intégration continue"
meta_description: "Apprenez à repérer l’étape en échec dans un workflow et à interpréter le premier message qui aide au diagnostic."
meta_keywords: "journaux de workflow, diagnostic, intégration continue, DevOps, Linux Journey"
---

Le résultat d’un workflow indique son état général. Pour comprendre un échec, ouvrez le job concerné et lisez ses étapes dans l’ordre. Si une étape échoue, les suivantes peuvent être ignorées.

## Repérer le premier échec

Cette exécution simulée montre l’état de chaque étape du job de vérification de la page.

```text
Prepare: passed
Build page: failed
Check heading: skipped
Package site: skipped
```

Commencez par `Build page`. Les vérifications ignorées n’ont fourni aucun résultat sur la page. Une fois l’échec corrigé, vérifiez les étapes suivantes lors d’une nouvelle exécution.

:::single-choice{#ci-workflow-logs-first-failure} Quelle sortie devez-vous lire en premier ?

::option[Package site, car cette étape apparaît en dernier.]{#ci-workflow-logs-first-failure-a explanation="L’étape de création de l’archive a été ignorée lors de cette exécution."}
::option[Check heading, car le workflow vérifie une page.]{#ci-workflow-logs-first-failure-c explanation="L’état indique que la vérification du titre n’a pas été exécutée."}
::option[Build page, car cette étape a échoué avant l’exécution des autres.]{#ci-workflow-logs-first-failure-b .correct explanation="Son journal indique pourquoi les étapes suivantes ont été ignorées."}
:::

![Exécution CI simulée avec un build en échec et des étapes suivantes ignorées](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-workflow-logs/skipped-steps.png)

## Suivre la piste du message d’erreur

L’étape en échec affiche ces lignes.

```text
Run cp index.html dist/index.html
cp: cannot create regular file 'dist/index.html': No such file or directory
Process completed with exit code 1.
```

Le message indique le chemin de destination. Si le dossier parent `dist` est absent, la commande de copie ne peut pas y créer de fichier. Vérifiez si une commande précédente devait créer ce dossier avant la copie. Le code de sortie 1 indique un échec. Le message vous dit où chercher.

:::single-choice{#ci-workflow-logs-actionable-log} Le dossier dist est absent. Quel changement résout le problème signalé ?

::option[Modifier le titre que grep vérifie.]{#ci-workflow-logs-actionable-log-b explanation="La vérification du titre n’a pas été lancée. Rien n’indique encore que le texte est incorrect."}
::option[Créer dist avant de copier le fichier.]{#ci-workflow-logs-actionable-log-a .correct explanation="Le dossier de destination doit exister pour y créer le fichier."}
::option[Télécharger un artefact de l’étape ignorée.]{#ci-workflow-logs-actionable-log-c explanation="L’étape de création de l’archive n’a produit aucun artefact ici."}
:::

## Contrôler une nouvelle exécution

Après avoir corrigé le build, comparez la révision et l’état de chaque étape de la nouvelle exécution. Une copie réussie indique que le fichier de sortie existe. Lisez les résultats du test et de la création de l’archive avant de dire que le processus entier a réussi. Pour signaler un problème, gardez le premier message utile avec le nom de l’étape.

:::single-choice{#ci-workflow-logs-rerun-evidence} Dans la nouvelle exécution, Build page a réussi et Check heading a échoué. Qu’est-ce qui a changé ?

::option[Le build a réussi. Vous disposez maintenant d’un résultat de la vérification du titre à examiner.]{#ci-workflow-logs-rerun-evidence-c .correct explanation="Le premier échec qui reste se trouve maintenant à l’étape de test."}
::option[La nouvelle exécution ne compte pas, puisque le build précédent a échoué.]{#ci-workflow-logs-rerun-evidence-a explanation="Chaque exécution renseigne sur sa propre révision."}
::option[La création de l’archive a forcément réussi, puisque le build a réussi.]{#ci-workflow-logs-rerun-evidence-b explanation="Une étape ultérieure peut toujours échouer ou être ignorée."}
:::

## Résumé

Vous savez maintenant interpréter l’échec d’un workflow dans son contexte.

1. Repérez la première étape qui s’est exécutée et a échoué.
2. Utilisez la ligne du journal pour décider quoi examiner.
3. Après correction, vérifiez la nouvelle révision et les étapes suivantes.
