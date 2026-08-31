---
lesson_id: "alias-command"
course_id: "command-line"
lang: "de"
order_index: 18
title: "alias"
description: "Lerne, Befehlsaliase in Bash zu erstellen, zu prüfen, dauerhaft zu speichern, zu umgehen und zu entfernen."
meta_title: "alias - Kommandozeile"
meta_description: "Lerne den Linux alias-Befehl mit Beispielen zum Erstellen temporärer Aliase, Speichern von Aliase in .bashrc, Auflisten von Aliase und Entfernen mit unalias."
meta_keywords: "linux alias befehl, alias befehl, bash alias, .bashrc alias, unalias befehl, befehl abkürzung linux, shell alias"
---

Ein Alias weist eine interaktive Shell an, ein Befehlswort vor der Ausführung der Zeile durch eine andere Zeichenfolge zu ersetzen. Damit kannst du häufige Befehle verkürzen oder eine bevorzugte Optionsauswahl hinterlegen.

## Einen Alias in der aktuellen Shell erstellen

In Bash definierst du einen Alias mit `alias NAME='REPLACEMENT'`. Um das Gleichheitszeichen dürfen keine Leerzeichen stehen:

```bash
$ alias ll='ls -la'
```

Nach dieser Definition wird `ll` als Befehl zu `ls -la` erweitert. Die Anführungszeichen halten die Ersetzung während der Definition zusammen.

Aliase eignen sich am besten für einfache Ersetzungen am Befehlsanfang. Verwende eine Shell-Funktion, wenn du Argumente strukturierter verarbeiten musst.

