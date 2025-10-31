---
index: 1
lang: "de"
title: "Dateiberechtigungen"
meta_title: "Dateiberechtigungen - Berechtigungen"
meta_description: "Ein wichtiger Teil unseres kompletten Linux-Tutorials. Erfahren Sie mehr über Linux-Dateiberechtigungen, einschließlich der rwx-Bits für Benutzer, Gruppe und andere. Meistern Sie die Ausgabe von `ls -l` und verstehen Sie Dateimodus."
meta_keywords: "Dateiberechtigungen, Linux Dateiberechtigungen, bester Weg, Linux zu lernen, komplettes Linux-Tutorial, rwx Berechtigungen, ls -l Befehl, Dateimodus, Linux Anleitung"
---

## Lesson Content

Unter Linux ist alles eine Datei, und die Verwaltung des Zugriffs auf diese Dateien ist eine entscheidende Fähigkeit. Das Verständnis der **Dateiberechtigungen** ist grundlegend für die Systemsicherheit und -administration. Lassen Sie uns untersuchen, wie man diese Berechtigungen liest und interpretiert.

### Einführung in Dateiberechtigungen

Wenn wir Dateien in einem detaillierten Format auflisten, sehen wir eine Zeichenfolge, die ihre Berechtigungen definiert. Betrachten wir ein Beispiel mit dem Befehl `ls -l`:

```bash
$ ls -l Desktop/
drwxr-xr-x 2 pete penguins 4096 Dez 1 11:45 .
```

Diese Ausgabe liefert eine Fülle von Informationen, aber wir konzentrieren uns auf die erste Spalte, `drwxr-xr-x`, die den Dateityp und seine Berechtigungen darstellt.

### Dekodierung der Berechtigungszeichenfolge

Die Berechtigungszeichenfolge besteht aus vier Hauptteilen. Das erste Zeichen gibt den Dateityp an. In unserem Beispiel bedeutet das **d**, dass `Desktop` ein Verzeichnis ist. Bei einer regulären Datei würden Sie einen Bindestrich (`-`) sehen.

Die nächsten neun Zeichen stellen die eigentlichen **Dateiberechtigungen** dar. Diese sind in drei Sätze von jeweils drei Zeichen unterteilt. Um es klarer zu machen, können wir sie wie folgt visualisieren:

```plaintext
d | rwx | r-x | r-x
```

Jedes Zeichen in diesen Sätzen entspricht einer bestimmten Berechtigung:

- **r**: Leseberechtigung.
- **w**: Schreibberechtigung.
- **x**: Ausführungsberechtigung.
- **-**: Keine Berechtigung erteilt.

Die Bedeutung dieser Berechtigungen kann sich leicht ändern, je nachdem, ob es sich um eine Datei oder ein Verzeichnis handelt. Zum Beispiel erlaubt die Ausführungsberechtigung (`x`) bei einem Verzeichnis, dieses zu betreten, während sie bei einer Datei erlaubt, sie als Programm auszuführen.

### Benutzer-, Gruppen- und Sonstige Berechtigungen

Die drei Berechtigungssätze gelten für unterschiedliche Zugriffsebenen:

1. **Benutzer (Eigentümer)**: Der erste Satz (`rwx`) gilt für den Eigentümer der Datei, in unserem Beispiel `pete`. Der Eigentümer hat Lese-, Schreib- und Ausführungsberechtigungen.
2. **Gruppe**: Der zweite Satz (`r-x`) gilt für die mit der Datei verknüpfte Gruppe, nämlich `penguins`. Mitglieder dieser Gruppe haben Lese- und Ausführungsberechtigungen, können aber nicht in die Datei schreiben.
3. **Sonstige**: Der letzte Satz (`r-x`) gilt für alle anderen Benutzer des Systems. Sie haben Lese- und Ausführungsberechtigungen.

Das Beherrschen der **Dateiberechtigungen** ist ein Kernkonzept, und diese Grundlage ist unerlässlich, wenn Sie mit diesem **kompletten Linux-Tutorial** fortfahren.

## Exercise

Die **beste Methode, um Linux zu lernen**, ist durch praktische Übungen. Diese Übungen helfen Ihnen, Linux **Dateiberechtigungen**, Benutzer und Gruppen zu meistern:

1. **[Linux Benutzergruppe und Dateiberechtigungen](https://labex.io/de/labs/linux-linux-user-group-and-file-permissions-18002)** - Lernen Sie wesentliche Konzepte zur Verwaltung von Linux-Benutzern und -Gruppen kennen, einschließlich der Erstellung von Benutzern, der Überprüfung von Gruppenmitgliedschaften, dem Verständnis von Dateiberechtigungen und der Bearbeitung von Dateieigentümerschaften.
2. **[Neuen Benutzer und Gruppe hinzufügen](https://labex.io/de/labs/linux-add-new-user-and-group-17987)** - Üben Sie das Erstellen neuer Benutzerkonten, das Einrichten benutzerdefinierter Gruppen und die Verwaltung von Gruppenmitgliedschaften, um reale Systemadministrationsaufgaben zu simulieren.
3. **[Eine Datei finden](https://labex.io/de/labs/linux-find-a-file-17993)** - Wenden Sie Ihr Wissen über Dateiberechtigungen an, indem Sie eine bestimmte Datei finden und ihre Zugriffsberechtigung festlegen, um sicherzustellen, dass nur Sie der autorisierte Benutzer sind.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Berechtigungen und Benutzern unter Linux aufzubauen.

## Quiz Question

Welches Berechtigungsbit wird für ausführbar verwendet? Bitte antworten Sie auf Englisch und achten Sie genau auf die Groß- und Kleinschreibung.

## Quiz Answer

x
