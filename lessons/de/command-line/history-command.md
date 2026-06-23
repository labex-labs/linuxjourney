---
index: 9
lang: "de"
title: "history"
meta_title: "history - Kommandozeile"
meta_description: "Lerne den Linux-Befehl history mit Beispielen zum Anzeigen des Befehlsverlaufs, erneuten Ausführen von Befehlen, Rückwärtssuche, Löschen von Einträgen und Leeren des Terminals."
meta_keywords: "linux history befehl, bash history, history -c, history -d, history -w, Ctrl-R, befehlshistorie, clear befehl"
---

## Lesson Content

Ihre Shell führt eine Aufzeichnung der zuvor eingegebenen Befehle. Sie können auf diese Liste zugreifen, wenn Sie einen Befehl finden und wiederverwenden möchten, ohne ihn erneut eingeben zu müssen. Der Befehl `history` ist ein grundlegendes Werkzeug in Bash und vielen Unix-ähnlichen Shell-Umgebungen.

### Anzeigen Ihres Befehlsverlaufs

Um die Liste der von Ihnen verwendeten Befehle zu sehen, geben Sie `history` ein.

```bash
$ history
  101  pwd
  102  ls -la
  103  cat notes.txt
```

Jede Zeile hat eine Verlaufnummer, gefolgt vom Befehl.

### Vorherige Befehle erneut ausführen

Die Shell bietet mehrere Abkürzungen, um das erneute Ausführen von Befehlen zu erleichtern.

- **Pfeil nach oben**: Möchten Sie denselben Befehl erneut ausführen, den Sie gerade verwendet haben? Drücken Sie einfach die Pfeil-nach-oben-Taste, um rückwärts durch Ihren Verlauf zu blättern.
- **Die `!!` Abkürzung**: Um den zuletzt ausgeführten Befehl erneut auszuführen, können Sie `!!` verwenden. Wenn Sie zum Beispiel gerade `cat file1` ausgeführt haben, führt das Eingeben von `!!` und Drücken der Eingabetaste `cat file1` erneut aus.
- **Ausführen nach Nummer**: Verwenden Sie `!102`, um den Befehl Nummer 102 aus Ihrem Verlauf auszuführen.
- **Ausführen nach Präfix**: Verwenden Sie `!cat`, um den zuletzt ausgeführten Befehl zu starten, der mit `cat` begann.

### Ihren Verlauf durchsuchen

Eine der mächtigsten Verlauf-Abkürzungen ist `Ctrl-R`. Dies startet eine Rückwärtssuche. Nachdem Sie `Ctrl-R` gedrückt haben, beginnen Sie, einen beliebigen Teil des gesuchten Befehls zu tippen, und die Shell zeigt die zuletzt passende Übereinstimmung an. Sie können `Ctrl-R` wiederholt drücken, um ältere Treffer zu durchlaufen. Sobald Sie den gewünschten Befehl gefunden haben, drücken Sie einfach Enter, um ihn auszuführen.

Wenn Sie den gefundenen Befehl vor dem Ausführen bearbeiten möchten, drücken Sie stattdessen die rechte oder linke Pfeiltaste.

### Den Verlauf verwalten

Neben dem bloßen Anzeigen Ihres Verlaufs können Sie ihn auch direkt verwalten.

- **Aktuelle Verlaufsliste löschen**: `history -c` entfernt alle Einträge aus der Verlaufsliste im Speicher.
- **Verlauf in Datei schreiben**: `history -w` speichert den Verlauf der aktuellen Sitzung in Ihrer Verlaufsdatei, normalerweise `~/.bash_history`.
- **Einen bestimmten Eintrag löschen**: `history -d <offset>` entfernt einen Befehl anhand seiner Verlaufnummer.

Beispiele:

```bash
$ history -d 101
$ history -w
```

Seien Sie vorsichtig mit Verlaufserweiterungsbefehlen wie `!!` und `!102`. Verwenden Sie zuerst `history`, um zu bestätigen, was ausgeführt wird.

### Weitere nützliche Terminal-Werkzeuge

Wenn Ihr Terminalfenster voll wird, möchten Sie es vielleicht säubern. Verwenden Sie den Befehl `clear`, um Ihre Anzeige zu löschen und mit einem frischen Bildschirm zu starten.

```bash
$ clear
```

Eine weitere unverzichtbare Funktion ist die Tab-Vervollständigung. Wenn Sie den Anfang eines Befehls, Dateinamens oder Verzeichnisses eingeben und die Tab-Taste drücken, versucht die Shell, diesen automatisch zu vervollständigen. Gibt es mehrere Möglichkeiten, zeigt sie Ihnen diese an oder tut nichts. Ein zweites Drücken der Tab-Taste listet oft alle möglichen Vervollständigungen auf.

### Häufige Fragen

**Wo wird die Bash-Historie gespeichert?** Üblicherweise in `~/.bash_history`, obwohl das genaue Verhalten von den Shell-Einstellungen abhängt.

**Enthält die Historie sofort jeden Befehl?** Nicht immer. Manche Shells schreiben die Historie erst beim Beenden einer Sitzung, sofern nicht anders konfiguriert.

**Kann die Historie sensible Daten enthalten?** Ja. Vermeiden Sie es, Passwörter, Tokens oder Geheimnisse direkt in Befehlen einzugeben.

**Was ist der Unterschied zwischen history -c und clear?** `history -c` löscht die Befehls-Historie im Speicher. `clear` löscht nur den Terminalbildschirm.

## Exercise

Es gibt keine spezifischen Labs zu diesem Thema, aber wir empfehlen, den umfassenden [Linux Learning Path](https://labex.io/de/learn/linux) zu erkunden, um verwandte Linux-Fähigkeiten und Konzepte zu üben.

## Quiz Question

Was ist der Befehl, um das Terminal zu leeren? (Bitte nur Kleinbuchstaben auf Englisch antworten)

## Quiz Answer

clear
