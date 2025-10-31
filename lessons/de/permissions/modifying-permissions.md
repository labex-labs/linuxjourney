---
index: 2
lang: "de"
title: "Berechtigungen ändern"
meta_title: "Berechtigungen ändern - Berechtigungen"
meta_description: "Erfahren Sie, wie Sie Berechtigungen unter Linux mit dem chmod-Befehl ändern. Diese Anleitung behandelt sowohl symbolische als auch numerische Methoden, um Ihnen bei der sicheren Verwaltung von Datei- und Verzeichniszugriffen zu helfen. Meistern Sie den Prozess zum Ändern von Linux-Berechtigungen für eine bessere Systemadministration."
meta_keywords: "linux berechtigung ändern, berechtigung linux ändern, wie berechtigungen in linux ändern, wie dateiberechtigungen in linux ändern, chmod, dateiberechtigungen, linux sicherheit, symbolische berechtigungen, numerische berechtigungen"
---

## Lesson Content

Wenn Sie die Zugriffsrechte für Dateien oder Verzeichnisse ändern müssen, ist das primäre Werkzeug, das Sie verwenden werden, der Befehl `chmod` (change mode). Zu verstehen, **wie man Berechtigungen unter Linux ändert**, ist eine grundlegende Fähigkeit für jeden Benutzer. Der Befehl `chmod` bietet zwei Hauptmethoden für diese Aufgabe: symbolischer und numerischer Modus.

### Verwendung des Symbolischen Modus

Der symbolische Modus wird oft als lesbarer angesehen, da er Buchstaben zur Darstellung von Benutzern und Berechtigungen verwendet. Sie geben zuerst an, welche Berechtigungsgruppe Sie ändern möchten (Benutzer, Gruppe oder andere), und verwenden dann ein `+`, um eine Berechtigung hinzuzufügen, oder ein `-`, um sie zu entfernen.

- `u` (user/owner - Benutzer/Eigentümer)
- `g` (group - Gruppe)
- `o` (others - Andere)
- `a` (all - Alle: Benutzer, Gruppe und andere)

Sehen wir uns an, **wie man Dateiberechtigungen unter Linux ändert** mit einigen Beispielen.

Um die Ausführungsberechtigung für den Benutzer für eine Datei hinzuzufügen, würden Sie verwenden:

```bash
chmod u+x myfile
```

Dieser Befehl fügt (`+`) die Ausführbarkeitsberechtigung (`x`) für den Benutzer (`u`) bei `myfile` hinzu.

Um eine Berechtigung zu entfernen, verwenden Sie den Operator `-`. Um beispielsweise die Schreibberechtigung für die Gruppe zu entfernen:

```bash
chmod g-w myfile
```

Sie können auch mehrere Berechtigungen gleichzeitig ändern. Der folgende Befehl fügt die Schreibberechtigung sowohl für den Benutzer als auch für die Gruppe hinzu:

```bash
chmod ug+w myfile
```

### Verwendung des Numerischen (Oktalen) Modus

Eine weitere leistungsstarke Möglichkeit, **Berechtigungen unter Linux zu ändern**, bietet der numerische oder oktale Modus. Diese Methode ermöglicht es Ihnen, alle Berechtigungen für den Benutzer, die Gruppe und andere gleichzeitig mit einer dreistelligen Zahl festzulegen.

Die Berechtigungen werden durch die folgenden Werte dargestellt:

- `4`: lesen (r)
- `2`: schreiben (w)
- `1`: ausführen (x)

Um einen Berechtigungssatz festzulegen, addieren Sie die Zahlen zusammen. Um beispielsweise Lese-, Schreib- und Ausführungsberechtigungen zu erteilen, würden Sie `4 + 2 + 1 = 7` verwenden.

Sehen wir uns ein häufiges Beispiel an:

```bash
chmod 755 myfile
```

Wie funktioniert dieser `linux change permission`-Befehl? Lassen Sie uns die Zahl `755` aufschlüsseln:

- **7 (Benutzer):** `4 + 2 + 1` -> Der Benutzer erhält Lese-, Schreib- und Ausführungsberechtigungen (`rwx`).
- **5 (Gruppe):** `4 + 0 + 1` -> Die Gruppe erhält Lese- und Ausführungsberechtigungen (`r-x`).
- **5 (Andere):** `4 + 0 + 1` -> Alle anderen Benutzer erhalten Lese- und Ausführungsberechtigungen (`r-x`).

### Sicherheitsaspekte

Obwohl `chmod` unerlässlich ist, ist es wichtig, es mit Bedacht einzusetzen. Das Ändern von Berechtigungen ohne Verständnis der Auswirkungen kann sensible Dateien unbefugten Änderungen oder Ansichten aussetzen. Beispielsweise ist das rekursive Setzen von `777`-Berechtigungen (`chmod -R 777 /some/directory`) eine übliche, aber gefährliche Praxis, die jedem vollen Lese-, Schreib- und Zugriffsrecht gewährt. Wenden Sie immer das Prinzip der geringsten Privilegien an und gewähren Sie nur die unbedingt notwendigen Berechtigungen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Linux-Dateiberechtigungen zu festigen:

1. **[Linux Benutzergruppe und Dateiberechtigungen](https://labex.io/de/labs/linux-linux-user-group-and-file-permissions-18002)** - Lernen Sie wesentliche Linux-Benutzer- und Gruppenverwaltungskonzepte kennen, einschließlich des Verständnisses von Dateiberechtigungen und der Bearbeitung des Datei-Eigentums. Dieses Labor bietet praktische Erfahrung bei der Sicherung einer Multi-User-Linux-Umgebung.
2. **[Neuen Benutzer und Gruppe hinzufügen](https://labex.io/de/labs/linux-add-new-user-and-group-17987)** - In dieser Herausforderung simulieren Sie das Hinzufügen neuer Teammitglieder zu einer Serverumgebung, erstellen neue Benutzerkonten, richten benutzerdefinierte Gruppen ein und verwalten Gruppenmitgliedschaften, was oft die Festlegung geeigneter Berechtigungen beinhaltet.

Diese Labs helfen Ihnen, die Konzepte von Benutzer-, Gruppen- und anderen Berechtigungen in realen Szenarien anzuwenden und Vertrauen in die Verwaltung des Zugriffs unter Linux aufzubauen.

## Quiz Question

Welche Zahl repräsentiert die Leseberechtigung bei Verwendung des numerischen Formats?

## Quiz Answer

4
