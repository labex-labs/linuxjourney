---
index: 1
lang: "de"
title: "ps (Prozesse)"
meta_title: "ps (Prozesse) - Prozesse"
meta_description: "Entdecken Sie den Linux-Befehl ps mit unserem umfassenden Leitfaden. Erfahren Sie, wie Sie den Befehl ps -ef unter Linux und andere Optionen verwenden, um laufende Prozesse anzuzeigen, PIDs zu verstehen und Systemaufgaben zu verwalten. Ein perfekter Start für Ihre Linux-Reise."
meta_keywords: "ps Befehl, ps -ef linux, ps -ef Befehl, linux ps -ef, ps -e linux, Linux Prozesse, Prozess-ID, PID, top Befehl, Linux Reise"
---

## Lesson Content

### Prozesse unter Linux verstehen

Prozesse sind die Programme, die gerade auf Ihrem Rechner laufen. Der Linux-Kernel verwaltet sie, und jedem Prozess wird eine eindeutige Nummer zugewiesen, die **Prozess-ID (PID)** genannt wird. PIDs werden typischerweise sequenziell vergeben, wenn neue Prozesse erstellt werden.

### Grundlegende Verwendung des ps-Befehls

Um einen schnellen Überblick über Ihre aktiven Prozesse zu erhalten, führen Sie einfach den Befehl `ps` aus. Dieser liefert eine Momentaufnahme der Prozesse, die mit Ihrer aktuellen Terminal-Sitzung verbunden sind.

```plaintext
$ ps

PID        TTY     STAT   TIME          CMD
41230    pts/4    Ss        00:00:00     bash
51224    pts/4    R+        00:00:00     ps
```

Diese Ausgabe zeigt einige wichtige Details:

- **PID**: Die eindeutige Prozess-ID.
- **TTY**: Das steuernde Terminal für den Prozess.
- **STAT**: Der aktuelle Status des Prozesses.
- **TIME**: Die gesamte CPU-Zeit, die der Prozess verbraucht hat.
- **CMD**: Der Befehl, der den Prozess gestartet hat.

### Erkundung von ps mit BSD-ähnlichen Optionen

Der `ps`-Befehl ist sehr vielseitig und verfügt über viele Optionen, die verschiedenen Syntaxstilen angehören (BSD, System V, GNU). Der BSD-Stil, der keinen Bindestrich für Optionen verwendet, ist recht verbreitet. Eine beliebte Kombination ist `ps aux`:

```bash
ps aux
```

Hier ist die Bedeutung dieser Optionen:

- **a**: Zeigt alle Prozesse aller Benutzer an.
- **u**: Bietet ein detailliertes, benutzerorientiertes Format.
- **x**: Schließt Prozesse ein, die keinem Terminal zugeordnet sind. Dies sind oft System-Daemons, die beim Booten starten und in der TTY-Spalte ein `?` anzeigen.

Dieser Befehl liefert eine viel reichhaltigere Ausgabe mit zusätzlichen Spalten wie `USER`, `%CPU`, `%MEM`, `VSZ` und `RSS`. Vorerst konzentrieren wir uns auf PID, STAT und COMMAND.

### Verwendung des ps -ef-Befehls unter Linux

Ein weiterer äußerst beliebter Syntax ist der System V-Stil. Sie werden häufig den **ps -ef-Befehl** sehen, der von Systemadministratoren verwendet wird. Dies ist eine leistungsstarke Methode, um ein vollständiges Bild davon zu erhalten, was auf Ihrem System läuft.

```bash
ps -ef
```

Der Befehl **ps -ef linux** liefert eine vollständige Liste aller Prozesse.

- **-e**: Wählt jeden Prozess im System aus.
- **-f**: Zeigt eine „vollständige“ Auflistung an, die Details wie UID, PPID (Parent Process ID), C (CPU-Auslastung) und STIME (Startzeit) enthält.

Viele Benutzer bevorzugen `ps -ef` gegenüber `ps aux` wegen seiner klaren, hierarchischen Ansicht und detaillierten Informationen. Bei der Fehlerbehebung auf einem Linux-System ist die Ausführung von **linux ps -ef** oft einer der ersten Schritte zur Diagnose von Problemen. Eine einfachere Variante, `ps -e linux`, listet ebenfalls alle Prozesse auf, jedoch in einem weniger detaillierten Format.

### Echtzeitüberwachung mit top

Während `ps` eine Momentaufnahme liefert, bietet der Befehl `top` eine Echtzeit-, dynamische Ansicht der Prozesse auf Ihrem System. Es ist ein ausgezeichnetes Werkzeug, um festzustellen, welche Prozesse die meiste CPU oder den meisten Speicher verbrauchen. Standardmäßig wird die Anzeige alle paar Sekunden aktualisiert.

```bash
top
```

## Exercise

Übung macht den Meister beim Beherrschen von Linux-Befehlen. Die folgenden praktischen Übungen helfen Ihnen, Ihr Verständnis der Prozessüberwachung und -verwaltung zu festigen:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** - Üben Sie wesentliche Fähigkeiten zur Verwaltung und Überwachung von Prozessen auf einem Linux-System, einschließlich der Interaktion mit Vordergrund-/Hintergrundprozessen, der Inspektion mit `ps`, der Überwachung mit `top` und dem Beenden mit `kill`.
2. **[Linux top-Befehl: Echtzeit-Systemüberwachung](https://labex.io/de/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Lernen Sie, den Linux `top`-Befehl für die Echtzeit-Systemüberwachung zu verwenden, einschließlich des Sortierens von Prozessen, des Anpassens von Aktualisierungsintervallen und des Filter nach Benutzer.

Diese Labs helfen Ihnen, die Konzepte der Prozessidentifizierung und -überwachung in realen Szenarien anzuwenden und Ihr Selbstvertrauen als Linux-Systemadministrator zu stärken.

## Quiz Question

Welche `ps`-Flagge wird in Kombination mit den Flaggen `a` und `x` verwendet, um detaillierte, benutzerorientierte Informationen über Prozesse anzuzeigen? Bitte antworten Sie mit einem einzigen Kleinbuchstaben in englischer Sprache.

## Quiz Answer

u
