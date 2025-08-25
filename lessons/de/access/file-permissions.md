---
index: 1
lang: "de"
title: "Dateiberechtigungen"
meta_title: "Dateiberechtigungen - Berechtigungen"
meta_description: "Lernen Sie Linux-Dateiberechtigungen: Verstehen Sie rwx-Bits, Benutzer-, Gruppen- und andere Berechtigungen. Meistern Sie die Ausgabe von `ls -l` für Anfänger. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "Linux-Dateiberechtigungen, ls -l Befehl, rwx Berechtigungen, Linux-Tutorial, Dateimodi, Linux für Anfänger, Linux-Anleitung"
---

## Lesson Content

Wie wir bereits gelernt haben, haben Dateien unterschiedliche Berechtigungen oder Dateimodi. Schauen wir uns ein Beispiel an:

```bash
$ ls -l Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 .
```

Die Berechtigungen einer Datei bestehen aus vier Teilen. Der erste Teil ist der Dateityp, der durch das erste Zeichen in den Berechtigungen angegeben wird. In unserem Fall, da wir ein Verzeichnis betrachten, wird **d** für den Dateityp angezeigt. Am häufigsten sehen Sie ein **-** für eine reguläre Datei.

Die nächsten drei Teile des Dateimodus sind die eigentlichen Berechtigungen. Die Berechtigungen sind in jeweils 3 Bits gruppiert. Die ersten 3 Bits sind Benutzerberechtigungen, dann Gruppenberechtigungen und dann andere Berechtigungen. Ich habe die Pipe hinzugefügt, um die Unterscheidung zu erleichtern.

```plaintext
d | rwx | r-x | r-x
```

Jedes Zeichen steht für eine andere Berechtigung:

- r: lesbar
- w: schreibbar
- x: ausführbar (im Grunde ein ausführbares Programm)
- -: leer

Im obigen Beispiel sehen wir also, dass der Benutzer pete Lese-, Schreib- und Ausführungsberechtigungen für die Datei hat. Die Gruppe penguins hat Lese- und Ausführungsberechtigungen. Und schließlich haben die anderen Benutzer (alle anderen) Lese- und Ausführungsberechtigungen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Linux-Dateiberechtigungen, Benutzern und Gruppen zu vertiefen:

1. **[Linux Benutzergruppe und Dateiberechtigungen](https://labex.io/de/labs/linux-linux-user-group-and-file-permissions-18002)** – Lernen Sie grundlegende Konzepte der Linux-Benutzer- und Gruppenverwaltung, einschließlich des Erstellens von Benutzern, des Erkundens von Gruppenmitgliedschaften, des Verständnisses von Dateiberechtigungen und der Manipulation von Dateibesitz.
2. **[Neuen Benutzer und Gruppe hinzufügen](https://labex.io/de/labs/linux-add-new-user-and-group-17987)** – Üben Sie das Erstellen neuer Benutzerkonten, das Einrichten benutzerdefinierter Gruppen und das Verwalten von Gruppenmitgliedschaften, um reale Systemadministrationsaufgaben zu simulieren.
3. **[Eine Datei finden](https://labex.io/de/labs/linux-find-a-file-17993)** – Wenden Sie Ihr Wissen über Dateiberechtigungen an, indem Sie eine bestimmte Datei finden und deren Zugriffsrechte festlegen, um sicherzustellen, dass Sie der einzige autorisierte Benutzer sind.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Berechtigungen und Benutzern in Linux aufzubauen.

## Quiz Question

Welches Berechtigungsbit wird für ausführbar verwendet?

## Quiz Answer

x
