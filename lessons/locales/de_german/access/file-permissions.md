# Datei Berechtigungen

## Inhalt der Lektion

Wie wir zuvor gelernt haben, haben Dateien unterschiedliche Berechtigungen oder Datei Modi. Schauen wir uns ein Beispiel an:

<pre>$ ls -l Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 .
</pre>

Die Dateiberechtigungen setzen sich aus vier Teilen zusammen. Der erste Buchstabe steht für den Dateityp. Im Beispiel sehen wir einen Ordner daher steht hier <b>d</b> für directory (engl. für Verzeichnis/Ordner). In den meisten Fällen sieht man an dieser Stelle ein <b>-</b> was für eine reguläre Datei steht.

Die nächten dei Teile des Datei Modus sind die eigentlichen Berechtigungen. Die Berechtigungen sind jeweils in 3 Buchstaben gruppiert. Die ersten 3 Buchstaben sind die Berechtiungen für den Dateieigentümer. Darauf folgen die Berechtigungen für die Benutzeruppe der die Datei gehört und am Schluss die Berechtigung die für Benutzer gilt die weder Eigentümer sind noch der Gruppe angehören.

Hier nochmal die Zeichenkette in ihren Bestandteilen (getrennt durch |):

<pre>d | rwx | r-x | r-x </pre>

Jeder Bucstabe steht für eine andere Berechtigung:
<ul>
<li>r: readable (lesbar)</li>
<li>w: writable (schreibbar)</li>
<li>x: executable (ausführbar als Programm)</li>
<li>-: berechtigung nicht gesetzt</li>
</ul>

Im obigen Beispiel sehen wir dass der Benutzer pete die Datei lesen, schreiben und ausführen darf. Die Gruppe penguins
darf die Datei lesen und ausführen. Alles anderen Benutzer haben ebenfalls Lese- und Ausführberechtigungen.

## Übung

Benutze dass Kommando ls -l um die Berechtiungen, Benutzer und Gruppen mehrerer Dateien aufzulisten.

## Quizfrage

Welche Buchstabe steht für die Berechtiung zum Ausführen einer Datei (executable)?

## Quiz Antwort

x
