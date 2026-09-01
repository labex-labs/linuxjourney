---
lesson_id: "mounting-and-unmounting-filesystems"
course_id: "filesystem"
lang: "fr"
order_index: 6
title: "mount et umount"
description: "Découvrez comment attacher, examiner et détacher sans risque des systèmes de fichiers avec des sources et points de montage vérifiés."
meta_title: "mount et umount - Le système de fichiers"
meta_description: "Apprenez à utiliser les commandes mount et umount sous Linux pour attacher et détacher des systèmes de fichiers avec des UUID."
meta_keywords: "mount, umount, sudo umount, démontage Linux, monter système de fichiers, démonter périphérique, UUID Linux, point de montage"
---

Le montage attache un système de fichiers à un répertoire de l'espace de noms visible. La source peut être un périphérique bloc, un export réseau, un système de fichiers virtuel, une source de montage bind ou un autre objet propre à une implémentation. Le répertoire cible est appelé point de montage.

## Préparer et examiner un point de montage

Créez un répertoire au nom explicite lorsque les règles locales le demandent :

```bash
$ sudo mkdir -p /mnt/mydrive
```

Examinez-le avant le montage :

```bash
$ findmnt --target /mnt/mydrive
$ sudo ls -la /mnt/mydrive
```

Monter un système de fichiers sur un répertoire non vide masque les entrées existantes derrière le nouveau système jusqu'au démontage ; cela ne les supprime pas. Ce comportement peut perturber les applications et consommer de l'espace disque de façon invisible. Employez donc un point de montage vide et réservé à cet usage.

