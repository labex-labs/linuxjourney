---
lesson_id: "compressed-archives-tar"
course_id: "packages"
lang: "fr"
order_index: 3
title: "tar et gzip"
description: "Découvrez comment archiver des fichiers avec `tar`, compresser des flux avec `gzip` et examiner les archives avant de les extraire en toute sécurité."
meta_title: "tar et gzip - Paquets"
meta_description: "Guide de tar et gzip sous Linux : création et extraction d’archives, différence entre archivage et compression, et gestion sûre des fichiers tar.gz."
meta_keywords: "tar et gzip, compression tar, gzip tar, compresser tar gz, archivage Linux, compression de fichiers, commande tar, commande gzip, tutoriel Linux"
---

L’archivage et la compression répondent à des besoins différents. Une archive rassemble une arborescence de répertoires et ses métadonnées dans un seul flux. La compression encode un flux afin de réduire sa taille. Par convention, un fichier `.tar.gz` est une archive tar dont le flux a été compressé avec gzip.

## Compresser un flux avec `gzip`

Par défaut, `gzip` compresse un fichier et remplace son nom d’origine par un fichier portant l’extension `.gz` :

```bash
$ gzip report.txt
```

Cette commande supprime normalement `report.txt` après avoir créé correctement `report.txt.gz`. Décompressez-le avec :

```bash
$ gunzip report.txt.gz
```

Employez `gzip -k report.txt` lorsque cette option est prise en charge pour conserver le fichier d’entrée, ou utilisez les flux standards lorsque vous souhaitez un contrôle explicite. Une extension de nom est une convention, et non une preuve du format réel ; des outils tels que `file` peuvent examiner le contenu.

