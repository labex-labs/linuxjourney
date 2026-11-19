---
lesson_id: "incident-evidence-preservation"
course_id: "incident-response"
lang: "fr"
order_index: 2
title: "Conservation des preuves"
description: "Apprenez à conserver une entrée d’exercice, sa copie et sa somme de contrôle pour un examen ultérieur."
meta_title: "Conservation des preuves - Réponse aux incidents"
meta_description: "Apprenez à conserver une entrée d’exercice, sa copie et sa somme de contrôle pour un examen ultérieur."
meta_keywords: "conservation des preuves, réponse aux incidents, cybersécurité, Linux Journey"
---

Pendant une intervention, un extrait de journal peut aider à expliquer ce qui s’est passé. Préservez la source originale ou l’export approuvé avec les renseignements nécessaires pour qu’une autre personne puisse l’examiner.

## Consigner le contexte

Notez l’hôte, la source, le fuseau horaire et la période couverte. Indiquez qui a collecté les entrées et avec quel filtre. Privée de ce contexte, une ligne copiée peut être identique à une ligne d’une autre machine.

:::single-choice{#incident-evidence-preservation-context-fields} Un collègue reçoit une ligne horodatée à 09:22 sans autre contexte. Que faut-il ajouter ?

::option[Le chemin local où la copie a été enregistrée.]{#incident-evidence-preservation-context-fields-b explanation="Ce chemin aide à retrouver la copie. La source et l’heure d’origine restent inconnues."}
::option[Une hypothèse sur la cause.]{#incident-evidence-preservation-context-fields-c explanation="Consignez les détails de la collecte indépendamment de leur interprétation."}
::option[L’hôte source, le fuseau horaire et la période de collecte.]{#incident-evidence-preservation-context-fields-a .correct explanation="Ces précisions permettent de placer la ligne sur la bonne chronologie."}
:::

## Comparer une copie à son original

Dans un nouveau dossier d’exercice, enregistrez une ligne d’exemple sans contenu sensible, copiez-la et calculez les valeurs SHA-256 des deux fichiers. Utilisez uniquement le fichier d’exemple. Ces écritures remplacent les fichiers du même nom dans le dossier.

```bash
$ printf '%s\n' '09:22 UTC public homepage returned 503' > sample.log
$ cp sample.log review-copy.log
$ sha256sum sample.log review-copy.log
```

La première colonne donne une empreinte du contenu. Les deux valeurs devraient correspondre. Le contrôle compare les octets de la copie à ceux de l’original au moment de la vérification. L’exactitude de la consignation de l’événement d’origine reste à vérifier séparément.

:::single-choice{#incident-evidence-preservation-copy-meaning} Qu’indiquent les empreintes identiques ?

::option[L’horodatage de la source est forcément exact.]{#incident-evidence-preservation-copy-meaning-a explanation="Le calcul d’empreinte mesure le contenu du fichier et ne valide aucune horloge."}
::option[La copie d’examen contient les mêmes octets mesurés que l’exemple.]{#incident-evidence-preservation-copy-meaning-b .correct explanation="Les deux empreintes ont été calculées avec le même algorithme."}
::option[La copie a été approuvée pour diffusion publique.]{#incident-evidence-preservation-copy-meaning-c explanation="L’autorisation concerne les personnes qui peuvent consulter le fichier. Son empreinte ne dit rien sur cette autorisation."}
:::

![Sortie de sommes de contrôle enregistrée dans LabEx, montrant les empreintes identiques d’un fichier d’exercice et de sa copie d’examen](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-evidence-preservation/matching-copy-hashes.png)

## Préparer une copie qui peut être partagée

Gardez l’original intact et limitez-y l’accès. Si une autre équipe a seulement besoin de quelques champs, préparez un extrait distinct et retirez-en les informations sensibles. Indiquez que le contenu a été réduit et conservez la référence à la source protégée.

:::single-choice{#incident-evidence-preservation-redact-copy} De quel fichier faut-il retirer les informations sensibles avant le partage ?

::option[D’un extrait distinct préparé pour l’examen.]{#incident-evidence-preservation-redact-copy-c .correct explanation="Cela préserve la source et limite ce qui est partagé."}
::option[De l’original protégé pour que toutes les copies changent.]{#incident-evidence-preservation-redact-copy-a explanation="Cela altérerait les preuves à préserver."}
::option[Du texte de la somme de contrôle pour que le fichier modifié paraisse identique.]{#incident-evidence-preservation-redact-copy-b explanation="Conservez les valeurs mesurées et les fichiers qu’elles décrivent."}
:::

## Résumé

Vous savez maintenant préparer des preuves qu’une autre personne pourra interpréter.

1. Notez où et quand les éléments ont été collectés.
2. Vérifiez qu’une copie contient les mêmes octets que sa source.
3. Retirez les données sensibles d’un extrait séparé avant de le partager.
