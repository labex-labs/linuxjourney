---
index: 2
lang: "de"
title: "pwd (Print Working Directory)"
meta_title: "pwd (Print Working Directory) - Befehlszeile"
meta_description: "Erfahren Sie, wie Sie den 'pwd'-Befehl in Linux verwenden, um Ihr aktuelles Arbeitsverzeichnis auszugeben. Verstehen Sie Linux-Dateisystempfade und -Navigation für Anfänger."
meta_keywords: "pwd command, Linux directory, current directory, Linux path, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

Alles in Linux ist eine Datei. Wenn Sie tiefer in Linux eintauchen, werden Sie das verstehen, aber vorerst sollten Sie das einfach im Hinterkopf behalten. Jede Datei ist in einem hierarchischen Verzeichnisbaum organisiert. Das erste Verzeichnis im Dateisystem wird passenderweise als Stammverzeichnis (root directory) bezeichnet. Das Stammverzeichnis enthält viele Ordner und Dateien, die wiederum weitere Ordner und Dateien speichern können usw. Hier ist ein Beispiel, wie der Verzeichnisbaum aussieht:

```plaintext
/
|-- bin
| |-- file1
| |-- file2
|-- etc
| |-- file3
| `-- directory1
|  |-- file4
|  `-- file5
|-- home
|-- var
```

Der Speicherort dieser Dateien und Verzeichnisse wird als Pfade bezeichnet. Wenn Sie einen Ordner namens `home` hätten, mit einem Ordner darin namens `pete` und einem weiteren Ordner in diesem Ordner namens `Movies`, würde dieser Pfad so aussehen: `/home/pete/Movies`. Ziemlich einfach, oder?

Die Navigation im Dateisystem ist, ähnlich wie im echten Leben, hilfreich, wenn Sie wissen, wo Sie sind und wohin Sie gehen. Um zu sehen, wo Sie sind, können Sie den Befehl `pwd` verwenden. Dieser Befehl bedeutet "print working directory" (aktuelles Arbeitsverzeichnis ausgeben) und zeigt Ihnen einfach an, in welchem Verzeichnis Sie sich befinden. Beachten Sie, dass der Pfad vom Stammverzeichnis ausgeht.

```bash
pwd
```

Wo sind Sie? Wo bin ich? Probieren Sie es aus.

## Exercise

Für praktische Übungen mit dem `pwd`-Befehl probieren Sie dieses interaktive Lab aus:

- [Linux pwd Command: Directory Displaying](https://labex.io/de/labs/linux-linux-pwd-command-directory-displaying-209734)

## Quiz Question

Wie finde ich heraus, in welchem Verzeichnis Sie sich gerade befinden?

## Quiz Answer

pwd
