---
lesson_id: "exit-command"
course_id: "command-line"
lang: "de"
order_index: 19
title: "exit"
description: "Lerne, die aktuelle Shell zu verlassen und ihren Rückgabestatus für den Aufrufer festzulegen."
meta_title: "exit - Kommandozeile"
meta_description: "Lernen Sie den Linux-Befehl exit kennen, wie man eine Shell-Sitzung beendet, wie sich logout von exit unterscheidet und wie Exit-Statuswerte funktionieren."
meta_keywords: "exit Befehl, linux exit, logout Befehl, shell Sitzung, Terminal beenden, Exit-Status, bash exit"
---

Shells können ineinander verschachtelt sein: Ein grafisches Terminal startet eine Shell, eine SSH-Verbindung eine entfernte Shell und eine Shell kann eine weitere Shell starten. Wenn du eine davon verlässt, erhält normalerweise der Prozess wieder die Kontrolle, der diese aktuelle Shell gestartet hat.

## Die aktuelle Shell verlassen

Der Befehl `exit` fordert die aktuelle Shell auf, sich zu beenden:

```bash
$ exit
```

Ist diese Shell der Hauptprozess in einem grafischen Terminal-Tab, kann sich der Tab entsprechend den Terminaleinstellungen schließen. In einer SSH-Sitzung kehrst du nach dem Verlassen der entfernten Shell normalerweise zur lokalen Shell zurück. Hast du eine verschachtelte Shell gestartet, führt `exit` zur übergeordneten Shell zurück.

:::single-choice{#leave-current-shell} Du hast Bash innerhalb einer anderen Shell gestartet und möchtest nun zur übergeordneten Shell zurückkehren. Welchen Befehl führst du in der verschachtelten Bash-Sitzung aus?

::option[`clear`]{#clear-nested explanation="`clear` erneuert den sichtbaren Terminalbereich, lässt die aktuelle Shell aber weiterlaufen."}
::option[`exit`]{#exit-nested .correct explanation="`exit` beendet die aktuelle Shell, sodass ihre übergeordnete Shell fortgesetzt werden kann."}
::option[`history -c`]{#clear-nested-history explanation="Dieser Befehl leert die Bash-Verlaufsliste im Arbeitsspeicher. Die aktuelle Shell wird nicht beendet."}
:::

## Einen Beendigungsstatus zurückgeben

Mit einem optionalen numerischen Argument legst du den Status fest, den die Shell an ihren Aufrufer zurückgibt:

```bash
$ exit 0
```

Konventionsgemäß bedeutet `0` Erfolg; ein von null verschiedener Wert steht für einen Fehler oder eine andere vom Programm definierte Bedingung. Erhält Bash kein numerisches Argument, beendet sie sich mit dem Status des letzten Befehls vor `exit`.

:::single-choice{#return-success-status} Welcher Befehl beendet die aktuelle Shell und meldet ihrem Aufrufer ausdrücklich Erfolg?

::option[`exit 0`]{#exit-zero .correct explanation="Der Status `0` meldet dem Aufrufer konventionsgemäß eine erfolgreiche Ausführung."}
::option[`exit 1`]{#exit-one explanation="Ein von null verschiedener Status steht konventionsgemäß für einen Fehler oder ein anderes außergewöhnliches Ergebnis, nicht für Erfolg."}
::option[`logout 0`]{#logout-zero explanation="Bash `logout` ist für eine Login-Shell gedacht und verwendet diese Form nicht zum Festlegen des verlangten Status."}
:::

:::single-choice{#exit-without-number} Welchen Status gibt `exit` in Bash zurück, wenn du keine Zahl angibst?

::option[Der Befehl gibt immer den Erfolgsstatus `0` zurück.]{#always-zero explanation="Die Erfolgskonvention zwingt ein `exit` ohne Argument nicht zu null. Bash bewahrt in diesem Fall einen vorherigen Status."}
::option[Der Befehl gibt immer den Fehlerstatus `1` zurück.]{#always-one explanation="Bash weist nicht jedem `exit` ohne Argument den Fehlerstatus `1` zu. Der vorangegangene Befehl bestimmt den Wert."}
::option[Der Befehl gibt den Beendigungsstatus des vorherigen Befehls zurück.]{#last-command-status .correct explanation="Ohne ausdrückliches numerisches Argument beendet sich Bash mit dem Status des zuletzt ausgeführten Befehls."}
:::

## logout in einer Login-Shell verwenden

Das Bash-Builtin `logout` beendet eine Login-Shell:

```bash
$ logout
```

In einer Bash-Shell ohne Login meldet `logout`, dass es sich nicht um eine Login-Shell handelt. Verwende dort stattdessen `exit`.

:::single-choice{#leave-login-shell} Welches Bash-Builtin ist speziell zum Verlassen einer Login-Shell vorgesehen?

::option[`logout`]{#logout-login .correct explanation="Bash stellt `logout` zum Beenden einer Login-Shell bereit."}
::option[`unalias`]{#unalias-login explanation="`unalias` entfernt Aliasdefinitionen aus der aktuellen Shell. Die Sitzung beendet der Befehl nicht."}
::option[`source`]{#source-login explanation="`source` liest Befehle aus einer Datei in die aktuelle Shell ein. Die Shell wird dabei nicht beendet."}
:::

## Ctrl+D verwenden oder ein Terminal schließen

An einer leeren interaktiven Eingabeaufforderung liefert `Ctrl+D` normalerweise das Dateiende-Eingabezeichen des Terminals. Bash deutet diesen Zustand häufig als Aufforderung zum Beenden. Es handelt sich nicht um ein Signal, und Shell-Einstellungen wie Bashs `ignoreeof` können das Verhalten ändern.

Beim Schließen eines grafischen Terminalfensters fordert die Terminalanwendung ihre Prozesse zum Beenden auf, was sich auf laufende Aufgaben auswirken kann. Bevorzuge nach Möglichkeit ein geordnetes `exit` und prüfe vor dem Schließen, ob noch Arbeit aktiv ist.

## Zusammenfassung

Du kannst nun die aktuelle Shell verlassen und ihren Abschlussstatus mitteilen.

1. Kehre mit `exit` zum Aufrufer der aktuellen Shell zurück.
2. Verwende `0` für Erfolg und andernfalls einen definierten, von null verschiedenen Status.
3. Verstehe den Status eines `exit` ohne Zahlenargument.
4. Verwende `logout` nur für eine Login-Shell.
5. Erkenne `Ctrl+D` als Dateiende-Eingabe und nicht als Signal.
