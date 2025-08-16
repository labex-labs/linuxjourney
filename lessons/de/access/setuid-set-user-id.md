---
title: "Setuid"
description: "Erfahren Sie mehr über Linux Setuid (SUID)-Berechtigungen, wie sie funktionieren und wie man sie ändert. Verstehen Sie SUID für sicheren Dateizugriff in Linux."
keywords: "Linux Setuid, SUID, Linux-Berechtigungen, chmod, passwd-Befehl, Linux-Sicherheit, Linux für Anfänger, Linux-Tutorial"
---

## Lesson Content

Es gibt viele Fälle, in denen normale Benutzer erhöhte Zugriffsrechte benötigen, um Aufgaben auszuführen. Der Systemadministrator kann nicht immer anwesend sein, um jedes Mal ein Root-Passwort einzugeben, wenn ein Benutzer Zugriff auf eine geschützte Datei benötigt. Daher gibt es spezielle Dateiberechtigungsbits, um dieses Verhalten zu ermöglichen. Die Set User ID (SUID) erlaubt es einem Benutzer, ein Programm als Eigentümer der Programmdatei und nicht als er selbst auszuführen.

Schauen wir uns ein Beispiel an:

Nehmen wir an, ich möchte mein Passwort ändern, ganz einfach, oder? Ich benutze einfach den Befehl `passwd`:

```bash
passwd
```

Was macht der Befehl `passwd`? Er ändert ein paar Dateien, aber am wichtigsten ist, dass er die Datei `/etc/shadow` ändert. Schauen wir uns diese Datei kurz an:

```bash
$ ls -l /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
```

Oh, warten Sie mal, diese Datei gehört root? Wie ist es möglich, dass wir eine Datei ändern können, die root gehört?

Schauen wir uns einen weiteren Berechtigungssatz an, diesmal den des Befehls, den wir ausgeführt haben:

```bash
$ ls -l /usr/bin/passwd

-rwsr-xr-x 1 root root 47032 Dec 1 11:45 /usr/bin/passwd
```

Sie werden hier ein neues Berechtigungsbit bemerken: **s**. Dieses Berechtigungsbit ist das SUID. Wenn eine Datei diese Berechtigung gesetzt hat, erlaubt es den Benutzern, die das Programm gestartet haben, die Berechtigung des Dateieigentümers sowie die Ausführungsberechtigung zu erhalten, in diesem Fall root. Im Wesentlichen läuft ein Benutzer, während er den Befehl `passwd` ausführt, als root.

Deshalb können wir auf eine geschützte Datei wie `/etc/shadow` zugreifen, wenn wir den Befehl `passwd` ausführen. Wenn Sie dieses Bit entfernen würden, würden Sie feststellen, dass Sie `/etc/shadow` nicht ändern und somit Ihr Passwort nicht ändern können.

### Modifying SUID

Genau wie bei regulären Berechtigungen gibt es zwei Möglichkeiten, SUID-Berechtigungen zu ändern.

_Symbolische Art:_

```bash
sudo chmod u+s myfile
```

_Numerische Art:_

```bash
sudo chmod 4755 myfile
```

Wie Sie sehen können, wird das SUID durch eine 4 dargestellt und dem Berechtigungssatz vorangestellt. Möglicherweise sehen Sie das SUID als Großbuchstaben **S** dargestellt. Dies bedeutet, dass es immer noch dasselbe tut, aber keine Ausführungsberechtigungen hat.

## Exercise

Schauen Sie sich die Berechtigungen für `/etc/passwd` im Detail an. Fällt Ihnen noch etwas auf? Dateien mit aktiviertem SUID sind auch leicht zu unterscheiden.

## Quiz Question

Welche Zahl repräsentiert das SUID?

## Quiz Answer

4
