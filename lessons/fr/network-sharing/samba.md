---
index: 5
lang: "fr"
title: "Samba"
meta_title: "Samba - Partage Réseau"
meta_description: "Apprenez à configurer un partage réseau Samba sous Linux. Ce guide couvre le protocole Samba, l'installation, la configuration et l'utilisation des clients smb linux pour se connecter aux partages."
meta_keywords: "Samba, smb linux, smb linux, réseau samba, protocole samba, smb samba, partage de fichiers, smb.conf, cifs, smbclient, tutoriel linux"
---

## Lesson Content

Depuis des décennies, un défi majeur dans les environnements mixtes (Windows/Linux) a été le partage de fichiers entre les machines Windows et Linux. La solution qui a émergé est le protocole Server Message Block (SMB). Initialement développé pour Windows, le **protocole samba** a été affiné plus tard en un dialecte connu sous le nom de Common Internet File System (CIFS). Aujourd'hui, les systèmes modernes utilisent des versions plus récentes de SMB, mais les termes sont souvent utilisés conjointement.

Samba est la suite logicielle puissante qui implémente le protocole **SMB/CIFS** sur Linux et d'autres systèmes de type Unix. C'est la clé de l'intégration **smb linux**, permettant à un serveur Linux d'agir comme serveur de fichiers et d'impression pour les clients Windows, macOS et autres Linux, créant un **réseau samba** transparent. La relation entre **smb samba** est simple : Samba est le logiciel qui parle le langage SMB.

### Installation de Samba sous Linux

Pour commencer, vous devez installer le paquet Samba. La commande varie en fonction du gestionnaire de paquets de votre distribution Linux. Pour les systèmes basés sur Debian comme Ubuntu, utilisez ce qui suit :

```bash
sudo apt update
sudo apt install samba
```

### Configuration d'un Partage Samba

Le fichier de configuration principal pour Samba est situé à l'emplacement `/etc/samba/smb.conf`. Ce fichier dicte quels répertoires sont partagés, qui peut y accéder et leurs permissions. Le fichier par défaut contient de nombreux exemples commentés qui servent de bonne référence.

Passons en revue les étapes pour configurer un partage de base.

Ouvrez d'abord le fichier de configuration dans un éditeur de texte :

```bash
sudo nano /etc/samba/smb.conf
```

Au bas du fichier, ajoutez une nouvelle section pour votre partage. Le nom entre crochets sera le nom du partage visible sur le réseau.

```ini
[myshare]
    comment = Mon Premier Partage Samba
    path = /my/directory/to/share
    read only = no
    browsable = yes
```

Ensuite, créez le répertoire que vous avez spécifié dans la configuration :

```bash
mkdir -p /my/directory/to/share
```

Enfin, vous devez configurer un mot de passe spécifique pour l'accès Samba. Samba maintient sa propre base de données de mots de passe, qui est séparée des mots de passe utilisateurs du système.

```bash
sudo smbpasswd -a [username]
```

Remplacez `[username]` par un utilisateur Linux existant sur votre système. Il vous sera demandé de créer un nouveau mot de passe pour cet utilisateur pour l'accès Samba.

### Gestion du Service Samba

Après avoir modifié le fichier `smb.conf`, vous devez redémarrer le service Samba pour que les changements prennent effet.

```bash
sudo service smbd restart
```

### Accès aux Partages Samba

Une fois votre partage configuré, les clients sur le réseau peuvent y accéder.

**Depuis Windows :**
Ouvrez l'invite d'exécution (Win + R) ou l'Explorateur de fichiers et tapez le chemin réseau : `\\HOTE\nomdupartage`, où `HOTE` est l'adresse IP ou le nom d'hôte de votre machine Linux.

**Depuis Linux :**
Le paquet Samba inclut un outil en ligne de commande appelé **smbclient** qui vous permet d'interagir avec n'importe quel partage **smb linux** ou Windows.

```bash
smbclient //HOTE/myshare -U username
```

Après la connexion, vous obtiendrez une invite `smb: \>` où vous pourrez utiliser des commandes comme `ls`, `get` et `put` pour gérer les fichiers.

### Montage d'un Partage Samba

Pour un accès plus permanent, vous pouvez monter le partage réseau directement sur votre système de fichiers, le faisant apparaître comme un répertoire local.

```bash
sudo mount -t cifs //SERVEUR/nomdupartage /mnt/pointdemontage -o user=username,pass=password
```

Cette commande utilise le type de système de fichiers `cifs` pour attacher le partage distant à un point de montage local.

## Exercise

Essayez de configurer un partage Samba simple sur votre propre machine Linux. Créez un répertoire, configurez-le dans `smb.conf`, et essayez d'y accéder en utilisant `smbclient` depuis la même machine pour tester la configuration. Pour une pratique plus concrète, explorez le [Parcours d'Apprentissage Linux](https://labex.io/fr/learn/linux) complet pour pratiquer les compétences et concepts Linux associés.

## Quiz Question

Quel est le nom du protocole, un ancien dialecte de SMB, qui a été développé pour le partage de fichiers ? Veuillez répondre en anglais, en faisant attention à la casse.

## Quiz Answer

CIFS
