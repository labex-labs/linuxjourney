---
lang: "fr"
title: "Surveillance Continue"
description: "Apprenez la surveillance continue des systèmes Linux avec sar. Comprenez l'installation, la collecte de données et comment analyser l'utilisation historique des ressources pour la performance. Commencez dès maintenant !"
keywords: "sar, sysstat, surveillance Linux, performance système, surveillance continue, débutant, tutoriel, guide"
---

## Lesson Content

Ces outils de surveillance sont utiles lorsque votre machine rencontre des problèmes, mais qu'en est-il des machines qui ont des problèmes lorsque vous ne regardez pas ? Pour celles-ci, vous devrez utiliser un outil de surveillance continue, quelque chose qui collectera, rapportera et sauvegardera les informations d'activité de votre système. Dans cette leçon, nous allons passer en revue un excellent outil à utiliser : **sar**.

### Installing sar

Sar est un outil utilisé pour effectuer une analyse historique sur votre système. Tout d'abord, assurez-vous de l'avoir installé en installant le package `sysstat` : `sudo apt install sysstat`.

### Setting up data collection

Habituellement, une fois que vous installez `sysstat`, votre système commencera automatiquement à collecter des données. Si ce n'est pas le cas, vous pouvez l'activer en modifiant le champ `ENABLED` dans `/etc/default/sysstat`.

### Using sar

```bash
sudo sar -q
```

Cette commande listera les détails depuis le début de la journée.

```bash
sudo sar -r
```

Ceci listera les détails de l'utilisation de la mémoire depuis le début de la journée.

```bash
sudo sar -P
```

Ceci listera les détails de l'utilisation du CPU.

Pour voir une vue d'un jour différent, vous pouvez aller dans `/var/log/sysstat/saXX` où `XX` est le jour que vous voulez voir.

```bash
sar -q /var/log/sysstat/sa02
```

## Exercise

Installez sar sur votre système et commencez à collecter et analyser l'utilisation des ressources de votre système.

## Quiz Question

Quel est un bon outil à utiliser pour surveiller les ressources système ?

## Quiz Answer

sar
