---
lesson_id: "remove-rm-command"
course_id: "command-line"
lang: "de"
order_index: 13
title: "rm (Entfernen)"
description: "Lerne, Dateien und Verzeichnisse zu entfernen, Ziele zu prüfen und sicherere rm-Optionen auszuwählen."
meta_title: "rm (Entfernen) - Kommandozeile"
meta_description: "Lernen Sie den Linux-Befehl rm mit sicheren Beispielen zum Löschen von Dateien, Entfernen von Verzeichnissen, Verwendung von rm -r, rm -i und Vermeidung von rm -rf Fehlern."
meta_keywords: "linux rm befehl, rm befehl, rm -r, rm -i, rm -f, rm -rf, dateien löschen linux, verzeichnis entfernen linux, rmdir"
---

Der Befehl `rm` entfernt Einträge aus dem Dateisystem. Auf der Kommandozeile gelöschte Elemente landen normalerweise nicht im Papierkorb, und `rm` besitzt keine eingebaute Rückgängig-Funktion. Bestätige daher jedes Ziel, bevor du den Befehl ausführst.

Die grundlegende Syntax lautet:

```bash
rm [OPTIONS] FILE...
```

## Dateien entfernen

Übergib `rm` einen oder mehrere Dateipfade:

```bash
$ rm file1
```

```bash
$ rm notes.txt old-report.txt draft.md
```

Prüfe Schreibweise und Ort, bevor du Enter drückst. Eine Sicherung oder eine Kopie in der Versionsverwaltung ist nach dem Löschen verlässlicher als Werkzeuge zur Dateisystemwiederherstellung.

