---
index: 8
lang: "de"
title: "less"
meta_title: "less - Kommandozeile"
meta_description: "Lerne den Linux-Befehl less mit Beispielen zum Anzeigen großer Dateien, Scrollen, Suchen, Springen zu Zeilen, Verfolgen von Logs und Beenden von less."
meta_keywords: "less Befehl, linux less, große Datei anzeigen linux, in less suchen, less beenden, less -N, less +F, Textanzeige linux"
---

## Lesson Content

Beim Betrachten von Textdateien, die zu groß sind, um auf einen Bildschirm zu passen, ist der Befehl `less` ein unverzichtbares Werkzeug. Wie das alte Unix-Sprichwort sagt: „less ist mehr.“ Dies spielt darauf an, dass es auch einen Befehl `more` mit ähnlicher Funktionalität gibt.

Das Dienstprogramm `less` zeigt Text in einem seitenweisen Format an, sodass du durch eine Datei navigieren kannst, ohne dein Terminal zu überfluten.

### Einstieg in den Less-Befehl

Um eine Datei anzusehen, verwende `less` gefolgt vom Dateinamen.

```bash
$ less /home/pete/Documents/text1
```

Sobald du dich im `less`-Viewer befindest, funktionieren deine üblichen Shell-Befehle nicht mehr. Stattdessen verwendest du eine spezielle Tastenbelegung, um dich durch den Text zu bewegen und mit ihm zu interagieren.

### Navigation und Steuerung

Du kannst verschiedene Tasten verwenden, um im Dokument zu navigieren:

- **Pfeiltasten und Bild-Tasten**: Verwende `Bild auf`, `Bild ab`, `Pfeil hoch` und `Pfeil runter`, um zeilen- oder seitenweise zu navigieren.
- **Zum Anfang springen**: Drücke `g`, um direkt zum Anfang der Textdatei zu springen.
- **Zum Ende springen**: Drücke `G` (Shift + g), um zum Ende der Textdatei zu springen.
- **Eine halbe Seite bewegen**: Drücke `u`, um nach oben und `d`, um nach unten zu scrollen.
- **Hilfemenü**: Wenn du die Befehle in `less` vergessen hast, drücke einfach `h`, um eine hilfreiche Zusammenfassung anzuzeigen.

### Suchen in Less

Eine mächtige Funktion von `less` ist die Möglichkeit, nach Text zu suchen. Tippe `/` gefolgt vom Suchbegriff und drücke Enter.

- `/search_term`: Sucht vorwärts nach „search_term“.
- `?search_term`: Sucht rückwärts nach „search_term“.
- `n`: Springt zum nächsten Vorkommen des Suchbegriffs.
- `N`: Springt zum vorherigen Vorkommen.

### Wie man Less beendet

Wenn du mit dem Betrachten der Datei fertig bist, musst du wissen, wie du `less` beendest und zur Eingabeaufforderung zurückkehrst.

- **Beenden**: Drücke einfach `q`, um den `less`-Viewer zu verlassen und zur Shell zurückzukehren.

### Nützliche less-Optionen

Du kannst `less` mit Optionen starten:

```bash
$ less -N file.txt
$ less +G file.txt
$ less +F /var/log/syslog
```

- `-N`: Zeigt Zeilennummern an.
- `+G`: Öffnet die Datei am Ende.
- `+F`: Folgt neuen Inhalten, während sie hinzugefügt werden, ähnlich wie `tail -f`.

Während du einer Datei mit `+F` folgst, drücke `Ctrl-C`, um das Folgen zu stoppen und zur normalen Navigation zurückzukehren, dann drücke `q`, um zu beenden.

### Häufige Fragen

**Ist less besser als cat?** Verwende `cat` für kurze Dateien und `less` für lange Dateien oder Dateien, in denen du suchen musst.

**Wie suche ich ohne Berücksichtigung der Groß-/Kleinschreibung?** Starte `less` mit `-i` oder tippe Suchbegriffe normal ein, wenn das Muster keine Großbuchstaben enthält (auf vielen Systemen).

**Kann less die Ausgabe von Befehlen öffnen?** Ja. Leite die Ausgabe hinein, z.B. `dmesg | less`.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um dein Verständnis für das Anzeigen und Navigieren von Textdateien in Linux zu vertiefen:

1. **[Linux less Command: File Paging](https://labex.io/de/labs/linux-linux-less-command-file-paging-214301)** – Lerne den Linux-Befehl 'less' für effizientes Anzeigen und Navigieren von Textdateien, einschließlich Suche, Zeilennummern und Mustererkennung.
2. **[Linux more Command: File Scrolling](https://labex.io/de/labs/linux-linux-more-command-file-scrolling-214299)** – Lerne den Linux-Befehl 'more' für effizientes Anzeigen von Textdateien, mit Grundlagen, Starten ab bestimmten Zeilen und Anpassung der Anzeige.
3. **[Viewing Log and Configuration Files in Linux](https://labex.io/de/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** – Lerne wichtige Linux-Kommandozeilenfähigkeiten zum effizienten Anzeigen und Navigieren von Textdateien, einschließlich Systemlogs und Konfigurationsdateien, mit Befehlen wie `cat`, `more` und `less`.

Diese Labs helfen dir, die Konzepte in realen Szenarien anzuwenden und Sicherheit im Umgang mit Textdateien und Navigation zu gewinnen.

## Quiz Question

Wie beendest du den Befehl `less`? Bitte gib die einzelne Zeichen-Taste als Antwort an. Hinweis: Die Antwort ist ein englischer Buchstabe mit Groß-/Kleinschreibung.

## Quiz Answer

q
