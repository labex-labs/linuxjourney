---
lang: "fr"
title: "udev"
meta_title: "udev - Périphériques"
meta_description: "Découvrez udev, comment il gère dynamiquement les fichiers de périphériques Linux, et utilisez udevadm. Comprenez la création de nœuds de périphériques pour les débutants."
meta_keywords: "udev, udevadm, gestion des périphériques Linux, fichiers de périphériques, tutoriel Linux, Linux pour débutants, règles udev, guide Linux"
---

## Lesson Content

Autrefois, et même aujourd'hui si vous le vouliez vraiment, vous créeriez des nœuds de périphérique en utilisant une commande telle que :

```bash
mknod /dev/sdb1 b 8 3
```

Cette commande créera un nœud de périphérique `/dev/sdb1` et en fera un périphérique bloc (b) avec un numéro majeur de 8 et un numéro mineur de 3.

Pour supprimer un périphérique, il vous suffirait de **rm** le fichier de périphérique dans le répertoire `/dev`.

Heureusement, nous n'avons plus vraiment besoin de faire cela grâce à udev. Le système udev crée et supprime dynamiquement les fichiers de périphérique pour nous, selon qu'ils sont connectés ou non. Il y a un démon `udevd` qui tourne sur le système, et il écoute les messages du noyau concernant les périphériques connectés au système. `Udevd` analysera ces informations et fera correspondre les données avec les règles spécifiées dans `/etc/udev/rules.d`. Selon ces règles, il créera très probablement des nœuds de périphérique et des liens symboliques pour les périphériques. Vous pouvez écrire vos propres règles udev, mais cela dépasse un peu le cadre de cette leçon. Heureusement, votre système est déjà livré avec de nombreuses règles udev, vous n'aurez donc peut-être jamais besoin d'écrire les vôtres.

Vous pouvez également consulter la base de données udev et sysfs en utilisant la commande **udevadm**. Cet outil est très utile, mais peut parfois devenir très complexe. Une commande simple pour afficher les informations d'un périphérique serait :

```bash
udevadm info --query=all --name=/dev/sda
```

## Exercise

Exécutez la commande `udevadm` donnée et vérifiez la sortie.

## Quiz Question

Qu'est-ce qui ajoute et supprime dynamiquement les périphériques ?

## Quiz Answer

udev
