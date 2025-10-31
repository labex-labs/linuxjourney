---
index: 4
lang: "de"
title: "Upstart Jobs"
meta_title: "Upstart Jobs - Init"
meta_description: "Ein Leitfaden zur Verwaltung von Diensten mit Upstart-Jobs in einer Linux-Umgebung. Lernen Sie, das initctl-Dienstprogramm zu verwenden, um Jobs auf einem Upstart-Linux-System aufzulisten, zu starten, zu stoppen und neu zu starten."
meta_keywords: "Upstart Jobs, initctl, Upstart Linux, Linux Dienste, Systemadministration, Init-System, Linux Tutorial"
---

## Lesson Content

Upstart ist ein ereignisbasiertes Init-System, das in einigen **Upstart Linux**-Distributionen zur Verwaltung von Diensten und Aufgaben während des Bootvorgangs und im laufenden Betrieb verwendet wird. Es arbeitet über ein System von Jobs und Ereignissen. Obwohl die Verfolgung des Ursprungs jedes Ereignisses komplex sein kann und oft erfordert, dass Sie Jobkonfigurationen in `/etc/init` untersuchen, müssen Sie diese Jobs häufiger direkt über die Befehlszeile verwalten. Das Dienstprogramm `initctl` bietet hierfür eine Reihe von Befehlen.

### Anzeigen des Jobstatus

Um eine Liste aller bekannten Upstart-Jobs und ihrer aktuellen Zustände anzuzeigen, verwenden Sie den Befehl `list`.

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

Die Ausgabe zeigt den Jobnamen, sein Ziel und seinen aktuellen Status. Im Beispiel `shutdown stop/waiting` ist der Jobname `shutdown`, sein Ziel ist `stop` und sein aktueller Status ist `waiting`. Der Jobstatus und die Ziele ändern sich, wenn Sie mit ihnen interagieren.

Um den Status eines bestimmten Jobs zu überprüfen, verwenden Sie den Befehl `status`.

```plaintext
initctl status networking
networking start/running
```

### Manuelle Steuerung von Jobs

Während Konfigurationsdateien für Jobs in `/etc/init` definieren, wie Jobs starten, stoppen und mit Ereignissen interagieren, können Sie diese Aktionen manuell mit `initctl` außer Kraft setzen. Dies ist nützlich für die Fehlerbehebung oder die Durchführung administrativer Aufgaben.

Um einen Job manuell zu starten:

```bash
sudo initctl start networking
```

Um einen Job manuell zu stoppen:

```bash
sudo initctl stop networking
```

Um einen Job manuell neu zu starten, was eine bequeme Abkürzung für das Stoppen und anschließende Starten ist:

```bash
sudo initctl restart networking
```

### Auslösen benutzerdefinierter Ereignisse

Upstart-Jobs werden durch Ereignisse ausgelöst. Sie können auch manuell ein Ereignis "emittieren" (auslösen), was nützlich sein kann, um benutzerdefinierte Jobs auszulösen oder zu Testzwecken. Jeder Job, der so konfiguriert ist, dass er auf `some_event` startet, würde durch den folgenden Befehl ausgelöst.

```bash
sudo initctl emit some_event
```

## Exercise

Übung macht den Meister! Obwohl es keine spezifischen Labore für Upstart gibt, ist das Verständnis, wie Aufgaben geplant und verwaltet werden, entscheidend für die Steuerung von Systemprozessen. Hier ist ein praktisches Labor, um Ihr Verständnis der Aufgabenverwaltung zu festigen:

1. **[Aufgaben mit at und cron in Linux planen](https://labex.io/de/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Üben Sie das Erstellen, Verwalten und Entfernen von einmaligen und wiederkehrenden Jobs, was grundlegende Konzepte im Zusammenhang mit der Verwaltung von Diensten und Aufgaben in Linux-Umgebungen sind, wie sie von Upstart gehandhabt werden.

Dieses Labor hilft Ihnen, die Konzepte der Aufgabenautomatisierung in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Systemoperationen aufzubauen.

## Quiz Question

Wie würden Sie einen Upstart-Job namens `peanuts` manuell neu starten? Bitte geben Sie den vollständigen Befehl an. (Hinweis: Die Antwort ist groß-/kleingeschrieben und muss in Englisch sein.)

## Quiz Answer

sudo initctl restart peanuts
