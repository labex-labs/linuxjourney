---
lesson_id: "emacs-manipulate-files"
course_id: "advanced-text-fu"
lang: "de"
order_index: 10
title: "Dateien in Emacs verwalten"
description: "Lerne, wie du Dateien in Emacs besuchst und speicherst sowie dateigebundene Puffer umbenennst, neu einliest und überprüfst."
meta_title: "Dateien in Emacs verwalten – Fortgeschrittenes Text-Fu"
meta_description: "Lerne die Dateiverwaltung in Emacs: Dateien mit C-x C-f öffnen, mit C-x C-s speichern und mit C-x C-w unter einem neuen Namen sichern."
meta_keywords: "Emacs, Emacs Datei speichern, Emacs Datei öffnen, Emacs Tutorial, Linux Befehle, Emacs für Anfänger, Emacs Anleitung"
---

Emacs besucht Dateien in Puffern. Beim Bearbeiten ändert sich zunächst der Puffer; beim Speichern wird sein aktueller Inhalt in den zugehörigen Pfad geschrieben. Lies die Meldungen im Minipuffer, denn Berechtigungen, widersprüchliche Änderungen auf dem Datenträger oder andere Fehler können das Schreiben verhindern.

## Eine Datei besuchen

Verwende `C-x C-f`, das `find-file` ausführt. Gib anschließend im Minipuffer einen Pfad ein und drücke Enter:

```text
C-x C-f
```

Emacs öffnet eine vorhandene lesbare Datei in einem Puffer. Fehlt der angegebene Pfad, bereitet Emacs einen neuen dateibesuchenden Puffer vor. Im zweiten Fall existiert auf dem Datenträger noch keine Datei, bis ein Speichervorgang erfolgreich ist.

Bei der Eingabe eines Pfads kannst du die Vervollständigung mit Tab verwenden. Beim Besuch eines Verzeichnisses öffnet Emacs normalerweise Dired, seinen Verzeichniseditor, statt das Verzeichnis als Textdatei zu behandeln.

