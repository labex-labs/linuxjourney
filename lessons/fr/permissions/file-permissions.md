---
lesson_id: "file-permissions"
course_id: "permissions"
lang: "fr"
order_index: 1
title: "Permissions des fichiers"
description: "Découvrez comment lire les types de fichiers Linux et les bits de permission du propriétaire, du groupe et des autres utilisateurs."
meta_title: "Permissions des fichiers - Permissions"
meta_description: "Découvrez les permissions des fichiers Linux, notamment les bits rwx de l’utilisateur, du groupe et des autres, ainsi que la sortie de ls -l et les modes des fichiers."
meta_keywords: "permissions des fichiers, permissions Linux, tutoriel Linux complet, permissions rwx, commande ls -l, modes des fichiers, guide Linux"
---

Linux représente de nombreuses ressources par des interfaces semblables à des fichiers, et chaque objet du système de fichiers possède des métadonnées qui contrôlent son accès. Savoir lire ces métadonnées est indispensable pour travailler en toute sécurité avec les fichiers et les répertoires.

## Lire une liste détaillée

Employez `ls -l` pour afficher une liste détaillée :

```bash
$ ls -ld Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 Desktop/
```

Le premier champ, `drwxr-xr-x`, associe un caractère de type de fichier à neuf caractères de permissions. La liste indique également que `pete` est le propriétaire et `penguins` le groupe associé au répertoire.

Le premier caractère décrit le type de l’objet. Les valeurs courantes comprennent :

- `-` pour un fichier ordinaire ;
- `d` pour un répertoire ;
- `l` pour un lien symbolique.

Il existe également d’autres types de fichiers spéciaux. Les neuf caractères restants représentent les permissions d’accès :

```text
d | rwx | r-x | r-x
```

:::single-choice{#file-permissions-type-character} Dans `drwxr-xr-x`, qu’indique le premier `d` ?

::option[L’objet est un lien symbolique.]{#file-permissions-type-link explanation="Un lien symbolique est normalement représenté par `l` à la position du type de fichier."}
::option[L’objet est un répertoire.]{#file-permissions-type-directory .correct explanation="Le premier caractère indique le type de fichier, et `d` désigne un répertoire."}
::option[Le propriétaire possède la permission de supprimer.]{#file-permissions-type-delete explanation="Les chaînes de modes Linux n’emploient pas `d` comme permission de suppression ; la première position décrit le type de l’objet."}
:::

## Comprendre `r`, `w` et `x`

Chaque triplet de permissions emploie ces caractères :

- `r` accorde la permission de lecture ;
- `w` accorde la permission d’écriture ;
- `x` accorde la permission d’exécution ;
- `-` signifie que la permission est absente.

Pour un fichier ordinaire, la lecture autorise l’accès à son contenu, l’écriture permet de le modifier et l’exécution permet au noyau d’essayer de le lancer comme programme. L’exécution peut tout de même échouer si le format du fichier, la ligne de l’interpréteur, les options de montage ou un autre contrôle de sécurité ne l’autorise pas.

Pour un répertoire, ces permissions concernent ses entrées :

- la lecture permet de répertorier les noms du répertoire ;
- l’écriture permet de créer ou de supprimer des entrées, normalement en combinaison avec la permission d’exécution ;
- l’exécution, également appelée permission de recherche, permet de traverser le répertoire et d’accéder aux entrées par leur nom.

La suppression d’un fichier dépend principalement des permissions de son répertoire parent, et non de son propre bit d’écriture.

:::single-choice{#file-permissions-directory-execute} Que permet principalement la permission d’exécution sur un répertoire ?

::option[Exécuter chaque fichier ordinaire conservé dans le répertoire.]{#file-permissions-directory-run-files explanation="Le bit d’exécution d’un répertoire n’accorde pas cette permission à chaque fichier qu’il contient."}
::option[Modifier le contenu de chaque fichier du répertoire.]{#file-permissions-directory-edit-files explanation="L’écriture dans les fichiers dépend de leurs permissions et d’autres contrôles d’accès."}
::option[Traverser le répertoire et accéder aux entrées par leur nom.]{#file-permissions-directory-search .correct explanation="La permission d’exécution, ou de recherche, d’un répertoire autorise sa traversée dans un chemin."}
:::

## Classes propriétaire, groupe et autres

Les neuf caractères du mode forment trois triplets dans un ordre fixe :

1. **Propriétaire** : permissions utilisées lorsque l’identifiant utilisateur effectif du processus correspond au propriétaire du fichier.
2. **Groupe** : permissions utilisées lorsqu’un identifiant de groupe applicable du processus correspond au groupe du fichier.
3. **Autres** : permissions utilisées lorsqu’aucune des deux classes précédentes ne correspond.

Le noyau sélectionne une seule classe applicable ; il ne combine pas les trois triplets pour obtenir le résultat le plus permissif. Des mécanismes supplémentaires tels que les listes de contrôle d’accès, les options de montage, les capacités ou les contrôles d’accès obligatoires peuvent encore influencer la décision finale.

Dans l’exemple, le triplet du propriétaire est `rwx`, tandis que ceux du groupe et des autres sont `r-x`. Le propriétaire peut lire, écrire et parcourir le répertoire. Les classes groupe et autres peuvent le lire et le parcourir, mais ne peuvent pas créer ou supprimer des entrées au moyen des bits ordinaires du répertoire.

:::single-choice{#file-permissions-triplet-order} Après le caractère du type de fichier, dans quel ordre apparaissent les trois triplets de permissions ?

::option[Groupe, propriétaire, puis autres.]{#file-permissions-order-group-first explanation="Le triplet du groupe est le deuxième, et non le premier."}
::option[Autres, groupe, puis propriétaire.]{#file-permissions-order-other-first explanation="Le triplet des autres est le dernier et celui du propriétaire le premier."}
::option[Propriétaire, groupe, puis autres.]{#file-permissions-order-owner-first .correct explanation="Les neuf caractères de permissions présentent toujours les triplets du propriétaire, du groupe et des autres dans cet ordre."}
:::

:::single-choice{#file-permissions-example-group} Quelles permissions ordinaires la classe groupe possède-t-elle dans `drwxr-xr-x` ?

::option[Lecture et écriture.]{#file-permissions-group-read-write explanation="Le triplet du groupe est `r-x` ; sa position d’écriture contient donc `-`."}
::option[Écriture et exécution.]{#file-permissions-group-write-execute explanation="Le triplet du groupe contient `r`, et non `w`, à sa première position."}
::option[Lecture et exécution.]{#file-permissions-group-read-execute .correct explanation="Le triplet central est `r-x`, ce qui accorde la lecture et l’exécution, mais pas l’écriture."}
:::

Pour renforcer ces notions dans un environnement isolé, essayez l’atelier [Groupes d’utilisateurs Linux et permissions des fichiers](https://labex.io/fr/labs/linux-linux-user-group-and-file-permissions-18002). Vous vous exercerez à lire les modes et à modifier la propriété et les permissions.

## Résumé

Vous savez maintenant interpréter le champ élémentaire des permissions dans une liste détaillée Linux.

1. Séparer le caractère du type de fichier des neuf bits de permissions.
2. Lire `r`, `w` et `x` selon que l’objet est un fichier ou un répertoire.
3. Diviser le mode en triplets du propriétaire, du groupe et des autres.
4. Relier les triplets au propriétaire et au groupe affichés par `ls -l`.
