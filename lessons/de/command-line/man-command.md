---
lesson_id: "man-command"
course_id: "command-line"
lang: "de"
order_index: 16
title: "man"
description: "Lerne, installierte Handbuchseiten zu öffnen, zu navigieren, zu durchsuchen und gezielt nach Abschnitt auszuwählen."
meta_title: "man - Kommandozeile"
meta_description: "Lernen Sie den Linux-Befehl man mit Beispielen zum Lesen von Handbuchseiten, Suchen in man-Seiten, Verständnis der Abschnitte und Finden von Befehlsoptionen."
meta_keywords: "man Befehl, linux man Seiten, Befehlsanleitung, man ls, man Abschnitte, man Seite durchsuchen, Kommandozeilenhilfe"
---

Für viele Linux-Befehle, Schnittstellen, Konfigurationsdateien und Verwaltungswerkzeuge ist eine Referenzdokumentation in Form von Handbuchseiten, den sogenannten Manpages, installiert. Der Befehl `man` findet diese Seiten und zeigt sie an.

## Eine Handbuchseite öffnen

Übergib `man` den Namen eines Themas. Die Seite zu `ls` öffnest du beispielsweise so:

```bash
$ man ls
```

Handbuchseiten enthalten häufig eine Übersicht der Syntax, eine Beschreibung, Optionen, zugehörige Dateien und Querverweise. Die genauen Abschnitte können jedoch variieren.

:::single-choice{#open-ls-manual}
Welcher Befehl öffnet die installierte Handbuchseite für `ls`?

::option[`help ls`]{#help-ls explanation="Bash `help` dokumentiert Shell-Builtins und öffnet normalerweise nicht die Handbuchseite des externen Programms `ls`."}
::option[`man ls`]{#manual-ls-page .correct explanation="`man` sucht im Handbuchbestand nach dem Thema `ls` und zeigt die passende Seite an."}
::option[`ls --help`]{#ls-usage explanation="Damit forderst du von `ls` eine eigene Nutzungsübersicht an. Die installierte Handbuchseite wird nicht geöffnet."}
:::

## Auf einer Seite navigieren und suchen

Auf vielen Systemen zeigt `man` Seiten über einen Pager wie `less` an. Bei geöffneter Seite kannst du mit Pfeil- oder Bildtasten scrollen und folgende Steuerungen verwenden:

Innerhalb einer Manpage:

- Gib `/pattern` ein und drücke Enter, um vorwärts zu suchen.
- Drücke `n`, um die Suche in derselben Richtung zu wiederholen.
- Drücke `N`, um sie in der Gegenrichtung zu wiederholen.
- Drücke `q`, um die Ansicht zu beenden.

Je nach System oder Umgebung kann ein anderer Pager zum Einsatz kommen. Die genannten Tasten gelten für die verbreitete Konfiguration mit `less`.

:::single-choice{#search-man-page}
Wie startest du in einer mit `less` geöffneten Manpage eine Vorwärtssuche nach `--recursive`?

::option[Gib `?--recursive` ein und drücke Enter.]{#backward-man-search explanation="Ein Fragezeichen beginnt eine Rückwärtssuche und sucht damit in der entgegengesetzten Richtung."}
::option[Gib `/--recursive` ein und drücke Enter.]{#forward-man-search .correct explanation="Ein Schrägstrich beginnt in `less` eine Vorwärtssuche; mit Enter sendest du das Muster ab."}
::option[Gib `n--recursive` ein und drücke Enter.]{#repeat-man-search explanation="Die Taste `n` wiederholt eine vorhandene Suche. Auf diese Weise wird kein neues Suchmuster eingeführt."}
:::

:::single-choice{#leave-man-page}
Welche Taste kehrt aus einer im üblichen Pager geöffneten Manpage zur Shell zurück?

::option[`G`]{#man-page-end explanation="Das große `G` springt in `less` ans Seitenende. Der Pager bleibt geöffnet."}
::option[`n`]{#next-man-match explanation="Die Taste `n` wiederholt die letzte Suche und lässt die Handbuchseite geöffnet."}
::option[`q`]{#quit-man .correct explanation="Die Taste `q` beendet den üblichen Pager und gibt die Kontrolle an die Shell zurück."}
:::

## Einen Handbuchabschnitt auswählen

Das Handbuch ist in nummerierte Abschnitte gegliedert. Häufige Abschnitte sind:

- `1`: Benutzerbefehle.
- `2`: Systemaufrufe.
- `3`: Bibliotheksfunktionen.
- `5`: Dateiformate.
- `8`: Systemverwaltungsbefehle.

Dasselbe Thema kann in mehreren Abschnitten vorkommen. Setze die Abschnittsnummer vor das Thema, um eine Seite ausdrücklich auszuwählen:

```bash
$ man 5 passwd
$ man 1 passwd
```

Der erste Befehl öffnet die Dateiformatseite zu `passwd` aus Abschnitt 5, der zweite die Benutzerbefehlsseite aus Abschnitt 1. Verweise wie `passwd(5)` verwenden dieselbe Schreibweise `topic(section)`.

:::single-choice{#open-passwd-file-format}
Welcher Befehl öffnet die Seite aus Abschnitt 5, die das Dateiformat `passwd` dokumentiert?

::option[`man passwd 5`]{#section-after-topic explanation="Bei dieser Befehlsform gehört der Abschnitt vor das Thema. Diese Reihenfolge fordert nicht `passwd(5)` an."}
::option[`man 5 passwd`]{#passwd-format-page .correct explanation="Wenn Abschnitt `5` vor `passwd` steht, wird gezielt die Dateiformatseite ausgewählt."}
::option[`man 1 passwd`]{#passwd-command-page explanation="Abschnitt 1 enthält Benutzerbefehle. Dieser Befehl wählt daher die Befehlsseite zu `passwd` statt der Dateiformatseite aus."}
:::

## Wenn eine Seite fehlt

Nicht für jeden Befehlsnamen ist eine eigene Handbuchseite installiert. Meldet `man`, dass kein Eintrag vorhanden ist:

- Führe `type NAME` aus, um die Namensauflösung durch Bash zu prüfen.
- Verwende bei einem Bash-Builtin `help NAME`.
- Probiere bei einem externen Programm `NAME --help`, sofern es diese Konvention unterstützt.
- Prüfe, ob deine Distribution ein separates Dokumentationspaket anbietet.

:::single-choice{#missing-builtin-manual}
`type cd` meldet, dass `cd` ein Bash-Builtin ist, und es ist keine eigene Manpage verfügbar. Welchen Befehl solltest du als Nächstes versuchen?

::option[`whatis cd`]{#whatis-missing-cd explanation="`whatis` fasst Einträge aus der Handbuchdatenbank zusammen. Eine fehlende eigene Seite für das Builtin kann es nicht bereitstellen."}
::option[`file cd`]{#file-cd-name explanation="`file` klassifiziert Dateisystemobjekte; hier wird `cd` jedoch als Shell-Builtin und nicht als Pfad aufgelöst."}
::option[`help cd`]{#builtin-cd-help .correct explanation="Das Bash-Builtin `help` stellt die eigene Dokumentation der Shell für `cd` bereit."}
:::

## Zusammenfassung

Du kannst nun installierte Handbuchdokumentation finden und darin navigieren.

1. Öffne eine Seite nach ihrem Themennamen.
2. Suche und navigiere im üblichen Pager durch eine Seite.
3. Beende den Pager und kehre zur Shell zurück.
4. Wähle einen nummerierten Handbuchabschnitt aus.
5. Nutze eine andere Hilfequelle, wenn keine Seite verfügbar ist.
