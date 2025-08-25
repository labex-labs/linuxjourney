---
index: 2
lang: "de"
title: "Berechtigungen ändern"
meta_title: "Berechtigungen ändern - Berechtigungen"
meta_description: "Erfahren Sie, wie Sie den Befehl chmod verwenden, um Dateiberechtigungen in Linux zu ändern. Verstehen Sie symbolische und numerische Modi für eine sichere Dateiverwaltung. Beginnen Sie jetzt mit dem Lernen!"
meta_keywords: "chmod Befehl, Linux Berechtigungen, Dateiberechtigungen, chmod Tutorial, Linux Sicherheit, Linux für Anfänger, Linux Anleitung, chmod numerisch"
---

## Lesson Content

Berechtigungen können einfach mit dem Befehl `chmod` geändert werden.

Wählen Sie zuerst aus, welchen Berechtigungssatz Sie ändern möchten: Benutzer, Gruppe oder Andere. Sie können Berechtigungen mit einem `+` oder `-` hinzufügen oder entfernen. Schauen wir uns einige Beispiele an.

### Hinzufügen eines Berechtigungsbits zu einer Datei

```bash
chmod u+x myfile
```

Der obige Befehl liest sich wie folgt: Ändere die Berechtigung für `myfile`, indem das ausführbare Berechtigungsbit zum Benutzersatz hinzugefügt wird. So hat der Benutzer nun die Ausführungsberechtigung für diese Datei!

### Entfernen eines Berechtigungsbits von einer Datei

```bash
chmod u-x myfile
```

### Hinzufügen mehrerer Berechtigungsbits zu einer Datei

```bash
chmod ug+w
```

Es gibt eine weitere Möglichkeit, Berechtigungen im numerischen Format zu ändern. Diese Methode ermöglicht es Ihnen, Berechtigungen auf einmal zu ändern. Anstatt r, w oder x zur Darstellung von Berechtigungen zu verwenden, verwenden Sie eine numerische Darstellung für einen einzelnen Berechtigungssatz. Es ist also nicht nötig, die Gruppe mit `g` oder den Benutzer mit `u` anzugeben.

Die numerischen Darstellungen sind unten aufgeführt:

- 4: Leseberechtigung
- 2: Schreibberechtigung
- 1: Ausführungsberechtigung

Schauen wir uns ein Beispiel an:

```bash
chmod 755 myfile
```

Können Sie erraten, welche Berechtigungen wir dieser Datei geben? Lassen Sie uns dies aufschlüsseln: `755` deckt die Berechtigungen für alle Sätze ab. Die erste Zahl (7) repräsentiert die Benutzerberechtigungen, die zweite Zahl (5) repräsentiert die Gruppenberechtigungen und die letzte 5 repräsentiert die Berechtigungen für Andere.

Warten Sie mal, 7 und 5 waren oben nicht aufgeführt. Woher bekommen wir diese Zahlen? Denken Sie daran, wir kombinieren jetzt alle Berechtigungen zu einer Zahl, also müssen Sie etwas Mathematik anwenden.

7 = 4 + 2 + 1, also ist 7 die Benutzerberechtigung, und sie hat Lese-, Schreib- und Ausführungsberechtigungen.

5 = 4 + 1, die Gruppe hat Lese- und Ausführungsberechtigungen.

5 = 4 + 1, und alle anderen Benutzer haben Lese- und Ausführungsberechtigungen.

Eine Sache ist zu beachten: Es ist keine gute Idee, Berechtigungen willkürlich zu ändern. Sie könnten möglicherweise eine sensible Datei für jedermann zur Änderung freigeben. Oftmals möchten Sie jedoch berechtigterweise Berechtigungen ändern; seien Sie einfach vorsichtig, wenn Sie den Befehl `chmod` verwenden.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Linux-Dateiberechtigungen zu vertiefen:

1. **[Linux Benutzergruppe und Dateiberechtigungen](https://labex.io/de/labs/linux-linux-user-group-and-file-permissions-18002)** - Lernen Sie grundlegende Konzepte der Linux-Benutzer- und Gruppenverwaltung, einschließlich des Verständnisses von Dateiberechtigungen und der Manipulation von Dateibesitz. Dieses Labor bietet praktische Erfahrung in der Sicherung einer Multi-User-Linux-Umgebung.
2. **[Neuen Benutzer und Gruppe hinzufügen](https://labex.io/de/labs/linux-add-new-user-and-group-17987)** - In dieser Herausforderung simulieren Sie das Hinzufügen neuer Teammitglieder zu einer Serverumgebung, das Erstellen neuer Benutzerkonten, das Einrichten benutzerdefinierter Gruppen und das Verwalten von Gruppenmitgliedschaften, was oft das Festlegen geeigneter Berechtigungen beinhaltet.

Diese Labs helfen Ihnen, die Konzepte von Benutzer-, Gruppen- und anderen Berechtigungen in realen Szenarien anzuwenden und Vertrauen im Umgang mit der Zugriffsverwaltung in Linux aufzubauen.

## Quiz Question

Welche Zahl repräsentiert die Leseberechtigung im numerischen Format?

## Quiz Answer

4
