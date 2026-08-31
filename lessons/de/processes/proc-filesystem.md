---
lesson_id: "proc-filesystem"
course_id: "processes"
lang: "de"
order_index: 10
title: "/proc-Dateisystem"
description: "Erfahre, wie Linux aktive Prozess- und Kernelinformationen über das virtuelle Dateisystem `/proc` bereitstellt."
meta_title: "/proc-Dateisystem – Prozesse"
meta_description: "Entdecke das Linux-Dateisystem /proc, ein virtuelles Verzeichnis, das eine Dashboard-ähnliche Sicht auf den Kernel und laufende Prozesse bietet. Erfahre, wie du über Standardbefehle hinaus zusätzliche Prozessdetails abrufst."
meta_keywords: "/proc-Dateisystem, Linux proc, Prozessinformationen, zusätzliche Linux-proc-Daten, System-Dashboard, Linux-Prozesse, Kernelinformationen"
---

Linux hängt `procfs` gewöhnlich unter `/proc` ein. Dieses virtuelle Dateisystem stellt vom Kernel erzeugte Schnittstellen als Dateien und Verzeichnisse dar; seine Inhalte sind keine gewöhnlichen dauerhaften Dateien auf einem Datenträger. Es stellt sowohl Prozesszustände als auch ausgewählte systemweite Kernelinformationen bereit.

## Prozessverzeichnisse finden

Zeige den Einhängepunkt und die Einträge der obersten Ebene an mit:

```bash
$ findmnt /proc
$ ls /proc
```

Numerische Verzeichnisnamen entsprechen den im PID-Namensraum des Aufrufers sichtbaren Prozess-IDs. `/proc/12345` repräsentiert beispielsweise die PID 12345, solange sie existiert. `/proc/self` ist ein symbolischer Link, der auf das eigene Verzeichnis des beobachtenden Prozesses verweist, und `/proc/thread-self` bezeichnet den aktuellen Thread.

Sichtbarkeit und Zugriff hängen von Zugangsdaten, Namensräumen, Sicherheitsrichtlinien und procfs-Einhängeoptionen wie `hidepid` ab. Ein Prozess kann sich zwischen dem Auflisten eines Verzeichnisses und dem Öffnen einer seiner Dateien beenden. Dieses Verschwinden ist ein normales Rennen, mit dem Inspektionswerkzeuge umgehen müssen.

