---
index: 11
lang: "de"
title: "Inodes"
meta_title: "Inodes - Das Dateisystem"
meta_description: "Erfahren Sie mehr über Linux-Inodes, ihre Struktur und wie sie Dateien verwalten. Verstehen Sie Inode-Nummern und verwenden Sie `df -i` und `ls -li`, um die Inode-Nutzung zu überprüfen. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "Linux Inodes, Inode Tutorial, df -i, ls -li, Linux Dateisystem, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Erinnern Sie sich, wie unser Dateisystem aus all unseren tatsächlichen Dateien und einer Datenbank besteht, die diese Dateien verwaltet? Die Datenbank ist als Inode-Tabelle bekannt.

### Was ist ein Inode?

Ein Inode (Indexknoten) ist ein Eintrag in dieser Tabelle, und es gibt einen für jede Datei. Er beschreibt alles über die Datei, wie zum Beispiel:

- Dateityp – reguläre Datei, Verzeichnis, Zeichendatei usw.
- Eigentümer
- Gruppe
- Zugriffsrechte
- Zeitstempel – mtime (Zeit der letzten Dateimodifikation), ctime (Zeit der letzten Attributänderung), atime (Zeit des letzten Zugriffs)
- Anzahl der Hardlinks zur Datei
- Größe der Datei
- Anzahl der der Datei zugewiesenen Blöcke
- Zeiger auf die Datenblöcke der Datei – am wichtigsten!

Grundsätzlich speichern Inodes alles über die Datei, außer dem Dateinamen und der Datei selbst!

### Wann werden Inodes erstellt?

Wenn ein Dateisystem erstellt wird, wird auch Speicherplatz für Inodes zugewiesen. Algorithmen bestimmen, wie viel Inode-Speicherplatz Sie benötigen, abhängig vom Volumen der Festplatte und mehr. Sie haben wahrscheinlich irgendwann in Ihrem Leben Fehler wegen Speichermangels gesehen. Dasselbe kann auch bei Inodes auftreten (obwohl seltener); Ihnen können die Inodes ausgehen, und Sie können daher keine weiteren Dateien erstellen. Denken Sie daran, dass die Datenspeicherung sowohl von den Daten als auch von der Datenbank (Inodes) abhängt.

Um zu sehen, wie viele Inodes auf Ihrem System verbleiben, verwenden Sie den Befehl `df -i`.

### Inode-Informationen

Inodes werden durch Nummern identifiziert. Wenn eine Datei erstellt wird, wird ihr eine Inode-Nummer zugewiesen, und die Nummer wird in sequenzieller Reihenfolge zugewiesen. Manchmal bemerken Sie jedoch, dass eine neu erstellte Datei eine Inode-Nummer erhält, die niedriger ist als andere. Dies liegt daran, dass gelöschte Inodes von anderen Dateien wiederverwendet werden können. Um Inode-Nummern anzuzeigen, führen Sie `ls -li` aus:

```bash
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

Das erste Feld in diesem Befehl listet die Inode-Nummer auf.

Sie können auch detaillierte Informationen über eine Datei mit `stat` anzeigen; es gibt Ihnen auch Informationen über den Inode.

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

### Wie lokalisieren Inodes Dateien?

Wir wissen, dass unsere Daten irgendwo auf der Festplatte liegen. Leider wurden sie wahrscheinlich nicht sequenziell gespeichert, daher müssen wir Inodes verwenden. Inodes zeigen auf die tatsächlichen Datenblöcke Ihrer Dateien. In einem typischen Dateisystem (nicht alle funktionieren gleich) enthält jeder Inode 15 Zeiger. Die ersten 12 Zeiger zeigen direkt auf die Datenblöcke. Der 13. Zeiger zeigt auf einen Block, der Zeiger auf weitere Blöcke enthält, der 14. Zeiger zeigt auf einen weiteren verschachtelten Block von Zeigern, und der 15. Zeiger zeigt wiederum auf einen weiteren Block von Zeigern! Verwirrend, ich weiß! Der Grund, warum dies so gemacht wird, ist, die Inode-Struktur für jeden Inode gleich zu halten, aber Dateien unterschiedlicher Größe referenzieren zu können. Wenn Sie eine kleine Datei hätten, könnten Sie sie schneller mit den ersten 12 direkten Zeigern finden; größere Dateien können mit den verschachtelten Zeigern gefunden werden. So oder so ist die Struktur des Inodes dieselbe.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis des Linux-Dateisystems und der Dateiverwaltung zu vertiefen:

1. **[Dateien und Verzeichnisse in Linux verwalten](https://labex.io/de/labs/comptia-manage-files-and-directories-in-linux-590835)** – Üben Sie das Erstellen, Entfernen, Kopieren und Verschieben von Dateien und Verzeichnissen und erkunden Sie das Erstellen von symbolischen und Hardlinks, während Sie Inodes analysieren.
2. **[Dateisystem in Linux navigieren](https://labex.io/de/labs/comptia-navigate-the-filesystem-in-linux-590971)** – Erlernen Sie die grundlegenden Fähigkeiten zur Navigation im Linux-Dateisystem mithilfe wichtiger Shell-Befehle wie `pwd`, `cd` und `ls`.
3. **[Dateien und Befehle in Linux finden](https://labex.io/de/labs/comptia-find-files-and-commands-in-linux-590834)** – Meistern Sie wesentliche Techniken zum Auffinden von Dateien und Befehlen in Linux mithilfe von `find`, `locate`, `whereis`, `which` und `type`.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Linux-Dateisystemverwaltung aufzubauen.

## Quiz Question

Wie sehen Sie, wie viele Inodes auf Ihrem System verbleiben?

## Quiz Answer

df -i
