---
lang: "fr"
title: "Service System V"
meta_description: "Apprenez à gérer les services System V à l'aide d'outils en ligne de commande. Découvrez comment lister, démarrer, arrêter et redémarrer des services avec ce tutoriel Linux convivial pour débutants."
meta_keywords: "services System V, services Linux, commande service, SysV init, tutoriel Linux, Linux pour débutants, gestion des services, guide Linux"
---

## Lesson Content

Il existe de nombreux outils en ligne de commande que vous pouvez utiliser pour gérer les services Sys V.

### List services

```bash
service --status-all
```

### Start a service

```bash
sudo service networking start
```

### Stop a service

```bash
sudo service networking stop
```

### Restart a service

```bash
sudo service networking restart
```

Ces commandes ne sont pas spécifiques aux systèmes d'initialisation Sys V ; vous pouvez également les utiliser pour gérer les services Upstart. Étant donné que Linux essaie de s'éloigner des scripts d'initialisation Sys V plus traditionnels, des mécanismes sont toujours en place pour faciliter cette transition.

## Exercise

Gérez quelques services et modifiez leurs états. Qu'observez-vous ?

## Quiz Question

Quelle est la commande pour arrêter un service nommé `peanut` avec Sys V ?

## Quiz Answer

sudo service peanut stop
