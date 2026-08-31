---
lesson_id: "process-details"
course_id: "processes"
lang: "de"
order_index: 3
title: "Prozessdetails"
description: "Erfahre, welcher Zustand und welche Ressourcen einen laufenden Prozess von einem auf dem Datenträger gespeicherten Programm unterscheiden."
meta_title: "Prozessdetails – Prozesse"
meta_description: "Erkunde die Grundlagen von Linux-Prozessdetails. Dieser Leitfaden für Einsteiger erklärt, was ein Prozess ist, wie der Linux-Kernel Prozesse verwaltet und Systemressourcen wie CPU und Speicher zuweist."
meta_keywords: "Linux-Prozess, Prozessdetails, Kernel, Prozessverwaltung, Systemressourcen, ps aux, CPU, Speicher, Linux-Tutorial, Leitfaden für Einsteiger"
---

Ein Programm besteht aus ausführbarem Code und Daten, die in einer Datei gespeichert sind. Ein Prozess ist ein aktiver Ausführungskontext: Er umfasst eingebundenen Code, Speicher, Zugangsdaten, offene Dateideskriptoren, Signalzustand, Scheduling-Informationen und einen oder mehrere Threads. Dasselbe Programm kann viele unabhängige Prozessinstanzen besitzen.

## Programminstanzen und PIDs

Starte beispielsweise `cat` ohne Operanden in zwei Terminals. Jede Instanz wartet auf Eingaben und besitzt eine eigene Prozess-ID:

```bash
$ pgrep -a cat
18420 cat
18457 cat
```

Beide Prozesse führen dasselbe Programm aus, können aber unterschiedliche Eingabeströme, Speicherinhalte, Zugangsdaten, Arbeitsverzeichnisse und Lebensdauern besitzen. Eine PID kennzeichnet jeweils einen laufenden Prozess und kann später nach dessen Beendigung erneut vergeben werden.

