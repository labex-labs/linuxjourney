---
lesson_id: "ownership-permissions"
course_id: "permissions"
lang: "fr"
order_index: 3
title: "Permissions de propriété"
description: "Découvrez comment examiner et modifier l’utilisateur et le groupe propriétaires des objets d’un système de fichiers Linux."
meta_title: "Permissions de propriété - Permissions"
meta_description: "Maîtrisez la propriété des fichiers Linux avec les commandes chown et chgrp pour modifier l’utilisateur et le groupe propriétaires."
meta_keywords: "chown, chgrp, propriété fichiers Linux, modifier propriétaire fichier, modifier groupe fichier, permissions Linux, commandes Linux, tutoriel Linux"
---

Chaque objet d’un système de fichiers Linux enregistre un utilisateur propriétaire et un groupe propriétaire. Ces identités déterminent quel triplet de permissions du propriétaire ou du groupe s’applique, mais n’accordent pas elles-mêmes une permission particulière. Examinez la propriété et le mode avec `ls -l`.

## Modifier l’utilisateur propriétaire

Employez `chown`, abréviation de change owner, pour attribuer un autre utilisateur propriétaire :

```bash
$ sudo chown patty myfile
```

Cette commande attribue `myfile` à l’utilisateur `patty` et laisse son groupe inchangé. La modification de l’utilisateur propriétaire d’un fichier nécessite normalement les privilèges appropriés, même si vous possédez actuellement le fichier. Cette restriction empêche les utilisateurs de transférer des fichiers afin de contourner des quotas ou d’autres contrôles fondés sur la propriété.

:::single-choice{#ownership-permissions-change-user} Quelle commande attribue `myfile` à l’utilisateur `patty` tout en laissant son groupe inchangé ?

::option[`chown patty myfile`]{#ownership-permissions-user-with-chown .correct explanation="Un nom d’utilisateur seul comme opérande de propriété de `chown` modifie l’utilisateur propriétaire et conserve le groupe."}
::option[`chgrp patty myfile`]{#ownership-permissions-user-with-chgrp explanation="`chgrp` modifie le groupe propriétaire plutôt que l’utilisateur propriétaire."}
::option[`chmod patty myfile`]{#ownership-permissions-user-with-chmod explanation="`chmod` modifie les bits de mode et n’accepte pas de nom d’utilisateur comme nouveau propriétaire."}
:::

## Modifier le groupe propriétaire

Employez `chgrp` pour attribuer un autre groupe propriétaire :

```bash
$ chgrp whales myfile
```

Sur un système courant, un propriétaire sans privilèges ne peut attribuer son fichier qu’à un groupe dont il est membre. Les processus privilégiés peuvent effectuer des changements plus larges. La forme équivalente de `chown` commence par deux-points :

```bash
$ chown :whales myfile
```

Ensuite, les bits de mode du groupe s’appliquent lorsque le noyau sélectionne cette classe ; la modification du groupe n’ajoute pas automatiquement de bits de lecture, d’écriture ou d’exécution.

:::single-choice{#ownership-permissions-change-group} Que modifie `chgrp whales myfile` ?

::option[L’utilisateur propriétaire enregistré pour `myfile`.]{#ownership-permissions-group-not-user explanation="L’utilisateur propriétaire se modifie avec `chown`, et non `chgrp`."}
::option[Les membres inscrits dans le groupe `whales`.]{#ownership-permissions-group-members explanation="La commande modifie les métadonnées du fichier, pas la base d’appartenance aux groupes du système."}
::option[Le groupe propriétaire enregistré pour `myfile`.]{#ownership-permissions-group-owner .correct explanation="`chgrp` attribue le groupe nommé comme groupe propriétaire de l’objet du système de fichiers."}
:::

## Modifier simultanément l’utilisateur et le groupe

Transmettez `UTILISATEUR:GROUPE` à `chown` pour mettre à jour les deux champs en une opération :

```bash
$ sudo chown patty:whales myfile
```

La commande définit `patty` comme utilisateur propriétaire et `whales` comme groupe propriétaire. Vérifiez le résultat au lieu de supposer sa réussite :

```bash
$ ls -l myfile
```

:::single-choice{#ownership-permissions-change-both} Quelle spécification de propriété attribue l’utilisateur `patty` et le groupe `whales` dans une seule commande `chown` ?

::option[`patty:whales`]{#ownership-permissions-both-colon .correct explanation="Des deux-points séparent les noms de l’utilisateur et du groupe dans la spécification combinée."}
::option[`patty/whales`]{#ownership-permissions-both-slash explanation="La barre oblique n’est pas le séparateur d’un opérande utilisateur-groupe de `chown`."}
::option[`patty+whales`]{#ownership-permissions-both-plus explanation="Le signe plus ne combine pas les deux champs de propriété pour `chown`."}
:::

## Manipuler prudemment les changements récursifs

L’option `-R` modifie la propriété récursivement, mais une commande trop large peut traverser des arborescences inattendues ou affecter les données d’un service. Confirmez précisément la cible, comprenez le comportement de votre implémentation envers les liens symboliques, prévisualisez l’arborescence et vérifiez un petit échantillon avant de modifier une vaste hiérarchie. Ne transposez pas des exemples de commandes de propriété privilégiées sur des systèmes réels sans en examiner la portée.

:::single-choice{#ownership-permissions-mode-separate} Après la modification du groupe propriétaire d’un fichier, que deviennent ses bits ordinaires de permissions du groupe ?

::option[Ils deviennent toujours automatiquement la lecture et l’écriture.]{#ownership-permissions-mode-read-write explanation="`chgrp` ne sélectionne pas automatiquement un mode de groupe fixe."}
::option[Ils sont copiés depuis le triplet du propriétaire.]{#ownership-permissions-mode-copied explanation="Les triplets du propriétaire et du groupe restent indépendants lorsque la propriété change."}
::option[Ils restent inchangés, sauf si une opération distincte les modifie.]{#ownership-permissions-mode-unchanged .correct explanation="Les champs de propriété et les bits de mode sont des métadonnées distinctes ; changer le groupe n’accorde pas intrinsèquement de nouveaux bits au groupe."}
:::

Pour vous exercer dans un environnement isolé, l’atelier [Groupes d’utilisateurs Linux et permissions des fichiers](https://labex.io/fr/labs/linux-linux-user-group-and-file-permissions-18002) couvre l’examen et la modification de la propriété parallèlement aux modes des fichiers.

## Résumé

Vous savez maintenant distinguer les métadonnées de propriété des bits de permissions et les modifier délibérément.

1. Employer `chown UTILISATEUR FICHIER` pour modifier l’utilisateur propriétaire.
2. Employer `chgrp GROUPE FICHIER` ou `chown :GROUPE FICHIER` pour modifier le groupe propriétaire.
3. Employer `chown UTILISATEUR:GROUPE FICHIER` pour définir les deux champs.
4. Vérifier les résultats et limiter soigneusement la portée des changements récursifs.
