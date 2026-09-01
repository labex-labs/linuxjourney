---
lesson_id: "inodes"
course_id: "filesystem"
lang: "fr"
order_index: 11
title: "Inodes"
description: "Découvrez comment les numéros d'inodes relient les noms des répertoires aux métadonnées et aux données des objets du système de fichiers."
meta_title: "Inodes - Le système de fichiers"
meta_description: "Explorez les inodes Linux, leurs métadonnées et numéros, et apprenez à contrôler leur utilisation avec df -i, ls -li et stat."
meta_keywords: "inode Linux, inodes, numéro inode, système de fichiers, df -i, ls -li, stat, liens physiques"
---

Dans les systèmes de fichiers Unix fondés sur les inodes, un répertoire associe chaque nom d'entrée à un numéro d'inode. L'inode représente l'objet du système de fichiers et consigne les métadonnées nécessaires pour trouver et interpréter ses données. Le chemin n'est donc pas enregistré comme identité principale propre à l'objet.

## Métadonnées associées à un inode

Les métadonnées couramment associées à un inode comprennent :

- le type d'objet et le mode de permissions ;
- le propriétaire utilisateur et groupe ;
- la taille logique et la comptabilité des blocs alloués ;
- le nombre de liens physiques ;
- les horodatages d'accès, de modification et de changement d'état ;
- les références aux données du fichier ou aux structures d'étendues propres au système de fichiers.

L'inode ne stocke normalement pas le nom de l'entrée de répertoire. Un système de fichiers peut aussi conserver des attributs étendus, listes de contrôle d'accès, une date de naissance, des données intégrées ou d'autres informations au moyen de structures propres au format.

`ctime` est la date de changement d'état de l'inode, pas nécessairement celle de création du fichier. Un horodatage distinct de naissance ou de création est facultatif et peut être indisponible.

