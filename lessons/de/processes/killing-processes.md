---
lesson_id: "killing-processes"
course_id: "processes"
lang: "de"
order_index: 7
title: "kill (Beenden)"
description: "Erfahre, wie du einen Prozess identifizierst und mit `kill` in einer sicheren Eskalationsreihenfolge ein geeignetes Signal sendest."
meta_title: "kill (Beenden) – Prozesse"
meta_description: "Beherrsche den Linux-Befehl kill, um Prozesse zu verwalten und zu beenden. Dieser Leitfaden behandelt die Unterschiede zwischen kill und terminate und erklärt Signale wie kill sigterm (SIGTERM), SIGKILL und kill sighup (SIGHUP)."
meta_keywords: "kill-Befehl, kill sigterm, kill sighup, Linux kill -0, kill oder terminate, kill -15 Linux, SIGTERM, SIGKILL, Prozessverwaltung, Prozess beenden"
---

Der Befehl `kill` sendet ein Signal an einen Prozess oder eine Prozessgruppe. Sein Name ist historisch bedingt: Das angeforderte Signal kann beenden, anhalten, fortsetzen oder eine anwendungsspezifische Aktion anstoßen. Bestätige immer das genaue Ziel und verstehe das dokumentierte Signalverhalten des Programms, bevor du ein Signal sendest.

## Eine geordnete Beendigung anfordern

Mit nur einer PID sendet `kill` standardmäßig `SIGTERM`:

```bash
$ kill 12445
```

Bevorzuge den symbolischen Namen, wenn du ein Signal ausdrücklich angibst:

```bash
$ kill -TERM 12445
```

Die Standardaktion von `SIGTERM` ist die Beendigung, doch ein Programm kann das Signal abfangen oder ignorieren. Ein gut entwickelter Dienst kann einen Handler verwenden, um keine neue Arbeit mehr anzunehmen, geeigneten Zustand zu speichern und Anwendungsressourcen freizugeben. Das ist eine Möglichkeit und keine Garantie für sofortige oder erfolgreiche Bereinigung.

