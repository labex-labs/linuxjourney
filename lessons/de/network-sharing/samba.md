---
index: 5
lang: "de"
title: "Samba"
meta_title: "Samba - Netzwerkfreigabe"
meta_description: "Lernen Sie, Samba-Dateifreigaben unter Linux für Windows und macOS einzurichten. Dieser Leitfaden für Anfänger behandelt Installation, Konfiguration und Zugriff auf Freigaben. Legen Sie los!"
meta_keywords: "Samba, Linux-Dateifreigabe, smb.conf, CIFS, smbclient, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

In den frühen Tagen der Computer wurde es notwendig, dass Windows-Maschinen Dateien mit Linux-Maschinen teilen konnten; so entstand das Server Message Block (SMB) Protokoll. SMB wurde zum Teilen von Dateien zwischen Windows-Betriebssystemen verwendet (macOS bietet ebenfalls Dateifreigabe mit SMB) und wurde später in Form des Common Internet File System (CIFS) Protokolls bereinigt und optimiert.

Samba nennen wir die Linux-Dienstprogramme, um mit CIFS unter Linux zu arbeiten. Neben der Dateifreigabe können Sie auch Ressourcen wie Drucker freigeben.

### Eine Netzwerkfreigabe mit Samba erstellen

Gehen wir die grundlegenden Schritte durch, um eine Netzwerkfreigabe zu erstellen, auf die eine Windows-Maschine zugreifen kann:

### Samba installieren

```bash
sudo apt update
sudo apt install samba
```

### smb.conf einrichten

Die Konfigurationsdatei für Samba befindet sich unter `/etc/samba/smb.conf`. Diese Datei sollte dem System mitteilen, welche Verzeichnisse freigegeben werden sollen, deren Zugriffsrechte und weitere Optionen. Die Standard-`smb.conf` enthält bereits viele auskommentierte Codes, die Sie als Beispiel für Ihre eigenen Konfigurationen verwenden können.

```bash
sudo vi /etc/samba/smb.conf
```

### Ein Passwort für Samba einrichten

```bash
sudo smbpasswd -a [username]
```

### Ein freigegebenes Verzeichnis erstellen

```bash
mkdir /my/directory/to/share
```

### Den Samba-Dienst neu starten

```bash
sudo service smbd restart
```

### Auf eine Samba-Freigabe über Windows zugreifen

In Windows geben Sie einfach die Netzwerkverbindung in der Ausführen-Eingabeaufforderung ein: `\\HOST\sharename`.

### Auf eine Samba-/Windows-Freigabe über Linux zugreifen

```bash
smbclient //HOST/directory -U user
```

Das Samba-Paket enthält ein Befehlszeilentool namens **smbclient**, mit dem Sie auf jeden Windows- oder Samba-Server zugreifen können. Sobald Sie mit der Freigabe verbunden sind, können Sie navigieren und Dateien übertragen.

### Eine Samba-Freigabe an Ihr System anhängen

Anstatt Dateien einzeln zu übertragen, können Sie die Netzwerkfreigabe einfach in Ihr System einbinden.

```bash
sudo mount -t cifs servername:directory mountpoint -o user=username,pass=password
```

## Exercise

Obwohl es keine spezifischen Labs für dieses Thema gibt, empfehlen wir Ihnen, den umfassenden [Linux-Lernpfad](https://labex.io/de/learn/linux) zu erkunden, um verwandte Linux-Fähigkeiten und -Konzepte zu üben.

## Quiz Question

Was ist das neueste Protokoll, das für die Dateiübertragung zwischen Windows und Linux verwendet wird?

## Quiz Answer

CIFS
