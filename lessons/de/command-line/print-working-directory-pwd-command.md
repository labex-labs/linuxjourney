---
lang: "de"
title: "pwd (Aktuelles Arbeitsverzeichnis ausgeben)"
meta_title: "pwd (Aktuelles Arbeitsverzeichnis ausgeben) - Command Line"
meta_description: "Erfahren Sie, wie Sie den Befehl 'pwd' in Linux verwenden, um Ihr aktuelles Arbeitsverzeichnis auszugeben. Verstehen Sie Linux-Dateisystempfade und -navigation für Anfänger."
meta_keywords: "pwd Befehl, Linux Verzeichnis, aktuelles Verzeichnis, Linux Pfad, Linux Tutorial, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Alles in Linux ist eine Datei. Wenn Sie tiefer in Linux eintauchen, werden Sie dies verstehen, aber vorerst sollten Sie es einfach im Hinterkopf behalten. Jede Datei ist in einem hierarchischen Verzeichnisbaum organisiert. Das erste Verzeichnis im Dateisystem wird passenderweise als Root-Verzeichnis bezeichnet. Das Root-Verzeichnis enthält viele Ordner und Dateien, die wiederum weitere Ordner und Dateien speichern können usw. Hier ist ein Beispiel, wie der Verzeichnisbaum aussieht:

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

Der Speicherort dieser Dateien und Verzeichnisse wird als Pfade bezeichnet. Wenn Sie einen Ordner namens `home` hätten, mit einem Ordner darin namens `pete` und einem weiteren Ordner in diesem Ordner namens `Movies`, würde dieser Pfad so aussehen: `/home/pete/Movies`. Ziemlich einfach, oder?

Die Navigation im Dateisystem ist, ähnlich wie im echten Leben, hilfreich, wenn man weiß, wo man ist und wohin man geht. Um zu sehen, wo Sie sich befinden, können Sie den Befehl `pwd` verwenden. Dieser Befehl bedeutet "print working directory" (aktuelles Arbeitsverzeichnis ausgeben) und zeigt Ihnen einfach an, in welchem Verzeichnis Sie sich befinden. Beachten Sie, dass der Pfad vom Root-Verzeichnis ausgeht.

```bash
pwd
```

Wo sind Sie? Wo bin ich? Probieren Sie es aus.

## Exercise

No exercises for this lesson.

## Quiz Question

Wie finde ich heraus, in welchem Verzeichnis ich mich gerade befinde?

## Quiz Answer

pwd
