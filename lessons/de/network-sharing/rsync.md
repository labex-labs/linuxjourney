---
index: 2
lang: "de"
title: "rsync"
meta_title: "rsync - Netzwerkfreigabe"
meta_description: "Lernen Sie rsync für effiziente Linux-Dateisynchronisation und Backups. Verstehen Sie die Remote- und lokale Datenübertragung mit rsync-Befehlen und -Optionen. Verbessern Sie Ihre Linux-Kenntnisse!"
meta_keywords: "rsync, Linux-Dateiübertragung, Datensicherung, Dateisynchronisation, Linux-Tutorial, rsync-Befehle, Anfänger, Leitfaden"
---

## Lesson Content

Ein weiteres Werkzeug zum Kopieren von Daten von verschiedenen Hosts ist rsync (kurz für Remote Synchronization). Rsync ist scp sehr ähnlich, hat aber einen großen Unterschied. Rsync verwendet einen speziellen Algorithmus, der im Voraus prüft, ob bereits Daten vorhanden sind, die Sie kopieren, und kopiert nur die Unterschiede. Nehmen wir zum Beispiel an, Sie kopieren eine Datei und Ihre Netzwerkverbindung wird unterbrochen; daher stoppt Ihr Kopiervorgang mitten im Prozess. Anstatt alles von Anfang an neu zu kopieren, kopiert rsync nur die Teile, die nicht kopiert wurden.

Es überprüft auch die Integrität einer Datei, die Sie kopieren, mit Prüfsummen. Diese kleinen Optimierungen ermöglichen eine größere Flexibilität bei der Dateiübertragung und machen rsync ideal für die Verzeichnissynchronisation remote und lokal, Datensicherungen, große Datenübertragungen und mehr.

Einige häufig verwendete rsync-Optionen:

- v - ausführliche Ausgabe
- r - rekursiv in Verzeichnisse
- h - menschenlesbare Ausgabe
- z - komprimiert für einfachere Übertragung, ideal für langsame Verbindungen

### Dateien auf demselben Host kopieren/synchronisieren

```bash
rsync -zvr /my/local/directory/one /my/local/directory/two
```

### Dateien vom Remote-Host auf den lokalen Host kopieren/synchronisieren

```bash
rsync /local/directory username@remotehost.com:/remote/directory
```

### Dateien vom lokalen Host auf einen Remote-Host kopieren/synchronisieren

```bash
rsync username@remotehost.com:/remote/directory /local/directory
```

## Exercise

Obwohl es keine spezifischen Labs für dieses Thema gibt, empfehlen wir, den umfassenden [Linux-Lernpfad](https://labex.io/de/learn/linux) zu erkunden, um verwandte Linux-Fähigkeiten und -Konzepte zu üben.

## Quiz Question

Welcher Befehl wäre für Datensicherungen nützlich?

## Quiz Answer

rsync
