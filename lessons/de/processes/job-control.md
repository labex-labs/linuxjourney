---
lesson_id: "job-control"
course_id: "processes"
lang: "de"
order_index: 11
title: "Jobsteuerung"
description: "Erfahre, wie eine interaktive Shell Vordergrund-, Hintergrund- und angehaltene Jobs verwaltet."
meta_title: "Jobsteuerung – Prozesse"
meta_description: "Erkunde unser Linux-Tutorial zur Jobsteuerung, um Hintergrundprozesse wirksam zu verwalten. Lerne die Befehle jobs, bg, fg und kill für leistungsfähiges Multitasking in der Shell kennen."
meta_keywords: "Linux-Jobsteuerung, Hintergrundprozesse, jobs-Befehl, bg-Befehl, fg-Befehl, kill-Befehl, Linux-Tutorial, Linux für Einsteiger"
---

Interaktive Shells verwenden die Jobsteuerung, um Pipelines innerhalb einer Terminalsitzung zu koordinieren. Ein Job kann einen Prozess oder eine vollständige Pipeline umfassen, die gewöhnlich in einer Prozessgruppe zusammengefasst wird, damit Terminal und Shell sie als Einheit behandeln können.

## Einen Hintergrundjob starten

Hänge `&` an, um eine Pipeline asynchron zu starten:

```bash
$ sleep 1000 &
[1] 18420
```

Die Shell zeigt wieder eine Eingabeaufforderung an, ohne auf die Beendigung des Jobs zu warten. Der Hintergrundstatus leitet Ausgaben nicht automatisch um, trennt das steuernde Terminal nicht ab und sorgt nicht dafür, dass der Job eine Abmeldung überlebt. Leite Ein- und Ausgaben bei Bedarf ausdrücklich um und verwende einen Dienstmanager, einen Aufgabenplaner oder einen Terminalmultiplexer für Arbeit, die die interaktive Shell überdauern muss.

Ein Hintergrundjob, der vom steuernden Terminal zu lesen versucht, wird gewöhnlich mit `SIGTTIN` angehalten, da er nicht zur Vordergrundprozessgruppe des Terminals gehört.

