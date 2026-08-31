---
lesson_id: "controlling-terminal"
course_id: "processes"
lang: "de"
order_index: 2
title: "Steuerndes Terminal"
description: "Erfahre, wie steuernde Terminals Sitzungen mit interaktiver Eingabe, Signalen und der Jobsteuerung der Shell verbinden."
meta_title: "Steuerndes Terminal – Prozesse"
meta_description: "Erkunde das Konzept eines steuernden Terminals unter Linux. Erfahre, was ein TTY ist, worin sich TTY und PTS unterscheiden und wie du die `ps`-Ausgabe TTY verwendest, um Prozesse ohne steuerndes Terminal wie Daemons zu erkennen."
meta_keywords: "steuerndes Terminal, ps tty, was ist tty, ps verwenden, TTY, PTS, Linux-Terminal, Daemon-Prozess, Linux-Prozesse"
---

Eine interaktive Anmeldesitzung kann ein steuerndes Terminal besitzen: ein der Sitzung zugeordnetes Terminalgerät, das der Kernel für vom Terminal erzeugte Signale und die Jobsteuerung verwendet. Das Feld `TTY` in Prozessauflistungen hilft dabei, diese Zuordnung zu erkennen.

## Terminal- und Pseudo-Terminalgeräte

Die Bezeichnung TTY stammt von historischen Fernschreibern. Unter modernem Linux sind Terminalschnittstellen Geräteabstraktionen und nicht unbedingt physische Geräte.

Eine virtuelle Systemkonsole kann unter einem Namen wie `tty1` erscheinen. Die Tastenkombinationen zum Wechseln zwischen Konsolen unterscheiden sich je nach Distribution und sollten nicht vorausgesetzt werden. Ein Terminalemulator, eine entfernte Anmeldung oder ein Multiplexer verwendet gewöhnlich ein Pseudo-Terminalpaar, dessen interaktive Seite unter einem Namen wie `pts/3` angezeigt wird.

Zeige das mit der Standardeingabe des aktuellen Befehls verbundene Terminal an mit:

```bash
$ tty
/dev/pts/3
```

Dieses Ergebnis hängt mit dem umfassenderen Konzept des steuernden Terminals zusammen, ist aber nicht mit ihm identisch. Ein Prozess kann seine Standardeingabe oder -ausgabe umleiten und dennoch zu einer Sitzung mit steuerndem Terminal gehören.

