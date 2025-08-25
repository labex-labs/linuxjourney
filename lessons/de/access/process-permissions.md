---
index: 7
lang: "de"
title: "Prozessberechtigungen"
meta_title: "Prozessberechtigungen - Berechtigungen"
meta_description: "Erfahren Sie mehr über Linux-Prozessberechtigungen, einschließlich Real-, Effektiver und Gespeicherter Benutzer-IDs. Verstehen Sie, wie UIDs die Sicherheit und Befehlsausführung beeinflussen. Beginnen Sie noch heute mit dem Lernen!"
meta_keywords: "Linux-Prozessberechtigungen, Reale UID, Effektive UID, Gespeicherte UID, Linux-Sicherheit, passwd-Befehl, Linux-Tutorial, Linux für Anfänger"
---

## Lesson Content

Lassen Sie uns kurz zu den Prozessberechtigungen übergehen. Erinnern Sie sich, wie ich Ihnen sagte, dass Sie, wenn Sie den Befehl `passwd` mit aktiviertem SUID-Berechtigungsbit ausführen, das Programm als root ausführen werden? Das stimmt. Bedeutet das aber, dass Sie, da Sie vorübergehend root sind, die Passwörter anderer Benutzer ändern können? Nein, glücklicherweise nicht!

Dies liegt an den vielen UIDs, die Linux implementiert. Jedem Prozess sind drei UIDs zugeordnet:

Wenn Sie einen Prozess starten, läuft dieser mit denselben Berechtigungen wie der Benutzer oder die Gruppe, die ihn gestartet hat. Dies wird als **effektive Benutzer-ID** bezeichnet. Diese UID wird verwendet, um einem Prozess Zugriffsrechte zu gewähren. Wenn Bob also den Befehl `touch` ausgeführt hat, würde der Prozess als er ausgeführt werden, und alle von ihm erstellten Dateien wären in seinem Besitz.

Es gibt eine weitere UID, die **reale Benutzer-ID** genannt wird. Dies ist die ID des Benutzers, der den Prozess gestartet hat. Diese werden verwendet, um zu verfolgen, wer der Benutzer ist, der den Prozess gestartet hat.

Eine letzte UID ist die **gespeicherte Benutzer-ID**. Diese ermöglicht es einem Prozess, zwischen der effektiven UID und der realen UID zu wechseln und umgekehrt. Dies ist nützlich, da wir nicht möchten, dass unser Prozess ständig mit erhöhten Rechten läuft; es ist einfach eine gute Praxis, spezielle Rechte zu bestimmten Zeiten zu verwenden.

Lassen Sie uns diese nun alle zusammenfügen, indem wir uns den Befehl `passwd` noch einmal ansehen.

Beim Ausführen des Befehls `passwd` ist Ihre effektive UID Ihre Benutzer-ID; sagen wir vorerst 500. Oh, aber warten Sie, erinnern Sie sich, der Befehl `passwd` hat die SUID-Berechtigung aktiviert. Wenn Sie ihn also ausführen, ist Ihre effektive UID jetzt 0 (0 ist die UID von root). Jetzt kann dieses Programm als root auf Dateien zugreifen.

Nehmen wir an, Sie bekommen ein wenig Macht zu schmecken und möchten Sallys Passwort ändern. Sally hat eine UID von 600. Nun, Sie werden Pech haben. Glücklicherweise hat der Prozess auch Ihre reale UID, in diesem Fall 500. Er weiß, dass Ihre UID 500 ist, und daher können Sie das Passwort von UID 600 nicht ändern. (Dies wird natürlich immer umgangen, wenn Sie ein Superuser auf einem Computer sind und alles kontrollieren und ändern können).

Da Sie `passwd` ausgeführt haben, wird der Prozess mit Ihrer realen UID gestartet, und die UID des Dateibesitzers (effektive UID) wird gespeichert, sodass Sie zwischen den beiden wechseln können. Es ist nicht nötig, alle Dateien mit Root-Zugriff zu ändern, wenn dies nicht erforderlich ist.

Meistens sind die reale UID und die effektive UID gleich, aber in Fällen wie dem Befehl `passwd` ändern sie sich.

## Exercise

Übung macht den Meister! Das Verständnis von Benutzer-IDs und Prozessberechtigungen ist entscheidend für die Linux-Sicherheit und -Administration. Hier sind einige praktische Übungen, um Ihr Verständnis der Benutzer- und Gruppenverwaltung zu vertiefen, die die Grundlage für die Funktionsweise von UIDs bildet:

1. **[Linux Benutzergruppe und Dateiberechtigungen](https://labex.io/de/labs/linux-linux-user-group-and-file-permissions-18002)** – Lernen Sie grundlegende Konzepte der Linux-Benutzer- und Gruppenverwaltung, einschließlich des Erstellens und Verwaltens von Benutzern, des Erkundens von Gruppenmitgliedschaften, des Verständnisses von Dateiberechtigungen und des Manipulierens von Dateibesitz. Dieses Labor bietet praktische Erfahrung bei der Sicherung einer Multi-User-Linux-Umgebung.
2. **[Neuen Benutzer und Gruppe hinzufügen](https://labex.io/de/labs/linux-add-new-user-and-group-17987)** – In dieser Herausforderung simulieren Sie das Hinzufügen neuer Teammitglieder zu einer Serverumgebung, indem Sie neue Benutzerkonten erstellen, benutzerdefinierte Gruppen einrichten und Gruppenmitgliedschaften verwalten. Dies wird Ihre Fähigkeiten in der Linux-Benutzer- und Gruppenadministration testen, die für Systemadministratoren und DevOps-Profis unerlässlich sind.

Diese Übungen helfen Ihnen, die Konzepte der Benutzer- und Gruppenverwaltung in realen Szenarien anzuwenden und eine starke Grundlage für das Verständnis zu schaffen, wie UIDs den Zugriff und die Berechtigungen in Linux steuern.

## Quiz Question

Welche UID entscheidet, welcher Zugriff gewährt werden soll?

## Quiz Answer

effective
