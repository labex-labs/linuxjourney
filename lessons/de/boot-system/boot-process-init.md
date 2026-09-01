---
lesson_id: "boot-process-init"
course_id: "boot-system"
lang: "de"
order_index: 5
title: "Bootvorgang: Init"
description: "Lerne, wie PID 1 den Userspace initialisiert, Dienste überwacht, Kindprozesse aufräumt und das Herunterfahren koordiniert."
meta_title: "Bootvorgang: Init – Systemstart"
meta_description: "Lerne die Rolle von PID 1 und verschiedene Linux-Init-Systeme wie System V init, Upstart und systemd sowie ihre Dienstverwaltung kennen."
meta_keywords: "Linux init, systemd, System V init, Upstart, Linux Bootvorgang, PID 1, Linux Tutorial, Linux Anleitung"
---

Der Kernel startet den ersten Userspace-Prozess mit PID 1 in einem PID-Namespace. Auf einem vollständigen Linux-System richtet dieser Init-Prozess die Dienstumgebung ein. In einem Container kann PID 1 stattdessen ein kleiner Init-Wrapper oder die Anwendung selbst sein, trägt aber weiterhin besondere Verantwortung für Signale und das Aufräumen von Kindprozessen.

## Aufgaben von PID 1

Ein Init-System übernimmt häufig folgende Aufgaben:

- Dienste, Anmeldungen, Einhängungen und andere Arbeitseinheiten starten und überwachen
- Arbeit anhand von Abhängigkeiten und dem konfigurierten Zielzustand anordnen
- verwaiste Kindprozesse übernehmen und aufräumen
- gemäß einer Richtlinie auf Dienstausfälle reagieren
- geordnetes Herunterfahren und Neustarten koordinieren

Die genaue Abgrenzung unterscheidet sich. Geräteverwaltung, Netzwerk, Protokollierung und geplante Aufgaben können getrennte, von Init überwachte Programme sein, statt direkt in PID 1 eingebaut zu sein.

