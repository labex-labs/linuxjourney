---
lesson_id: "process-creation"
course_id: "processes"
lang: "de"
order_index: 4
title: "Prozesserzeugung"
description: "Erfahre, wie fork, exec, PIDs und Elternbeziehungen an der Erzeugung von Linux-Prozessen beteiligt sind."
meta_title: "Prozesserzeugung – Prozesse"
meta_description: "Erkunde die Grundlagen der Prozesserzeugung unter Linux. Dieser Leitfaden behandelt die Systemaufrufe fork und execve, Eltern-Kind-Beziehungen (PID und PPID) sowie die Rolle des init-Prozesses. Erfahre, wie du unter Linux einen Prozess erzeugst, und verstehe die Kernkonzepte der Prozesserzeugung im Betriebssystem."
meta_keywords: "Prozesserzeugung unter Linux, Linux-Prozesserzeugung, Prozess unter Linux erzeugen, Prozesserzeugung im Betriebssystem, Prozesserzeugung, fork, execve, PID, PPID, init-Prozess, Linux-Prozesse"
---

Linux-Prozesse bilden Eltern-Kind-Beziehungen. Eine Shell startet einen externen Befehl gewöhnlich, indem sie einen Kindprozess erzeugt und dafür sorgt, dass dieser das angeforderte Programm ausführt. Die klassische Erklärung teilt diese Arbeit in die Vorgänge `fork` und `exec` auf.

## Mit `fork` einen Kindprozess erzeugen

Der Systemaufruf `fork()` erzeugt anhand des aufrufenden Prozesses einen Kindprozess. Eltern- und Kindprozess setzen ihre Ausführung am Rückkehrpunkt von `fork` fort, erhalten jedoch unterschiedliche Rückgabewerte und besitzen unterschiedliche PIDs.

Der Kindprozess erhält einen logisch getrennten Prozesszustand. Linux kann physische Speicherseiten zunächst mittels Copy-on-Write gemeinsam verwenden und eine Seite erst kopieren, wenn einer der Prozesse sie ändert. Offene Dateideskriptoren werden vererbt und verweisen auf dieselben zugrunde liegenden Beschreibungen geöffneter Dateien. Einzelheiten wie Dateipositionen können daher gemeinsam bleiben.