:::single-choice{#define-ll-alias}
Welcher Bash-Befehl definiert `ll` in der aktuellen Shell als Alias für `ls -la`?

::option[`alias ll = 'ls -la'`]{#alias-spaces explanation="Leerzeichen um `=` teilen die Definition in einzelne Shell-Wörter. Bash erhält dadurch keine gültige Aliaszuweisung."}
::option[`alias ll='ls -la'`]{#alias-ll .correct explanation="Diese Form verwendet das erforderliche Muster `NAME=REPLACEMENT` und schützt die Ersetzung mit ihrem Leerzeichen durch Anführungszeichen."}
::option[`unalias ll='ls -la'`]{#unalias-definition explanation="`unalias` entfernt vorhandene Aliasnamen. Eine Ersetzung erstellt der Befehl nicht."}
:::

## Einen Alias in zukünftigen Bash-Sitzungen laden

Ein an der Eingabeaufforderung definierter Alias gehört zur aktuellen Shell und verschwindet, wenn sie beendet wird. Interaktive Bash-Sitzungen ohne Login lesen normalerweise `~/.bashrc`; diese Datei ist daher der übliche Ort für persönliche Bash-Aliase:

```bash
alias ll='ls -la'
```

Starte nach dem Bearbeiten eine neue interaktive Bash-Sitzung oder lade die Datei in der aktuellen Shell erneut:

```bash
$ source ~/.bashrc
```

Das Startverhalten kann je nach Shell, Login-Modus und Distributionskonfiguration variieren. Ein Zsh-Benutzer würde normalerweise die Zsh-Konfiguration statt der Bash-Datei `.bashrc` verwenden.

:::single-choice{#persist-bash-alias}
Wo sollte ein persönlicher Alias normalerweise definiert werden, damit ihn zukünftige interaktive Bash-Sitzungen ohne Login laden?

::option[In der Datei `~/.bashrc` des Benutzers.]{#bashrc-alias .correct explanation="Interaktive Bash-Sitzungen ohne Login lesen normalerweise `~/.bashrc`; deshalb ist sie der übliche Ort für persönliche Bash-Aliase."}
::option[In der ausführbaren Datei des Befehls, für den der Alias gilt.]{#edit-executable explanation="Eine installierte ausführbare Datei zu verändern hat nichts mit der Alias-Erweiterung der Shell zu tun und kann verwaltete Systemdateien beschädigen."}
::option[Im Scrollback-Verlauf des aktuellen Terminals.]{#terminal-scrollback explanation="Der Scrollback zeichnet nur angezeigten Text auf. Bash führt ihn nicht als Startkonfiguration aus."}
:::

## Aliase und Namensauflösung untersuchen

Führe `alias` ohne Argumente aus, um die Aliase der aktuellen Shell aufzulisten:

```bash
$ alias
alias ll='ls -la'
alias grep='grep --color=auto'
```

Mit `type NAME` prüfst du, wie Bash einen bestimmten Namen auflöst:

```bash
$ type ll
ll is aliased to 'ls -la'
```

:::single-choice{#inspect-command-alias}
Welcher Befehl zeigt, ob Bash `ll` derzeit als Alias, Funktion, Builtin oder ausführbare Datei auflöst?

::option[`file ll`]{#file-ll explanation="`file` klassifiziert einen Dateisystempfad. Ein Alias gehört zum Shell-Zustand und muss keiner Datei namens `ll` entsprechen."}
::option[`type ll`]{#type-ll .correct explanation="Das Builtin `type` meldet, wie die aktuelle Bash-Sitzung den Namen `ll` auflöst."}
::option[`whatis ll`]{#whatis-ll explanation="`whatis` fragt Handbuchbeschreibungen ab. Persönliche Aliase besitzen normalerweise keinen Eintrag in dieser Datenbank."}
:::

## Einen Alias umgehen und entfernen

Um einen Alias für eine einzelne Befehlszeile zu umgehen, setzt du einen Backslash vor den Befehlsnamen oder stellst ihm das Bash-Builtin `command` voran:

```bash
$ \ls
$ command ls
```

Das ist hilfreich, wenn du das normale Verhalten des zugrunde liegenden Befehls benötigst. Halte Aliase kurz und vorhersehbar und verstecke kein überraschendes oder destruktives Verhalten hinter vertrauten Befehlsnamen.

:::single-choice{#bypass-ls-alias}
In der aktuellen Bash-Sitzung existiert ein Alias namens `ls`. Welcher Befehl umgeht ihn für einen einzelnen Aufruf?

::option[`alias ls`]{#show-ls-alias explanation="Dieser Befehl gibt die Definition des Alias `ls` aus. Der zugrunde liegende Befehl wird nicht aufgerufen."}
::option[`command ls`]{#command-ls .correct explanation="Da `command` das Befehlswort ist, erweitert Bash das nachfolgende `ls` nicht als Alias und verwendet die normale Befehlsauflösung."}
::option[`source ls`]{#source-ls explanation="`source` liest eine Datei als Shell-Code in die aktuelle Shell ein. Zum sicheren Umgehen eines Alias ist das ungeeignet."}
:::

Mit `unalias` entfernst du einen Alias aus der aktuellen Shell:

```bash
$ unalias ll
```

Bleibt die Definition in `~/.bashrc`, kann eine zukünftige Shell den Alias erneut anlegen. Entferne oder ändere daher auch diese Konfigurationszeile, wenn der Alias dauerhaft verschwinden soll.

:::single-choice{#remove-current-alias}
Welcher Befehl entfernt den Alias `ll` aus der aktuellen Bash-Sitzung?

::option[`unalias ll`]{#unalias-ll .correct explanation="`unalias` löscht den benannten Alias aus der Aliastabelle der aktuellen Shell."}
::option[`alias ll=''`]{#empty-ll explanation="Damit wird der Alias durch eine leere Erweiterung ersetzt, seine Definition aber nicht entfernt."}
::option[`command ll`]{#command-ll explanation="`command` kann die Alias-Erweiterung in dieser Zeile umgehen, löscht den Alias aber nicht aus dem Shell-Zustand."}
:::

## Zusammenfassung

Du kannst Bash nun mit einfachen und nachvollziehbaren Aliasen anpassen.

1. Definiere einen temporären Alias mit korrekten Anführungszeichen.
2. Lade persönliche Aliase in zukünftigen Sitzungen aus `~/.bashrc`.
3. Untersuche Aliase und Befehlsauflösung.
4. Umgehe einen Alias für einen einzelnen Aufruf.
5. Entferne bei Bedarf sowohl die aktive als auch die gespeicherte Definition.
