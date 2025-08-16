---
lang: "fr"
title: "mount et umount"
description: "Apprenez à utiliser les commandes Linux mount et umount pour gérer les systèmes de fichiers. Comprenez le montage, le démontage des périphériques et les UUID pour les débutants."
keywords: "mount Linux, commande umount, monter un système de fichiers, UUID Linux, Linux débutant, tutoriel Linux, point de montage, guide Linux"
---

## Lesson Content

Avant de pouvoir visualiser le contenu de votre système de fichiers, vous devrez le monter. Pour ce faire, j'aurai besoin de l'emplacement du périphérique, du type de système de fichiers et d'un point de montage. Le point de montage est un répertoire sur le système où le système de fichiers va être attaché. Nous voulons donc essentiellement monter notre périphérique sur un point de montage.

Tout d'abord, créez le point de montage ; dans notre cas, **mkdir /mydrive**.

```bash
sudo mount -t ext4 /dev/sdb2 /mydrive
```

C'est aussi simple que ça ! Maintenant, lorsque nous allons dans /mydrive, nous pouvons voir le contenu de notre système de fichiers. Le **-t** spécifie le type de système de fichiers, puis nous avons l'emplacement du périphérique, puis le point de montage.

Pour démonter un périphérique d'un point de montage :

```bash
sudo umount /mydrive
```

ou

```bash
sudo umount /dev/sdb2
```

Rappelez-vous que le noyau nomme les périphériques dans l'ordre où il les trouve. Que se passe-t-il si le nom de notre périphérique change pour une raison quelconque après que nous l'ayons monté ? Eh bien, heureusement, vous pouvez utiliser l'ID universellement unique (UUID) d'un périphérique au lieu d'un nom.

Pour afficher les UUID sur votre système pour les périphériques de bloc :

```bash
pete@icebox:~$ sudo blkid
/dev/sda1: UUID="130b882f-7d79-436d-a096-1e594c92bb76" TYPE="ext4"
/dev/sda5: UUID="22c3d34b-467e-467c-b44d-f03803c2c526" TYPE="swap"
/dev/sda6: UUID="78d203a0-7c18-49bd-9e07-54f44cdb5726" TYPE="xfs"
```

Nous pouvons voir les noms de nos périphériques, leurs types de systèmes de fichiers correspondants et leurs UUID. Maintenant, lorsque nous voulons monter quelque chose, nous pouvons utiliser :

```bash
sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mydrive
```

La plupart du temps, vous n'aurez pas besoin de monter des périphériques via leurs UUID ; il est beaucoup plus facile d'utiliser le nom du périphérique, et souvent le système d'exploitation saura monter les périphériques courants comme les clés USB. Cependant, si vous avez besoin de monter automatiquement un système de fichiers au démarrage, par exemple si vous avez ajouté un disque dur secondaire, vous voudrez utiliser l'UUID, et nous aborderons cela dans la prochaine leçon.

## Exercise

Look at the manpage for `mount` and `umount` and see what other options you can use.

## Quiz Question

Quelle commande est utilisée pour attacher un système de fichiers ?

## Quiz Answer

mount
