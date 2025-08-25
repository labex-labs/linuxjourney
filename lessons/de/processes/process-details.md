---
index: 3
lang: "de"
title: "Prozessdetails"
meta_title: "Prozessdetails - Prozesse"
meta_description: "Erfahren Sie mehr über Linux-Prozessdetails, wie der Kernel Ressourcen verwaltet und was Prozesse sind. Verstehen Sie Prozesskonzepte für Anfänger."
meta_keywords: "Linux-Prozesse, Kernel, Prozessverwaltung, ps aux, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Bevor wir uns mit praktischeren Anwendungen von Prozessen befassen, müssen wir zunächst verstehen, was sie sind und wie sie funktionieren. Dieser Teil kann verwirrend sein, da wir ins Detail gehen. Sie können also gerne zu dieser Lektion zurückkehren, wenn Sie jetzt nichts darüber lernen möchten.

Ein Prozess ist, wie bereits erwähnt, ein laufendes Programm auf dem System. Genauer gesagt, weist das System Speicher, CPU und E/A zu, um das Programm auszuführen. Ein Prozess ist eine Instanz eines laufenden Programms. Öffnen Sie drei Terminalfenster. Führen Sie in zwei Fenstern den Befehl `cat` ohne Optionen aus (der `cat`-Prozess bleibt als Prozess geöffnet, da er stdin erwartet). Führen Sie nun im dritten Fenster Folgendes aus: `ps aux | grep cat`. Sie werden sehen, dass es zwei Prozesse für `cat` gibt, obwohl sie dasselbe Programm aufrufen.

Der kernel ist für Prozesse zuständig. Wenn wir ein Programm ausführen, lädt der kernel den Code des Programms in den Speicher, bestimmt und weist Ressourcen zu und überwacht dann jeden Prozess. Er weiß:

- Den Status des Prozesses
- Die Ressourcen, die der Prozess verwendet und empfängt
- Den Prozessbesitzer
- Signalbehandlung (mehr dazu später)
- Und im Grunde alles andere

Alle Prozesse versuchen, einen Teil des begehrten Ressourcenkuchens abzubekommen. Es ist die Aufgabe des kernels, sicherzustellen, dass Prozesse die richtige Menge an Ressourcen erhalten, abhängig von den Prozessanforderungen. Wenn ein Prozess endet, werden die von ihm verwendeten Ressourcen für andere Prozesse freigegeben.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Linux-Prozessen und deren Verwaltung zu vertiefen:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** – Erlernen Sie grundlegende Fähigkeiten zur Verwaltung und Überwachung von Prozessen auf einem Linux-System, einschließlich der Interaktion mit Vordergrund-/Hintergrundprozessen, der Inspektion mit `ps`, der Überwachung mit `top` und der Beendigung mit `kill`.
2. **[Linux top Befehl: Echtzeit-Systemüberwachung](https://labex.io/de/labs/linux-linux-top-command-real-time-system-monitoring-388500)** – Lernen Sie, den Befehl `top` für die Echtzeit-Systemüberwachung zu verwenden, einschließlich des Sortierens von Prozessen, des Anpassens von Aktualisierungsintervallen und des Filterns nach Benutzer.
3. **[Linux free Befehl: Systemarbeitsspeicher überwachen](https://labex.io/de/labs/linux-linux-free-command-monitoring-system-memory-388496)** – Lernen Sie, den Befehl `free` zu verwenden, um die Systemarbeitsspeichernutzung zu überwachen und zu analysieren und zu verstehen, wie der kernel Ressourcen für Prozesse zuweist.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Prozessverwaltung unter Linux aufzubauen.

## Quiz Question

Was verwaltet und steuert Prozesse?

## Quiz Answer

kernel
