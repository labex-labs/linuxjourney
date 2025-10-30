---
index: 8
lang: "de"
title: "Das Sticky Bit"
meta_title: "Das Sticky Bit - Berechtigungen"
meta_description: "Erfahren Sie mehr über das Linux Sticky Bit, seinen Zweck in freigegebenen Verzeichnissen wie /tmp und wie Sie es mit chmod setzen. Verstehen Sie diese wichtige Dateiberechtigung!"
meta_keywords: "Linux Sticky Bit, chmod +t, /tmp Verzeichnis, Linux Berechtigungen, Dateisicherheit, Linux Tutorial, Linux für Anfänger"
---

## Lesson Content

Ein letztes spezielles Berechtigungsbit, über das ich sprechen möchte, ist das Sticky Bit.

Dieses Berechtigungsbit "klebt eine Datei/ein Verzeichnis", was bedeutet, dass nur der Eigentümer oder der Root-Benutzer die Datei löschen oder ändern kann. Dies ist sehr nützlich für freigegebene Verzeichnisse. Sehen Sie sich das folgende Beispiel an:

```bash
$ ls -ld /tmp
drwxrwxrwx+t 6 root root 4096 Dec 15 11:45 /tmp
```

Sie sehen hier am Ende ein spezielles Berechtigungsbit **t**. Das bedeutet, dass jeder Dateien im Verzeichnis `/tmp` hinzufügen, schreiben und ändern kann, aber nur root das Verzeichnis `/tmp` löschen kann.

### Sticky Bit ändern

```bash
sudo chmod +t mydir

sudo chmod 1755 mydir
```

Die numerische Darstellung für das Sticky Bit ist **1**.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Linux-Dateiberechtigungen und deren Auswirkungen auf die Datei- und Verzeichnisverwaltung zu vertiefen:

1. **[Linux Benutzergruppe und Dateiberechtigungen](https://labex.io/de/labs/linux-linux-user-group-and-file-permissions-18002)** - Üben Sie das Erstellen und Verwalten von Benutzern und Gruppen, das Verständnis von Dateiberechtigungen und das Manipulieren des Dateibesitzes. Dieses Labor vermittelt das grundlegende Wissen, um zu verstehen, wie spezielle Berechtigungen wie das Sticky Bit funktionieren.
2. **[Dateien löschen und verschieben](https://labex.io/de/labs/linux-delete-and-move-files-7777)** - Erfahren Sie, wie Sie Dateien in Linux-Systemen löschen und verschieben. Dieses Labor hilft Ihnen, die praktischen Auswirkungen von Berechtigungen zu verstehen, einschließlich der Art und Weise, wie sie diese Aktionen einschränken können.
3. **[Eine Datei finden](https://labex.io/de/labs/linux-find-a-file-17993)** - Üben Sie das Auffinden von Dateien und das Festlegen von Zugriffsrechten. Dieses Labor unterstreicht die Bedeutung von Dateiberechtigungen und wie sie den Zugriff und die Änderung steuern.

Diese Labore helfen Ihnen, die Konzepte der Dateiberechtigungen in realen Szenarien anzuwenden und Vertrauen in die Verwaltung des Dateizugriffs unter Linux aufzubauen.

## Quiz Question

Welches Symbol repräsentiert das Sticky Bit?

## Quiz Answer

t
