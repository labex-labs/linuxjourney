---
index: 3
lang: "de"
title: "Systemaufrufe"
meta_title: "Systemaufrufe - Kernel"
meta_description: "Erkunden Sie die Grundlagen eines Systemaufrufs unter Linux. Erfahren Sie, wie Prozesse im Benutzermodus Systemaufrufe (Syscalls) verwenden, um Dienste vom Kernel anzufordern, Modi zu wechseln und wie die Syscall-Tabelle funktioniert. Nutzen Sie `strace`, um Systemaufrufe in Aktion zu sehen."
meta_keywords: "system call linux, systemaufrufe, syscall tabelle, kernel modus, benutzer modus, strace, linux kernel, syscall API"
---

## Lesson Content

Stellen Sie sich vor, Sie befinden sich auf einem großen Konzert. Um vom allgemeinen Zuschauerbereich zur exklusiven Backstage zu gelangen, können Sie nicht einfach hineinspazieren. Sie benötigen einen speziellen Ausweis, der Ihnen den Zugang durch eine bestimmte, bewachte Tür gewährt. In der Welt der Computer sind **Systemaufrufe** (System Calls) diese speziellen Ausweise.

### Was sind Systemaufrufe?

Systemaufrufe, oft als Syscalls abgekürzt, bieten Benutzerprozessen eine Möglichkeit, Dienste direkt vom Kernel anzufordern. Der Kernel stellt eine Reihe von Diensten über die Systemaufruf-API bereit. Diese Dienste sind wesentlich für Operationen wie das Lesen oder Schreiben in eine Datei, die Speicherverwaltung oder die Handhabung von Netzwerkverbindungen. Die Anzahl der verfügbaren Systemaufrufe ist festgelegt; Sie können nicht willkürlich neue hinzufügen. Ihr System führt eine `Syscall-Tabelle` (syscall table), in der jeder Systemaufruf mit einer eindeutigen ID registriert ist.

### Der Systemaufruf-Mechanismus unter Linux

Wenn Sie ein Programm wie `ls` ausführen, führt der darin enthaltene Code den Befehl **Systemaufruf Linux** nicht direkt aus. Stattdessen verwendet er eine Bibliotheksfunktion, die als Wrapper fungiert. Diese Wrapper-Funktion richtet die notwendigen Parameter ein und löst dann eine Software-Unterbrechung oder eine „Trap“ aus.

Diese Trap signalisiert dem Prozessor, vom nicht-privilegierten Benutzermodus in den privilegierten Kernelmodus zu wechseln. Im Kernelmodus übernimmt ein Systemaufruf-Handler die Steuerung. Er verwendet die eindeutige ID, um die angeforderte Funktion in der `Syscall-Tabelle` nachzuschlagen und führt sie dann aus. Beispielsweise wird der Systemaufruf `stat()`, der zur Abfrage des Status einer Datei verwendet wird, auf diese Weise gefunden und ausgeführt. Nachdem der Kernel die Aufgabe abgeschlossen hat, schaltet er den Kontext zurück in den Benutzermodus und gibt einen Statuscode an Ihren Prozess zurück, der Erfolg oder einen Fehler anzeigt.

### Systemaufrufe mit strace anzeigen

Sie können die Systemaufrufe, die ein Prozess tätigt, in Echtzeit mit dem Befehl `strace` beobachten. Dieses Tool ist unglaublich nützlich für das Debugging und das Verständnis, wie ein Programm mit dem Kernel interagiert.

Um die Systemaufrufe des `ls`-Befehls anzuzeigen, würden Sie Folgendes ausführen:

```bash
strace ls
```

Dies gibt eine detaillierte Liste jedes Systemaufrufs aus, den `ls` während seiner Ausführung durchführt.

## Exercise

Übung macht den Meister! Obwohl die internen Abläufe von Systemaufrufen komplex sind, ist das Verständnis, wie Benutzerbereichsprogramme mit dem Kernel interagieren, grundlegend. Der beste Weg, diese Interaktion zu erfassen, ist das Üben mit Befehlen, die diese zugrunde liegenden Operationen durchführen. Hier sind einige praktische Labs, um Ihr Verständnis der Dateisysteminteraktionen zu festigen, die stark von Systemaufrufen abhängen:

1. **[Navigieren Sie im Dateisystem unter Linux](https://labex.io/de/labs/comptia-navigate-the-filesystem-in-linux-590971)** – Üben Sie wesentliche Befehle wie `ls`, `cd` und `pwd`, um sich in Ihrem Linux-Dateisystem zu bewegen und es zu inspizieren, wobei Sie direkt die Dateisystemdienste des Kernels nutzen.
2. **[Verwalten Sie Dateien und Verzeichnisse unter Linux](https://labex.io/de/labs/comptia-manage-files-and-directories-in-linux-590835)** – Lernen Sie, Dateien und Verzeichnisse mit Befehlen wie `mkdir`, `rm`, `cp` und `mv` zu erstellen, zu entfernen, zu kopieren und zu verschieben, die alle Systemaufrufe zur Ausführung ihrer Aktionen benötigen.
3. **[Finden Sie Dateien und Befehle unter Linux](https://labex.io/de/labs/comptia-find-files-and-commands-in-linux-590834)** – Meistern Sie Techniken zum Auffinden von Dateien und Befehlen mit `find`, `whereis` und `which`, was weiter veranschaulicht, wie Benutzerbefehle Kernel-Dienste nutzen, um mit dem Dateisystem zu interagieren.

Diese Labs helfen Ihnen, die Konzepte der Dateisysteminteraktion in realen Szenarien anzuwenden und Vertrauen in grundlegende Linux-Operationen aufzubauen, die implizit auf Systemaufrufen beruhen.

## Quiz Question

What is used to switch from user mode to kernel mode? Please answer in English, using two words.

## Quiz Answer

System call
