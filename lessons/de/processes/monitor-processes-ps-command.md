---
lesson_id: "monitor-processes-ps-command"
course_id: "processes"
lang: "de"
order_index: 1
title: "ps (Prozesse)"
description: "Erfahre, wie du mit `ps` Prozessmomentaufnahmen erstellst und mit `top` veränderliche Aktivitäten überwachst."
meta_title: "ps (Prozesse) – Prozesse"
meta_description: "Erkunde den Linux-Befehl ps mit unserem umfassenden Leitfaden. Erfahre, wie du unter Linux ps -ef und andere Optionen verwendest, um laufende Prozesse anzuzeigen, PIDs zu verstehen und Systemaufgaben zu verwalten. Ein perfekter Einstieg in deine Linux-Reise."
meta_keywords: "ps-Befehl, ps -ef Linux, Befehl ps -ef, Linux ps -ef, ps -e Linux, Linux-Prozesse, Prozess-ID, PID, top-Befehl, Linux-Reise"
---

Ein Prozess ist eine laufende Instanz eines Programms zusammen mit seinem Speicher, seinen Zugangsdaten, geöffneten Ressourcen und seinem Ausführungszustand. Linux kennzeichnet jeden laufenden Prozess mit einer numerischen Prozess-ID oder PID. Eine PID ist unter gleichzeitig vorhandenen Prozessen eindeutig, kann vom Kernel nach dem Beenden eines Prozesses jedoch erneut vergeben werden.

## Eine einfache Momentaufnahme erstellen

Führe `ps` ohne Optionen aus, um eine Momentaufnahme gemäß den Voreinstellungen der Implementierung anzuzeigen – gewöhnlich Prozesse, die deinem aktuellen Terminal und Benutzer zugeordnet sind:

```text
$ ps
    PID TTY          TIME CMD
  41230 pts/4    00:00:00 bash
  51224 pts/4    00:00:00 ps
```

Typische Felder sind:

- `PID`: Prozess-ID
- `TTY`: steuerndes Terminal oder `?`, wenn keines zugeordnet ist
- `TIME`: angesammelte CPU-Zeit und nicht die verstrichene reale Zeit
- `CMD`: Befehlsname oder Befehlszeile, abhängig vom ausgewählten Format

Die genauen Spalten und standardmäßigen Auswahlregeln unterscheiden sich zwischen `ps`-Implementierungen und Umgebungen.

