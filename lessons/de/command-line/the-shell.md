---
lesson_id: "the-shell"
course_id: "command-line"
lang: "de"
order_index: 1
title: "Die Shell"
description: "Lerne, was die Linux-Shell ist und wie Befehle ausgeführt werden."
meta_title: "Die Shell – Kommandozeile"
meta_description: "Lerne, was die Linux-Shell ist, wie die Bash-Eingabeaufforderung funktioniert und wie du deinen ersten Befehl mit anfängerfreundlichen Kommandozeilenbeispielen ausführst."
meta_keywords: "linux shell, bash shell, kommandozeile, linux terminal, shell prompt, echo befehl, grundlegende linux befehle"
---

## Was ist die Linux-Shell?

Willkommen auf deiner Linux-Reise! Der erste Schritt besteht darin, die Linux-Shell zu verstehen. Eine Shell ist ein Programm, das deine eingegebenen Befehle entgegennimmt, das Betriebssystem mit ihrer Ausführung beauftragt und das Ergebnis anschließend im Terminal ausgibt.

Wenn du bereits grafische Benutzeroberflächen verwendet hast, kennst du das Arbeiten mit Fenstern, Menüs und Schaltflächen. Auf der Kommandozeile gibst du stattdessen präzise Anweisungen ein. Anwendungen mit Namen wie „Terminal“, „Konsole“ oder „Console“ öffnen in der Regel eine Shell-Sitzung für dich.

Das Terminal ist das Fenster oder die Anwendung, in der du schreibst. Die Shell ist dagegen das Programm, das darin ausgeführt wird.

Die Shell ist nützlich, weil sie schnell, skriptfähig und auf nahezu jedem Linux-System verfügbar ist. Mit zunehmender Erfahrung kannst du Befehle kombinieren, um Dateien zu untersuchen, Verzeichnisse zu verwalten, Texte zu durchsuchen, Software zu installieren und wiederkehrende Aufgaben zu automatisieren.

