---
lesson_id: "modifying-permissions"
course_id: "permissions"
lang: "fr"
order_index: 2
title: "Modifier les permissions"
description: "Découvrez comment modifier les bits de permissions Linux avec les modes symboliques et octaux de `chmod`."
meta_title: "Modifier les permissions - Permissions"
meta_description: "Apprenez à modifier les permissions sous Linux avec chmod, au moyen des méthodes symbolique et numérique, afin de gérer les accès aux fichiers et répertoires."
meta_keywords: "modifier permissions Linux, chmod, permissions des fichiers, sécurité Linux, permissions symboliques, permissions numériques"
---

La commande `chmod` modifie les bits de mode des fichiers et des répertoires. Normalement, seul le propriétaire du fichier ou un processus doté des privilèges nécessaires peut effectuer ce changement. Examinez le mode actuel avec `ls -l` avant et après l’exécution de `chmod`.

## Employer le mode symbolique

Un mode symbolique indique la classe de permissions à modifier, la manière de la modifier et les permissions concernées.

- `u` sélectionne la classe du propriétaire.
- `g` sélectionne la classe du groupe.
- `o` sélectionne la classe des autres.
- `a` sélectionne les trois classes.
- `+` ajoute des permissions, `-` les retire et `=` définit exactement la classe sélectionnée.

Par exemple, ajoutez la permission d’exécution pour le propriétaire :

```bash
$ chmod u+x myfile
```

Retirez la permission d’écriture au groupe :

```bash
$ chmod g-w myfile
```

Ajoutez la permission d’écriture au propriétaire et au groupe :

```bash
$ chmod ug+w myfile
```

Plusieurs clauses peuvent être séparées par des virgules. Cette commande accorde au propriétaire la lecture et l’écriture, au groupe la lecture seule, et aucune permission aux autres :

```bash
$ chmod u=rw,g=r,o= myfile
```

Si la classe est omise, comme dans `chmod +x myfile`, l’umask du processus influence les classes modifiées. La désignation explicite de la classe facilite l’examen du résultat voulu.

:::single-choice{#modifying-permissions-remove-group-write}
Quel mode symbolique retire la permission d’écriture au groupe sans modifier ses autres bits ?

::option[`chmod u-w myfile`]{#modifying-permissions-user-minus-write explanation="Cette commande retire l’écriture à la classe du propriétaire plutôt qu’à celle du groupe."}
::option[`chmod g-w myfile`]{#modifying-permissions-group-minus-write .correct explanation="`g` sélectionne le groupe, `-` retire un bit et `w` désigne la permission d’écriture."}
::option[`chmod g=w myfile`]{#modifying-permissions-group-equals-write explanation="L’opérateur `=` remplace la classe sélectionnée par la seule permission d’écriture au lieu de retirer celle-ci."}
:::

## Employer le mode octal

Un mode octal définit chaque triplet de permissions élémentaires par un chiffre. Additionnez ces valeurs au sein de chaque classe :

- `4` pour la lecture ;
- `2` pour l’écriture ;
- `1` pour l’exécution ;
- `0` pour aucune permission.

Les trois chiffres les plus à droite représentent le propriétaire, le groupe et les autres dans cet ordre. Par exemple :

```bash
$ chmod 755 myfile
```

Le mode `755` se développe ainsi :

- le `7` du propriétaire vaut `4 + 2 + 1`, soit `rwx` ;
- le `5` du groupe vaut `4 + 1`, soit `r-x` ;
- le `5` des autres vaut `4 + 1`, soit `r-x`.

Contrairement aux opérations symboliques `+` ou `-`, un mode octal fournit l’ensemble complet des permissions ordinaires. Une leçon ultérieure présente le premier chiffre facultatif employé pour les bits de mode spéciaux.

:::single-choice{#modifying-permissions-octal-read-value}
Quelle valeur octale représente la permission de lecture ?

::option[`1`]{#modifying-permissions-value-one explanation="La valeur `1` représente la permission d’exécution."}
::option[`2`]{#modifying-permissions-value-two explanation="La valeur `2` représente la permission d’écriture."}
::option[`4`]{#modifying-permissions-value-four .correct explanation="La permission de lecture contribue pour `4` au chiffre octal d’une classe."}
:::

:::single-choice{#modifying-permissions-mode-640}
Quelles permissions ordinaires `chmod 640 report` définit-il ?

::option[Lecture pour le propriétaire, écriture pour le groupe et exécution pour les autres.]{#modifying-permissions-640-separated explanation="Les chiffres octaux sont des sommes pour chaque classe, et non des colonnes distinctes de lecture, d’écriture et d’exécution."}
::option[Lecture et exécution pour le propriétaire, écriture pour le groupe, aucune pour les autres.]{#modifying-permissions-640-wrong-sums explanation="La valeur `6` du propriétaire correspond à la lecture et à l’écriture, tandis que la valeur `4` du groupe correspond à la lecture."}
::option[Lecture et écriture pour le propriétaire, lecture pour le groupe, aucune pour les autres.]{#modifying-permissions-640-correct .correct explanation="Les chiffres deviennent `6` (`rw-`) pour le propriétaire, `4` (`r--`) pour le groupe et `0` (`---`) pour les autres."}
:::

## Appliquer les changements en toute sécurité

N’accordez que les accès nécessaires aux utilisateurs et aux services. Évitez `chmod 777` comme raccourci de dépannage, car il accorde la lecture, l’écriture et l’exécution à chaque classe, souvent au prix d’un risque accru sans corriger la propriété, la traversée des répertoires, les ACL ou la politique du service.

Les changements récursifs exigent une prudence particulière. Prévisualisez l’arborescence cible, tenez compte des liens symboliques et des systèmes de fichiers montés, puis testez sur un périmètre réduit avant d’employer `chmod -R`. Après une modification, vérifiez le mode obtenu au lieu de supposer que la commande a affecté les objets voulus.

:::single-choice{#modifying-permissions-least-privilege}
Pourquoi `chmod 777` est-il généralement une mauvaise solution universelle à un problème d’accès ?

::option[Il retire toutes les permissions au propriétaire.]{#modifying-permissions-777-removes explanation="Chaque `7` accorde la lecture, l’écriture et l’exécution ; il ne retire pas les permissions du propriétaire."}
::option[Il accorde toutes les permissions élémentaires au propriétaire, au groupe et aux autres.]{#modifying-permissions-777-grants-all .correct explanation="Les trois classes reçoivent `rwx`, ce qui dépasse généralement les accès réellement nécessaires."}
::option[Il ne modifie que le groupe propriétaire du fichier.]{#modifying-permissions-777-group explanation="`chmod` modifie les bits de mode ; la propriété du groupe se change avec un outil tel que `chgrp` ou `chown`."}
:::

Pour vous exercer dans un environnement isolé, utilisez l’atelier [Groupes d’utilisateurs Linux et permissions des fichiers](https://labex.io/fr/labs/linux-linux-user-group-and-file-permissions-18002) et examinez chaque mode avant et après sa modification.

## Résumé

Vous savez maintenant modifier les bits de mode ordinaires de Linux avec des expressions `chmod` délibérées.

1. Employer le mode symbolique pour des ajouts, retraits ou affectations ciblés.
2. Construire les chiffres octaux à partir de la lecture `4`, de l’écriture `2` et de l’exécution `1`.
3. Lire les classes octales dans l’ordre propriétaire, groupe et autres.
4. Vérifier les changements et appliquer le moindre privilège nécessaire.