:::single-choice{#process-details-program-versus-process}
Was unterscheidet zwei laufende Instanzen desselben Programms?

::option[Die ausführbare Datei muss für jede Instanz einmal kopiert werden.]{#process-details-copied-executable explanation="Mehrere Prozesse können die Codeseiten derselben ausführbaren Datei einbinden und gemeinsam nutzen, ohne die Datei zu duplizieren."}
::option[Nur eine Instanz kann Speicher oder offene Dateien besitzen.]{#process-details-one-instance-resources explanation="Jeder Prozess kann eigene Speicherabbildungen und eine eigene Dateideskriptortabelle besitzen."}
::option[Jede Instanz besitzt einen eigenen Prozesskontext und eine eigene PID.]{#process-details-independent-context .correct explanation="Getrennte Ausführungen erhalten einen eigenen aktiven Prozesszustand, auch wenn ihr ausführbarer Code aus derselben Datei stammt."}
:::

## Vom Kernel verfolgter Zustand

Der Kernel verwaltet die Informationen, die zum Planen und Steuern jedes Prozesses erforderlich sind, darunter:

- Prozess- und Elternkennungen
- Benutzer- und Gruppenzugangsdaten
- virtuelle Speicherabbildungen
- offene Dateideskriptoren und das aktuelle Verzeichnis
- Signalbehandlungen und ausstehende Signale
- Scheduling-Richtlinie, Priorität und Ausführungszustand
- Abrechnungsdaten wie CPU-Zeit

Einige zugrunde liegende Ressourcen können gemeinsam verwendet werden. Verwandte Prozesse können eingebundenen Speicher teilen, und Threads eines Prozesses teilen sich einen Adressraum und viele prozessweite Ressourcen. Ein Prozess stellt daher Isolationsgrenzen bereit, ohne dass jedes Byte oder Kernelobjekt physisch privat sein muss.

:::single-choice{#process-details-kernel-state}
Welche Komponente verwaltet Scheduling- und Zugangsdatenzustände für Linux-Prozesse?

::option[Der Kernel.]{#process-details-kernel .correct explanation="Der Kernel verfolgt den Prozesszustand und wendet Regeln für Scheduling, Speicher, Signale und Zugriffskontrolle an."}
::option[Das Verzeichnis der ausführbaren Datei.]{#process-details-directory explanation="Ein Verzeichnis speichert eine Zuordnung von Namen zu Inodes und plant keine laufenden Prozesse."}
::option[Ausschließlich der Terminalemulator des Benutzers.]{#process-details-terminal explanation="Ein Terminal kann mit Prozessen interagieren, doch die Prozessverwaltung bleibt Aufgabe des Kernels."}
:::

## CPU-Scheduling und Speicher

Ausführungsbereite Threads konkurrieren um CPU-Zeit. Der Kernel-Scheduler wählt anhand von Scheduling-Klasse, Priorität, CPU-Affinität, Last und Richtlinie aus, welcher Thread auf welcher CPU läuft. Das ist keine Zusage, dass jeder Prozess einen gleichen Anteil erhält.

Jeder Prozess sieht gewöhnlich einen virtuellen Adressraum. Kernel und Hardware ordnen virtuelle Adressen physischem Speicher oder einem anderen Hintergrundspeicher zu, setzen Schutzmechanismen durch und können Seiten gegebenenfalls gemeinsam nutzen. Eine Speicherangabe in `ps` oder `top` entspricht daher nicht automatisch der Menge an eindeutig diesem Prozess zurechenbarem physischem RAM.

:::single-choice{#process-details-scheduler-role}
Was wählt der Linux-Scheduler aus?

::option[Welcher ausführungsbereite Thread auf einer verfügbaren CPU ausgeführt wird.]{#process-details-runnable-thread .correct explanation="Die Scheduling-Richtlinie wählt unter ausführungsbereiten Ausführungskontexten aus und weist CPU-Zeit zu."}
::option[Welcher Dateieigentümer beim Formatieren eines Datenträgers erfasst wird.]{#process-details-format-owner explanation="Dateisystemeigentum hat nichts mit CPU-Scheduling zu tun."}
::option[Welche Befehlszeile ein Benutzer eingeben darf.]{#process-details-command-entry explanation="Der Scheduler verwaltet Ausführungszeit und nicht die Syntax interaktiver Befehle."}
:::

## Prozessbeendigung und Ressourcenbereinigung

Wenn sich ein Prozess beendet, gibt der Kernel die meisten seiner privaten Ressourcen frei, schließt verbleibende Deskriptoren und erfasst Beendigungsinformationen für den Elternprozess. Ein kleiner Eintrag in der Prozesstabelle kann als Zombie bestehen bleiben, bis der Elternprozess den Beendigungsstatus abruft. Daher sind „der Prozess hat seine Ausführung beendet“ und „jede Spur ist aus der Prozesstabelle verschwunden“ nicht immer gleichzeitige Ereignisse.

:::single-choice{#process-details-exit-status}
Warum kann ein beendeter Prozess kurzzeitig als Zombie bestehen bleiben?

::option[Er führt weiterhin Anweisungen aus und besitzt seinen gesamten Speicher.]{#process-details-zombie-running explanation="Ein Zombie hat seine Ausführung abgeschlossen und besitzt keinen gewöhnlichen laufenden Adressraum mehr."}
::option[Sein Elternprozess hat den erfassten Beendigungsstatus noch nicht abgeholt.]{#process-details-parent-wait .correct explanation="Der Kernel bewahrt minimale Beendigungsinformationen auf, bis der Elternprozess einen wait-Vorgang ausführt."}
::option[Seine ausführbare Datei wird vom Kernel dauerhaft gesperrt.]{#process-details-zombie-file-lock explanation="Der Zombie-Zustand betrifft die Eltern-Kind-Abrechnung bei der Beendigung und keine dauerhafte Sperre der ausführbaren Datei."}
:::

Nutze das Lab [Linux-Prozesse verwalten und überwachen](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864), um mehrere Instanzen zu starten und ihre PIDs und Zustände zu vergleichen. Das Lab [Linux-Befehl `top`](https://labex.io/labs/linux-linux-top-command-real-time-system-monitoring-388500) bietet eine veränderliche Ansicht von Scheduling- und Ressourcenmetriken.

## Zusammenfassung

Du kannst nun einen Prozess als mehr als eine Programmdatei beschreiben.

1. Unterscheide gespeicherten ausführbaren Code von einer aktiven Prozessinstanz.
2. Bestimme den vom Kernel verfolgten Zustand und die Ressourcen.
3. Setze Scheduling mit ausführungsbereiten Threads statt mit gleichen Anteilen in Beziehung.
4. Erkenne, dass der Beendigungsstatus bestehen bleiben kann, bis der Elternprozess ihn abholt.
