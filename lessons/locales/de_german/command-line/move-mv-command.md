# mv (Move)

## Inhalt der Lektion

Das mv Kommando wird zum verschieben und umbenennen von Dateien und Ordnern benutzt. Es ist sehr ähnlich zum cp Kommando hinsichtlich seiner Argumente und seiner Benutzung.

So kannst du Dateien umbenennen:

<pre>$ mv alte_datei neue_datei</pre>

Du kannst eine Datei auch in ein anderes Verzeichnis verschieben:

<pre>$ mv file2 /home/pete/Documents</pre>

Das geht auch mit mehreren Dateien:

<pre>$ mv datei_1 datei_2 /ein_ordner</pre>

Du kannst auch Ordner umbenennen:

<pre>$ mv ordner_1 ordner_2</pre>

Wie cp wird auch mv alles überschreiben dass schon unter gleichem Namen existiert. Aber auch hier gibt es die -i Option, die dich vor dem Überschreiben warnt.

<pre>mv -i datei_1 datei_2</pre>

Wenn du zwar eine Datei mit einer neuen Datei überschreiben möchtest, aber noch ein Backup dieser brauchst geht das mit dem -b Argument. Das sichert den Inhalt bevor die Datei überschrieben wird indem es der Datei ein ~ anhängt.

<pre>$ mv -b datei_1 datei_2</pre>

Das überschreibt datei_2 mit Inhalt aus datei_1 sichert aber die ursprüngliche datei_2 als datei_2~.

## Übung

Ändere den Namen einer Datei und verchiebe sie dann in ein anderes Verzeichnis.

## Quizfrage

Wie nennt man eine Datei namens cat in dog um?

## Quiz Antwort

mv cat dog
