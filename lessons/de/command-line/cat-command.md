---
lesson_id: "cat-command"
course_id: "command-line"
lang: "de"
order_index: 7
title: "cat"
description: "Lerne, mit cat Dateiinhalte sicher anzuzeigen, zu verketten und umzuleiten."
meta_title: "cat - Kommandozeile"
meta_description: "Lernen Sie den Linux-Befehl cat mit Beispielen zum Anzeigen von Dateien, Verketten von Dateien, Nummerieren von Zeilen, Erstellen von Dateien und sicherer Verwendung von Umleitungen."
meta_keywords: "linux cat befehl, cat befehl, datei anzeigen linux, dateien verketten, cat -n, cat -b, cat umleitung, linux cat"
---

Nachdem du Dateien bestimmen kannst, besteht der nächste Schritt darin, ihren Inhalt zu lesen. `cat` zeigt Dateien an und reiht ihre Inhalte aneinander; sein Name ist die Kurzform von „concatenate“.

## Dateiinhalte anzeigen

In der einfachsten Form zeigt `cat` eine Datei direkt im Terminal an:

```bash
$ cat myfile.txt
```

Der Befehl schreibt die gesamte Datei in die Standardausgabe, hier also ins Terminal. Das eignet sich gut für kurze Texte; lange Dateien können jedoch zu schnell vorbeiscrollen.

