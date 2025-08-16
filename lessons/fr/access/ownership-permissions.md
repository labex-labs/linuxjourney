---
lang: "fr"
title: "Permissions de Propriété"
description: "Apprenez à changer la propriété des fichiers sous Linux en utilisant les commandes chown et chgrp. Comprenez les permissions d'utilisateur et de groupe avec ce tutoriel Linux pour débutants."
keywords: "chown, chgrp, propriété de fichier Linux, permissions Linux, commandes Linux, Linux débutant, tutoriel Linux, guide Linux"
---

## Lesson Content

En plus de modifier les permissions sur les fichiers, vous pouvez également modifier la propriété de groupe et d'utilisateur du fichier.

### Modifier la propriété de l'utilisateur

```bash
sudo chown patty myfile
```

Cette commande définira l'utilisateur `patty` comme propriétaire de `myfile`.

### Modifier la propriété du groupe

```bash
sudo chgrp whales myfile
```

Cette commande définira le groupe `whales` comme propriétaire de `myfile`.

### Modifier la propriété de l'utilisateur et du groupe simultanément

Si vous ajoutez un deux-points et un nom de groupe après l'utilisateur, vous pouvez définir l'utilisateur et le groupe en même temps.

```bash
sudo chown patty:whales myfile
```

## Exercise

Modifiez le groupe et l'utilisateur de certains fichiers de test. Ensuite, examinez les permissions avec `ls -l`.

## Quiz Question

Quelle commande utilisez-vous pour changer la propriété de l'utilisateur ?

## Quiz Answer

chown
