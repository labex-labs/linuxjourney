---
lang: "de"
title: "Umask"
description: "Erfahren Sie, wie Sie den Befehl `umask` verwenden, um die Standard-Dateiberechtigungen in Linux zu steuern. Verstehen Sie numerische Berechtigungen und verwalten Sie den Zugriff auf neue Dateien einfach."
keywords: "umask, linux-berechtigungen, dateiberechtigungen, linux-befehle, linux für anfänger, linux-tutorial, standardberechtigungen"
---

## Lesson Content

Jede Datei, die erstellt wird, erhält einen Standardsatz von Berechtigungen. Wenn Sie diesen Standardsatz von Berechtigungen ändern möchten, können Sie dies mit dem Befehl `umask` tun. Dieser Befehl verwendet den 3-Bit-Berechtigungssatz, den wir bei numerischen Berechtigungen sehen.

Anstatt diese Berechtigungen hinzuzufügen, entzieht `umask` diese Berechtigungen jedoch.

```bash
umask 021
```

Im obigen Beispiel geben wir an, dass die Standardberechtigungen neuer Dateien Benutzern vollen Zugriff ermöglichen sollen, aber für Gruppen möchten wir deren Schreibberechtigung entziehen, und für andere möchten wir deren Ausführungsberechtigung entziehen. Die Standard-`umask` auf den meisten Distributionen ist `022`, was vollen Benutzerzugriff bedeutet, aber keinen Schreibzugriff für Gruppen und andere Benutzer.

Wenn Sie den Befehl `umask` ausführen, wendet er diesen Standardsatz von Berechtigungen auf jede neue Datei an, die Sie erstellen. Wenn Sie jedoch möchten, dass dies dauerhaft ist, müssen Sie Ihre Startdatei (`.profile`) ändern, aber das werden wir in einer späteren Lektion besprechen.

## Exercise

1. Erstellen Sie eine neue Datei und notieren Sie deren Berechtigungen.
2. Ändern Sie die `umask` und erstellen Sie dann eine weitere neue Datei.
3. Überprüfen Sie die Berechtigungen der neuen Datei erneut. Was erwarten Sie zu sehen?

## Quiz Question

Welcher Befehl wird verwendet, um die Standard-Dateiberechtigungen zu ändern?

## Quiz Answer

umask
