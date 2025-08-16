---
lang: "de"
title: "Symlinks"
description: "Erfahren Sie mehr über Linux-Symlinks und Hardlinks, einschließlich deren Erstellung und Verwaltung. Verstehen Sie ihre Unterschiede und Anwendungsfälle mit diesem anfängerfreundlichen Leitfaden."
keywords: "Linux Symlinks, Hardlinks, ln Befehl, symbolische Links, Linux Dateisystem, Linux Tutorial, Linux für Anfänger"
---

## Lesson Content

Betrachten wir ein früheres Beispiel für Inode-Informationen:

```plaintext
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

Es ist Ihnen vielleicht aufgefallen, dass wir das dritte Feld im `ls`-Befehl bisher übergangen haben; dieses Feld ist die Link-Anzahl. Die Link-Anzahl ist die Gesamtzahl der Hardlinks, die eine Datei hat. Nun, das sagt Ihnen im Moment noch nichts, also lassen Sie uns zuerst über Links sprechen.

### Symlinks

Im Windows-Betriebssystem gibt es sogenannte Verknüpfungen (shortcuts). Verknüpfungen sind lediglich Aliase zu anderen Dateien. Wenn Sie etwas mit der Originaldatei tun, könnten Sie die Verknüpfung möglicherweise beschädigen. In Linux sind die Entsprechungen von Verknüpfungen symbolische Links (oder Soft Links oder Symlinks). Symlinks ermöglichen es uns, auf eine andere Datei über ihren Dateinamen zu verlinken. Eine andere Art von Links, die in Linux zu finden ist, sind Hardlinks; dies sind tatsächlich andere Dateien mit einem Link zu einem Inode. Lassen Sie uns sehen, was ich in der Praxis meine, beginnend mit Symlinks.

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

Sie können sehen, dass ich einen symbolischen Link namens `myfilelink` erstellt habe, der auf `myfile` zeigt. Symbolische Links werden durch `->` gekennzeichnet. Beachten Sie jedoch, dass ich eine neue Inode-Nummer erhalten habe; Symlinks sind nur Dateien, die auf Dateinamen zeigen. Wenn Sie einen Symlink ändern, wird auch die Datei geändert. Inode-Nummern sind für Dateisysteme einzigartig; Sie können nicht zwei gleiche Inode-Nummern in einem einzigen Dateisystem haben, was bedeutet, dass Sie eine Datei in einem anderen Dateisystem nicht über ihre Inode-Nummer referenzieren können. Wenn Sie jedoch Symlinks verwenden, verwenden diese keine Inode-Nummern; sie verwenden Dateinamen, sodass sie über verschiedene Dateisysteme hinweg referenziert werden können.

### Hardlinks

Sehen wir uns ein Beispiel für einen Hardlink an:

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

Ein Hardlink erstellt einfach eine weitere Datei mit einem Link zum selben Inode. Wenn ich also den Inhalt von `myfile2` oder `myhardlink` ändern würde, wäre die Änderung auf beiden sichtbar. Aber wenn ich `myfile2` löschen würde, wäre die Datei immer noch über `myhardlink` zugänglich. Hier kommt unsere Link-Anzahl im `ls`-Befehl ins Spiel. Die Link-Anzahl ist die Anzahl der Hardlinks, die ein Inode hat. Wenn Sie eine Datei entfernen, verringert sich diese Link-Anzahl. Der Inode wird erst gelöscht, wenn alle Hardlinks zum Inode gelöscht wurden. Wenn Sie eine Datei erstellen, ist ihre Link-Anzahl 1, da sie die einzige Datei ist, die auf diesen Inode zeigt. Im Gegensatz zu Symlinks erstrecken sich Hardlinks nicht über Dateisysteme, da Inodes für das Dateisystem einzigartig sind.

### Creating a symlink

```bash
ln -s myfile mylink
```

Um einen symbolischen Link zu erstellen, verwenden Sie den Befehl `ln` mit `-s` für symbolisch, und Sie geben eine Zieldatei und dann einen Linknamen an.

### Creating a hardlink

```bash
ln somefile somelink
```

Ähnlich wie bei der Erstellung eines Symlinks, nur dass Sie diesmal das `-s` weglassen.

## Exercise

Spielen Sie mit der Erstellung von Symlinks und Hardlinks. Löschen Sie ein paar und sehen Sie, was passiert.

## Quiz Question

Welcher Befehl wird verwendet, um einen Symlink zu erstellen?

## Quiz Answer

ln -s
