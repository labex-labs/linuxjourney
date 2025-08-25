---
index: 6
lang: "de"
title: "Setgid"
meta_title: "Setgid - Berechtigungen"
meta_description: "Erfahren Sie mehr über Linux SGID (Set Group ID) Berechtigungen, wie sie funktionieren und wie man sie ändert. Verstehen Sie dieses entscheidende Linux-Sicherheitskonzept."
meta_keywords: "Linux SGID, Set Group ID, Linux-Berechtigungen, chmod g+s, Linux-Sicherheit, Linux für Anfänger, Linux-Tutorial"
---

## Lesson Content

Ähnlich dem Set-User-ID-Berechtigungsbit gibt es ein Set-Group-ID (SGID)-Berechtigungsbit. Dieses Bit ermöglicht es einem Programm, so ausgeführt zu werden, als wäre es ein Mitglied dieser Gruppe.

Schauen wir uns ein Beispiel an:

```bash
$ ls -l /usr/bin/wall
-rwxr-sr-x 1 root tty 19024 Dec 14 11:45 /usr/bin/wall
```

Wir können nun sehen, dass das Berechtigungsbit im Gruppenberechtigungssatz enthalten ist.

### SGID ändern

```bash
sudo chmod g+s myfile
sudo chmod 2555 myfile
```

Die numerische Darstellung für SGID ist 2.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Linux-Benutzer-, Gruppen- und Dateiberechtigungen zu vertiefen:

1. **[Linux-Benutzergruppen- und Dateiberechtigungen](https://labex.io/de/labs/linux-linux-user-group-and-file-permissions-18002)** – Lernen Sie grundlegende Konzepte der Linux-Benutzer- und Gruppenverwaltung, einschließlich des Erstellens und Verwaltens von Benutzern, des Erkundens von Gruppenmitgliedschaften, des Verständnisses von Dateiberechtigungen und des Manipulierens von Dateibesitz.
2. **[Neuen Benutzer und neue Gruppe hinzufügen](https://labex.io/de/labs/linux-add-new-user-and-group-17987)** – Üben Sie das Erstellen neuer Benutzerkonten, das Einrichten benutzerdefinierter Gruppen und das Verwalten von Gruppenmitgliedschaften, um reale Systemadministrationsaufgaben zu simulieren.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in Linux-Berechtigungen und Benutzerverwaltung aufzubauen.

## Quiz Question

Welche Zahl repräsentiert die SGID?

## Quiz Answer

2
