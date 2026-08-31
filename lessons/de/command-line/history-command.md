---
lesson_id: "history-command"
course_id: "command-line"
lang: "de"
order_index: 9
title: "history"
description: "Lerne, den Bash-Befehlsverlauf anzuzeigen, zu durchsuchen, wiederzuverwenden und zu verwalten."
meta_title: "history - Kommandozeile"
meta_description: "Lerne den Linux-Befehl history mit Beispielen zum Anzeigen des Befehlsverlaufs, erneuten Ausführen von Befehlen, Rückwärtssuche, Löschen von Einträgen und Leeren des Terminals."
meta_keywords: "linux history befehl, bash history, history -c, history -d, history -w, Ctrl-R, befehlshistorie, clear befehl"
---

Interaktive Shells können die von dir eingegebenen Befehle aufzeichnen. Diese Lektion konzentriert sich auf Bash, wo der eingebaute Befehl `history` diesen Verlauf anzeigt und verwaltet. Andere Shells können andere Tastenkürzel, Dateien oder Einstellungen verwenden.

## Den Bash-Verlauf anzeigen

Führe `history` aus, um die aktuelle Verlaufsliste anzuzeigen:

```bash
$ history
  101  pwd
  102  ls -la
  103  cat notes.txt
```

Jede Zeile enthält eine Verlaufsnummer, gefolgt vom Befehl.

