---
index: 3
lang: "de"
title: "Eigentumsberechtigungen"
meta_title: "Eigentumsberechtigungen - Berechtigungen"
meta_description: "Meistern Sie die Linux-Dateiberechtigung, indem Sie lernen, wie Sie die Linux-Befehle chown und chgrp verwenden. Dieses Linux-Tutorial erklärt, wie man die Benutzer- und Gruppenberechtigung für Dateien ändert, eine Schlüsselkompetenz für die Verwaltung von Linux-Berechtigungen."
meta_keywords: "chown, chgrp, linux dateibesitz, dateibesitzer ändern, dateigruppe ändern, linux berechtigungen, linux befehle, linux tutorial, linux anleitung, benutzerberechtigung, gruppenberechtigung"
---

## Lesson Content

In einem Linux-System werden jeder Datei und jedem Verzeichnis ein Besitzer und eine Gruppe zugewiesen. Die Verwaltung der **Linux-Dateiberechtigung** ist eine grundlegende Aufgabe zur Kontrolle des Zugriffs und der Berechtigungen. Sie können sowohl die Benutzer- als auch die Gruppenbesitzerschaft einer Datei mithilfe spezifischer **Linux-Befehle** ändern.

### Benutzerbesitzerschaft ändern

Um die Besitzerschaft einer Datei auf einen anderen Benutzer zu übertragen, verwenden Sie den Befehl `chown` (change owner). Dies ist nützlich, wenn sich die Verantwortlichkeiten eines Benutzers ändern oder wenn Sie die Kontrolle über eine Datei jemand anderem zuweisen müssen. Sie benötigen in der Regel Superuser-Rechte (`sudo`), um den Besitzer einer Datei zu ändern, die Ihnen nicht gehört.

```bash
sudo chown patty myfile
```

Dieser Befehl ändert den Benutzerbesitzer von `myfile` auf den Benutzer `patty`.

### Gruppenbesitzerschaft ändern

Ähnlich können Sie die einer Datei zugeordnete Gruppe mit dem Befehl `chgrp` (change group) ändern. Dies ermöglicht allen Mitgliedern der neuen Gruppe den Zugriff basierend auf den **Linux-Berechtigungen** der Gruppe.

```bash
sudo chgrp whales myfile
```

Dieser Befehl setzt die Gruppenbesitzerschaft von `myfile` auf die Gruppe `whales`.

### Benutzer- und Gruppenbesitzerschaft gleichzeitig ändern

Zur Effizienz ermöglicht der Befehl `chown` die gleichzeitige Änderung der Benutzer- und Gruppenbesitzerschaft in einem einzigen Schritt. Indem Sie den Benutzernamen und den Gruppennamen durch einen Doppelpunkt trennen, können Sie beide Attribute gleichzeitig aktualisieren.

```bash
sudo chown patty:whales myfile
```

Dieser einzelne Befehl weist der Datei `myfile` die Benutzerbesitzerschaft `patty` und die Gruppenbesitzerschaft `whales` zu. Dies ist die gebräuchlichste Methode zur Verwaltung der **Linux-Dateiberechtigung**.

## Exercise

Um Ihr Verständnis der **Linux-Dateiberechtigung** zu festigen, empfehlen wir Ihnen, diese praktischen Labs zu üben. Sie bieten reale Szenarien für die Anwendung der Befehle `chown` und `chgrp`.

1. **[Linux Benutzergruppe und Dateiberechtigungen](https://labex.io/de/labs/linux-linux-user-group-and-file-permissions-18002)** – Lernen Sie wesentliche Linux-Konzepte zur Benutzer- und Gruppenverwaltung kennen, einschließlich des Verständnisses von Dateiberechtigungen und der Manipulation der Dateiberechtigung. Dieses Lab bietet praktische Erfahrung bei der Sicherung einer Multi-User-Linux-Umgebung.
2. **[Neuen Benutzer und neue Gruppe hinzufügen](https://labex.io/de/labs/linux-add-new-user-and-group-17987)** – In dieser Herausforderung simulieren Sie das Hinzufügen neuer Teammitglieder zu einer Serverumgebung, indem Sie neue Benutzerkonten erstellen, benutzerdefinierte Gruppen einrichten und Gruppenmitgliedschaften verwalten. Dies testet Ihre Fähigkeiten in der Linux-Benutzer- und Gruppenadministration.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Verwaltung der Dateiberechtigung und Berechtigungen unter Linux aufzubauen.

## Quiz Question

Welcher Befehl wird verwendet, um die Benutzerbesitzerschaft einer Datei zu ändern? Bitte geben Sie nur den Befehlsnamen in Kleinbuchstaben in englischer Sprache an.

## Quiz Answer

chown
