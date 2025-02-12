# cp (Copy)

## Inhalt der Lektion

Lass uns ein paar Kopien von Dateien anlegen. So wie man per Kopieren und Einfügen Dateien mit grafischen Programmen kopieren kann, gibt es auch in der Shell eine Möglichkeit dies zu tun.

<pre>$ cp mycoolfile /home/pete/Documents/cooldocs</pre>

mycoolfile ist hier die Datei die man kopieren möchte und /home/pete/Documents/cooldocs ist das Ziel an das der Inhalt kopiert werden soll.

Man kann mehrere Dateien und Ordner auf einmal kopieren, oder Platzhalter verwenden. Ein Platzhalterzeichen ist ein Zeichen dass bei der Suche für andere Zeichen stehen kann und somit erlaubt nach bestimmten Mustern zu suchen. Man kann Platzhalter in jedem Kommando verwenden um Pfade flexibler anzugeben.

<ul>
<li>* Dieser Platzhalter seht für jede Anzahl an beliebigen Zeichen.</li>
<li>? Steht für genau ein Zeichen (Buchstaben oder Zahlen)</li>
<li>[] Dieser Platzhalter kann für alle Zeichen die in den Klammer angegeben werden stehen.</li>
</ul>

<pre>$ cp *.jpg /home/pete/Bilder</pre>

Dieser Befehl kopiert alle Dateien mit der Endung .jpg im aktuellen Verzeichnis in das Bilderverzeichnis.

Ein nützlicher Parameter von cp ist der -r Parameter. Er erlaubt das rekursive Kopieren, also das Kopieren aller Dateien und Ordner innerhalb eines Ordners.

Versuche einen Ordner, der ein paar Dateien enthält, in deinen Dokumentenordner zu kopieren. Hat es nicht funktioniert? Das ist weil du die Dateien innerhalb des Ordners mitkopieren musst, daher klappt es nur mit dem -r Argument.

<pre>$ cp -r Pumpkin/ /home/pete/Documents</pre>

Eine Sache die man wissen sollte: Wenn du eine Datei in einen Ordner kopierst, indem es schon eine Datei mit diesem Namen gibt, wird diese Datei überschrieben. Das ist natürlich blöd wenn du den Inhalt der alten Datei noch brauchst. Um diesem Versehen vorzubeugen gibt es das -i Argument (interaktiv). cp -i fragt dich also bevor es eine Datei überschreibt.

<pre>$ cp -i mycoolfile /home/pete/Pictures</pre>

## Übung

Kopiere einige Dateien hin- und her. Sei vorsichtig, dass du nichts wichtiges überschreibst.

## Quizfrage

Welchen Parameter brauchst du um einen Ordner zu kopieren?

## Quiz Antwort

-r
