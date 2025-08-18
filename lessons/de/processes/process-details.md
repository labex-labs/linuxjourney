---
index: 3
lang: "de"
title: "Prozessdetails"
meta_title: "Prozessdetails - Prozesse"
meta_description: "Erfahren Sie mehr über Linux-Prozessdetails, wie der Kernel Ressourcen verwaltet und was Prozesse sind. Verstehen Sie Prozesskonzepte für Anfänger."
meta_keywords: "Linux-Prozesse, Kernel, Prozessverwaltung, ps aux, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Bevor wir uns mit praktischeren Anwendungen von Prozessen befassen, müssen wir zunächst verstehen, was sie sind und wie sie funktionieren. Dieser Teil kann verwirrend sein, da wir uns ins Detail vertiefen. Sie können jederzeit zu dieser Lektion zurückkehren, wenn Sie dies jetzt nicht lernen möchten.

Ein Prozess ist, wie bereits erwähnt, ein laufendes Programm auf dem System. Genauer gesagt, weist das System Speicher, CPU und E/A zu, um das Programm auszuführen. Ein Prozess ist eine Instanz eines laufenden Programms. Öffnen Sie drei Terminalfenster. Führen Sie in zwei Fenstern den Befehl `cat` ohne Optionen aus (der `cat`-Prozess bleibt als Prozess geöffnet, da er stdin erwartet). Führen Sie nun im dritten Fenster Folgendes aus: `ps aux | grep cat`. Sie werden sehen, dass es zwei Prozesse für `cat` gibt, obwohl sie dasselbe Programm aufrufen.

Der kernel ist für Prozesse zuständig. Wenn wir ein Programm ausführen, lädt der kernel den Code des Programms in den Speicher, bestimmt und weist Ressourcen zu und behält dann jeden Prozess im Auge. Er weiß:

- Den Status des Prozesses
- Die Ressourcen, die der Prozess verwendet und empfängt
- Den Prozessbesitzer
- Signalbehandlung (mehr dazu später)
- Und im Grunde alles andere

Alle Prozesse versuchen, einen Anteil an diesem süßen Ressourcenkuchen zu bekommen. Es ist die Aufgabe des kernel, sicherzustellen, dass Prozesse die richtige Menge an Ressourcen erhalten, abhängig von den Prozessanforderungen. Wenn ein Prozess endet, werden die von ihm verwendeten Ressourcen für andere Prozesse freigegeben.

## Exercise

Keine Übungen für diese Lektion.

## Quiz Question

Was verwaltet und steuert Prozesse?

## Quiz Answer

kernel
