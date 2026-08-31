---
lesson_id: "less-command"
course_id: "command-line"
lang: "de"
order_index: 8
title: "less"
description: "Lerne, lange Textdateien mit less interaktiv zu navigieren, zu durchsuchen und zu verfolgen."
meta_title: "less - Kommandozeile"
meta_description: "Lerne den Linux-Befehl less mit Beispielen zum Anzeigen großer Dateien, Scrollen, Suchen, Springen zu Zeilen, Verfolgen von Logs und Beenden von less."
meta_keywords: "less Befehl, linux less, große Datei anzeigen linux, in less suchen, less beenden, less -N, less +F, Textanzeige linux"
---

Ist eine Textdatei länger als eine Bildschirmseite, kannst du sie mit `less` lesen, ohne dass ihr gesamter Inhalt durch das Terminal scrollt. Sein Name inspirierte den alten Unix-Scherz „less is more“, denn `more` ist ein anderer Pager.

## Eine Datei öffnen

Starte den Pager, indem du ihm einen Dateinamen übergibst:

```bash
$ less /home/pete/Documents/text1
```

Solange `less` aktiv ist, steuern Tastendrücke den Pager, statt gewöhnliche Shell-Befehle zu starten. Erst nach dem Beenden des Pagers kehrst du zur Shell zurück.

