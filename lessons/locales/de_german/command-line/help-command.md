# help

## Inhalt der Lektion

Linux hat einige gut Möglichkeiten mit an Bord, um Hilfe zu Kommandos zu bekommen und zu sehen was diese an Argumenten und Optionen untersützten. Eine Möglichkeit ist help, ein in Bash integriertes Kommando das Hilfe für andere Bash Kommandos anzeigt (echo, logout, pwd, etc).

<pre>$ help echo</pre>

Das gibt eine Beschreibung und die Optionen aus, welche man für echo Benutzen kann. Für andere ausführbare Programme ist es Konvention eine --help Option zu haben (manchmal auch nur -h oder ähnlich).

<pre>$ ls --help</pre>

Nich alle Entwickler statten ihre Programme mit einer --help Option aus, es ist aber die beste Möglichkeit um schnell eine Kurzhilfe für das Kommando zu bekommen.

## Übung

Benutze help mit dem echo, dem logout und dem pwd Kommando.

## Quizfrage

Wie bekommst du schnelle Kommandozeilenhilfe für integrierte Bash Kommandos?

## Quiz Antwort

help