:::single-choice{#emacs-find-file-key}
Welche Emacs-Tastenfolge fragt nach einem Pfad und besucht ihn?

::option[`C-x C-s`]{#emacs-file-save explanation="Diese Tastenfolge speichert den aktuellen dateibesuchenden Puffer und fragt nicht nach einem anderen zu besuchenden Pfad."}
::option[`C-x C-c`]{#emacs-file-exit explanation="Diese Tastenfolge leitet das Beenden von Emacs ein, statt eine Datei zu öffnen."}
::option[`C-x C-f`]{#emacs-find-file .correct explanation="Diese Tastenfolge führt `find-file` aus und fragt im Minipuffer nach dem zu besuchenden Pfad."}
:::

:::single-choice{#emacs-find-missing-file}
Wann wird die Datei auf dem Datenträger normalerweise angelegt, wenn `C-x C-f` einen noch nicht vorhandenen Pfad besucht?

::option[Erst nachdem der neue Puffer erfolgreich gespeichert wurde.]{#emacs-file-created-on-save .correct explanation="Der Puffer kann Änderungen aufnehmen, bevor eine Datei existiert; erst das Speichern legt sie an."}
::option[Sofort nach der Eingabe des Pfads.]{#emacs-file-created-immediately explanation="Emacs erstellt zunächst einen mit dem neuen Pfad verknüpften Puffer und verschiebt das Anlegen der Datei auf später."}
::option[Erst nachdem Emacs selbst geschlossen wurde.]{#emacs-file-created-on-exit explanation="Beim Beenden kann Emacs zum Speichern auffordern, doch die Datei entsteht durch einen erfolgreichen Speichervorgang und nicht zwangsläufig durch das Schließen von Emacs."}
:::

## Den aktuellen Puffer speichern

Verwende `C-x C-s`, das `save-buffer` ausführt, um den aktuellen dateibesuchenden Puffer zu speichern:

```text
C-x C-s
```

Ist dem Puffer kein Dateiname zugeordnet, fragt Emacs nach einem. Ein erfolgreicher Schreibvorgang entfernt die Änderungsmarkierung des Puffers. Bei einem Fehler bleiben die ungespeicherten Daten im Puffer erhalten und Emacs meldet den Fehler.

:::single-choice{#emacs-save-current-buffer}
Welche Tastenfolge speichert den aktuellen dateibesuchenden Puffer?

::option[`C-x C-s`]{#emacs-save-buffer-key .correct explanation="`C-x C-s` führt `save-buffer` für den aktuellen Puffer aus."}
::option[`C-x C-w`]{#emacs-write-file-key explanation="Diese Tastenfolge fragt nach einem anderen Dateinamen und ändert, welche Datei der Puffer besucht."}
::option[`C-x s`]{#emacs-save-some-key explanation="Diese Tastenfolge prüft mehrere dateibesuchende Puffer und fragt nach deren Speicherung, statt nur den aktuellen Puffer anzusprechen."}
:::

## Unter einem anderen Namen schreiben

Verwende `C-x C-w`, das `write-file` ausführt, um nach einem Pfad gefragt zu werden, den Puffer dorthin zu schreiben und ihn anschließend diese neue Datei besuchen zu lassen:

```text
C-x C-w
```

Das entspricht in Emacs dem Verhalten von „Speichern unter“. Es unterscheidet sich davon, lediglich eine getrennte Kopie zu schreiben und weiterhin den ursprünglichen Pfad zu besuchen.

:::single-choice{#emacs-write-file-as}
Welche Tastenfolge führt für den aktuellen Puffer das übliche „Speichern unter“ aus?

::option[`C-x C-f`]{#emacs-find-file-other explanation="Diese Tastenfolge besucht eine Datei und wechselt dabei möglicherweise zu einem anderen Puffer; sie ist kein „Speichern unter“ für den aktuellen Puffer."}
::option[`C-x k`]{#emacs-write-as-kill-buffer explanation="Diese Tastenfolge fragt nach dem Beenden eines Puffers und kann wegen ungespeicherter Änderungen nachfragen; sie speichert nicht unter einem neuen Namen."}
::option[`C-x C-w`]{#emacs-write-file-answer .correct explanation="`write-file` schreibt unter den ausgewählten Pfad und lässt den Puffer anschließend diese Datei besuchen."}
:::

## Mehrere geänderte Puffer prüfen

Verwende `C-x s`, das `save-some-buffers` ausführt, um geänderte dateibesuchende Puffer zu prüfen:

```text
C-x s
```

Emacs fragt normalerweise für jeden infrage kommenden geänderten Puffer, ob er gespeichert werden soll. Lies den Puffernamen und antworte bewusst; dies ist kein bedingungsloser Befehl zum Speichern aller Puffer.

:::single-choice{#emacs-save-some-buffers}
Was bewirkt `C-x s` normalerweise?

::option[Es fragt nach dem Speichern geänderter dateibesuchender Puffer.]{#emacs-prompt-save-some .correct explanation="`save-some-buffers` prüft infrage kommende geänderte Puffer und fragt, welche davon geschrieben werden sollen."}
::option[Es speichert jeden Puffer stillschweigend, ohne Namen anzuzeigen.]{#emacs-silent-save-all explanation="Der normale interaktive Befehl fragt nach, statt jeden Puffer bedingungslos zu schreiben."}
::option[Es schließt alle Puffer, nachdem der aktuelle gespeichert wurde.]{#emacs-close-all-buffers explanation="Der Befehl betrifft das Speichern mehrerer Puffer und schließt sie normalerweise nicht."}
:::

## Den Stand vom Datenträger wiederherstellen

Wenn sich eine Datei auf dem Datenträger geändert hat und du den aktuellen Pufferinhalt bewusst verwerfen möchtest, führe `M-x revert-buffer` aus und prüfe die Bestätigungsfrage. Das erneute Einlesen kann ungespeicherte Änderungen im Puffer zerstören. Verwende es daher erst, nachdem du entschieden hast, welcher Stand gelten soll.

Speichere vor der Entscheidung eine getrennte Kopie oder verwende Versionskontroll- und Diff-Werkzeuge für einen Vergleich. Behandle das erneute Laden nicht als harmlosen Vorgang, wenn der Puffer geändert wurde.

## Zusammenfassung

Du kannst nun dateigebundene Puffer verwalten, ohne Besuche und Schreibvorgänge zu verwechseln.

1. Besuche mit `C-x C-f` einen Pfad.
2. Lege eine fehlende Datei erst beim Speichern ihres Puffers an.
3. Speichere den aktuellen Puffer mit `C-x C-s`.
4. Speichere mit `C-x C-w` unter einem neuen besuchten Namen.
5. Prüfe mit `C-x s` mehrere geänderte Puffer.
