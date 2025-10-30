---
index: 1
lang: "fr"
title: "Hiérarchie du Système de Fichiers"
meta_title: "Hiérarchie du Système de Fichiers - Le Système de Fichiers"
meta_description: "Explorez la hiérarchie standard du système de fichiers Linux (FHS). Ce guide explique l'objectif des répertoires clés tels que /bin, /etc, /home et /var, offrant un aperçu clair de la hiérarchie du système de fichiers sous Linux."
meta_keywords: "hiérarchie système de fichiers linux, hiérarchie système de fichiers sous linux, structure hiérarchie fichiers linux, hiérarchie fichiers linux, FHS, structure répertoires linux"
---

## Lesson Content

Vous vous familiarisez probablement avec la structure des répertoires sur votre système. La plupart des distributions Linux organisent leurs systèmes de fichiers selon la norme **Hiérarchie du Système de Fichiers Linux** (FHS). Cette norme garantit que les fichiers sont stockés dans des emplacements prévisibles, rendant les systèmes plus cohérents.

Pour voir les répertoires de plus haut niveau, exécutez la commande `ls -l /`. Bien que votre système puisse présenter des différences mineures, la **structure de la hiérarchie des fichiers Linux** de base sera très similaire à celle décrite ci-dessous.

### Le Répertoire Racine

- `/` - C'est le répertoire racine, le point de départ de l'ensemble du système de fichiers. Chaque fichier et répertoire de votre système est situé sous ce répertoire.

### Répertoires Système Essentiels

La **hiérarchie des fichiers sous Linux** comprend plusieurs répertoires essentiels au fonctionnement du système.

- `/bin` - Contient les programmes essentiels en ligne de commande (binaires) disponibles pour tous les utilisateurs, tels que `ls`, `cp` et `mv`.
- `/sbin` - Contient les binaires système essentiels, principalement destinés à l'administration système et qui ne peuvent généralement être exécutés que par l'utilisateur root.
- `/etc` - C'est le répertoire de configuration système principal. Il contient les fichiers de configuration pour le système d'exploitation et les applications installées, mais il ne doit contenir aucun binaire exécutable.
- `/lib` - Contient les fichiers de bibliothèques partagées essentiels dont dépendent les binaires système dans `/bin` et `/sbin` pour fonctionner correctement.
- `/boot` - Stocke les fichiers requis pour le processus de démarrage du système, y compris le noyau Linux et les fichiers du programme de démarrage (boot loader).

### Données Utilisateur et Applications

- `/home` - Contient les répertoires personnels pour chaque utilisateur. C'est là que vous stockez vos documents, paramètres d'application et autres fichiers personnels.
- `/root` - Le répertoire personnel de l'utilisateur root, séparé du répertoire `/home` pour garantir que l'utilisateur root puisse se connecter même si `/home` n'est pas disponible.
- `/opt` - Réservé aux logiciels optionnels ou aux progiciels d'applications tiers.
- `/usr` - Ce répertoire contient les logiciels et utilitaires installés par l'utilisateur. Malgré son nom, il ne contient généralement pas les fichiers personnels des utilisateurs. Il possède sa propre structure de sous-répertoires, comme `/usr/bin` pour les binaires utilisateur non essentiels et `/usr/local` pour les logiciels compilés à partir des sources.

### Données Dynamiques et Temporaires

- `/var` - Abréviation de « variable », il stocke les fichiers dont on s'attend à ce que leur taille et leur contenu changent, tels que les journaux système (`/var/log`), les caches et les fichiers de mise en file d'attente (spool).
- `/tmp` - Un espace inscriptible par tous pour stocker des fichiers temporaires. Les fichiers dans ce répertoire sont souvent supprimés lors du redémarrage du système.
- `/run` - Contient des informations sur le système en cours d'exécution depuis le dernier démarrage, telles que les identifiants de processus (PID) et d'autres données d'exécution.

### Périphériques et Points de Montage

- `/dev` - Contient des fichiers de périphériques spéciaux qui représentent des composants matériels comme les disques durs, les terminaux et les périphériques d'entrée.
- `/media` - Un point de montage standard pour les médias amovibles comme les clés USB, les cartes SD et les CD-ROM.
- `/mnt` - Un point de montage générique pour monter temporairement des systèmes de fichiers.

### Informations Système

- `/proc` - Un système de fichiers virtuel qui fournit des informations en temps réel sur les processus en cours d'exécution et les paramètres du noyau.
- `/srv` - Destiné aux données spécifiques au site servies par le système, comme les fichiers pour un serveur web.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du système de fichiers Linux :

1. **[Naviguer dans le Système de Fichiers sous Linux](https://labex.io/fr/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Entraînez-vous à utiliser des commandes shell essentielles comme `pwd`, `cd` et `ls` pour vous déplacer entre les répertoires et explorer le système de fichiers.
2. **[Gérer les Fichiers et Répertoires sous Linux](https://labex.io/fr/labs/comptia-manage-files-and-directories-in-linux-590835)** - Apprenez à créer, supprimer, copier et déplacer des fichiers et des répertoires, et comprenez les liens symboliques et les liens physiques.
3. **[Trouver des Fichiers et des Commandes sous Linux](https://labex.io/fr/labs/comptia-find-files-and-commands-in-linux-590834)** - Maîtrisez les techniques pour localiser des fichiers et des commandes en utilisant `find`, `locate`, `whereis`, `which` et `type`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion du système de fichiers Linux.

## Quiz Question

Quel répertoire est utilisé pour stocker les journaux ? (Veuillez fournir le chemin complet. La réponse est sensible à la casse et doit être en anglais.)

## Quiz Answer

/var
