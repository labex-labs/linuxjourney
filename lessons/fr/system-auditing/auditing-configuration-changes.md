---
lesson_id: "auditing-configuration-changes"
course_id: "system-auditing"
lang: "fr"
order_index: 5
title: "Modifications de configuration"
description: "Apprenez à rapprocher une modification approuvée, une différence de fichier et un événement d’audit."
meta_title: "Modifications de configuration - Audit système"
meta_description: "Apprenez à rapprocher une modification approuvée, une différence de fichier et un événement d’audit."
meta_keywords: "modifications de configuration, audit système, cybersécurité, Linux Journey"
---

Un ticket de changement indique l’action prévue. Une comparaison de fichiers montre les différences actuelles. Un événement d’audit décrit une action observée dans le périmètre couvert. Appuyez-vous sur ces trois sources pour établir ce que vous savez d’une modification de configuration.

## Retrouver la modification prévue

Examinez cette fiche de maintenance simulée.

```text
Approved: change banner.txt mode to 640
Window: 09:00–09:30 UTC
Host: web-01
```

Elle indique le fichier et la propriété concernés par l’autorisation. Une différence ailleurs requiert une explication distincte, même si elle apparaît pendant la même période.

:::single-choice{#auditing-configuration-changes-approve-scope} Quelle modification correspond à l’action approuvée ?

::option[Le contenu de site.conf a changé sur web-01.]{#auditing-configuration-changes-approve-scope-b explanation="Ce fichier de configuration sort du périmètre de l’autorisation."}
::option[Le fichier banner.txt a disparu d’un autre hôte.]{#auditing-configuration-changes-approve-scope-c explanation="L’opération signalée et l’hôte diffèrent tous deux."}
::option[Les permissions de banner.txt sont passées à 640 sur web-01.]{#auditing-configuration-changes-approve-scope-a .correct explanation="Le fichier, la propriété, l’hôte et le résultat correspondent à la fiche."}
:::

## Comparer les observations

Une comparaison révèle deux différences dans les fichiers, les permissions de la bannière et le contenu de `site.conf`. Un événement d’audit distinct, à 09:15, enregistre une écriture dans `site.conf` sur `web-01`. Cet événement vous donne une heure à examiner. L’autorisation de l’écriture reste à vérifier.

:::single-choice{#auditing-configuration-changes-source-comparison} Quelle conclusion tirer des deux observations sur site.conf ?

::option[L’écriture était autorisée, car elle a eu lieu pendant la période de maintenance.]{#auditing-configuration-changes-source-comparison-a explanation="Le ticket indique une autre action."}
::option[L’écriture enregistrée et la modification du contenu justifient d’examiner ce fichier.]{#auditing-configuration-changes-source-comparison-b .correct explanation="La comparaison indique la différence et l’événement d’audit aide à la situer dans le temps."}
::option[La modification de la bannière a provoqué l’écriture.]{#auditing-configuration-changes-source-comparison-c explanation="Ces observations ne permettent pas d’établir un lien de causalité entre les actions."}
:::

## Rédiger une note de suivi

Indiquez quelle différence correspond au plan et laquelle reste inexpliquée. Précisez le fichier, l’hôte, l’heure et la référence à la source. Vous pouvez ensuite comparer la configuration actuelle à la copie approuvée et vérifier si une autre autorisation couvre ce changement.

:::single-choice{#auditing-configuration-changes-useful-review} Que faut-il transmettre au sujet de site.conf ?

::option[Décrire la différence, citer l’écriture observée et demander le justificatif d’autorisation.]{#auditing-configuration-changes-useful-review-c .correct explanation="La note conserve les éléments observés et indique ce qui reste à vérifier."}
::option[Marquer la modification comme approuvée et omettre le chemin du fichier.]{#auditing-configuration-changes-useful-review-a explanation="Cela fait perdre la cible et suppose une autorisation absente des éléments recueillis."}
::option[Attribuer l’écriture à la personne responsable de la modification de la bannière.]{#auditing-configuration-changes-useful-review-b explanation="Les éléments disponibles ne permettent pas cette attribution."}
:::

## Comparer deux fiches de maintenance

Un autre ticket autorise une modification ultérieure de site.conf. Comparez l’heure observée, l’hôte cible et le fichier avec le ticket avant de clore l’examen. Une autorisation sur le bon fichier peut ne pas expliquer un événement antérieur.

:::single-choice{#auditing-configuration-changes-final-application} Le ticket couvre site.conf sur web-01 de 09:40 à 10:00. Quel point reste à vérifier pour l’écriture enregistrée à 09:15 ?

::option[Si site.conf existe en dehors du système de tickets.]{#auditing-configuration-changes-final-application-b explanation="La comparaison de fichiers montre déjà la configuration."}
::option[Si le ticket ultérieur explique automatiquement toutes les écritures précédentes.]{#auditing-configuration-changes-final-application-c explanation="L’autorisation s’applique à l’action et à la période indiquées."}
::option[Si une autorisation distincte couvre cette écriture antérieure.]{#auditing-configuration-changes-final-application-a .correct explanation="L’hôte et le chemin correspondent, mais l’heure enregistrée est en dehors de la période approuvée."}
:::

## Résumé

Vous savez maintenant reconstituer ce qui est établi au sujet d’une modification de configuration.

1. Relevez le périmètre prévu dans l’autorisation de changement.
2. Utilisez les comparaisons et les événements d’audit pour décrire les faits observés.
3. Expliquez ce qui reste à établir et choisissez la prochaine vérification.
