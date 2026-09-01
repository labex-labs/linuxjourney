---
lesson_id: "etc-group-file"
course_id: "user-management"
lang: "fr"
order_index: 5
title: "/etc/group"
description: "Découvrez comment les groupes locaux associent des noms aux GID et recensent les membres supplémentaires."
meta_title: "/etc/group - Gestion des utilisateurs"
meta_description: "Comprenez le fichier /etc/group sous Linux, ses GID, ses listes de membres et la résolution complète avec NSS."
meta_keywords: "/etc/group, Linux, gestion groupes, GID, permissions, groupes Linux"
---

`/etc/group` stocke les groupes locaux. Il associe leurs noms aux GID numériques et recense les membres explicites pour permettre des accès partagés.

## Groupes locaux et groupes résolus

Le fichier n'est qu'une source possible. NSS peut résoudre des groupes depuis les fichiers, annuaires ou autres bases configurées.

```bash
$ cat /etc/group
```

Interrogez la base résolue avec `getent` :

```bash
$ getent group
$ getent group developers
```

Les listes peuvent révéler noms de comptes et rôles internes ; relisez-les avant partage.

:::single-choice{#group-query-resolved-database} Quelle commande interroge la base de groupes résolue par NSS ?

::option[`getent group`]{#group-getent-all .correct explanation="`getent` consulte les sources NSS configurées pour les groupes."}
::option[`cat /etc/group`]{#group-cat-local explanation="Cette commande ne lit que le fichier local et peut omettre d'autres sources."}
::option[`groups /etc/group`]{#group-groups-file explanation="`groups` attend des noms d'utilisateurs, pas le chemin d'une base à interroger."}
:::

## Lire les quatre champs

```text
developers:x:1500:alice,bob
```

1. **Nom du groupe** : `developers`.
2. **Champ mot de passe** : souvent `x`, `*` ou un indicateur ; des données protégées peuvent figurer dans `/etc/gshadow`.
3. **GID** : identité numérique, ici `1500`.
4. **Liste des membres** : noms explicites séparés par des virgules, ici `alice` et `bob`.

Les mots de passe de groupe sont une fonction ancienne utilisée par `newgrp` dans certaines configurations. Ils ne constituent pas le mécanisme normal d'autorisation sudo et ne doivent pas être introduits par édition manuelle.

:::single-choice{#group-gid-field} Dans `developers:x:1500:alice,bob`, quel champ contient le GID ?

::option[Le deuxième, `x`]{#group-second-password explanation="Le champ 2 est l'indicateur de mot de passe."}
::option[Le quatrième, `alice,bob`]{#group-fourth-members explanation="Le champ 4 recense les membres explicites."}
::option[Le troisième, `1500`]{#group-third-gid .correct explanation="Le troisième champ séparé par des deux-points est le GID numérique."}
:::

:::single-choice{#group-explicit-member-field} Comment les noms des membres explicites sont-ils représentés ?

::option[Comme une liste séparée par des virgules au champ 4.]{#group-members-field-four .correct explanation="Le dernier champ contient les noms des membres supplémentaires séparés par des virgules."}
::option[Comme une liste séparée par des espaces au champ 2.]{#group-members-field-two explanation="Le champ 2 concerne le mot de passe ou son indicateur."}
::option[Comme des UID intégrés au nom du groupe.]{#group-members-in-name explanation="Nom du groupe et membres sont des champs distincts ; les membres ordinaires sont des noms de connexion."}
:::

## Tenir compte de l'appartenance principale

La liste de `/etc/group` ne répète normalement pas les utilisateurs dont l'enregistrement passwd désigne ce GID comme groupe principal. Alice appartient donc à `developers` si son GID principal vaut 1500, même avec :

```text
developers:x:1500:
```

Analyser seulement le champ 4 donne une vue incomplète.

:::single-choice{#group-primary-membership-visibility} Le passwd d'Alice utilise 1500 comme GID principal, mais son nom est absent du champ 4 du groupe. En est-elle membre ?

::option[Non, toute appartenance doit figurer au champ 4.]{#group-field-four-only explanation="Cela ignore l'appartenance principale et sous-estime les membres."}
::option[Oui, l'appartenance principale vient du champ GID de passwd.]{#group-primary-from-passwd .correct explanation="La liste explicite sert surtout aux appartenances supplémentaires ; le groupe principal est enregistré avec le compte."}
::option[Seulement si le champ mot de passe contient son nom.]{#group-password-member explanation="Le champ mot de passe ne déclare pas l'appartenance principale."}
:::

## Inspecter les groupes d'un utilisateur

```bash
$ id alice
$ groups alice
```

Ces commandes donnent une vue résolue. Sans opérande, `id` rapporte les groupes actifs dans les attributs du processus courant. Une nouvelle appartenance supplémentaire n'apparaît généralement pas dans une session déjà ouverte ; démarrez une nouvelle session authentifiée ou employez délibérément `newgrp` si adapté.

:::single-choice{#group-current-process-credentials} Quelle commande indique l'UID, le GID principal et les groupes supplémentaires du processus courant ?

::option[`id`]{#group-current-id .correct explanation="Sans utilisateur, `id` décrit les attributs d'identité du processus courant."}
::option[`cat /etc/group`]{#group-current-cat explanation="Le fichier local ne montre pas les groupes résolus actifs dans ce processus."}
::option[`getent passwd`]{#group-current-passwd explanation="Cette commande interroge les comptes, pas spécialement les groupes du processus."}
:::

## Modifier les groupes locaux en sécurité

Utilisez `groupadd`, `groupmod`, `groupdel`, `gpasswd` et `usermod`, pas un éditeur général. `usermod -aG GROUP USER` ajoute une appartenance ; `usermod -G ...` sans `-a` remplace toute la liste supplémentaire. Si une réparation manuelle est incontournable, employez `vigr` pour le verrouillage et `grpck` pour la validation, avec une voie de récupération.

Pour vous exercer :

1. **[Gérer les comptes Linux](https://labex.io/fr/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Créez et modifiez des comptes.
2. **[Gérer les groupes Linux](https://labex.io/fr/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Utilisez `groupadd`, `usermod` et `groupdel`.
3. **[Ajouter un utilisateur et un groupe](https://labex.io/fr/labs/linux-add-new-user-and-group-17987)** - Créez des comptes, groupes et appartenances.

## Résumé

Vous savez interpréter les groupes locaux et résoudre plus justement leurs membres.

1. Interroger les sources configurées avec `getent group`.
2. Lire les quatre champs séparés par des deux-points.
3. Repérer le GID et la liste explicite.
4. Inclure l'appartenance principale issue de passwd.
5. Examiner les attributs actifs avant de compter sur un changement.
