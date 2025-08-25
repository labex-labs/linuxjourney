---
index: 3
lang: "de"
title: "Systemaufrufe"
meta_title: "Systemaufrufe - Kernel"
meta_description: "Erfahren Sie mehr über Linux-Systemaufrufe (Syscalls) und wie sie mit dem Kernel interagieren. Verstehen Sie den Benutzer- und Kernelmodus und verwenden Sie `strace` zum Debuggen. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "Linux-Systemaufrufe, Syscalls, Kernelmodus, Benutzermodus, strace-Befehl, Linux-Tutorial, Linux für Anfänger, Linux-Anleitung"
---

## Lesson Content

Erinnern Sie sich an Britney aus der vorherigen Lektion? Nehmen wir an, wir wollen sie sehen und ein paar Drinks zusammen nehmen. Wie kommen wir vom Stehen draußen in der Menschenmenge in ihren innersten Kreis? Wir würden Systemaufrufe verwenden. Systemaufrufe sind wie die VIP-Pässe, die Sie zu einer geheimen Seitentür führen, die direkt zu Britney führt.

Systemaufrufe (syscalls) bieten Prozessen im Benutzerbereich eine Möglichkeit, den Kernel aufzufordern, etwas für uns zu tun. Der Kernel stellt bestimmte Dienste über die Systemaufruf-API zur Verfügung. Diese Dienste ermöglichen es uns, eine Datei zu lesen oder zu schreiben, die Speichernutzung zu ändern, unser Netzwerk zu ändern usw. Die Anzahl der Dienste ist festgelegt, sodass Sie nicht willkürlich Systemaufrufe hinzufügen können. Ihr System verfügt bereits über eine Tabelle der vorhandenen Systemaufrufe, und jeder Systemaufruf hat eine eindeutige ID.

Ich werde nicht auf die Besonderheiten von Systemaufrufen eingehen, da Sie dafür ein wenig C kennen müssten, aber die Grundlagen sind, dass, wenn Sie ein Programm wie `ls` aufrufen, der Code in diesem Programm einen Systemaufruf-Wrapper enthält (also noch nicht den eigentlichen Systemaufruf). Innerhalb dieses Wrappers ruft er den Systemaufruf auf, der einen Trap ausführt. Dieser Trap wird dann vom Systemaufruf-Handler abgefangen und verweist dann auf den Systemaufruf in der Systemaufruftabelle. Nehmen wir an, wir versuchen, den Systemaufruf `stat()` aufzurufen; er wird durch eine Syscall-ID identifiziert, und der Zweck des Systemaufrufs `stat()` ist es, den Status einer Datei abzufragen. Nun, erinnern Sie sich, Sie haben das Programm `ls` im nicht-privilegierten Modus ausgeführt. Es sieht also, dass Sie versuchen, einen Syscall zu machen, und schaltet Sie dann in den Kernel-Modus um. Dort tut es viele Dinge, aber am wichtigsten ist, dass es Ihre Syscall-Nummer nachschlägt, sie in einer Tabelle basierend auf der Syscall-ID findet und dann die Funktion ausführt, die Sie ausführen wollten. Sobald dies geschehen ist, kehrt es in den Benutzermodus zurück, und Ihr Prozess erhält einen Rückgabestatus, ob er erfolgreich war oder ob ein Fehler aufgetreten ist. Die inneren Abläufe von Syscalls werden sehr detailliert; ich würde empfehlen, online nach Informationen zu suchen, wenn Sie mehr erfahren möchten.

Sie können die Systemaufrufe, die ein Prozess macht, tatsächlich mit dem Befehl `strace` anzeigen. Der Befehl `strace` ist nützlich, um zu debuggen, wie ein Programm ausgeführt wurde.

```bash
strace ls
```

## Exercise

Übung macht den Meister! Obwohl die inneren Abläufe von Systemaufrufen komplex sind, ist das Verständnis, wie Benutzerbereichsprogramme mit dem Kernel interagieren, von grundlegender Bedeutung. Der beste Weg, diese Interaktion zu verstehen, ist das Üben mit Befehlen, die diese zugrunde liegenden Operationen ausführen. Hier sind einige praktische Übungen, um Ihr Verständnis der Dateisysteminteraktionen zu vertiefen, die stark auf Systemaufrufen basieren:

1. **[Dateisystem in Linux navigieren](https://labex.io/de/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Üben Sie grundlegende Befehle wie `ls`, `cd` und `pwd`, um sich in Ihrem Linux-Dateisystem zu bewegen und es zu inspizieren, wobei Sie direkt mit den Dateisystemdiensten des Kernels interagieren.
2. **[Dateien und Verzeichnisse in Linux verwalten](https://labex.io/de/labs/comptia-manage-files-and-directories-in-linux-590835)** - Lernen Sie, Dateien und Verzeichnisse mit Befehlen wie `mkdir`, `rm`, `cp` und `mv` zu erstellen, zu entfernen, zu kopieren und zu verschieben, die alle Systemaufrufe zur Ausführung ihrer Aktionen beinhalten.
3. **[Dateien und Befehle in Linux finden](https://labex.io/de/labs/comptia-find-files-and-commands-in-linux-590834)** - Meistern Sie Techniken zum Auffinden von Dateien und Befehlen mit `find`, `whereis` und `which`, was weiter veranschaulicht, wie Benutzerbefehle Kernel-Dienste nutzen, um mit dem Dateisystem zu interagieren.

Diese Labs helfen Ihnen, die Konzepte der Dateisysteminteraktion in realen Szenarien anzuwenden und Vertrauen in grundlegende Linux-Operationen aufzubauen, die implizit auf Systemaufrufen basieren.

## Quiz Question

Was wird verwendet, um vom Benutzermodus in den Kernelmodus zu wechseln?

## Quiz Answer

System call
