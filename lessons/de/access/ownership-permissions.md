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

### Benutzer- und Gruppenbesitz gleichzeitig ändern

Wenn Sie einen Doppelpunkt und den Gruppennamen nach dem Benutzer hinzufügen, können Sie sowohl den Benutzer als auch die Gruppe gleichzeitig festlegen.

```bash
sudo chown patty:whales myfile
```

## Exercise

Ändern Sie die Gruppe und den Benutzer einiger Testdateien. Überprüfen Sie anschließend die Berechtigungen mit `ls -l`.

## Quiz Question

Welchen Befehl verwenden Sie, um den Benutzerbesitz zu ändern?

## Quiz Answer

chown
