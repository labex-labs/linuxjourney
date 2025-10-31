---
index: 7
lang: "fr"
title: "Compiler le Code Source"
meta_title: "Compiler le Code Source - Paquets"
meta_description: "Apprenez à compiler à partir du code source sous Linux. Ce guide couvre les étapes essentielles pour construire du code source en utilisant configure, make et la commande checkinstall recommandée pour une gestion propre des paquets."
meta_keywords: "compiler à partir du code source, construire le code source, compiler le code source, make install, checkinstall, compilation Linux, build-essential, script configure, makefile, tutoriel Linux"
---

## Lesson Content

Occasionnellement, vous trouverez peut-être un paquet qui n'est disponible que sous forme de code source. Pour l'utiliser, vous devrez le compiler et l'installer sur votre système. Cette leçon vous guidera à travers le processus courant de compilation à partir du code source.

### Préparation de votre système

Avant de pouvoir compiler quoi que ce soit, vous avez besoin des outils nécessaires. Sur les systèmes basés sur Debian comme Ubuntu, vous pouvez les installer avec une seule commande.

```bash
sudo apt install build-essential
```

Le paquet `build-essential` installe une suite d'outils de développement logiciel, y compris le compilateur GCC et l'utilitaire `make`, qui sont essentiels pour la compilation.

Après avoir installé les outils, extrayez le contenu du paquet de code source, qui est généralement un fichier `.tar.gz`.

```bash
tar -xzvf package.tar.gz
```

Avant de continuer, vérifiez toujours la présence d'un fichier `README` ou `INSTALL` à l'intérieur du répertoire extrait. Ces fichiers contiennent souvent des instructions spécifiques ou des dépendances requises pour ce paquet particulier.

### Le processus de construction standard

Bien que différents développeurs puissent utiliser divers systèmes de construction comme `cmake`, la méthode la plus traditionnelle implique un processus en trois étapes. Comprendre cela est fondamental pour apprendre à construire du code source.

Premièrement, exécutez le script `configure`. Ce script vérifie votre système pour toutes les dépendances et bibliothèques nécessaires dont le logiciel a besoin pour être construit et exécuté correctement.

```bash
./configure
```

Le préfixe `./` indique au shell d'exécuter le script à partir du répertoire courant. Si le script signale des dépendances manquantes, vous devez les installer avant de continuer.

Ensuite, exécutez la commande `make`. Cette commande lit un fichier nommé `Makefile` dans le répertoire, qui contient un ensemble de règles sur la manière de compiler le code source en programmes exécutables.

```bash
make
```

Enfin, pour installer le logiciel sur votre système, vous exécuteriez typiquement :

```bash
sudo make install
```

Cette commande copie les fichiers compilés dans les répertoires système appropriés, rendant le logiciel disponible pour utilisation.

### Une meilleure façon d'installer

Bien que `sudo make install` fonctionne, il présente un inconvénient majeur : il n'enregistre pas le logiciel auprès du gestionnaire de paquets de votre système. Cela rend difficile le suivi, la mise à jour ou la désinstallation propre du paquet ultérieurement.

Avec `checkinstall`, l'approche est bien meilleure. Cet outil exécute le processus d'installation mais, au lieu de copier directement les fichiers, il crée un paquet système natif (comme un fichier `.deb` sur Debian/Ubuntu) et l'installe.

```bash
sudo checkinstall
```

L'utilisation de `checkinstall` intègre le logiciel compilé dans votre système de gestion de paquets. Cela signifie que vous pouvez facilement le supprimer plus tard en utilisant `apt` ou `dpkg`, tout comme n'importe quel autre paquet installé à partir des dépôts officiels. Pour cette raison, vous devriez toujours préférer `checkinstall` à `make install`.

Pour désinstaller un paquet installé avec `make install`, vous devriez revenir au répertoire source et exécuter `sudo make uninstall`, mais ce n'est pas toujours fiable.

## Exercise

La pratique rend parfait ! Voici un laboratoire pratique pour renforcer votre compréhension de la construction de logiciels à partir de la source :

1. **[Construire des logiciels à partir du code source sous Linux](https://labex.io/fr/labs/comptia-build-software-from-source-code-in-linux-590853)** - Entraînez-vous au processus fondamental de construction et d'installation de logiciels à partir de leur code source, y compris l'utilisation de `configure`, `make` et `make install`.

Ce laboratoire vous aidera à appliquer les concepts dans un scénario réel et à gagner en confiance dans la compilation de logiciels.

## Quiz Question

Par quoi devriez-vous TOUJOURS remplacer `make install` ?

## Quiz Answer

checkinstall