:::single-choice{#show-command-history}
Welcher Bash-Befehl zeigt die aktuelle nummerierte Verlaufsliste an?

::option[`clear`]{#clear-display explanation="`clear` erneuert den sichtbaren Terminalbereich. Vorherige Befehle zeigt der Befehl nicht an."}
::option[`history -w`]{#write-history explanation="`history -w` schreibt die aktuelle Liste in die Verlaufsdatei. Diese Option dient dem Speichern, nicht dem Anzeigen."}
::option[`history`]{#show-history .correct explanation="Der eingebaute Befehl `history` gibt die Befehle der aktuellen Verlaufsliste normalerweise zusammen mit ihren Verlaufsnummern aus."}
:::

## Vorherige Befehle wiederverwenden

Bash bietet mehrere Möglichkeiten, Befehle zurückzuholen oder unmittelbar erneut auszuführen:

- **Pfeil nach oben**: Ruft frühere Befehle zum Prüfen oder Bearbeiten auf.
- **`!!`**: Wird zum zuletzt ausgeführten Befehl erweitert und führt ihn aus.
- **Ausführen nach Nummer**: `!102` führt Befehl Nummer 102 aus dem Verlauf aus.
- **Ausführen nach Präfix**: `!cat` führt den neuesten Befehl aus, der mit `cat` begann.

Verlaufserweiterungen mit `!` können einen Befehl ausführen, sobald du Enter drückst. Prüfe bei Zweifeln zuerst den Treffer – besonders bevor du erhöhte Rechte hinzufügst oder mit wichtigen Dateien arbeitest.

:::single-choice{#repeat-most-recent-command}
Welche Bash-Verlaufserweiterung wiederholt den zuletzt ausgeführten Befehl?

::option[`!102`]{#event-number explanation="Diese Erweiterung wählt den Befehl mit der Verlaufsnummer 102. Dieser Eintrag ist nicht zwangsläufig der neueste."}
::option[`!cat`]{#event-prefix explanation="Damit wird der neueste Befehl gewählt, dessen Text mit `cat` beginnt, nicht der neueste beliebige Befehl."}
::option[`!!`]{#previous-event .correct explanation="In Bash wird `!!` zum vorherigen Befehl erweitert und führt ihn nach dem Absenden der Zeile aus."}
:::

## Den Verlauf interaktiv durchsuchen

Drücke `Ctrl+R`, um eine inkrementelle Rückwärtssuche zu starten, und gib anschließend einen Teil des gesuchten Befehls ein. Mit einem weiteren `Ctrl+R` wechselst du zu einem älteren Treffer.

Mit Enter führst du den angezeigten Treffer aus. Möchtest du ihn vorher prüfen oder bearbeiten, übernimmst du ihn mit einer Pfeiltaste in die Bearbeitungszeile.

:::single-choice{#search-before-executing}
Du erinnerst dich an einen Teil eines früheren Bash-Befehls und möchtest ihn interaktiv suchen. Was drückst du zuerst?

::option[`Ctrl+D`]{#end-input explanation="`Ctrl+D` signalisiert in vielen Terminalkontexten das Ende der Eingabe und kann eine unbeschäftigte Shell beenden. Eine Verlaufssuche startet es nicht."}
::option[`Ctrl+C`]{#cancel-input explanation="`Ctrl+C` unterbricht oder verwirft normalerweise den aktuellen Vorgang. Der Befehlsverlauf wird damit nicht durchsucht."}
::option[`Ctrl+R`]{#reverse-search .correct explanation="`Ctrl+R` startet eine inkrementelle Rückwärtssuche im Befehlsverlauf. Weitere eingegebene Zeichen grenzen den Treffer ein."}
:::

## Die Verlaufsliste verwalten

Der eingebaute Befehl `history` kann die aktuelle Liste verändern oder speichern:

- `history -c`: Leert die aktuelle Verlaufsliste im Arbeitsspeicher.
- `history -w`: Schreibt die aktuelle Liste in die konfigurierte Verlaufsdatei, üblicherweise `~/.bash_history`.
- `history -d <offset>`: Löscht den Eintrag an der angegebenen Verlaufsposition.

Beispiele:

```bash
$ history -d 101
$ history -w
```

Das Leeren der Liste im Arbeitsspeicher garantiert nicht, dass ältere Befehle auch aus allen Dateien, Sicherungen oder anderen aktiven Shells verschwunden sind. Das genaue Verhalten hängt außerdem von den Bash-Einstellungen und davon ab, wann Sitzungen ihre Verlaufsdateien lesen oder schreiben.

:::single-choice{#save-current-history-list}
Welcher Befehl schreibt die aktuelle Bash-Verlaufsliste in die konfigurierte Verlaufsdatei?

::option[`history -c`]{#clear-current-list explanation="Die Option `-c` leert die Liste im Arbeitsspeicher. Sie fordert nicht das Speichern der aktuellen Liste an."}
::option[`history -d 101`]{#delete-one-entry explanation="Die Option `-d` entfernt einen ausgewählten Verlaufseintrag. Sie speichert nicht die vollständige Liste."}
::option[`history -w`]{#write-current-list .correct explanation="Die Option `-w` schreibt die aktuelle Verlaufsliste in die konfigurierte Verlaufsdatei."}
:::

## Die Anzeige leeren und Namen vervollständigen

Verwende `clear`, wenn du einen frischen sichtbaren Terminalbereich möchtest:

```bash
$ clear
```

Dadurch wird die Bash-Verlaufsliste nicht gelöscht. Je nach Terminal bleiben ältere Bildschirminhalte außerdem im Scrollback erreichbar.

Mit der Tab-Vervollständigung musst du weniger tippen. Beginne einen Befehl, Datei- oder Verzeichnisnamen und drücke Tab. Bash vervollständigt einen eindeutigen Treffer oder zeigt mögliche Ergänzungen an, wenn mehrere vorhanden sind.

Befehlszeilen können im Verlauf gespeichert werden. Gib Passwörter, Tokens und andere Geheimnisse deshalb nicht direkt in Befehlen an, wenn eine sicherere Eingabemethode verfügbar ist.

:::single-choice{#distinguish-clear-from-history-clear}
Du möchtest den sichtbaren Terminalbereich erneuern, ohne den Befehlsverlauf im Arbeitsspeicher zu löschen. Welchen Befehl führst du aus?

::option[`clear`]{#clear-visible-area .correct explanation="`clear` erneuert den sichtbaren Terminalbereich, lässt die Bash-Verlaufsliste im Arbeitsspeicher aber unverändert."}
::option[`history -c`]{#clear-memory explanation="Dieser Befehl entfernt Einträge aus der aktuellen Verlaufsliste im Arbeitsspeicher. Er verändert den Verlauf, statt nur die Anzeige zu erneuern."}
::option[`history -d 1`]{#delete-first-entry explanation="Damit wird Bash angewiesen, einen bestimmten Verlaufseintrag zu löschen. Der sichtbare Terminalbereich wird nicht geleert."}
:::

## Zusammenfassung

Du kannst nun Bash-Befehle finden und wiederverwenden und den Verlauf bewusst verwalten.

1. Zeige die aktuelle nummerierte Verlaufsliste an.
2. Hole einen früheren Befehl vorsichtig zurück oder erweitere ihn.
3. Durchsuche den Verlauf interaktiv mit `Ctrl+R`.
4. Lösche, leere oder speichere Verlaufseinträge.
5. Unterscheide zwischen Befehlsverlauf und Terminalanzeige.
