# alias

## Inhalt der Lektion

Manchmal ist das wiederholte Schreiben von Kommandos sehr nervig oder umständlich. Vor allem für lange Befehle die man häufig benutzt lohnt sich da ein Alias. Um so einen Alias anzulegen denkt man sich einfach einen namen für den Alias aus (der idealerweise noch nicht von einem anderen Programm in Verwendung ist) und hinterlegt den Befehl der unter diesem Alias ausgeführt werdem soll.

<pre>$ alias la='ls -la'</pre>

Jetzt kann man statt ls -la einfach la eingeben und es wird ls -la ausgeführt. Das ist eine sehr praktische Funktion. Damit diese Einstellung allerdings einen Neustart überlebt, muss man diesen Alias in der Datei

<pre>~/.bashrc</pre>

oder ähnlichen Dateien hinterlegen. Damit ist er dann auch nach einem Neustart verfügbar.

Um Aliase wieder aufzuheben gibt es das unalias Kommando:

<pre>$ unalias la</pre>


## Übung

Erstelle ein paar Aliase und entferne sie wieder.

## Quizfrage

Welches Kommando wird benutzt um Aliase anzulegen?

## Quiz Antwort

alias
