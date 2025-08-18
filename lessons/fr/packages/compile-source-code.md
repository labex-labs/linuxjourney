---
index: 7
lang: "fr"
title: "Compiler le code source"
meta_title: "Compiler le code source - Packages"
meta_description: "Apprenez à compiler le code source sous Linux en utilisant make, configure et checkinstall. Comprenez le processus de construction pour les utilisateurs débutants et intermédiaires."
meta_keywords: "compiler le code source, make install, checkinstall, compilation Linux, build-essential, tutoriel Linux, guide du débutant"
---

## Lesson Content

Souvent, vous rencontrerez un paquet obscur qui n'existe que sous forme de code source pur. Vous devrez utiliser quelques commandes pour que ce paquet de code source soit compilé et installé sur votre système.

Tout d'abord, vous devrez disposer d'un logiciel pour installer les outils qui vous permettront de compiler le code source.

```bash
sudo apt install build-essential
```

Une fois cela fait, extrayez le contenu du fichier du paquet, très probablement un fichier `.tar.gz`.

```bash
tar -xzvf package.tar.gz
```

Avant de faire quoi que ce soit, jetez un œil au fichier `README` ou `INSTALL` à l'intérieur du paquet. Parfois, il y aura des instructions d'installation spécifiques.

Selon la méthode de compilation utilisée par le développeur, vous devrez utiliser différentes commandes, telles que `cmake` ou autre chose.

Cependant, le plus souvent, vous verrez une compilation `make` de base, nous allons donc en discuter :

À l'intérieur du contenu du paquet se trouvera un script `configure`. Ce script vérifie les dépendances sur votre système, et s'il vous manque quelque chose, vous verrez une erreur et vous devrez corriger ces dépendances.

```bash
./configure
```

Le `./` vous permet d'exécuter un script dans le répertoire courant.

```bash
make
```

À l'intérieur du contenu du paquet, il y a un fichier appelé `Makefile` qui contient les règles pour construire le logiciel. Lorsque vous exécutez la commande `make`, elle examine ce fichier pour construire le logiciel.

```bash
sudo make install
```

Cette commande installe réellement le paquet ; elle copiera les fichiers corrects aux bons emplacements sur votre ordinateur.

Si vous souhaitez désinstaller le paquet, utilisez :

```bash
sudo make uninstall
```

Soyez prudent lorsque vous utilisez `make install` ; vous ne réalisez peut-être pas tout ce qui se passe en arrière-plan. Si vous décidez de supprimer ce paquet, vous risquez de ne pas tout supprimer parce que vous n'avez pas réalisé ce qui a été ajouté à votre système. Au lieu de cela, oubliez tout ce que je viens de vous expliquer sur `make install` et utilisez la commande **checkinstall**. Cette commande créera un fichier `.deb` pour vous que vous pourrez facilement installer et désinstaller.

```bash
sudo checkinstall
```

Cette commande va essentiellement « make install » et construire un paquet `.deb` et l'installer. Cela facilite la suppression du paquet par la suite.

## Exercise

Trouvez un programme de code source (à partir d'un site de confiance) et installez-le à partir de la source.

## Quiz Question

Que devriez-vous TOUJOURS utiliser à la place de `make install` ?

## Quiz Answer

checkinstall
