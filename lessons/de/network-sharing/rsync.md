---
index: 2
lang: "de"
title: "rsync"
meta_title: "rsync - Netzwerkfreigabe"
meta_description: "Lernen Sie rsync für effiziente Linux-Dateisynchronisation und Backups. Verstehen Sie die Remote- und lokale Datenübertragung mit rsync-Befehlen und -Optionen. Verbessern Sie Ihre Linux-Kenntnisse!"
meta_keywords: "rsync, Linux-Dateiübertragung, Datensicherung, Dateisynchronisation, Linux-Tutorial, rsync-Befehle, Anfänger, Leitfaden"
---

## Lesson Content

Ein weiteres Tool zum Kopieren von Daten von verschiedenen Hosts ist rsync (kurz für remote synchronization). Rsync ist scp sehr ähnlich, hat aber einen großen Unterschied. Rsync verwendet einen speziellen Algorithmus, der im Voraus prüft, ob bereits Daten vorhanden sind, in die Sie kopieren, und kopiert nur die Unterschiede. Nehmen wir zum Beispiel an, Sie kopieren eine Datei und Ihre Netzwerkverbindung wird unterbrochen; daher wurde Ihr Kopiervorgang mittendrin gestoppt. Anstatt alles von vorne zu kopieren, kopiert rsync nur die Teile, die nicht kopiert wurden.

Es überprüft auch die Integrität einer Datei, die Sie kopieren, mit Prüfsummen. Diese kleinen Optimierungen ermöglichen eine größere Flexibilität bei der Dateiübertragung und machen rsync ideal für die Verzeichnissynchronisation remote und lokal, Datensicherungen, große Datenübertragungen und mehr.

Einige häufig verwendete rsync-Optionen:

- v - verbose output
- r - recursive into directories
- h - human-readable output
- z - compressed for easier transfer, great for slow connections

### Copy/sync files on the same host

```bash
rsync -zvr /my/local/directory/one /my/local/directory/two
```

### Copy/sync files to local host from a remote host

```bash
rsync /local/directory username@remotehost.com:/remote/directory
```

### Copy/sync files to a remote host from a local host

```bash
rsync username@remotehost.com:/remote/directory /local/directory
```

## Exercise

Verwenden Sie rsync, um ein Verzeichnis mit einem anderen Verzeichnis zu synchronisieren. Achten Sie darauf, kein wichtiges Verzeichnis zu überschreiben!

## Quiz Question

Welcher Befehl wäre für Datensicherungen nützlich?

## Quiz Answer

rsync
