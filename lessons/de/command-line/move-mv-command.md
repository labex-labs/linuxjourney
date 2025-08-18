---
lang: "de"
title: "mv (Verschieben)"
meta_description: "Lernen Sie, wie Sie den Linux-Befehl mv zum Verschieben und Umbenennen von Dateien/Verzeichnissen verwenden. Verstehen Sie seine Optionen und verhindern Sie Überschreibungen. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "mv Befehl, Linux mv, Dateien verschieben Linux, Dateien umbenennen Linux, Linux Tutorial, Anfänger, Linux Anleitung"
---

## Lesson Content

Wird zum Verschieben von Dateien und auch zum Umbenennen verwendet. Ziemlich ähnlich dem `cp`-Befehl in Bezug auf Flags und Funktionalität.

Sie können Dateien wie folgt umbenennen:

```bash
mv oldfile newfile
```

Oder Sie können eine Datei tatsächlich in ein anderes Verzeichnis verschieben:

```bash
mv file2 /home/pete/Documents
```

Und mehr als eine Datei verschieben:

```bash
mv file_1 file_2 /somedirectory
```

Sie können auch Verzeichnisse umbenennen:

```bash
mv directory1 directory2
```

Wie `cp`, wenn Sie eine Datei oder ein Verzeichnis `mv`en, wird alles im selben Verzeichnis überschrieben. Sie können also das Flag `-i` verwenden, um vor dem Überschreiben eine Bestätigung anzufordern.

```bash
mv -i directory1 directory2
```

Angenommen, Sie wollten eine Datei `mv`en, um die vorherige zu überschreiben. Sie können auch ein Backup dieser Datei erstellen, und die alte Version wird einfach mit einem `~` umbenannt.

```bash
mv -b directory1 directory2
```

## Exercise

Benennen Sie eine Datei um und verschieben Sie diese Datei dann in ein anderes Verzeichnis.

## Quiz Question

Wie benennt man eine Datei namens `cat` in `dog` um?

## Quiz Answer

mv cat dog
