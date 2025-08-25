---
index: 2
lang: "de"
title: "root"
meta_title: "root - Benutzerverwaltung"
meta_description: "Erfahren Sie mehr über den Linux-Root-Benutzer, den su-Befehl und die Datei /etc/sudoers. Verstehen Sie Superuser-Zugriff und Berechtigungen in Linux mit diesem Leitfaden für Anfänger."
meta_keywords: "Linux root, su Befehl, sudoers Datei, Linux Berechtigungen, Superuser, Linux Tutorial, Anfängerleitfaden"
---

## Lesson Content

Wir haben eine Möglichkeit kennengelernt, Superuser-Zugriff mit dem Befehl `sudo` zu erhalten. Sie können Befehle auch als Superuser mit dem Befehl `su` ausführen. Dieser Befehl wird „Benutzer wechseln“ und öffnet eine Root-Shell, wenn kein Benutzername angegeben ist. Sie können diesen Befehl verwenden, um zu jedem Benutzer zu wechseln, solange Sie das Passwort kennen.

```bash
su
```

Die Verwendung dieser Methode hat einige Nachteile: Es ist viel einfacher, einen kritischen Fehler zu machen, wenn alles als Root ausgeführt wird, Sie haben keine Aufzeichnungen über die Befehle, die Sie zum Ändern von Systemkonfigurationen verwenden, usw. Grundsätzlich gilt: Wenn Sie Befehle als Superuser ausführen müssen, bleiben Sie einfach bei `sudo`.

Nachdem Sie nun wissen, welche Befehle als Superuser ausgeführt werden müssen, stellt sich die Frage, woher Sie wissen, wer Zugriff darauf hat? Das System lässt nicht jeden Joe Schmoe Befehle als Superuser ausführen, woher weiß es das also? Es gibt eine Datei namens `/etc/sudoers`; diese Datei listet Benutzer auf, die `sudo` ausführen können. Sie können diese Datei mit dem Befehl **visudo** bearbeiten.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Superuser-Zugriff und -Berechtigungen zu vertiefen:

1. **[Benutzerkonten und Sudo-Berechtigungen in Linux konfigurieren](https://labex.io/de/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** – Üben Sie das Erzwingen von Passwortrichtlinien, das Sperren und Entsperren von Benutzerkonten, das Sichern des Root-Kontos und das Erteilen von Administratorberechtigungen, direkt im Zusammenhang mit der Verwaltung des Superuser-Zugriffs.

Dieses Lab hilft Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Benutzerberechtigungen und Superuser-Zugriff aufzubauen.

## Quiz Question

Welche Datei zeigt die Benutzer, die Zugriff auf `sudo` haben?

## Quiz Answer

/etc/sudoers
