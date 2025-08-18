---
index: 7
lang: "de"
title: "kill (Beenden)"
meta_title: "kill (Beenden) - Prozesse"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl 'kill' verwenden, um Prozesse zu beenden. Verstehen Sie SIGTERM, SIGKILL und andere Signale für die Prozessverwaltung. Beginnen Sie jetzt mit dem Lernen!"
meta_keywords: "kill-Befehl, Linux-Prozesse, SIGTERM, SIGKILL, Linux-Tutorial, Anfänger, Prozessverwaltung, Linux-Anleitung"
---

## Lesson Content

Sie können Signale senden, die Prozesse beenden; ein solcher Befehl wird passenderweise `kill` genannt.

```bash
kill 12445
```

Die `12445` ist die PID des Prozesses, den Sie beenden möchten. Standardmäßig wird ein `TERM`-Signal gesendet. Das `SIGTERM`-Signal wird an einen Prozess gesendet, um dessen Beendigung anzufordern, wodurch er seine Ressourcen sauber freigeben und seinen Zustand speichern kann.

Sie können auch ein Signal mit dem `kill`-Befehl angeben:

```bash
kill -9 12445
```

Dies führt das `SIGKILL`-Signal aus und beendet den Prozess.

### Unterschiede zwischen SIGHUP, SIGINT, SIGTERM, SIGKILL, SIGSTOP?

Diese Signale klingen alle einigermaßen ähnlich, aber sie haben ihre Unterschiede.

- SIGHUP - Hangup, wird an einen Prozess gesendet, wenn das steuernde Terminal geschlossen wird. Wenn Sie beispielsweise ein Terminalfenster geschlossen haben, in dem ein Prozess lief, würden Sie ein `SIGHUP`-Signal erhalten. Im Grunde wurden Sie also aufgelegt.
- SIGINT - Ist ein Interrupt-Signal, sodass Sie Strg-C verwenden können, und das System wird versuchen, den Prozess sauber zu beenden.
- SIGTERM - Beendet den Prozess, erlaubt ihm aber zuerst eine Bereinigung.
- SIGKILL - Beendet den Prozess, beendet ihn mit Feuer, führt keine Bereinigung durch.
- SIGSTOP - Stoppt/pausiert einen Prozess.

## Exercise

Beenden Sie einige Prozesse mit verschiedenen Signalen.

## Quiz Question

Wie lautet der Signalname für den Standardbefehl `kill`?

## Quiz Answer

SIGTERM
