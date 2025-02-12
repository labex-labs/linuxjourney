# history

## Inhalt der Lektion

In deiner Shell wird ein Verlauf (history) deiner Befehle, die du bereits ausgeführt hast, geführt. Man kann sich diesen Verlauf anschauen. Das ist sehr nützlich um einen bereits benutzten Befehl nich noch einmal tippen zu müssen.

<pre>$ history</pre>

Willst du einen Befehl noch einmal ausführen drücke einfach die Pfeiltaste nach oben um durch den Verlauf zu blättern, gehst du weiter zurück als gewollt, kannst mit der Pfeiltaste nach unten wieder Richtung Gegenwart zurückblättern.

Um lediglich den letzten Befehl noch einmal auszuführen kanst du auch !! benutzen. Wenn du z.B. cat file1 ausgeführt hast und es noch einmal ausführen möchtest, tippe lediglich !! drücke Enter und der Befehl wird noch einmal ausgeführt.

Ein weiterer Trick ist das drücken von Strg. + R, das öffnet die sog. reverse Suche. Hier kannst du nach Befehlen in deinem Verlauf suchen. Tippe einfach den Anfang eines früheren Befehls und die Suche findet den Rest. Du kannst durch die passenden Treffer navigieren indem du wiedeholt Strg. + R drückst. Ist der richtige Befehl gefunden muss man nur noch Enter drücken um ihn direkt auszuführen.

Wenn dir dein Terminalfenster mit der Zeit zu voll geworden ist, kannst du es einfach mit dem clear Kommando bereinigen.

<pre>$ clear</pre>

Alles wieder schön leer. Ctr. + L hat übrigens die gleiche Wirkung wie clear.

Wenn wir gerade über nützliche Dinge reden. Eine der nützlichsten Funktionen jeder Linux Kommandozeilen Umgebung ist die Tab-Vervollständigung.
Wenn du beginnst ein Kommando oder einen Pfad zu tippen, kannst du einfach die Tab-Taste drücken um passende Kommandos oder Pfade zu vervollständigen, so lange es nicht mehrere Möglichkeiten gibt die mit dieser Zeichenkette beginnen. Ist dies der Fall reicht es meist ein paar weitere Zeichen einzugeben und es noch einmal zu versuchen. Alternativ kannst du Tab auch noch einmal drücken um die Auswahlmöglichkeiten die noch bestehen anzuzeigen.
Wenn du also z.B. Firefox öffnen möchtest, schreibe einfach fir und drücke Tab und das Kommando wird auf firefox erweitert. Tippst du hingegen nur fi wird das nicht direkt klappen, da es noch weitere Kommandos gibt die mit fi beginnen. Drücke Tab noch einmal um diese anzuzeigen.

## Übung

Navigiere durch deinen Befehlsverlauf durch drücken deiner Pfeiltasten ↑ und ↓. Spiele ein bisschen mit der Strg. + R reverse Suche.

## Quizfrage

Wie lautet das Kommando zum Bereinigen des Terminalfensters

## Quiz Antwort

clear
