# find

## Inhalt der Lektion

Bei all diesen Dateien verliert man leicht den Überblick und es wird schwieriger die richtige Datei zu finden. Zum Glück gibt es auch für dieses Problem ein Kommando um zu helfen, find!

<pre>$ find /home -name puppies.jpg</pre>

Mit find muss man ein Verzeichnis angeben in dem man suchen möchte. In diesem Fall suchen wir nach einer Datei namens puppies.jpg innerhalb von /home.

Man kann auch angeben ob man nach einer Datei- oder nach einem Ordnernamen sucht.

<pre>$ find /home -type d -name MyFolder</pre>

Wie man sieht ist der Typ hier mit d (directory) angegeben, find sucht jetzt nur nach Ordnernamen. Der gesuchte Ordner soll MyFolder heißen.

Das gute an find ist, dass es nicht nur innerhalb des angebenen Verzeichnisses sucht, sondern auch in allen Untervezeichnissen in diesem Verzeichnis, und in den Verzeichnissen der Unterverzeicnisse und so weiter.

## Übung

Finde eine Datei vom Root Verzeichnis ausgehend, dass das Wort net beinhaltet.

## Quizfrage

Welche Option solltest du bei find angeben wenn du nach einem Namen suchst?

## Quiz Antwort

-name
