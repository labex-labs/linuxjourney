---
index: 1
lang: "de"
title: "Dateifreigabe-Übersicht"
meta_title: "Dateifreigabe-Übersicht - Netzwerkfreigabe"
meta_description: "Erfahren Sie mehr über die Linux-Dateifreigabe und den Befehl secure copy (scp). Übertragen Sie Dateien zwischen Hosts in Ihrem Netzwerk. Beginnen Sie mit diesem anfängerfreundlichen Leitfaden!"
meta_keywords: "Linux-Dateifreigabe, scp-Befehl, sicheres Kopieren, Netzwerkdateitransfer, Linux-Tutorial, Linux für Anfänger, Linux-Leitfaden"
---

## Lesson Content

Sie sind normalerweise nicht der einzige Computer in Ihrem Netzwerk, besonders wenn Sie in einem kommerziellen Umfeld arbeiten. Wenn wir Daten von einer Maschine auf eine andere übertragen möchten, ist es manchmal einfacher, ein USB-Laufwerk anzuschließen und sie manuell zu kopieren. Aber größtenteils, wenn Sie mit Maschinen im selben Netzwerk arbeiten, erfolgt die Datenübertragung über die Netzwerkdateifreigabe.

In diesem Kurs werden wir einige verschiedene Methoden zum Kopieren von Daten zu und von verschiedenen Maschinen in Ihrem Netzwerk behandeln. Wir werden einige einfache Dateikopien besprechen, dann werden wir über das Einhängen ganzer Verzeichnisse auf Ihrer Maschine sprechen, die als separates Laufwerk fungieren.

Ein einfaches Dateifreigabe-Tool ist der Befehl **scp**. Der Befehl scp steht für secure copy; er funktioniert genau wie der Befehl cp, ermöglicht es Ihnen jedoch, von einem Host zu einem anderen Host im selben Netzwerk zu kopieren. Er funktioniert über ssh, sodass alle Ihre Aktionen dieselbe Authentifizierung und Sicherheit wie ssh verwenden.

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

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis der sicheren Netzwerkdateiverwaltung zu vertiefen:

1. **[Sicherer Fernzugriff in Linux mit SSH](https://labex.io/de/labs/comptia-secure-remote-access-in-linux-with-ssh-592816)** – Üben Sie schlüsselbasierte Authentifizierung, sicheres Übertragen von Dateien mit `scp` und das Erstellen von SSH-Tunneln für die Portweiterleitung.

Dieses Labor wird Ihnen helfen, die Konzepte des sicheren Fernzugriffs und der Dateiübertragung in einem realen Szenario anzuwenden und Vertrauen in `scp` aufzubauen.

## Quiz Question

Welchen Befehl können Sie verwenden, um Dateien sicher von einem Host auf einen anderen zu kopieren?

## Quiz Answer

scp
