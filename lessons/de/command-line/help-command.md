---
lesson_id: "help-command"
course_id: "command-line"
lang: "de"
order_index: 15
title: "help"
description: "Lerne, für einen Befehl zwischen eingebauter Hilfe, Programmnutzung und Handbuchseiten zu wählen."
meta_title: "help - Kommandozeile"
meta_description: "Lernen Sie, wie Sie Linux-Kommandozeilenhilfe mit Bash help, --help-Ausgabe, Manpages und type für Shell-Built-ins und externe Befehle erhalten."
meta_keywords: "linux help befehl, bash help, kommandozeilenhilfe, --help, shell built-in, man befehl, type befehl"
---

Du musst nicht jede Befehlsoption auswendig lernen. Bash und viele installierte Programme können ihre Syntax direkt im Terminal erklären. Welche Hilfequelle passt, hängt jedoch von der Art des Befehls ab.

## Hilfe für Bash-Builtins aufrufen

Bash stellt den eingebauten Befehl `help` für Befehle bereit, die von der Shell selbst implementiert werden. Dazu gehören beispielsweise `cd`, `history` und `type`.

Übergib den Namen des Builtins als Argument:

```bash
$ help echo
```

Die Ausgabe beschreibt Syntax und Verhalten des Builtins. `help` ohne Argument listet die Builtins auf, für die Bash Hilfe bereithält.

:::single-choice{#help-for-bash-cd} Welcher Befehl zeigt den Bash-Hilfeeintrag für das eingebaute `cd` an?

::option[`cd --help`]{#cd-help-option explanation="Einige Builtins erkennen Optionen, doch die dafür vorgesehene Bash-Dokumentationsschnittstelle ist `help` gefolgt vom Namen des Builtins."}
::option[`help cd`]{#help-cd .correct explanation="Das Bash-Builtin `help` sucht die Dokumentation für das benannte Builtin, hier also `cd`."}
::option[`type cd`]{#type-cd explanation="`type` erklärt, wie Bash den Namen `cd` auflöst. Der Befehl identifiziert ihn, zeigt aber nicht den vollständigen Hilfeeintrag."}
:::

## Die Nutzungsübersicht eines Programms anfordern

Viele externe Programme folgen der Konvention, `--help` zu akzeptieren und eine Nutzungsübersicht auszugeben:

```bash
$ ls --help
```

Diese Konvention ist verbreitet, aber nicht universell. Lies Ausgabe und Beendigungsstatus, statt anzunehmen, dass jedes Programm dieselbe Option unterstützt.

:::single-choice{#quick-ls-usage} Welcher Befehl gibt üblicherweise eine kurze Nutzungsübersicht des externen Programms `ls` aus?

::option[`help ls`]{#bash-help-ls explanation="Bash `help` dokumentiert Shell-Builtins. Auf einem typischen System enthält es keine Nutzungsseite des externen Programms `ls`."}
::option[`ls --help`]{#ls-help .correct explanation="GNU `ls` folgt der verbreiteten Konvention `--help` und gibt seine Nutzung und Optionen aus."}
::option[`type --help ls`]{#type-help-ls explanation="Damit fragst du das Builtin `type` nach dessen eigener Optionsverarbeitung, nicht `ls` nach seiner Nutzung."}
:::

## Prüfen, wie Bash einen Namen auflöst

Mit `type` erkennst du, ob Bash einen Namen als Builtin, Alias, Funktion, Schlüsselwort oder ausführbare Datei auflöst:

```bash
$ type cd
cd is a shell builtin
$ type ls
ls is /usr/bin/ls
```

Das genaue Ergebnis kann durch Aliase, Funktionen, installierte Programme und `PATH` variieren. Mit `type -a NAME` zeigt Bash alle bekannten Auflösungen statt nur der zuerst verwendeten an.

:::single-choice{#identify-command-resolution} Du weißt nicht, ob `deploy` ein Alias, eine Funktion, ein Builtin oder eine ausführbare Datei ist. Welcher Bash-Befehl prüft die Auflösung des Namens?

::option[`type deploy`]{#type-deploy .correct explanation="Das Builtin `type` meldet, wie Bash den Befehlsnamen in der aktuellen Shell-Umgebung interpretiert."}
::option[`help deploy`]{#help-deploy explanation="`help` sucht nach Bash-Builtin-Dokumentation. Aliase, Funktionen und externe Dateien identifiziert es im Allgemeinen nicht."}
::option[`deploy --help`]{#deploy-help explanation="Damit versuchst du, den Befehl auszuführen, und bist von seiner eigenen Optionsunterstützung abhängig. Die Namensauflösung durch Bash wird nicht zuerst erklärt."}
:::

## Den passenden Detailgrad wählen

- Verwende `help COMMAND` für ein Bash-Builtin.
- Verwende `COMMAND --help` für eine kurze Übersicht vieler externer Befehle.
- Verwende `man COMMAND` für eine installierte Handbuchseite mit ausführlicher Dokumentation.
- Verwende `whatis COMMAND` für eine einzeilige Beschreibung.

Die nächsten Lektionen behandeln Handbuchseiten und Kurzbeschreibungen ausführlicher.

:::single-choice{#choose-detailed-manual} Du benötigst eine ausführliche Dokumentation des externen Befehls `ls`, nicht nur eine kurze Nutzungsübersicht. Welchen Befehl solltest du versuchen?

::option[`man ls`]{#man-ls .correct explanation="`man ls` öffnet die installierte Handbuchseite, die normalerweise Syntax, Optionen und Verhalten ausführlicher beschreibt."}
::option[`whatis ls`]{#whatis-ls explanation="`whatis` zeigt knappe Beschreibungen von Handbuchseiten. Die verlangte ausführliche Dokumentation liefert es nicht."}
::option[`type ls`]{#type-ls explanation="`type` meldet, wie Bash `ls` auflöst. Das ausführliche Programmhandbuch zeigt der Befehl nicht an."}
:::

## Zusammenfassung

Du kannst nun abhängig von der Namensauflösung durch Bash die passende Hilfequelle wählen.

1. Verwende `help` für Bash-Builtins.
2. Probiere `--help` für eine kurze Programmnutzung.
3. Prüfe die Namensauflösung mit `type`.
4. Öffne ausführliche Dokumentation mit `man`.
