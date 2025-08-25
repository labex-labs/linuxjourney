---
index: 5
lang: "de"
title: "Setuid"
meta_title: "Setuid - Berechtigungen"
meta_description: "Erfahren Sie mehr über Linux Setuid (SUID)-Berechtigungen, wie sie funktionieren und wie man sie ändert. Verstehen Sie SUID für sicheren Dateizugriff in Linux."
meta_keywords: "Linux Setuid, SUID, Linux-Berechtigungen, chmod, passwd-Befehl, Linux-Sicherheit, Linux für Anfänger, Linux-Tutorial"
---

## Lesson Content

Es gibt viele Fälle, in denen normale Benutzer erhöhten Zugriff benötigen, um Aufgaben auszuführen. Der Systemadministrator kann nicht immer zur Stelle sein, um jedes Mal ein Root-Passwort einzugeben, wenn ein Benutzer Zugriff auf eine geschützte Datei benötigt. Daher gibt es spezielle Dateiberechtigungsbits, um dieses Verhalten zu ermöglichen. Die Set User ID (SUID) erlaubt es einem Benutzer, ein Programm als Eigentümer der Programmdatei und nicht als er selbst auszuführen.

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

### SUID ändern

Genau wie bei regulären Berechtigungen gibt es zwei Möglichkeiten, SUID-Berechtigungen zu ändern.

_Symbolische Methode:_

```bash
sudo chmod u+s myfile
```

_Numerische Methode:_

```bash
sudo chmod 4755 myfile
```

Wie Sie sehen können, wird das SUID durch eine 4 dargestellt und dem Berechtigungssatz vorangestellt. Möglicherweise sehen Sie das SUID als Großbuchstaben **S** dargestellt. Das bedeutet, dass es immer noch dasselbe tut, aber keine Ausführungsberechtigungen hat.

## Exercise

Übung macht den Meister! Das Verständnis, wie Dateiberechtigungen, Benutzergruppen und spezielle Bits wie SUID funktionieren, ist entscheidend für die Verwaltung und Sicherung von Linux-Systemen. Praktische Erfahrung wird Ihr Wissen festigen.

Hier ist ein praktisches Labor, um Ihr Verständnis von Dateiberechtigungen und Benutzerverwaltung zu vertiefen:

1. **[Linux Benutzergruppen und Dateiberechtigungen](https://labex.io/de/labs/linux-linux-user-group-and-file-permissions-18002)** - Üben Sie das Erstellen und Verwalten von Benutzern und Gruppen, das Verständnis von Dateiberechtigungen und das Manipulieren des Dateibesitzes. Dieses Labor vermittelt das grundlegende Wissen, das notwendig ist, um zu verstehen, wie SUID diese Konzepte für erhöhten Zugriff nutzt.

Dieses Labor wird Ihnen helfen, die Konzepte in einem realen Szenario anzuwenden und Vertrauen in die Linux-Benutzer- und Dateiverwaltung aufzubauen.

## Quiz Question

Welche Zahl repräsentiert das SUID?

## Quiz Answer

4
