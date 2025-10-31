---
index: 5
lang: "de"
title: "Samba"
meta_title: "Samba - Netzwerkfreigabe"
meta_description: "Erfahren Sie, wie Sie eine Samba-Netzwerkfreigabe unter Linux einrichten. Diese Anleitung behandelt das Samba-Protokoll, Installation, Konfiguration und die Verwendung von smb-Linux-Clients zur Verbindung mit Freigaben."
meta_keywords: "Samba, smb linux, linux smb, samba netzwerk, samba protokoll, smb samba, dateifreigabe, smb.conf, cifs, smbclient, linux anleitung"
---

## Lesson Content

Jahrzehntelang war die gemeinsame Nutzung von Dateien zwischen Windows- und Linux-Rechnern eine primäre Herausforderung in gemischten Betriebssystemumgebungen. Die Lösung, die sich herauskristallisierte, ist das Server Message Block (SMB) Protokoll. Ursprünglich für Windows entwickelt, wurde das **Samba-Protokoll** später zu einem Dialekt verfeinert, der als Common Internet File System (CIFS) bekannt ist. Heutzutage verwenden moderne Systeme neuere Versionen von SMB, aber die Begriffe werden oft zusammen verwendet.

Samba ist die leistungsstarke Software-Suite, die das **SMB/CIFS**-Protokoll auf Linux und anderen Unix-ähnlichen Systemen implementiert. Es ist der Schlüssel zur **smb linux**-Integration und ermöglicht es einem Linux-Server, als Datei- und Druckserver für Windows-, macOS- und andere Linux-Clients zu fungieren und so ein nahtloses **Samba-Netzwerk** zu schaffen. Die Beziehung zwischen **smb samba** ist einfach: Samba ist die Software, die die SMB-Sprache spricht.

### Samba unter Linux installieren

Zuerst müssen Sie das Samba-Paket installieren. Der Befehl variiert je nach Paketmanager Ihrer Linux-Distribution. Für Debian-basierte Systeme wie Ubuntu verwenden Sie Folgendes:

```bash
sudo apt update
sudo apt install samba
```

### Eine Samba-Freigabe konfigurieren

Die Hauptkonfigurationsdatei für Samba befindet sich unter `/etc/samba/smb.conf`. Diese Datei legt fest, welche Verzeichnisse freigegeben werden, wer darauf zugreifen kann und welche Berechtigungen gelten. Die Standarddatei enthält viele auskommentierte Beispiele, die als hervorragende Referenz dienen.

Gehen wir die Schritte zur Konfiguration einer einfachen Freigabe durch.

Öffnen Sie zuerst die Konfigurationsdatei in einem Texteditor:

```bash
sudo nano /etc/samba/smb.conf
```

Fügen Sie am Ende der Datei einen neuen Abschnitt für Ihre Freigabe hinzu. Der Name in den Klammern ist der Name der Freigabe, der im Netzwerk sichtbar ist.

```ini
[myshare]
    comment = Meine erste Samba-Freigabe
    path = /my/directory/to/share
    read only = no
    browsable = yes
```

Erstellen Sie als Nächstes das Verzeichnis, das Sie in der Konfiguration angegeben haben:

```bash
mkdir -p /my/directory/to/share
```

Zuletzt müssen Sie ein spezifisches Passwort für den Samba-Zugriff einrichten. Samba pflegt eine eigene Passwortdatenbank, die von den Systembenutzerpasswörtern getrennt ist.

```bash
sudo smbpasswd -a [username]
```

Ersetzen Sie `[username]` durch einen vorhandenen Linux-Benutzer auf Ihrem System. Sie werden aufgefordert, ein neues Passwort für diesen Benutzer für den Samba-Zugriff zu erstellen.

### Den Samba-Dienst verwalten

Nachdem Sie Änderungen an der Datei `smb.conf` vorgenommen haben, müssen Sie den Samba-Dienst neu starten, damit diese wirksam werden.

```bash
sudo service smbd restart
```

### Auf Samba-Freigaben zugreifen

Sobald Ihre Freigabe konfiguriert ist, können Clients im Netzwerk darauf zugreifen.

**Von Windows aus:**
Öffnen Sie das Ausführen-Fenster (Win + R) oder den Datei-Explorer und geben Sie den Netzwerkpfad ein: `\\HOST\sharename`, wobei HOST die IP-Adresse oder der Hostname Ihres Linux-Rechners ist.

**Von Linux aus:**
Das Samba-Paket enthält ein Befehlszeilenwerkzeug namens **smbclient**, mit dem Sie mit jeder **linux smb**- oder Windows-Freigabe interagieren können.

```bash
smbclient //HOST/myshare -U username
```

Nach der Verbindung erhalten Sie eine `smb: \>`-Eingabeaufforderung, in der Sie Befehle wie `ls`, `get` und `put` zur Verwaltung von Dateien verwenden können.

### Eine Samba-Freigabe einbinden (mounten)

Für einen dauerhafteren Zugriff können Sie die Netzwerkfreigabe direkt in Ihr Dateisystem einbinden, sodass sie wie ein lokales Verzeichnis erscheint.

```bash
sudo mount -t cifs //SERVER/sharename /mnt/mountpoint -o user=username,pass=password
```

Dieser Befehl verwendet den Dateisystemtyp `cifs`, um die Remote-Freigabe an einen lokalen Einhängepunkt anzuhängen.

## Exercise

Versuchen Sie, eine einfache Samba-Freigabe auf Ihrem eigenen Linux-Rechner einzurichten. Erstellen Sie ein Verzeichnis, konfigurieren Sie es in `smb.conf` und versuchen Sie, von demselben Rechner aus mit `smbclient` darauf zuzugreifen, um die Konfiguration zu testen. Für mehr praktische Übung erkunden Sie den umfassenden [Linux Lernpfad](https://labex.io/de/learn/linux), um verwandte Linux-Fähigkeiten und Konzepte zu üben.

## Quiz Question

What is the name of the protocol, an early dialect of SMB, that was developed for file sharing? Please answer in English, paying attention to capitalization.

## Quiz Answer

CIFS
