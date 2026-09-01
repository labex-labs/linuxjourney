---
lesson_id: "etc-passwd-file"
course_id: "user-management"
lang: "fr"
order_index: 3
title: "/etc/passwd"
description: "Apprenez à lire les enregistrements passwd locaux et à les distinguer de la vue complète des comptes fournie par NSS."
meta_title: "/etc/passwd - Gestion des utilisateurs"
meta_description: "Interprétez les sept champs de /etc/passwd sous Linux, notamment UID, GID, répertoire personnel et shell."
meta_keywords: "/etc/passwd, Linux, UID, GID, root:x:0:0, gestion utilisateurs"
---

`/etc/passwd` stocke les comptes locaux dans un format texte séparé par des deux-points. Il associe les noms de connexion aux UID et enregistre GID principal, description, répertoire personnel et programme de connexion.

## Enregistrements locaux et comptes résolus

```bash
$ cat /etc/passwd
```

Pour interroger la base passwd résolue par NSS :

```bash
$ getent passwd
$ getent passwd root
```

Le fichier local ne contient pas forcément tous les comptes connus. NSS peut les résoudre depuis des fichiers, annuaires, bases système ou autres sources. `getent` interroge la base passwd résolue. La première commande `getent` peut révéler des noms et métadonnées : relisez sa sortie avant publication.

:::single-choice{#passwd-query-resolved-database} Quelle commande interroge la base passwd résolue par NSS plutôt que le seul fichier local ?

::option[`cat /etc/passwd`]{#passwd-cat-local explanation="Cette commande affiche seulement le fichier local."}
::option[`cat /etc/shadow`]{#passwd-cat-shadow explanation="Le fichier shadow contient des données protégées et ne doit pas être affiché à cette fin."}
::option[`getent passwd`]{#passwd-getent-all .correct explanation="`getent` consulte les sources configurées pour la base passwd via NSS."}
:::

## Lire les sept champs

```text
root:x:0:0:root:/root:/bin/bash
```

Les sept champs sont :

1. **Nom de connexion** : nom lisible, tel que `root`.
2. **Champ mot de passe** : souvent `x`, qui renvoie aux données protégées.
3. **UID** : identité numérique ; l'UID 0 reçoit traditionnellement les pouvoirs du superutilisateur.
4. **GID principal** : identifiant numérique du groupe principal.
5. **GECOS/commentaire** : informations descriptives.
6. **Répertoire personnel** : chemin configuré, qui peut ne pas exister.
7. **Shell/programme de connexion** : par exemple `/bin/bash` ou un programme refusant la connexion.

Le noyau n'impose pas l'unicité des UID dans des enregistrements mal formés, mais deux comptes partageant un UID deviennent indistinguables pour de nombreux contrôles. Gardez-les normalement uniques.

:::single-choice{#passwd-uid-field} Dans `root:x:0:0:root:/root:/bin/bash`, quel champ contient l'UID ?

::option[Le deuxième, `x`]{#passwd-second-password explanation="Le deuxième est l'indicateur de mot de passe, pas l'identité numérique."}
::option[Le quatrième, le second `0`]{#passwd-fourth-gid explanation="Le champ 4 est le GID principal."}
::option[Le troisième, le premier `0`]{#passwd-third-uid .correct explanation="Le champ 3 est l'UID ; ce zéro désigne donc l'UID 0."}
:::

:::single-choice{#passwd-primary-gid-field} Quel champ d'un enregistrement passwd contient le GID principal ?

::option[Le champ 5]{#passwd-gecos-five explanation="Le cinquième est le champ GECOS ou commentaire."}
::option[Le champ 4]{#passwd-gid-four .correct explanation="Le quatrième champ identifie numériquement le groupe principal."}
::option[Le champ 7]{#passwd-shell-seven explanation="Le septième spécifie le shell ou programme de connexion."}
:::

## Interpréter l'indicateur de mot de passe

Sur un système shadow courant, `x` dans le champ 2 renvoie les outils aux données protégées de `/etc/shadow`. `*` ou `!` ne sont pas des hachages valides et empêchent généralement l'authentification par mot de passe Unix via cette entrée.

Cela ne prouve pas l'impossibilité de toute authentification : clés SSH, certificats, jetons ou mécanismes de service peuvent être indépendants. Un champ vide dépend de la pile d'authentification ; ne le créez ni ne le « corrigez » manuellement.

:::single-choice{#passwd-x-placeholder} Que signifie couramment `x` dans le champ 2 d'un `/etc/passwd` local ?

::option[Que le compte n'a assurément aucun moyen d'authentification.]{#passwd-no-auth-guarantee explanation="L'indicateur ne décrit pas tous les mécanismes possibles."}
::option[Que le répertoire personnel a été supprimé.]{#passwd-home-deleted explanation="Le répertoire figure au champ 6 et n'a aucun rapport avec `x`."}
::option[Que les données protégées du mot de passe se trouvent dans la base shadow.]{#passwd-shadow-placeholder .correct explanation="Le fichier public porte un indicateur tandis que hachage et vieillissement restent protégés."}
:::

## Reconnaître les comptes de service

De nombreux enregistrements représentent des services plutôt que des personnes. Leurs identités séparées limitent l'autorité d'un démon. Leur répertoire peut être atypique ou absent, et leur programme `/usr/sbin/nologin`, `/bin/false` ou un autre programme restreint.

Ne déduisez pas leur rôle de la seule plage d'UID : les règles varient selon les distributions et les comptes centraux.

:::single-choice{#passwd-nologin-shell} Quel est un rôle courant de `/usr/sbin/nologin` dans le champ 7 ?

::option[Supprimer les fichiers du compte à l'arrêt d'un service.]{#passwd-nologin-delete explanation="Le programme de connexion ne gère ni fichiers ni arrêt du service."}
::option[Empêcher un shell interactif ordinaire par les chemins de connexion qui respectent ce champ.]{#passwd-nologin-purpose .correct explanation="Cette configuration convient aux comptes de service qui ne doivent pas recevoir de shell interactif."}
::option[Accorder les privilèges de l'UID 0.]{#passwd-nologin-root explanation="Restreindre la connexion ne modifie pas l'UID ni les privilèges."}
:::

## Modifier les comptes en sécurité

Préférez `useradd`, `usermod` et `userdel`, qui coordonnent les enregistrements et appliquent les réglages du système. Si une réparation manuelle est indispensable, utilisez `vipw`, qui verrouille la base, puis validez avec `pwck`. Gardez une session de récupération avant de modifier à distance des fichiers d'authentification.

Pour vous exercer :

1. **[Gérer les comptes Linux avec useradd, usermod et userdel](https://labex.io/fr/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Pratiquez tout le cycle de vie des comptes.
2. **[Gérer les groupes Linux avec groupadd, usermod et groupdel](https://labex.io/fr/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Créez des groupes et modifiez les appartenances.

## Résumé

Vous savez interpréter les enregistrements passwd locaux sans les confondre avec toute la base d'identités.

1. Interroger les comptes résolus avec `getent passwd`.
2. Lire les sept champs séparés par des deux-points.
3. Repérer UID et GID principal.
4. Interpréter les indicateurs sans surestimer l'état de connexion.
5. Employer les outils de comptes ou `vipw`, pas un éditeur ordinaire.