:::single-choice{#mount-umount-nonempty-target} Que deviennent les fichiers existants d'un répertoire lorsqu'un autre système de fichiers y est monté ?

::option[Ils sont automatiquement copiés dans le nouveau système de fichiers.]{#mount-umount-copied-files explanation="Le montage change le rattachement dans l'espace de noms et ne déplace pas le contenu du répertoire."}
::option[Ils sont définitivement effacés par le noyau.]{#mount-umount-erased-files explanation="Les fichiers réapparaissent normalement après le démontage, car ils étaient masqués et non supprimés."}
::option[Ils sont masqués par le montage jusqu'à son détachement.]{#mount-umount-hidden-files .correct explanation="Le répertoire sous-jacent subsiste, mais la recherche des chemins passe dans le système de fichiers monté."}
:::

## Monter un système de fichiers vérifié

Après avoir confirmé l'identité de la source, le type détecté et le contenu attendu, effectuez un montage explicite :

```bash
$ sudo mount -t ext4 /dev/PARTITION-VÉRIFIÉE /mnt/mydrive
```

L'option `-t` indique l'implémentation du système de fichiers. Mount peut souvent détecter le type, mais un type explicite et des options examinées rendent l'intention plus claire. Pour un contenu non fiable ou amovible, envisagez des options restrictives comme `ro`, `nosuid`, `nodev` et `noexec` si elles conviennent à la charge ; chacune a ses limites et ne doit pas être considérée comme un bac à sable complet.

Vérifiez ce qui est réellement monté :

```bash
$ findmnt --target /mnt/mydrive -o TARGET,SOURCE,FSTYPE,OPTIONS
```

Les montages sont propres à un espace de noms. Un montage créé dans un conteneur ou dans l'espace privé d'un service peut ne pas apparaître dans la vue d'un autre processus.

:::single-choice{#mount-umount-mount-role} Que fait la commande `mount` dans la méthode présentée ?

::option[Elle crée un nouveau système de fichiers et efface la source.]{#mount-umount-format-source explanation="La création d'un système de fichiers est une opération destructive `mkfs` distincte."}
::option[Elle attache une source de système de fichiers à un répertoire dans un espace de noms de montage.]{#mount-umount-attach-filesystem .correct explanation="La recherche des chemins sous la cible entre alors dans le système de fichiers attaché."}
::option[Elle modifie les limites des partitions du disque.]{#mount-umount-change-partitions explanation="La modification de la table de partitions est distincte du montage dans l'espace de noms."}
:::

## Employer les UUID des systèmes de fichiers

Les noms d'énumération comme `/dev/sdb2` peuvent changer. Découvrez les identifiants des systèmes de fichiers avec :

```bash
$ lsblk -f
$ sudo blkid
```

Montez ensuite un système de fichiers vérifié par son UUID :

```bash
$ sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mnt/mydrive
```

Un UUID identifie le système de fichiers, pas nécessairement le disque physique. Un reformatage le modifie, tandis qu'un clonage peut le dupliquer. Vérifiez son unicité avant d'attacher l'original et sa copie au même système.

:::single-choice{#mount-umount-uuid-benefit} Pourquoi l'UUID d'un système de fichiers est-il souvent préférable à `/dev/sdX` dans une configuration persistante ?

::option[Il empêche toute panne future des périphériques de stockage.]{#mount-umount-uuid-no-failure explanation="Un identifiant ne fournit ni redondance, ni réparation de l'intégrité, ni sauvegarde."}
::option[Il garantit que les systèmes de fichiers clonés possèdent des identifiants différents.]{#mount-umount-uuid-clone-unique explanation="Une copie au niveau des blocs peut reproduire l'UUID et créer un conflit."}
::option[Il est lié à l'identité du système de fichiers plutôt qu'à l'ordre d'énumération actuel.]{#mount-umount-uuid-identity .correct explanation="Le chemin du périphérique bloc peut changer tandis que les métadonnées du système de fichiers conservent son UUID."}
:::

## Démonter sans risque

Détachez le système par son point de montage exact :

```bash
$ sudo umount /mnt/mydrive
```

La commande s'écrit `umount`, sans le premier `n`. Un démontage réussi détache le système de fichiers une fois que le noyau a terminé les écritures nécessaires et que les références le permettent. Confirmez ensuite le résultat avec `findmnt` avant de débrancher le stockage.

Un démontage réussi n'est pas toujours la dernière opération nécessaire au retrait sûr d'un support amovible. Les piles de stockage des environnements de bureau peuvent proposer une action d'éjection ou de mise hors tension qui vide les caches du périphérique et désactive un appareil USB. Suivez la procédure de la plateforme et du matériel.

:::single-choice{#mount-umount-command-name} Quelle commande détache `/mnt/mydrive` ?

::option[`umount /mnt/mydrive`]{#mount-umount-umount-correct .correct explanation="`umount` détache le système de fichiers monté sur la cible indiquée."}
::option[`unmount /mnt/mydrive`]{#mount-umount-unmount-spelling explanation="Le nom de la commande standard omet le premier `n`."}
::option[`mkfs /mnt/mydrive`]{#mount-umount-mkfs-target explanation="Mkfs crée les structures d'un système de fichiers et ne doit pas servir à le détacher."}
:::

## Diagnostiquer un système de fichiers occupé

Le démontage échoue lorsque l'espace de noms conserve des références actives, par exemple des fichiers ouverts, le répertoire de travail d'un processus, des montages imbriqués, du swap ou d'autres couches de stockage. Recherchez la cause au lieu de forcer immédiatement l'opération :

```bash
$ findmnt --submounts /mnt/mydrive
$ sudo fuser -vm /mnt/mydrive
```

Sortez les shells de l'arborescence, arrêtez proprement l'application responsable et démontez les montages enfants avant leur parent. Le démontage différé et les options de forçage possèdent une sémantique particulière et peuvent laisser des références actives ou entraîner une perte de données ; ne les employez qu'en suivant un raisonnement de récupération documenté.

:::single-choice{#mount-umount-busy-cause} Quelle situation peut amener `umount` à signaler qu'un système de fichiers est occupé ?

::option[Le nom du répertoire de point de montage contient des lettres minuscules.]{#mount-umount-lowercase explanation="La casse du chemin ne crée pas à elle seule une référence active au système de fichiers."}
::option[Le répertoire de travail actuel d'un processus se trouve dans le montage.]{#mount-umount-cwd-busy .correct explanation="Le processus conserve une référence dans le système de fichiers monté, ce qui empêche son détachement ordinaire."}
::option[L'UUID du système de fichiers est plus long que le nom du périphérique.]{#mount-umount-uuid-length explanation="La longueur d'un identifiant est sans rapport avec la détection d'un état occupé."}
:::

Utilisez [Gérer les partitions et systèmes de fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845) pour vous exercer sur le stockage jetable prévu à cet effet.

## Résumé

Vous savez maintenant attacher et détacher des systèmes de fichiers dans une portée vérifiable.

1. Employer un point de montage vide et réservé à cet usage.
2. Vérifier la source, le type, les options et le montage obtenu.
3. Préférer un identifiant de système de fichiers unique pour les références persistantes.
4. Démonter par la cible et confirmer le détachement avant le retrait.
5. Diagnostiquer les références actives au lieu de forcer le démontage d'un système occupé.
