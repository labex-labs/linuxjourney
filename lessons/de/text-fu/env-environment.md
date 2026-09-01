---
lesson_id: "env-environment"
course_id: "text-fu"
lang: "de"
order_index: 5
title: "env (Umgebung)"
description: "Lerne, wie Bash Umgebungsvariablen erweitert, exportiert, untersucht und vorübergehend überschreibt."
meta_title: "env (Umgebung) - Text-Fu"
meta_description: "Erfahren Sie, was der env-Befehl in Linux bewirkt. Diese Anleitung erklärt, wie Sie Linux-Umgebungsvariablen wie PATH, HOME und USER mit dem env-Linux-Befehl anzeigen und verwenden."
meta_keywords: "env, linux env, env linux, env befehl linux, linux env befehl, was macht env in linux, umgebungsvariablen, PATH variable, shell variablen"
---

Jeder Prozess besitzt eine Umgebung: eine Sammlung von Name-Wert-Zeichenfolgen, die er von seinem Elternprozess erbt. Shells übergeben damit Einstellungen wie Sprachvorgaben und Suchpfade für ausführbare Dateien an die Programme, die sie starten.

## Variablenwerte in Bash erweitern

Bash ersetzt `$NAME` oder `${NAME}` vor der Ausführung eines Befehls durch den Variablenwert. Setze die Erweiterung in Anführungszeichen, damit der Wert als ein Argument erhalten bleibt:

```bash
$ printf '%s\n' "$HOME"
/home/pete
```

Häufige Umgebungsvariablen sind:

- `HOME`: Pfad zum Home-Verzeichnis des aktuellen Benutzers.
- `USER`: Ein auf vielen Systemen von der Anmeldeumgebung bereitgestellter Benutzername.
- `PWD`: Aktuelles Arbeitsverzeichnis der Shell.
- `PATH`: Verzeichnisse, in denen nach Befehlsnamen gesucht wird.

Die Werte hängen von der Umgebung des aktuellen Prozesses ab und sind keine universellen Konstanten. Eine nicht gesetzte Variable wird als leere Zeichenfolge erweitert, sofern kein strengeres Shell-Verhalten aktiviert ist.

