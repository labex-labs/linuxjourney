---
index: 6
lang: "fr"
title: "Monter et démonter"
meta_title: "mount et umount - Le système de fichiers"
meta_description: "Apprenez à utiliser les commandes mount et umount sous Linux pour attacher et détacher des systèmes de fichiers. Ce guide couvre le montage de périphériques, le processus sudo umount pour un démontage Linux sûr, et l'utilisation des UUID."
meta_keywords: "mount, umount, sudo umount, umount linux, démontage linux, umount debian, monter système de fichiers, démonter périphérique, UUID Linux, point de montage"
---

## Lesson Content

Avant de pouvoir accéder aux fichiers d'un périphérique de stockage, vous devez d'abord monter son système de fichiers sur un répertoire de votre système. Ce processus implique un emplacement de périphérique, un type de système de fichiers et un point de montage. Le point de montage est simplement un répertoire existant où le système de fichiers sera attaché.

### Comment monter un système de fichiers

Tout d'abord, vous devez créer un point de montage. Créons un répertoire à cet effet :

```bash
sudo mkdir /mydrive
```

Le point de montage étant prêt, vous pouvez utiliser la commande `mount` pour attacher votre périphérique. L'indicateur `-t` spécifie le type de système de fichiers.

```bash
sudo mount -t ext4 /dev/sdb2 /mydrive
```

C'est aussi simple que cela ! Maintenant, si vous naviguez vers le répertoire `/mydrive`, vous verrez le contenu du système de fichiers de votre périphérique.

### Comment démonter un système de fichiers sous Linux

Lorsque vous avez terminé avec un périphérique, vous devez le démonter pour vous assurer que toutes les données sont écrites en toute sécurité et que le système de fichiers est proprement détaché. La commande standard pour cette opération sous Linux est `umount`. Pour effectuer un `linux unmount`, vous pouvez spécifier soit le point de montage, soit le nom du périphérique.

En utilisant le point de montage :

```bash
sudo umount /mydrive
```

Alternativement, en utilisant le nom du périphérique :

```bash
sudo umount /dev/sdb2
```

Il est préférable d'utiliser `sudo umount` pour vous assurer que vous disposez des autorisations nécessaires pour détacher le système de fichiers. Cette commande est universelle sur les distributions Linux, donc la même syntaxe s'applique que vous soyez sur Ubuntu, Fedora, ou que vous effectuiez un `debian umount`. Notez que vous ne pouvez pas `umount` un périphérique s'il est actuellement utilisé (par exemple, si un fichier est ouvert ou si votre répertoire de travail actuel se trouve sur le périphérique).

### Utilisation des UUID pour un montage stable

Le noyau nomme les périphériques dans l'ordre où il les découvre, ce qui signifie qu'un nom de périphérique comme `/dev/sdb2` pourrait changer entre les redémarrages. Pour éviter les problèmes, vous pouvez utiliser l'identifiant unique universel (UUID) d'un périphérique, qui reste constant.

Pour afficher les UUID de vos périphériques de bloc, utilisez la commande `blkid` :

```bash
pete@icebox:~$ sudo blkid
/dev/sda1: UUID="130b882f-7d79-436d-a096-1e594c92bb76" TYPE="ext4"
/dev/sda5: UUID="22c3d34b-467e-467c-b44d-f03803c2c526" TYPE="swap"
/dev/sda6: UUID="78d203a0-7c18-49bd-9e07-54f44cdb5726" TYPE="xfs"
```

Ce résultat montre les noms des périphériques, leurs types de systèmes de fichiers et leurs UUID correspondants. Vous pouvez ensuite monter un périphérique en utilisant son UUID :

```bash
sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mydrive
```

Bien que vous n'ayez pas toujours besoin de monter des périphériques via leurs UUID, c'est la méthode recommandée pour monter automatiquement les systèmes de fichiers au démarrage, comme un disque dur secondaire. Nous aborderons ce processus dans la prochaine leçon.

## Exercise

La pratique rend parfait ! Voici un laboratoire pratique pour renforcer votre compréhension de la gestion des systèmes de fichiers Linux :

- **[Gérer les partitions et les systèmes de fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Dans ce laboratoire, vous apprendrez à gérer les partitions de disque et les systèmes de fichiers sous Linux. Vous utiliserez fdisk pour créer une nouvelle partition, la formater avec ext4, la monter, configurer le montage persistant dans /etc/fstab, et créer une partition swap, le tout sur un disque virtuel secondaire sécurisé.

Ce laboratoire vous aidera à appliquer les concepts de montage et de démontage dans des scénarios réels et à renforcer votre confiance dans la gestion des systèmes de fichiers.

## Quiz Question

Quelle commande est utilisée pour attacher un système de fichiers ? (Veuillez utiliser un seul mot anglais en minuscules pour votre réponse.)

## Quiz Answer

mount
