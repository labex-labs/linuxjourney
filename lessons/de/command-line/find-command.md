---
lesson_id: "find-command"
course_id: "command-line"
lang: "de"
order_index: 14
title: "find"
description: "Lerne, Verzeichnisbäume nach Name, Typ, Größe und Zeit zu durchsuchen und auf geprüfte Treffer einzuwirken."
meta_title: "find - Kommandozeile"
meta_description: "Lernen Sie den Linux-Befehl find mit Beispielen zum Suchen nach Name, Typ, Größe, Änderungszeit und zum Ausführen von Aktionen auf passenden Dateien."
meta_keywords: "linux find befehl, find befehl, dateien finden linux, nach name finden, nach typ finden, nach größe finden, find mtime, find exec"
---

Der Befehl `find` durchläuft einen Verzeichnisbaum und prüft jeden Eintrag anhand von Kriterien wie Name, Typ, Größe oder Änderungszeit.

## Den Suchort festlegen

Die grundlegende Syntax lautet:

```bash
find [PATH] [EXPRESSION]
```

Der Pfad legt den Startpunkt fest; der Ausdruck wählt darunterliegende Einträge aus oder führt Aktionen auf ihnen aus.

Dieser Befehl durchsucht `/home` und alle Nachkommen nach Einträgen namens `puppies.jpg`:

```bash
$ find /home -name puppies.jpg
```

Die Suche ist standardmäßig rekursiv. Verwende `.` als Startpfad, um den aktuellen Verzeichnisbaum zu durchsuchen.

