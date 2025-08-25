---
index: 2
lang: "de"
title: "pwd (Print Working Directory)"
meta_title: "pwd (Print Working Directory) - Befehlszeile"
meta_description: "Erfahren Sie, wie Sie den Befehl 'pwd' in Linux verwenden, um Ihr aktuelles Arbeitsverzeichnis auszugeben. Verstehen Sie Linux-Dateisystempfade und -navigation für Anfänger."
meta_keywords: "pwd Befehl, Linux Verzeichnis, aktuelles Verzeichnis, Linux Pfad, Linux Tutorial, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Alles in Linux ist eine Datei. Wenn Sie tiefer in Linux eintauchen, werden Sie dies verstehen, aber vorerst sollten Sie es einfach im Hinterkopf behalten. Jede Datei ist in einem hierarchischen Verzeichnisbaum organisiert. Das erste Verzeichnis im Dateisystem wird passenderweise als Stammverzeichnis bezeichnet. Das Stammverzeichnis enthält viele Ordner und Dateien, die weitere Ordner und Dateien speichern können usw. Hier ist ein Beispiel dafür, wie der Verzeichnisbaum aussieht:

```plaintext
/
|-- bin
|   |-- file1
|   |-- file2
|-- etc
|   |-- file3
|   `-- directory1
|       |-- file4
|       `-- file5
|-- home
|-- var
```

Der Speicherort dieser Dateien und Verzeichnisse wird als Pfade bezeichnet. Wenn Sie einen Ordner namens `home` mit einem Unterordner namens `pete` und einem weiteren Unterordner namens `Movies` hätten, würde dieser Pfad so aussehen: `/home/pete/Movies`. Ziemlich einfach, oder?

Die Navigation im Dateisystem ist, ähnlich wie im echten Leben, hilfreich, wenn Sie wissen, wo Sie sind und wohin Sie gehen. Um zu sehen, wo Sie sind, können Sie den Befehl `pwd` verwenden. Dieser Befehl bedeutet "print working directory" (Arbeitsverzeichnis ausgeben) und zeigt Ihnen einfach an, in welchem Verzeichnis Sie sich befinden. Beachten Sie, dass der Pfad vom Stammverzeichnis ausgeht.

```bash
pwd
```

Wo sind Sie? Wo bin ich? Probieren Sie es aus.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Linux-Dateisystemnavigation und der Identifizierung Ihres aktuellen Standorts zu vertiefen:

1. **[Linux pwd Befehl: Verzeichnisanzeige](https://labex.io/de/labs/linux-linux-pwd-command-directory-displaying-209734)** - Dieses Lab bietet einen fokussierten Überblick und die praktische Anwendung des `pwd`-Befehls, der direkt mit der Einführung der Lektion zum Auffinden Ihres aktuellen Verzeichnisses übereinstimmt.
2. **[Linux Verzeichnisnavigation](https://labex.io/de/labs/linux-directory-navigation-387844)** - Stellen Sie Ihre grundlegenden Linux-Befehlszeilenkenntnisse auf die Probe, indem Sie durch verschiedene Verzeichnisse navigieren und so Ihr Verständnis von Pfaden und der Dateisystemstruktur festigen.
3. **[Linux cd Befehl: Verzeichniswechsel](https://labex.io/de/labs/linux-linux-cd-command-directory-changing-209733)** - Lernen Sie, Ihr Dateisystem effizient mit dem `cd`-Befehl zu navigieren, und verstehen Sie verschiedene Techniken zum Wechseln von Verzeichnissen und zum Erkunden der Dateistruktur.

Diese Labs helfen Ihnen, die Konzepte der Dateisystemhierarchie und -navigation in realen Szenarien anzuwenden und Vertrauen in wesentliche Linux-Befehle aufzubauen.

## Quiz Question

Wie finde ich heraus, in welchem Verzeichnis ich mich gerade befinde?

## Quiz Answer
pwd
