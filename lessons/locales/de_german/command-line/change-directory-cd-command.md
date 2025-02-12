# cd (Change Directory)

## Inhalt der Lektion

Nachdem du jetzt weißt wo du dich im System befindest, lass uns herausfinden wie wir uns im Dateisystem herumbewegen können. Wie du dich erinnerst, brauchen wir dazu eine Pfadangabe. Es gibt zwei Möglichkeiten einen Pfad anzugeben, absolut oder relativ.

<ul>
<li>Absoluter Pfad: Dies ist eine Pfadangabe beginnend beim Wurzelverzeichnis. Das Wurzel- oder Root-Verzeichnis wird meist als Schrägstrich dargestellt. Jedesmal wenn ein Pfad mit / beginnt heißt es er beginnt beim Root-Verzeichnis und ist damit absolut. Z.B. /home/pete/Desktop</li>

<li>Relativer Pfad: Hier wir der Pfad relativ zum gegenwärigen Ort im Dateisystem angegeben. Wenn man sich also bereits im Verzeichnis /home/pete befindet reicht es den Pfad Desktop/ anzugeben um in den Desktop Ordner zu gelangen und man muss nicht den kompletten Pfad /home/pete/Desktop benutzen.</li>
</ul>

Jetzt wo du weißt wie Pfade funktionieren, brauchen wir lediglich noch etwas, dass uns dabei hilft in das gewünschte Verzeichnisse zu wechseln. Glücklicherweise gibt es dafür das cd (change directory) Kommando, dass das für uns erledigt.

<pre>$ cd /home/pete/Bilder</pre>

Damit wechselt man ins Verzeichnis mit dem Pfad /home/pete/Bilder.

In diesem Verzeichnis habe ich einen Ordner namens Hawaii, in diesen kann ich mit diesem Befehl hineinwechseln:

<pre>$ cd Hawaii</pre>

Wie du siehst habe ich lediglich den Ordnernamen benutzt, da ich mich bereits in /home/pete/Bilder befand.

Es kann recht ermüdend sein, ständig mit absoluten und relativen Pfaden zu navigieren, zum Glück gibt es ein paar Abkürzungen um es ein wenig einfacher zu machen Pfade zu schreiben.

<ul>
<li>. (aktuelles Verzeichnis). Dies verweist auf das Verzeichnis in dem du gerade bist. </li>
<li>.. (übergeordnetes Verzeichnis). Verweist auf das übergeordnete Verzeichnis (Elternverzeichnis).</li>
<li>~ (home Vorzeichnis). Verweist auf das "home directory" (Heimatverzeichnis des Benutzters). Z.B. /home/pete.</li>
<li>- (vorheriges Verzeichnis). Verweist auf das zuletzt besuchte Verzeichnis, zum Zurückspringen.</li>
</ul>

<pre>$ cd .
$ cd ..
$ cd ~
$ cd -
</pre>
Probiere es einfach aus!

## Übung

Führe das cd Kommando ohne irgendwelche Argumente (Pfadangaben) aus, wo landest du?

## Quizfrage

Wenn du dich in /home/pete/Bilder befindest was ist eine gute Abkürzung um ins Verzeichnis /home/pete zu wechseln?

## Quiz Answer

cd ..
