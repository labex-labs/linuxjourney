---
index: 4
lang: "de"
title: "Umask"
meta_title: "Umask - Berechtigungen"
meta_description: "Erfahren Sie, wie Sie den Befehl `umask` verwenden, um Standard-Dateiberechtigungen in Linux zu steuern. Verstehen Sie numerische Berechtigungen und verwalten Sie den Zugriff auf neue Dateien einfach."
meta_keywords: "umask, linux-berechtigungen, dateiberechtigungen, linux-befehle, linux für anfänger, linux-tutorial, standardberechtigungen"
---

## Lesson Content

Jede Datei, die erstellt wird, erhält einen Standardsatz von Berechtigungen. Wenn Sie diesen Standardsatz von Berechtigungen ändern möchten, können Sie dies mit dem Befehl `umask` tun. Dieser Befehl verwendet den 3-Bit-Berechtigungssatz, den wir in numerischen Berechtigungen sehen.

Anstatt diese Berechtigungen hinzuzufügen, entzieht `umask` diese Berechtigungen jedoch.

```bash
umask 021
```

Im obigen Beispiel geben wir an, dass die Standardberechtigungen neuer Dateien dem Benutzer vollen Zugriff erlauben sollen, aber für Gruppen möchten wir deren Schreibberechtigung entziehen, und für andere möchten wir deren Ausführungsberechtigung entziehen. Die Standard-`umask` auf den meisten Distributionen ist `022`, was vollen Benutzerzugriff bedeutet, aber keinen Schreibzugriff für Gruppen und andere Benutzer.

Wenn Sie den Befehl `umask` ausführen, wendet er diesen Standardsatz von Berechtigungen auf jede neue Datei an, die Sie erstellen. Wenn Sie jedoch möchten, dass dies dauerhaft ist, müssen Sie Ihre Startdatei (`.profile`) ändern, aber das werden wir in einer späteren Lektion besprechen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Dateiberechtigungen und deren Beziehung zu Standardeinstellungen zu vertiefen:

1. **[Linux-Benutzergruppe und Dateiberechtigungen](https://labex.io/de/labs/linux-linux-user-group-and-file-permissions-18002)** – Üben Sie das Erstellen und Verwalten von Benutzern, das Erkunden von Gruppenmitgliedschaften, das Verstehen von Dateiberechtigungen und das Bearbeiten des Dateibesitzes. Dieses Labor bietet praktische Erfahrung bei der Sicherung einer Linux-Umgebung mit mehreren Benutzern, was entscheidend ist, um zu verstehen, wie `umask` neue Dateiberechtigungen beeinflusst.

Dieses Labor wird Ihnen helfen, die Konzepte der Dateiberechtigungen in realen Szenarien anzuwenden und Vertrauen im Umgang mit Zugriffsrechten in Linux aufzubauen.

## Quiz Question

Welcher Befehl wird verwendet, um die Standard-Dateiberechtigungen zu ändern?

## Quiz Answer

umask
