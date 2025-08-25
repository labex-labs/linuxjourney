---
index: 1
lang: "de"
title: "stdout (Standard Out)"
meta_title: "stdout (Standard Out) - Text-Fu"
meta_description: "Erfahren Sie mehr über Linux stdout und I/O-Umleitung. Verstehen Sie, wie Sie die Befehlsausgabe mit den Operatoren > und >> in Dateien umleiten. Beginnen Sie noch heute Ihre Linux-Reise!"
meta_keywords: "Linux stdout, I/O-Umleitung, Linux-Befehle, Ausgabe umleiten, Linux-Tutorial, Linux für Anfänger, Linux-Anleitung, Shell-Skripting"
---

## Lesson Content

Inzwischen sind wir mit vielen Befehlen und deren Ausgabe vertraut, und das bringt uns zu unserem nächsten Thema: I/O (Input/Output) Streams. Lassen Sie uns den folgenden Befehl ausführen, und wir werden besprechen, wie das funktioniert.

```bash
echo Hello World > peanuts.txt
```

Was ist gerade passiert? Nun, überprüfen Sie das Verzeichnis, in dem Sie diesen Befehl ausgeführt haben, und siehe da, Sie sollten eine Datei namens `peanuts.txt` sehen. Schauen Sie in diese Datei, und Sie sollten den Text "Hello World" sehen. Viele Dinge sind gerade in einem Befehl passiert, also lassen Sie uns ihn aufschlüsseln.

Zuerst zerlegen wir den ersten Teil:

```bash
echo Hello World
```

Wir wissen, dass dies "Hello World" auf dem Bildschirm ausgibt, aber wie? Prozesse verwenden I/O-Streams, um Eingaben zu empfangen und Ausgaben zurückzugeben. Standardmäßig nimmt der Befehl `echo` die Eingabe (Standardeingabe oder stdin) von der Tastatur und gibt die Ausgabe (Standardausgabe oder stdout) auf dem Bildschirm zurück. Deshalb erhalten Sie "Hello World" auf dem Bildschirm, wenn Sie `echo Hello World` in Ihrer Shell eingeben. Die I/O-Umleitung ermöglicht es uns jedoch, dieses Standardverhalten zu ändern, was uns eine größere Dateiflexibilität bietet.

Fahren wir mit dem nächsten Teil des Befehls fort:

```bash
>
```

Das `>` ist ein Umleitungsoperator, der es uns ermöglicht, zu ändern, wohin die Standardausgabe geht. Er ermöglicht es uns, die Ausgabe von `echo Hello World` in eine Datei statt auf den Bildschirm zu senden. Wenn die Datei noch nicht existiert, wird sie für uns erstellt. Wenn sie jedoch existiert, wird sie überschrieben (Sie können ein Shell-Flag hinzufügen, um dies zu verhindern, je nachdem, welche Shell Sie verwenden).

Und so funktioniert die stdout-Umleitung im Grunde!

Nun, nehmen wir an, ich wollte meine `peanuts.txt` nicht überschreiben. Glücklicherweise gibt es dafür auch einen Umleitungsoperator: `>>`.

```bash
echo Hello World >> peanuts.txt
```

Dies wird "Hello World" an das Ende der Datei `peanuts.txt` anhängen. Wenn die Datei noch nicht existiert, wird sie für uns erstellt, genau wie der `>`-Umleiter!

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der I/O-Umleitung zu festigen:

1. **[Eingabe und Ausgabe in Linux umleiten](https://labex.io/de/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Üben Sie die Steuerung des Datenflusses von Befehlen, indem Sie die Standardausgabe (stdout), die Standardfehlerausgabe (stderr) und die Standardeingabe (stdin) mithilfe von Operatoren wie `>`, `>>`, `2>` und dem Befehl `tee` manipulieren.

Dieses Labor wird Ihnen helfen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die I/O-Umleitung aufzubauen.

## Quiz Question

Welchen Umleitungsoperator verwenden Sie, um die Ausgabe an eine Datei anzuhängen?

## Quiz Answer

> >
