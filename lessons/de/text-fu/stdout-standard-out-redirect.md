---
lang: "de"
title: "stdout (Standardausgabe)"
meta_title: "stdout (Standardausgabe) - Text-Fu"
meta_description: "Erfahren Sie mehr über Linux stdout und I/O-Umleitung. Verstehen Sie, wie Sie die Befehlsausgabe mit den Operatoren > und >> in Dateien umleiten. Beginnen Sie Ihre Linux-Reise noch heute!"
meta_keywords: "Linux stdout, I/O-Umleitung, Linux-Befehle, Ausgabe umleiten, Linux-Tutorial, Linux für Anfänger, Linux-Anleitung, Shell-Skripting"
---

## Lesson Content

Inzwischen sind wir mit vielen Befehlen und deren Ausgabe vertraut, und das bringt uns zu unserem nächsten Thema: I/O (Input/Output) Streams. Lassen Sie uns den folgenden Befehl ausführen, und wir werden besprechen, wie das funktioniert.

```bash
echo Hello World > peanuts.txt
```

Was ist gerade passiert? Nun, überprüfen Sie das Verzeichnis, in dem Sie diesen Befehl ausgeführt haben, und siehe da, Sie sollten eine Datei namens `peanuts.txt` sehen. Schauen Sie in diese Datei, und Sie sollten den Text "Hello World" sehen. Viele Dinge sind gerade in einem Befehl passiert, also lassen Sie uns das aufschlüsseln.

Zuerst zerlegen wir den ersten Teil:

```bash
echo Hello World
```

Wir wissen, dass dies "Hello World" auf den Bildschirm ausgibt, aber wie? Prozesse verwenden I/O-Streams, um Eingaben zu empfangen und Ausgaben zurückzugeben. Standardmäßig nimmt der Befehl `echo` Eingaben (Standardeingabe oder stdin) von der Tastatur entgegen und gibt Ausgaben (Standardausgabe oder stdout) auf dem Bildschirm zurück. Deshalb erhalten Sie "Hello World" auf dem Bildschirm, wenn Sie `echo Hello World` in Ihrer Shell eingeben. Die I/O-Umleitung ermöglicht es uns jedoch, dieses Standardverhalten zu ändern, was uns eine größere Dateiflexibilität bietet.

Fahren wir mit dem nächsten Teil des Befehls fort:

```bash
>
```

Das `>` ist ein Umleitungsoperator, der es uns ermöglicht, zu ändern, wohin die Standardausgabe geht. Es ermöglicht uns, die Ausgabe von `echo Hello World` in eine Datei statt auf den Bildschirm zu senden. Wenn die Datei noch nicht existiert, wird sie für uns erstellt. Wenn sie jedoch existiert, wird sie überschrieben (Sie können ein Shell-Flag hinzufügen, um dies zu verhindern, je nachdem, welche Shell Sie verwenden).

Und so funktioniert die stdout-Umleitung im Grunde!

Nun, nehmen wir an, ich wollte meine `peanuts.txt` nicht überschreiben. Glücklicherweise gibt es dafür auch einen Umleitungsoperator: `>>`.

```bash
echo Hello World >> peanuts.txt
```

Dies wird "Hello World" an das Ende der Datei `peanuts.txt` anhängen. Wenn die Datei noch nicht existiert, wird sie für uns erstellt, genau wie der `>`-Umleiter!

## Exercise

Try a couple of commands:

```bash
ls -l /var/log > myoutput.txt
echo Hello World > rm
> somefile.txt
```

## Quiz Question

Welchen Umleiter verwenden Sie, um die Ausgabe an eine Datei anzuhängen?

## Quiz Answer

> >
