---
lesson_id: "kernel-installation"
course_id: "kernel"
lang: "de"
order_index: 4
title: "Kernelinstallation"
description: "Erfahre, wie du einen Distributionskernel mit einem getesteten Fallback installierst, startest, überprüfst und beibehältst."
meta_title: "Kernelinstallation – Kernel"
meta_description: "Erfahre, wie du Linux-Kernel installierst und verwaltest. Entdecke Kernelversionen und die Verwendung von `uname -r` sowie apt-Befehlen. Beginne deine Reise durch den Linux-Kernel!"
meta_keywords: "Linux-Kernel, Kernel installieren, uname -r, apt dist-upgrade, Kernelverwaltung, Linux-Tutorial, Linux für Einsteiger, Linux-Leitfaden"
---

Distributionen paketieren Kernel zusammen mit Modulen, initramfs-Integration, Bootloader-Aktualisierungen, Signaturen und Supportrichtlinien. Verwende diesen verwalteten Arbeitsablauf, sofern du nicht bewusst einen eigenen Kernel entwickelst oder testest und den Computer wiederherstellen kannst.

## Laufende und installierte Kernel

Zeige die Veröffentlichung des derzeit laufenden Kernels an:

```bash
$ uname -r
6.8.0-00-generic
```

Dies listet weder jeden installierten Kernel auf noch ändert es sich unmittelbar, wenn ein neueres Paket installiert wird. Das System muss das neue Abbild starten, bevor `uname -r` es meldet. Frage installierte Pakete und Starteinträge mit den Werkzeugen der jeweiligen Distribution ab.

