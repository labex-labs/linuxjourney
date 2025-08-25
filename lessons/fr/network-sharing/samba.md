---
index: 5
lang: "fr"
title: "Samba"
meta_title: "Samba - Partage réseau"
meta_description: "Apprenez à configurer des partages de fichiers Samba sur Linux pour Windows et macOS. Ce guide pour débutants couvre l'installation, la configuration et l'accès aux partages. Lancez-vous !"
meta_keywords: "Samba, partage de fichiers Linux, smb.conf, CIFS, smbclient, tutoriel Linux, guide du débutant"
---

## Lesson Content

Au début de l'informatique, il est devenu nécessaire pour les machines Windows de partager des fichiers avec les machines Linux ; ainsi est né le protocole Server Message Block (SMB). SMB était utilisé pour le partage de fichiers entre les systèmes d'exploitation Windows (macOS dispose également du partage de fichiers avec SMB) et a ensuite été nettoyé et optimisé sous la forme du protocole Common Internet File System (CIFS).

Samba est ce que nous appelons les utilitaires Linux pour travailler avec CIFS sur Linux. En plus du partage de fichiers, vous pouvez également partager des ressources comme les imprimantes.

### Créer un partage réseau avec Samba

Passons en revue les étapes de base pour créer un partage réseau auquel une machine Windows peut accéder :

### Installer Samba

```bash
sudo apt update
sudo apt install samba
```

### Configurer smb.conf

Le fichier de configuration de Samba se trouve à l'adresse `/etc/samba/smb.conf`. Ce fichier doit indiquer au système quels répertoires doivent être partagés, leurs permissions d'accès et d'autres options. Le fichier `smb.conf` par défaut contient déjà beaucoup de code commenté, et vous pouvez les utiliser comme exemple pour écrire vos propres configurations.

```bash
sudo vi /etc/samba/smb.conf
```

### Définir un mot de passe pour Samba

```bash
sudo smbpasswd -a [username]
```

### Créer un répertoire partagé

```bash
mkdir /my/directory/to/share
```

### Redémarrer le service Samba

```bash
sudo service smbd restart
```

### Accéder à un partage Samba via Windows

Sous Windows, il suffit de taper la connexion réseau dans l'invite Exécuter : `\\HOST\sharename`.

### Accéder à un partage Samba/Windows via Linux

```bash
smbclient //HOST/directory -U user
```

Le paquet Samba inclut un outil en ligne de commande appelé **smbclient** que vous pouvez utiliser pour accéder à n'importe quel serveur Windows ou Samba. Une fois connecté au partage, vous pouvez naviguer et transférer des fichiers.

### Attacher un partage Samba à votre système

Au lieu de transférer les fichiers un par un, vous pouvez simplement monter le partage réseau sur votre système.

```bash
sudo mount -t cifs servername:directory mountpoint -o user=username,pass=password
```

## Exercise

Bien qu'il n'y ait pas de laboratoires spécifiques pour ce sujet, nous vous recommandons d'explorer le [Parcours d'apprentissage Linux](https://labex.io/fr/learn/linux) complet pour pratiquer les compétences et concepts Linux connexes.

## Quiz Question

Quel est le dernier protocole utilisé pour le transfert de fichiers entre Windows et Linux ?

## Quiz Answer

CIFS
