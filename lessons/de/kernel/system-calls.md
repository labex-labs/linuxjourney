---
title: "Systemaufrufe"
description: "Erfahren Sie mehr über Linux-Systemaufrufe (Syscalls) und wie sie mit dem Kernel interagieren. Verstehen Sie den Benutzer- und Kernel-Modus und verwenden Sie `strace` zum Debuggen. Beginnen Sie Ihre Linux-Reise!"
keywords: "Linux-Systemaufrufe, Syscalls, Kernel-Modus, Benutzer-Modus, strace-Befehl, Linux-Tutorial, Linux für Anfänger, Linux-Anleitung"
---

## Lesson Content

Erinnern Sie sich an Britney aus der vorherigen Lektion? Nehmen wir an, wir wollen sie sehen und ein paar Drinks zusammen nehmen. Wie kommen wir vom Stehen draußen in der Menschenmenge in ihren innersten Kreis? Wir würden Systemaufrufe verwenden. Systemaufrufe sind wie die VIP-Pässe, die Sie zu einer geheimen Seitentür bringen, die direkt zu Britney führt.

Systemaufrufe (syscalls) bieten Prozessen im Benutzerbereich eine Möglichkeit, den Kernel aufzufordern, etwas für uns zu tun. Der Kernel stellt bestimmte Dienste über die Systemaufruf-API zur Verfügung. Diese Dienste ermöglichen es uns, in eine Datei zu lesen oder zu schreiben, die Speichernutzung zu ändern, unser Netzwerk zu ändern usw. Die Anzahl der Dienste ist festgelegt, sodass Sie nicht willkürlich Systemaufrufe hinzufügen können. Ihr System verfügt bereits über eine Tabelle der vorhandenen Systemaufrufe, und jeder Systemaufruf hat eine eindeutige ID.

Ich werde nicht auf die Besonderheiten von Systemaufrufen eingehen, da Sie dafür ein wenig C beherrschen müssten, aber die Grundlagen sind, dass, wenn Sie ein Programm wie `ls` aufrufen, der Code in diesem Programm einen Systemaufruf-Wrapper enthält (also noch nicht den eigentlichen Systemaufruf). Innerhalb dieses Wrappers wird der Systemaufruf aufgerufen, der einen Trap ausführt. Dieser Trap wird dann vom Systemaufruf-Handler abgefangen und verweist dann auf den Systemaufruf in der Systemaufruftabelle. Nehmen wir an, wir versuchen, den `stat()`-Systemaufruf aufzurufen; er wird durch eine Syscall-ID identifiziert, und der Zweck des `stat()`-Systemaufrufs ist es, den Status einer Datei abzufragen. Denken Sie daran, Sie haben das Programm `ls` im nicht-privilegierten Modus ausgeführt. Wenn es nun feststellt, dass Sie einen Syscall ausführen möchten, wechselt es Sie in den Kernel-Modus. Dort tut es viele Dinge, aber am wichtigsten ist, dass es Ihre Syscall-Nummer nachschlägt, sie in einer Tabelle basierend auf der Syscall-ID findet und dann die Funktion ausführt, die Sie ausführen wollten. Sobald dies geschehen ist, kehrt es in den Benutzermodus zurück, und Ihr Prozess erhält einen Rückgabestatus, ob er erfolgreich war oder ob ein Fehler aufgetreten ist. Die inneren Abläufe von Syscalls sind sehr detailliert; ich würde empfehlen, online nach Informationen zu suchen, wenn Sie mehr erfahren möchten.

Sie können die Systemaufrufe, die ein Prozess tätigt, tatsächlich mit dem Befehl `strace` anzeigen. Der Befehl `strace` ist nützlich, um zu debuggen, wie ein Programm ausgeführt wurde.

```bash
strace ls
```

## Exercise

No exercises for this lesson.

## Quiz Question

Was wird verwendet, um vom Benutzermodus in den Kernel-Modus zu wechseln?

## Quiz Answer

System call