:::single-choice{#search-current-tree}
Welcher Befehl durchsucht das aktuelle Verzeichnis und seine Nachkommen nach Einträgen namens `notes.txt`?

::option[`find . -name notes.txt`]{#find-current-notes .correct explanation="Der Punkt wählt das aktuelle Verzeichnis als Startpfad; `-name` prüft den Basisnamen jedes Eintrags."}
::option[`find / -name notes.txt`]{#find-root-notes explanation="Der Startpfad `/` durchsucht ab der Wurzel des Dateisystems und damit einen viel größeren Bereich als den aktuellen Verzeichnisbaum."}
::option[`find notes.txt .`]{#find-operands-reversed explanation="`find` erwartet Startpfade vor dem Ausdruck. Diese Reihenfolge beschreibt nicht die verlangte Suche."}
:::

## Namen und Typen abgleichen

Der Test `-name` akzeptiert einen genauen Basisnamen oder ein Shell-ähnliches Muster. Setze Platzhaltermuster in Anführungszeichen, damit die aktuelle Shell sie unverändert an `find` übergibt:

```bash
$ find . -name "*.txt"
```

Ohne Anführungszeichen kann die Shell `*.txt` bereits im aktuellen Verzeichnis erweitern, bevor `find` startet. Verwende `-iname` statt `-name`, wenn beim Namensvergleich die Groß- und Kleinschreibung ignoriert werden soll.

Mit `-type d` wählst du Verzeichnisse, mit `-type f` reguläre Dateien aus:

```bash
$ find /home -type d -name MyFolder
```

Hier müssen beide Tests zutreffen: Der Eintrag muss ein Verzeichnis sein und sein Basisname muss `MyFolder` lauten.

:::single-choice{#find-text-regular-files}
Welcher Befehl findet unterhalb des aktuellen Verzeichnisses reguläre Dateien, deren Namen auf `.txt` enden?

::option[`find . -type f -name "*.txt"`]{#text-files .correct explanation="`-type f` wählt reguläre Dateien aus; das in Anführungszeichen gesetzte `-name`-Muster wird von `find` für jeden Eintrag ausgewertet."}
::option[`find . -type d -name "*.txt"`]{#text-directories explanation="Das Muster ist korrekt geschützt, aber `-type d` wählt Verzeichnisse statt regulärer Dateien aus."}
::option[`find . -type f -name *.txt`]{#unquoted-text-files explanation="Der ungeschützte Platzhalter kann von der aktuellen Shell erweitert werden, bevor `find` läuft, und dadurch den vorgesehenen Ausdruck verändern."}
:::

## Größe und Änderungszeit abgleichen

Bei `-size` steht `+` für größer und `-` für kleiner als die angegebene Einheit:

```bash
$ find . -type f -size +10M
$ find . -type f -size -1k
```

Das große `M` steht hier für Einheiten von 1.048.576 Byte, das kleine `k` für Einheiten von 1.024 Byte. `find` rundet Größen vor dem numerischen Vergleich auf die gewählte Einheit auf; das Verhalten an Grenzen richtet sich daher nach diesen Einheiten.

Mit `-mtime` prüfst du die Anzahl vollständiger 24-Stunden-Zeiträume seit der letzten Dateiänderung:

```bash
$ find . -type f -mtime -7
$ find . -type f -mtime +30
```

`-mtime -7` entspricht einem Wert unter 7, `-mtime +30` einem Wert über 30. Da vollständige 24-Stunden-Zeiträume zählen, orientieren sich diese Tests nicht an Kalendertagen um Mitternacht.

:::single-choice{#find-recent-regular-files}
Welcher Befehl findet unterhalb von `.` reguläre Dateien, deren Änderungsalter weniger als sieben vollständige 24-Stunden-Zeiträume beträgt?

::option[`find . -type f -mtime -7`]{#recent-files .correct explanation="`-type f` wählt reguläre Dateien aus; `-mtime -7` wählt ein Änderungsalter unter sieben vollständigen 24-Stunden-Zeiträumen."}
::option[`find . -type f -mtime +7`]{#older-than-seven explanation="Das Pluszeichen wählt ein Alter über sieben Einheiten aus. Damit werden ältere statt kürzlich geänderter Dateien gesucht."}
::option[`find . -type d -mtime -7`]{#recent-directories explanation="Der Zeittest wählt aktuelle Einträge aus, doch `-type d` beschränkt die Ergebnisse auf Verzeichnisse statt auf reguläre Dateien."}
:::

## Treffer ausgeben und verarbeiten

Wird keine Aktion angegeben, gibt GNU `find` die passenden Pfade aus. Mit einem ausdrücklichen `-print` machst du die Aktion des Ausdrucks deutlich:

Treffer ausdrücklich ausgeben:

```bash
$ find . -name "*.log" -print
```

Mit `-exec` führst du einen anderen Befehl für Treffer aus:

```bash
$ find . -name "*.log" -exec ls -l {} \;
```

Bei der Form mit `\;` wird `{}` in jedem Befehlsaufruf durch einen passenden Pfad ersetzt. Das Semikolon beendet die `-exec`-Aktion und ist maskiert, damit die Shell es an `find` weitergibt.

Bevor du eine destruktive Aktion wie `-delete` oder einen dateiverändernden `-exec`-Befehl verwendest, führe dieselben Tests mit `-print` aus und prüfe jedes Ergebnis. Ein engerer Startpfad und `-maxdepth N` können die Suche zusätzlich begrenzen.

:::single-choice{#verify-before-delete}
Du entwickelst einen `find`-Befehl, der später alte `.log`-Dateien löschen soll. Was solltest du zuerst tun?

::option[Füge sofort `-delete` hinzu und prüfe, welche Dateien verschwinden.]{#delete-first explanation="Eine Löschung ist keine sichere Vorschau und lässt sich nicht eingebaut rückgängig machen. Prüfe die vollständige Treffermenge, bevor du sie hinzufügst."}
::option[Führe dieselben Tests mit `-print` aus und prüfe jeden Treffer.]{#print-first .correct explanation="Eine schreibgeschützte Auflistung bestätigt Startpfad und Tests, bevor eine destruktive Aktion ergänzt wird."}
::option[Starte die Suche bei `/`, damit keine Protokolldatei übersehen wird.]{#root-first explanation="Der Start bei `/` vergrößert den Umfang und kann unabhängige oder geschützte Pfade einschließen. Verwende den engsten geeigneten Startpunkt."}
:::

:::single-choice{#run-ls-for-each-match}
Wofür steht `{}` in `find . -name "*.log" -exec ls -l {} \;`?

::option[Für den aktuellen passenden Pfad, der an `ls -l` übergeben wird.]{#match-placeholder .correct explanation="Bei dieser `-exec`-Form ersetzt `find` `{}` vor dem Aufruf von `ls -l` durch den aktuellen Treffer."}
::option[Für das Verzeichnis, in dem der `find`-Befehl gestartet wurde.]{#starting-placeholder explanation="Das Startverzeichnis ist der Punkt am Anfang des Befehls. Die geschweiften Klammern haben innerhalb von `-exec` eine andere Aufgabe."}
::option[Für das Semikolon, das den `-exec`-Ausdruck beendet.]{#terminator-placeholder explanation="Das maskierte Semikolon beendet die `-exec`-Aktion. Die geschweiften Klammern dienen als Pfadplatzhalter."}
:::

Meldungen wie „Permission denied“ bedeuten meist, dass das aktuelle Konto einen Teil des Baums nicht durchsuchen darf. Bevorzuge einen engeren, relevanten Startpfad und verwende erhöhte Rechte erst, wenn du den erweiterten Zugriff verstehst und bewusst beabsichtigst.

Mit diesen praktischen Übungen kannst du gezielte Suchausdrücke aufbauen:

1. **[Linux find Command: File Searching](https://labex.io/de/labs/linux-linux-find-command-file-searching-219191)** – Lerne den vielseitigen Befehl `find` kennen und nutze `find`, um Dateien sowie Verzeichnisse anhand verschiedener Kriterien zu suchen.
2. **[Discover Critical System Resources](https://labex.io/de/labs/linux-discover-critical-system-resources-388032)** – Nutze unter anderem `find`, um Dateien und ausführbare Programme zu lokalisieren und wichtige Systemressourcen zu entdecken.

## Zusammenfassung

Du kannst nun gezielte `find`-Ausdrücke erstellen und Ergebnisse prüfen, bevor du auf sie einwirkst.

1. Wähle den engsten sinnvollen Startpfad.
2. Schütze Namensmuster mit Anführungszeichen und kombiniere sie mit Typtests.
3. Filtere nach Größe oder vollständigen 24-Stunden-Änderungszeiträumen.
4. Begrenze bei Bedarf die Rekursionstiefe.
5. Gib Treffer aus und prüfe sie vor destruktiven Aktionen.
