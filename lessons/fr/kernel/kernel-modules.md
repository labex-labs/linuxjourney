---
index: 6
lang: "fr"
title: "Modules Noyau"
meta_title: "Modules Noyau - Noyau"
meta_description: "Découvrez ce que sont les modules noyau sous Linux et comment ils étendent les fonctionnalités du noyau. Cette leçon couvre l'utilisation de lsmod et modprobe pour lister, charger et décharger des modules à la demande."
meta_keywords: "modules noyau, modules noyau Linux, modprobe, lsmod, gestion noyau, tutoriel Linux, Linux débutant, guide Linux"
---

## Lesson Content

Considérez le noyau Linux comme le moteur central d'une voiture. Vous pouvez ajouter des accessoires comme une galerie de toit ou un nouveau système audio sans modifier le moteur lui-même. Ces accessoires peuvent être ajoutés ou retirés selon les besoins. Le noyau Linux utilise un concept similaire avec les modules du noyau.

### Que sont les modules du noyau

Alors, **que sont les modules du noyau** ? Ce sont des morceaux de code qui peuvent être chargés dans le noyau et en être déchargés à la demande. Ils étendent la fonctionnalité du noyau sans nécessiter de recompiler le noyau principal ou de redémarrer le système. Cette approche modulaire permet d'ajouter dynamiquement la prise en charge de nouveau matériel (comme une nouvelle carte Wi-Fi) ou de nouvelles fonctionnalités logicielles (comme un nouveau système de fichiers). Cela maintient le noyau principal léger tout en permettant une flexibilité immense.

### Lister les modules chargés

Pour voir la liste de tous les modules du noyau actuellement chargés en mémoire, vous pouvez utiliser la commande `lsmod`. Cela vous donne un instantané des modules actifs et de leurs dépendances.

```bash
lsmod
```

### Charger un module du noyau

Pour charger un module du noyau, nous utilisons la commande `modprobe`. Par exemple, pour charger le module `bluetooth`, vous exécuteriez :

```bash
sudo modprobe bluetooth
```

La commande `modprobe` est intelligente ; elle recherche le module dans le répertoire standard (`/lib/modules/$(uname -r)/`) et charge également tous les autres modules dont le module cible dépend.

### Décharger un module du noyau

Si un module n'est plus nécessaire, vous pouvez le décharger pour libérer des ressources système. Utilisez l'option `-r` avec `modprobe` pour supprimer un module :

```bash
sudo modprobe -r bluetooth
```

### Gérer les modules au démarrage

Les modules chargés avec `modprobe` sont temporaires et disparaîtront après un redémarrage. Pour rendre les configurations des modules permanentes, vous pouvez créer des fichiers de configuration dans le répertoire `/etc/modprobe.d/`.

Pour charger automatiquement un module au démarrage avec des options spécifiques, créez un fichier `.conf`. Par exemple, si vous aviez un module hypothétique nommé `peanut_butter` et que vous vouliez définir son paramètre `type` sur `almond`, votre fichier ressemblerait à ceci :

```plaintext
# /etc/modprobe.d/peanutbutter.conf

options peanut_butter type=almond
```

Inversement, pour empêcher un module de se charger au démarrage (un processus appelé "blacklisting" ou mise sur liste noire), vous pouvez utiliser le mot-clé `blacklist` dans un fichier de configuration :

```plaintext
# /etc/modprobe.d/peanutbutter.conf

blacklist peanut_butter
```

Ces fichiers de configuration permettent un contrôle précis sur les modules disponibles lorsque votre système démarre.

## Exercise

La pratique rend parfait ! Voici un laboratoire pratique pour renforcer votre compréhension des modules du noyau Linux :

1. **[Gérer les modules du noyau sous Linux](https://labex.io/fr/labs/comptia-manage-kernel-modules-in-linux-590865)** - Entraînez-vous à lister, inspecter, charger et décharger les modules du noyau, et à les configurer pour qu'ils se chargent automatiquement au démarrage. Ce laboratoire vous aidera à appliquer les concepts dans un scénario réel et à gagner en confiance avec la gestion des modules du noyau.

## Quiz Question

Quelle commande est utilisée pour décharger un module ?

## Quiz Answer

modprobe -r