:::single-choice{#proc-filesystem-numeric-directory}
Was repräsentiert das numerische Verzeichnis `/proc/12345` gewöhnlich?

::option[Den Datenträgerblock mit der Nummer 12345.]{#proc-filesystem-disk-block explanation="`/proc` ist eine virtuelle Kernel-Schnittstelle und kein Verzeichnis aus Rohdatenblöcken eines Datenträgers."}
::option[Den derzeit sichtbaren Prozess mit PID 12345.]{#proc-filesystem-pid-directory .correct explanation="Prozessbezogene procfs-Daten sind in einem Verzeichnis zusammengefasst, dessen Name der sichtbaren PID entspricht."}
::option[Das Benutzerkonto mit der UID 12345.]{#proc-filesystem-user-directory explanation="Die numerischen Prozessverzeichnisse der obersten Ebene werden nach PID und nicht nach UID benannt."}
:::

## Prozessinformationen lesen

Prüfe die Statusdatei eines Prozesses, sofern die Berechtigungen dies erlauben:

```bash
$ less /proc/12345/status
```

Sie enthält Felder wie Prozessname, Zustand, IDs, Zugangsdaten, Speicherzähler, Capabilities und Signalmasken. Weitere nützliche Einträge sind:

- `/proc/12345/cmdline`: durch Nullbytes getrennte Befehlszeilenargumente
- `/proc/12345/environ`: umgebungsbezogene Einträge, zugriffsgesteuert und potenziell vertraulich
- `/proc/12345/fd/`: symbolische Links, die offene Dateideskriptoren darstellen
- `/proc/12345/maps`: aktuelle Speicherabbildungen
- `/proc/12345/cwd`: symbolischer Link auf das aktuelle Arbeitsverzeichnis

Behandle diese Angaben als veränderliche Beobachtungen. Felder können je nach Kernelversion variieren, der Zustand eines Prozesses kann sich während des Lesens mehrerer Dateien ändern und einige Zähler besitzen Feinheiten, die ihre Namen allein nicht ausdrücken.

:::single-choice{#proc-filesystem-status-file}
Welcher Pfad enthält für PID 12345 eine lesbare, feldorientierte Zusammenfassung?

::option[`/proc/status/12345`]{#proc-filesystem-status-reversed explanation="Prozessbezogene Dateien liegen innerhalb des nach der PID benannten Verzeichnisses und nicht unter einem Verzeichnis `status` auf oberster Ebene."}
::option[`/proc/12345/status`]{#proc-filesystem-process-status .correct explanation="Die prozessbezogene Schnittstelle `status` stellt Kennungen, Zustand, Speicher-, Signal- und Zugangsdatenfelder bereit."}
::option[`/proc/cpuinfo/12345`]{#proc-filesystem-cpuinfo-pid explanation="`/proc/cpuinfo` ist eine systemweite Schnittstelle und kein Verzeichnis mit Statusdateien pro PID."}
:::

## Systemweite Schnittstellen lesen

Nicht jeder Eintrag unter `/proc` gehört zu einem Prozess. Beispiele sind:

- `/proc/cpuinfo` für vom Kernel gemeldete CPU-Informationen
- `/proc/meminfo` für Systemspeicherzähler
- `/proc/mounts` für die Einhängeansicht des aktuellen Prozesses
- `/proc/loadavg` für Lastmittelwerte und Informationen zu ausführungsbereiten Aufgaben
- `/proc/sys/` für Kernelparameter zur Laufzeit

Einige Dateien, insbesondere unter `/proc/sys`, sind beschreibbare Konfigurationsschnittstellen. Schreibe nicht in sie, nur weil sie wie gewöhnliche Dateien aussehen. Verstehe Parameter, Gültigkeitsbereich, Mechanismus zur dauerhaften Speicherung und Rücksetzweg, bevor du eine autorisierte Systemänderung vornimmst.

:::single-choice{#proc-filesystem-system-interface}
Welcher Eintrag stellt systemweite Speicherzähler und nicht den Status eines einzelnen Prozesses bereit?

::option[`/proc/self/status`]{#proc-filesystem-self-status explanation="Dies verweist auf den eigenen prozessbezogenen Status des beobachtenden Prozesses."}
::option[`/proc/meminfo`]{#proc-filesystem-memory-info .correct explanation="`meminfo` enthält vom Kernel gemeldete Systemspeicherstatistiken."}
::option[`/proc/1/fd`]{#proc-filesystem-one-fd explanation="Dieses Verzeichnis stellt vorbehaltlich der Zugriffskontrollen die Dateideskriptoren von PID 1 dar."}
:::

## `/proc` über Werkzeuge verwenden

Linux-Implementierungen von Werkzeugen wie `ps`, `top` und `free` beziehen einen großen Teil ihrer Daten aus procfs und anderen Kernel-Schnittstellen und beschriften, berechnen und formatieren sie anschließend. Bevorzuge diese Werkzeuge für Routinearbeiten, wenn sie das benötigte Feld bereitstellen. Lies `/proc` für bestimmte Einzelheiten oder Skripte nur dann direkt, wenn du die Dokumentation der Schnittstelle studiert hast.

Direkte Leser müssen Formate korrekt auswerten, mit verschwundenen Prozessen umgehen, vertrauliche Ausgaben schützen und dürfen nicht annehmen, dass ein einzelner Lesevorgang eine atomare Momentaufnahme des Systems darstellt.

:::single-choice{#proc-filesystem-live-data}
Warum kann `/proc/PID` zwischen zwei Inspektionsbefehlen verschwinden?

::option[Jede procfs-Datei wird automatisch einmal pro Sekunde umbenannt.]{#proc-filesystem-renamed explanation="Es gibt keine Regel zur regelmäßigen Umbenennung aller procfs-Einträge."}
::option[Das Lesen von `status` löscht das Prozessverzeichnis.]{#proc-filesystem-read-delete explanation="Die Statusprüfung ist schreibgeschützt und beendet oder entfernt den Prozess nicht."}
::option[Der Prozess kann sich während der Beobachtung beenden.]{#proc-filesystem-process-exit .correct explanation="Procfs bildet einen aktiven Zustand ab, daher entfernt der Kernel ein prozessbezogenes Verzeichnis, nachdem der Prozess verschwunden ist."}
:::

## Zusammenfassung

Du kannst procfs nun als aktive, zugriffsgesteuerte Kernel-Schnittstelle verwenden.

1. Ordne numerische `/proc`-Verzeichnisse sichtbaren PIDs zu.
2. Lies ausgewählte prozessbezogene Dateien unter Berücksichtigung von Rennen und Vertraulichkeit.
3. Unterscheide Prozessverzeichnisse von systemweiten Schnittstellen.
4. Bevorzuge dokumentierte Werkzeuge und Formate für zuverlässige Routineprüfungen.
