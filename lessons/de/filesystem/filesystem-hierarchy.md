---
index: 1
lang: "de"
title: "Dateisystemhierarchie"
meta_title: "Dateisystemhierarchie - Das Dateisystem"
meta_description: "Erkunden Sie die Standard-Linux-Dateisystemhierarchie (FHS). Dieser Leitfaden erklärt den Zweck wichtiger Verzeichnisse wie /bin, /etc, /home und /var und bietet einen klaren Überblick über die Dateisystemhierarchie unter Linux."
meta_keywords: "linux dateisystemhierarchie, dateisystemhierarchie in linux, linux dateihierarchiestruktur, linux dateihierarchie, FHS, linux verzeichnisstruktur"
---

## Lesson Content

Sie machen sich wahrscheinlich mit der Verzeichnisstruktur auf Ihrem System vertraut. Die meisten Linux-Distributionen organisieren ihre Dateisysteme nach dem Standard der **Linux Filesystem Hierarchy** (FHS). Dieser Standard stellt sicher, dass Dateien an vorhersehbaren Orten gespeichert werden, was die Systeme konsistenter macht.

Um die obersten Verzeichnisse anzuzeigen, führen Sie den Befehl `ls -l /` aus. Obwohl Ihr System geringfügige Unterschiede aufweisen kann, wird die Kernstruktur der **linux file hierarchy structure** der unten beschriebenen sehr ähnlich sein.

### Das Root-Verzeichnis

- `/` - Dies ist das Root-Verzeichnis, der Ausgangspunkt für das gesamte Dateisystem. Jede einzelne Datei und jedes Verzeichnis auf Ihrem System befindet sich unter diesem Verzeichnis.

### Wesentliche Systemverzeichnisse

Die **file hierarchy in linux** umfasst mehrere Verzeichnisse, die für den Betrieb des Systems von entscheidender Bedeutung sind.

- `/bin` - Enthält wesentliche Befehlszeilenprogramme (Binärdateien), die allen Benutzern zur Verfügung stehen, wie z. B. `ls`, `cp` und `mv`.
- `/sbin` - Enthält wesentliche System-Binärdateien, die hauptsächlich für die Systemadministration bestimmt sind und typischerweise nur vom Root-Benutzer ausgeführt werden können.
- `/etc` - Dies ist das zentrale Konfigurationsverzeichnis des Systems. Es enthält Konfigurationsdateien für das Betriebssystem und installierte Anwendungen, sollte aber keine ausführbaren Binärdateien enthalten.
- `/lib` - Enthält wesentliche gemeinsam genutzte Bibliotheksdateien, von denen System-Binärdateien in `/bin` und `/sbin` für eine korrekte Funktion abhängen.
- `/boot` - Speichert die für den Bootvorgang des Systems erforderlichen Dateien, einschließlich des Linux-Kernels und der Bootloader-Dateien.

### Benutzer- und Anwendungsdaten

- `/home` - Enthält persönliche Verzeichnisse für jeden Benutzer. Hier speichern Sie Ihre Dokumente, Anwendungseinstellungen und andere persönliche Dateien.
- `/root` - Das Home-Verzeichnis für den Root-Benutzer, getrennt vom `/home`-Verzeichnis, um sicherzustellen, dass sich der Root-Benutzer anmelden kann, selbst wenn `/home` nicht verfügbar ist.
- `/opt` - Reserviert für optionale oder Drittanbieter-Anwendungssoftwarepakete.
- `/usr` - Dieses Verzeichnis enthält benutzerinstallierte Software und Dienstprogramme. Trotz seines Namens enthält es im Allgemeinen keine Home-Dateien einzelner Benutzer. Es verfügt über eine eigene Unterverzeichnisstruktur, wie z. B. `/usr/bin` für nicht wesentliche Benutzer-Binärdateien und `/usr/local` für aus der Quelle kompilierte Software.

### Dynamische und temporäre Daten

- `/var` - Steht für „variabel“ und speichert Dateien, deren Größe und Inhalt sich voraussichtlich ändern werden, wie z. B. Systemprotokolle (`/var/log`), Caches und Spool-Dateien.
- `/tmp` - Ein für alle beschreibbarer Bereich zur Speicherung temporärer Dateien. Dateien in diesem Verzeichnis werden oft beim Neustart des Systems gelöscht.
- `/run` - Enthält Informationen über das laufende System seit dem letzten Start, wie z. B. Prozess-IDs (PIDs) und andere Laufzeitdaten.

### Geräte- und Einhängepunkte

- `/dev` - Enthält spezielle Gerätedateien, die Hardwarekomponenten wie Festplatten, Terminals und Eingabegeräte darstellen.
- `/media` - Ein Standard-Einhängepunkt für Wechselmedien wie USB-Sticks, SD-Karten und CD-ROMs.
- `/mnt` - Ein generischer Einhängepunkt zum temporären Einhängen von Dateisystemen.

### Systeminformationen

- `/proc` - Ein virtuelles Dateisystem, das Echtzeitinformationen über aktuell laufende Prozesse und Kernelparameter bereitstellt.
- `/srv` - Vorgesehen für standortspezifische Daten, die vom System bereitgestellt werden, wie z. B. Dateien für einen Webserver.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis des Linux-Dateisystems zu festigen:

1. **[Navigieren im Dateisystem unter Linux](https://labex.io/de/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Üben Sie die Verwendung wesentlicher Shell-Befehle wie `pwd`, `cd` und `ls`, um zwischen Verzeichnissen zu wechseln und das Dateisystem zu erkunden.
2. **[Dateien und Verzeichnisse unter Linux verwalten](https://labex.io/de/labs/comptia-manage-files-and-directories-in-linux-590835)** - Lernen Sie, wie man Dateien und Verzeichnisse erstellt, entfernt, kopiert und verschiebt, und verstehen Sie symbolische und harte Links.
3. **[Dateien und Befehle unter Linux finden](https://labex.io/de/labs/comptia-find-files-and-commands-in-linux-590834)** - Meistern Sie Techniken zum Auffinden von Dateien und Befehlen mit `find`, `locate`, `whereis`, `which` und `type`.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Verwaltung des Linux-Dateisystems aufzubauen.

## Quiz Question

Welches Verzeichnis wird zur Speicherung von Protokollen (Logs) verwendet? (Bitte geben Sie den vollständigen Pfad an. Die Antwort ist groß-/kleingeschrieben und muss in Englisch sein.)

## Quiz Answer

/var
