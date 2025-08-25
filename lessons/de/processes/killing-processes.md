---
index: 7
lang: "de"
title: "kill (Beenden)"
meta_title: "kill (Beenden) - Prozesse"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl 'kill' verwenden, um Prozesse zu beenden. Verstehen Sie SIGTERM, SIGKILL und andere Signale für die Prozessverwaltung. Beginnen Sie jetzt mit dem Lernen!"
meta_keywords: "kill-Befehl, Linux-Prozesse, SIGTERM, SIGKILL, Linux-Tutorial, Anfänger, Prozessverwaltung, Linux-Anleitung"
---

## Lesson Content

Sie können Signale senden, die Prozesse beenden; ein solcher Befehl wird passenderweise `kill`-Befehl genannt.

```bash
kill 12445
```

Die `12445` ist die PID des Prozesses, den Sie beenden möchten. Standardmäßig sendet er ein `TERM`-Signal. Das `SIGTERM`-Signal wird an einen Prozess gesendet, um dessen Beendigung anzufordern, wodurch er seine Ressourcen sauber freigeben und seinen Zustand speichern kann.

Sie können auch ein Signal mit dem `kill`-Befehl angeben:

```bash
kill -9 12445
```

Dies führt das `SIGKILL`-Signal aus und beendet den Prozess.

### Unterschiede zwischen SIGHUP, SIGINT, SIGTERM, SIGKILL, SIGSTOP?

Diese Signale klingen alle ziemlich ähnlich, aber sie haben ihre Unterschiede.

- SIGHUP - Hangup, wird an einen Prozess gesendet, wenn das steuernde Terminal geschlossen wird. Wenn Sie beispielsweise ein Terminalfenster geschlossen haben, in dem ein Prozess lief, würden Sie ein `SIGHUP`-Signal erhalten. Im Grunde wurden Sie also aufgelegt.
- SIGINT - Ist ein Interrupt-Signal, sodass Sie Strg-C verwenden können, und das System wird versuchen, den Prozess sauber zu beenden.
- SIGTERM - Beendet den Prozess, erlaubt ihm aber zuerst eine Bereinigung.
- SIGKILL - Beendet den Prozess, beendet ihn mit Feuer, führt keine Bereinigung durch.
- SIGSTOP - Stoppt/pausiert einen Prozess.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Prozessmanagement und -beendigung zu vertiefen:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** - In diesem Lab lernen Sie grundlegende Fähigkeiten zur Verwaltung und Überwachung von Prozessen auf einem Linux-System. Sie werden erkunden, wie Sie mit Vordergrund- und Hintergrundprozessen interagieren, diese mit `ps` inspizieren, Ressourcen mit `top` überwachen, die Priorität mit `renice` anpassen und sie mit `kill` beenden.

Dieses Lab wird Ihnen helfen, die Konzepte der Prozesssteuerung und -beendigung in realen Szenarien anzuwenden und Vertrauen im Umgang mit Linux-Prozessen aufzubauen.

## Quiz Question

Wie lautet der Signalname für den Standard-`kill`-Befehl?

## Quiz Answer

SIGTERM
