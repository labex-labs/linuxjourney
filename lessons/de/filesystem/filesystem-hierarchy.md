---
title: "Dateisystemhierarchie"
description: "Lernen Sie den Linux Filesystem Hierarchy Standard (FHS) und verstehen Sie wichtige Verzeichnisse wie /bin, /etc und /var. Erkunden Sie die Linux-Verzeichnisstruktur."
keywords: "Linux Dateisystemhierarchie, FHS, Linux Verzeichnisstruktur, Linux Befehle, Linux für Anfänger, Linux Tutorial, Linux Anleitung"
---

## Lesson Content

An diesem Punkt sind Sie wahrscheinlich gut mit der Verzeichnisstruktur Ihres Systems vertraut; falls nicht, werden Sie es bald sein. Dateisysteme können in ihrer Struktur variieren, aber größtenteils sollten sie dem Filesystem Hierarchy Standard entsprechen.

Führen Sie `ls -l /` aus, um die Verzeichnisse unter dem Stammverzeichnis anzuzeigen. Ihre Ausgabe kann sich von meiner unterscheiden, aber die Verzeichnisse sollten größtenteils wie folgt aussehen:

- `/` - Das Stammverzeichnis der gesamten Dateisystemhierarchie; alles ist unter diesem Verzeichnis verschachtelt.
- `/bin` - Essentielle ausführbare Programme (Binaries); enthält die grundlegendsten Befehle wie `ls` und `cp`.
- `/boot` - Enthält Kernel-Bootloader-Dateien.
- `/dev` - Gerätedateien.
- `/etc` - Kern-Systemkonfigurationsverzeichnis; sollte nur Konfigurationsdateien und keine Binaries enthalten.
- `/home` - Persönliche Verzeichnisse für Benutzer; enthält Ihre Dokumente, Dateien, Einstellungen usw.
- `/lib` - Enthält Bibliotheksdateien, die von Binaries verwendet werden können.
- `/media` - Wird als Einhängepunkt für Wechselmedien wie USB-Laufwerke verwendet.
- `/mnt` - Temporär eingehängte Dateisysteme.
- `/opt` - Optionale Anwendungssoftwarepakete.
- `/proc` - Informationen über aktuell laufende Prozesse.
- `/root` - Das Home-Verzeichnis des Root-Benutzers.
- `/run` - Informationen über das laufende System seit dem letzten Boot.
- `/sbin` - Enthält essentielle System-Binaries, die normalerweise nur von root ausgeführt werden können.
- `/srv` - Site-spezifische Daten, die vom System bereitgestellt werden.
- `/tmp` - Speicher für temporäre Dateien.
- `/usr` - Dies ist unglücklich benannt; meistens enthält es keine Benutzerdateien im Sinne eines Home-Ordners. Dies ist für vom Benutzer installierte Software und Dienstprogramme gedacht; das heißt jedoch nicht, dass Sie dort keine persönlichen Verzeichnisse hinzufügen können. In diesem Verzeichnis befinden sich Unterverzeichnisse für `/usr/bin`, `/usr/local` usw.
- `/var` - Variables Verzeichnis; es wird für Systemprotokollierung, Benutzerverfolgung, Caches usw. verwendet. Im Grunde alles, was ständig Änderungen unterliegt.

## Exercise

Schauen Sie in Ihr `/usr`-Verzeichnis. Welche Art von Informationen befindet sich dort?

## Quiz Question

Welches Verzeichnis wird zum Speichern von Protokollen verwendet?

## Quiz Answer

/var
