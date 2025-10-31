---
index: 4
lang: "fr"
title: "NFS"
meta_title: "NFS - Partage Réseau"
meta_description: "Découvrez comment utiliser le système de fichiers réseau (NFS) sous Linux. Ce tutoriel couvre la configuration d'un client NFS, l'utilisation de la commande mount et la configuration d'automount pour un accès transparent aux partages réseau."
meta_keywords: "NFS, client NFS, automount, système de fichiers réseau, réseau Linux, commande mount, tutoriel Linux, débutant"
---

## Lesson Content

Le protocole le plus standard pour le partage de fichiers en réseau sous Linux est NFS, qui signifie **Network File System** (Système de Fichiers Réseau). NFS permet à un serveur de partager ses répertoires et fichiers avec une ou plusieurs machines clientes sur un réseau, les faisant apparaître comme s'ils étaient des ressources locales.

Cette leçon se concentrera sur la configuration d'un **client NFS**, car la configuration d'un serveur NFS peut être un processus plus complexe.

### Montage d'un Partage NFS

Pour se connecter à un partage NFS, vous devez d'abord vous assurer que le service client NFS est en cours d'exécution. Ensuite, vous pouvez utiliser la commande `mount` pour attacher le répertoire distant à un point de montage local sur votre système.

```bash
sudo service nfsclient start
sudo mount serveur:/repertoire /point_de_montage
```

Dans cet exemple, `serveur:/repertoire` est le partage distant auquel vous souhaitez accéder, et `/point_de_montage` est le répertoire local où le partage sera monté.

### Utilisation d'Automount pour NFS

Si vous accédez fréquemment à un partage NFS, vous pourriez envisager de rendre le montage permanent. Bien que l'ajout d'une entrée dans le fichier `/etc/fstab` soit une méthode courante pour les disques locaux, cela peut entraîner des retards de démarrage importants, voire des échecs si la connexion réseau ou le serveur NFS n'est pas disponible au démarrage.

Aucune solution n'est meilleure pour les partages réseau que **automount**. Ce service, géré par l'outil `automount` ou son implémentation moderne `amd`, monte dynamiquement un système de fichiers à la demande. Lorsqu'un fichier ou un répertoire dans un chemin spécifié est accédé, automount se connecte automatiquement au serveur distant et monte le partage. Cela garantit un accès transparent lorsque nécessaire sans impacter le processus de démarrage du système.

## Exercise

Bien qu'il n'y ait pas de laboratoires spécifiques pour ce sujet, nous vous recommandons d'explorer le [Parcours d'Apprentissage Linux](https://labex.io/fr/learn/linux) complet pour pratiquer les compétences et concepts Linux connexes.

## Quiz Question

Quel outil est utilisé pour gérer les points de montage automatiquement ? Veuillez répondre en anglais, et notez que la réponse est sensible à la casse.

## Quiz Answer

automount