:::single-choice{#remove-one-file} Welcher Befehl entfernt nach einer sorgfältigen Zielprüfung die Datei `old-report.txt`?

::option[`rm old-report.txt`]{#rm-report .correct explanation="`rm` entfernt den benannten Dateieintrag. Normalerweise wird die Datei dabei nicht in einen Papierkorb verschoben."}
::option[`rmdir old-report.txt`]{#rmdir-report explanation="`rmdir` arbeitet mit leeren Verzeichnissen, nicht mit regulären Dateien. Für dieses Ziel ist der Befehl ungeeignet."}
::option[`mv old-report.txt`]{#mv-report explanation="`mv` benötigt ein Ziel und ändert einen Pfad, statt ihn zu löschen. Dieser unvollständige Befehl führt die verlangte Entfernung nicht aus."}
:::

## Platzhalterziele vorab prüfen

Die Shell kann einen Platzhalter zu mehreren Operanden erweitern. Beispielsweise wählt `*.tmp` passende nicht versteckte Namen im aktuellen Verzeichnis aus:

```bash
$ rm *.tmp
```

Zeige dasselbe nicht in Anführungszeichen gesetzte Muster vor dem Entfernen mit `ls` an:

```bash
$ ls *.tmp
cache.tmp  test.tmp
$ rm *.tmp
```

Die Shell erweitert das Muster, bevor `rm` startet. Enthält die Vorschau eine unerwartete Datei, korrigiere das Muster, statt fortzufahren.

:::single-choice{#preview-removal-pattern} Du möchtest `*.tmp` entfernen. Welcher Befehl zeigt zuerst die von diesem Muster ausgewählten nicht versteckten Pfade an, ohne sie zu löschen?

::option[`rm -v *.tmp`]{#verbose-remove explanation="Der ausführliche Modus meldet Entfernungen während ihrer Ausführung. Er löscht die passenden Dateien weiterhin und ist keine schreibgeschützte Vorschau."}
::option[`ls '*.tmp'`]{#quoted-pattern explanation="Anführungszeichen verhindern die Platzhaltererweiterung. So wird nach einem wörtlichen Namen mit `*` gesucht, statt die vorgesehenen Ziele anzuzeigen."}
::option[`ls *.tmp`]{#list-temp-matches .correct explanation="Die Shell erweitert `*.tmp` für `ls`, sodass du vor dem Entfernen dieselben nicht versteckten Treffer prüfen kannst."}
:::

## Eine Bestätigung anfordern

Die Option `-i` fragt vor jeder Entfernung nach:

```bash
$ rm -i important.txt
rm: remove regular file 'important.txt'? y
```

GNU `rm` bietet mit `-I` eine weniger aufdringliche Absicherung: Sie fragt einmal nach, wenn ein Befehl mehr als drei Dateien entfernen oder rekursiv arbeiten würde.

:::single-choice{#confirm-each-removal} Welcher Befehl fragt vor dem Entfernen jeder benannten Datei nach einer Bestätigung?

::option[`rm -i important.txt`]{#interactive-important .correct explanation="Die Option `-i` fragt vor jeder Entfernung nach und gibt dir die Möglichkeit, den Vorgang abzulehnen."}
::option[`rm -f important.txt`]{#force-important explanation="Die Option `-f` unterdrückt Nachfragen und ignoriert ein fehlendes Ziel. Sie entfernt Bestätigungen, statt sie hinzuzufügen."}
::option[`rm -v important.txt`]{#verbose-important explanation="Die Option `-v` meldet, was entfernt wurde, fragt aber nicht vorher nach Zustimmung."}
:::

## Fehlende Dateien mit -f ignorieren

Die Option `-f` ignoriert fehlende Operanden und unterdrückt Nachfragen:

```bash
$ rm -f old-cache.txt
```

Das kann eine skriptgesteuerte Bereinigung wiederholbar machen, wenn eine erzeugte Datei bereits fehlen darf. Da `-f` Bestätigungen entfernt, solltest du die Option nicht nur ergänzen, um einen unverstandenen Fehler zum Schweigen zu bringen.

## Verzeichnisse entfernen

Ein einfaches `rm` entfernt kein Verzeichnis:

```bash
$ rm projects
rm: cannot remove 'projects': Is a directory
```

Verwende `-r` oder `-R` nur dann, wenn du einen Verzeichnisbaum samt seinem gesamten Inhalt entfernen möchtest:

```bash
$ rm -r old-project
```

Für ein leeres Verzeichnis ist `rmdir` die engere Alternative:

```bash
$ rmdir empty-directory
```

`rmdir` schlägt fehl, wenn das Verzeichnis nicht leer ist, und schützt dessen Inhalt dadurch vor einer rekursiven Löschung.

:::single-choice{#remove-empty-directory-only} Welcher Befehl entfernt `old-cache/` nur dann, wenn dieses Verzeichnis leer ist?

::option[`rm -r old-cache/`]{#recursive-cache explanation="Rekursives `rm` entfernt das Verzeichnis und seinen Inhalt. Es erzwingt nicht die Bedingung, dass das Verzeichnis leer sein muss."}
::option[`rmdir old-cache/`]{#rmdir-cache .correct explanation="`rmdir` ist nur bei einem leeren Verzeichnis erfolgreich und löscht deshalb keine darin enthaltenen Dateien rekursiv."}
::option[`rm -f old-cache/`]{#force-cache explanation="Die Option `-f` bewirkt nicht, dass ein einfaches `rm` ein Verzeichnis entfernt. Sie unterdrückt Sicherungen, statt den Leerzustand zu prüfen."}
:::

## Eine rekursive Entfernung prüfen

Rekursives Entfernen kann einen vollständigen Baum löschen. Die Kombination aus `-r` und `-f` unterdrückt zusätzlich Nachfragen, weshalb `rm -rf` eine besonders sorgfältige Zielprüfung verlangt. Prüfe vor jeder rekursiven Entfernung:

- Befindest du dich im erwarteten Verzeichnis? Verwende `pwd`.
- Zeigt `ls -ld -- TARGET` den vorgesehenen obersten Pfad?
- Passt eine schreibgeschützte Vorschau bei einem Platzhalter genau zu deiner Erwartung?
- Ist der Pfad absolut oder relativ? `/tmp/cache` und `tmp/cache` unterscheiden sich grundlegend.
- Gibt es ein versehentliches Leerzeichen? `rm -rf old-project` und `rm -rf old project` betreffen unterschiedliche Pfade.

Setze `--` vor ein Ziel, das mit einem Bindestrich beginnen könnte, damit es nicht als Option interpretiert wird:

```bash
$ rm -- -old-name
```

Greife nicht allein deshalb zu `sudo`, weil `rm` einen Berechtigungsfehler meldet. Prüfe zuerst das Ziel und ermittle, warum dein Konto das enthaltende Verzeichnis nicht ändern darf. Eine rekursive Entfernung mit erhöhten Rechten kann das Betriebssystem oder Daten anderer Benutzer beschädigen.

Mit `-v` meldet `rm` jede erfolgreiche Entfernung:

```bash
$ rm -rv old-project
removed 'old-project/notes.txt'
removed directory 'old-project'
```

:::single-choice{#remove-nonempty-tree} Welcher Befehl entfernt nach vollständiger Zielprüfung `old-project/` samt allen darunterliegenden Inhalten, ohne normale Nachfragen zu unterdrücken?

::option[`rm old-project/`]{#plain-rm-project explanation="Ein einfaches `rm` steigt nicht in ein Verzeichnis hinab und kann daher keinen nicht leeren Baum entfernen."}
::option[`rm -r old-project/`]{#recursive-old-project .correct explanation="Die Option `-r` entfernt den Verzeichnisbaum rekursiv. Anders als `-rf` ergänzt diese Form kein `-f`, das Nachfragen unterdrückt."}
::option[`rmdir old-project/`]{#rmdir-project explanation="`rmdir` setzt ein leeres Verzeichnis voraus und schlägt fehl, wenn das Projekt noch Einträge enthält."}
:::

Mit diesen Übungen kannst du das Entfernen in einer kontrollierten Umgebung trainieren:

1. **[Linux rm Command: File Removing](https://labex.io/de/labs/linux-linux-rm-command-file-removing-209741)** – Entferne mit `rm` Dateien und Verzeichnisse, verwende Optionen wie `-r` und `-i` und übe ein sicheres Vorgehen.
2. **[Organizing Files and Directories](https://labex.io/de/labs/linux-organizing-files-and-directories-387877)** – Wende `rm` in einer praktischen Aufgabe an, um nicht mehr benötigte Verzeichnisse aus einer Projektstruktur zu entfernen.

## Zusammenfassung

Du kannst nun Dateisystemeinträge entfernen und dabei jedes Ziel als unwiderruflich behandeln.

1. Bestätige Dateipfade vor der Entfernung.
2. Prüfe Platzhaltererweiterungen mit einem schreibgeschützten Befehl.
3. Fordere mit `-i` oder `-I` eine Bestätigung an.
4. Bevorzuge `rmdir`, wenn ein Verzeichnis leer sein muss.
5. Prüfe ein vollständiges Ziel vor jeder rekursiven Entfernung.
