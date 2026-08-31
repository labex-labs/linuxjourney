---
lesson_id: "symlinks"
course_id: "filesystem"
lang: "fr"
order_index: 12
title: "Liens symboliques"
description: "Découvrez les différences entre liens symboliques et physiques concernant la résolution des chemins, l'identité des inodes et la portée du système de fichiers."
meta_title: "Liens symboliques - Le système de fichiers"
meta_description: "Explorez les liens symboliques et physiques sous Linux, leur création avec ln, leurs inodes et leurs différences de résolution et de durée de vie."
meta_keywords: "liens symboliques Linux, liens physiques, commande ln, symlink, inode, nombre de liens Linux, système de fichiers"
---

Une entrée de répertoire donne un nom à un inode. Un lien physique crée une autre entrée de répertoire pour le même inode, tandis qu'un lien symbolique crée un inode distinct dont le contenu est un chemin à résoudre. Cette différence détermine l'identité, la durée de vie et le comportement entre systèmes de fichiers.

## Créer et examiner un lien symbolique

Créez un lien symbolique avec `ln -s CIBLE NOM_DU_LIEN` :

```bash
$ printf '%s\n' 'example' > myfile
$ ln -s -- myfile myfilelink
$ ls -li myfile myfilelink
151   -rw-r--r-- 1 user user 8 ... myfile
93403 lrwxrwxrwx 1 user user 6 ... myfilelink -> myfile
```

Le lien symbolique possède son propre inode et stocke le texte `myfile`. Lorsqu'un programme suit `myfilelink`, la résolution du chemin se poursuit vers la cible. Affichez le texte stocké sans suivre le lien avec :

```bash
$ readlink myfilelink
```

