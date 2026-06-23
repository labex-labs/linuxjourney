---
index: 19
lang: "de"
title: "exit"
meta_title: "exit - Kommandozeile"
meta_description: "Lernen Sie den Linux-Befehl exit kennen, wie man eine Shell-Sitzung beendet, wie sich logout von exit unterscheidet und wie Exit-Statuswerte funktionieren."
meta_keywords: "exit Befehl, linux exit, logout Befehl, shell Sitzung, Terminal beenden, Exit-Status, bash exit"
---

## Lesson Content

Herzlichen Glückwunsch zum Abschluss der grundlegenden Lektionen Ihrer Linux-Reise! Sie haben wichtige Linux-Grundlagen behandelt, und jetzt ist es an der Zeit zu lernen, wie Sie Ihre Sitzung richtig beenden. Das Verlassen der Linux-Shell ist ein einfacher, aber wichtiger letzter Schritt.

### Der Exit-Befehl

Die gebräuchlichste Methode, eine Shell-Sitzung zu beenden, ist der Befehl `exit`. Wenn Sie `exit` eingeben und Enter drücken, wird der aktuelle Shell-Prozess beendet. Dieser Befehl funktioniert in nahezu jeder Shell-Umgebung.

```bash
$ exit
```

Wenn Sie ein Terminalfenster geöffnet haben, schließt `exit` normalerweise die darin laufende Shell. Wenn Sie sich über SSH verbunden haben, beendet `exit` die entfernte Shell-Sitzung und bringt Sie zurück zur lokalen Eingabeaufforderung.

### Exit-Statuswerte

Der Befehl `exit` kann auch einen Statuscode zurückgeben. Ein Status von `0` bedeutet in der Regel Erfolg, und ein nicht null Status signalisiert meist einen Fehler oder eine besondere Bedingung.

```bash
$ exit 0
```

Exit-Statuswerte sehen Sie häufiger beim Schreiben von Shell-Skripten. Für die interaktive Nutzung reicht es aus, einfach `exit` einzugeben.

### Der Logout-Befehl

Ein weiterer Befehl, den Sie zum Verlassen eines Terminals verwenden können, ist `logout`. Dieser Befehl ist speziell dafür gedacht, eine Login-Shell zu beenden. Obwohl er sich in vielen modernen Systemen ähnlich wie `exit` verhält, ist es gut, beide Befehle zu kennen.

```bash
$ logout
```

### Das Terminalfenster schließen

Wenn Sie in einer grafischen Benutzeroberfläche arbeiten, haben Sie auch die Möglichkeit, das Terminalfenster einfach zu schließen. Diese Aktion sendet typischerweise ein Signal, das die darin laufende Shell-Sitzung beendet.

### Häufige Wege, eine Shell zu verlassen

- Geben Sie `exit` ein, um die aktuelle Shell zu beenden.
- Drücken Sie `Ctrl-D` bei einer leeren Eingabeaufforderung, um ein End-of-File zu senden, was oft die Shell beendet.
- Geben Sie `logout` ein, wenn Sie sich in einer Login-Shell befinden.
- Schließen Sie das Terminalfenster, wenn Sie ein grafisches Terminal verwenden.

### Häufige Fragen

**Ist exit dasselbe wie das Schließen des Terminalfensters?** Oft ist das Ergebnis ähnlich, aber `exit` teilt der Shell sauber mit, dass sie beendet werden soll.

**Was ist Ctrl-D?** Es sendet ein End-of-File-Signal an die Shell. Bei einer leeren Eingabeaufforderung beendet dies normalerweise die Shell.

**Was bedeutet exit 1?** Es beendet die Shell mit dem Statuscode `1`, der in Skripten häufig verwendet wird, um einen Fehler anzuzeigen.

Sie haben erfolgreich gelernt, wie man navigiert, mit Dateien arbeitet, Hilfe erhält und die Shell verlässt.

## Exercise

Für dieses Thema gibt es keine spezifischen Labs, aber wir empfehlen, den umfassenden [Linux Learning Path](https://labex.io/de/learn/linux) zu erkunden, um verwandte Linux-Fähigkeiten und Konzepte zu üben.

## Quiz Question

What is the most common command to exit from the Linux shell? Please answer using only a single lowercase English word.

## Quiz Answer

exit
