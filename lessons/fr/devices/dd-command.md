---
index: 7
lang: "fr"
title: "dd"
meta_title: "dd - Périphériques"
meta_description: "Explorez l'outil puissant dd sous Linux. Ce guide explique comment utiliser la commande dd linux pour la copie de données efficace, l'imagerie disque et les sauvegardes. Apprenez les options clés comme if, of et bs."
meta_keywords: "commande dd, dd linux, outil dd, copier des données, imagerie disque, tutoriel Linux, débutant, guide, sauvegarde de données"
---

## Lesson Content

La commande `dd` est un utilitaire polyvalent et puissant pour convertir et copier des données. Elle fonctionne en lisant à partir d'un fichier d'entrée ou d'un flux de données et en écrivant vers un fichier de sortie ou un flux de données, ce qui en fait un `outil dd` essentiel pour de nombreuses tâches d'administration système.

### Comprendre la commande dd

À la base, `dd` copie les données octet par octet. Considérez la commande suivante :

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1024
```

Cette commande copie le contenu du fichier `backup.img` vers le périphérique de bloc `/dev/sdb`. Elle effectue cette opération en copiant les données par blocs de 1024 octets jusqu'à ce que l'intégralité du fichier d'entrée ait été lue.

### Options dd essentielles

Le comportement de la commande `dd` est contrôlé par plusieurs options clés :

- `if=fichier` : Spécifie le **fichier d'entrée**. `dd` lira à partir de ce fichier au lieu de l'entrée standard.
- `of=fichier` : Spécifie le **fichier de sortie**. `dd` écrira dans ce fichier au lieu de la sortie standard.
- `bs=octets` : Définit la **taille du bloc**. `dd` lit et écrit ce nombre d'octets à la fois. Vous pouvez utiliser des suffixes pour des unités plus grandes, comme `k` pour les kilo-octets (1024 octets), `M` pour les mégaoctets et `G` pour les gigaoctets. Par exemple, `bs=1M`.
- `count=nombre` : Copie uniquement ce **nombre de blocs** spécifié.

### Utilisation de bs et count ensemble

L'option `count` est utile lorsque vous devez copier une quantité spécifique de données. La quantité totale de données copiées sera `bs` multiplié par `count`. Par exemple, si vous exécutez la commande suivante sur un fichier de 10 Mo :

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1M count=2
```

Même si `backup.img` fait 10 Mo, cette commande indique à `dd` de copier 2 blocs, chacun de 1 Mo. Par conséquent, seuls 2 Mo de données seront copiés, ce qui entraînera un transfert incomplet. Bien que `count` soit précieux dans certains scénarios, vous pouvez souvent l'omettre si votre objectif est de copier un fichier entier. L'optimisation de `bs` peut améliorer considérablement les vitesses de transfert, mais les paramètres par défaut sont souvent suffisants.

### La puissance et le danger de dd

La commande `dd linux` est extrêmement puissante. Vous pouvez l'utiliser pour créer des sauvegardes de disques entiers, restaurer des images de disque et effacer des données de manière sécurisée. Cependant, cette puissance comporte un risque. Une petite erreur, comme inverser les valeurs `if` et `of`, peut entraîner une perte de données irréversible. Vérifiez toujours vos commandes avant de les exécuter, surtout lors de l'écriture sur un périphérique tel que `/dev/sda`.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la manipulation des données et de la gestion des disques sous Linux :

1. **[Créer et restaurer une sauvegarde avec tar sous Linux](https://labex.io/fr/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843)** - Entraînez-vous à créer et restaurer des sauvegardes de systèmes de fichiers, une compétence critique liée à l'intégrité et à la récupération des données, pour laquelle `dd` peut également être utilisé.
2. **[Gérer les partitions et les systèmes de fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Apprenez à gérer les partitions de disque et les systèmes de fichiers, y compris la création, le formatage et le montage, qui sont des concepts fondamentaux lorsque vous travaillez avec des outils comme `dd` pour l'imagerie disque.

Ces laboratoires vous aideront à appliquer les concepts de gestion des données et d'opérations sur disque dans des scénarios réels et à renforcer votre confiance dans les tâches d'administration système.

## Quiz Question

Quelle est l'option de `dd` pour la taille du bloc ? Veuillez répondre en utilisant uniquement des lettres anglaises minuscules.

## Quiz Answer

bs
