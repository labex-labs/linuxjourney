# rm (Remove)

## Inhalt der Lektion

Ich denke inzwischen haben wir zu viele Dateien. Lass uns ein paar davon löschen. Um Dateien zu löschen benutzt man das rm Kommando. Es wird werwendet um Dateien und Ordner zu löschen.

<pre>$ rm datei_1</pre>

Sei vorsichtig wenn du rm benutzt. Hier gibt es keinen magischen Papierkorb, aus dem du gelöschte Dateien herausfischen kannst. Einmal gelöscht sind Dateien für immer verloren, überlege also bevor du Enter drückst!

Glücklicherweise gibt es ein paar Sicherheitsmechanismen, so dass man zumindest nicht alle wichtigen Dateien auf einmal löschen kann. Schreibgeschützte Dateien und Ordner etwa müssen beim löschen quitiert werden.

Wenn man sich darum nicht kümmern möchte gibt es die -f Option, um auch diese Dateien ohne Nachfrage zu löschen.

<pre>$ rm -f datei_geschützt</pre>

Die -f (force) Option löscht alle angegebenen Dateien ohne Nachfrage, es sei denn man hat nicht die nötigen Datei-Berechtigungen.

<pre>$ rm -i datei</pre>

Wie bei vielen anderen Kommandos führt die -i Option dazu, dass vor dem löschen von Dateien noch einmal nachgefragt wird.

<pre>$ rm -r ordner</pre>

Ordner lassen sich nicht ohne die -r Option entfernen. Wie bei cp steht das -r hier für rekursiv. Es führt dazu, dass man Verzeichnisse mitsamt ihren Unterverzeichnisen und Dateien löschen kann.

Ein Ordner lässt sich alternativ mit dem rmdir Kommando löschen.

<pre>$ rmdir ordner</pre>

## Übung

<ol>
<li>Lege eine Datei namens -file an (vergesse nicht den Bindestrich!).</li>
<li>Lösche diese Datei.</li>
</ol>

## Quizfrage

Wie entfernt man eine Datei namens myfile?

## Quiz Antwort

rm myfile
