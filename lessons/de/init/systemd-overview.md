---
index: 5
lang: "de"
title: "Systemd-Übersicht"
meta_title: "Systemd-Übersicht - Init"
meta_description: "Lernen Sie die Grundlagen von Systemd kennen: Verstehen Sie Units, Targets und den Boot-Prozess. Entdecken Sie, wie Systemd Dienste und Systemzustände unter Linux verwaltet. Beginnen Sie Ihre Reise!"
meta_keywords: "Systemd, Systemd Units, Systemd Targets, Linux Boot-Prozess, Linux Dienste, Anfänger, Tutorial, Leitfaden"
---

## Lesson Content

Systemd ist das Standard-Init-System in den meisten modernen Linux-Distributionen. Wenn Sie ein Verzeichnis `/usr/lib/systemd` haben, verwenden Sie höchstwahrscheinlich systemd.

Systemd verwendet Ziele (Goals), um Ihr System hochzufahren und betriebsbereit zu machen. Im Grunde haben Sie ein Ziel, das Sie erreichen möchten, und dieses Ziel hat auch Abhängigkeiten, die erfüllt werden müssen. Systemd ist extrem flexibel und robust; es folgt keiner strengen Reihenfolge, um Prozesse zu starten. Hier ist, was während eines typischen Systemd-Boots passiert:

1. Zuerst lädt systemd seine Konfigurationsdateien, die sich normalerweise unter `/etc/systemd/system` oder `/usr/lib/systemd/system` befinden.
2. Dann bestimmt es sein Boot-Ziel (Boot Goal), welches normalerweise `default.target` ist.
3. Systemd ermittelt die Abhängigkeiten des Boot-Ziels und aktiviert sie.

Ähnlich wie bei SysV-Runlevels bootet systemd in verschiedene Targets:

- `poweroff.target` - System herunterfahren
- `rescue.target` - Einzelbenutzermodus
- `multi-user.target` - Mehrbenutzerbetrieb mit Netzwerk
- `graphical.target` - Mehrbenutzerbetrieb mit Netzwerk und GUI
- `reboot.target` - Neustart

Das Standard-Boot-Ziel `default.target` verweist normalerweise auf das `graphical.target`.

Die Hauptobjekte, mit denen systemd arbeitet, sind als Units bekannt. Systemd stoppt und startet nicht nur Dienste; es kann Dateisysteme einbinden, Ihre Netzwerksockets überwachen usw. Aufgrund dieser Robustheit gibt es verschiedene Arten von Units, mit denen es arbeitet. Die gebräuchlichsten Units sind:

- Service units - Dies sind die Dienste, die wir gestartet und gestoppt haben; diese Unit-Dateien enden mit `.service`.
- Mount units - Diese binden Dateisysteme ein; diese Unit-Dateien enden mit `.mount`.
- Target units - Diese gruppieren andere Units; die Dateien enden mit `.target`.

Nehmen wir zum Beispiel an, wir booten in unser `default.target`. Dieses Target gruppiert die Unit `networking.service`, die Unit `crond.service` usw., sodass sobald wir eine einzelne Unit aktivieren, alles unterhalb dieser Unit ebenfalls aktiviert wird.

## Exercise

Obwohl es für dieses Thema keine spezifischen Übungen gibt, empfehlen wir Ihnen, den umfassenden [Linux Lernpfad](https://labex.io/de/learn/linux) zu erkunden, um verwandte Linux-Fähigkeiten und Konzepte zu üben.

## Quiz Question

Welche Unit wird verwendet, um andere Units zu gruppieren?

## Quiz Answer

target
