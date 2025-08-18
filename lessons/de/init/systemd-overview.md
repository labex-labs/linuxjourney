---
lang: "de"
title: "Systemd Überblick"
meta_title: "Systemd Überblick - Init"
meta_description: "Lernen Sie die Grundlagen von Systemd: Verstehen Sie Units, Targets und den Boot-Prozess. Entdecken Sie, wie Systemd Dienste und Systemzustände in Linux verwaltet. Beginnen Sie Ihre Reise!"
meta_keywords: "Systemd, Systemd Units, Systemd Targets, Linux Boot-Prozess, Linux Dienste, Anfänger, Tutorial, Anleitung"
---

## Lesson Content

Systemd entwickelt sich langsam zum aufkommenden Standard für init. Wenn Sie ein Verzeichnis `/usr/lib/systemd` haben, verwenden Sie höchstwahrscheinlich systemd.

Systemd verwendet Ziele, um Ihr System zum Laufen zu bringen. Grundsätzlich haben Sie ein Ziel, das Sie erreichen möchten, und dieses Ziel hat auch Abhängigkeiten, die erfüllt werden müssen. Systemd ist extrem flexibel und robust; es folgt keiner strengen Reihenfolge, um Prozesse zu starten. Hier ist, was während eines typischen systemd-Boots passiert:

1. Zuerst lädt systemd seine Konfigurationsdateien, die sich normalerweise in `/etc/systemd/system` oder `/usr/lib/systemd/system` befinden.
2. Dann bestimmt es sein Boot-Ziel, das normalerweise `default.target` ist.
3. Systemd ermittelt die Abhängigkeiten des Boot-Ziels und aktiviert sie.

Ähnlich wie SysV-Runlevels bootet systemd in verschiedene Ziele:

- `poweroff.target` - System herunterfahren
- `rescue.target` - Einzelbenutzermodus
- `multi-user.target` - Mehrbenutzer mit Netzwerk
- `graphical.target` - Mehrbenutzer mit Netzwerk und GUI
- `reboot.target` - Neustart

Das Standard-Boot-Ziel von `default.target` verweist normalerweise auf das `graphical.target`.

Die Hauptobjekte, mit denen systemd arbeitet, werden als Units bezeichnet. Systemd stoppt und startet nicht nur Dienste; es kann Dateisysteme mounten, Ihre Netzwerk-Sockets überwachen usw. Aufgrund dieser Robustheit hat es verschiedene Arten von Units, mit denen es arbeitet. Die häufigsten Units sind:

- Service units - dies sind die Dienste, die wir gestartet und gestoppt haben; diese Unit-Dateien enden mit `.service`.
- Mount units - Diese mounten Dateisysteme; diese Unit-Dateien enden mit `.mount`.
- Target units - Diese gruppieren andere Units; die Dateien enden mit `.target`.

Nehmen wir zum Beispiel an, wir booten in unser `default.target`. Dieses Ziel gruppiert die Unit `networking.service`, die Unit `crond.service` usw., so dass, sobald wir eine einzelne Unit aktivieren, alles, was unter dieser Unit liegt, ebenfalls aktiviert wird.

## Exercise

No exercises for this lesson.

## Quiz Question

Welche Unit wird verwendet, um andere Units zu gruppieren?

## Quiz Answer

target
