---
lesson_id: "process-termination"
course_id: "processes"
lang: "de"
order_index: 5
title: "Prozessbeendigung"
description: "Erfahre, wie Beendigungsstatus, Warten, Zombies und neue Elternzuordnung den Lebenszyklus eines Linux-Prozesses abschließen."
meta_title: "Prozessbeendigung – Prozesse"
meta_description: "Erkunde die Linux-Prozessbeendigung, den Systemaufruf wait und die entscheidenden Unterschiede zwischen Zombie- und verwaisten Prozessen. Erfahre, wie du Zustände von Kindprozessen verwaltest und Linux-Kindprozesse beendest, um ein stabiles System zu erhalten."
meta_keywords: "Linux-Prozessbeendigung, Zombie-Prozess, verwaister Prozess, Zombie- oder verwaister Prozess, Linux-Kindprozess beenden, Systemaufruf wait, _exit, Prozessverwaltung"
---

Ein Prozess kann enden, indem er aus seiner Hauptfunktion zurückkehrt, eine Beendigungsschnittstelle aufruft oder durch ein Signal beendet wird. Der Kernel gibt die meisten seiner Ressourcen frei, doch die Eltern-Kind-Abrechnung wird fortgesetzt, bis der Elternprozess die Beendigungsinformationen abholt.

## Beendigungsstatus

Ein sich normal beendendes Programm liefert einen ganzzahligen Status. Konventionsgemäß bedeutet Status `0` Erfolg, während ein von null verschiedener Wert eine Art von Fehler oder ein anderes Ergebnis meldet. Die genaue Bedeutung von Werten ungleich null gehört zur Schnittstelle des jeweiligen Programms.

Prüfe in einer Shell den Status der letzten Vordergrund-Pipeline mit:

```bash
$ command
$ printf '%s\n' "$?"
```

Shells stellen einen begrenzten codierten Statusbereich bereit und bilden außerdem Signalbeendigungen ab. Dieser Wert ist daher kein vollständiger Diagnosebericht. Programme sollten ihre eigenen Beendigungscodes dokumentieren.

