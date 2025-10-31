---
index: 1
lang: "fr"
title: "/dev directory"
meta_title: "Répertoire /dev - Périphériques"
meta_description: "Découvrez la fonction du répertoire /dev sous Linux. Ce guide explique ce qu'est le dossier dev, comment l'explorer avec `ls /dev`, et le rôle des fichiers de périphériques pour le matériel système."
meta_keywords: "dev sous linux, répertoire /dev sous linux, dossier dev linux, ls /dev, commande dev linux, fichiers de périphériques, nœuds de périphériques, périphériques linux"
---

## Lesson Content

Sous Linux, chaque périphérique connecté à votre système, des disques durs aux claviers, est représenté par un fichier spécial. Ces fichiers, connus sous le nom de fichiers de périphériques ou nœuds de périphériques, permettent aux logiciels d'interagir avec les pilotes matériels. L'emplacement central de ces fichiers est le répertoire `/dev`.

### Qu'est-ce que le répertoire /dev sous Linux ?

Le répertoire `/dev` est une partie fondamentale de la hiérarchie du système de fichiers Linux. Il contient les fichiers spéciaux qui représentent les périphériques. Comme ceux-ci sont traités comme des fichiers ordinaires, vous pouvez utiliser des utilitaires de ligne de commande standard pour interagir avec eux. Par exemple, vous pouvez utiliser la commande `ls /dev` pour afficher une liste de tous les fichiers de périphériques actuellement présents sur votre système.

```bash
ls /dev
```

L'exécution de `ls /dev` révélera un grand nombre d'entrées, chacune correspondant à un composant matériel ou à un périphérique virtuel reconnu par le noyau.

### Interaction avec les fichiers de périphériques

Vous avez probablement déjà interagi avec un fichier de périphérique sans même vous en rendre compte. Un exemple courant de périphérique virtuel est `/dev/null`. Lorsque vous redirigez la sortie d'une commande vers `/dev/null`, vous l'envoyez à un périphérique spécial que le noyau sait simplement ignorer toute entrée.

Bien que vous utilisiez des commandes pour interagir avec le contenu de `/dev`, il est important de noter qu'il n'existe pas de commande `dev command in linux` spécifique. Au lieu de cela, vous utilisez des utilitaires existants comme `ls`, `cat`, et d'autres pour lire ou écrire dans ces fichiers de périphériques, bien que le faire directement nécessite de la prudence.

### L'évolution de /dev

Dans les anciens systèmes Unix et Linux, le répertoire `/dev` était statique. Cela signifiait que les fichiers de périphériques pour tout matériel possible étaient créés lors de l'installation. Cette approche entraînait un dossier `dev folder linux` encombré de fichiers de périphériques inutilisés pour du matériel qui n'était même pas présent. De plus, les noms des périphériques pouvaient changer entre les redémarrages en fonction de l'ordre dans lequel le noyau les détectait, provoquant des problèmes de configuration.

Heureusement, les systèmes Linux modernes utilisent une approche dynamique. Un système comme `udev` gère désormais l'environnement `/dev in linux`, créant et supprimant dynamiquement les fichiers de périphériques à mesure que le matériel est connecté et déconnecté. Cela garantit que `/dev` ne contient que des fichiers pour les périphériques actuellement utilisés et fournit un schéma de nommage persistant, rendant le système plus fiable et plus facile à gérer.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des périphériques matériels et de leur interaction avec le système Linux :

1. **[Explorer les périphériques matériels sous Linux](https://labex.io/fr/labs/comptia-explore-hardware-devices-in-linux-590861)** - Dans ce laboratoire, vous apprendrez les compétences essentielles pour explorer, identifier et inspecter les périphériques matériels dans un environnement Linux. Vous acquerrez une expérience pratique avec de puissants utilitaires de ligne de commande pour comprendre comment le système d'exploitation interagit avec les composants physiques.

Ce laboratoire vous aidera à appliquer les concepts d'interaction des périphériques dans des scénarios réels et à renforcer votre confiance dans la gestion du matériel sous Linux.

## Quiz Question

Où sont stockés les fichiers de périphériques sur le système ? (Veuillez fournir le chemin absolu. La réponse est sensible à la casse et doit être en anglais.)

## Quiz Answer

/dev
