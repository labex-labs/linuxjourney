---
lesson_id: "sysv-overview"
course_id: "init"
lang: "de"
order_index: 1
title: "Überblick über System V"
description: "Erfahre, wie das traditionelle System-V-init Runlevel und geordnete Links zu Dienstskripten verwendet."
meta_title: "Überblick über System V – Init"
meta_description: "Erkunde das traditionelle System-V-init-System, auch SysV oder init v genannt. Dieser Leitfaden behandelt, wie systemv Prozesse verwaltet, seinen sequenziellen Start und die Rolle von Runleveln unter Linux. Lerne die Grundlagen des klassischen initv-Prozesses kennen."
meta_keywords: "System V, systemv, SysV init, systemv init, init v, initv, Linux-Runlevel, init-System, Prozessverwaltung, Linux-Tutorial"
---

System-V-init, gewöhnlich SysV init oder sysvinit genannt, ist ein traditioneller Entwurf für PID 1 und den Dienststart. Er bleibt auf älteren Systemen und durch Kompatibilitätsskripte wichtig. Installierte Dateien im SysV-Stil beweisen jedoch nicht, dass sysvinit als PID 1 läuft.

## Das aktive init-System erkennen

Prüfe die laufende PID 1:

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
```

Eine Datei `/etc/inittab` oder ein Verzeichnis `/etc/init.d/` ist nur ein unterstützender Hinweis. systemd und andere init-Systeme können diese Dateien aus Kompatibilitätsgründen behalten, und Container können einen anderen PID-Namensraum als der Host anzeigen.

:::single-choice{#sysv-overview-detection}
Was ist der stärkste Beleg dafür, dass sysvinit aktiv ist?

::option[Die ausführbare Datei der laufenden PID 1 ist sysvinit oder dessen init-Programm.]{#sysv-overview-live-pid-one .correct explanation="Die Prüfung des laufenden ersten Prozesses ist unmittelbarer als eine Schlussfolgerung aus Kompatibilitätsdateien."}
::option[Ein Verzeichnis `/etc/init.d/` ist vorhanden.]{#sysv-overview-init-d-only explanation="Andere init-Systeme bewahren SysV-Skripte oder Wrapper häufig auf."}
::option[Eine Paketbeschreibung enthält das Wort service.]{#sysv-overview-package-word explanation="Pakettext bestimmt nicht den Prozess, der derzeit als PID 1 arbeitet."}
:::

## Runlevel

Ein Runlevel ist ein benannter numerischer Betriebsmodus. SysV-Konfigurationen verwenden traditionell die Level `0` bis `6` und besondere Level, ihre Bedeutungen sind jedoch Distributionsrichtlinien und kein universelles Gesetz. Verbreitete Konventionen sind:

- `0`: Übergang zum Anhalten oder Ausschalten
- `1` oder `S`: Einzelbenutzer- oder Rettungsmodus
- `2` bis `5`: von der Distribution definierte Mehrbenutzermodi
- `6`: Übergang zum Neustart

Systeme der Debian-Familie behandeln die Level 2–5 historisch ähnlich, während Konventionen der Red-Hat-Familie Text- und Grafikmodi unterscheiden. Prüfe auf dem tatsächlichen Host `/etc/inittab`, die init-Dokumentation und Runlevel-Verzeichnisse.

:::single-choice{#sysv-overview-shutdown-runlevel}
Welches Runlevel fordert auf vielen SysV-Systemen konventionsgemäß das Anhalten oder Ausschalten an?

::option[`3`]{#sysv-overview-runlevel-three explanation="Dies ist gewöhnlich ein Mehrbenutzer-Betriebsmodus und kein Herunterfahren."}
::option[`0`]{#sysv-overview-runlevel-zero .correct explanation="Level null ist konventionsgemäß der Übergang zum Herunterfahren, auch wenn die lokale init-Richtlinie maßgeblich bleibt."}
::option[`6`]{#sysv-overview-runlevel-six explanation="Level sechs fordert konventionsgemäß einen Neustart an."}
:::

## Init-Skripte und Runlevel-Links

Dienstskripte befinden sich gewöhnlich unter `/etc/init.d/`. Runlevel-Verzeichnisse wie `/etc/rc2.d/` oder `/etc/rc.d/rc2.d/` enthalten Links, deren Namen Übergangsaktion und Reihenfolge codieren:

- Links `SNNname` fordern eine Startaktion an.
- Links `KNNname` fordern eine Stoppaktion an.
- `NN` legt die lexikografische Reihenfolge der Links für diesen Übergang fest.

Der genaue Algorithmus und die Verzeichnisse unterscheiden sich. Abhängigkeiten können außerdem in Skriptköpfen ausgedrückt und von Distributionswerkzeugen verarbeitet werden, und einige Implementierungen parallelisieren Arbeit. SysV sollte nicht auf eine Garantie reduziert werden, dass jeder Dienst streng nacheinander startet.

:::single-choice{#sysv-overview-start-link}
Was fordert ein Link `S20networking` beim Eintritt in ein Runlevel konventionsgemäß an?

::option[Signal 20 unmittelbar an jeden Netzwerkprozess zu senden.]{#sysv-overview-signal-twenty explanation="Die Ziffern sind Reihenfolgemetadaten und keine Signalnummer."}
::option[Zwanzig Sicherungen der Netzwerkkonfiguration zu speichern.]{#sysv-overview-twenty-backups explanation="Runlevel-Links stellen keine Sicherungsaufbewahrung bereit."}
::option[Das verknüpfte Dienstskript mit seiner Startaktion in der `S`-Reihenfolge auszuführen.]{#sysv-overview-start-action .correct explanation="Das Präfix kennzeichnet Startlinks, während die Zahl zur Reihenfolge beiträgt."}
:::

## Zwischen Runleveln wechseln

Wenn init das Runlevel wechselt, stoppt die rc-Logik der Distribution nicht mehr benötigte Dienste und startet die im neuen Modus erforderlichen Dienste. Skripte müssen hinreichend idempotent sein, um wiederholte Status- oder Übergangsvorgänge zu verarbeiten und aussagekräftige Statuswerte zurückzugeben.

Die Anforderung von Runlevel 0 oder 6 ist eine systemweite destruktive Verfügbarkeitsaktion. Verwende die Schnittstelle des Systems zum Herunterfahren, benachrichtige Benutzer, sichere aktive Arbeit und überprüfe den Zugriff auf die Fernkonsole, statt rohe init-Übergänge beiläufig aufzurufen.

:::single-choice{#sysv-overview-runlevel-six-meaning}
Was fordert Runlevel `6` konventionsgemäß an?

::option[Die Erstellung von sechs zusätzlichen Benutzerkonten.]{#sysv-overview-six-users explanation="Runlevel beschreiben Betriebsmodi und keine Kontoanzahlen."}
::option[Einen Übergang zum Systemneustart.]{#sysv-overview-reboot .correct explanation="Die klassische SysV-Richtlinie reserviert Level sechs zum Stoppen von Diensten und Neustarten des Systems."}
::option[Alle Dateisysteme dauerhaft schreibgeschützt einzuhängen.]{#sysv-overview-six-readonly explanation="Dies ist nicht der konventionelle Zweck von Runlevel sechs."}
:::

## Grenzen der Kompatibilität

Auf einem systemd-Host können SysV-Skripte als erzeugte Units eingebunden werden, doch Abhängigkeiten, Zeitüberschreitungen, Protokollierung und Zustandssemantik von systemd gelten weiterhin. Die unmittelbare Ausführung eines älteren Skripts kann die Verfolgung des Dienstmanagers umgehen. Bestimme den aktiven Manager und verwende nach Möglichkeit seine native Schnittstelle.

:::single-choice{#sysv-overview-compatibility-script}
Warum sollte ein Skript im SysV-Stil auf einem systemd-Host gewöhnlich über den Dienstmanager aufgerufen werden?

::option[Die direkte Ausführung kann Abhängigkeits- und Zustandsverfolgung umgehen.]{#sysv-overview-manager-tracking .correct explanation="Der Manager muss Prozesseigentum, Reihenfolge, Zeitüberschreitungen und Status koordinieren."}
::option[Shell-Skripte können auf einem systemd-System nicht ausgeführt werden.]{#sysv-overview-scripts-impossible explanation="Sie können ausgeführt werden, doch die Umgehung der Überwachung kann einen inkonsistenten Zustand erzeugen."}
::option[Systemd wandelt jedes Dienstskript in ein Kernelmodul um.]{#sysv-overview-script-module explanation="Kompatibilitäts-Units bleiben Dienstverwaltung im User-Space."}
:::

## Zusammenfassung

Du kannst nun ein traditionelles SysV-Layout interpretieren, ohne anzunehmen, dass es aktiv ist.

1. Bestimme die laufende PID 1, bevor du init-Befehle auswählst.
2. Behandle Runlevel-Bedeutungen als von der Distribution definierte Konventionen.
3. Lies `S`, `K` und die numerische Reihenfolge in Runlevel-Links.
4. Verwende kontrollierte Verfahren zum Herunterfahren für die Level 0 und 6.
5. Respektiere den aktiven Manager, wenn Kompatibilitätsskripte vorhanden sind.
