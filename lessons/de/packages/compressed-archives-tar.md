---
lang: "de"
title: "tar und gzip"
meta_description: "Lernen Sie, tar und gzip für die Archivierung und Komprimierung von Dateien unter Linux zu verwenden. Verstehen Sie Befehle zum Erstellen, Extrahieren und Komprimieren von Dateien. Beginnen Sie mit diesem Leitfaden für Anfänger!"
meta_keywords: "tar, gzip, Linux-Archivierung, Dateikomprimierung, tar-Befehl, gzip-Befehl, Linux-Tutorial, Linux für Anfänger"
---

## Lesson Content

Bevor wir uns mit der Paketinstallation und den verschiedenen Managern befassen, müssen wir die Archivierung und Komprimierung von Dateien besprechen, da Sie diese höchstwahrscheinlich antreffen werden, wenn Sie im Internet nach Software suchen.

Sie wissen wahrscheinlich bereits, was ein Dateiarchiv ist; Sie sind höchstwahrscheinlich schon auf Dateitypen wie .rar und .zip gestoßen. Dies sind Dateiarchive; sie enthalten viele Dateien, aber sie kommen in dieser sehr praktischen einzelnen Datei, die als Archiv bekannt ist.

### Dateien mit gzip komprimieren

gzip ist ein Programm, das zum Komprimieren von Dateien unter Linux verwendet wird; diese enden mit der Erweiterung .gz.

Um eine Datei zu komprimieren:

```bash
gzip mycoolfile
```

Um die Datei zu dekomprimieren:

```bash
gunzip mycoolfile.gz
```

### Archive mit tar erstellen

Leider kann gzip nicht mehrere Dateien in einem Archiv für uns zusammenfassen. Zum Glück haben wir das tar-Programm, das dies tut. Wenn Sie ein Archiv mit tar erstellen, hat es die Erweiterung .tar.

```bash
tar cvf mytarfile.tar mycoolfile1 mycoolfile2
```

- `c` - create (erstellen)
- `v` - tell the program to be verbose and let us see what it's doing (dem Programm mitteilen, ausführlich zu sein und uns zeigen, was es tut)
- `f` - the filename of the tar file has to come after this option; if you are creating a tar file, you'll have to come up with a name (der Dateiname der tar-Datei muss nach dieser Option stehen; wenn Sie eine tar-Datei erstellen, müssen Sie sich einen Namen ausdenken)

### Archive mit tar entpacken

Um den Inhalt einer tar-Datei zu extrahieren, verwenden Sie:

```bash
tar xvf mytarfile.tar
```

- `x` - extract (extrahieren)
- `v` - tell the program to be verbose and let us see what it's doing (dem Programm mitteilen, ausführlich zu sein und uns zeigen, was es tut)
- `f` - the file you want to extract (die Datei, die Sie extrahieren möchten)

### Archive mit tar und gzip komprimieren/dekomprimieren

Oft sehen Sie eine tar-Datei, die komprimiert wurde, wie z.B.: `mycompressedarchive.tar.gz`. Alles, was Sie tun müssen, ist von außen nach innen zu arbeiten, also zuerst die Komprimierung mit `gunzip` zu entfernen und dann können Sie die tar-Datei entpacken. Oder Sie können alternativ die Option **z** mit tar verwenden, die ihm einfach sagt, dass es das gzip- oder gunzip-Dienstprogramm verwenden soll.

Eine komprimierte tar-Datei erstellen:

```bash
tar czf myfile.tar.gz
```

Dekomprimieren und entpacken:

```bash
tar xzf file.tar
```

Wenn Sie sich das merken müssen: e**X**tract all **Z**ee **F**iles! (e**X**trahiere alle **Z**-Dateien!)

tar ist einer dieser Befehle, der so wichtig ist und den man sich doch nie wirklich merkt. Relevanter xkcd: <https://xkcd.com/1168/>

### Andere Dienstprogramme

Auf Ihrer Reise mit Linux werden Sie auf andere Archiv- und Komprimierungstypen stoßen, wie z.B.: bzip2, compress, zip, unzip, etc. Sie sind etwas seltener, aber denken Sie daran, dass verschiedene Dienstprogramme unterschiedliche Befehle erfordern.

## Exercise

Machen Sie sich mit der tar-Dokumentation vertraut und sehen Sie sich die anderen verfügbaren Optionen in der Manpage an.

## Quiz Question

Welches tar-Flag wird zum Erstellen von Archiven verwendet?

## Quiz Answer

c
