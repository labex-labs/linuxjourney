---
lesson_id: "disk-usage"
course_id: "filesystem"
lang: "fr"
order_index: 9
title: "Utilisation du disque"
description: "Découvrez comment `df` et `du` mesurent différemment la consommation des blocs et des inodes d'un système de fichiers."
meta_title: "Utilisation du disque - Le système de fichiers"
meta_description: "Apprenez à contrôler l'utilisation et l'espace libre des disques Linux avec df et du, notamment les inodes avec df -i."
meta_keywords: "commande df, commande du, utilisation disque Linux, espace libre, df -i Linux, gestion disque, inodes, système de fichiers"
---

La capacité d'un système de fichiers possède au moins deux limites : les blocs de données et les objets de métadonnées comme les inodes. `df` indique l'allocation du point de vue du système de fichiers, tandis que `du` parcourt les chemins accessibles et additionne l'utilisation qui leur est attribuée. Ces valeurs répondent à des questions différentes et ne sont pas obligées de correspondre.

## Capacité du système de fichiers avec `df`

Affichez le type des systèmes de fichiers montés et les chiffres des blocs dans un format lisible :

```bash
$ df -hT
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/sda1      ext4  6.2G  2.3G  3.6G  40% /
```

`Size`, `Used` et `Avail` proviennent de la comptabilité du système de fichiers. L'espace disponible peut être inférieur au total moins l'espace utilisé en raison des blocs réservés, des métadonnées, des règles d'allocation, des quotas ou des arrondis. Exécutez `df` sur un chemin pour obtenir le système de fichiers qui le contient :

```bash
$ df -hT /var/log
```

