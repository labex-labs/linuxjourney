---
lang: "fr"
title: "Installation du noyau"
meta_title: "Installation du noyau - Kernel"
meta_description: "Apprenez à installer et à gérer les noyaux Linux. Découvrez les versions de noyaux, utilisez `uname -r` et les commandes apt. Commencez votre parcours avec le noyau Linux !"
meta_keywords: "noyau Linux, installer le noyau, uname -r, apt dist-upgrade, gestion du noyau, tutoriel Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

Maintenant que nous avons réglé toutes ces choses ennuyeuses, parlons de l'installation et de la modification des noyaux. Vous pouvez installer plusieurs noyaux sur votre système ; vous vous souvenez de notre leçon sur le processus de démarrage ? Dans notre menu GRUB, nous pouvons choisir le noyau sur lequel démarrer.

Pour voir la version du noyau que vous avez sur votre système, utilisez la commande suivante :

```bash
$ uname -r
3.19.0-43-generic
```

La commande `uname` affiche les informations système ; l'option `-r` affichera la version de la publication du noyau.

Vous pouvez installer le noyau Linux de différentes manières : vous pouvez télécharger le paquet source et compiler à partir du source, ou vous pouvez l'installer à l'aide d'outils de gestion de paquets.

```bash
sudo apt install linux-generic-lts-vivid
```

Et ensuite, il suffit de redémarrer sur le noyau que vous avez installé. Simple, n'est-ce pas ? En quelque sorte. Vous devrez également installer d'autres paquets Linux tels que `linux-headers`, `linux-image-generic`, etc. Vous pouvez également spécifier le numéro de version, de sorte que la commande ci-dessus peut ressembler à : **`sudo apt install 3.19.0-43-generic`**

Alternativement, si vous voulez juste la version mise à jour du noyau, utilisez simplement `dist-upgrade` ; il effectue des mises à niveau de tous les paquets sur votre système :

```bash
sudo apt dist-upgrade
```

Il existe de nombreuses versions différentes de noyaux. Certaines sont utilisées comme LTS (Long Term Support), d'autres sont les plus récentes et les meilleures. La compatibilité peut être très différente entre les versions de noyaux, vous voudrez donc peut-être essayer différents noyaux.

## Exercise

1. Find out what kernel version you have.
2. Research the different versions of kernels available.

## Quiz Question

Comment voyez-vous la version du noyau de votre système ?

## Quiz Answer

uname -r
