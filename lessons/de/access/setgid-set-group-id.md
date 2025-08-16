---
lang: "de"
title: "Setgid"
description: "Erfahren Sie mehr über Linux SGID (Set Group ID)-Berechtigungen, wie sie funktionieren und wie man sie ändert. Verstehen Sie dieses entscheidende Linux-Sicherheitskonzept."
keywords: "Linux SGID, Set Group ID, Linux-Berechtigungen, chmod g+s, Linux-Sicherheit, Linux für Anfänger, Linux-Tutorial"
---

## Lesson Content

Ähnlich dem Set User ID-Berechtigungsbit gibt es ein Set Group ID (SGID)-Berechtigungsbit. Dieses Bit ermöglicht es einem Programm, so ausgeführt zu werden, als wäre es Mitglied dieser Gruppe.

Betrachten wir ein Beispiel:

```bash
$ ls -l /usr/bin/wall
-rwxr-sr-x 1 root tty 19024 Dec 14 11:45 /usr/bin/wall
```

Wir können nun sehen, dass das Berechtigungsbit im Gruppenberechtigungssatz enthalten ist.

### Modifying SGID

```bash
sudo chmod g+s myfile
sudo chmod 2555 myfile
```

Die numerische Darstellung für SGID ist 2.

## Exercise

Keine Übungen für diese Lektion.

## Quiz Question

Welche Zahl repräsentiert das SGID?

## Quiz Answer

2
