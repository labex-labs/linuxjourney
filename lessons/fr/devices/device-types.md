---
index: 2
lang: "fr"
title: "types de périphériques"
meta_title: "types de périphériques - Périphériques"
meta_description: "Explorez les différents types de périphériques Linux, y compris les périphériques caractère, bloc, tube (pipe) et socket. Apprenez comment Linux gère les périphériques, comment identifier un fichier de périphérique avec `ls -l /dev`, et comprenez le rôle des numéros de périphérique majeurs et mineurs."
meta_keywords: "périphériques linux, types de périphériques linux, fichier de périphérique, périphérique caractère, périphérique bloc, numéros majeurs mineurs, linux pour périphériques, répertoire /dev"
---

## Lesson Content

Dans Linux, un principe fondamental est que « tout est un fichier ». Cette philosophie s'étend aux composants matériels, qui sont représentés par des fichiers spéciaux dans le système de fichiers. Comprendre ces **périphériques Linux** et leurs fichiers correspondants est crucial pour l'administration système. Commençons par explorer le répertoire `/dev`, l'emplacement traditionnel de chaque **fichier de périphérique**.

### Exploration des périphériques Linux dans /dev

You pouvez lister les fichiers dans le répertoire `/dev` pour voir comment le système représente les différents **périphériques Linux**.

```bash
$ ls -l /dev
brw-rw----   1 root disk      8,   0 Dec 20 20:13 sda
crw-rw-rw-   1 root root      1,   3 Dec 20 20:13 null
srw-rw-rw-   1 root root           0 Dec 20 20:13 log
prw-r--r--   1 root root           0 Dec 20 20:13 fdata
```

Voici une répartition des colonnes de gauche à droite :

- Permissions
- Propriétaire
- Groupe
- Numéro de périphérique majeur
- Numéro de périphérique mineur
- Horodatage
- Nom du périphérique

### Identification des types de périphériques Linux

Le premier caractère de la chaîne de permissions du résultat de `ls -l` indique le type de fichier. Pour un **fichier de périphérique**, vous verrez l'un des éléments suivants, ce qui aide à identifier les **types de périphériques Linux** spécifiques :

- `c` - caractère
- `b` - bloc
- `p` - pipe
- `s` - socket

### Périphériques de type Caractère

Ces périphériques transfèrent les données un caractère à la fois. De nombreux pseudo-périphériques, qui ne sont pas du matériel physiquement connecté mais fournissent des fonctions essentielles du système d'exploitation, sont représentés comme des périphériques de type caractère. Un exemple classique est `/dev/null`.

### Périphériques de type Bloc

Ces périphériques transfèrent les données en gros blocs de taille fixe. Vous constaterez souvent que le matériel de stockage, tel que les disques durs (`/dev/sda`), les SSD et d'autres composants de stockage de masse, sont représentés comme des périphériques de bloc, car ils sont optimisés pour l'accès aux données basé sur des blocs.

### Périphériques de type Pipe

Les tubes nommés, ou FIFOs (First-In, First-Out), permettent la communication inter-processus. Ils agissent comme des périphériques de type caractère mais canalisent leur sortie vers un autre processus au lieu d'un périphérique physique.

### Périphériques de type Socket

Les périphériques de type socket facilitent également la communication entre processus. Contrairement aux pipes, ils sont plus polyvalents et peuvent prendre en charge la communication entre plusieurs processus, même à travers un réseau.

### Comprendre les numéros de périphérique

Chaque **périphérique Linux** est identifié de manière unique par deux nombres : le **numéro de périphérique majeur** et le **numéro de périphérique mineur**. Vous pouvez les voir dans le résultat de `ls`, séparés par une virgule. Pour un périphérique avec les numéros **8, 0** :

Le numéro majeur (8) identifie le pilote responsable du périphérique. Dans ce cas, 8 est couramment utilisé pour les disques SCSI. Le numéro mineur (0) indique au pilote quelle instance spécifique du périphérique il s'agit. Ici, 0 représente le premier disque (`a`).

## Exercise

Pour appliquer ce que vous avez appris sur les **périphériques Linux**, nous vous recommandons les laboratoires pratiques suivants. Ces exercices vous aideront à gagner en confiance dans l'interaction et la gestion des périphériques dans des scénarios réels.

1.  **[Gérer les partitions et les systèmes de fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Entraînez-vous à créer et gérer des partitions de disque et des systèmes de fichiers, qui sont des périphériques de bloc fondamentaux sous Linux.
2.  **[Explorer les périphériques matériels sous Linux](https://labex.io/fr/labs/comptia-explore-hardware-devices-in-linux-590861)** - Apprenez à identifier et inspecter divers périphériques matériels, en comprenant comment ils sont représentés dans le répertoire `/dev`.
3.  **[Créer et activer un fichier d'échange sous Linux](https://labex.io/fr/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Acquérir une expérience pratique dans la création et l'activation d'un fichier d'échange, qui fonctionne comme un périphérique de mémoire virtuelle.

## Quiz Question

Quel est le symbole des périphériques de type caractère dans la commande `ls -l` ? (Fournissez le seul caractère anglais minuscule comme réponse)

## Quiz Answer

c
