---
lang: "fr"
title: "Dépôts de Paquets"
meta_description: "Découvrez les dépôts de paquets Linux et comment ils gèrent les logiciels. Apprenez à trouver et à ajouter des sources de paquets comme /etc/apt/sources.list pour une installation facile."
meta_keywords: "dépôts de paquets Linux, liste des sources apt, /etc/apt/sources.list, paquets Linux, Linux pour débutants, tutoriel Linux, gestion des paquets"
---

## Lesson Content

Comment les paquets téléchargés sur Internet se retrouvent-ils sur nos ordinateurs ? Allez-vous sur la page de téléchargement de chaque paquet que vous voulez et cliquez-vous sur télécharger et installer ? Bien que cela soit possible, il existe une meilleure solution : les dépôts de paquets. Les dépôts sont des emplacements de stockage centraux pour les paquets. Il existe des tonnes de dépôts contenant de nombreux paquets, et le meilleur de tout, ils se trouvent tous sur Internet — pas de disques d'installation inutiles. Votre machine ne sait pas où chercher ces dépôts à moins que vous ne lui indiquiez explicitement où chercher.

Par exemple, disons que je veux le logiciel WackyWidgets sur ma machine. WackyWidgets gère ses propres dépôts pour ses paquets de widgets. Dans ce dépôt se trouvent 10 paquets, tels que le paquet CoolWidget, le paquet SuperWidget, etc. WackyWidgets héberge ce dépôt à un lien source appelé : <http://download.widgets/linux/deb/>

Maintenant, au lieu d'aller sur leur site web pour télécharger le paquet directement, vous pouvez dire à votre machine de trouver le logiciel WackyWidgets à partir du lien source.

Votre distribution est déjà livrée avec des sources pré-approuvées pour obtenir des paquets, et c'est ainsi qu'elle installe tous les paquets de base que vous voyez sur votre système. Sur un système Debian, ce fichier de sources est le fichier `/etc/apt/sources.list`. Votre machine saura y chercher et vérifier tous les dépôts sources que vous avez ajoutés.

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Où se trouve le fichier des sources dans un système Debian ?

## Quiz Answer

/etc/apt/sources.list