:::single-choice{#killing-processes-default-signal} Welches Signal fordert `kill PID` standardmäßig an?

::option[`SIGKILL`]{#killing-processes-default-kill explanation="Das erzwungene, nicht abfangbare Signal muss ausdrücklich ausgewählt werden."}
::option[`SIGTERM`]{#killing-processes-default-term .correct explanation="Ohne einen anderen Signaloperanden sendet `kill` die standardmäßige Beendigungsanforderung."}
::option[`SIGSTOP`]{#killing-processes-default-stop explanation="Das Anhalten eines Prozesses ist nicht die von `kill` standardmäßig angeforderte Aktion."}
:::

## Das Ziel überprüfen

PIDs können wiederverwendet werden, sodass eine veraltete PID später einen anderen Prozess kennzeichnen kann. Prüfe das laufende Ziel unmittelbar vor der Aktion:

```bash
$ ps -p 12445 -o pid,ppid,user,lstart,stat,cmd
```

Prüfe Benutzer, Startzeit, Befehl, Elternprozess, Dienstzugehörigkeit und betriebliche Aufgabe. Wenn ein Dienstmanager den Prozess verwaltet, verwende nach Möglichkeit dessen Stopp- oder Neuladebefehl, damit er den richtigen Zustand beibehält und den Kindprozess nicht sofort neu startet.

Du darfst vorbehaltlich der Regeln für Zugangsdaten Prozesse signalisieren, die dir gehören. Das Signalisieren des Prozesses eines anderen Benutzers erfordert gewöhnlich entsprechende Privilegien. Verwende keinen weit gefassten namensbasierten Befehl, bevor du jede Übereinstimmung geprüft hast.

:::single-choice{#killing-processes-pid-reuse} Warum solltest du eine PID unmittelbar vor dem Senden eines Signals prüfen?

::option[Eine PID ändert sich jedes Mal, wenn der Prozess eine Datei liest.]{#killing-processes-pid-read explanation="Ein laufender Prozess behält gewöhnlich während seiner gesamten Lebensdauer dieselbe PID."}
::option[Der Kernel kann eine PID wiederverwenden, nachdem ihr früherer Prozess beendet wurde.]{#killing-processes-pid-reused .correct explanation="Eine gemerkte numerische PID kann später einen anderen laufenden Prozess bezeichnen."}
::option[`kill` akzeptiert Befehlsnamen, aber keine numerischen Kennungen.]{#killing-processes-no-numeric explanation="Eine numerische PID ist der gewöhnliche Zieloperand für `kill`."}
:::

## Signalberechtigung mit Signal null prüfen

Die Signalnummer null führt Fehlerprüfungen durch, ohne ein echtes Signal zuzustellen:

```bash
$ kill -0 12445
```

Ein erfolgreiches Ergebnis bedeutet, dass in diesem Augenblick ein Prozess mit dieser PID existiert und der Aufrufer ihm ein Signal senden darf. Ein Fehler ist mehrdeutig: Der Prozess ist möglicherweise nicht vorhanden oder dem Aufrufer fehlt die Berechtigung. Prüfe die Fehlermeldung und den Beendigungsstatus, statt jeden Fehler als „läuft nicht“ zu deuten. Außerdem ist dies nur eine Momentaufnahme und kann ein späteres Rennen durch PID-Wiederverwendung nicht ausschließen.

:::single-choice{#killing-processes-signal-zero} Was bestätigt ein erfolgreiches `kill -0 PID` in diesem Augenblick?

::option[Der Prozess hat jede Bereinigung abgeschlossen und wurde beendet.]{#killing-processes-zero-exited explanation="Erfolg bedeutet ein signalisierbares laufendes Ziel und nicht eine abgeschlossene Beendigung."}
::option[Der Prozess behält diese PID dauerhaft.]{#killing-processes-zero-permanent explanation="Die Prüfung gilt für einen einzelnen Zeitpunkt, und PIDs können nach der Beendigung wiederverwendet werden."}
::option[Der Prozess existiert und der Aufrufer darf ihm ein Signal senden.]{#killing-processes-zero-permitted .correct explanation="Signal null prüft die Existenz des Ziels und die Autorisierung, ohne ein gewöhnliches Signal zuzustellen."}
:::

## Nur bei Bedarf eskalieren

Wenn sich ein autorisiertes Ziel nach `SIGTERM` nicht beendet, warte eine der Arbeitslast angemessene Zeitspanne und untersuche den Grund. Wenn eine erzwungene Beendigung anschließend gerechtfertigt ist, sende:

```bash
$ kill -KILL 12445
```

`SIGKILL` kann weder abgefangen noch ignoriert oder blockiert werden. Das Programm kann daher keine Bereinigung auf Anwendungsebene durchführen. Es kann unvollständige Transaktionen, temporären Zustand oder Wiederherstellungsarbeit für andere Komponenten hinterlassen. Verwende es als Eskalation und nicht routinemäßig als ersten Schritt.

Andere Signale sind nur gemäß dem Vertrag des empfangenden Programms sinnvoll. `SIGHUP` fordert häufig das Neuladen der Konfiguration an, doch einige Programme behalten seine standardmäßige Beendigungswirkung bei. `SIGSTOP` hält ohne Bereinigung an und `SIGCONT` setzt einen angehaltenen Prozess fort.

:::single-choice{#killing-processes-kill-tradeoff} Was ist der wichtigste betriebliche Nachteil von `SIGKILL`?

::option[Es kann nur vom Prozesseigentümer behandelt werden.]{#killing-processes-kill-owner-handler explanation="Kein Zielprozess kann einen Handler für `SIGKILL` einrichten."}
::option[Es hält den Prozess an, beendet ihn aber niemals.]{#killing-processes-kill-pauses explanation="`SIGSTOP` hält an; `SIGKILL` beendet."}
::option[Es gibt dem Programm keine Gelegenheit zur Bereinigung auf Anwendungsebene.]{#killing-processes-kill-no-cleanup .correct explanation="Der Kernel erzwingt die Beendigung, ohne einen Signalhandler im User-Space aufzurufen."}
:::

Übe die Signalauswahl ausschließlich an Prozessen, die du selbst in einer isolierten Umgebung gestartet hast. Das Lab [Linux-Prozesse verwalten und überwachen](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) bietet einen kontrollierten Arbeitsablauf für Prüfung und Beendigung.

## Zusammenfassung

Du kannst nun Prozesssignale in einem bewussten, überprüfbaren Arbeitsablauf senden.

1. Bestätige das laufende Ziel und seinen Supervisor, bevor du handelst.
2. Verwende `SIGTERM` als normale Beendigungsanforderung.
3. Interpretiere Signal null als momentane Existenz- und Berechtigungsprüfung.
4. Reserviere `SIGKILL` für eine gerechtfertigte Eskalation nach einer Untersuchung.
