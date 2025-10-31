---
index: 2
lang: "fr"
title: "Modification des permissions"
meta_title: "Modification des permissions - Permissions"
meta_description: "Apprenez à modifier les permissions sous Linux avec la commande chmod. Ce guide couvre les méthodes symboliques et numériques pour vous aider à gérer l'accès aux fichiers et aux répertoires en toute sécurité. Maîtrisez le processus de changement de permission Linux pour une meilleure administration système."
meta_keywords: "changer permission linux, modifier permission linux, comment changer les permissions sous linux, comment changer les permissions de fichiers linux, chmod, permissions de fichiers, sécurité linux, permissions symboliques, permissions numériques"
---

## Lesson Content

Lorsque vous devez modifier les droits d'accès aux fichiers ou aux répertoires, l'outil principal que vous utiliserez est la commande `chmod` (change mode). Comprendre **comment changer les permissions sous Linux** est une compétence fondamentale pour tout utilisateur. La commande `chmod` offre deux méthodes principales pour cette tâche : le mode symbolique et le mode numérique.

### Utilisation du Mode Symbolique

Le mode symbolique est souvent considéré comme plus lisible car il utilise des lettres pour représenter les utilisateurs et les permissions. Vous spécifiez d'abord quel ensemble de permissions vous souhaitez modifier (utilisateur, groupe ou autres), puis vous utilisez un `+` pour ajouter une permission ou un `-` pour la supprimer.

- `u` (user/propriétaire)
- `g` (group)
- `o` (others/autres)
- `a` (all/tout : utilisateur, groupe et autres)

Voyons **comment changer les permissions de fichiers linux** avec quelques exemples.

Pour ajouter la permission d'exécution pour l'utilisateur sur un fichier, vous utiliseriez :

```bash
chmod u+x monfichier
```

Cette commande ajoute (`+`) la permission d'exécution (`x`) pour l'utilisateur (`u`) sur `monfichier`.

Pour supprimer une permission, vous utilisez l'opérateur `-`. Par exemple, pour supprimer la permission d'écriture pour le groupe :

```bash
chmod g-w monfichier
```

Vous pouvez également modifier plusieurs permissions à la fois. La commande suivante ajoute la permission d'écriture pour l'utilisateur et le groupe :

```bash
chmod ug+w monfichier
```

### Utilisation du Mode Numérique (Octal)

Une autre façon puissante de **changer les permissions linux** est d'utiliser le mode numérique, ou octal. Cette méthode vous permet de définir toutes les permissions pour l'utilisateur, le groupe et les autres simultanément avec un nombre à trois chiffres.

Les permissions sont représentées par les valeurs suivantes :

- `4` : lecture (r)
- `2` : écriture (w)
- `1` : exécution (x)

Pour définir un ensemble de permissions, vous additionnez les nombres. Par exemple, pour accorder les permissions de lecture, d'écriture et d'exécution, vous utiliseriez `4 + 2 + 1 = 7`.

Regardons un exemple courant :

```bash
chmod 755 monfichier
```

Comment fonctionne cette commande de **changement de permission linux** ? Décomposons le nombre `755` :

- **7 (Utilisateur) :** `4 + 2 + 1` -> L'utilisateur obtient les permissions de lecture, d'écriture et d'exécution (`rwx`).
- **5 (Groupe) :** `4 + 0 + 1` -> Le groupe obtient les permissions de lecture et d'exécution (`r-x`).
- **5 (Autres) :** `4 + 0 + 1` -> Tous les autres utilisateurs obtiennent les permissions de lecture et d'exécution (`r-x`).

### Considérations de Sécurité

Bien que `chmod` soit essentiel, il est crucial de l'utiliser avec prudence. Modifier les permissions sans comprendre les implications peut exposer des fichiers sensibles à des modifications ou des consultations non autorisées. Par exemple, définir récursivement les permissions `777` (`chmod -R 777 /un/repertoire`) est une pratique courante mais dangereuse qui donne à tout le monde un accès complet en lecture, écriture et exécution. Appliquez toujours le principe du moindre privilège, en n'accordant que les permissions strictement nécessaires.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des permissions de fichiers Linux :

1.  **[Groupes d'Utilisateurs Linux et Permissions de Fichiers](https://labex.io/fr/labs/linux-linux-user-group-and-file-permissions-18002)** - Apprenez les concepts essentiels de gestion des utilisateurs et des groupes sous Linux, y compris la compréhension des permissions de fichiers et la manipulation de la propriété des fichiers. Ce laboratoire offre une expérience pratique pour sécuriser un environnement Linux multi-utilisateur.
2.  **[Ajouter un Nouvel Utilisateur et un Nouveau Groupe](https://labex.io/fr/labs/linux-add-new-user-and-group-17987)** - Dans ce défi, vous simulerez l'ajout de nouveaux membres d'équipe à un environnement serveur, en créant de nouveaux comptes utilisateurs, en configurant des groupes personnalisés et en gérant les appartenances aux groupes, ce qui implique souvent de définir les permissions appropriées.

Ces laboratoires vous aideront à appliquer les concepts de permissions utilisateur, groupe et autres dans des scénarios réels et à renforcer votre confiance dans la gestion des accès sous Linux.

## Quiz Question

Quel nombre représente la permission de lecture lorsque vous utilisez le format numérique ?

## Quiz Answer

4
