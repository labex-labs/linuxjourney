---
index: 5
lang: "de"
title: "Samba"
meta_title: "Samba - Netzwerkfreigabe"
meta_description: "Lernen Sie, Samba-Dateifreigaben unter Linux für Windows und macOS einzurichten. Dieser Anfängerleitfaden behandelt Installation, Konfiguration und den Zugriff auf Freigaben. Legen Sie los!"
meta_keywords: "Samba, Linux-Dateifreigabe, smb.conf, CIFS, smbclient, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

In den frühen Tagen des Computings wurde es notwendig, dass Windows-Maschinen Dateien mit Linux-Maschinen teilen konnten; so entstand das Server Message Block (SMB)-Protokoll. SMB wurde zum Teilen von Dateien zwischen Windows-Betriebssystemen verwendet (macOS verfügt ebenfalls über Dateifreigabe mit SMB) und wurde später in Form des Common Internet File System (CIFS)-Protokolls bereinigt und optimiert.

Samba nennen wir die Linux-Dienstprogramme, um mit CIFS unter Linux zu arbeiten. Neben der Dateifreigabe können Sie auch Ressourcen wie Drucker freigeben.

### Eine Netzwerkfreigabe mit Samba erstellen

Gehen wir die grundlegenden Schritte durch, um eine Netzwerkfreigabe zu erstellen, auf die eine Windows-Maschine zugreifen kann:

### Install Samba

```bash
sudo apt update
sudo apt install samba
```

### Setup smb.conf

Die Konfigurationsdatei für Samba befindet sich unter `/etc/samba/smb.conf`. Diese Datei sollte dem System mitteilen, welche Verzeichnisse freigegeben werden sollen, deren Zugriffsrechte und weitere Optionen. Die Standard-`smb.conf` enthält bereits viele auskommentierte Codes, und Sie können diese als Beispiel verwenden, um Ihre eigenen Konfigurationen zu schreiben.

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

In Windows, just type the network connection in the Run prompt: `\\HOST\sharename`.

### Accessing a Samba/Windows share via Linux

```bash
smbclient //HOST/directory -U user
```

The Samba package includes a command-line tool called **smbclient** that you can use to access any Windows or Samba server. Once you're connected to the share, you can navigate and transfer files.

### Attach a Samba share to your system

Instead of transferring files one by one, you can just mount the network share on your system.

```bash
sudo mount -t cifs servername:directory mountpoint -o user=username,pass=password
```

## Exercise

Richten Sie eine Samba-Freigabe ein. Falls Sie keine haben, öffnen Sie `smb.conf` und machen Sie sich mit den Optionen in der Konfigurationsdatei vertraut.

## Quiz Question

Was ist das neueste Protokoll, das für die Dateiübertragung zwischen Windows und Linux verwendet wird?

## Quiz Answer

CIFS
