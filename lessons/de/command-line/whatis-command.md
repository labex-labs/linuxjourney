---
lesson_id: "whatis-command"
course_id: "command-line"
lang: "de"
order_index: 17
title: "whatis"
description: "Lerne, knappe Beschreibungen von Handbuchseiten abzurufen und ihre Abschnittsnummern zu deuten."
meta_title: "whatis - Kommandozeile"
meta_description: "Lerne den Linux-Befehl whatis mit Beispielen kennen, um einzeilige Befehlsbeschreibungen aus Manpages zu erhalten und mehrere Handbuchabschnitte zu verstehen."
meta_keywords: "whatis Befehl, linux whatis, Befehlsbeschreibung linux, man page Zusammenfassung, Kommandozeilenhilfe, apropos"
---

Wenn du einen Befehlsnamen wiedererkennst, aber seinen Zweck vergessen hast, liefert `whatis` eine kurze Erinnerung aus der Handbuchdatenbank.

## Einen genauen Namen nachschlagen

Übergib `whatis` einen oder mehrere genaue Themennamen. Jedes Ergebnis stammt aus dem Abschnitt `NAME` einer installierten Handbuchseite:

```bash
$ whatis cat
cat (1)              - concatenate files and print on the standard output
```

Die Ausgabe ist eine Beschreibung, keine Liste von Befehlsoptionen oder Beispielen. Verwende `man cat` oder `cat --help`, wenn du weitere Einzelheiten benötigst.

:::single-choice{#describe-known-command}
Du kennst den Namen `cat` und möchtest seine einzeilige Beschreibung aus dem Handbuch sehen. Welchen Befehl führst du aus?

::option[`man cat`]{#manual-cat explanation="`man cat` öffnet die vollständige Handbuchseite und liefert damit mehr als die verlangte einzeilige Erinnerung."}
::option[`apropos cat`]{#apropos-cat explanation="`apropos` durchsucht Beschreibungen nach einem Stichwort und kann zahlreiche verwandte Themen liefern. Das ist breiter als eine genaue Namenssuche."}
::option[`whatis cat`]{#whatis-cat .correct explanation="`whatis` schlägt den genauen Themennamen nach und gibt dessen knappe Beschreibung aus der Handbuchdatenbank aus."}
:::

## Abschnittsnummern lesen

Existieren Handbuchseiten mit demselben Thema in mehreren Abschnitten, kann `whatis` mehrere Ergebnisse anzeigen:

```bash
$ whatis passwd
passwd (1)           - change user password
passwd (5)           - the password file
```

Die Zahl in Klammern bezeichnet den Handbuchabschnitt. Hier beschreibt `passwd(1)` den Benutzerbefehl und `passwd(5)` ein Dateiformat. Mit `man 1 passwd` oder `man 5 passwd` öffnest du eine Seite gezielt.

:::single-choice{#interpret-whatis-section}
Was bezeichnet `(5)` in der Ausgabe `passwd (5) - the password file`?

::option[Die fünfte Option, die der Befehl `passwd` akzeptiert.]{#fifth-option explanation="Die Zahl ist keine Optionsposition. Optionen werden innerhalb einer ausgewählten Handbuchseite dokumentiert."}
::option[Den Handbuchabschnitt, der die Dateiformatseite enthält.]{#section-five .correct explanation="Abschnitt 5 behandelt Dateiformate und Konventionen; `passwd(5)` verweist daher auf diesen Handbuchabschnitt."}
::option[Fünf Handbuchseiten, die den Namen `passwd` teilen.]{#five-pages explanation="Es kann mehrere Ergebnisse geben, doch der Klammerwert bezeichnet einen Abschnitt und keine Seitenanzahl."}
:::

## Zwischen whatis, man und apropos wählen

- `whatis NAME`: Zeigt knappe Beschreibungen zu einem genauen Handbuchthema.
- `man NAME`: Öffnet eine vollständige Handbuchseite.
- `apropos KEYWORD`: Durchsucht Namen und Beschreibungen von Handbuchseiten nach einem Stichwort.

Zum Beispiel:

```bash
$ apropos password
```

Verwende `apropos`, wenn du die Aufgabe, aber nicht den Befehlsnamen kennst. `whatis` eignet sich, wenn der Name bereits bekannt ist.

:::single-choice{#search-by-purpose}
Du kennst den Befehlsnamen nicht, möchtest aber Handbuchbeschreibungen nach dem Stichwort `password` durchsuchen. Welcher Befehl passt dazu?

::option[`apropos password`]{#apropos-password .correct explanation="`apropos` durchsucht Namen und Beschreibungen von Handbuchseiten nach dem Stichwort und hilft so beim Entdecken passender Themen."}
::option[`whatis password`]{#exact-password explanation="`whatis` sucht nach einem genauen Handbuchthema namens `password`. Es ist keine allgemeine Stichwortsuche."}
::option[`man password`]{#manual-password explanation="`man` versucht, eine Seite mit diesem Themennamen zu öffnen. Die verlangte Beschreibungssuche führt es nicht aus."}
:::

## Wenn keine Beschreibung erscheint

Meldet `whatis`, dass nichts Passendes vorhanden ist, besitzt das Thema möglicherweise keine installierte Handbuchseite oder die Datenbank ist veraltet. Das beweist nicht, dass keine ausführbare Datei, kein Alias, keine Funktion oder kein Builtin dieses Namens existiert. Prüfe mit `type NAME`, wie Bash den Befehlsnamen auflöst, und wähle danach eine passende Hilfequelle.

:::single-choice{#whatis-versus-type}
`whatis deploy` findet keine Handbuchbeschreibung. Welcher Befehl prüft, ob Bash `deploy` als Alias, Funktion, Builtin oder ausführbare Datei auflöst?

::option[`whatis -r deploy`]{#whatis-regex-deploy explanation="Eine veränderte Abfrage der Handbuchdatenbank zeigt nicht alle Aliase, Funktionen, Builtins und Pfadauflösungen von Bash an."}
::option[`man 5 deploy`]{#manual-five-deploy explanation="Damit versuchst du, eine Seite aus Abschnitt 5 zu öffnen. Die Namensauflösung durch Bash wird nicht bestimmt."}
::option[`type deploy`]{#resolve-deploy .correct explanation="Das Bash-Builtin `type` meldet, wie die aktuelle Shell einen Befehlsnamen auflöst – unabhängig davon, ob eine Handbuchbeschreibung installiert ist."}
:::

## Zusammenfassung

Du kannst nun knappe Beschreibungen aus der Handbuchdatenbank abrufen und deuten.

1. Schlage ein genaues Thema mit `whatis` nach.
2. Lies den in Klammern angegebenen Handbuchabschnitt.
3. Verwende `man`, wenn du die vollständige Seite benötigst.
4. Verwende `apropos`, wenn du ein Stichwort statt eines Namens kennst.