:::single-choice{#env-print-home-value} Welcher Bash-Befehl gibt den Wert von `HOME` aus und bewahrt ihn als ein Argument?

::option[`printf '%s\n' '$HOME'`]{#env-literal-home explanation="Einfache Anführungszeichen verhindern die Parametererweiterung, sodass die wörtlichen Zeichen `$HOME` ausgegeben werden."}
::option[`printf '%s\n' "$HOME"`]{#env-quoted-home .correct explanation="Bash erweitert `$HOME` in doppelten Anführungszeichen; `printf` erhält den vollständigen Wert als ein Argument."}
::option[`printf '%s\n' HOME`]{#env-name-home explanation="Ohne Dollarzeichen oder Parametersyntax ist `HOME` gewöhnlicher Text und keine Variablenerweiterung."}
:::

## Die aktuelle Umgebung untersuchen

Führe `env` ohne Operanden aus, um die Umgebung auszugeben, die der `env`-Prozess geerbt hat:

```bash
$ env
```

Die Ausgabe enthält Einträge im Format `NAME=value`, zum Beispiel:

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

Umgebungsvariablen können Zugangsdaten, Tokens, interne Pfade oder andere vertrauliche Daten enthalten. Veröffentliche keine vollständige `env`-Ausgabe in Issues oder Protokollen, ohne sie zu prüfen und sensible Werte zu entfernen.

:::single-choice{#env-list-exported-values} Welcher Befehl gibt die Umgebung aus, die ein neu gestarteter Prozess sieht?

::option[`env`]{#env-print-all .correct explanation="Ohne Befehl oder Zuweisungen gibt `env` die empfangene Name-Wert-Umgebung aus."}
::option[`alias`]{#env-alias-list explanation="`alias` listet Shell-Aliasdefinitionen auf. Sie gehören zum Shell-Zustand und nicht zu exportierten Umgebungseinträgen."}
::option[`history`]{#env-history-list explanation="`history` zeigt die von der Shell gemerkten Befehlszeilen an. Exportierte Variablen zählt der Befehl nicht auf."}
:::

## Befehle über PATH finden

`PATH` ist eine durch Doppelpunkte getrennte Verzeichnisliste, die Bash durchsucht, wenn ein Befehlsname keinen Schrägstrich enthält:

```bash
$ printf '%s\n' "$PATH"
```

Die Reihenfolge ist wichtig: Bash verwendet nach ihren Auflösungsregeln den ersten geeigneten Befehl. Mit `type -a NAME` kannst du prüfen, wie die aktuelle Shell einen Namen auflöst.

So stellst du `/opt/coolapp/bin` für die aktuelle Shell und ihre künftigen Kindprozesse voran und behältst den vorhandenen Suchpfad:

```bash
$ export PATH="/opt/coolapp/bin:$PATH"
```

Ersetze `PATH` nicht versehentlich ausschließlich durch das neue Verzeichnis und füge keine nicht vertrauenswürdigen beschreibbaren Verzeichnisse hinzu. Andernfalls können normale Befehle unauffindbar werden oder unerwartete Programme ausgeführt werden.

:::single-choice{#env-prepend-path-directory} Welcher Befehl setzt `/opt/coolapp/bin` vor den vorhandenen `PATH` der aktuellen Bash und ihrer künftigen Kindprozesse?

::option[`export PATH="/opt/coolapp/bin"`]{#env-replace-path explanation="Damit gehen alle vorhandenen Suchverzeichnisse verloren, sodass gewöhnliche Befehle schwer auffindbar werden können."}
::option[`export PATH="/opt/coolapp/bin:$PATH"`]{#env-export-path .correct explanation="Diese Form setzt das neue Verzeichnis voran, bewahrt den bisherigen Wert und exportiert das Ergebnis für Kindprozesse."}
::option[`PATH='$PATH:/opt/coolapp/bin'`]{#env-literal-path explanation="Einfache Anführungszeichen erhalten den wörtlichen Text `$PATH`; außerdem wird die Zuweisung nicht an künftige Kindprozesse exportiert."}
:::

## Eine Variable an Kindprozesse exportieren

Bash-Variablen gehören nicht automatisch zur Umgebung von Kindprozessen. Markiere einen Namen mit `export` für die Vererbung:

```bash
$ export TEST=test
```

Die aktuelle Bash besitzt nun eine Variable namens `TEST`, und von ihr gestartete Befehle erben `TEST=test`. Ein Kindprozess kann über diesen Mechanismus die Umgebung seines Elternprozesses nicht verändern.

```bash
$ printenv TEST
test
```

Die Zuweisung bleibt normalerweise bestehen, bis du sie mit unset entfernst oder die Shell beendest. Eine systemweite Umgebung verändert sie nicht.

:::single-choice{#env-export-inheritance} Was ist die wichtigste Wirkung von `export TEST=test` in Bash?

::option[Der Befehl schreibt `TEST` in die Systemkonfiguration aller Benutzer.]{#env-system-wide explanation="Die Zuweisung betrifft die aktuelle Shell und die Vererbung an ihre Kinder, nicht alle Benutzer oder das gesamte Betriebssystem."}
::option[Der Befehl markiert `TEST=test` zur Vererbung an künftige Kindprozesse.]{#env-child-inheritance .correct explanation="`export` nimmt die Shell-Variable in die Umgebung auf, die Bash an neu gestartete Befehle übergibt."}
::option[Der Befehl verändert die Umgebung bereits laufender Prozesse.]{#env-existing-processes explanation="Bereits laufende unabhängige Prozesse oder Kindprozesse behalten ihre eigene Umgebung. Der Export wirkt auf später gestartete Prozesse."}
:::

## Einen Wert für einen Befehl setzen

Setze Zuweisungen vor einen Befehl, um Werte nur für dessen Umgebung bereitzustellen:

```bash
$ LANG=C sort names.txt
```

Der `LANG`-Wert der aktuellen Shell wird dadurch nicht dauerhaft verändert. Das Dienstprogramm `env` bietet eine weitere ausdrückliche Form:

```bash
$ env LANG=C sort names.txt
```

Mit `env -i COMMAND` startest du einen Befehl mit einer zunächst leeren Umgebung und kannst anschließend erforderliche Zuweisungen ergänzen. Viele Programme sind auf Umgebungswerte angewiesen; verwende diese Option daher bewusst.

:::single-choice{#env-one-command-value} Welcher Befehl führt `sort names.txt` mit `LANG=C` aus, ohne `LANG` der aktuellen Shell dauerhaft zu ändern?

::option[`env LANG=C sort names.txt`]{#env-lang-sort .correct explanation="`env` ergänzt die Zuweisung in der Umgebung des gestarteten Befehls; die Eltern-Shell behält ihren bisherigen Wert."}
::option[`export LANG=C; sort names.txt`]{#env-export-lang explanation="Damit wird `LANG=C` in der aktuellen Shell exportiert und bleibt auch nach dem Ende von `sort` gesetzt."}
::option[`env -i sort names.txt`]{#env-empty-sort explanation="Dieser Befehl beginnt mit einer leeren Umgebung, setzt aber nicht den verlangten Wert `LANG=C`."}
:::

## Persönliche Werte in künftigen Sitzungen laden

Damit eine exportierte Variable in künftigen interaktiven Bash-Sitzungen erneut gesetzt wird, fügst du eine passende `export`-Zeile in die tatsächlich gelesene Startdatei ein, bei interaktiver Bash ohne Login häufig `~/.bashrc`:

```bash
export TEST=test
```

Zsh verwendet häufig `~/.zshrc`, Fish eine andere Syntax und Konfiguration. Login- und nicht interaktive Shells können weitere Dateien lesen. Ermittle daher Shell und Sitzungstyp, statt anzunehmen, dass eine Datei jeden Prozess konfiguriert.

Mit diesen Übungen kannst du Vererbung und Shell-Konfiguration praktisch trainieren:

1. **[Shell-Umgebung und Konfiguration in Linux verwalten](https://labex.io/de/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** – Erstelle und verwalte lokale sowie Umgebungsvariablen, untersuche ihre Vererbung und mache Einstellungen über `.bashrc` dauerhaft.
2. **[Umgebungsvariablen in Linux](https://labex.io/de/labs/linux-environment-variables-in-linux-385274)** – Lerne Umgebungsvariablen zu erstellen, zu ändern und zu verwalten und verstehe ihre Rolle in der Systemkonfiguration.

## Zusammenfassung

Du kannst nun die von Bash an Kindprozesse übergebene Umgebung untersuchen und steuern.

1. Erweitere Variablenwerte mit bewusst gesetzten Anführungszeichen.
2. Prüfe exportierte Werte, ohne Geheimnisse offenzulegen.
3. Bewahre und ordne Befehlsverzeichnisse in `PATH`.
4. Exportiere eine Shell-Variable für künftige Kindprozesse.
5. Überschreibe einen Wert für einen Befehl, ohne die Eltern-Shell zu verändern.
