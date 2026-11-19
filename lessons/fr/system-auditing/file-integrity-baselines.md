---
lesson_id: "file-integrity-baselines"
course_id: "system-auditing"
lang: "fr"
order_index: 4
title: "Références d’intégrité"
description: "Apprenez à lire un rapport d’intégrité et à décider quand approuver une nouvelle référence."
meta_title: "Références d’intégrité - Audit système"
meta_description: "Apprenez à lire un rapport d’intégrité et à décider quand approuver une nouvelle référence."
meta_keywords: "références d’intégrité, audit système, cybersécurité, Linux Journey"
---

Une **référence d’intégrité** consigne de manière fiable les propriétés attendues des fichiers à un moment connu. Un contrôle ultérieur peut y comparer les fichiers actuels et signaler les différences.

## Lire un rapport de différences

Cet extrait simulé compare un hôte à son dernier état approuvé.

```text
File                      Property  Previous  Current
/etc/journey/site.conf    content   hash-A    hash-B
/etc/journey/banner.txt   mode      644       640
/etc/journey/site.prev    present   yes       no
```

La première ligne montre une modification du contenu. La deuxième montre un changement de permissions. La troisième indique qu’un fichier précédemment suivi était absent lors du contrôle.

:::single-choice{#file-integrity-baselines-report-mode} Quelle ligne signale un changement des droits d’accès ?

::option[La ligne site.conf.]{#file-integrity-baselines-report-mode-a explanation="Elle signale un changement d’empreinte du contenu."}
::option[La ligne banner.txt.]{#file-integrity-baselines-report-mode-b .correct explanation="Le mode est passé de 644 à 640."}
::option[La ligne site.prev.]{#file-integrity-baselines-report-mode-c explanation="Cette ligne indique si le chemin existait."}
:::

![Rapport d’intégrité simulé comparant le contenu, les permissions et la présence des fichiers](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/file-integrity-baselines/reference-comparison.png)

## Vérifier la référence

Le rapport n’est utile que si l’ancienne référence est fiable. Conservez son identifiant et sa date de création. Une copie réalisée alors qu’un problème existait déjà peut produire une comparaison trompeuse. Demandez à quel état approuvé correspond la référence.

:::single-choice{#file-integrity-baselines-reference-source} Quelle référence est la plus utile pour examiner la configuration d’aujourd’hui ?

::option[Une copie approuvée et consignée avant la modification.]{#file-integrity-baselines-reference-source-a .correct explanation="Elle fournit un point de comparaison connu que la personne chargée de l’examen peut vérifier."}
::option[Une référence créée à partir des fichiers d’aujourd’hui dont l’état reste inexpliqué.]{#file-integrity-baselines-reference-source-b explanation="Elle intégrerait les différences avant leur examen."}
::option[La configuration d’un autre hôte sans contexte de comparaison.]{#file-integrity-baselines-reference-source-c explanation="Des hôtes aux rôles différents peuvent avoir des fichiers et des permissions différents."}
:::

## Examiner les différences avant d’actualiser la référence

Comparez chaque différence à une modification approuvée et vérifiez le fonctionnement du service. Si le changement de permissions de la bannière était prévu et celui de la configuration ne l’était pas, examinez-les séparément. Actualisez la référence une fois les écarts compris et validés. Gardez une trace de l’ancienne référence.

:::single-choice{#file-integrity-baselines-update-timing} Le changement de permissions de la bannière est approuvé et celui de site.conf reste inexpliqué. Que faire avant d’accepter une nouvelle référence ?

::option[Tout approuver parce qu’une ligne était attendue.]{#file-integrity-baselines-update-timing-a explanation="Les différences de fichiers correspondent à des modifications distinctes."}
::option[Jeter le rapport de différences.]{#file-integrity-baselines-update-timing-b explanation="Il consigne les points qui restent à examiner."}
::option[Examiner le changement inexpliqué de site.conf.]{#file-integrity-baselines-update-timing-c .correct explanation="L’actualisation de la référence doit suivre l’examen de l’état actuel."}
:::

Pour créer et comparer une référence d’intégrité dans un environnement d’exercice, essayez [Surveiller l’intégrité des fichiers](https://labex.io/tutorials/linux-file-integrity-monitoring-fim-656122).

## Résumé

Vous savez maintenant utiliser une référence comme élément de preuve pour une comparaison précise.

1. Distinguez le contenu, les permissions et la présence dans un rapport.
2. Vérifiez que la référence représente un état fiable.
3. Examinez les écarts inattendus avant d’accepter une nouvelle référence.
