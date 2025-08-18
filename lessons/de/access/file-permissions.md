---
lang: "de"
title: "Dateiberechtigungen"
meta_title: "Dateiberechtigungen - Berechtigungen"
meta_description: "Lernen Sie Linux-Dateiberechtigungen: Verstehen Sie rwx-Bits, Benutzer-, Gruppen- und andere Berechtigungen. Meistern Sie die `ls -l`-Ausgabe für Anfänger. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "Linux-Dateiberechtigungen, ls -l Befehl, rwx Berechtigungen, Linux-Tutorial, Dateimodi, Linux für Anfänger, Linux-Anleitung"
---

## Lesson Content

Wie wir bereits gelernt haben, haben Dateien unterschiedliche Berechtigungen oder Dateimodi. Schauen wir uns ein Beispiel an:

```bash
$ ls -l Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 .
```

Die Berechtigungen einer Datei bestehen aus vier Teilen. Der erste Teil ist der Dateityp, der durch das erste Zeichen in den Berechtigungen angezeigt wird. In unserem Fall, da wir ein Verzeichnis betrachten, zeigt es **d** für den Dateityp an. Am häufigsten sehen Sie ein **-** für eine reguläre Datei.

Die nächsten drei Teile des Dateimodus sind die eigentlichen Berechtigungen. Die Berechtigungen sind in jeweils 3 Bits gruppiert. Die ersten 3 Bits sind Benutzerberechtigungen, dann Gruppenberechtigungen und dann andere Berechtigungen. Ich habe die Pipe hinzugefügt, um die Unterscheidung zu erleichtern.

```plaintext
d | rwx | r-x | r-x
```

Jedes Zeichen repräsentiert eine andere Berechtigung:

- r: lesbar
- w: schreibbar
- x: ausführbar (im Grunde ein ausführbares Programm)
- -: leer

Im obigen Beispiel sehen wir also, dass der Benutzer pete Lese-, Schreib- und Ausführungsberechtigungen für die Datei hat. Die Gruppe penguins hat Lese- und Ausführungsberechtigungen. Und schließlich haben die anderen Benutzer (alle anderen) Lese- und Ausführungsberechtigungen.

## Exercise

Verwenden Sie den Befehl `ls -l` für mehrere Dateien und nennen Sie deren Berechtigungen, Benutzer und Gruppe.

## Quiz Question

Welches Berechtigungsbit wird für ausführbar verwendet?

## Quiz Answer

x