:::single-choice{#symlinks-create-symbolic}
Quelle commande crée le lien symbolique `myfilelink` contenant la cible `myfile` ?

::option[`ln -s -- myfile myfilelink`]{#symlinks-ln-s .correct explanation="L'option `-s` demande un lien symbolique ; elle est suivie de la cible puis du nom du nouveau lien."}
::option[`ln -- myfile myfilelink`]{#symlinks-ln-hard explanation="Sans `-s`, `ln` demande un lien physique vers l'inode existant."}
::option[`readlink myfile myfilelink`]{#symlinks-readlink-create explanation="Readlink examine un lien symbolique et n'en crée pas."}
:::

## Cibles relatives et absolues des liens symboliques

Une cible absolue commence à `/`. Une cible relative est résolue par rapport au répertoire qui contient le lien symbolique, et non par rapport au répertoire actuel du shell lorsqu'une personne l'ouvre plus tard.

```bash
$ mkdir -p tree/data tree/current
$ printf '%s\n' 'value' > tree/data/item
$ ln -s ../data/item tree/current/item
```

Déplacer toute l'arborescence `tree` préserve cette relation relative. Déplacer seulement le lien ou sa cible peut la rompre. Un lien symbolique peut contenir une cible inexistante ; on dit alors qu'il est pendant ou cassé.

:::single-choice{#symlinks-relative-resolution}
À partir de quel emplacement la cible relative d'un lien symbolique est-elle résolue ?

::option[Le répertoire personnel de l'utilisateur qui l'a créé.]{#symlinks-creator-home explanation="L'identité du créateur ne devient pas une base de résolution permanente."}
::option[Le répertoire actuel du premier shell qui l'affiche.]{#symlinks-listing-shell explanation="Le contexte d'affichage ne réécrit pas la relation de cible stockée."}
::option[Le répertoire qui contient le lien symbolique.]{#symlinks-containing-directory .correct explanation="Le parcours du chemin substitue le texte relatif stocké à l'emplacement du lien."}
:::

## Créer un lien physique

Créez un autre nom pour un fichier ordinaire existant sans `-s` :

```bash
$ ln -- myfile myhardlink
$ ls -li myfile myhardlink
151 -rw-r--r-- 2 user user 8 ... myfile
151 -rw-r--r-- 2 user user 8 ... myhardlink
```

Les deux noms correspondent au même système de fichiers et au même numéro d'inode. Le nombre de liens passe à 2. Aucun nom n'est intrinsèquement « l'original » : modifier le contenu par l'un modifie l'objet partagé, et supprimer un nom laisse subsister l'autre.

Les liens physiques ne peuvent pas franchir les limites d'un système de fichiers, car un numéro d'inode n'a de sens qu'à l'intérieur de celui-ci. Linux interdit également aux utilisateurs ordinaires de créer des liens physiques vers des répertoires et peut restreindre les liens vers des fichiers dont ils ne sont pas propriétaires, afin d'éviter les cycles et les problèmes de sécurité.

:::single-choice{#symlinks-hard-link-inode}
Que partagent deux liens physiques vers un même fichier ordinaire ?

::option[Uniquement des noms semblables, mais des données distinctes.]{#symlinks-separate-data explanation="Cela décrirait des copies indépendantes, pas des liens physiques."}
::option[Un chemin stocké dans l'inode distinct d'un lien symbolique.]{#symlinks-stored-path explanation="Le texte d'un chemin est le mécanisme qui définit un lien symbolique."}
::option[Le même inode et le même contenu de fichier.]{#symlinks-same-inode .correct explanation="Chaque entrée de répertoire nomme le même objet du système de fichiers."}
:::

## Durée de vie et suppression

Supprimer un lien symbolique retire l'objet lien, pas sa cible :

```bash
$ rm -- myfilelink
```

La suppression du nom d'un lien physique diminue le nombre de liens de l'inode partagé. Le système de fichiers ne peut récupérer l'objet qu'une fois ce nombre arrivé à zéro et lorsqu'aucune description de fichier ouverte ni autre référence ne le maintient en vie.

Évitez la barre oblique finale lorsque vous supprimez un lien symbolique vers un répertoire, car la résolution d'un chemin qui se termine ainsi peut suivre la sémantique des répertoires selon la commande. Examinez le lien avec `ls -ld -- LIEN`, puis supprimez délibérément son nom.

:::single-choice{#symlinks-remove-symbolic}
Que se produit-il normalement lorsque vous supprimez le lien symbolique lui-même ?

::option[L'inode et le nom du lien symbolique sont supprimés, tandis que la cible subsiste.]{#symlinks-remove-link-only .correct explanation="Délier le lien symbolique n'agit pas sur l'objet désigné par le texte de sa cible."}
::option[La cible et tous ses liens physiques sont automatiquement effacés.]{#symlinks-remove-target explanation="Le lien symbolique est un objet distinct du système de fichiers et ne possède pas sa cible."}
::option[La cible est copiée dans le lien symbolique avant sa suppression.]{#symlinks-copy-target explanation="La suppression ne conserve pas le contenu de la cible dans le lien."}
:::

## Suivre les liens en toute sécurité

Les liens symboliques peuvent rediriger un programme privilégié hors du répertoire attendu ou changer entre la validation et l'utilisation. Les programmes sûrs doivent éviter les courses de type vérifier-puis-ouvrir sur les chemins et employer les interfaces relatives à un répertoire, sans suivi ou à résolution limitée adaptées au langage et au système d'exploitation.

Pour les examens courants :

- `ls -ld LIEN` affiche le lien lui-même ;
- `readlink LIEN` affiche le texte de sa cible stockée ;
- `stat LIEN` indique généralement les métadonnées du lien, tandis que `stat -L LIEN` le suit avec GNU coreutils ;
- `find -L` suit les liens et peut rencontrer des cycles : ne l'employez que délibérément.

Les permissions affichées sous la forme `lrwxrwxrwx` ne constituent pas une autorisation générale d'accès. Celui-ci dépend de la traversée des répertoires, des règles de suivi des liens et des permissions de la cible ; le propriétaire du lien symbolique compte aussi pour certaines règles des répertoires protégés.

:::single-choice{#symlinks-readlink-output}
Qu'affiche `readlink LIEN` par défaut ?

::option[Le texte du chemin stocké dans le lien symbolique.]{#symlinks-readlink-target-text .correct explanation="La commande examine l'objet lien sans lire le contenu du fichier cible."}
::option[La totalité des octets du fichier ordinaire cible.]{#symlinks-readlink-file-content explanation="Pour lire le contenu de la cible, employez une commande de lecture après l'avoir résolue délibérément."}
::option[Tous les liens physiques présents dans le système de fichiers.]{#symlinks-readlink-all-hard explanation="La découverte des liens physiques exige une recherche tenant compte des inodes et est sans rapport avec le texte cible d'un lien symbolique."}
:::

Utilisez [Gérer les fichiers et répertoires sous Linux](https://labex.io/fr/labs/comptia-manage-files-and-directories-in-linux-590835) pour vous exercer avec des fichiers jetables et comparer leurs numéros d'inodes.

## Résumé

Vous savez maintenant choisir et examiner le bon type de lien de système de fichiers.

1. Employer `ln -s CIBLE LIEN` pour un lien symbolique fondé sur un chemin.
2. Résoudre les cibles relatives depuis le répertoire qui contient le lien.
3. Employer `ln EXISTANT LIEN` pour créer un autre nom du même inode dans le même système de fichiers.
4. Distinguer la suppression d'un lien symbolique de celle d'un lien physique.
5. Éviter le suivi dangereux des liens dans les opérations privilégiées ou récursives.
