---
index: 11
lang: "de"
title: "Inodes"
meta_title: "Inodes - Das Dateisystem"
meta_description: "Erkunden Sie das Konzept des Linux-Inodes. Erfahren Sie, was ein i-node ist, wie Inodes unter Linux Dateimetadaten verwalten und wie Sie die Inode-Nutzung mit `df -i` und `ls -li` überprüfen."
meta_keywords: "linux inode, inode in linux, i node, inode, inode linux, inode nummer, dateisystem, df -i, ls -li, stat"
---

## Lesson Content

Erinnern Sie sich, wie unser Dateisystem aus all unseren tatsächlichen Dateien und einer Datenbank besteht, die diese verwaltet? Diese Datenbank ist als Inode-Tabelle bekannt, ein grundlegender Bestandteil der Funktionsweise von `inode in linux`.

### Was ist ein Linux Inode

Ein Inode (Kurzform für Index Node) ist ein Eintrag in dieser Tabelle. Jede Datei und jedes Verzeichnis hat seinen eigenen `inode`. Er beschreibt alles über die Datei, wie zum Beispiel:

- Dateityp (z. B. reguläre Datei, Verzeichnis, Zeichengerät)
- Besitzer
- Gruppe
- Zugriffsberechtigungen
- Zeitstempel: mtime (letzte Änderung), ctime (letzte Attributänderung), atime (letzter Zugriff)
- Anzahl der Hardlinks auf die Datei
- Größe der Datei
- Anzahl der der Datei zugewiesenen Blöcke
- Zeiger auf die Datenblöcke der Datei (am wichtigsten!)

Im Wesentlichen speichert ein `i node` alle Metadaten über die Datei, außer deren Namen und dem eigentlichen Inhalt.

### Inode-Erstellung und -Zuweisung

Wenn ein Dateisystem erstellt wird, wird auch Speicherplatz für Inodes zugewiesen. Algorithmen bestimmen, wie viel `inode`-Speicherplatz Sie basierend auf dem Volumen der Festplatte und anderen Faktoren benötigen. Sie haben wahrscheinlich schon Fehler wegen "out of disk space" gesehen. Dasselbe kann mit Inodes passieren, obwohl es seltener vorkommt. Wenn Ihnen die Inodes ausgehen, können Sie keine neuen Dateien erstellen. Die Datenspeicherung hängt sowohl von den Datenblöcken als auch von der Datenbank (der `inode`-Tabelle) ab.

Um zu sehen, wie viele Inodes auf Ihrem System noch frei sind, verwenden Sie den Befehl `df -i`. Dies ist eine entscheidende Überprüfung für Systemadministratoren, die eine große Anzahl kleiner Dateien verwalten.

### Anzeigen von Inode-Informationen

Jeder `linux inode` wird durch eine eindeutige Nummer identifiziert. Wenn eine Datei erstellt wird, erhält sie eine Inode-Nummer, oft sequenziell. Sie werden jedoch möglicherweise feststellen, dass eine neue Datei eine niedrigere Inode-Nummer als ältere Dateien erhält. Dies geschieht, weil gelöschte Inode-Nummern für neue Dateien wiederverwendet werden können. Um Inode-Nummern anzuzeigen, führen Sie `ls -li` aus:

```bash
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

Das erste Feld in der Ausgabe dieses Befehls ist die Inode-Nummer. Detaillierte Informationen zum `i node` einer Datei erhalten Sie auch mit dem Befehl `stat`:

```bash
pete@icebox:~$ stat ~/Desktop/
  File: ‘/home/pete/Desktop/’
  Size: 6               Blocks: 0          IO Block: 4096   directory
Device: 806h/2054d      Inode: 140         Links: 2
Access: (0755/drwxr-xr-x)  Uid: ( 1000/   pete)   Gid: ( 1000/   pete)
Access: 2016-01-20 20:13:50.647435982 -0800
Modify: 2016-01-20 20:13:06.191675843 -0800
Change: 2016-01-20 20:13:06.191675843 -0800
 Birth: -
```

### Wie ein I-Node auf Daten verweist

Wir wissen, dass unsere Daten auf der Festplatte gespeichert sind, aber wahrscheinlich nicht in einem einzigen zusammenhängenden Block. Hier wird die Struktur des `inode linux` unerlässlich. Inodes verweisen auf die tatsächlichen Datenblöcke Ihrer Dateien. In einem typischen Dateisystem (obwohl die Implementierungen variieren) enthält jeder Inode 15 Zeiger. Die ersten 12 Zeiger verweisen direkt auf Datenblöcke. Der 13. Zeiger verweist auf einen Block, der weitere Zeiger enthält. Die 14. und 15. Zeiger verweisen auf weiter verschachtelte Zeigerblöcke. Das mag verwirrend erscheinen, aber diese Struktur ermöglicht es dem `i node`, eine feste Größe beizubehalten und gleichzeitig auf Dateien unterschiedlicher Größe verweisen zu können. Kleine Dateien können schnell über die direkten Zeiger abgerufen werden, während größere Dateien über die verschachtelten Zeiger gefunden werden.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis des Linux-Dateisystems und der Dateiverwaltung zu festigen:

1. **[Dateien und Verzeichnisse unter Linux verwalten](https://labex.io/de/labs/comptia-manage-files-and-directories-in-linux-590835)** - Üben Sie das Erstellen, Entfernen, Kopieren und Verschieben von Dateien und Verzeichnissen und erkunden Sie das Erstellen von symbolischen und Hardlinks, während Sie Inodes analysieren.
2. **[Im Linux-Dateisystem navigieren](https://labex.io/de/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Lernen Sie die grundlegenden Fähigkeiten zur Navigation im Linux-Dateisystem mithilfe wichtiger Shell-Befehle wie `pwd`, `cd` und `ls`.
3. **[Dateien und Befehle unter Linux finden](https://labex.io/de/labs/comptia-find-files-and-commands-in-linux-590834)** - Meistern Sie wesentliche Techniken zum Auffinden von Dateien und Befehlen unter Linux mit `find`, `locate`, `whereis`, `which` und `type`.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Selbstvertrauen in die Verwaltung des Linux-Dateisystems aufzubauen.

## Quiz Question

How do you see how many inodes are left on your system? (Please answer in English, paying attention to case sensitivity.)

## Quiz Answer

df -i