:::single-choice{#boot-init-pid-one-role} Welche Aufgabe ist für PID 1 in seinem PID-Namespace besonders?

::option[Bei jedem Start alle Anwendungen aus dem Quellcode kompilieren.]{#boot-init-compile-apps explanation="Beim normalen Dienststart werden installierte Programme verwendet, statt sämtliche Software neu zu bauen."}
::option[Die physische Sektorgröße des Datenträgers festlegen.]{#boot-init-sector-size explanation="Speicherhardware und Treiber stellen die Sektorgeometrie bereit, bevor Init Dienste verwaltet."}
::option[Verwaiste Kindprozesse übernehmen und aufräumen.]{#boot-init-reap-orphans .correct explanation="PID 1 ist der letztliche Elternprozess und muss den Beendigungsstatus einsammeln, damit sich keine Zombie-Einträge ansammeln."}
:::

## System V init und Runlevel

Das traditionelle sysvinit verwendet Konfigurationen wie `/etc/inittab` sowie runlevelspezifische Start- und Stoppskripte. Ein Runlevel steht für einen Betriebsmodus, wobei sich die Bedeutung nummerierter Level zwischen Distributionen unterscheiden kann. Die Reihenfolge der Skripte folgt Konventionen und kann durch Distributionswerkzeuge erweitert oder parallelisiert werden.

Schließe nicht allein aus der Existenz von `/etc/init.d/` auf das aktive Init-System eines Hosts. Kompatibilitätsskripte können auf Systemen erhalten bleiben, deren PID 1 eine andere Implementierung ist.

:::single-choice{#boot-init-sysv-runlevel} Wofür steht ein System-V-Runlevel?

::option[Für eine vom Bootloader ausgewählte Kernel-Version.]{#boot-init-runlevel-kernel explanation="Die Auswahl des Kernels ist Aufgabe des Bootloaders und wird nicht durch einen Init-Runlevel codiert."}
::option[Für einen konfigurierten Betriebsmodus, der mit Dienstaktionen verbunden ist.]{#boot-init-runlevel-mode .correct explanation="SysV-Aufbauten ordnen den Leveln Gruppen und Reihenfolgen von Start- oder Stoppskripten zu."}
::option[Für den aktuellen prozentualen Verbrauch von Inodes in einem Dateisystem.]{#boot-init-runlevel-inodes explanation="Die Kapazität von Dateisystemmetadaten steht in keinem Zusammenhang mit Betriebsmodi für Dienste."}
:::

## Ereignis- und abhängigkeitsbasierte Systeme

Upstart führte ein ereignisgesteuertes Jobmodell ein und wurde von älteren Ubuntu-Versionen sowie einigen anderen Systemen verwendet. Heute ist es hauptsächlich historisch oder für den Betrieb älterer Systeme relevant.

systemd wird von vielen aktuellen Allzweckdistributionen eingesetzt. Es bildet Dienste, Sockets, Einhängungen, Timer, Geräte, Targets und andere Ressourcen als Units ab. Deklarative Abhängigkeiten und Aktivierungsmechanismen lassen unabhängige Arbeit gleichzeitig ablaufen und bewahren dabei die erforderliche Reihenfolge.

Weitere aktive Init- und Überwachungsansätze sind OpenRC, runit, s6 und BusyBox init. „Am neuesten“ ist keine sinnvolle Kompatibilitätsregel. Ermittle, was das konkrete System ausführt, und verwende dessen Dokumentation.

:::single-choice{#boot-init-systemd-unit-model} Wie stellt systemd verwaltete Ressourcen wie Dienste und Einhängungen dar?

::option[Als primäre Partitionseinträge eines MBR.]{#boot-init-systemd-partitions explanation="Partitionsmetadaten von Datenträgern stehen in keinem Zusammenhang mit Units des Dienstmanagers."}
::option[Ausschließlich als Hardlinks auf die ausführbare Datei von PID 1.]{#boot-init-systemd-hard-links explanation="Units sind Konfigurations- und Laufzeitobjekte und nicht lediglich Inode-Aliasse."}
::option[Als Units mit Abhängigkeiten und Aktivierungsbeziehungen.]{#boot-init-systemd-units .correct explanation="Unit-Typen bieten ein gemeinsames Modell für Reihenfolge, Zustand und Überwachung."}
:::

## Das laufende Init-System bestimmen

Prüfe PID 1, statt anhand installierter Dateien zu raten:

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
```

Berechtigungen, Container und Namespaces beeinflussen, was du siehst. Ein in einem Container ausgeführter Befehl zeigt PID 1 dieses Namespace und nicht zwangsläufig das Init-System des Hosts. Verwende nach der Bestimmung dessen eigene Status- und Protokollwerkzeuge, statt Befehle verschiedener Init-Familien zu vermischen.

:::single-choice{#boot-init-detect-running} Warum ist die Prüfung von PID 1 aussagekräftiger als die Suche nach einem Verzeichnis mit älteren Skripten?

::option[PID 1 besitzt auf jedem Linux-System immer denselben Namen der ausführbaren Datei.]{#boot-init-same-name explanation="systemd, sysvinit, BusyBox, Container-Init-Programme und weitere Implementierungen können PID 1 belegen."}
::option[Kompatibilitätsdateien können vorhanden sein, obwohl eine andere Init-Implementierung läuft.]{#boot-init-compatibility-files .correct explanation="Die tatsächlich als PID 1 laufende Datei ist ein stärkerer Beleg für das aktive Init-System."}
::option[Ältere Verzeichnisse werden bei jedem Systemstart automatisch gelöscht.]{#boot-init-directories-deleted explanation="Installierte Kompatibilitätsdateien können über viele Systemstarts hinweg erhalten bleiben."}
:::

## Zusammenfassung

Du kannst Init nun als Rolle erklären, statt es mit einer zwingenden Implementierung gleichzusetzen.

1. Ordne PID 1 die Dienstinitialisierung, das Aufräumen von Kindprozessen und das Herunterfahren zu.
2. Erkenne System-V-Runlevel als von der Distribution definierte Betriebsmodi.
3. Ordne systemd-Ressourcen und -Abhängigkeiten Units zu.
4. Prüfe vor der Auswahl von Werkzeugen die tatsächlich laufende PID 1 im relevanten Namespace.
