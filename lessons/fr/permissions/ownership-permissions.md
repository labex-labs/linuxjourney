---
index: 3
lang: "fr"
title: "Permissions de Propriété"
meta_title: "Permissions de Propriété - Permissions"
meta_description: "Maîtrisez la propriété des fichiers Linux en apprenant à utiliser les commandes Linux chown et chgrp. Ce tutoriel Linux explique comment modifier la propriété utilisateur et groupe des fichiers, une compétence clé pour gérer les permissions Linux."
meta_keywords: "chown, chgrp, propriété fichiers linux, changer propriétaire fichier, changer groupe fichier, permissions linux, commandes linux, tutoriel linux, guide linux, propriété utilisateur, propriété groupe"
---

## Lesson Content

Dans un système Linux, chaque fichier et répertoire se voit attribuer un propriétaire et un groupe. La gestion de la **propriété des fichiers Linux** est une tâche fondamentale pour contrôler l'accès et les permissions. Vous pouvez modifier à la fois la propriété utilisateur et la propriété de groupe d'un fichier à l'aide de **commandes Linux** spécifiques.

### Changer la propriété utilisateur

Pour transférer la propriété d'un fichier à un autre utilisateur, vous utilisez la commande `chown` (change owner). Ceci est utile lorsque les responsabilités d'un utilisateur changent ou lorsque vous devez attribuer le contrôle du fichier à quelqu'un d'autre. Vous avez généralement besoin des privilèges de superutilisateur (`sudo`) pour changer le propriétaire d'un fichier qui ne vous appartient pas.

```bash
sudo chown patty myfile
```

Cette commande change le propriétaire utilisateur de `myfile` pour l'utilisateur `patty`.

### Changer la propriété de groupe

De même, vous pouvez changer le groupe associé à un fichier en utilisant la commande `chgrp` (change group). Cela permet à tous les membres du nouveau groupe d'avoir accès en fonction des **permissions Linux** du groupe.

```bash
sudo chgrp whales myfile
```

Cette commande définit la propriété de groupe de `myfile` sur le groupe `whales`.

### Changer l'utilisateur et le groupe

Pour plus d'efficacité, la commande `chown` vous permet de modifier à la fois la propriété utilisateur et la propriété de groupe en une seule étape. En séparant le nom d'utilisateur et le nom de groupe par deux-points, vous pouvez mettre à jour les deux attributs simultanément.

```bash
sudo chown patty:whales myfile
```

Cette commande unique attribue la propriété utilisateur à `patty` et la propriété de groupe à `whales` pour le fichier `myfile`. C'est la méthode la plus courante pour gérer la **propriété des fichiers Linux**.

## Exercise

Pour consolider votre compréhension de la **propriété des fichiers Linux**, nous vous recommandons de vous entraîner avec ces laboratoires pratiques. Ils offrent des scénarios réels pour appliquer les commandes `chown` et `chgrp`.

1. **[Groupe d'utilisateurs et permissions de fichiers Linux](https://labex.io/fr/labs/linux-linux-user-group-and-file-permissions-18002)** - Apprenez les concepts essentiels de gestion des utilisateurs et des groupes sous Linux, y compris la compréhension des permissions de fichiers et la manipulation de la propriété des fichiers. Ce laboratoire offre une expérience pratique pour sécuriser un environnement Linux multi-utilisateur.
2. **[Ajouter un nouvel utilisateur et un nouveau groupe](https://labex.io/fr/labs/linux-add-new-user-and-group-17987)** - Dans ce défi, vous simulerez l'ajout de nouveaux membres d'équipe à un environnement serveur en créant de nouveaux comptes utilisateurs, en configurant des groupes personnalisés et en gérant les appartenances aux groupes. Cela testera vos compétences en administration des utilisateurs et des groupes sous Linux.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion de la propriété des fichiers et des permissions sous Linux.

## Quiz Question

Quelle commande est utilisée pour changer la propriété utilisateur d'un fichier ? Veuillez fournir uniquement le nom de la commande en lettres minuscules anglaises.

## Quiz Answer

chown