:::single-choice{#job-control-ampersand-effect}
Wozu fordert ein abschließendes `&` eine interaktive Shell auf?

::option[Zu garantieren, dass der Job Abmeldung und Systemneustart überlebt.]{#job-control-survive-restart explanation="Das Ausführen im Hintergrund bietet weder dauerhafte Überwachung noch Beständigkeit über einen Neustart hinweg."}
::option[Die Pipeline als Hintergrundjob auszuführen, ohne vor der nächsten Eingabeaufforderung zu warten.]{#job-control-background-job .correct explanation="Die Shell startet den Job asynchron und bleibt für weitere Befehle verfügbar."}
::option[Die Standardausgabe und Fehlerausgabe des Jobs zu verwerfen.]{#job-control-discard-output explanation="Ohne Umleitung kann ein Hintergrundjob weiterhin in das Terminal schreiben."}
:::

## Shell-Jobs auflisten

Das Built-in `jobs` listet die der aktuellen Shell bekannten Jobs auf:

```text
$ jobs
[1]    Running    sleep 1000 &
[2]-   Running    sleep 1001 &
[3]+   Stopped    sleep 1002
```

Die Zahl in eckigen Klammern ist eine Shell-Job-ID und keine PID. Ein vorangestelltes `%` bildet eine Jobspezifikation wie `%1`. Die Markierung `+` kennzeichnet den aktuellen Job, den viele Befehle auswählen, wenn kein Operand angegeben ist; `-` kennzeichnet den vorherigen Job.

Da die Jobtabelle zu einer einzelnen Shell gehört, kann die Shell eines anderen Terminals diese Jobs gewöhnlich nicht mit ihren eigenen Built-ins `jobs`, `fg` oder `bg` auflisten oder ansprechen.

:::single-choice{#job-control-jobs-scope}
Was listet das Built-in `jobs` auf?

::option[Von der aktuellen Shell-Sitzung verfolgte Jobs.]{#job-control-jobs-current-shell .correct explanation="Job-IDs und Zustand werden von der interaktiven Shell verwaltet, die diese Jobs gestartet oder übernommen hat."}
::option[Jeden derzeit auf dem System sichtbaren Prozess.]{#job-control-jobs-all-processes explanation="Die systemweite Prozessprüfung gehört zu Werkzeugen wie `ps`; die Jobtabelle der Shell ist enger gefasst."}
::option[Ausschließlich Dienste, die beim Systemstart gestartet wurden.]{#job-control-jobs-boot-services explanation="Startdienste werden gewöhnlich von einem Dienstmanager und nicht von der Jobtabelle einer interaktiven Shell überwacht."}
:::

## Einen Job anhalten und fortsetzen

Während ein Job im Vordergrund läuft, veranlasst das Drücken von `Ctrl-Z` das Terminal gewöhnlich, `SIGTSTP` an seine Vordergrundprozessgruppe zu senden. Nach dem Anhalten des Jobs erhält die Shell wieder die Kontrolle:

```text
$ sleep 1002
^Z
[3]+  Stopped    sleep 1002
```

Setze den aktuellen angehaltenen Job im Hintergrund fort mit:

```bash
$ bg
```

`bg` sendet ein Fortsetzungssignal und lässt den Job außerhalb des Terminalvordergrunds. Es ist nur für einen angehaltenen Job nützlich; ein bereits im Hintergrund laufender Befehl muss nicht fortgesetzt werden.

:::single-choice{#job-control-bg-purpose}
Was bewirkt `bg %3` bei dem angehaltenen Job 3?

::option[Es verschiebt seine Dateien in ein Verzeichnis namens `bg`.]{#job-control-bg-files explanation="`bg` ist ein Built-in zur Jobsteuerung der Shell und verschiebt keine Dateisystemobjekte."}
::option[Es setzt ihn als Hintergrundjob fort.]{#job-control-bg-continue .correct explanation="Die Shell setzt den ausgewählten angehaltenen Job fort, ohne ihn dem Terminalvordergrund zuzuweisen."}
::option[Es beendet ihn mit `SIGKILL`.]{#job-control-bg-kill explanation="Das Built-in setzt den Job fort, statt ihn zu beenden."}
:::

## Einen Job in den Vordergrund holen

Verwende `fg` mit einer Jobspezifikation, um einen Job zur Vordergrundprozessgruppe des Terminals zu machen und auf ihn zu warten:

```bash
$ fg %1
```

Ohne Operanden wählt `fg` gewöhnlich den mit `+` markierten aktuellen Job aus. Ein angehaltener Job wird beim Wechsel in den Vordergrund fortgesetzt.

:::single-choice{#job-control-fg-effect}
Was bewirkt `fg %1`?

::option[Es weist Job 1 dem Terminalvordergrund zu und wartet auf ihn.]{#job-control-fg-foreground .correct explanation="Die Shell holt den ausgewählten Job in den Vordergrund, damit er mit dem Terminal interagieren kann."}
::option[Es wandelt Job 1 in PID 1 um.]{#job-control-fg-pid-one explanation="Eine Shell-Job-ID ersetzt oder verändert keine Prozess-IDs."}
::option[Es startet eine zweite Kopie von Job 1 im Hintergrund.]{#job-control-fg-copy explanation="`fg` arbeitet mit dem bestehenden Job und erzeugt kein Duplikat."}
:::

## Ein Signal an einen Job senden

Shells erlauben `kill` die Annahme einer Jobspezifikation:

```bash
$ kill -TERM %1
```

Dies signalisiert gewöhnlich die Prozessgruppe des Jobs und nicht nur ein einzelnes Mitglied der Pipeline. Prüfe zuerst den ausgewählten Job und verwende `SIGTERM`, bevor du eine erzwungene Eskalation in Betracht ziehst. Jobspezifikationen sind Shell-Syntax; Skripte und externe Werkzeuge arbeiten häufiger mit überprüften PIDs oder Prozessgruppen-IDs.

:::single-choice{#job-control-job-specification}
Welcher Operand bezeichnet Shell-Job 1 und nicht Prozess-ID 1?

::option[`1`]{#job-control-plain-one explanation="Ein einfacher numerischer Operand für `kill` wird gewöhnlich als PID interpretiert."}
::option[`#1`]{#job-control-hash-one explanation="Ein Rautenzeichen ist nicht die hier eingeführte Syntax für eine Shell-Job-ID."}
::option[`%1`]{#job-control-percent-one .correct explanation="Das Prozentzeichen kennzeichnet eine Shell-Jobspezifikation."}
:::

Übe diese Vorgänge mit harmlosen Befehlen wie `sleep` im Lab [Linux-Prozesse verwalten und überwachen](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864).

## Zusammenfassung

Du kannst Jobs nun gezielt zwischen von der Shell gesteuerten Zuständen verschieben.

1. Verwende `&`, um einen Hintergrundjob ohne automatische Abtrennung zu starten.
2. Verwende `jobs`, um die Jobtabelle der aktuellen Shell zu prüfen.
3. Halte mit `Ctrl-Z` an und setze mit `bg` im Hintergrund fort.
4. Hole einen ausgewählten Job mit `fg` zurück an das Terminal.
5. Sprich Shell-Jobs beim Senden von Signalen mit `%JOB_ID` an.