:::single-choice{#distinguish-shell-and-terminal}
Welche Aussage beschreibt das Verhältnis zwischen Terminal und Shell richtig?

::option[Das Terminal stellt das Fenster bereit, in dem die Shell ausgeführt wird.]{#shell-runs-in-terminal .correct explanation="Das Terminal ist die Bedienoberfläche; die Shell ist das darin laufende Programm, das Befehle verarbeitet."}
::option[Das Terminal nimmt Befehle an, während die Shell nur deren Ausgabe anzeigt.]{#terminal-accepts-commands explanation="Damit sind die Rollen vertauscht. Das Terminal stellt die Oberfläche bereit, während die Shell Befehle entgegennimmt und ausführt."}
::option[Terminal und Shell sind zwei Bezeichnungen für dasselbe Programm.]{#terminal-equals-shell explanation="Beide arbeiten zusammen, sind aber nicht dasselbe Programm. Das Terminal öffnet eine Sitzung, in der eine Shell läuft."}
:::

## Mit der Bash-Shell arbeiten

In diesem Kurs konzentrieren wir uns auf Bash, kurz für Bourne Again Shell. Bash gehört zu den verbreitetsten Linux-Shells und bietet eine gute Grundlage, selbst wenn du später `zsh`, `fish` oder eine andere Shell verwendest.

Wenn du ein Terminal öffnest, erscheint die Shell-Eingabeaufforderung, auch Prompt genannt. Ihr Aussehen kann variieren; häufig zeigt sie deinen Benutzernamen, den Hostnamen und das aktuelle Verzeichnis an.

```plaintext
pete@icebox:/home/pete $
```

Das Zeichen `$` zeigt an, dass die Shell Eingaben eines normalen Benutzers erwartet. Bei der Eingabe eines Befehls tippst du dieses Zeichen nicht mit; es wird von der Shell angezeigt. Steht dort stattdessen `#`, arbeitest du üblicherweise als Root-Benutzer, was mehr Rechte, aber auch größere Risiken bedeutet.

:::single-choice{#interpret-dollar-prompt}
Was bedeutet das `$` am Ende der Beispiel-Eingabeaufforderung?

::option[Die Shell läuft mit den Rechten des Root-Benutzers.]{#root-user-ready explanation="Eine Root-Eingabeaufforderung endet normalerweise mit `#` statt mit `$`. Root-Zugriff bringt zusätzliche Rechte und Risiken mit sich."}
::option[Die Shell wartet auf die Eingabe eines normalen Benutzers.]{#normal-user-ready .correct explanation="Das `$` kennzeichnet die Eingabeaufforderung eines normalen Benutzers und zeigt, dass die Shell für einen Befehl bereit ist."}
::option[Der nächste Befehl muss mit einem Dollarzeichen beginnen.]{#type-dollar-first explanation="Das `$` gehört zur Eingabeaufforderung. Du gibst nur den darauf folgenden Befehl ein, nicht das Zeichen selbst."}
:::

Befehle folgen häufig diesem Muster:

```bash
command options arguments
```

In `echo Hello World` ist beispielsweise `echo` der Befehl und `Hello World` der Text, der ihm übergeben wird.

:::single-choice{#identify-command-name}
Welcher Teil von `echo Hello World` ist der Befehlsname?

::option[`Hello`]{#hello-command explanation="`Hello` steht nach dem Befehlsnamen und gehört daher zu dem Text, der an `echo` übergeben wird."}
::option[`World`]{#world-command explanation="Auch `World` ist an `echo` übergebener Text und nicht der Name des ausgeführten Befehls."}
::option[`echo`]{#echo-command .correct explanation="`echo` bezeichnet das Programm, das die Shell ausführen soll. Die nachfolgenden Wörter werden ihm als Argumente übergeben."}
:::

## Dein erster Linux-Befehl

Beginnen wir mit einem der grundlegendsten Linux-Befehle: `echo`. Dieser Befehl gibt den von dir angegebenen Text im Terminal aus.

```bash
$ echo Hello World
Hello World
```

Probiere einige weitere Beispiele aus:

```bash
$ echo Linux is fun
Linux is fun
$ echo "Hello from Bash"
Hello from Bash
```

Anführungszeichen sind hilfreich, wenn die Shell mehrere Wörter als eine zusammengehörige Texteinheit behandeln soll.

:::single-choice{#group-words-with-quotes}
Bei welchem Befehl behandelt die Shell `Hello from Bash` als eine zusammengehörige, in Anführungszeichen gesetzte Texteinheit?

::option[`echo "Hello from Bash"`]{#quoted-words .correct explanation="Die Anführungszeichen fassen die drei Wörter zu einem Argument zusammen, das an `echo` übergeben wird."}
::option[`echo Hello from Bash`]{#unquoted-words explanation="Die sichtbare Ausgabe ist zwar gleich, doch ohne Anführungszeichen behandelt die Shell die Wörter als getrennte Argumente."}
::option[`"echo Hello from Bash"`]{#quoted-command explanation="Wenn die gesamte Zeile in Anführungszeichen steht, sucht die Shell nach einem Befehl mit diesem vollständigen Namen, statt `echo` mit Text auszuführen."}
:::

Zum Üben dieser Fähigkeiten kannst du den umfassenden [![Shell Learning Path](https://labex.io/cdn-cgi/image/width=200,height=200,quality=80,format=auto,onerror=redirect/https://file.labex.io/path/FaVTnI4iqZP0.png)Shell Learning Path](https://labex.io/de/learn/shell) durcharbeiten.

## Häufige Tipps für Einsteiger

- Drücke `Enter`, um einen Befehl auszuführen.
- Rufe mit der Taste `Up Arrow` einen vorherigen Befehl erneut auf.
- Bei Linux wird in Befehlen und Dateinamen zwischen Groß- und Kleinschreibung unterschieden.
- Leerzeichen sind wichtig: `echo hello` und `echohello` sind nicht dasselbe.
- Scheint ein Befehl festzuhängen, kannst du ihn häufig mit `Ctrl-C` abbrechen.

## Zusammenfassung

Du kannst nun die Aufgabe einer Shell erklären und mit einer einfachen Shell-Eingabeaufforderung arbeiten.

1. Unterscheide zwischen Terminal und Shell.
2. Erkenne eine Befehlszeilen-Eingabeaufforderung.
3. Führe mit `echo` einen einfachen Befehl aus.
