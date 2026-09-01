---
lesson_id: "process-states"
course_id: "processes"
lang: "de"
order_index: 9
title: "Prozesszustände"
description: "Erfahre, wie du häufige Linux-Prozesszustandscodes in `ps`-Momentaufnahmen interpretierst."
meta_title: "Prozesszustände – Prozesse"
meta_description: "Ein umfassender Leitfaden zu Linux-Prozesszuständen. Lerne die verschiedenen Prozesszustände unter Linux (R, S, D, Z, T) kennen und erfahre, wie du sie mit dem Befehl `ps` interpretierst."
meta_keywords: "Linux-Prozesszustände, Prozesszustände unter Linux, Linux-Prozesszustand, Prozesszustand unter Linux, Linux-Prozesszustände erklärt, ps-Befehl, STAT-Codes, Prozessverwaltung"
---

Eine Linux-Aufgabe wechselt während ihrer Ausführung, ihres Wartens, Anhaltens und Beendens zwischen verschiedenen Zuständen. Das Feld `STAT` von `ps` erfasst einen einzelnen Augenblick. Bei der Diagnose eines Verhaltens sind wiederholte Beobachtungen daher nützlicher als ein einzelner Buchstabe.

```bash
$ ps -o pid,ppid,stat,wchan:24,cmd
```

Das erste Zeichen in `STAT` ist der primäre Zustand. Weitere Zeichen sind Modifikatoren, die Eigenschaften wie die Leitung einer Sitzung oder die Mitgliedschaft in einer Vordergrundprozessgruppe beschreiben. Den vollständigen Satz findest du im lokalen `ps`-Handbuch.

## Laufend und unterbrechbarer Schlaf

- `R` bedeutet laufend oder ausführungsbereit. Die Aufgabe wird auf einer CPU ausgeführt oder wartet in einer Ausführungswarteschlange auf CPU-Zeit.
- `S` bedeutet unterbrechbarer Schlaf. Die Aufgabe wartet auf ein Ereignis und kann durch ein geeignetes Signal oder Ereignis geweckt werden.

Schlafen ist normal. Interaktive Programme und Dienste verbringen einen großen Teil ihrer Zeit damit, auf Eingaben, Zeitgeber, Netzwerkverkehr, Sperren oder andere Ereignisse zu warten, statt fortlaufend CPU zu verbrauchen.

