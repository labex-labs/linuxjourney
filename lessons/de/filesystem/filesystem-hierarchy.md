---
index: 1
lang: "de"
title: "Dateisystem Hierarchie"
meta_title: "Dateisystem Hierarchie - Das Dateisystem"
meta_description: "Lernen Sie den Linux Filesystem Hierarchy Standard (FHS) und verstehen Sie wichtige Verzeichnisse wie /bin, /etc und /var. Erkunden Sie die Linux-Verzeichnisstruktur."
meta_keywords: "Linux Dateisystem Hierarchie, FHS, Linux Verzeichnisstruktur, Linux Befehle, Linux für Anfänger, Linux Tutorial, Linux Anleitung"
---

## Lesson Content

An diesem Punkt sind Sie wahrscheinlich schon gut mit der Verzeichnisstruktur Ihres Systems vertraut; falls nicht, werden Sie es bald sein. Dateisysteme können in ihrer Struktur variieren, aber zum größten Teil sollten sie dem Filesystem Hierarchy Standard entsprechen.

Führen Sie ein `ls -l /` aus, um die Verzeichnisse unter dem Stammverzeichnis anzuzeigen. Ihre können anders aussehen als meine, aber die Verzeichnisse sollten größtenteils wie folgt aussehen:

- `/` - Das Stammverzeichnis der gesamten Dateisystemhierarchie; alles ist unter diesem Verzeichnis verschachtelt.
- `/bin` - Essentielle ausführbare Programme (Binärdateien); enthält die grundlegendsten Befehle wie `ls` und `cp`.
- `/boot` - Enthält Kernel-Bootloader-Dateien.
- `/dev` - Gerätedateien.
- `/etc` - Kern-Systemkonfigurationsverzeichnis; sollte nur Konfigurationsdateien und keine Binärdateien enthalten.
- `/home` - Persönliche Verzeichnisse für Benutzer; enthält Ihre Dokumente, Dateien, Einstellungen usw.
- `/lib` - Enthält Bibliotheksdateien, die Binärdateien verwenden können.
- `/media` - Wird als Einhängepunkt für Wechselmedien wie USB-Laufwerke verwendet.
- `/mnt` - Temporär eingehängte Dateisysteme.
- `/opt` - Optionale Anwendungssoftwarepakete.
- `/proc` - Informationen über aktuell laufende Prozesse.
- `/root` - Das Home-Verzeichnis des Root-Benutzers.
- `/run` - Informationen über das laufende System seit dem letzten Boot.
- `/sbin` - Enthält essentielle System-Binärdateien, die normalerweise nur von root ausgeführt werden können.
- `/srv` - Site-spezifische Daten, die vom System bereitgestellt werden.
- `/tmp` - Speicher für temporäre Dateien.
- `/usr` - Dies ist unglücklich benannt; meistens enthält es keine Benutzerdateien im Sinne eines Home-Ordners. Dies ist für vom Benutzer installierte Software und Dienstprogramme gedacht; das heißt jedoch nicht, dass Sie dort keine persönlichen Verzeichnisse hinzufügen können. In diesem Verzeichnis befinden sich Unterverzeichnisse für `/usr/bin`, `/usr/local` usw.
- `/var` - Variables Verzeichnis; es wird für Systemprotokollierung, Benutzerverfolgung, Caches usw. verwendet. Im Grunde alles, was sich ständig ändern kann.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis des Linux-Dateisystems zu vertiefen:

1. **[Dateisystem in Linux navigieren](https://labex.io/de/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Üben Sie die Verwendung grundlegender Shell-Befehle wie `pwd`, `cd` und `ls`, um zwischen Verzeichnissen zu wechseln und das Dateisystem zu erkunden.
2. **[Dateien und Verzeichnisse in Linux verwalten](https://labex.io/de/labs/comptia-manage-files-and-directories-in-linux-590835)** - Lernen Sie, Dateien und Verzeichnisse zu erstellen, zu entfernen, zu kopieren und zu verschieben, und verstehen Sie symbolische und Hardlinks.
3. **[Dateien und Befehle in Linux finden](https://labex.io/de/labs/comptia-find-files-and-commands-in-linux-590834)** - Meistern Sie Techniken zum Auffinden von Dateien und Befehlen mit `find`, `locate`, `whereis`, `which` und `type`.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Linux-Dateisystemverwaltung aufzubauen.

## Quiz Question

Welches Verzeichnis wird zum Speichern von Protokollen verwendet?

## Quiz Answer

/var
