---
lang: "de"
title: "root"
meta_title: "root - Benutzerverwaltung"
meta_description: "Erfahren Sie mehr über den Linux-Root-Benutzer, den su-Befehl und die Datei /etc/sudoers. Verstehen Sie Superuser-Zugriff und Berechtigungen in Linux mit diesem Anfängerleitfaden."
meta_keywords: "Linux root, su command, sudoers file, Linux permissions, superuser, Linux tutorial, Anfängerleitfaden"
---

## Lesson Content

Wir haben eine Möglichkeit kennengelernt, Superuser-Zugriff mit dem Befehl `sudo` zu erhalten. Sie können Befehle auch als Superuser mit dem Befehl `su` ausführen. Dieser Befehl wird „Benutzer wechseln“ und eine Root-Shell öffnen, wenn kein Benutzername angegeben ist. Sie können diesen Befehl verwenden, um zu jedem Benutzer zu wechseln, solange Sie das Passwort kennen.

```bash
su
```

Die Verwendung dieser Methode hat einige Nachteile: Es ist viel einfacher, einen kritischen Fehler zu machen, wenn alles als Root ausgeführt wird, Sie haben keine Aufzeichnungen über die Befehle, die Sie zum Ändern von Systemkonfigurationen verwenden, usw. Grundsätzlich gilt: Wenn Sie Befehle als Superuser ausführen müssen, bleiben Sie einfach bei `sudo`.

Nun, da Sie wissen, welche Befehle als Superuser ausgeführt werden sollen, stellt sich die Frage, woher Sie wissen, wer Zugriff dazu hat? Das System lässt nicht jeden Hans und Franz Befehle als Superuser ausführen, woher weiß es das also? Es gibt eine Datei namens `/etc/sudoers`; diese Datei listet Benutzer auf, die `sudo` ausführen können. Sie können diese Datei mit dem Befehl **visudo** bearbeiten.

## Exercise

Öffnen Sie die Datei `/etc/sudoers` und sehen Sie, welche Superuser-Berechtigungen andere Benutzer auf dem Computer haben.

## Quiz Question

Welche Datei zeigt die Benutzer an, die Zugriff auf `sudo` haben?

## Quiz Answer

/etc/sudoers
