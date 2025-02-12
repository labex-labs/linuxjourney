# ls (List Directories)

## Inhalt der Lektion

Nachdem wir jetzt wissen wie wir uns im Verzeichnisbaum bewegen, stellt sich die Frage wie wir herausfinden welche Verzeichnisse und Dateien es überhaupt gibt. Bis jetzt bewegten wir uns völlig im dunkeln. Aber es gibt Abhilfe, mit dem ls Kommando zum auflisten von Verzeichnisinhalten. Das ls Kommando listet standardmäßig Ordner und Dateien auf die sich im aktuellen Verzeichnis befinden, man kann aber auch einen Pfad angeben für den man eine Liste haben möchte.

<pre>$ ls
$ ls /home/pete</pre>

ls ist ein sehr nützliches Werkzeug, es zeigt nicht nur die Dateien und Ornder selbst an, sondern gibt auch detailierte Informationen über sie preis.

Merke dir ebenfalls, dass nicht alle Dateien und Ordner sichtbar sind. Dateinamen die mit einem . beginnen werden standardmäßig ausgeblendet, sie können mit dem -a Parameter angezeigt werden (a steht für alle).

<pre>$ ls -a</pre>

Es gibt einen weiteren nützlichen Parameter, -l für lang, er bringt die oben erwähnten detailierten Informationen zum vorschein. In diesem langen Format wird folgendes mit angezeigt (von links): Dateiberechtigungen, Anzahl der Links, Dateibesitzer, Eigentümer Gruppe, Dateigröße, Zeitpunkt der letzten Modifikation, Datei-/Ordnername.

<pre>$ ls -l</pre>

<pre>pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46 Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13 Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41 Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41 Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41 Videos</pre>

Shell-Kommandos haben meist Optionen (auch Argumente oder Flags genannt) für mehr Funktionen. In unserem Beispiel haben wir -a und -l kennengelern, man kann diese Optionen aber auch kombinieren z.B. -la. Die Reihenfolge der Optionen spielt meistens keine Rolle, ls -al funtkioniert genauso wie ls -la.

<pre>$ ls -la</pre>

## Übung

Führe ls mit unterschiedlichen Optionen aus und vergleiche die Ausgabe.

Tipp: `ls --help` zeigt dir weitere optionen an.

## Quizfrage

Mit welchem Befehl zeigt man versteckte dateien an?

## Quiz Antwort

ls -a
