---
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

- Dateityp - reguläre Datei, Verzeichnis, Zeichendatei usw.
- Eigentümer
- Gruppe
- Zugriffsrechte
- Zeitstempel - mtime (Zeit der letzten Dateimodifikation), ctime (Zeit der letzten Attributänderung), atime (Zeit des letzten Zugriffs)
- Anzahl der Hardlinks zur Datei
- Größe der Datei
- Anzahl der der Datei zugewiesenen Blöcke
- Zeiger auf die Datenblöcke der Datei - am wichtigsten!

Im Grunde speichern Inodes alles über die Datei, außer dem Dateinamen und der Datei selbst!

### Wann werden Inodes erstellt?

Wenn ein Dateisystem erstellt wird, wird auch Speicherplatz für Inodes zugewiesen. Algorithmen bestimmen, wie viel Inode-Speicherplatz Sie benötigen, abhängig vom Volumen der Festplatte und mehr. Sie haben wahrscheinlich irgendwann in Ihrem Leben Fehlermeldungen wegen Speichermangels gesehen. Dasselbe kann auch bei Inodes auftreten (obwohl seltener); Ihnen können die Inodes ausgehen, und Sie können daher keine weiteren Dateien erstellen. Denken Sie daran, dass die Datenspeicherung sowohl von den Daten als auch von der Datenbank (Inodes) abhängt.

Um zu sehen, wie viele Inodes auf Ihrem System übrig sind, verwenden Sie den Befehl `df -i`.

### Inode-Informationen

Inodes werden durch Nummern identifiziert. Wenn eine Datei erstellt wird, wird ihr eine Inode-Nummer zugewiesen, und die Nummer wird in sequenzieller Reihenfolge zugewiesen. Es kann jedoch manchmal vorkommen, dass Sie beim Erstellen einer neuen Datei feststellen, dass sie eine Inode-Nummer erhält, die niedriger ist als andere. Dies liegt daran, dass gelöschte Inodes von anderen Dateien wiederverwendet werden können. Um Inode-Nummern anzuzeigen, führen Sie `ls -li` aus:

```bash
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

Das erste Feld in diesem Befehl listet die Inode-Nummer auf.

Sie können auch detaillierte Informationen zu einer Datei mit `stat` anzeigen; es gibt Ihnen auch Informationen über den Inode.

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

Wir wissen, dass unsere Daten irgendwo auf der Festplatte liegen. Leider wurden sie wahrscheinlich nicht sequenziell gespeichert, daher müssen wir Inodes verwenden. Inodes zeigen auf die tatsächlichen Datenblöcke Ihrer Dateien. In einem typischen Dateisystem (nicht alle funktionieren gleich) enthält jeder Inode 15 Zeiger. Die ersten 12 Zeiger zeigen direkt auf die Datenblöcke. Der 13. Zeiger zeigt auf einen Block, der Zeiger auf weitere Blöcke enthält, der 14. Zeiger zeigt auf einen weiteren verschachtelten Block von Zeigern, und der 15. Zeiger zeigt wiederum auf einen weiteren Block von Zeigern! Verwirrend, ich weiß! Der Grund, warum dies so gemacht wird, ist, die Inode-Struktur für jeden Inode gleich zu halten, aber Dateien unterschiedlicher Größe referenzieren zu können. Wenn Sie eine kleine Datei hätten, könnten Sie sie mit den ersten 12 direkten Zeigern schneller finden; größere Dateien können mit den verschachtelten Zeigern gefunden werden. So oder so ist die Struktur des Inodes dieselbe.

## Exercise

Beobachten Sie einige Inode-Nummern für verschiedene Dateien. Welche werden normalerweise zuerst erstellt?

## Quiz Question

Wie sehen Sie, wie viele Inodes auf Ihrem System übrig sind?

## Quiz Answer

df -i