:::single-choice{#inodes-name-location} Où le composant de chemin d'un fichier ordinaire est-il normalement associé à son numéro d'inode ?

::option[Dans l'ordonnanceur de processus.]{#inodes-scheduler-name explanation="L'état d'ordonnancement du processeur n'assure pas la recherche des chemins du système de fichiers."}
::option[Dans une entrée de répertoire.]{#inodes-directory-entry .correct explanation="Un répertoire associe un nom à un numéro d'inode dans ce système de fichiers."}
::option[Dans la table de partitions du disque.]{#inodes-partition-name explanation="Une table de partitions cartographie des régions de stockage, pas des noms de fichiers individuels."}
:::

## Numéros d'inodes et portée du système de fichiers

Affichez les numéros d'inodes avec :

```bash
$ ls -li
```

Le premier champ est le numéro d'inode. Examinez un objet plus en détail avec :

```bash
$ stat path
```

Un numéro d'inode n'est unique qu'au sein d'un système de fichiers et à un moment donné. Le même numéro peut exister dans un autre système, et un numéro peut être réutilisé après la libération de son inode. Pour identifier solidement un objet, employez à la fois l'identité du système de fichiers et le numéro d'inode plutôt que ce dernier seul.

:::single-choice{#inodes-number-scope} Dans quelle portée un numéro d'inode identifie-t-il un objet ?

::option[Dans tous les systèmes Linux du monde, pour toujours.]{#inodes-global-forever explanation="L'allocation des inodes est locale au système de fichiers et leurs identifiants sont réutilisables."}
::option[Dans un système de fichiers, à un moment donné.]{#inodes-one-filesystem .correct explanation="D'autres systèmes de fichiers peuvent employer le même numéro, et les numéros d'inodes libérés peuvent ensuite être réutilisés."}
::option[Uniquement dans le processus shell qui a créé le fichier.]{#inodes-shell-scope explanation="C'est le système de fichiers, et non un seul shell, qui maintient l'identité de l'inode."}
:::

## Liens physiques et références ouvertes

Plusieurs entrées de répertoire peuvent désigner le même inode : ce sont des liens physiques. La création d'un nouveau lien physique augmente le nombre de liens de l'objet. La suppression d'un nom le diminue sans supprimer les données tant qu'un autre lien subsiste.

Même après la suppression de la dernière entrée de répertoire, un fichier ouvert reste alloué jusqu'à la fermeture de la dernière référence d'un processus. Son nombre de liens peut être nul alors qu'un descripteur de fichier y accède encore. Cela explique pourquoi la suppression d'un gros journal ouvert ne réduit pas forcément immédiatement l'utilisation signalée par `df`.

:::single-choice{#inodes-unlinked-open-file} Quand les ressources d'un fichier délié sont-elles normalement libérées ?

::option[Immédiatement après la suppression d'un seul nom de lien physique.]{#inodes-one-link-removed explanation="D'autres liens physiques ou références ouvertes peuvent maintenir l'objet en vie."}
::option[Seulement lors du reformatage complet du système de fichiers.]{#inodes-reformat-only explanation="Les opérations normales de suppression et de fermeture récupèrent les inodes et blocs inutilisés."}
::option[Lorsque son nombre de liens vaut zéro et que sa dernière référence ouverte est fermée.]{#inodes-zero-links-no-opens .correct explanation="Les noms de répertoires et les descripteurs de fichiers des processus sont des références indépendantes à l'inode."}
:::

## Capacité en inodes

Sur les systèmes de fichiers dont le nombre d'inodes est fini ou communiqué, des millions de petits fichiers peuvent épuiser la capacité des métadonnées avant de remplir les blocs de données. Examinez la comptabilité des inodes des systèmes montés avec :

```bash
$ df -i
```

S'il ne reste aucun inode libre, la création d'un nouveau fichier peut échouer même lorsque `df -h` signale des blocs disponibles. Les stratégies d'allocation diffèrent : certains systèmes préallouent les structures d'inodes lors de leur création, tandis que d'autres gèrent les métadonnées dynamiquement et peuvent présenter leur capacité d'inodes autrement.

:::single-choice{#inodes-df-i-purpose} Qu'indique `df -i` lorsque le système de fichiers fournit une comptabilité des inodes ?

::option[Le contenu de chaque fichier dans l'ordre des inodes.]{#inodes-df-i-content explanation="Df indique des statistiques globales du système de fichiers et ne lit pas le contenu des fichiers."}
::option[La capacité en inodes utilisée et disponible.]{#inodes-df-i-capacity .correct explanation="Cette vue aide à diagnostiquer l'épuisement des objets de métadonnées indépendamment des blocs de données."}
::option[La révision du micrologiciel du disque.]{#inodes-df-i-firmware explanation="L'inventaire du micrologiciel est sans rapport avec l'utilisation des inodes."}
:::

## Cartographie des données propre au système de fichiers

Ne supposez pas que chaque inode possède exactement 12 pointeurs directs et trois pointeurs indirects. Cela décrit utilement certaines organisations classiques, mais ext4 moderne peut employer des étendues, tandis que XFS, Btrfs et d'autres systèmes utilisent des structures différentes. Les données intégrées et les étendues compressées ou copy-on-write modifient encore cette relation.

N'employez les outils de diagnostic propres au système de fichiers qu'en lecture seule ou dans des modes documentés lorsque la cartographie interne est importante. Pour l'administration courante, `stat`, `find -inum`, `df -i` et les outils tenant compte des liens fournissent des abstractions plus sûres.

:::single-choice{#inodes-layout-portability} Pourquoi ne faut-il pas supposer une organisation fixe des pointeurs pour chaque inode ?

::option[Les inodes ne font jamais référence aux données des fichiers.]{#inodes-no-data-reference explanation="Le système de fichiers doit associer l'objet à son contenu, même si le mécanisme varie."}
::option[Les implémentations emploient des structures différentes d'étendues, d'arbres et de données intégrées.]{#inodes-format-specific-layout .correct explanation="La cartographie sur disque entre l'inode et le contenu fait partie du format de chaque système de fichiers."}
::option[Chaque propriétaire choisit séparément l'organisation de ses inodes.]{#inodes-owner-layout explanation="L'implémentation et le format du système de fichiers déterminent la structure des métadonnées."}
:::

Utilisez [Gérer les fichiers et répertoires sous Linux](https://labex.io/fr/labs/comptia-manage-files-and-directories-in-linux-590835) pour comparer les numéros d'inodes et nombres de liens sur des fichiers jetables.

## Résumé

Vous savez maintenant relier chemins, inodes, liens et capacité du système de fichiers.

1. Considérer les entrées de répertoires comme des associations entre noms et numéros d'inodes.
2. Lire les métadonnées et horodatages sans confondre ctime avec la création.
3. Limiter la portée des numéros d'inodes à un système de fichiers et un moment.
4. Tenir compte des liens physiques et des descripteurs de fichiers ouverts.
5. Employer les modèles propres aux systèmes de fichiers plutôt qu'une organisation universelle des pointeurs.
