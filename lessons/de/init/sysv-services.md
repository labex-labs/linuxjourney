---
index: 2
lang: "de"
title: "System V Dienst"
meta_title: "System V Dienst - Init"
meta_description: "Erfahren Sie, wie Sie traditionelle System V (SysV) Dienste in Linux verwalten. Diese Anleitung behandelt die Verwendung des `service`-Befehls zum Auflisten, Starten, Stoppen und Neustarten von Diensten unter einem System V Init-System."
meta_keywords: "system v, sysv init, linux dienste, service befehl, linux dienste verwalten, dienst starten, dienst stoppen, dienst neu starten, linux system v"
---

## Lesson Content

**System V** (oder SysV) ist eines der klassischen Initialisierungssysteme in Unix-ähnlichen Betriebssystemen. Obwohl viele moderne Linux-Distributionen auf neuere Systeme wie `systemd` umgestiegen sind, ist das Verständnis der Verwaltung von **System V**-Diensten immer noch eine wertvolle Fähigkeit, da viele Systeme die Abwärtskompatibilität aufrechterhalten.

### Der service-Befehl

Das primäre Werkzeug für die Interaktion mit Diensten in einem **System V**-Init-System ist der Befehl `service`. Er fungiert als Wrapper-Skript und vereinfacht den Prozess der Steuerung von Diensten.

### Auflisten aller Dienste

Um einen Überblick über alle verfügbaren Dienste und deren aktuellen Status zu erhalten, können Sie das Flag `--status-all` verwenden. Dieser Befehl listet jeden Dienst auf und zeigt an, ob er läuft (`+`), gestoppt (`-`) ist oder ob sein Zustand unbekannt ist (`?`).

```bash
service --status-all
```

### Steuern eines bestimmten Dienstes

Um einen einzelnen Dienst zu verwalten, geben Sie den Dienstnamen gefolgt von einer Aktion wie `start`, `stop` oder `restart` an. Diese Aktionen erfordern Administratorrechte, daher werden Sie typischerweise `sudo` verwenden.

Um einen Dienst zu starten, beispielsweise den Netzwerkdienst:

```bash
sudo service networking start
```

Um einen laufenden Dienst zu stoppen:

```bash
sudo service networking stop
```

Um einen Dienst zu stoppen und sofort wieder zu starten, was nützlich ist, um Konfigurationsänderungen zu übernehmen:

```bash
sudo service networking restart
```

Diese Befehle sind nicht auf **System V**-Init-Systeme beschränkt; Sie können sie oft auch zur Verwaltung von Upstart-Diensten verwenden. Während sich Linux-Distributionen weiterentwickeln, werden Kompatibilitätsschichten wie der `service`-Befehl beibehalten, um den Übergang von traditionellen Init-Skripten zu erleichtern.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis der Prozess- und Aufgabenverwaltung zu festigen, die für die Verwaltung von Diensten in Linux von grundlegender Bedeutung sind:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** - Üben Sie die Interaktion mit, Inspektion, Überwachung und Beendigung von Prozessen in einer realen Linux-Umgebung.
2. **[Aufgaben mit at und cron in Linux planen](https://labex.io/de/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Lernen Sie, Aufgaben mithilfe von `at` für einmalige Jobs und `cron` für wiederkehrende Aufgaben zu automatisieren, eine Schlüsselqualifikation für die Dienstautomatisierung.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Systemoperationen aufzubauen.

## Quiz Question

Was ist der vollständige Befehl, um einen Dienst namens `peanut` auf einem System V-System zu stoppen? Bitte geben Sie den exakten Befehl in Englisch an und achten Sie auf die Groß- und Kleinschreibung.

## Quiz Answer

sudo service peanut stop
