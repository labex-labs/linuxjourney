---
index: 3
lang: "de"
title: "cd (Verzeichnis wechseln)"
meta_title: "cd (Verzeichnis wechseln) - Kommandozeile"
meta_description: "Lernen Sie den essentiellen cd Linux-Befehl, um Verzeichnisse zu wechseln. Diese Anleitung behandelt die Verwendung des cd-Befehls in der Eingabeaufforderung, die Navigation zu jedem cd-Ordner mit absoluten und relativen Pfaden sowie nützliche Abkürzungen."
meta_keywords: "cd Befehl, cd Linux Befehl, cd Ordner, cd Eingabeaufforderung, cd Befehl cmd, Verzeichnis wechseln, Linux Navigation, absoluter Pfad, relativer Pfad"
---

## Lesson Content

Um sich im Linux-Dateisystem zu bewegen, verwenden Sie Pfade, um Ihr Ziel anzugeben. Das primäre Werkzeug dafür ist der `cd` (change directory/Verzeichnis wechseln) Befehl. Zu verstehen, wie man diesen `cd linux befehl` verwendet, ist eine grundlegende Fähigkeit für die Arbeit im Terminal oder in der `cd befehlszeile`.

### Pfade verstehen

Es gibt zwei Möglichkeiten, einen Pfad anzugeben: absolut und relativ.

- **Absoluter Pfad**: Dies ist der vollständige Pfad, der vom Stammverzeichnis (`/`) ausgeht. Die Wurzel ist das oberste Verzeichnis im Dateisystem. Jeder Pfad, der mit `/` beginnt, ist ein absoluter Pfad. Zum Beispiel: `/home/pete/Desktop`.

- **Relativer Pfad**: Dieser Pfad bezieht sich auf Ihren aktuellen Standort im Dateisystem. Wenn Sie sich in `/home/pete/Documents` befinden und auf ein Unterverzeichnis namens `taxes` zugreifen möchten, benötigen Sie nicht den vollständigen Pfad. Sie können einfach den relativen Pfad verwenden: `taxes/`.

### Den cd Befehl verwenden

Sobald Sie Pfade verstehen, können Sie den `cd befehl` verwenden, um Ihr aktuelles Verzeichnis zu wechseln. Ob Sie sich in einem Linux-Terminal oder einer Windows `cd befehlszeile cmd` befinden, das Konzept des Verzeichniswechsels ist universell, auch wenn sich die Syntax leicht unterscheiden kann.

Um mit einem absoluten Pfad in ein bestimmtes Verzeichnis zu wechseln, würden Sie Folgendes eingeben:

```bash
cd /home/pete/Pictures
```

Dieser Befehl bringt Sie direkt in das Verzeichnis `Pictures`.

### Navigation zu einem cd Ordner

Wenn Sie sich bereits in einem Verzeichnis befinden und in ein Unterverzeichnis wechseln möchten, können Sie einen relativen Pfad verwenden. Angenommen, Ihr aktueller Standort ist `/home/pete/Pictures` und es enthält einen `cd ordner` namens `Hawaii`, können Sie mit folgendem Befehl hinein navigieren:

```bash
cd Hawaii
```

Beachten Sie, dass wir nur den Namen des Ordners verwendet haben. Das liegt daran, dass wir uns bereits im übergeordneten Verzeichnis, `/home/pete/Pictures`, befanden.

### Wesentliche Navigations-Abkürzungen

Die Navigation mit vollständigen Pfaden kann mühsam sein. Glücklicherweise bietet die Shell mehrere Abkürzungen, um die Bewegung viel schneller zu machen.

- `.` (aktuelles Verzeichnis): Stellt das Verzeichnis dar, in dem Sie sich gerade befinden.
- `..` (übergeordnetes Verzeichnis): Bewegt Sie eine Ebene nach oben in das Verzeichnis, das Ihr aktuelles Verzeichnis enthält.
- `~` (Home-Verzeichnis): Eine Abkürzung zu Ihrem persönlichen Home-Verzeichnis, wie `/home/pete`.
- `-` (vorheriges Verzeichnis): Bringt Sie zurück in das letzte Verzeichnis, in dem Sie sich befanden.

You can use these shortcuts with the `cd command`:

```bash
cd .
cd ..
cd ~
cd -
```

Experimentieren Sie mit diesen Abkürzungen, um in der Befehlszeile effizienter zu werden.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Linux-Verzeichnisnavigation zu festigen:

1. **[Linux cd Befehl: Verzeichniswechsel](https://labex.io/de/labs/linux-linux-cd-command-directory-changing-209733)** - Lernen Sie den Linux `cd` Befehl kennen, um effizient durch Ihr Dateisystem zu navigieren, einschließlich verschiedener Techniken zum Wechseln von Verzeichnissen, zum Verständnis von Pfaden und zur Erkundung der Dateistruktur.
2. **[Linux Verzeichnisnavigation](https://labex.io/de/labs/linux-directory-navigation-387844)** - Stellen Sie Ihre grundlegenden Linux-Befehlszeilenkenntnisse auf die Probe, indem Sie mit wesentlichen Befehlen durch Verzeichnisse navigieren.
3. **[Einrichten einer neuen Projektstruktur](https://labex.io/de/labs/linux-setting-up-a-new-project-structure-387859)** - Üben Sie Ihre Linux-Verwaltungsfähigkeiten, indem Sie eine bestimmte Projektstruktur erstellen und mit wichtigen Befehlen wie `mkdir` und `cd` darin navigieren.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Selbstvertrauen beim Navigieren im Linux-Dateisystem aufzubauen.

## Quiz Question

Wenn Sie sich in `/home/pete/Pictures` befinden und in das übergeordnete Verzeichnis (`/home/pete`) navigieren möchten, lautet der vollständige Befehl, den Sie verwenden sollten? Bitte antworten Sie auf Englisch, achten Sie auf Groß-/Kleinschreibung und Leerzeichen.

## Quiz Answer

cd ..