:::single-choice{#display-short-file}
Welcher Befehl zeigt `myfile.txt` vollständig im Terminal an?

::option[`file myfile.txt`]{#classify-myfile explanation="`file` meldet den wahrscheinlichen Dateityp. Der Befehl gibt nicht den vollständigen gespeicherten Text aus."}
::option[`touch myfile.txt`]{#update-myfile explanation="`touch` aktualisiert Zeitstempel oder erstellt eine fehlende Datei. Der Befehl zeigt keinen Dateiinhalt an."}
::option[`cat myfile.txt`]{#display-myfile .correct explanation="`cat` liest `myfile.txt` und schreibt den Inhalt in die Standardausgabe, die hier mit dem Terminal verbunden ist."}
:::

## Dateien verketten

Übergibst du `cat` mehrere Dateien, liest der Befehl sie in der angegebenen Reihenfolge und gibt ihre Inhalte nacheinander aus:

```bash
$ cat dogfile birdfile
```

Damit erscheint zuerst `dogfile`, anschließend `birdfile`. Um die kombinierte Ausgabe in einer neuen Datei zu speichern, leitest du die Standardausgabe mit `>` um:

```bash
$ cat dogfile birdfile > animals
```

Die Shell erstellt `animals` beziehungsweise leert eine bereits vorhandene Datei, bevor sie `cat` ausführt, und leitet die kombinierte Ausgabe dorthin. Verwende deshalb keine der Eingabedateien zugleich als Ziel: Sie könnte geleert werden, bevor `cat` sie liest.

:::single-choice{#combine-files-in-order}
Welcher Befehl schreibt erst `part1`, dann `part2` in die neu erstellte oder ersetzte Datei `whole`?

::option[`cat whole > part1 part2`]{#reverse-redirection explanation="Eine Umleitung besitzt genau ein Ziel; die übrigen Wörter werden zu Operanden von `cat`. Dieser Befehl drückt die verlangte Ein- und Ausgabereihenfolge nicht aus."}
::option[`cat part1 part2 > whole`]{#ordered-inputs .correct explanation="`cat` gibt beide Dateien in der aufgeführten Reihenfolge aus und `>` leitet die kombinierte Ausgabe nach `whole` um."}
::option[`cat part2 part1 > whole`]{#reverse-inputs explanation="Dieser Befehl schreibt zwar dieselben Eingaben nach `whole`, liest aber `part2` vor `part1`. Die Operandenreihenfolge bestimmt die Ausgabereihenfolge."}
:::

## Terminaleingaben in eine Datei schreiben

Ohne Eingabedatei liest `cat` aus der Standardeingabe. Zusammen mit `>` kannst du so Text im Terminal eingeben und in eine Datei schreiben:

```bash
$ cat > newfile.txt
```

Gib anschließend den gewünschten Text ein. Mit `Ctrl+D` sendest du ein Dateiende-Signal und kehrst zur Shell zurück. Vorsicht: Existiert `newfile.txt` bereits, löscht `>` den bisherigen Inhalt.

Mit `>>` hängst du neue Eingaben an, statt vorhandene Inhalte zu ersetzen:

```bash
$ cat >> notes.txt
```

:::single-choice{#append-terminal-input}
Du möchtest weiteren Text am Ende einer vorhandenen `notes.txt` eingeben. Welcher Befehl startet diesen Vorgang, ohne die Datei zu leeren?

::option[`cat > notes.txt`]{#overwrite-notes explanation="Ein einzelnes `>` leert das Ziel, bevor die Eingabe dorthin umgeleitet wird. Der vorhandene Text in `notes.txt` ginge verloren."}
::option[`cat >> notes.txt`]{#append-notes .correct explanation="Der Operator `>>` öffnet das Ziel zum Anhängen. Der von `cat` gelesene Text wird daher hinter dem vorhandenen Inhalt ergänzt."}
::option[`cat notes.txt > notes.txt`]{#same-input-output explanation="Dieselbe Datei als Eingabe und als Ziel von `>` zu verwenden kann sie leeren, bevor `cat` sie liest. Das ist kein sicherer Anhängevorgang."}
:::

## Die Ausgabe formatieren

Mehrere Optionen erleichtern die Prüfung der Ausgabe:

- `-n`: Nummeriert alle Ausgabezeilen, beginnend bei 1.
- `-b`: Nummeriert nur nicht leere Ausgabezeilen.
- `-s`: Fasst mehrere aufeinanderfolgende Leerzeilen zu einer zusammen.
- `-A`: Macht nicht druckbare Zeichen, Tabulatoren und Zeilenenden sichtbar.

Beispiele:

```bash
$ cat -n script.sh
$ cat -b notes.txt
$ cat -s messy.txt
```

:::single-choice{#number-nonempty-lines}
Welcher Befehl nummeriert nur die nicht leeren Ausgabezeilen von `notes.txt`?

::option[`cat -b notes.txt`]{#number-nonblank .correct explanation="Die Option `-b` nummeriert nicht leere Ausgabezeilen und lässt Leerzeilen unnummeriert."}
::option[`cat -n notes.txt`]{#number-all-lines explanation="Die Option `-n` nummeriert jede Ausgabezeile, auch leere Zeilen. Sie erfüllt daher nicht die Bedingung „nur nicht leere“."}
::option[`cat -s notes.txt`]{#squeeze-blank-lines explanation="Die Option `-s` reduziert aufeinanderfolgende Leerzeilen auf eine. Sie fügt keine Zeilennummern hinzu."}
:::

## Einen Betrachter für lange Dateien wählen

Verwende `cat`, wenn du die gesamte Ausgabe auf einmal sehen möchtest. Bei langen Dateien ist `less` meist angenehmer, weil du darin scrollen, suchen und die Ansicht verlassen kannst, ohne das Terminal mit Text zu überfluten:

```bash
$ less /var/log/syslog
```

:::single-choice{#choose-viewer-for-long-file}
Welcher Befehl eignet sich besser zum interaktiven Lesen einer langen Protokolldatei?

::option[`less /var/log/syslog`]{#page-through-log .correct explanation="`less` ermöglicht Scrollen, Suchen und ein kontrolliertes Beenden und eignet sich deshalb zum interaktiven Lesen langer Dateien."}
::option[`cat /var/log/syslog`]{#print-entire-log explanation="`cat` schreibt das gesamte Protokoll auf einmal ins Terminal. Bei einer langen Datei kann der Text vorbeiscrollen, bevor du ihn prüfen kannst."}
::option[`touch /var/log/syslog`]{#update-log-time explanation="`touch` ändert Zeitstempel und kann besondere Berechtigungen erfordern. Der Befehl dient nicht zum Lesen des Protokolls."}
:::

Zum Üben des Anzeigens und Verkettens von Dateiinhalten eignen sich diese Labs:

1. **[Linux cat Command: File Concatenating](https://labex.io/de/labs/linux-linux-cat-command-file-concatenating-210986)** – Übe das Anzeigen, Verketten und Verarbeiten von Textdateien mit `cat`.
2. **[Viewing Log and Configuration Files in Linux](https://labex.io/de/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** – Zeige mit Befehlen wie `cat` Systemprotokolle und Konfigurationsdateien effizient an und entnimm ihnen gezielt Informationen.

## Zusammenfassung

Du kannst nun mit `cat` Dateiinhalte anzeigen und verketten und dabei sichere Umleitungen wählen.

1. Zeige den vollständigen Inhalt einer kurzen Datei an.
2. Verkette Dateien in einer bestimmten Reihenfolge.
3. Ersetze oder ergänze ein Ziel bewusst.
4. Nummeriere oder vereinfache Ausgabezeilen.
5. Verwende `less`, wenn interaktives Lesen geeigneter ist.