:::single-choice{#ps-command-pid-meaning}
Was kennzeichnet die Spalte `PID`?

::option[Die Nummer des aktuellen Verzeichnisses des Prozesses.]{#ps-command-pid-directory explanation="Ein aktuelles Verzeichnis ist eine Dateisystemreferenz und wird nicht durch die PID dargestellt."}
::option[Die angesammelte CPU-Zeit in Sekunden.]{#ps-command-pid-cpu explanation="Die CPU-Nutzung wird in einem getrennten Feld wie `TIME` angezeigt."}
::option[Die vom Kernel zugewiesene Prozess-ID.]{#ps-command-pid-kernel .correct explanation="Die PID ist die numerische Kennung, mit der auf einen laufenden Prozess verwiesen wird."}
:::

## Prozesse mit Optionen im BSD-Stil auflisten

Linux-`ps` akzeptiert mehrere Optionsstile. Optionen im BSD-Stil werden gewöhnlich ohne führenden Bindestrich geschrieben:

```bash
$ ps aux
```

In dieser Kombination:

- `a` erweitert die Auswahl auf Prozesse anderer Benutzer, die Terminals besitzen.
- `x` nimmt zusätzlich Prozesse ohne steuernde Terminals auf und erweitert in Verbindung mit `a` die Auswahl.
- `u` wählt ein benutzerorientiertes Ausgabeformat mit Feldern wie `USER`, `%CPU`, `%MEM`, `VSZ` und `RSS`.

Da sich die Bedeutungen der Optionen gegenseitig beeinflussen können, solltest du die vollständige Kombination interpretieren, statt jeden Buchstaben als unabhängigen Befehl zu behandeln.

:::single-choice{#ps-command-aux-user-format}
Welche Option fordert in `ps aux` das benutzerorientierte Ausgabeformat an?

::option[`u`]{#ps-command-aux-u .correct explanation="Die BSD-Option `u` wählt eine benutzerorientierte Gruppe von Ausgabespalten aus."}
::option[`x`]{#ps-command-aux-x explanation="Die Option `x` beeinflusst die Prozessauswahl, insbesondere bei Prozessen ohne steuerndes Terminal."}
::option[`a`]{#ps-command-aux-a explanation="Die Option `a` erweitert die Auswahl über die Terminalprozesse des aktuellen Benutzers hinaus."}
:::

## Optionen im Standardstil verwenden

Der weitverbreitete Befehl `ps -ef` im Standardstil schreibt Optionen mit einem führenden Bindestrich:

```bash
$ ps -ef
```

- `-e` wählt jeden für den Aufrufer sichtbaren Prozess aus.
- `-f` fordert eine Auflistung im vollständigen Format an.

Die Ausgabe enthält gewöhnlich `UID`, `PID`, `PPID`, Startzeit und Befehlsinformationen. `PPID` ist die ID des Elternprozesses. Diese Auflistung ist nicht von sich aus hierarchisch. Verwende eine Option wie `--forest`, sofern unterstützt, oder eine spezielle Baumansicht wie `pstree`, wenn die Eltern-Kind-Anordnung wichtig ist.

:::single-choice{#ps-command-ef-selection}
Was fordert `-e` in `ps -ef` an?

::option[Eine Aktualisierung jede Sekunde bis zum Abbruch.]{#ps-command-e-refresh explanation="`ps` erzeugt eine Momentaufnahme; fortlaufende Aktualisierung ist eine Funktion von Werkzeugen wie `top`."}
::option[Eine Auswahl mit jedem für den Aufrufer sichtbaren Prozess.]{#ps-command-e-every .correct explanation="Die Standardoption `-e` erweitert die Momentaufnahme auf alle auswählbaren Prozesse."}
::option[Ausschließlich Prozesse, deren Befehl mit einem Fehler endete.]{#ps-command-e-errors explanation="Die Prozessauswahl basiert nicht auf dem späteren Beendigungsstatus eines Befehls."}
:::

## Aktivitäten im Zeitverlauf überwachen

`ps` beendet sich nach der Ausgabe einer Momentaufnahme. Verwende `top` für eine interaktive Ansicht, die regelmäßig aktualisiert wird:

```bash
$ top
```

`top` hilft dabei, wechselnde CPU- und Speicherverbraucher zu erkennen, doch seine Werte sind Stichproben und können schwanken. Bestätige ein vermutetes Problem über mehrere Beobachtungen hinweg und setze Prozentwerte mit der CPU-Anzahl, der Speicherbilanzierung und der Arbeitslast des Computers in Beziehung.

:::single-choice{#ps-command-snapshot-versus-top}
Welches hier vorgestellte Werkzeug aktualisiert seine Prozessanzeige standardmäßig regelmäßig?

::option[`top`]{#ps-command-top-refresh .correct explanation="`top` ist ein interaktiver Monitor, der seine Anzeige in Intervallen aktualisiert."}
::option[`ps -ef`]{#ps-command-ps-ef-snapshot explanation="Dieser Befehl gibt eine Prozessmomentaufnahme im vollständigen Format aus und beendet sich anschließend."}
::option[`ls -l`]{#ps-command-ls-files explanation="`ls -l` zeigt Dateisystemeinträge an und ist kein laufender Prozessmonitor."}
:::

Nutze für praktische Übungen [Linux-Prozesse verwalten und überwachen](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864), um Momentaufnahmen mit einem interaktiven Monitor zu vergleichen, oder erkunde Sortierung und Filterung im Lab [Linux-Befehl `top`](https://labex.io/labs/linux-linux-top-command-real-time-system-monitoring-388500).

## Zusammenfassung

Du kannst nun eine Prozessansicht auswählen und ihre grundlegenden Kennungen interpretieren.

1. Behandle eine PID als wiederverwendbare Kennung eines aktuell laufenden Prozesses.
2. Verwende ein einfaches `ps` für eine kleine standardmäßige Momentaufnahme.
3. Verwende `ps aux` oder `ps -ef` für umfassendere Auswahlen und aussagekräftigere Spalten.
4. Verwende `top`, wenn Veränderungen im Zeitverlauf wichtig sind.
