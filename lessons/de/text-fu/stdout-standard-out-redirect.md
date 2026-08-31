---
lesson_id: "stdout-standard-out-redirect"
course_id: "text-fu"
lang: "de"
order_index: 1
title: "stdout (Standardausgabe)"
description: "Lerne, wie die Standardausgabe zum Terminal fließt und wie Bash sie in Dateien umleitet."
meta_title: "stdout (Standardausgabe) - Text-Fu"
meta_description: "Beginnen Sie Ihre Reise zum Erlernen von Linux, indem Sie die Standardausgabe (stdout) und I/O-Umleitung meistern. Diese Lektion behandelt, wie man die Ausgabe von Befehlen mithilfe der Operatoren > und >> in Dateien umleitet – eine grundlegende Fähigkeit für jeden Linux-Benutzer."
meta_keywords: "Linux, Linux lernen, stdout, I/O-Umleitung, Standardausgabe, Ausgabe umleiten, bash, Shell-Skripting, Linux-Befehle, Linux-Tutorial"
---

Programme kommunizieren über Ein- und Ausgabeströme. Die Standardausgabe, abgekürzt **stdout**, ist der Strom, über den ein Programm normalerweise seine regulären Ergebnisse ausgibt. In einem Terminal verbindet die Shell diesen Strom zunächst mit der Terminalanzeige.

## In die Standardausgabe schreiben

Der Befehl `echo` schreibt seine Argumente nach stdout:

```bash
$ echo Hello World
Hello World
```

Stdout ist der Dateideskriptor `1`. Diese Zahl wird nützlich, wenn du mehrere Ströme umleitest. Programme können außerdem über die Standardeingabe, stdin, und die Standardfehlerausgabe, stderr, verfügen; die nächsten Lektionen behandeln diese Ströme.

