---
index: 1
lang: "fr"
title: "Hiérarchie du système de fichiers"
meta_title: "Hiérarchie du système de fichiers - Le système de fichiers"
meta_description: "Apprenez la norme de la hiérarchie du système de fichiers Linux (FHS) et comprenez les répertoires clés comme /bin, /etc et /var. Explorez la structure des répertoires Linux."
meta_keywords: "Hiérarchie du système de fichiers Linux, FHS, structure des répertoires Linux, commandes Linux, Linux pour débutants, tutoriel Linux, guide Linux"
---

## Lesson Content

À ce stade, vous êtes probablement déjà familiarisé avec la structure des répertoires de votre système ; sinon, vous le serez bientôt. Les systèmes de fichiers peuvent varier dans leur structure, mais pour la plupart, ils doivent se conformer à la norme de la hiérarchie du système de fichiers (Filesystem Hierarchy Standard).

Allez-y et exécutez un `ls -l /` pour voir les répertoires listés sous le répertoire racine. Le vôtre peut être différent du mien, mais les répertoires devraient pour la plupart ressembler à ce qui suit :

- `/` - Le répertoire racine de toute la hiérarchie du système de fichiers ; tout est niché sous ce répertoire.
- `/bin` - Programmes essentiels prêts à l'emploi (binaires) ; inclut les commandes les plus basiques telles que `ls` et `cp`.
- `/boot` - Contient les fichiers du chargeur de démarrage du noyau.
- `/dev` - Fichiers de périphériques.
- `/etc` - Répertoire de configuration système principal ; ne devrait contenir que des fichiers de configuration et aucun binaire.
- `/home` - Répertoires personnels pour les utilisateurs ; contient vos documents, fichiers, paramètres, etc.
- `/lib` - Contient les fichiers de bibliothèque que les binaires peuvent utiliser.
- `/media` - Utilisé comme point de montage pour les médias amovibles comme les clés USB.
- `/mnt` - Systèmes de fichiers temporairement montés.
- `/opt` - Paquets logiciels d'application optionnels.
- `/proc` - Informations sur les processus en cours d'exécution.
- `/root` - Le répertoire personnel de l'utilisateur root.
- `/run` - Informations sur le système en cours d'exécution depuis le dernier démarrage.
- `/sbin` - Contient les binaires système essentiels, généralement ne peuvent être exécutés que par root.
- `/srv` - Données spécifiques au site qui sont servies par le système.
- `/tmp` - Stockage pour les fichiers temporaires.
- `/usr` - Ce nom est malheureusement choisi ; le plus souvent, il ne contient pas de fichiers utilisateur au sens d'un dossier personnel. Il est destiné aux logiciels et utilitaires installés par l'utilisateur ; cependant, cela ne veut pas dire que vous ne pouvez pas y ajouter de répertoires personnels. À l'intérieur de ce répertoire se trouvent des sous-répertoires pour `/usr/bin`, `/usr/local`, etc.
- `/var` - Répertoire variable ; il est utilisé pour la journalisation du système, le suivi des utilisateurs, les caches, etc. En gros, tout ce qui est sujet à des changements constants.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension du système de fichiers Linux :

1. **[Naviguer dans le système de fichiers sous Linux](https://labex.io/fr/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Entraînez-vous à utiliser des commandes shell essentielles comme `pwd`, `cd` et `ls` pour vous déplacer entre les répertoires et explorer le système de fichiers.
2. **[Gérer les fichiers et les répertoires sous Linux](https://labex.io/fr/labs/comptia-manage-files-and-directories-in-linux-590835)** - Apprenez à créer, supprimer, copier et déplacer des fichiers et des répertoires, et comprenez les liens symboliques et physiques.
3. **[Trouver des fichiers et des commandes sous Linux](https://labex.io/fr/labs/comptia-find-files-and-commands-in-linux-590834)** - Maîtrisez les techniques pour localiser des fichiers et des commandes en utilisant `find`, `locate`, `whereis`, `which` et `type`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion du système de fichiers Linux.

## Quiz Question

Quel répertoire est utilisé pour stocker les journaux ?

## Quiz Answer

/var
