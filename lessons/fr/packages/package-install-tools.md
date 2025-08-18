---
lang: "fr"
title: "rpm et dpkg"
meta_description: "Apprenez à installer, supprimer et lister des paquets en utilisant les commandes rpm et dpkg. Comprenez la gestion directe des paquets pour les fichiers .deb et .rpm. Commencez votre parcours Linux !"
meta_keywords: "rpm, dpkg, gestion de paquets Linux, .deb, .rpm, tutoriel Linux, guide du débutant, installer des paquets"
---

## Lesson Content

Bien que la majeure partie de ce cours porte sur les systèmes de gestion de paquets (les Batmans de la gestion de paquets), nous ne devons pas oublier les Robins. Bien que très utiles et fiables, ils ne sont pas livrés avec cette douce Batmobile et cette ceinture utilitaire.

Tout comme `.exe` est un fichier exécutable unique, il en va de même pour `.deb` et `.rpm`. Vous ne les verriez normalement pas si vous utilisez des dépôts de paquets, mais si vous téléchargez directement des paquets, vous les obtiendrez très probablement dans ces formats populaires. Évidemment, ils sont exclusifs à leurs distributions : `.deb` pour les systèmes basés sur Debian et `.rpm` pour les systèmes basés sur Red Hat.

Pour installer ces paquets directs, vous pouvez utiliser les commandes de gestion de paquets : `rpm` et `dpkg`. Ces outils sont utilisés pour installer des fichiers de paquets ; cependant, ils n'installeront pas les dépendances des paquets. Ainsi, si votre paquet avait 10 dépendances, vous devriez installer ces paquets séparément, puis leurs dépendances, et ainsi de suite. Comme vous pouvez le constater, c'est l'une des raisons qui ont donné naissance aux systèmes de gestion complets dont nous discuterons plus tard.

Gardez à l'esprit qu'il y aura d'innombrables fois où vous devrez installer, interroger ou vérifier un paquet avec l'un de ces outils, alors souvenez-vous de ces commandes.

### Install a package

```bash
Debian: $ dpkg -i some_deb_package.deb
RPM: $ rpm -i some_rpm_package.rpm
```

Le `i` signifie installer. Vous pouvez également utiliser le format plus long de `--install`.

### Remove a package

```bash
Debian: $ dpkg -r some_deb_package.deb
RPM: $ rpm -e some_rpm_package.rpm
```

Debian: `r` pour supprimer
RPM: `e` pour effacer

### List installed packages

```bash
Debian: $ dpkg -l
RPM: $ rpm -qa
```

Debian: `l` pour lister
RPM: `q` pour interroger et `a` pour tout

## Exercise

Trouvez un programme que vous souhaitez installer sur votre système, comme Google Chrome, et installez-le en utilisant l'une de ces commandes.

## Quiz Question

Quel est l'outil de gestion de paquets pour les fichiers `.deb` ?

## Quiz Answer

dpkg