:::single-choice{#stdout-default-destination}
Wohin sendet `echo Hello World` ohne Umleitung normalerweise seine reguläre Ausgabe in einem interaktiven Terminal?

::option[In eine Datei namens `stdout` im aktuellen Verzeichnis.]{#stdout-file explanation="Die Standardausgabe ist ein Strom und keine automatisch erstellte Datei namens `stdout`. Eine Datei wird erst durch eine entsprechende Umleitung verwendet."}
::option[Über die Standardausgabe an das Terminal.]{#stdout-terminal .correct explanation="Die Shell verbindet die Standardausgabe eines Befehls normalerweise mit dem Terminal, weshalb `echo` dort angezeigt wird."}
::option[In den Standardeingabestrom des Befehls.]{#stdout-to-stdin explanation="Die Standardeingabe transportiert Daten in ein Programm hinein. `echo` sendet sein reguläres Ergebnis über stdout hinaus."}
:::

## Eine Datei mit > ersetzen

Bash interpretiert `>` als Operator zur Ausgabeumleitung. Die Shell öffnet die Zieldatei und verbindet die Standardausgabe des Befehls mit ihr:

```bash
$ echo Hello World > peanuts.txt
```

Der Text erscheint nicht mehr im Terminal, weil stdout nun nach `peanuts.txt` fließt. Fehlt die Datei, wird sie von der Shell erstellt. Existiert sie bereits, leert die Shell sie vor der Ausgabe des Befehls; ihr vorheriger Inhalt geht verloren.

Prüfe das Ergebnis mit `cat`:

```bash
$ cat peanuts.txt
Hello World
```

:::single-choice{#stdout-replace-file}
`notes.txt` enthält bereits Text. Was bewirkt `echo new > notes.txt`?

::option[Der Dateiinhalt wird durch `new` ersetzt.]{#stdout-replace-existing .correct explanation="Für `>` leert die Shell das vorhandene Ziel und leitet die Ausgabe von `echo` anschließend in die nun leere Datei."}
::option[`new` wird hinter dem vorhandenen Text ergänzt.]{#stdout-add-existing explanation="Zum Anhängen ist `>>` erforderlich. Ein einzelnes `>` bewahrt den bisherigen Inhalt des Ziels nicht."}
::option[`new` wird angezeigt, ohne die Datei zu verändern.]{#stdout-display-only explanation="Die Umleitung sendet stdout nach `notes.txt`; die reguläre Ausgabe verbleibt daher nicht im Terminal."}
:::

Da die Shell das Ziel öffnet, bevor der Befehl läuft, solltest du den Pfad vor dem Drücken von Enter prüfen. Eine falsch geschriebene oder unbeabsichtigte vorhandene Datei kann selbst dann geleert werden, wenn der Befehl später fehlschlägt.

## Mit >> an eine Datei anhängen

Verwende `>>`, wenn eine neue Standardausgabe hinter den vorhandenen Dateiinhalt gesetzt werden soll:

```bash
$ echo Another line >> peanuts.txt
$ cat peanuts.txt
Hello World
Another line
```

Wie `>` erstellt auch `>>` ein fehlendes Ziel. Der Unterschied besteht darin, wie eine vorhandene Datei geöffnet wird: `>>` hängt an, statt sie zu leeren.

:::single-choice{#stdout-append-file}
Welcher Befehl fügt `Finished` am Ende von `status.log` hinzu, ohne vorhandenen Inhalt zu löschen?

::option[`echo Finished > status.log`]{#stdout-truncate-status explanation="Ein einzelnes `>` leert ein vorhandenes Ziel vor dem Schreiben. Der bisherige Protokollinhalt würde verloren gehen."}
::option[`echo Finished >> status.log`]{#stdout-append-status .correct explanation="`echo` erzeugt den Text und `>>` hängt diese Standardausgabe an die Zieldatei an."}
::option[`cat Finished >> status.log`]{#stdout-cat-filename explanation="Dieser Befehl fordert `cat` auf, eine Datei namens `Finished` zu lesen. Den verlangten Text erzeugt er nicht als Standardausgabe."}
:::

## Die Umleitung ist Aufgabe der Shell

Die Shell erkennt `>` und `>>`, entfernt die Operatoren aus den an das Programm übergebenen Argumenten, öffnet die Datei und richtet die Stromverbindung ein. Der Befehl selbst schreibt wie gewohnt in seine Standardausgabe.

Deshalb funktioniert dieselbe Umleitungssyntax mit vielen Befehlen:

```bash
$ pwd > current-directory.txt
$ ls -la >> directory-list.txt
```

:::single-choice{#stdout-shell-role}
Wer interpretiert normalerweise `>` in `pwd > current-directory.txt`?

::option[Der Befehl `pwd`, nachdem er `>` als Argument erhalten hat.]{#stdout-pwd-redirection explanation="Die Shell verbraucht die Umleitungssyntax. `pwd` erhält deshalb normalerweise weder `>` noch das Ziel als gewöhnliche Argumente."}
::option[Die Bash-Shell, bevor sie `pwd` startet.]{#stdout-bash-redirection .correct explanation="Bash öffnet das Ziel und verbindet den Dateideskriptor 1, bevor der Befehl ausgeführt wird."}
::option[Das Terminal, nachdem `pwd` den Pfad auf dem Bildschirm ausgegeben hat.]{#stdout-terminal-redirection explanation="Der Strom wird vor der Ausgabe umgeleitet, weshalb das Terminal diese Standardausgabe gar nicht erst erhält."}
:::

Mit dieser Übung kannst du die Steuerung von stdout, stderr und stdin praktisch trainieren:

1. **[Eingabe und Ausgabe in Linux umleiten](https://labex.io/de/labs/comptia-redirecting-input-and-output-in-linux-590840)** – Steuere Standardausgabe, Standardfehler und Standardeingabe mit Operatoren wie `>`, `>>` und `2>` sowie dem Befehl `tee`.

## Zusammenfassung

Du kannst nun die Standardausgabe eines Befehls umleiten und Ersetzen von Anhängen unterscheiden.

1. Erkenne stdout als Strom für reguläre Befehlsergebnisse.
2. Ersetze einen Dateiinhalt mit `>`.
3. Bewahre vorhandenen Inhalt und hänge mit `>>` an.
4. Prüfe ein Ziel, bevor die Shell es öffnet.