:::single-choice{#process-states-runnable-code} Was bedeutet der primäre Zustand `R`?

::option[Auf einer CPU laufend oder zur Ausführung bereit.]{#process-states-r-running .correct explanation="`R` umfasst sowohl aktuell ausgeführte Aufgaben als auch ausführungsbereite Aufgaben, die auf CPU-Zeit warten."}
::option[Aufgeräumt, nachdem der Elternprozess den Status abgeholt hat.]{#process-states-r-reaped explanation="Ein vollständig aufgeräumter Prozess erscheint nicht mehr als gewöhnlicher Eintrag in der Prozesstabelle."}
::option[In nicht unterbrechbarem Schlaf wartend.]{#process-states-r-uninterruptible explanation="Nicht unterbrechbarer Schlaf wird durch `D` dargestellt."}
:::

:::single-choice{#process-states-interruptible-code} Welcher primäre Zustand steht für unterbrechbaren Schlaf?

::option[`D`]{#process-states-sleep-d explanation="`D` steht für nicht unterbrechbaren Schlaf."}
::option[`Z`]{#process-states-sleep-z explanation="`Z` steht für einen beendeten Kindprozess, dessen Status noch nicht aufgeräumt wurde."}
::option[`S`]{#process-states-sleep-s .correct explanation="`S` ist der übliche `ps`-Code für unterbrechbares Warten."}
:::

## Nicht unterbrechbarer Schlaf

`D` bedeutet nicht unterbrechbarer Schlaf, gewöhnlich während die Aufgabe in einem Kernelvorgang wie bestimmter Speicher- oder Netzwerkdateisystem-E/A wartet. Die Aufgabe reagiert erst auf gewöhnliche Signale, wenn sie diesen Wartezustand verlässt; ein Signal kann währenddessen ausstehend bleiben.

Ein kurzer Zustand `D` kann normal sein. Dauerhaft oder zahlreich in `D` befindliche Aufgaben können auf langsame, nicht verfügbare oder fehlerhafte E/A hindeuten, doch der Zustand allein bestimmt nicht die Ursache. Prüfe den Wartekanal, Kernelprotokolle, den Zustand von Speicher und Netzwerk sowie das betreffende Subsystem, bevor du Schlüsse ziehst.

:::single-choice{#process-states-uninterruptible-code} Welcher primäre Zustand steht für nicht unterbrechbaren Schlaf?

::option[`T`]{#process-states-d-stopped explanation="`T` kennzeichnet eine angehaltene Aufgabe."}
::option[`D`]{#process-states-d-uninterruptible .correct explanation="`D` wird für eine Aufgabe verwendet, die in einem nicht unterbrechbaren Kernel-Schlaf wartet."}
::option[`R`]{#process-states-d-runnable explanation="`R` kennzeichnet eine ausgeführte oder ausführungsbereite Aufgabe."}
:::

## Angehaltene und Zombie-Zustände

- `T` bedeutet gewöhnlich, dass die Aufgabe durch die Jobsteuerung, etwa mit `SIGTSTP`, oder durch `SIGSTOP` angehalten wurde. Einige Werkzeuge verwenden ein kleingeschriebenes `t` für einen durch Tracing verursachten Stopp.
- `Z` bedeutet Zombie: Der Prozess wurde beendet, aber sein Elternprozess hat den Beendigungseintrag noch nicht abgeholt.

Setze einen Jobsteuerungsstopp gegebenenfalls mit `SIGCONT` fort. Ein Zombie kann weder fortgesetzt noch beendet werden, da er nicht mehr läuft; sein Elternprozess oder ein adoptierender Reaper muss ihn aufräumen.

:::single-choice{#process-states-zombie-code} Was kennzeichnet der primäre Zustand `Z`?

::option[Einen beendeten Prozess, dessen Beendigungseintrag noch auf das Aufräumen wartet.]{#process-states-z-zombie .correct explanation="Ein Zombie bewahrt nach dem Ende der Ausführung einen minimalen, für den Elternprozess sichtbaren Status auf."}
::option[Einen durch ein Terminal-Anhaltesignal pausierten Prozess.]{#process-states-z-terminal-stop explanation="Ein Jobsteuerungsstopp wird gewöhnlich als `T` angezeigt."}
::option[Einen Prozess, der derzeit einen vollständigen CPU-Kern verwendet.]{#process-states-z-cpu explanation="Eine aktiv laufende Aufgabe wird durch `R` dargestellt, während ein Zombie keine Anweisungen ausführt."}
:::

## Zustände im Zusammenhang lesen

Zustandscodes sind Beobachtungen und keine Diagnosen. Kombiniere sie mit verstrichener Zeit, CPU-Nutzung, Wartekanälen, Elternbeziehungen, Protokollen und wiederholten Stichproben. Eine Aufgabe kann ihren Zustand zwischen dem Augenblick, in dem der Kernel ihn meldet, und dem Augenblick, in dem du den Bildschirm liest, wechseln.

Das Lab [Linux-Prozesse verwalten und überwachen](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) bietet eine sichere Umgebung zum Beobachten von Vordergrund-, schlafenden, angehaltenen und beendeten Aufgaben.

## Zusammenfassung

Du kannst nun die häufigsten primären Prozesszustände interpretieren.

1. Lies `R` als laufend oder ausführungsbereit und `S` als unterbrechbaren Schlaf.
2. Untersuche dauerhaftes `D` als Wartesymptom und nicht als Diagnose.
3. Unterscheide angehaltenes `T` von beendetem, nicht aufgeräumtem `Z`.
4. Verwende wiederholte Beobachtungen und umgebende Belege.