:::single-choice{#kernel-installation-uname-release} Was zeigt `uname -r` an?

::option[Die Veröffentlichungszeichenfolge des derzeit laufenden Kernels.]{#kernel-installation-running-release .correct explanation="Der Befehl meldet den aktiven Kernelzustand und nicht bloß das neueste auf dem Datenträger gespeicherte Abbild."}
::option[Jedes in allen Paketquellen verfügbare Kernelpaket.]{#kernel-installation-all-packages explanation="Der Bestand einer Paketquelle gehört zur Paketverwaltung."}
::option[Die Firmwareversion jedes angeschlossenen Geräts.]{#kernel-installation-device-firmware explanation="Kernelveröffentlichung und Gerätefirmwarebestände sind unterschiedliche Daten."}
:::

## Das Tracking-Paket der Distribution bevorzugen

Installiere oder behalte das unterstützte Kernel-Tracking- oder Metapaket der Distribution, damit zukünftige Sicherheitsaktualisierungen weiterhin eintreffen. Paketnamen hängen von Veröffentlichung, Architektur, Hardwareklasse und Kernelvariante ab. Ubuntu bietet beispielsweise häufig `linux-generic` an, doch Cloud-, Low-Latency-, HWE-, OEM-, Echtzeit- und architekturspezifische Systeme verwenden andere Pakete.

Verwandle eine Versionszeichenfolge aus `uname -r` nicht unmittelbar in einen Operanden für `apt install` und gehe nicht davon aus, dass er gültig ist. Lies die aktuelle Dokumentation der Distribution und prüfe Kandidaten vor der Installation mit der Paketverwaltung.

:::single-choice{#kernel-installation-meta-package} Warum ist ein unterstütztes Kernel-Metapaket nützlich?

::option[Es garantiert, dass niemals ein Neustart erforderlich ist.]{#kernel-installation-no-reboot explanation="Ein neu installierter Kernel wird erst nach dem Start dieses Kernels aktiv, abgesehen vom begrenzten Umfang spezieller Live-Patches."}
::option[Es wandelt jeden externen Treiber in fest eingebauten Code um.]{#kernel-installation-convert-drivers explanation="Externe Module benötigen weiterhin kompatible Builds und Signaturen."}
::option[Es verfolgt die von der Distribution vorgesehene Folge von Kernelaktualisierungen.]{#kernel-installation-update-tracking .correct explanation="Abhängigkeiten verschieben das System auf neuere unterstützte Abbild- und Modulpakete, sobald Aktualisierungen veröffentlicht werden."}
:::

## Die Änderung vorbereiten

Vor einer Kerneltransaktion:

1. Bestätige unterstützte Paketquellen, Paketsignaturen, den Veröffentlichungslebenszyklus und die beabsichtigte Kernelvariante.
2. Stelle sicher, dass `/boot` oder die EFI-Systempartition genügend Platz besitzt.
3. Bewahre mindestens einen bekanntermaßen funktionierenden installierten Kernel und einen auswählbaren Starteintrag auf.
4. Überprüfe den Zugriff auf Konsole, Fernverwaltung, Rettungsmedium, Verschlüsselungswiederherstellung und Rollback.
5. Prüfe externe Module, Speicher- und Netzwerktreiber, Secure-Boot-Signaturen, Ruhezustand und Virtualisierungskompatibilität.

Die Pakettransaktion sollte durch Distributions-Hooks ein passendes initramfs erzeugen und Starteinträge aktualisieren. Lies jeden Fehler; ein als installiert markiertes Paket reicht nicht aus, wenn die Erzeugung von initramfs oder Bootloader-Einträgen fehlgeschlagen ist.

:::single-choice{#kernel-installation-initramfs-error} Warum muss ein Fehler bei der initramfs-Erzeugung die Annahme eines Erfolgs verhindern?

::option[Die initramfs-Erzeugung ändert das Shell-Passwort des Benutzers.]{#kernel-installation-initramfs-password explanation="Der Arbeitsablauf für das Bootarchiv hat nichts mit Authentifizierungsgeheimnissen von Konten zu tun."}
::option[Dem neuen Kernel können frühe Module oder Werkzeuge fehlen, die zum Erreichen des Root-Speichers erforderlich sind.]{#kernel-installation-missing-early-tools .correct explanation="Ein Abbild kann installiert sein, während sein erforderliches frühes User-Space-Artefakt fehlt oder veraltet ist."}
::option[Der Fehler beweist, dass der derzeit laufende Kernel bereits angehalten wurde.]{#kernel-installation-current-stopped explanation="Paket-Hooks laufen, während der alte Kernel aktiv bleiben kann."}
:::

## Starten und validieren

Plane einen kontrollierten Neustart unter Berücksichtigung von Beteiligten und aktiven Arbeitslasten. Stelle sicher, dass an der Konsole der ältere Eintrag ausgewählt werden kann, falls der Standardstart fehlschlägt. Nach dem Start:

```bash
$ uname -r
$ journalctl -k -b
$ systemctl --failed
```

Verwende auf Systemen ohne systemd gleichwertige Werkzeuge. Validiere Speicher, Dateisysteme, Netzwerk, Grafik, Eingabe, Sicherheitsmodule, externe Module, Container, virtuelle Maschinen und den Zustand der Anwendungen. Eine Anmeldeaufforderung allein ist keine vollständige Validierung.

:::single-choice{#kernel-installation-activation} Wann wird ein neu installiertes gewöhnliches Kernelpaket zum laufenden Kernel?

::option[Sobald `uname -r` eingegeben wird.]{#kernel-installation-uname-activates explanation="Uname ist schreibgeschützt und kann keine Kernel wechseln."}
::option[Nachdem der Computer dieses Kernelabbild gestartet hat.]{#kernel-installation-after-boot .correct explanation="Die Installation von Dateien ersetzt nicht den bereits im Speicher ausgeführten Kernel."}
::option[Wenn das Paketarchiv heruntergeladen wurde, aber noch vor der Installation.]{#kernel-installation-download-activates explanation="Ein heruntergeladenes Archiv hat keine Auswirkung auf die aktive Ausführung."}
:::

## Ältere Kernel entfernen

Verwende den unterstützten Bereinigungsablauf der Paketverwaltung erst, nachdem der neue Kernel die Validierung bestanden hat. Entferne niemals den derzeit laufenden Kernel, den einzigen bekanntermaßen funktionierenden Fallback oder Pakete, die vom aktiven Tracking-Paket benötigt werden. Prüfe die genaue vorgeschlagene Entfernung und die resultierenden Starteinträge.

Das manuelle Löschen aus `/boot` hinterlässt Paket- und Bootloaderzustand inkonsistent. Wenn der Speicherplatz bereits erschöpft ist, erstelle vor Dateiänderungen einen Wiederherstellungsplan, statt beliebige Abbilder zu löschen.

:::single-choice{#kernel-installation-old-kernel-removal} Welcher Kernel sollte während der ersten Validierung eines neuen Kernels installiert bleiben?

::option[Ausschließlich der ungetestete neue Kernel.]{#kernel-installation-only-new explanation="Das Entfernen aller Fallbacks vor dem Test verwandelt ein Kompatibilitätsproblem in einen Wiederherstellungsvorfall."}
::option[Überhaupt keine Kerneldateien unter dem Bootpfad.]{#kernel-installation-no-kernels explanation="Der Computer benötigt ein ladbares Kernelartefakt, um Linux zu starten."}
::option[Ein bekanntermaßen funktionierender, vom Bootloader auswählbarer Fallback.]{#kernel-installation-known-good-fallback .correct explanation="Der Fallback bietet einen Wiederherstellungsweg, wenn der neue Kernel auf der Hardware oder mit Arbeitslasten fehlschlägt."}
:::

Das Lab [Das GRUB2-Startmenü anpassen](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859) bietet eine wiederherstellungssichere Umgebung zum Verständnis mehrerer Einträge.

## Zusammenfassung

Du kannst eine Kernelaktualisierung nun als Änderung der Startkette und Kompatibilität behandeln.

1. Unterscheide die laufende Veröffentlichung von installierten Abbildern.
2. Verfolge unterstützte Aktualisierungen über das richtige Distributionspaket.
3. Prüfe Speicherplatz, initramfs, Signaturen, Module und Wiederherstellungszugriff vorab.
4. Starte und validiere das Verhalten von Hardware und Anwendungen.
5. Bewahre einen bekanntermaßen funktionierenden Fallback, bis der neue Kernel erprobt ist.
