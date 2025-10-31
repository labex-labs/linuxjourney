---
index: 9
lang: "de"
title: "Festplattennutzung"
meta_title: "Festplattennutzung - Das Dateisystem"
meta_description: "Erfahren Sie, wie Sie die Linux-Festplattennutzung und den freien Speicherplatz mit den Befehlen df und du überprüfen. Diese Anleitung behandelt die Analyse des Speicherplatzes, einschließlich der Inode-Nutzung mit df -i linux, und wie Sie herausfinden, welche Dateien Platz belegen."
meta_keywords: "df Befehl, du Befehl, Linux Festplattennutzung, freien Speicherplatz prüfen, df -i linux, Speicherverwaltung, Linux Tutorial, Speichernutzung, Dateisystemnutzung"
---

## Lesson Content

Die Verwaltung des Speicherplatzes ist eine grundlegende Aufgabe für jeden Linux-Benutzer oder Administrator. Zwei wesentliche Befehle hierfür sind `df` und `du`. Lassen Sie uns untersuchen, wie Sie diese verwenden können, um Ihre Festplattenauslastung effektiv zu überwachen.

### Überprüfung des Dateisystemspeichers mit df

Der Befehl `df` (disk free) meldet den auf Ihren gemounteten Dateisystemen verwendeten und verfügbaren Speicherplatz. Er bietet einen Überblick über Ihre Speicherkapazität.

Um einen Bericht in einem menschenlesbaren Format (z. B. GB, MB, KB) zu erhalten, verwenden Sie das Flag `-h`:

```bash
pete@icebox:~$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       6.2G  2.3G  3.6G  40% /
```

Diese Ausgabe zeigt das Dateisystemgerät, die Gesamtgröße, den belegten Speicherplatz, den verfügbaren Speicherplatz, den Nutzungsprozentsatz und den Einhängepunkt.

### Analyse der Inode-Nutzung

Neben dem Block-Speicher verwenden Dateisysteme auch Inodes, um Metadaten über Dateien (wie Berechtigungen, Eigentümerschaft und Speicherort) zu speichern. In seltenen Fällen kann Ihnen der Speicherplatz für Inodes ausgehen, selbst wenn noch freier Speicherplatz vorhanden ist. Um die Inode-Nutzung zu überprüfen, können Sie den Befehl `df -i` verwenden. Die Ausführung von `df -i` unter Linux gibt Ihnen einen klaren Überblick über die Inode-Zuweisung.

```bash
pete@icebox:~$ df -i
Filesystem      Inodes  IUsed   IFree IUse% Mounted on
/dev/sda1      4128768 128768 4000000    4% /
```

### Zusammenfassung der Verzeichnisnutzung mit du

Wenn Sie feststellen, dass eine Festplatte voll wird, möchten Sie herausfinden, welche Dateien oder Verzeichnisse den meisten Speicherplatz verbrauchen. Für diese Aufgabe ist der Befehl `du` (disk usage) das perfekte Werkzeug.

Die Ausführung von `du` ohne Argumente zeigt die Festplattennutzung für jedes Unterverzeichnis an Ihrem aktuellen Standort. Die Verwendung des Flags `-h` liefert eine menschenlesbare Zusammenfassung:

```bash
du -h
```

Sie können auch einen Pfad angeben, z. B. `du -h /home/pete`, um ein bestimmtes Verzeichnis zu analysieren. Die Ausführung auf dem Stammverzeichnis (`du -h /`) kann viele Ergebnisse liefern, daher ist es oft besser, bestimmte Verzeichnisse zu überprüfen, von denen Sie vermuten, dass sie groß sind.

### df vs du Eine kurze Zusammenfassung

Die Syntax für `df` und `du` ist so ähnlich, dass man sie leicht verwechseln kann. Hier ist eine einfache Möglichkeit, sich den Unterschied zu merken:

- Verwenden Sie `df`, um zu prüfen, wie viel **d**isk **f**ree (Festplatte frei) auf Ihren Dateisystemen ist.
- Verwenden Sie `du`, um die **d**isk **u**sage (Festplattennutzung) spezifischer Dateien und Verzeichnisse zu prüfen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis für die Verwaltung und Auslastung des Speicherplatzes unter Linux zu festigen:

1. **[Linux-Partitionen und Dateisysteme verwalten](https://labex.io/de/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Üben Sie das Erstellen, Formatieren und Einhängen von Dateisystemen, welche die zugrunde liegenden Strukturen sind, über die `df` und `du` berichten.
2. **[Eine Swap-Datei unter Linux erstellen und aktivieren](https://labex.io/de/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Lernen Sie, den virtuellen Speicher auf der Festplatte zu verwalten, ein kritischer Aspekt der Systemressourcenverwaltung, der den Speicherplatz beeinflusst.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Speicherressourcen aufzubauen.

## Quiz Question

Welcher Befehl wird verwendet, um anzuzeigen, wie viel Speicherplatz auf Ihrer Festplatte frei ist? Bitte antworten Sie in Kleinbuchstaben auf Englisch.

## Quiz Answer

df