:::single-choice{#controlling-terminal-pts-meaning}
Was kennzeichnet ein Name wie `pts/3` gewöhnlich?

::option[Eine Prozess-ID, die der dritten Shell zugewiesen wurde.]{#controlling-terminal-pts-pid explanation="Eine PID ist eine numerische Prozessmetadatenangabe und wird nicht als Gerätename `pts/N` ausgedrückt."}
::option[Ein Pseudo-Terminalgerät, das von einer interaktiven Sitzung verwendet wird.]{#controlling-terminal-pts-device .correct explanation="Einträge unter `/dev/pts` sind Pseudo-Terminal-Slave-Geräte, die häufig von Terminalemulatoren und entfernten Sitzungen verwendet werden."}
::option[Eine Dateisystempartition mit Terminalprogrammen.]{#controlling-terminal-pts-partition explanation="Der Name bezeichnet eine Terminalgeräteschnittstelle und keine Speicherpartition."}
:::

## Sitzungen, Prozessgruppen und Jobsteuerung

Ein steuerndes Terminal gehört zu einer Sitzung und nicht bloß zu dem Befehl, der zufällig ein Fenster geöffnet hat. Innerhalb dieser Sitzung verfolgt das Terminal eine Vordergrundprozessgruppe. Die Shell stellt eine Vordergrund-Pipeline in diese Gruppe, damit sie Eingaben lesen und vom Terminal erzeugte Signale empfangen kann.

Das Drücken von `Ctrl-C` veranlasst den Terminaltreiber beispielsweise gewöhnlich, `SIGINT` an die Vordergrundprozessgruppe zu senden. Eine Hintergrundgruppe, die vom Terminal zu lesen versucht, kann `SIGTTIN` empfangen. Diese Regeln ermöglichen der Shell die Koordination von Vordergrund- und Hintergrundjobs.

:::single-choice{#controlling-terminal-ctrl-c-target}
An welche Prozesse richtet ein Terminal gewöhnlich das durch `Ctrl-C` erzeugte Signal?

::option[An jeden Prozess, der dem aktuellen Benutzer gehört.]{#controlling-terminal-ctrl-c-user explanation="Vom Terminal erzeugte Signale sind auf die Vordergrundprozessgruppe begrenzt und nicht auf alle Prozesse eines Benutzers gerichtet."}
::option[Unabhängig vom Vordergrundjob ausschließlich an die Anmelde-Shell.]{#controlling-terminal-ctrl-c-shell explanation="Während ein anderer Job im Vordergrund läuft, ist gewöhnlich dessen Gruppe das Signalziel."}
::option[An die Vordergrundprozessgruppe des Terminals.]{#controlling-terminal-ctrl-c-foreground .correct explanation="Der Terminaltreiber sendet `SIGINT` an die aktuelle Vordergrundprozessgruppe."}
:::

## Die Spalte `TTY` lesen

Fordere bestimmte Prozessfelder ausdrücklich an, wenn du eine stabile Ansicht möchtest:

```bash
$ ps -o pid,tty,stat,cmd
```

Ein Terminalname wie `pts/3` bezeichnet das für diesen Prozess erfasste steuernde Terminal. Ein Fragezeichen (`?`) bedeutet gewöhnlich, dass der Prozess kein steuerndes Terminal besitzt.

Viele Dienstprozesse besitzen kein steuerndes Terminal, weil ein Dienstmanager sie unabhängig von einer interaktiven Anmeldesitzung startet. Ein fehlendes TTY beweist für sich allein jedoch nicht, dass ein Prozess ein Daemon ist, und ein Hintergrundjob der Shell kann weiterhin ein steuerndes Terminal besitzen.

:::single-choice{#controlling-terminal-question-mark}
Was bedeutet `?` in der Spalte `TTY` von `ps` gewöhnlich?

::option[Der Prozess besitzt kein steuerndes Terminal.]{#controlling-terminal-no-tty .correct explanation="Ein Fragezeichen ist die übliche Darstellung, wenn dem Prozess kein steuerndes Terminal zugeordnet ist."}
::option[Das Terminal des Prozesses konnte nicht gelesen werden, weil es belegt ist.]{#controlling-terminal-busy-tty explanation="Die Markierung steht für das Fehlen eines steuernden Terminals und nicht für eine vorübergehende Gerätebelegung."}
::option[Der Prozess ist immer ein Kernel-Thread.]{#controlling-terminal-kernel-only explanation="Kernel-Threads besitzen häufig keine Terminals, aber dasselbe gilt für viele Dienste im User-Space."}
:::

## Schließen des Terminals und Hangups

Wenn eine Terminalverbindung verschwindet, kann der Kernel oder die Terminal-/Sitzungssoftware `SIGHUP` an zugehörige Prozesse senden. Ein Prozess kann sich beenden, das Signal abfangen, es ignorieren oder bereits so eingerichtet worden sein, dass er es überlebt. Shell-Funktionen wie `disown`, Werkzeuge wie `nohup`, Multiplexer und Dienstmanager beeinflussen das Lebenszyklusverhalten.

Das Schließen eines Terminals garantiert daher nicht, dass sich jeder darin gestartete Befehl beendet. Prüfe die Sitzung, Signalbehandlung, Umleitungen und den Supervisor eines Prozesses, wenn sein Fortbestehen wichtig ist.

:::single-choice{#controlling-terminal-close-effect}
Warum ist die Aussage ungenau, das Schließen eines Terminals beende immer jeden darin gestarteten Prozess?

::option[Linux-Terminals erzeugen beim Schließen niemals Signale.]{#controlling-terminal-never-signals explanation="Hangup-Signale sind ein reales Terminal- und Sitzungsverhalten, auch wenn sie nicht garantiert zur Beendigung führen."}
::option[Nur Prozesse mit numerischen PIDs können Hangups empfangen.]{#controlling-terminal-pid-hangup explanation="Alle gewöhnlichen Prozesse besitzen numerische PIDs; diese Tatsache bestimmt nicht, ob sie ein Terminal überleben."}
::option[Prozesse können den Hangup behandeln oder vermeiden und unabhängig verwaltet werden.]{#controlling-terminal-hangup-handling .correct explanation="Signalbehandlung, Shell-Verhalten, Multiplexer und Supervisoren können einem Prozess erlauben, nach dem Schließen des Terminals weiterzulaufen."}
:::

Das Lab [Linux-Prozesse verwalten und überwachen](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) bietet eine sichere Umgebung, um Vordergrundjobs, Hintergrundjobs und ihre `TTY`-Felder zu vergleichen.

## Zusammenfassung

Du kannst nun ein steuerndes Terminal mit der interaktiven Prozessverwaltung in Beziehung setzen.

1. Unterscheide virtuelle Terminals von Pseudo-Terminals.
2. Verbinde Terminalsignale mit der Vordergrundprozessgruppe.
3. Interpretiere Terminalnamen und `?` in der Ausgabe von `ps`.
4. Behandle das Schließen eines Terminals als Signalisierung und nicht als garantierte Prozessbeendigung.
