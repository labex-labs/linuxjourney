---
index: 4
lang: "fr"
title: "Installation du noyau"
meta_title: "Installation du noyau - Noyau"
meta_description: "Apprenez à installer et gérer les noyaux Linux. Découvrez les versions de noyau, utilisez `uname -r` et les commandes apt. Commencez votre parcours avec le noyau Linux !"
meta_keywords: "noyau Linux, installer le noyau, uname -r, apt dist-upgrade, gestion du noyau, tutoriel Linux, Linux débutant, guide Linux"
---

## Lesson Content

Bien, maintenant que nous avons réglé toutes ces choses ennuyeuses, parlons de l'installation et de la modification des noyaux. Vous pouvez installer plusieurs noyaux sur votre système ; vous vous souvenez de notre leçon sur le processus de démarrage ? Dans notre menu GRUB, nous pouvons choisir le noyau sur lequel démarrer.

Pour voir la version du noyau que vous avez sur votre système, utilisez la commande suivante :

```bash
$ uname -r
3.19.0-43-generic
```

La commande `uname` affiche les informations système ; l'option `-r` affichera la version de la publication du noyau.

Vous pouvez installer le noyau Linux de différentes manières : vous pouvez télécharger le paquet source et compiler à partir des sources, ou vous pouvez l'installer à l'aide d'outils de gestion de paquets.

```bash
sudo apt install linux-generic-lts-vivid
```

Et ensuite, il suffit de redémarrer sur le noyau que vous avez installé. Simple, n'est-ce pas ? En quelque sorte. Vous devrez également installer d'autres paquets Linux tels que `linux-headers`, `linux-image-generic`, etc. Vous pouvez également spécifier le numéro de version, de sorte que la commande ci-dessus peut ressembler à : **`sudo apt install 3.19.0-43-generic`**

Alternativement, si vous voulez juste la version mise à jour du noyau, utilisez simplement `dist-upgrade` ; il effectue des mises à niveau de tous les paquets sur votre système :

```bash
sudo apt dist-upgrade
```

Il existe de nombreuses versions différentes du noyau. Certaines sont utilisées comme LTS (Long Term Support), d'autres sont les plus récentes et les meilleures. La compatibilité peut être très différente entre les versions du noyau, vous voudrez donc peut-être essayer différents noyaux.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion du noyau Linux et des tâches d'administration système associées :

1. **[Personnaliser le menu de démarrage GRUB2 sous Linux](https://labex.io/fr/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Entraînez-vous à modifier le menu de démarrage GRUB2, ce qui est essentiel pour gérer plusieurs versions de noyau et choisir celle sur laquelle démarrer.
2. **[Gérer les modules du noyau sous Linux](https://labex.io/fr/labs/comptia-manage-kernel-modules-in-linux-590865)** - Apprenez à lister, inspecter, charger et décharger les modules du noyau, un aspect fondamental de la gestion du noyau et de la compréhension de la façon dont le matériel interagit avec votre système.
3. **[Installation de logiciels sous Linux](https://labex.io/fr/labs/linux-software-installation-on-linux-18005)** - Acquérez une expérience pratique avec diverses méthodes d'installation et de gestion de logiciels, y compris l'utilisation de gestionnaires de paquets, ce qui est un moyen courant d'installer et de mettre à jour les noyaux.

Ces laboratoires vous aideront à appliquer les concepts de gestion du noyau, de processus de démarrage et de gestion de paquets dans des scénarios réels, renforçant ainsi votre confiance en matière d'administration système.

## Quiz Question

Comment voyez-vous la version du noyau de votre système ?

## Quiz Answer

uname -r
