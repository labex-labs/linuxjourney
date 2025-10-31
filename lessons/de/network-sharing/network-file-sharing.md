---
index: 1
lang: "de"
title: "Dateifreigabe-Übersicht"
meta_title: "Dateifreigabe-Übersicht - Netzwerkfreigabe"
meta_description: "Entdecken Sie Linux-Dateifreigabe mit unserem kostenlosen Online-Kurs. Lernen Sie eine der besten Methoden, um Linux-Befehle wie scp für sichere Dateiübertragungen im Netzwerk zu beherrschen. Eine wichtige Ressource für das Programmieren unter Linux."
meta_keywords: "linux dateifreigabe, scp befehl, sichere kopie, linux befehle lernen, bester linux kurs online kostenlos, programmieren unter linux, netzwerk dateiübertragung, beste ressourcen linux lernen"
---

## Lesson Content

In den meisten modernen Computerumgebungen ist Ihr Rechner selten isoliert. Ob zu Hause oder in einem Unternehmensumfeld, Sie sind typischerweise Teil eines Netzwerks. Wenn Sie Daten zwischen Computern übertragen müssen, könnten Sie ein USB-Laufwerk verwenden, aber für Maschinen im selben Netzwerk ist die Netzwerkdateifreigabe weitaus effizienter. Dies ist eine grundlegende Fähigkeit für jeden, der es ernst meint mit dem `coding in linux` oder der Systemverwaltung.

Diese Lektion, Teil dessen, was viele als den `best linux course online free` (beste kostenlose Online-Linux-Kurs) betrachten, führt Sie in Methoden zum Kopieren von Daten über ein Netzwerk ein. Wir beginnen mit einfachen Dateiübertragungen und besprechen später das Einhängen ganzer Remote-Verzeichnisse, sodass sie auf Ihrem Rechner wie lokale Laufwerke erscheinen. Diese Seite hat zum Ziel, die `best website to learn linux` (beste Webseite, um Linux zu lernen) zu sein, indem sie klare, praktische Beispiele liefert.

### Der Secure Copy Befehl (scp)

Eines der einfachsten und leistungsstärksten Werkzeuge für diese Aufgabe ist der `scp`-Befehl, was für "secure copy" (sichere Kopie) steht. Er funktioniert ähnlich wie der Standardbefehl `cp`, erweitert seine Fähigkeit jedoch auf das Netzwerk. Das Verständnis ist einer der `best ways to learn linux commands` (beste Wege, Linux-Befehle zu lernen) für die Netzwerkinteraktion. Da `scp` über SSH (Secure Shell) läuft, profitieren alle Übertragungen von denselben robusten Authentifizierungs- und Sicherheitsprotokollen.

### Häufige scp-Befehlsbeispiele

Lassen Sie uns einige praktische Beispiele untersuchen. Die Syntax ist unkompliziert: `scp [optionen] quelle ziel`. Der Hauptunterschied zu `cp` besteht darin, dass die Quelle oder das Ziel eine Remote-Host-Spezifikation im Format `benutzername@remotehost:/pfad/zur/datei` enthält.

### Eine Datei von einem lokalen Host auf einen Remote-Host kopieren

Dieser Befehl sendet eine lokale Datei an ein angegebenes Verzeichnis auf einem Remote-Rechner.

```bash
scp myfile.txt benutzername@remotehost.com:/remote/verzeichnis
```

### Eine Datei von einem Remote-Host auf Ihren lokalen Host kopieren

Dieser Befehl ruft eine Datei von einem Remote-Rechner ab und speichert sie in einem lokalen Verzeichnis.

```bash
scp benutzername@remotehost.com:/remote/verzeichnis/myfile.txt /lokales/verzeichnis
```

### Ein Verzeichnis von Ihrem lokalen Host auf einen Remote-Host kopieren

Um ein ganzes Verzeichnis und seinen Inhalt zu kopieren, verwenden Sie die Option `-r` (rekursiv).

```bash
scp -r meinverzeichnis benutzername@remotehost.com:/remote/verzeichnis
```

Die Beherrschung von `scp` ist ein wesentlicher Schritt, und die Erforschung solcher Werkzeuge ist der Grund, warum viele dies als eine der `best resources to learn linux` (beste Ressourcen, um Linux zu lernen) ansehen.

## Exercise

Übung ist der Schlüssel zum Beherrschen neuer Befehle. Um Ihr Verständnis der sicheren Netzwerkdateitransfer zu festigen, empfehlen wir dieses praktische Labor:

1. **[Sicherer Remote-Zugriff unter Linux mit SSH](https://labex.io/de/labs/comptia-secure-remote-access-in-linux-with-ssh-592816)** - Üben Sie schlüsselbasierte Authentifizierung, sicheren Dateitransfer mit `scp` und das Erstellen von SSH-Tunneln für die Portweiterleitung.

Dieses Labor hilft Ihnen, die Konzepte des sicheren Remote-Zugriffs und des Dateitransfers in einem realen Szenario anzuwenden und Vertrauen in `scp` aufzubauen.

## Quiz Question

Welchen Befehl können Sie verwenden, um Dateien sicher von einem Host auf einen anderen zu kopieren? Bitte antworten Sie nur mit dem Befehlsnamen, in Kleinbuchstaben in englischer Sprache.

## Quiz Answer

scp