:::single-choice{#process-creation-fork-result} Was erzeugt ein erfolgreiches `fork()`?

::option[Ausschließlich ein Ersatzprogramm innerhalb desselben Prozesses.]{#process-creation-fork-replacement explanation="Das Ersetzen des aktuellen Programmabbilds ist die Aufgabe eines `exec`-Vorgangs."}
::option[Einen Kindprozess mit einer neuen PID.]{#process-creation-fork-child .correct explanation="`fork()` richtet einen getrennten Kindprozess und eine Eltern-Kind-Beziehung ein."}
::option[Sofort eine dauerhafte Kopie jeder physischen Speicherseite.]{#process-creation-fork-full-copy explanation="Linux verwendet gewöhnlich Copy-on-Write, statt alle physischen Seiten sofort zu duplizieren."}
:::

## Ein Programm mit `execve` ersetzen

Ein Aufruf von `execve()` lädt ein neues Programm in den aufrufenden Prozess. Bei Erfolg ersetzt er das Prozessabbild und kehrt nicht zum alten Programm zurück. Die PID bleibt unverändert, da `execve()` keinen neuen Prozess erzeugt.

Viele Shell-Befehle folgen deshalb einem fork-exec-Muster:

1. Die Shell erzeugt einen Kindprozess.
2. Der Kindprozess bereitet Umleitungen und anderen Ausführungszustand vor.
3. Der Kindprozess führt das angeforderte Programm aus.
4. Die Shell wartet oder setzt ihre Arbeit fort, abhängig von der Ausführung im Vorder- oder Hintergrund.

Bibliotheken und Anwendungen können übergeordnete Schnittstellen wie `posix_spawn()` bereitstellen, und Linux besitzt weitere Primitive wie `clone()`. Das vertraute fork-exec-Modell bleibt nützlich, ist aber nicht die einzig mögliche Schnittstelle.

:::single-choice{#process-creation-exec-pid} Was geschieht nach einem erfolgreichen `execve()` mit der PID eines Prozesses?

::option[Sie wird mit der PID des Elternprozesses identisch.]{#process-creation-exec-parent-pid explanation="Eltern- und Kindprozess behalten getrennte Prozess-IDs."}
::option[Sie bleibt unverändert, während das Programmabbild ersetzt wird.]{#process-creation-exec-same-pid .correct explanation="`execve()` verwandelt den aufrufenden Prozess, statt einen weiteren Prozess zu erzeugen."}
::option[Sie wird entfernt, bevor das neue Programm startet.]{#process-creation-exec-pid-removed explanation="Der bestehende Prozess läuft unter seiner PID mit neuem Code, neuen Daten, einem neuen Stack und zugehörigem Programmzustand weiter."}
:::

## Eltern- und Kind-IDs prüfen

`PID` kennzeichnet den Prozess, während `PPID` seinen Elternprozess kennzeichnet. Fordere diese Felder ausdrücklich an:

```bash
$ ps -o pid,ppid,stat,cmd
```

Wenn eine Shell `ps` startet, erscheint die PID der Shell gewöhnlich als `PPID` dieses `ps`-Prozesses. Der Zeitpunkt ist wichtig: Kurzlebige Prozesse können sich beenden, bevor eine getrennte Beobachtung sie erfasst.

:::single-choice{#process-creation-ppid} Wofür steht `PPID` in einer Prozessauflistung?

::option[Für die vorherige PID, die dem Prozess früher zugewiesen war.]{#process-creation-previous-pid explanation="PIDs können wiederverwendet werden, doch `PPID` erfasst keinen Verlauf von Kennungen."}
::option[Für die Kennung der Scheduling-Priorität des Prozesses.]{#process-creation-priority-id explanation="Die Scheduling-Priorität wird durch andere Felder wie Priorität oder Nice-Wert dargestellt."}
::option[Für die Prozess-ID des Elternprozesses.]{#process-creation-parent-pid .correct explanation="PPID erfasst die aktuelle Elternbeziehung des Prozesses."}
:::

## PID 1 und neue Elternzuordnung

Der Kernel startet den ersten User-Space-Prozess mit der PID 1. Je nach System kann es sich um `systemd`, eine andere init-Implementierung oder ein kleines init innerhalb eines Containers oder PID-Namensraums handeln. PID 1 startet und überwacht Teile der User-Space-Umgebung und besitzt besondere Zuständigkeiten für Signale und das Aufräumen verwaister Prozesse.

Wenn sich ein Elternprozess vor seinem Kind beendet, wird der Kindprozess einem geeigneten Subreaper oder dem init-Prozess seines PID-Namensraums als neues Kind zugeordnet. Er muss sich nicht allein deshalb beenden, weil sein ursprünglicher Elternprozess beendet wurde.

:::single-choice{#process-creation-pid-one} Welche Aussage über PID 1 ist richtig?

::option[Es muss immer ein Programm sein, dessen ausführbarer Name genau `init` lautet.]{#process-creation-pid-one-name explanation="Die Implementierung kann `systemd`, ein anderes init oder ein containerspezifisches Programm sein."}
::option[Es ist der Elternprozess, der jeden aktuell laufenden Prozess unmittelbar erzeugt hat.]{#process-creation-pid-one-direct explanation="Die meisten Prozesse entstehen über viele Generationen dazwischenliegender Elternprozesse."}
::option[Es ist der erste Prozess in seinem PID-Namensraum und besitzt init-ähnliche Zuständigkeiten.]{#process-creation-pid-one-init .correct explanation="PID 1 verankert die Überwachung und Bereinigung von User-Space-Prozessen innerhalb eines PID-Namensraums."}
:::

Im Lab [Linux-Prozesse verwalten und überwachen](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) kannst du Eltern- und Kind-IDs beobachten, während du Befehle im Vorder- und Hintergrund ausführst.

## Zusammenfassung

Du kannst nun die klassische Reihenfolge der Linux-Prozesserzeugung nachvollziehen.

1. Verwende `fork()`, um einen Kindprozess mit eigener PID zu erzeugen.
2. Verwende `execve()`, um ein Prozessabbild zu ersetzen, ohne seine PID zu ändern.
3. Lies PID und PPID, um Eltern-Kind-Beziehungen zu erkennen.
4. Erkenne PID 1 und Subreaper als Ziele für Kindprozesse mit neuer Elternzuordnung.
