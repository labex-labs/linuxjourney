---
lang: "fr"
title: "/etc/fstab"
description: "Découvrez /etc/fstab sous Linux, comment configurer les montages de systèmes de fichiers au démarrage et gérer les entrées de périphériques. Comprenez fstab pour les débutants !"
keywords: "/etc/fstab, Linux fstab, monter des systèmes de fichiers, démarrage Linux, tutoriel fstab, débutant, guide"
---

## Lesson Content

Lorsque nous voulons monter automatiquement des systèmes de fichiers au démarrage, nous pouvons les ajouter à un fichier appelé `/etc/fstab` (prononcé "eff es tab"), abréviation de table des systèmes de fichiers. Ce fichier contient une liste permanente des systèmes de fichiers qui sont montés.

```plaintext
pete@icebox:~$ cat /etc/fstab
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /               ext4    relatime,errors=remount-ro 0       1
UUID=78d203a0-7c18-49bd-9e07-54f44cdb5726 /home           xfs     relatime        0       2
UUID=22c3d34b-467e-467c-b44d-f03803c2c526 none            swap    sw              0       0
```

Chaque ligne représente un système de fichiers ; les champs sont :

- UUID - Identifiant du périphérique
- Mount point - Répertoire sur lequel le système de fichiers est monté
- Filesystem type - Type de système de fichiers
- Options - Autres options de montage ; voir la page de manuel pour plus de détails
- Dump - Utilisé par l'utilitaire dump pour décider quand faire une sauvegarde ; vous devriez simplement laisser la valeur par défaut à 0
- Pass - Utilisé par fsck pour décider dans quel ordre les systèmes de fichiers doivent être vérifiés ; si la valeur est 0, il ne sera pas vérifié

Pour ajouter une entrée, modifiez directement le fichier `/etc/fstab` en utilisant la syntaxe d'entrée ci-dessus. Soyez prudent lorsque vous modifiez ce fichier ; vous pourriez potentiellement vous compliquer la vie si vous faites une erreur.

## Exercise

Ajoutez le lecteur USB sur lequel nous avons travaillé comme entrée dans `/etc/fstab`. Lorsque vous redémarrerez, vous devriez toujours le voir monté.

## Quiz Question

Quel fichier est utilisé pour définir comment les systèmes de fichiers doivent être montés ?

## Quiz Answer

/etc/fstab