:::single-choice{#open-long-file}
Welcher Befehl öffnet `/var/log/syslog` in einem interaktiven Pager?

::option[`less /var/log/syslog`]{#page-log .correct explanation="`less` öffnet die Datei in einem Pager, in dem du navigieren und suchen kannst, bevor du zur Shell zurückkehrst."}
::option[`cat /var/log/syslog`]{#print-log explanation="`cat` sendet die gesamte Datei auf einmal an die Standardausgabe. Interaktive Navigation steht dabei nicht zur Verfügung."}
::option[`file /var/log/syslog`]{#classify-log explanation="`file` meldet den wahrscheinlichen Inhaltstyp. Der Befehl öffnet das Protokoll nicht zum interaktiven Lesen."}
:::

## In less navigieren

Verwende bei geöffnetem Pager diese Tasten:

- Mit `Up`, `Down`, `Page Up` und `Page Down` bewegst du dich zeilen- oder seitenweise.
- Mit `g` springst du an den Anfang.
- Mit `G` springst du ans Ende.
- Mit `u` gehst du einen halben Bildschirm nach oben, mit `d` einen halben Bildschirm nach unten.
- Mit `h` öffnest du die integrierte Hilfe.

:::single-choice{#jump-to-file-end}
Welche Taste springt in `less` direkt ans Dateiende?

::option[`g`]{#lowercase-g explanation="Das kleine `g` springt an den Dateianfang. Die großgeschriebene Variante bewegt sich in die entgegengesetzte Richtung."}
::option[`G`]{#uppercase-g .correct explanation="Das große `G` springt ans Ende der Eingabe. Bei diesem Befehl wird zwischen Groß- und Kleinschreibung unterschieden."}
::option[`h`]{#help-key explanation="Die Taste `h` öffnet die Hilfe des Pagers. Sie springt nicht ans Dateiende."}
:::

## In less suchen

Gib `/` gefolgt von einem Muster ein und drücke Enter, um vorwärts zu suchen. Eine Rückwärtssuche beginnt mit `?`.

- `/search_term`: Sucht vorwärts nach `search_term`.
- `?search_term`: Sucht rückwärts nach `search_term`.
- `n`: Wiederholt die Suche in derselben Richtung.
- `N`: Wiederholt die Suche in der entgegengesetzten Richtung.

:::single-choice{#repeat-search-direction}
Welche Taste wiederholt nach einer Vorwärtssuche nach `error` die Suche in derselben Richtung?

::option[`n`]{#same-search .correct explanation="Das kleine `n` wiederholt die letzte Suche in ihrer ursprünglichen Richtung, hier also vorwärts."}
::option[`N`]{#opposite-search explanation="Das große `N` wiederholt die letzte Suche in der Gegenrichtung. Nach einer Vorwärtssuche bewegt es sich rückwärts durch die Treffer."}
::option[`g`]{#search-to-start explanation="Die Taste `g` springt an den Anfang der Eingabe. Sie wiederholt keine Suche."}
:::

## less verlassen

Drücke `q`, um `less` zu beenden und zur Shell-Eingabeaufforderung zurückzukehren.

:::single-choice{#quit-less}
Welche Taste beendet `less` und kehrt zur Shell zurück?

::option[`q`]{#less-quit .correct explanation="Der Befehl `q` beendet den Pager und stellt die Shell-Eingabeaufforderung wieder her."}
::option[`h`]{#less-help explanation="Die Taste `h` öffnet die Hilfe innerhalb von `less`. Sie führt nicht direkt zur Shell zurück."}
::option[`G`]{#less-end explanation="Das große `G` bewegt sich ans Ende der Eingabe. Der Pager bleibt dabei geöffnet."}
:::

## less mit Optionen starten

Optionen und anfängliche Befehle können beeinflussen, wie der Pager startet:

```bash
$ less -N file.txt
$ less +G file.txt
$ less +F /var/log/syslog
```

- `-N`: Zeigt Zeilennummern an.
- `+G`: Öffnet die Datei an ihrem Ende.
- `+F`: Verfolgt neu hinzukommende Inhalte, ähnlich wie `tail -f`.

Drücke beim Verfolgen mit `+F` zunächst `Ctrl+C`, um zur normalen Navigation zurückzukehren, und anschließend `q`, um den Pager zu beenden. Mit `-i` ignoriert die Suche die Groß- und Kleinschreibung, sofern das Muster keinen Großbuchstaben enthält; `-I` ignoriert sie unabhängig vom Muster.

Auch Befehlsausgaben lassen sich über eine Pipe an `less` senden:

```bash
$ dmesg | less
```

:::single-choice{#follow-growing-log}
Welcher Befehl öffnet `/var/log/syslog` und verfolgt neue Inhalte, sobald sie eintreffen?

::option[`less +F /var/log/syslog`]{#follow-log .correct explanation="Der anfängliche Befehl `+F` aktiviert den Folgemodus, sodass `less` neu angehängte Protokollinhalte anzeigt."}
::option[`less +G /var/log/syslog`]{#open-at-log-end explanation="Der anfängliche Befehl `+G` öffnet die Datei am Ende, verfolgt später eintreffende Inhalte aber nicht fortlaufend."}
::option[`less -N /var/log/syslog`]{#number-log-lines explanation="Die Option `-N` zeigt Zeilennummern an. Sie aktiviert kein fortlaufendes Verfolgen."}
:::

Mit diesen Übungen kannst du das Navigieren, Suchen und Lesen von Systemtexten praktisch trainieren:

1. **[Linux less Command: File Paging](https://labex.io/de/labs/linux-linux-less-command-file-paging-214301)** – Lerne, mit less Textdateien effizient anzuzeigen und darin zu navigieren, zu suchen und Zeilennummern zu verwenden.
2. **[Viewing Log and Configuration Files in Linux](https://labex.io/de/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** – Zeige Protokoll- und Konfigurationsdateien mit Befehlen wie `cat`, `more` und `less` an und navigiere darin.

## Zusammenfassung

Du kannst nun mit `less` lange Dateien untersuchen, ohne das Terminal mit Text zu überfluten.

1. Öffne eine Datei oder eine weitergeleitete Befehlsausgabe im Pager.
2. Navigiere gezielt zu bestimmten Teilen der Eingabe.
3. Suche vorwärts oder rückwärts und wiederhole eine Suche.
4. Zeige Zeilennummern an oder verfolge wachsende Inhalte.
5. Beende den Pager sicher und kehre zur Shell zurück.
