---
index: 12
lang: "de"
title: "Symlinks"
meta_title: "Symlinks – Das Dateisystem"
meta_description: "Erkunden Sie Linux-Symlinks (symbolische Links) und Hardlinks. Erfahren Sie, wie Sie diese mit dem ln-Befehl erstellen, die Link-Anzahl in Linux mit ls überprüfen und den Unterschied verstehen, wenn Sie die Ausgabe von Symlinks und Hardlinks anzeigen."
meta_keywords: "Linux Symlinks, Hardlinks, ln Befehl, symbolische Links, ls Symlink, Link-Anzahl in Linux, ls Symlinks, ls Links, Linux Dateisystem, Linux Tutorial"
---

## Lesson Content

Wenn Sie Dateien im Detail auflisten, sehen Sie viele Informationen. Betrachten wir ein früheres Beispiel von Inode-Informationen aus dem Befehl `ls -li`:

```plaintext
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

Wir sind zuvor über das dritte Feld in dieser Ausgabe hinweggegangen. Dieses Feld ist die Link-Anzahl.

### Die Link-Anzahl in Linux

Die **Link-Anzahl in Linux** ist die Gesamtzahl der Hardlinks, die eine Datei besitzt. Um zu verstehen, was das bedeutet, müssen wir zuerst besprechen, was Links sind. In Linux gibt es zwei Arten von Links: symbolische Links (Symlinks) und Hardlinks.

### Symlinks verstehen

Im Windows-Betriebssystem gibt es Verknüpfungen (Shortcuts), die im Wesentlichen Aliase sind, die auf andere Dateien zeigen. In Linux ist das Äquivalent ein symbolischer Link, auch bekannt als Softlink oder **Symlink**. Ein Symlink ist ein spezieller Dateityp, der über seinen Namen auf eine andere Datei oder ein anderes Verzeichnis zeigt.

Sehen wir uns das in der Praxis an. Wir erstellen einige Dateien und dann einen Symlink.

```bash
pete@icebox:~/Desktop$ echo 'myfile' > myfile
pete@icebox:~/Desktop$ echo 'myfile2' > myfile2
pete@icebox:~/Desktop$ echo 'myfile3' > myfile3

pete@icebox:~/Desktop$ ln -s myfile myfilelink
pete@icebox:~/Desktop$ ls -li
total 12
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
```

Hier haben wir einen symbolischen Link namens `myfilelink` erstellt, der auf `myfile` zeigt. Wenn Sie `ls` verwenden, um einen `ls symlink` anzuzeigen, wird er durch das `l` am Anfang der Berechtigungszeichenfolge und das `->`-Symbol, das auf das Ziel zeigt, deutlich gekennzeichnet. Beachten Sie, dass der Symlink seine eigene eindeutige Inode-Nummer (93403) hat. Da Symlinks auf Dateinamen und nicht auf Inodes zeigen, können sie verschiedene Dateisysteme überspannen.

### Hardlinks verstehen

Die andere Art von Link ist ein Hardlink. Ein Hardlink erstellt einen weiteren Dateieintrag, der direkt auf denselben Inode wie die Originaldatei zeigt.

Erstellen wir einen Hardlink für `myfile2`:

```bash
pete@icebox:~/Desktop$ ln myfile2 myhardlink
pete@icebox:~/Desktop$ ls -li
total 16
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myhardlink
```

Beachten Sie, dass `myhardlink` exakt dieselbe Inode-Nummer (93401) wie `myfile2` teilt. Auch die Link-Anzahl für beide Dateien ist auf 2 gestiegen. Das liegt daran, dass nun zwei Dateieinträge auf denselben Inode zeigen. Wenn Sie den Inhalt von `myfile2` ändern, werden die Änderungen in `myhardlink` widergespiegelt, und umgekehrt. Wenn Sie `myfile2` löschen, sind die Daten der Datei immer noch über `myhardlink` zugänglich. Der Inode und seine Daten werden erst dann von der Festplatte entfernt, wenn die Link-Anzahl auf Null sinkt. Da Hardlinks auf Inodes zeigen, die innerhalb eines einzigen Dateisystems eindeutig sind, können sie keine verschiedenen Dateisysteme überspannen.

### Erstellen von Symlinks und Hardlinks

You können beide Arten von Links mit dem Befehl `ln` erstellen. Die Syntax ist unkompliziert.

Um einen symbolischen Link zu erstellen, verwenden Sie das Flag `-s`:

```bash
ln -s /pfad/zum/original /pfad/zum/link
```

Um einen Hardlink zu erstellen, lassen Sie das Flag `-s` weg:

```bash
ln /pfad/zum/original /pfad/zum/link
```

Die Verwendung der Befehle `ls symlinks` oder allgemeiner `ls links` mit der Option `-l` ist für die Verwaltung und Identifizierung dieser verschiedenen Dateitypen unerlässlich.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Dateiverwaltung, Links und Inodes zu festigen:

1.  **[Dateien und Verzeichnisse unter Linux verwalten](https://labex.io/de/labs/comptia-manage-files-and-directories-in-linux-590835)** – Üben Sie das Erstellen, Kopieren, Verschieben und Entfernen von Dateien und Verzeichnissen und lernen Sie speziell symbolische und Hardlinks kennen und wie man Inodes analysiert.
2.  **[Im Dateisystem unter Linux navigieren](https://labex.io/de/labs/comptia-navigate-the-filesystem-in-linux-590971)** – Meistern Sie wesentliche Befehle wie `pwd`, `cd` und `ls`, um sich effizient durch das Linux-Dateisystem zu bewegen, eine grundlegende Fähigkeit, um zu verstehen, wo sich Dateien und ihre Inodes befinden.

Diese Labs helfen Ihnen, die Konzepte der Dateiverwaltung und Links in realen Szenarien anzuwenden und Vertrauen in das Linux-Dateisystem aufzubauen.

## Quiz Question

Was ist der Befehl und seine primäre Option, die zum Erstellen eines Symlinks verwendet werden? Ihre Antwort muss auf Englisch sein und ist groß-/kleingeschrieben. Bitte fügen Sie das Leerzeichen zwischen dem Befehl und der Option ein.

## Quiz Answer

ln -s
