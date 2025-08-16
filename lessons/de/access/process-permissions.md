---
title: "Prozessberechtigungen"
description: "Erfahren Sie mehr über Linux-Prozessberechtigungen, einschließlich Real-, Effective- und Saved-User-IDs. Verstehen Sie, wie UIDs die Sicherheit und Befehlsausführung beeinflussen. Beginnen Sie noch heute mit dem Lernen!"
keywords: "Linux-Prozessberechtigungen, Real UID, Effective UID, Saved UID, Linux-Sicherheit, passwd-Befehl, Linux-Tutorial, Linux für Anfänger"
---

## Lesson Content

Lassen Sie uns kurz auf Prozessberechtigungen eingehen. Erinnern Sie sich, wie ich Ihnen sagte, dass Sie, wenn Sie den Befehl `passwd` mit aktiviertem SUID-Berechtigungsbit ausführen, das Programm als root ausführen werden? Das stimmt. Bedeutet das jedoch, dass Sie, da Sie vorübergehend root sind, die Passwörter anderer Benutzer ändern können? Nein, glücklicherweise nicht!

Dies liegt an den vielen UIDs, die Linux implementiert. Es gibt drei UIDs, die jedem Prozess zugeordnet sind:

Wenn Sie einen Prozess starten, läuft dieser mit denselben Berechtigungen wie der Benutzer oder die Gruppe, die ihn gestartet hat. Dies wird als **effektive Benutzer-ID** bezeichnet. Diese UID wird verwendet, um einem Prozess Zugriffsrechte zu gewähren. Wenn Bob also den Befehl `touch` ausgeführt hat, würde der Prozess natürlich als er laufen, und alle von ihm erstellten Dateien wären in seinem Besitz.

Es gibt eine weitere UID, die **reale Benutzer-ID** genannt wird. Dies ist die ID des Benutzers, der den Prozess gestartet hat. Diese werden verwendet, um zu verfolgen, wer der Benutzer ist, der den Prozess gestartet hat.

Eine letzte UID ist die **gespeicherte Benutzer-ID**. Diese ermöglicht es einem Prozess, zwischen der effektiven UID und der realen UID zu wechseln und umgekehrt. Dies ist nützlich, da wir nicht möchten, dass unser Prozess ständig mit erhöhten Rechten läuft; es ist einfach eine gute Praxis, spezielle Privilegien zu bestimmten Zeiten zu verwenden.

Lassen Sie uns nun all dies zusammenfügen, indem wir uns den Befehl `passwd` noch einmal ansehen.

Beim Ausführen des Befehls `passwd` ist Ihre effektive UID Ihre Benutzer-ID; nehmen wir an, sie ist vorerst 500. Oh, aber warten Sie, erinnern Sie sich, der Befehl `passwd` hat die SUID-Berechtigung aktiviert. Wenn Sie ihn also ausführen, ist Ihre effektive UID jetzt 0 (0 ist die UID von root). Jetzt kann dieses Programm als root auf Dateien zugreifen.

Nehmen wir an, Sie bekommen ein wenig Macht zu spüren und möchten Sallys Passwort ändern. Sally hat eine UID von 600. Nun, Sie werden Pech haben. Glücklicherweise hat der Prozess auch Ihre reale UID, in diesem Fall 500. Er weiß, dass Ihre UID 500 ist, und daher können Sie das Passwort der UID 600 nicht ändern. (Dies wird natürlich immer umgangen, wenn Sie ein Superuser auf einem Computer sind und alles kontrollieren und ändern können).

Da Sie `passwd` ausgeführt haben, startet es den Prozess mit Ihrer realen UID und speichert die UID des Dateibesitzers (effektive UID), sodass Sie zwischen den beiden wechseln können. Es ist nicht nötig, alle Dateien mit Root-Zugriff zu ändern, wenn dies nicht erforderlich ist.

Meistens sind die reale UID und die effektive UID gleich, aber in Fällen wie dem Befehl `passwd` ändern sie sich.

## Exercise

Wir haben Prozesse noch nicht besprochen, aber wir können diese Änderung trotzdem in Echtzeit beobachten:

1. Open one terminal window and run the command: `watch -n 1 "ps aux | grep passwd"`. This will watch for the `passwd` process.
2. Open a second terminal window and run: `passwd`.
3. Look at the first terminal window; you'll see a process come up for `passwd`. The first column in the process table is the effective user ID. Lo and behold, it's the root user!

## Quiz Question

Welche UID entscheidet, welcher Zugriff gewährt werden soll?

## Quiz Answer

effective