:::single-choice{#tar-gzip-gzip-role} Quel est le rôle principal de `gzip` dans cette leçon ?

::option[Rassembler une arborescence de répertoires et ses métadonnées dans une archive.]{#tar-gzip-directory-archive explanation="Tar assure cette fonction d’archivage avant l’application de la compression gzip."}
::option[Compresser un seul flux d’entrée.]{#tar-gzip-compress-stream .correct explanation="Gzip transforme un flux d’octets et n’encode pas lui-même une hiérarchie de répertoires."}
::option[Installer les métadonnées de dépendances dans une base de paquets.]{#tar-gzip-package-install explanation="La compression est distincte de l’installation de paquets natifs et du suivi des dépendances."}
:::

## Créer une archive tar

Créez une archive non compressée avec :

```bash
$ tar -cvf project.tar file1 file2 directory1
```

- `-c` crée une nouvelle archive.
- `-v` affiche les membres pendant le traitement et reste facultatif.
- `-f project.tar` nomme le fichier d’archive ; comme `-f` consomme un argument, gardez le nom du fichier à côté de cette option.

Les chemins sont enregistrés comme noms de membres de l’archive. Créez les archives depuis un répertoire de travail choisi délibérément et évitez d’inclure involontairement des secrets, des caches, des sockets ou de vastes chemins absolus.

:::single-choice{#tar-gzip-create-option} Quelle option de `tar` crée une nouvelle archive ?

::option[`-x`]{#tar-gzip-option-extract explanation="L’opération `-x` extrait les membres de l’archive."}
::option[`-c`]{#tar-gzip-option-create .correct explanation="L’opération de création écrit une nouvelle archive à partir des entrées nommées."}
::option[`-t`]{#tar-gzip-option-list explanation="L’opération `-t` répertorie les membres de l’archive sans les extraire."}
:::

## Créer une archive tar compressée avec gzip

GNU tar et de nombreuses autres implémentations peuvent appeler gzip avec `-z` :

```bash
$ tar -czvf project.tar.gz file1 file2 directory1
```

Le résultat est un seul flux tar compressé avec gzip. La compression ne chiffre pas l’archive et ne dissimule pas son contenu à une personne capable de la lire et de la décompresser. Si la confidentialité est requise, employez une procédure de chiffrement authentifié appropriée et gérez les clés séparément.

:::single-choice{#tar-gzip-z-option} Que demande `-z` dans la commande `tar` présentée ?

::option[Chiffrer l’archive avec une clé à divulgation nulle.]{#tar-gzip-z-encrypt explanation="Ni tar ni gzip ne fournit de chiffrement par cette option."}
::option[Ignorer chaque membre de taille nulle.]{#tar-gzip-z-zero explanation="Cette option sélectionne gzip et ne filtre pas les membres selon leur taille."}
::option[Faire passer le flux de l’archive par gzip.]{#tar-gzip-z-gzip .correct explanation="L’option `z` relie l’opération d’archivage de tar à la compression ou à la décompression gzip."}
:::

## Répertorier avant d’extraire

Considérez une archive reçue d’un tiers comme une entrée non fiable. Répertoriez d’abord les noms de ses membres :

```bash
$ tar -tzf download.tar.gz
```

Recherchez les chemins absolus inattendus, les composants de traversée `..`, les liens symboliques ou physiques surprenants, les fichiers de périphérique et les noms susceptibles d’écraser des fichiers importants. Les implémentations modernes de tar appliquent des protections, mais leur comportement et leurs options varient, et l’extraction crée toujours des noms et du contenu choisis par l’auteur de l’archive.

Extrayez dans un nouveau répertoire intermédiaire sans privilèges :

```bash
$ mkdir extraction-stage
$ tar -xzf download.tar.gz -C extraction-stage
```

N’extrayez pas en tant que root une archive qui n’a pas été examinée. Vérifiez les éléments créés avant de déplacer les fichiers sélectionnés vers leur emplacement final.

:::single-choice{#tar-gzip-list-before-extract} Quelle opération répertorie les membres d’une archive sans les extraire ?

::option[`tar -czf download.tar.gz .`]{#tar-gzip-create-download explanation="Cette commande crée ou remplace une archive à partir du répertoire actuel."}
::option[`tar -xzf download.tar.gz`]{#tar-gzip-extract-download explanation="L’opération `-x` écrit les membres dans le répertoire cible."}
::option[`tar -tzf download.tar.gz`]{#tar-gzip-list-members .correct explanation="L’opération `-t` lit et affiche la table des membres tandis que `-z` gère gzip."}
:::

## Autres formats de compression

Les implémentations de tar peuvent fonctionner avec des compresseurs tels que bzip2 et xz, généralement sélectionnés respectivement avec `-j` et `-J` dans GNU tar. La prise en charge des formats et leur détection automatique diffèrent ; consultez `tar --help` ou le manuel local. ZIP est un format d’archive distinct, manipulé avec des outils tels que `zip` et `unzip`.

:::single-choice{#tar-gzip-archive-confidentiality} La compression gzip rend-elle une archive tar confidentielle ?

::option[Non ; toute personne capable de la lire peut généralement la décompresser.]{#tar-gzip-not-encryption .correct explanation="La compression modifie la représentation et la taille, mais n’apporte ni contrôle d’accès ni secret cryptographique."}
::option[Oui ; gzip dérive une clé de chiffrement du nom du fichier.]{#tar-gzip-filename-key explanation="Gzip ne met en œuvre aucun mécanisme de chiffrement de ce type."}
::option[Oui ; tar chiffre chaque membre avant que gzip ne le traite.]{#tar-gzip-tar-encrypt explanation="Tar archive les membres, mais ne chiffre pas automatiquement leur contenu."}
:::

Entraînez-vous avec des fichiers jetables dans [Empaquetage et compression de fichiers](https://labex.io/fr/labs/linux-file-packaging-and-compression-385413), puis appliquez l’examen et l’extraction intermédiaire dans [Créer et restaurer une sauvegarde avec tar](https://labex.io/fr/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843).

## Résumé

Vous savez maintenant associer en toute sécurité l’archivage tar et la compression gzip.

1. Distinguer une archive tar de la compression gzip.
2. Créer des archives avec `-c` et des flux gzip avec `-z`.
3. Répertorier les membres avec `-t` avant de les extraire avec `-x`.
4. Extraire le contenu non fiable dans un répertoire intermédiaire sans privilèges.
5. Distinguer la compression du chiffrement.
