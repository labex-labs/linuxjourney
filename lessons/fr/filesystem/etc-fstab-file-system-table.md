---
index: 7
lang: "fr"
title: "/etc/fstab"
meta_title: "/etc/fstab - Le Système de Fichiers"
meta_description: "Apprenez à utiliser le fichier /etc/fstab sous Linux pour monter automatiquement les systèmes de fichiers au démarrage. Ce guide couvre la syntaxe fstab, comment éditer le fichier etc fstab en toute sécurité et son rôle au démarrage du système."
meta_keywords: "fstab, fstab linux, etc fstab, /etc/fstab, fichier fstab, monter systèmes de fichiers, démarrage Linux, tutoriel fstab"
---

## Lesson Content

Sous Linux, lorsque vous souhaitez monter automatiquement des systèmes de fichiers au démarrage, vous les configurez dans un fichier de configuration spécial situé à l'adresse `/etc/fstab`. Le nom `fstab` est l'abréviation de "filesystem table" (table des systèmes de fichiers), et ce fichier contient une liste permanente des systèmes de fichiers que le système doit monter pendant le processus de démarrage. Comprendre la configuration **fstab linux** est une compétence clé pour tout administrateur système.

### Qu'est-ce que /etc/fstab

Le fichier `/etc/fstab` est un fichier de configuration système qui définit toutes les partitions de disque disponibles et d'autres types de systèmes de fichiers et sources de données qui ne sont pas nécessairement basés sur des disques. Le système consulte ce fichier au démarrage pour déterminer quels systèmes de fichiers monter automatiquement.

Voici un exemple d'un **fichier fstab** typique :

```plaintext
pete@icebox:~$ cat /etc/fstab
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /               ext4    relatime,errors=remount-ro 0       1
UUID=78d203a0-7c18-49bd-9e07-54f44cdb5726 /home           xfs     relatime        0       2
UUID=22c3d34b-467e-467c-b44d-f03803c2c526 none            swap    sw              0       0
```

### La structure du fichier fstab

Chaque ligne dans le fichier **etc fstab** représente un système de fichiers et contient six champs séparés par des espaces ou des tabulations. Décomposons la signification de chaque champ :

- **Identifiant du périphérique** : Spécifie le périphérique à monter. Les systèmes modernes utilisent un UUID (Universally Unique Identifier) pour éviter les problèmes si le nom du périphérique (par exemple, `/dev/sda1`) change.
- **Point de montage** : Le répertoire dans le système de fichiers où le périphérique sera monté (par exemple, `/` ou `/home`).
- **Type de système de fichiers** : Le type de système de fichiers sur le périphérique, tel que `ext4`, `xfs`, `btrfs`, ou `swap`.
- **Options** : Options de montage qui contrôlent la manière dont le système de fichiers est monté. Les options courantes incluent `defaults`, `relatime`, et `errors=remount-ro`. Pour une liste complète, consultez la page de manuel `mount`.
- **Dump** : Ce champ est utilisé par l'utilitaire `dump` pour déterminer si un système de fichiers doit être sauvegardé. Une valeur de `0` signifie qu'il sera ignoré, ce qui est une valeur par défaut sûre.
- **Pass** : Ce champ est utilisé par `fsck` pour déterminer l'ordre de vérification des systèmes de fichiers au démarrage. Le système de fichiers racine (`/`) doit être `1`, les autres systèmes de fichiers doivent être `2`, et une valeur de `0` signifie que le système de fichiers ne sera pas vérifié.

### Comment éditer /etc/fstab

Vous pouvez ajouter une entrée en modifiant directement le fichier `/etc/fstab` à l'aide d'un éditeur de texte avec des privilèges root. Soyez extrêmement prudent lorsque vous éditez ce fichier ; une entrée incorrecte dans le **fstab** peut empêcher votre système de démarrer correctement. C'est toujours une bonne pratique de sauvegarder le fichier avant d'apporter des modifications. Après avoir enregistré vos modifications, vous pouvez les tester sans redémarrer en exécutant la commande `sudo mount -a`, qui monte tous les systèmes de fichiers listés dans `/etc/fstab`.

## Exercise

La pratique rend parfait ! L'expérience pratique est cruciale pour comprendre comment gérer les systèmes de fichiers et s'assurer qu'ils sont correctement montés au démarrage du système. Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des systèmes de fichiers Linux et du fichier `/etc/fstab` :

1. **[Gérer les partitions et les systèmes de fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Entraînez-vous à créer des partitions, à les formater, à les monter et à configurer le montage persistant à l'aide de `/etc/fstab`.
2. **[Créer et activer un fichier Swap sous Linux](https://labex.io/fr/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Apprenez la tâche administrative essentielle de création et d'activation d'un fichier swap, ce qui implique souvent des entrées dans `/etc/fstab`.

Ces laboratoires vous aideront à appliquer les concepts de montage et de configuration des systèmes de fichiers dans des scénarios réels et à renforcer votre confiance dans la gestion des ressources disque sous Linux.

## Quiz Question

Quel fichier est utilisé pour définir comment les systèmes de fichiers doivent être montés ? (Veuillez fournir le chemin complet. La réponse est sensible à la casse.)

## Quiz Answer

/etc/fstab