:::single-choice{#disk-usage-df-scope} Qu'indique principalement `df` ?

::option[Le contenu en octets de chaque fichier d'un répertoire.]{#disk-usage-df-file-content explanation="La comptabilité d'une arborescence de répertoires relève d'outils comme `du`."}
::option[La capacité, l'utilisation et l'espace disponible au niveau du système de fichiers.]{#disk-usage-df-filesystem .correct explanation="Df interroge les statistiques d'allocation des systèmes de fichiers montés au lieu de parcourir chaque chemin."}
::option[Uniquement la taille physique imprimée sur l'étiquette du disque.]{#disk-usage-df-physical-label explanation="Ses chiffres décrivent la comptabilité du système de fichiers, pas seulement la capacité commerciale du matériel."}
:::

## Capacité en inodes

Les systèmes de fichiers qui allouent des objets comparables à des inodes peuvent les épuiser alors que des blocs restent libres :

```bash
$ df -i /var
```

Un grand nombre de petits fichiers peut consommer tous les inodes disponibles. Supprimer un gros fichier libère de nombreux blocs, mais généralement un seul inode ; supprimer de nombreux petits fichiers inutiles peut réduire la pression sur les inodes. Certains systèmes de fichiers allouent leurs métadonnées dynamiquement et présentent ces notions différemment.

:::single-choice{#disk-usage-inode-exhaustion} Que peut-il se produire lorsqu'un système de fichiers possède des blocs libres, mais plus aucun inode libre ?

::option[Chaque fichier existant double automatiquement de taille.]{#disk-usage-inode-double explanation="L'épuisement des inodes empêche l'allocation de nouvelles métadonnées et n'agrandit pas le contenu existant."}
::option[La création d'un autre fichier peut échouer.]{#disk-usage-inode-create-fail .correct explanation="Un nouvel objet du système de fichiers a besoin de métadonnées même s'il reste de la place pour ses données."}
::option[Le système de fichiers est converti en swap.]{#disk-usage-inode-swap explanation="L'épuisement d'une ressource ne change pas le type du système de fichiers."}
:::

## Utilisation des chemins avec `du`

Résumez l'espace alloué accessible sous un répertoire :

```bash
$ du -sh /var/log
```

Comparez ses enfants directs tout en restant sur un seul système de fichiers :

```bash
$ sudo du -xhd1 /var | sort -h
```

Les options GNU présentées signifient respectivement sortie lisible, profondeur maximale d'un niveau et limitation à un système de fichiers. Les permissions peuvent masquer des sous-arborescences et produire un total incomplet. Par défaut, `du` peut aussi ne compter qu'une seule fois les fichiers possédant plusieurs liens physiques, distinguer la taille apparente des blocs alloués et traiter les fichiers creux différemment selon les options.

:::single-choice{#disk-usage-du-purpose} Quelle commande résume l'espace alloué sous `/var/log` ?

::option[`df -i /var/log`]{#disk-usage-df-inodes explanation="Cette commande indique les statistiques d'inodes du système de fichiers qui contient le chemin."}
::option[`du -sh /var/log`]{#disk-usage-du-summary .correct explanation="Du parcourt l'arborescence indiquée et `-s` produit un seul résumé dans des unités lisibles."}
::option[`mount -a /var/log`]{#disk-usage-mount-a explanation="Le montage est sans rapport avec le résumé en lecture seule de l'utilisation d'un répertoire."}
:::

## Pourquoi `df` et `du` diffèrent

Parmi les causes courantes figurent :

- un processus conserve ouvert un fichier supprimé : ses blocs restent alloués, mais aucun chemin n'existe plus pour `du` ;
- les métadonnées, espaces réservés, journaux, reflinks, instantanés ou la compression du système de fichiers influencent la comptabilité ;
- un autre système de fichiers est monté dans l'arborescence parcourue ;
- les permissions empêchent `du` de lire certains répertoires ;
- les fichiers creux possèdent des tailles apparente et allouée différentes.

Pour les fichiers supprimés mais encore ouverts, examinez les processus autorisés avec un outil comme `lsof +L1` ; redémarrez ou signalez le service responsable selon sa procédure normale au lieu de tronquer des descripteurs inconnus.

:::single-choice{#disk-usage-deleted-open-file} Pourquoi `df` peut-il signaler de l'espace utilisé qu'un `du` fondé sur les chemins ne trouve pas ?

::option[`df` multiplie toujours la taille de chaque fichier par deux.]{#disk-usage-df-doubles explanation="Il n'existe aucune règle universelle de doublement."}
::option[Un fichier supprimé peut rester ouvert et alloué à un processus actif.]{#disk-usage-open-deleted .correct explanation="L'entrée de répertoire a disparu, mais le système de fichiers conserve les blocs jusqu'à la fermeture de la dernière référence ouverte."}
::option[`du` supprime automatiquement les fichiers après les avoir comptés.]{#disk-usage-du-deletes explanation="Du est un outil de comptabilité et ne supprime pas les fichiers parcourus."}
:::

## Enquêter sans aggraver l'incident

Partez du système de fichiers plein signalé par `df`, identifiez sa cible de montage avec `findmnt`, puis réduisez la portée des recherches `du` sur ce même système. Tenez compte des instantanés, couches de conteneurs, journaux, caches de paquets et règles de conservation des applications. Ne supprimez pas un fichier au seul motif qu'il est volumineux ; déterminez d'abord son propriétaire, sa sauvegarde, les obligations de conformité et le comportement du service.

:::single-choice{#disk-usage-safe-investigation} Quelle est la réaction la plus sûre après avoir trouvé un fichier volumineux ?

::option[Le supprimer immédiatement pendant que le service y écrit.]{#disk-usage-delete-immediately explanation="Cela peut détruire des données nécessaires et ne pas libérer d'espace si le fichier reste ouvert."}
::option[Exécuter `mkfs` sur le périphérique qui le contient.]{#disk-usage-mkfs-device explanation="Le formatage détruirait le système de fichiers au lieu de résoudre la croissance d'un seul fichier."}
::option[Identifier son propriétaire et son rôle dans la conservation avant de le modifier.]{#disk-usage-review-large-file .correct explanation="La taille seule ne prouve pas que le fichier est inutile ou peut être tronqué sans risque."}
:::

## Résumé

Vous savez maintenant rapprocher les rapports d'espace produits au niveau du système de fichiers et au niveau des chemins.

1. Employer `df` pour la capacité en blocs des systèmes de fichiers montés.
2. Employer `df -i` pour la pression sur les inodes lorsqu'elle est prise en charge.
3. Limiter les parcours `du` afin d'attribuer l'utilisation des chemins accessibles.
4. Rechercher les fichiers supprimés encore ouverts et les différences de comptabilité propres aux formats.
5. Appliquer les règles de propriété et de conservation avant de supprimer des données.
