---
index: 3
lang: "de"
title: "Besitzberechtigungen"
meta_title: "Besitzberechtigungen - Berechtigungen"
meta_description: "Erfahren Sie, wie Sie den Dateibesitz in Linux mit den Befehlen chown und chgrp ändern. Verstehen Sie Benutzer- und Gruppenberechtigungen mit diesem anfängerfreundlichen Linux-Tutorial."
meta_keywords: "chown, chgrp, Linux Dateibesitz, Linux Berechtigungen, Linux Befehle, Linux für Anfänger, Linux Tutorial, Linux Anleitung"
---

## Lesson Content

Zusätzlich zur Änderung der Berechtigungen für Dateien können Sie auch den Gruppen- und Benutzerbesitz der Datei ändern.

### Benutzerbesitz ändern

```bash
sudo chown patty myfile
```

Dieser Befehl setzt den Besitzer von `myfile` auf `patty`.

### Gruppenbesitz ändern

```bash
sudo chgrp whales myfile
```

Dieser Befehl setzt die Gruppe von `myfile` auf `whales`.

### Gleichzeitiges Ändern von Benutzer- und Gruppenbesitz

Wenn Sie einen Doppelpunkt und einen Gruppennamen nach dem Benutzer hinzufügen, können Sie sowohl den Benutzer als auch die Gruppe gleichzeitig festlegen.

```bash
sudo chown patty:whales myfile
```

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Dateibesitz und Berechtigungen zu vertiefen:

1. **[Linux Benutzergruppen und Dateiberechtigungen](https://labex.io/de/labs/linux-linux-user-group-and-file-permissions-18002)** – Lernen Sie grundlegende Konzepte der Linux-Benutzer- und Gruppenverwaltung, einschließlich des Verständnisses von Dateiberechtigungen und der Manipulation des Dateibesitzes. Dieses Lab bietet praktische Erfahrung bei der Absicherung einer Linux-Umgebung mit mehreren Benutzern.
2. **[Neuen Benutzer und Gruppe hinzufügen](https://labex.io/de/labs/linux-add-new-user-and-group-17987)** – In dieser Herausforderung simulieren Sie das Hinzufügen neuer Teammitglieder zu einer Serverumgebung, indem Sie neue Benutzerkonten erstellen, benutzerdefinierte Gruppen einrichten und Gruppenmitgliedschaften verwalten. Dies wird Ihre Fähigkeiten in der Linux-Benutzer- und Gruppenadministration testen.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Dateibesitz und Berechtigungen in Linux aufzubauen.

## Quiz Question

Welchen Befehl verwenden Sie, um den Benutzerbesitz zu ändern?

## Quiz Answer

chown
