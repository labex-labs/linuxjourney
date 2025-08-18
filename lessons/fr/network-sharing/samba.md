---
lang: "fr"
title: "Samba"
meta_description: "Apprenez à configurer des partages de fichiers Samba sur Linux pour Windows et macOS. Ce guide pour débutants couvre l'installation, la configuration et l'accès aux partages. Lancez-vous !"
meta_keywords: "Samba, partage de fichiers Linux, smb.conf, CIFS, smbclient, tutoriel Linux, guide du débutant"
---

## Lesson Content

Au début de l'informatique, il est devenu nécessaire pour les machines Windows de partager des fichiers avec les machines Linux ; ainsi, le protocole Server Message Block (SMB) est né. SMB était utilisé pour le partage de fichiers entre les systèmes d'exploitation Windows (macOS permet également le partage de fichiers avec SMB) et a ensuite été nettoyé et optimisé sous la forme du protocole Common Internet File System (CIFS).

Samba est ce que nous appelons les utilitaires Linux pour travailler avec CIFS sur Linux. En plus du partage de fichiers, vous pouvez également partager des ressources comme les imprimantes.

### Créer un partage réseau avec Samba

Passons en revue les étapes de base pour créer un partage réseau auquel une machine Windows peut accéder :

### Install Samba

```bash
sudo apt update
sudo apt install samba
```

### Setup smb.conf

Le fichier de configuration pour Samba se trouve à `/etc/samba/smb.conf`. Ce fichier doit indiquer au système quels répertoires doivent être partagés, leurs permissions d'accès et d'autres options. Le `smb.conf` par défaut est livré avec beaucoup de code commenté, et vous pouvez les utiliser comme exemple pour écrire vos propres configurations.

```bash
sudo vi /etc/samba/smb.conf
```

### Set up a password for Samba

```bash
sudo smbpasswd -a [username]
```

### Create a shared directory

```bash
mkdir /my/directory/to/share
```

### Restart the Samba service

```bash
sudo service smbd restart
```

### Accessing a Samba share via Windows

Sous Windows, il suffit de taper la connexion réseau dans l'invite Exécuter : `\\HOST\sharename`.

### Accessing a Samba/Windows share via Linux

```bash
smbclient //HOST/directory -U user
```

Le paquet Samba inclut un outil en ligne de commande appelé **smbclient** que vous pouvez utiliser pour accéder à n'importe quel serveur Windows ou Samba. Une fois connecté au partage, vous pouvez naviguer et transférer des fichiers.

### Attach a Samba share to your system

Au lieu de transférer les fichiers un par un, vous pouvez simplement monter le partage réseau sur votre système.

```bash
sudo mount -t cifs servername:directory mountpoint -o user=username,pass=password
```

## Exercise

Configurez un partage Samba. Si vous n'en avez pas, ouvrez `smb.conf` et familiarisez-vous avec les options du fichier de configuration.

## Quiz Question

Quel est le protocole le plus récent utilisé pour le transfert de fichiers entre Windows et Linux ?

## Quiz Answer

CIFS
