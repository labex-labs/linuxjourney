---
lesson_id: "setgid-set-group-id"
course_id: "permissions"
lang: "fr"
order_index: 6
title: "Setgid"
description: "Découvrez comment set-group-ID affecte les identifiants des exécutables et l’héritage du groupe dans les répertoires partagés."
meta_title: "Setgid - Permissions"
meta_description: "Découvrez les permissions SGID ou Set Group ID sous Linux, leur fonctionnement, leur modification et leur rôle dans la sécurité."
meta_keywords: "SGID Linux, Set Group ID, permissions Linux, chmod g+s, sécurité Linux, Linux débutant, tutoriel Linux"
---

Le bit set-group-ID, couramment appelé setgid ou SGID, possède deux usages importants. Sur un fichier ordinaire exécutable, il peut modifier l’identifiant de groupe effectif du nouveau processus. Sur un répertoire, il fait hériter aux nouvelles entrées le groupe du répertoire, ce qui est particulièrement utile dans les arborescences collaboratives.

## Setgid sur les fichiers exécutables

Une liste détaillée peut afficher setgid à la position d’exécution du groupe :

```bash
$ ls -l /path/to/program
-rwxr-sr-x 1 root operators 24576 Jan 10 09:30 /path/to/program
```

Le `s` minuscule signifie que setgid et l’exécution du groupe sont tous deux définis. Le `S` majuscule signifie que setgid est défini mais que l’exécution du groupe est absente.

Lorsque le noyau honore ce bit pendant l’exécution, le processus reçoit un identifiant de groupe effectif dérivé du groupe propriétaire de l’exécutable. Des contrôles tels qu’un montage `nosuid` peuvent supprimer ce comportement, qui ne doit pas être considéré comme une garantie universelle pour chaque type de fichier ou environnement.

:::single-choice{#setgid-executable-effect}
Lorsque setgid sur un exécutable est honoré, quel identifiant provient du groupe propriétaire de l’exécutable ?

::option[L’identifiant de groupe effectif du processus.]{#setgid-effective-group .correct explanation="L’exécution set-group-ID définit le groupe propriétaire de l’exécutable comme identité de groupe effective du processus."}
::option[L’identifiant utilisateur réel du processus.]{#setgid-real-user explanation="Ce bit concerne l’identifiant de groupe, et non l’identité utilisateur réelle de l’appelant."}
::option[Le propriétaire de chaque fichier ouvert par le processus.]{#setgid-opened-owner explanation="Les identifiants d’exécution ne réécrivent pas les métadonnées de propriété des fichiers ouverts."}
:::

## Setgid sur les répertoires

Setgid sur un répertoire possède un autre rôle. Les nouveaux fichiers et sous-répertoires héritent normalement du groupe du répertoire plutôt que du groupe par défaut de leur créateur. Sous Linux, les nouveaux sous-répertoires héritent également du bit setgid, ce qui aide une arborescence de projet partagée à conserver un groupe cohérent.

Setgid n’accorde pas à lui seul l’écriture au groupe. Le mode du répertoire, l’umask du processus, le mode demandé lors de la création, les ACL par défaut et d’autres contrôles continuent de déterminer l’accès.

```bash
$ sudo chgrp developers /srv/project
$ sudo chmod g+s /srv/project
$ ls -ld /srv/project
drwxr-sr-x 2 root developers 4096 Jan 10 09:30 /srv/project
```

:::single-choice{#setgid-directory-inheritance}
De quoi setgid sur `/srv/project` fait-il normalement hériter un nouveau fichier ?

::option[De l’utilisateur propriétaire du répertoire.]{#setgid-inherit-user explanation="Setgid sur un répertoire affecte l’héritage du groupe, et non l’utilisateur propriétaire de la nouvelle entrée."}
::option[Du mode de permissions complet du répertoire.]{#setgid-inherit-mode explanation="Les permissions de création restent calculées à partir du mode demandé, de l’umask et des éventuelles ACL."}
::option[Du groupe propriétaire du répertoire.]{#setgid-inherit-group .correct explanation="Une nouvelle entrée reçoit normalement le groupe du répertoire setgid, ce qui assure une propriété partagée cohérente."}
:::

## Définir et retirer setgid

Définissez le bit symboliquement avec :

```bash
$ sudo chmod g+s myfile
```

Définissez-le avec les bits ordinaires au moyen d’un premier `2` octal :

```bash
$ sudo chmod 2755 myfile
```

Retirez uniquement le bit spécial avec `chmod g-s myfile`.

:::single-choice{#setgid-octal-value}
Quelle valeur setgid ajoute-t-il au premier chiffre octal des bits spéciaux ?

::option[`4`]{#setgid-value-four explanation="La valeur `4` représente setuid dans le chiffre des bits spéciaux."}
::option[`1`]{#setgid-value-one explanation="La valeur `1` représente le sticky bit."}
::option[`2`]{#setgid-value-two .correct explanation="Setgid contribue pour `2`, comme dans le mode `2755`."}
:::

## Employer les répertoires partagés en toute sécurité

Pour un répertoire collaboratif, associez le groupe propriétaire voulu, setgid et des bits d’accès choisis avec précision. Testez la création avec des utilisateurs représentatifs et examinez les résultats avec `ls -ld`. Évitez de rendre une arborescence accessible en écriture à tous simplement pour résoudre un problème de partage en groupe ; un groupe dédié, un umask ou une ACL par défaut appropriés et un répertoire setgid offrent généralement un contrôle plus clair.

:::single-choice{#setgid-directory-write-access}
La définition de setgid suffit-elle à autoriser les membres du groupe à créer des fichiers dans un répertoire ?

::option[Oui ; setgid ajoute toujours la lecture, l’écriture et l’exécution au groupe.]{#setgid-adds-rwx explanation="Le bit spécial ne modifie pas automatiquement les trois bits ordinaires de permissions du groupe."}
::option[Oui ; setgid désactive tous les contrôles pour les membres du groupe.]{#setgid-disables-checks explanation="Les contrôles discrétionnaires ordinaires et les contrôles de sécurité supplémentaires continuent de s’appliquer."}
::option[Non ; les permissions applicables d’écriture et de recherche doivent également autoriser la création.]{#setgid-no-automatic-write .correct explanation="Setgid contrôle l’héritage du groupe, tandis que les permissions ordinaires et les autres contrôles régissent les écritures dans le répertoire."}
:::

## Résumé

Vous savez maintenant distinguer les significations de setgid pour les exécutables et les répertoires.

1. Reconnaître setgid à la position d’exécution du groupe.
2. Relier setgid sur un exécutable à l’identifiant de groupe effectif.
3. Employer setgid sur un répertoire pour préserver la propriété du groupe dans les arborescences partagées.
4. Définir ou retirer le bit sans le confondre avec l’accès ordinaire en écriture.
