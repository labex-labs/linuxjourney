---
index: 3
lang: "de"
title: "cd (Verzeichnis wechseln)"
meta_title: "cd (Verzeichnis wechseln) - Kommandozeile"
meta_description: "Lerne den Linux-Befehl cd mit Beispielen für absolute Pfade, relative Pfade, Home-Verzeichnis-Verknüpfungen, übergeordnete Verzeichnisse und Navigation zum vorherigen Verzeichnis."
meta_keywords: "cd Befehl, linux cd Befehl, Verzeichnis wechseln, cd übergeordnetes Verzeichnis, cd home, cd vorheriges Verzeichnis, absoluter Pfad, relativer Pfad"
---

## Lesson Content

Um sich im Linux-Dateisystem zu bewegen, verwendet man Pfade, um das Ziel anzugeben. Das wichtigste Werkzeug dafür ist der Befehl `cd`, kurz für change directory (Verzeichnis wechseln). Er ändert das aktuelle Arbeitsverzeichnis der Shell.

Die grundlegende Syntax lautet:

```bash
cd [DIRECTORY]
```

### Pfade verstehen

Es gibt zwei Möglichkeiten, einen Pfad anzugeben: absolut und relativ.

- **Absoluter Pfad**: Der vollständige Pfad, beginnend beim Wurzelverzeichnis (`/`). Zum Beispiel: `/home/pete/Desktop`.

- **Relativer Pfad**: Ein Pfad basierend auf deinem aktuellen Standort. Wenn du dich in `/home/pete/Documents` befindest und auf ein Unterverzeichnis namens `taxes` zugreifen möchtest, kannst du `taxes/` verwenden.

### Verwendung des cd-Befehls

Um in ein bestimmtes Verzeichnis mit einem absoluten Pfad zu wechseln, gib ein:

```bash
$ cd /home/pete/Pictures
```

Dieser Befehl bringt dich direkt in das Verzeichnis `Pictures`.

Du kannst deinen Standort mit `pwd` überprüfen:

```bash
$ pwd
/home/pete/Pictures
```

### Navigation in ein Unterverzeichnis

Wenn du dich bereits in einem Verzeichnis befindest und in ein Unterverzeichnis wechseln möchtest, verwende einen relativen Pfad. Zum Beispiel, wenn dein aktueller Standort `/home/pete/Pictures` ist und es einen Ordner namens `Hawaii` enthält, kannst du mit folgendem Befehl hineinnavigieren:

```bash
$ cd Hawaii
```

Beachte, dass wir nur den Ordnernamen verwendet haben. Das liegt daran, dass wir uns bereits im übergeordneten Verzeichnis `/home/pete/Pictures` befanden.

### Wichtige Navigationskürzel

Die Navigation mit vollständigen Pfaden kann mühsam sein. Glücklicherweise bietet die Shell mehrere Kürzel, die das Bewegen deutlich schneller machen.

- `.` (aktuelles Verzeichnis): Repräsentiert das Verzeichnis, in dem du dich gerade befindest.
- `..` (übergeordnetes Verzeichnis): Bewegt dich eine Ebene nach oben in das Verzeichnis, das dein aktuelles Verzeichnis enthält.
- `~` (Home-Verzeichnis): Ein Kürzel für dein persönliches Home-Verzeichnis, z.B. `/home/pete`.
- `-` (vorheriges Verzeichnis): Bringt dich zurück in das letzte Verzeichnis, in dem du warst.

Du kannst diese Kürzel mit `cd` verwenden:

```bash
$ cd .
$ cd ..
$ cd ~
$ cd -
```

Probiere diese Kürzel aus, um effizienter an der Kommandozeile zu arbeiten.

### Praktische cd-Beispiele

Wechsle in dein Home-Verzeichnis:

```bash
$ cd
```

Gehe zwei Ebenen nach oben:

```bash
$ cd ../..
```

Wechsle in ein Verzeichnis, dessen Name Leerzeichen enthält, indem du es in Anführungszeichen setzt:

```bash
$ cd "Vacation Photos"
```

Gehe zurück in das vorherige Verzeichnis:

```bash
$ cd -
/home/pete/Documents
```

### Häufige Fragen

**Warum sagt cd „No such file or directory“?** Der Pfad existiert von deinem aktuellen Standort aus nicht, oder der Name wurde falsch eingegeben. Verwende `ls`, um verfügbare Verzeichnisse aufzulisten.

**Warum sagt cd „Permission denied“?** Du hast keine Berechtigung, dieses Verzeichnis zu betreten.

**Was passiert, wenn ich cd ohne Argumente ausführe?** Du gelangst in dein Home-Verzeichnis.

**Funktioniert cd mit Dateien?** Nein. `cd` wechselt nur in Verzeichnisse, nicht in reguläre Dateien.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um dein Verständnis der Linux-Verzeichnisnavigation zu vertiefen:

1. **[Linux cd Command: Directory Changing](https://labex.io/de/labs/linux-linux-cd-command-directory-changing-209733)** – Lerne den Linux-Befehl `cd`, um dein Dateisystem effizient zu navigieren, einschließlich verschiedener Techniken zum Verzeichniswechsel, Verständnis von Pfaden und Erkundung der Dateistruktur.
2. **[Linux Directory Navigation](https://labex.io/de/labs/linux-directory-navigation-387844)** – Teste deine grundlegenden Linux-Kommandozeilen-Fähigkeiten, indem du dich mit wichtigen Befehlen durch Verzeichnisse bewegst.
3. **[Setting Up a New Project Structure](https://labex.io/de/labs/linux-setting-up-a-new-project-structure-387859)** – Übe deine Fähigkeiten im Linux-Verzeichnismanagement, indem du eine bestimmte Projektstruktur erstellst und dich mit wichtigen Befehlen wie `mkdir` und `cd` darin bewegst.

Diese Labs helfen dir, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Navigation des Linux-Dateisystems zu gewinnen.

## Quiz Question

Wenn du dich in `/home/pete/Pictures` befindest und in das übergeordnete Verzeichnis (`/home/pete`) wechseln möchtest, welcher vollständige Befehl ist korrekt? Bitte antworte auf Englisch und achte auf Groß- und Kleinschreibung sowie Leerzeichen.

## Quiz Answer

cd ..