:::single-choice{#process-termination-success-status}
Welcher normale Beendigungsstatus bedeutet gemäß Unix-Konvention Erfolg?

::option[`1`]{#process-termination-status-one explanation="Viele Programme verwenden `1` für einen allgemeinen Fehler, auch wenn die Bedeutungen befehlsspezifisch sind."}
::option[`0`]{#process-termination-status-zero .correct explanation="Ein normaler Status von null kennzeichnet konventionsgemäß den erfolgreichen Abschluss."}
::option[`255`]{#process-termination-status-255 explanation="Dieser Wert ist ungleich null und steht konventionsgemäß nicht für Erfolg."}
:::

## Warten und Aufräumen

Der Kernel erfasst, wie sich ein Kindprozess beendet hat, und benachrichtigt dessen Elternprozess. Der Elternprozess verwendet einen Aufruf aus der Systemaufruffamilie `wait()`, um diese Informationen abzurufen. Das Abholen des Eintrags wird als Reaping bezeichnet.

Warten kann außerdem die Ausführung koordinieren: Eine Shell wartet auf einen Vordergrundbefehl, bevor sie eine neue Eingabeaufforderung anzeigt, kann das Warten auf einen Hintergrundjob aber aufschieben. Ein gut entwickelter langlebiger Elternprozess muss Kindprozesse aufräumen, ohne unabhängige Arbeit zu blockieren.

:::single-choice{#process-termination-wait-purpose}
Welche Informationen kann ein Elternprozess mit einem erfolgreichen wait-Vorgang abrufen?

::option[Die Beendigungsinformationen des Kindprozesses.]{#process-termination-wait-status .correct explanation="Die wait-Familie meldet, wie ein Kindprozess angehalten oder beendet wurde, und räumt einen abgeschlossenen Kindprozess auf."}
::option[Eine Kopie des früheren Adressraums des Kindprozesses.]{#process-termination-wait-memory explanation="Der größte Teil des Prozessspeichers wurde bereits freigegeben und wird dem Elternprozess nicht durch `wait()` zurückgegeben."}
::option[Das Eigentum an jeder Datei, die der Kindprozess geöffnet hatte.]{#process-termination-wait-files explanation="Das Warten überträgt keine Eigentumsmetadaten des Dateisystems."}
:::

## Zombie-Prozesse

Nachdem sich ein Kindprozess beendet hat, aber bevor sein Beendigungseintrag aufgeräumt wurde, erscheint er als Zombie, häufig mit dem Zustand `Z` in `ps`. Er wird nicht mehr ausgeführt und besitzt keinen gewöhnlichen Adressraum mehr, doch ein minimaler Eintrag in der Prozesstabelle und Abrechnungsinformationen bleiben erhalten.

Ein Signal an einen Zombie kann ihn nicht noch einmal beenden. Diagnostiziere bei einer dauerhaften Ansammlung von Zombies den Elternprozess, der nicht wartet, starte oder korrigiere diesen Elternprozess nach einem geeigneten Betriebsverfahren oder ermögliche die neue Elternzuordnung zu einem Prozess, der den Zombie aufräumt. Eine große Zahl kann die Kapazität für PIDs oder Prozesstabelleneinträge erschöpfen.

:::single-choice{#process-termination-zombie-definition}
Welche Beschreibung passt zu einem Zombie-Prozess?

::option[Ein laufender Kindprozess, dessen Elternprozess sich bereits beendet hat.]{#process-termination-zombie-orphan explanation="Das beschreibt einen verwaisten Kindprozess und keinen Zombie-Zustand."}
::option[Ein abgeschlossener Kindprozess, dessen Beendigungseintrag noch nicht aufgeräumt wurde.]{#process-termination-zombie-unreaped .correct explanation="Der Prozess führt nichts mehr aus, doch der Kernel bewahrt einen minimalen Status für seinen Elternprozess auf."}
::option[Ein Prozess, der in einer nicht unterbrechbaren Schleife CPU verbraucht.]{#process-termination-zombie-cpu explanation="Ein Zombie führt keine Anweisungen aus und verbraucht keine CPU-Zeit."}
:::

## Verwaiste Prozesse und neue Elternzuordnung

Wenn sich ein Elternprozess beendet, während sein Kind weiterläuft, ordnet der Kernel diesen Kindprozess einem geeigneten Subreaper oder dem init-Prozess im betreffenden PID-Namensraum als neues Kind zu. Der Kindprozess kann laufen, schlafen, angehalten sein oder später zum Zombie werden. „Verwaist“ beschreibt den Verlust der ursprünglichen Elternbeziehung und nicht einen einzelnen Ausführungszustand.

Der adoptierende Prozess wird für das Abholen des Beendigungsstatus verantwortlich. Moderne Dienstmanager und Containerumgebungen machen es wichtig, nicht anzunehmen, dass der neue Elternprozess immer PID 1 des Hosts ist.

:::single-choice{#process-termination-orphan-definition}
Was geschieht, wenn ein Prozess seinen ursprünglichen Elternprozess überlebt?

::option[Er wird einem geeigneten Subreaper oder dem init-Prozess seines Namensraums als Kind zugeordnet.]{#process-termination-orphan-reparented .correct explanation="Der Kernel bewahrt eine gültige Elternbeziehung, indem er einen adoptierenden Prozess zuweist."}
::option[Er wird sofort zum Zombie, selbst wenn er sich noch nicht beendet hat.]{#process-termination-orphan-zombie explanation="Der Zombie-Zustand beginnt erst, nachdem die Ausführung beendet ist und der Status auf seine Abholung wartet."}
::option[Er verliert dauerhaft seine PID und läuft anonym weiter.]{#process-termination-orphan-no-pid explanation="Ein lebender verwaister Prozess behält seine Prozessidentität, während sich seine Elternbeziehung ändert."}
:::

Nutze das Lab [Linux-Prozesse verwalten und überwachen](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864), um Beendigungscodes und Prozesszustände zu beobachten, ohne eine Produktivarbeitslast zu beeinträchtigen.

## Zusammenfassung

Du kannst nun das Ende der Ausführung von der Bereinigung durch den Elternprozess unterscheiden.

1. Interpretiere null als konventionellen Erfolg und von null verschiedene Statuswerte anhand der Programmdokumentation.
2. Verwende Warten, um die Beendigungsinformationen eines Kindprozesses abzuholen.
3. Erkenne einen Zombie als beendet, aber noch nicht aufgeräumt.
4. Erkenne einen verwaisten Prozess als Kind, das nach der Beendigung seines ursprünglichen Elternprozesses neu zugeordnet wurde.
