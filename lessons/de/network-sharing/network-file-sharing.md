---
index: 1
lang: "de"
title: "Übersicht über die Dateifreigabe"
meta_title: "Übersicht über die Dateifreigabe - Netzwerkfreigabe"
meta_description: "Erfahren Sie mehr über die Linux-Dateifreigabe und den Befehl secure copy (scp). Übertragen Sie Dateien zwischen Hosts in Ihrem Netzwerk. Beginnen Sie mit dieser anfängerfreundlichen Anleitung!"
meta_keywords: "Linux-Dateifreigabe, scp-Befehl, sichere Kopie, Netzwerk-Dateiübertragung, Linux-Tutorial, Linux für Anfänger, Linux-Anleitung"
---

## Lesson Content

Sie sind normalerweise nicht der einzige Computer in Ihrem Netzwerk, besonders wenn Sie in einem kommerziellen Umfeld arbeiten. Wenn wir Daten von einer Maschine auf eine andere übertragen möchten, kann es manchmal einfacher sein, ein USB-Laufwerk anzuschließen und sie manuell zu kopieren. Aber größtenteils, wenn Sie mit Maschinen im selben Netzwerk arbeiten, erfolgt die Datenübertragung über die Netzwerkdateifreigabe.

In diesem Kurs werden wir verschiedene Methoden zum Kopieren von Daten zu und von verschiedenen Maschinen in Ihrem Netzwerk behandeln. Wir werden einige einfache Dateikopien besprechen, dann werden wir über das Einhängen ganzer Verzeichnisse auf Ihrer Maschine sprechen, die als separates Laufwerk fungieren.

Ein einfaches Dateifreigabe-Tool ist der Befehl **scp**. Der scp-Befehl steht für secure copy; er funktioniert genau wie der cp-Befehl, ermöglicht es Ihnen jedoch, von einem Host zu einem anderen Host im selben Netzwerk zu kopieren. Er funktioniert über ssh, sodass alle Ihre Aktionen dieselbe Authentifizierung und Sicherheit wie ssh verwenden.

### So kopieren Sie eine Datei von einem lokalen Host auf einen Remote-Host

```bash
scp myfile.txt username@remotehost.com:/remote/directory
```

### So kopieren Sie eine Datei von einem Remote-Host auf Ihren lokalen Host

```bash
scp username@remotehost.com:/remote/directory/myfile.txt /local/directory
```

### So kopieren Sie ein Verzeichnis von Ihrem lokalen Host auf einen Remote-Host

```bash
scp -r mydir username@remotehost.com:/remote/directory
```

## Exercise

Versuchen Sie, eine Datei mit scp von einer Maschine auf eine andere zu kopieren.

## Quiz Question

Welchen Befehl können Sie verwenden, um Dateien sicher von einem Host auf einen anderen zu kopieren?

## Quiz Answer

scp
