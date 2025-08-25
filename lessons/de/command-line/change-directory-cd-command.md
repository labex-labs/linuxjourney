---
index: 3
lang: "de"
title: "cd (Verzeichnis wechseln)"
meta_title: "cd (Verzeichnis wechseln) - Befehlszeile"
meta_description: "Erfahren Sie, wie Sie den 'cd'-Befehl in Linux verwenden, um Verzeichnisse zu navigieren. Verstehen Sie absolute, relative Pfade und nützliche Abkürzungen. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "cd Befehl, Verzeichnis wechseln, Linux Pfade, absoluter Pfad, relativer Pfad, Linux Tutorial, Linux für Anfänger, Linux Navigation"
---

## Lesson Content

Nachdem Sie nun wissen, wo Sie sich befinden, wollen wir uns ein wenig im Dateisystem bewegen. Denken Sie daran, dass wir uns mithilfe von Pfaden zurechtfinden müssen. Es gibt zwei verschiedene Möglichkeiten, einen Pfad anzugeben: mit absoluten und relativen Pfaden.

- Absoluter Pfad: Dies ist der Pfad vom Stammverzeichnis aus. Das Stammverzeichnis ist der Chef. Das Stammverzeichnis wird üblicherweise als Schrägstrich (`/`) dargestellt. Jedes Mal, wenn Ihr Pfad mit `/` beginnt, bedeutet dies, dass Sie vom Stammverzeichnis aus starten. Zum Beispiel `/home/pete/Desktop`.

- Relativer Pfad: Dies ist der Pfad von Ihrem aktuellen Standort im Dateisystem aus. Wenn ich mich im Verzeichnis `/home/pete/Documents` befände und zu einem Unterverzeichnis namens `taxes` gelangen wollte, müsste ich nicht den gesamten Pfad vom Stammverzeichnis aus angeben, wie `/home/pete/Documents/taxes`; ich könnte stattdessen einfach zu `taxes/` gehen.

Nachdem Sie nun wissen, wie Pfade funktionieren, brauchen wir nur noch etwas, das uns hilft, in das gewünschte Verzeichnis zu wechseln. Glücklicherweise haben wir dafür `cd` oder „change directory“ (Verzeichnis wechseln).

```bash
cd /home/pete/Pictures
```

Ich habe nun meinen Verzeichnisstandort nach `/home/pete/Pictures` geändert.

Von diesem Verzeichnis aus habe ich nun einen Ordner namens `Hawaii` darin. Ich kann zu diesem Ordner navigieren mit:

```bash
cd Hawaii
```

Beachten Sie, dass ich nur den Namen des Ordners verwendet habe? Das liegt daran, dass ich bereits in `/home/pete/Pictures` war.

Es kann ziemlich ermüdend sein, ständig mit absoluten und relativen Pfaden zu navigieren. Glücklicherweise gibt es einige Abkürzungen, die Ihnen helfen.

- `.` (aktuelles Verzeichnis): Dies ist das Verzeichnis, in dem Sie sich gerade befinden.
- `..` (vorheriges Verzeichnis): Bringt Sie in das Verzeichnis oberhalb Ihres aktuellen Verzeichnisses.
- `~` (Home-Verzeichnis): Dieses Verzeichnis ist standardmäßig Ihr „Home-Verzeichnis“, z. B. `/home/pete`.
- `-` (vorheriges Verzeichnis): Dies bringt Sie in das Verzeichnis zurück, in dem Sie sich gerade befunden haben.

```bash
cd .
cd ..
cd ~
cd -
```

Probieren Sie sie aus!

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Linux-Verzeichnisnavigation zu vertiefen:

1. **[Linux cd Befehl: Verzeichniswechsel](https://labex.io/de/labs/linux-linux-cd-command-directory-changing-209733)** - Lernen Sie den Linux `cd`-Befehl, um Ihr Dateisystem effizient zu navigieren, einschließlich verschiedener Techniken zum Wechseln von Verzeichnissen, zum Verständnis von Pfaden und zum Erkunden der Dateistruktur.
2. **[Linux Verzeichnisnavigation](https://labex.io/de/labs/linux-directory-navigation-387844)** - Stellen Sie Ihre grundlegenden Linux-Befehlszeilenkenntnisse auf die Probe, indem Sie mit wichtigen Befehlen durch Verzeichnisse navigieren.
3. **[Einrichten einer neuen Projektstruktur](https://labex.io/de/labs/linux-setting-up-a-new-project-structure-387859)** - Üben Sie Ihre Linux-Verwaltungsfähigkeiten, indem Sie eine spezifische Projektstruktur erstellen und diese mit wichtigen Befehlen wie `mkdir` und `cd` navigieren.

Diese Übungen helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Navigation im Linux-Dateisystem aufzubauen.

## Quiz Question

Wenn Sie sich in `/home/pete/Pictures` befinden und nach `/home/pete` wechseln möchten, welche gute Abkürzung können Sie verwenden?

## Quiz Answer

cd ..
