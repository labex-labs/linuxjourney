---
lang: "fr"
title: "NFS"
meta_title: "NFS - Partage Réseau"
meta_description: "Apprenez la configuration du client NFS et le montage automatique dans Linux. Comprenez comment se connecter aux partages de fichiers réseau et utiliser le montage automatique pour un accès transparent."
meta_keywords: "client NFS, automount, Network File System, réseau Linux, commande mount, tutoriel Linux, débutant"
---

## Lesson Content

Le partage de fichiers réseau le plus standard pour Linux est NFS (Network File System). NFS permet à un serveur de partager des répertoires et des fichiers avec un ou plusieurs clients sur le réseau.

Nous n'entrerons pas dans les détails de la création d'un serveur NFS, car cela peut devenir complexe ; cependant, nous discuterons de la configuration des clients NFS.

### Configuration du client NFS

```bash
sudo service nfsclient start
sudo mount server:/directory /mount_directory
```

### Montage automatique (Automounting)

Supposons que vous utilisiez le serveur NFS assez souvent et que vous souhaitiez le maintenir monté en permanence. Normalement, vous pourriez penser à modifier le fichier `/etc/fstab`, mais il se peut que vous n'obteniez pas toujours une connexion au serveur, ce qui peut causer des problèmes au démarrage. Au lieu de cela, ce que vous voulez faire est de configurer le montage automatique (automounting) afin de pouvoir vous connecter au serveur NFS lorsque vous en avez besoin. Cela se fait avec l'outil **automount** ou, dans les versions récentes de Linux, **amd**. Lorsqu'un fichier est accédé dans un répertoire spécifié, automount recherchera le serveur distant et le montera automatiquement.

## Exercise

Lisez la page de manuel de NFS pour en savoir plus.

## Quiz Question

Quel outil est utilisé pour gérer automatiquement les points de montage ?

## Quiz Answer

automount
