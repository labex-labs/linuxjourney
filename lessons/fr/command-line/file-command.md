---
lesson_id: "file-command"
course_id: "command-line"
lang: "fr"
order_index: 6
title: "file"
description: "Apprenez à identifier le type probable du contenu d'un fichier sans vous fier à son nom ou à son extension."
meta_title: "file - Ligne de commande"
meta_description: "Apprenez la commande Linux file avec des exemples pour identifier les fichiers texte, images, scripts, archives compressées, binaires et types MIME."
meta_keywords: "commande linux file, commande file, identifier type fichier linux, type mime linux, fichier texte, fichier binaire, fichier archive"
---

Dans la leçon précédente, vous avez utilisé `touch` pour créer un fichier sans extension. Sous Linux, le nom d'un fichier ne doit pas nécessairement décrire son contenu : un fichier nommé `funny.gif` n'est pas forcément une image GIF.

Utilisez la commande `file` pour inspecter un fichier et indiquer son type probable :

```bash
$ file banana.jpg
banana.jpg: JPEG image data
```

## Pourquoi les extensions ne suffisent pas

Les outils Linux n'ont généralement pas besoin d'une extension pour déterminer le type d'un fichier. Un script shell peut s'appeler `backup`, un fichier texte `README`, et une image porter une extension trompeuse. `file` examine des propriétés comme les métadonnées du système de fichiers et les motifs reconnaissables du contenu.

```bash
$ file README
README: ASCII text
$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable
```

Le résultat est une classification et non une garantie. Un fichier inhabituel, incomplet ou endommagé peut recevoir une description générale comme `data` plutôt qu'un type précis.

:::single-choice{#identify-misleading-extension} Un fichier nommé `report.jpg` peut ne pas contenir d'image. Quelle commande vérifie son type de contenu probable ?

::option[`ls report.jpg`]{#list-report explanation="`ls` confirme l'existence du nom et peut afficher ses métadonnées, mais ne classe pas le contenu du fichier."}
::option[`file report.jpg`]{#inspect-report .correct explanation="`file` examine le fichier et indique un type probable sans se fier uniquement au suffixe `.jpg`."}
::option[`touch report.jpg`]{#touch-report explanation="`touch` actualise les horodatages ou crée un fichier absent ; elle n'identifie pas le type du contenu."}
:::

## Vérifier plusieurs fichiers

Vous pouvez contrôler plusieurs fichiers à la fois :

```bash
$ file notes.txt image.png archive.tar.gz
notes.txt: ASCII text
image.png: PNG image data
archive.tar.gz: gzip compressed data
```

Vous pouvez aussi fournir un joker du shell. Le shell développe `*` en noms correspondants avant que `file` ne les examine :

```bash
$ file *
```

:::single-choice{#inspect-multiple-files} Quelle commande demande à `file` d'inspecter tous les noms non cachés auxquels `*` correspond dans le répertoire actuel ?

::option[`file *`]{#file-wildcard .correct explanation="Le shell développe `*` en noms non cachés correspondants, puis `file` examine chaque opérande obtenu."}
::option[`file .`]{#file-current-directory explanation="Un point désigne le répertoire actuel lui-même. Cette commande classe ce répertoire, pas chaque élément qu'il contient."}
::option[`file -b`]{#file-brief-no-operand explanation="L'option `-b` modifie la présentation de la sortie, mais cette commande ne fournit aucun fichier à inspecter."}
:::

## Afficher les informations MIME

L'option `-i` produit des informations au format MIME, notamment un type de média et, lorsqu'il est disponible, un jeu de caractères. Cette forme est utile lorsqu'un autre programme attend une valeur comme `text/html`.

```bash
$ file -i index.html
index.html: text/html; charset=us-ascii
```

:::single-choice{#show-mime-information} Quelle commande indique les informations au format MIME pour `index.html` ?

::option[`file -b index.html`]{#brief-index explanation="L'option `-b` omet le nom du fichier dans la description habituelle ; elle ne demande pas spécialement un format MIME."}
::option[`file -i index.html`]{#mime-index .correct explanation="L'option `-i` demande une sortie au format MIME, par exemple `text/html` avec des informations sur le jeu de caractères."}
::option[`file -L index.html`]{#follow-index explanation="L'option `-L` contrôle le traitement des liens symboliques ; elle ne choisit pas le format MIME."}
:::

## Options utiles de file

- `-i` : afficher les informations au format MIME ;
- `-b` : utiliser le mode bref et omettre le nom du fichier ;
- `-L` : suivre les liens symboliques et classer leur cible ;
- `-z` : essayer d'examiner le contenu des fichiers compressés.

Par exemple :

```bash
$ file -b notes.txt
ASCII text
```

:::single-choice{#omit-filename-from-output} Quelle commande classe `notes.txt` en omettant son nom dans la sortie ?

::option[`file -i notes.txt`]{#mime-notes explanation="L'option `-i` demande des informations au format MIME ; la sortie inclut normalement toujours le nom du fichier."}
::option[`file -z notes.txt`]{#compressed-notes explanation="L'option `-z` demande à `file` d'examiner si possible les données compressées ; elle n'active pas le mode bref."}
::option[`file -b notes.txt`]{#brief-notes .correct explanation="Le mode bref, sélectionné avec `-b`, affiche la classification sans le préfixe du nom de fichier."}
:::

## Résumé

Vous savez maintenant utiliser `file` pour déterminer ce qu'un fichier contient probablement.

1. Classer un fichier sans faire confiance à son extension.
2. Inspecter plusieurs chemins avec une seule commande.
3. Demander des informations au format MIME.
4. Adapter le traitement des liens, des données compressées et des libellés de sortie.
