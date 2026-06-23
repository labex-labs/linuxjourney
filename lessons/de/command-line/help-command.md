---
index: 15
lang: "de"
title: "help"
meta_title: "help - Kommandozeile"
meta_description: "Lernen Sie, wie Sie Linux-Kommandozeilenhilfe mit Bash help, --help-Ausgabe, Manpages und type für Shell-Built-ins und externe Befehle erhalten."
meta_keywords: "linux help befehl, bash help, kommandozeilenhilfe, --help, shell built-in, man befehl, type befehl"
---

## Lesson Content

Wenn Sie an der Linux-Kommandozeile arbeiten, benötigen Sie oft eine schnelle Erinnerung daran, wie ein Befehl funktioniert oder welche Optionen er akzeptiert. Linux stellt mehrere Hilfsmittel direkt im Terminal zur Verfügung.

### Der 'help'-Befehl für Bash Built-ins

Eines der direktesten Hilfsmittel ist `help`, ein Befehl, der direkt in die Bash-Shell eingebaut ist. Er ist speziell dafür gedacht, Informationen über andere Bash-eigene Befehle bereitzustellen. Ein Built-in-Befehl ist Teil der Shell selbst, kein separates Programm. Beispiele sind `echo`, `cd` und `pwd`.

Um `help` zu verwenden, geben Sie es gefolgt vom Namen des Built-in-Befehls ein.

```bash
$ help echo
```

Dies zeigt eine Zusammenfassung des Befehls `echo`, seine Syntax und eine Liste der verfügbaren Optionen an. Dies ist der schnellste Weg, um Unterstützung für shell-spezifische Funktionen zu erhalten.

### Der --help-Schalter für ausführbare Programme

Für die meisten anderen ausführbaren Programme, die nicht in die Shell eingebaut sind, funktioniert der `help`-Befehl nicht. Stattdessen ist es eine gängige Konvention, einen `--help`-Schalter bereitzustellen. Diese Option signalisiert dem Programm, eine Nutzungsübersicht auszugeben und dann zu beenden.

```bash
$ ls --help
```

Obwohl die meisten Entwickler diesem Standard folgen, ist er nicht universell. Das Ausprobieren von `--help` ist normalerweise ein guter erster Schritt bei einem unbekannten Programm.

### Den Befehlstyp herausfinden

Wenn Sie nicht sicher sind, ob ein Befehl ein Bash Built-in oder ein externes Programm ist, verwenden Sie `type`.

```bash
$ type cd
cd is a shell builtin
$ type ls
ls is /usr/bin/ls
```

Dies hilft Ihnen bei der Entscheidung zwischen `help cd`, `ls --help` oder `man ls`.

### Das richtige Hilfsmittel wählen

- Verwenden Sie `help COMMAND` für Bash Built-ins wie `cd`, `echo` und `history`.
- Verwenden Sie `COMMAND --help` für eine schnelle Zusammenfassung vieler externer Befehle.
- Verwenden Sie `man COMMAND` für ausführliche Handbuchseiten.
- Verwenden Sie `whatis COMMAND` für eine einzeilige Beschreibung.

### Häufige Fragen

**Warum funktioniert help ls nicht?** `ls` ist normalerweise ein externes Programm, kein Bash Built-in. Versuchen Sie `ls --help` oder `man ls`.

**Warum funktioniert --help nicht bei jedem Befehl?** Es ist eine Konvention, keine strikte Regel.

**Was ist der schnellste Weg, einen Befehl zu überprüfen?** Versuchen Sie `COMMAND --help` für externe Befehle und `help COMMAND` für Bash Built-ins.

## Exercise

Obwohl es keine spezifischen Labs zu diesem Thema gibt, empfehlen wir, den umfassenden [Linux Learning Path](https://labex.io/de/learn/linux) zu erkunden, um verwandte Linux-Fähigkeiten und Konzepte zu üben.

## Quiz Question

Wie erhält man schnelle Kommandozeilenhilfe für eingebaute Bash-Befehle? (Bitte geben Sie den einzelnen Befehlsnamen auf Englisch und in Kleinbuchstaben an.)

## Quiz Answer

help
