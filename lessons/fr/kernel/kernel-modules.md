---
index: 6
lang: "fr"
title: "Modules du noyau"
meta_title: "Modules du noyau - Kernel"
meta_description: "Découvrez les modules du noyau Linux : comment les charger, les décharger et les gérer. Comprenez les commandes `modprobe` et `lsmod` pour étendre les fonctionnalités du noyau. Commencez votre parcours Linux !"
meta_keywords: "modules du noyau Linux, modprobe, lsmod, gestion du noyau, tutoriel Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

Disons que j'ai une super voiture ; j'y investis beaucoup de temps et d'argent. J'ajoute un aileron, un attelage, un porte-vélos et d'autres choses aléatoires. Ces composants ne modifient pas la fonctionnalité principale de la voiture, et je peux les retirer et les ajouter très facilement. Le noyau utilise le même concept avec les modules du noyau.

Le noyau en lui-même est un logiciel monolithique. Lorsque nous voulons ajouter la prise en charge d'un nouveau type de clavier, nous n'écrivons pas ce code directement dans le code du noyau. Tout comme nous ne souderions pas un porte-vélos à notre voiture (enfin, certaines personnes le feraient peut-être). Les modules du noyau sont des morceaux de code qui peuvent être chargés et déchargés dans le noyau à la demande. Ils nous permettent d'étendre les fonctionnalités du noyau sans réellement ajouter au code du noyau principal. Nous pouvons également ajouter des modules sans avoir à redémarrer le système (dans la plupart des cas).

### View a list of currently loaded modules

```bash
lsmod
```

### Load a module

```bash
sudo modprobe bluetooth
```

`modprobe` charge le module depuis `/lib/modules/(kernel version)/kernel/drivers`. Les modules du noyau peuvent également avoir des dépendances ; `modprobe` charge les dépendances de notre module si elles ne sont pas déjà chargées.

### Remove a module

```bash
sudo modprobe -r bluetooth
```

### Load on bootup

Vous pouvez également charger des modules au démarrage du système, au lieu de les charger temporairement avec `modprobe` (qui seront déchargés au redémarrage). Il suffit de modifier le répertoire `/etc/modprobe.d` et d'y ajouter un fichier de configuration comme suit :

```plaintext
pete@icebox:~$ /etc/modprobe.d/peanutbutter.conf

options peanut_butter type=almond
```

Un exemple un peu extravagant, mais si vous aviez un module nommé `peanut_butter` et que vous vouliez ajouter un paramètre de noyau pour `type=almond`, vous pouvez le faire charger au démarrage en utilisant ce fichier de configuration. Notez également que les modules du noyau ont leurs propres paramètres de noyau, vous voudrez donc lire spécifiquement sur le module pour en savoir plus.

### Do not load on bootup

Vous pouvez également vous assurer qu'un module ne se charge pas au démarrage en ajoutant un fichier de configuration comme suit :

```plaintext
pete@icebox:~$ /etc/modprobe.d/peanutbutter.conf

blacklist peanut_butter
```

## Exercise

Déchargez votre module Bluetooth avec `modprobe` et voyez ce qui se passe. Comment allez-vous résoudre ce problème ?

## Quiz Question

Quelle commande est utilisée pour décharger un module ?

## Quiz Answer

modprobe -r
