---
index: 15
lang: "de"
title: "Hilfe"
meta_title: "Hilfe - Kommandozeile"
meta_description: "Erfahren Sie, wie Sie den Linux-Hilfebefehl für schnelle Unterstützung in Ihrem Terminal verwenden. Dieses Bash-Tutorial erklärt, wie Sie Hilfe für Shell-eigene Befehle erhalten und das --help-Flag für andere Linux-Programme nutzen."
meta_keywords: "Linux Hilfebefehl, Bash Hilfe, Kommandozeilenhilfe, Linux Befehle, Linux Anfänger, Linux Tutorial, Bash Tutorial, Shell Built-in, Kommandozeilenunterstützung"
---

## Lesson Content

Wenn Sie auf der Linux-Kommandozeile arbeiten, benötigen Sie oft eine schnelle Erinnerung daran, wie ein Befehl funktioniert oder welche Optionen er akzeptiert. Glücklicherweise bietet Linux hervorragende Werkzeuge für die Hilfe auf der Kommandozeile direkt im Terminal.

### Der 'help'-Befehl für Bash-Built-ins

Eines der direktesten Werkzeuge ist `help`, ein Befehl, der direkt in die Bash-Shell integriert ist. Er wurde speziell entwickelt, um Informationen über andere Bash-Built-in-Befehle bereitzustellen. Ein Built-in-Befehl ist Teil der Shell selbst, kein separates Programm. Beispiele hierfür sind `echo`, `cd` und `pwd`.

Um den **Linux-Hilfebefehl** zu verwenden, geben Sie einfach `help` gefolgt vom Namen des Built-in-Befehls ein.

```bash
help echo
```

Dies zeigt eine Zusammenfassung des `echo`-Befehls, seine Syntax und eine Liste der verfügbaren Optionen. Dies ist der schnellste Weg, um Hilfe für Shell-spezifische Funktionen zu erhalten.

### Das --help-Flag für ausführbare Programme

Für die meisten anderen ausführbaren Programme, die nicht in die Shell integriert sind, funktioniert der `help`-Befehl nicht. Stattdessen ist es eine gängige Konvention, ein `--help`-Flag bereitzustellen. Diese Option signalisiert dem Programm, eine Nutzungsszusammenfassung auszugeben und dann zu beenden.

```bash
ls --help
```

Obwohl sich die meisten Entwickler an diesen Standard halten, ist er nicht universell. Das Ausprobieren des `--help`-Flags ist jedoch normalerweise der beste erste Schritt, um Hilfe für ein unbekanntes Programm zu finden. Es ist eine grundlegende Fähigkeit für jeden, der **Linux-Befehle** lernt.

## Exercise

Obwohl es für dieses Thema keine spezifischen Übungen gibt, empfehlen wir Ihnen, den umfassenden [Linux Lernpfad](https://labex.io/de/learn/linux) zu erkunden, um verwandte Linux-Fähigkeiten und -Konzepte zu üben.

## Quiz Question

Wie erhalten Sie schnelle Hilfe auf der Kommandozeile für eingebaute Bash-Befehle? (Bitte geben Sie den einzelnen Befehlsnamen auf Englisch und in Kleinbuchstaben an.)

## Quiz Answer

help
