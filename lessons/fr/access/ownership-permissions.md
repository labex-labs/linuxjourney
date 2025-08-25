---
index: 3
lang: "fr"
title: "Permissions de propriété"
meta_title: "Permissions de propriété - Permissions"
meta_description: "Apprenez à changer la propriété des fichiers sous Linux en utilisant les commandes chown et chgrp. Comprenez les permissions d'utilisateur et de groupe avec ce tutoriel Linux pour débutants."
meta_keywords: "chown, chgrp, propriété de fichier Linux, permissions Linux, commandes Linux, Linux débutant, tutoriel Linux, guide Linux"
---

## Lesson Content

En plus de modifier les permissions sur les fichiers, vous pouvez également modifier la propriété de groupe et d'utilisateur du fichier.

### Modifier la propriété de l'utilisateur

```bash
sudo chown patty myfile
```

Cette commande définira `patty` comme propriétaire de `myfile`.

### Modifier la propriété du groupe

```bash
sudo chgrp whales myfile
```

Cette commande définira `whales` comme groupe de `myfile`.

### Modifier la propriété de l'utilisateur et du groupe en même temps

Si vous ajoutez un deux-points et le nom du groupe après l'utilisateur, vous pouvez définir l'utilisateur et le groupe en même temps.

```bash
sudo chown patty:whales myfile
```

## Exercise

C'est en forgeant qu'on devient forgeron ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la propriété et des permissions des fichiers :

1. **[Groupe d'utilisateurs Linux et permissions de fichiers](https://labex.io/fr/labs/linux-linux-user-group-and-file-permissions-18002)** - Apprenez les concepts essentiels de la gestion des utilisateurs et des groupes Linux, y compris la compréhension des permissions de fichiers et la manipulation de la propriété des fichiers. Ce laboratoire offre une expérience pratique dans la sécurisation d'un environnement Linux multi-utilisateur.
2. **[Ajouter un nouvel utilisateur et un nouveau groupe](https://labex.io/fr/labs/linux-add-new-user-and-group-17987)** - Dans ce défi, vous simulerez l'ajout de nouveaux membres d'équipe à un environnement serveur en créant de nouveaux comptes d'utilisateurs, en configurant des groupes personnalisés et en gérant les appartenances aux groupes. Cela testera vos compétences en administration des utilisateurs et des groupes Linux.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion de la propriété et des permissions des fichiers sous Linux.

## Quiz Question

Quelle commande utilisez-vous pour changer la propriété de l'utilisateur ?

## Quiz Answer

chown
