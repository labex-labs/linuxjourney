---
index: 7
lang: "de"
title: "kill (Beenden)"
meta_title: "kill (Beenden) - Prozesse"
meta_description: "Meistern Sie den Linux-kill-Befehl, um Prozesse zu verwalten und zu beenden. Dieser Leitfaden behandelt die Unterschiede zwischen kill vs. beenden und erklärt Signale wie kill sigterm (SIGTERM), SIGKILL und kill sighup (SIGHUP)."
meta_keywords: "kill Befehl, kill sigterm, kill sighup, linux kill -0, kill vs beenden, kill -15 linux, SIGTERM, SIGKILL, Prozessverwaltung, Prozess beenden"
---

## Lesson Content

In Linux können Sie Prozesse verwalten, indem Sie ihnen Signale senden. Der primäre Befehl hierfür ist `kill`, der trotz seines Namens verschiedene Signale senden kann, nicht nur solche, die einen Prozess beenden.

### Standardbeendigung mit kill sigterm

Wenn Sie den Befehl `kill` nur mit einer Prozess-ID (PID) verwenden, sendet er standardmäßig ein `TERM`-Signal. Dies ist die übliche, saubere Methode, ein Programm zum Beenden aufzufordern.

```bash
kill 12445
```

Das Signal `kill sigterm` (auch bekannt als `SIGTERM` oder Signal 15) fordert den Prozess auf, sich ordnungsgemäß herunterzufahren. Dies gibt dem Prozess die Möglichkeit, seinen Fortschritt zu speichern und Ressourcen korrekt freizugeben. Sie können auch explizit die Signalnummer verwenden, wodurch `kill -15 12445` äquivalent zum obigen Befehl wird. Dies beantwortet die häufige Anfrage zu `kill -15 linux`.

### Erzwingen der Beendigung mit SIGKILL

Manchmal reagiert ein Prozess nicht mehr und ignoriert das `SIGTERM`-Signal. In solchen Fällen können Sie ihn mit dem `KILL`-Signal zum sofortigen Stoppen zwingen.

```bash
kill -9 12445
```

Das Signal `SIGKILL` (Signal 9) beendet den Prozess sofort, ohne ihm die Möglichkeit zur Bereinigung zu geben. Dies ist ein wesentlicher Unterschied in der Debatte um `kill vs terminate`; `SIGKILL` ist eine bedingungslose Beendigung, während `SIGTERM` eine höfliche Aufforderung ist.

### Andere gängige Signale verstehen

Obwohl `SIGTERM` und `SIGKILL` am häufigsten vorkommen, sind auch andere Signale für die Prozessverwaltung nützlich.

- **SIGHUP**: Das Signal `kill sighup` (Hangup, Signal 1) wird traditionell an einen Prozess gesendet, wenn sein steuerndes Terminal geschlossen wird. Es kann verwendet werden, um Daemon-Prozessen mitzuteilen, ihre Konfigurationsdateien neu zu laden.
- **SIGINT**: Das Interrupt-Signal (Signal 2) wird gesendet, wenn Sie `Strg-C` drücken. Es fordert den Prozess auf, seine aktuelle Operation zu unterbrechen.
- **SIGSTOP**: Dieses Signal (Signal 19) hält einen Prozess an, ohne ihn zu beenden. Der Prozess kann später mit dem Signal `SIGCONT` fortgesetzt werden.

### Überprüfen der Prozess-Existenz mit kill -0

Ein Sonderfall ist `linux kill -0`. Dieser Befehl sendet tatsächlich kein Signal, sondern prüft, ob ein Prozess mit der angegebenen PID existiert und ob Sie die Berechtigung haben, ihm ein Signal zu senden.

```bash
kill -0 12445
```

Wenn der Befehl erfolgreich ausgeführt wird (Exit-Code 0), existiert der Prozess. Wenn er fehlschlägt, existiert der Prozess nicht oder Sie haben keine Berechtigungen.

## Exercise

Um das Gelernte anzuwenden, versuchen Sie dieses praktische Labor, um Ihr Verständnis der Prozessverwaltung und -beendigung zu festigen:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** - In diesem Labor erlernen Sie wesentliche Fähigkeiten zur Verwaltung und Überwachung von Prozessen auf einem Linux-System. Sie werden untersuchen, wie man mit Vordergrund- und Hintergrundprozessen interagiert, sie mit `ps` inspiziert, Ressourcen mit `top` überwacht, die Priorität mit `renice` anpasst und sie mit `kill` beendet.

Dieses Labor hilft Ihnen, die Konzepte der Prozesssteuerung und -beendigung in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Linux-Prozessen aufzubauen.

## Quiz Question

Wie lautet der Signalname für den Standardbefehl `kill`? Bitte antworten Sie auf Englisch. Beachten Sie, dass die Antwort groß- und kleingeschrieben werden muss.

## Quiz Answer

SIGTERM
