---
index: 5
lang: "fr"
title: "rpm et dpkg"
meta_title: "rpm et dpkg - Paquets"
meta_description: "Apprenez à installer, supprimer et lister des paquets en utilisant les commandes rpm et dpkg. Comprenez la gestion directe des paquets pour les fichiers .deb et .rpm. Commencez votre parcours Linux !"
meta_keywords: "rpm, dpkg, gestion de paquets Linux, .deb, .rpm, tutoriel Linux, guide du débutant, installer des paquets"
---

## Lesson Content

Bien que la majeure partie de ce cours porte sur les systèmes de gestion de paquets (les Batmans de la gestion de paquets), nous ne devons pas oublier les Robins. Bien que très utiles et fiables, ils ne sont pas livrés avec cette douce Batmobile et cette ceinture utilitaire.

Tout comme `.exe` est un fichier exécutable unique, `.deb` et `.rpm` le sont aussi. Vous ne les verriez normalement pas si vous utilisez des dépôts de paquets, mais si vous téléchargez directement des paquets, vous les obtiendrez très probablement dans ces formats populaires. Évidemment, ils sont exclusifs à leurs distributions : `.deb` pour les distributions basées sur Debian et `.rpm` pour celles basées sur Red Hat.

Pour installer ces paquets directs, vous pouvez utiliser les commandes de gestion de paquets : `rpm` et `dpkg`. Ces outils sont utilisés pour installer des fichiers de paquets ; cependant, ils n'installeront pas les dépendances du paquet. Ainsi, si votre paquet avait 10 dépendances, vous devriez installer ces paquets séparément, puis leurs dépendances, et ainsi de suite. Comme vous pouvez le constater, c'est l'une des raisons qui ont donné naissance aux systèmes de gestion complets dont nous discuterons plus tard.

Gardez à l'esprit qu'il y aura d'innombrables fois où vous devrez installer, interroger ou vérifier un paquet avec l'un de ces outils, alors souvenez-vous de ces commandes.

### Installer un paquet

```bash
Debian: $ dpkg -i some_deb_package.deb
RPM: $ rpm -i some_rpm_package.rpm
```

Le `i` signifie installer. Vous pouvez également utiliser le format plus long de `--install`.

### Supprimer un paquet

```bash
Debian: $ dpkg -r some_deb_package.deb
RPM: $ rpm -e some_rpm_package.rpm
```

Debian : `r` pour remove (supprimer)
RPM : `e` pour erase (effacer)

### Lister les paquets installés

```bash
Debian: $ dpkg -l
RPM: $ rpm -qa
```

Debian : `l` pour list (lister)
RPM : `q` pour query (interroger) et `a` pour all (tout)

## Exercise

La pratique rend parfait ! Voici un laboratoire pratique pour renforcer votre compréhension de la gestion directe des paquets :

1. **[Gérer les paquets avec RPM sous Linux](https://labex.io/fr/labs/rhel-managing-packages-with-rpm-in-linux-590868)** - Acquérez une expérience pratique en interrogeant les informations de paquet, en vérifiant l'intégrité, en listant les dépendances, en simulant la suppression et en inspectant le contenu des paquets RPM avec `rpm` et les outils associés.

Ce laboratoire vous aidera à appliquer les concepts de gestion des fichiers de paquets individuels dans un scénario réel et à renforcer votre confiance avec ces outils Linux essentiels.

## Quiz Question

Quel est l'outil de gestion de paquets pour les fichiers `.deb` ?

## Quiz Answer

dpkg
