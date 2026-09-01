---
lesson_id: "tail-command"
course_id: "text-fu"
lang: "de"
order_index: 9
title: "tail"
description: "Lerne, das Ende einer Eingabe anzuzeigen und Dateien bei neu angehängten Inhalten zu verfolgen."
meta_title: "tail - Text-Fu"
meta_description: "Ein Linux-Leitfaden für Anfänger zum tail-Befehl. Erfahren Sie, wie Sie Linux tail verwenden, um das Ende von Dateien anzuzeigen und Protokolle in Echtzeit mit der leistungsstarken Option tail -f zu überwachen."
meta_keywords: "tail Befehl, Linux tail, tail -f, Protokolle anzeigen, Protokolle überwachen, Linux Tutorial, Linux für Anfänger, Linux Anleitung, Dateiüberwachung"
---

Der Befehl `tail` zeigt das Ende einer Datei oder eines Eingabestroms an. Er kann außerdem aktiv bleiben und neu angehängte Daten ausgeben, was beim Beobachten von Protokollen hilfreich ist.

## Die letzten zehn Zeilen anzeigen

Ohne Zähloption gibt `tail` die letzten 10 Zeilen jeder benannten Datei aus:

```bash
$ tail application.log
```

Enthält die Datei weniger als 10 Zeilen, werden alle vorhandenen Zeilen ausgegeben. Die Datei selbst wird nicht verändert.

:::single-choice{#tail-default-lines} Was zeigt `tail application.log` standardmäßig an?

::option[Bis zu 10 Zeilen am Anfang der Datei.]{#tail-first-ten explanation="Den Dateianfang wählt `head` aus. `tail` arbeitet vom Ende her."}
::option[Jede Zeile, die nach dem Befehlsstart hinzugefügt wird.]{#tail-follow-only explanation="Zum fortlaufenden Verfolgen ist `-f` oder eine ähnliche Option erforderlich. Ein einfaches `tail` gibt eine Momentaufnahme aus und beendet sich."}
::option[Bis zu 10 Zeilen am Ende der Datei.]{#tail-last-ten .correct explanation="Ohne Zähloption wählt `tail` die letzten zehn Zeilen aus oder alle Zeilen, wenn weniger vorhanden sind."}
:::

## Eine Zeilen- oder Byteanzahl wählen

Mit `-n NUMBER` wählst du eine andere Anzahl letzter Zeilen aus:

```bash
$ tail -n 20 application.log
```

Mit `-c NUMBER` wählst du stattdessen die letzten Bytes:

```bash
$ tail -c 100 payload.bin
```

Der Bytemodus kann mitten in einer Textzeile oder einem kodierten Zeichen beginnen. Für Text ist der Zeilenmodus daher meist verständlicher.

:::single-choice{#tail-twenty-lines} Welcher Befehl zeigt die letzten 20 Zeilen von `application.log` an?

::option[`tail -n 20 application.log`]{#tail-twenty-end .correct explanation="Die Option `-n` wählt eine Zeilenanzahl; `tail` entnimmt diese Zeilen am Ende."}
::option[`head -n 20 application.log`]{#head-twenty-start explanation="Dieser Befehl wählt 20 Zeilen am Anfang statt am Ende aus."}
::option[`tail -c 20 application.log`]{#tail-twenty-bytes explanation="Die Option `-c` wählt die letzten 20 Bytes, was nicht 20 Zeilen entspricht."}
:::

## Bei einer bestimmten Zeile beginnen

Ein vorangestelltes `+` ändert die Bedeutung: `tail -n +N` beginnt bei Zeile N und gibt bis zum Ende aus.

```bash
$ tail -n +5 report.txt
```

Damit werden die ersten vier Zeilen übersprungen und die Ausgabe beginnt bei Zeile 5. Das eignet sich, um eine bekannte Anzahl von Kopfzeilen aus einem Strom zu entfernen.

:::single-choice{#tail-start-line-five} Welcher Befehl gibt `report.txt` ab Zeile 5 aus?

::option[`tail -n +5 report.txt`]{#tail-from-five .correct explanation="Die Anzahl `+5` weist `tail` an, bei Zeile 5 zu beginnen und bis zum Ende fortzufahren."}
::option[`tail -n 5 report.txt`]{#tail-final-five explanation="Ohne Pluszeichen werden unabhängig von ihren absoluten Zeilennummern die letzten fünf Zeilen gewählt."}
::option[`head -n +5 report.txt`]{#head-plus-five explanation="Dies ist nicht die `tail`-Form für einen Start bei einer Zeile. Für den verlangten Bereich dient `tail -n +5`."}
:::

## Neu angehängte Daten verfolgen

Mit `-f` gibt `tail` zunächst das aktuelle Ende aus und bleibt anschließend aktiv, um neu angehängte Daten anzuzeigen:

```bash
$ tail -f application.log
```

Mit `Ctrl+C` unterbrichst du `tail` und kehrst zur Shell zurück. Das Verfolgen einer Datei zeigt nur neue Inhalte; es garantiert weder, dass die protokollierende Anwendung gesund ist, noch dass jedes relevante Ereignis in dieser Datei landet.

:::single-choice{#tail-follow-file} Welcher Befehl zeigt das aktuelle Ende von `application.log` und wartet anschließend auf neu angehängte Inhalte?

::option[`tail -f application.log`]{#tail-follow-app .correct explanation="Die Option `-f` hält `tail` aktiv und zeigt Daten an, die an die Datei angehängt werden."}
::option[`tail -n 0 application.log`]{#tail-zero-lines explanation="Dieser Befehl gibt zunächst keine Zeile aus und beendet sich, weil keine Folgeoption angegeben ist."}
::option[`less application.log`]{#less-log explanation="`less` ermöglicht interaktives Blättern; diese Form bleibt aber nicht in einem Folgemodus wie `tail`."}
:::

## Ein rotiertes Protokoll nach Namen verfolgen

Bei einer Protokollrotation kann eine alte Datei umbenannt und unter dem ursprünglichen Pfad eine neue angelegt werden. GNU `tail -F` folgt nach Namen und wiederholt Öffnungsversuche. Dadurch kann der Befehl eine ersetzte oder zeitweise fehlende Datei erneut öffnen:

```bash
$ tail -F application.log
```

Verwende `-f`, wenn du der aktuell geöffneten Datei folgen möchtest, und `-F`, wenn ein benanntes Protokoll voraussichtlich rotiert wird. Diese Beschreibung gilt für GNU; andere Implementierungen können abweichen.

:::single-choice{#tail-follow-rotated-name} Welche Option eignet sich unter GNU/Linux besser, um `application.log` über eine übliche Umbenennen-und-neu-erstellen-Protokollrotation hinweg zu verfolgen?

::option[`-n`]{#tail-rotation-lines explanation="Die Option `-n` verändert die Anzahl der angezeigten Zeilen. Einen ersetzten Pfad öffnet sie nicht erneut."}
::option[`-c`]{#tail-rotation-bytes explanation="Die Option `-c` ändert die Auswahleinheit in Bytes. Ein rotationsbewusstes Verfolgen bietet sie nicht."}
::option[`-F`]{#tail-follow-name .correct explanation="GNU `-F` folgt nach Namen und versucht erneut zu öffnen, sodass `tail` ein ersetztes oder zeitweise fehlendes Protokoll wieder aufnehmen kann."}
:::

Ohne benannte Datei liest `tail` von stdin und kann so das Ende einer Befehlsausgabe auswählen. Mehrere benannte Dateien erhalten wie bei `head` standardmäßig identifizierende Kopfzeilen.

Mit diesen Übungen kannst du Dateiende und Folgefunktionen praktisch trainieren:

1. **[Linux tail Befehl: Dateiende anzeigen](https://labex.io/de/labs/linux-linux-tail-command-file-end-display-214303)** – Zeige mit `tail` das Ende von Textdateien an und verfolge Aktualisierungen mit der Option `-f` in Echtzeit.
2. **[Protokoll- und Konfigurationsdateien in Linux anzeigen](https://labex.io/de/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** – Nutze `tail` zusammen mit `cat` und `more`, um Protokoll- und Konfigurationsdateien effizient zu lesen.
3. **[Schnelle Bedrohungserkennung](https://labex.io/de/labs/linux-rapid-threat-detection-387930)** – Extrahiere und analysiere mit `tail` aktuelle Protokolleinträge für eine schnelle Bedrohungserkennung.

## Zusammenfassung

Du kannst nun Dateiende untersuchen und neu angehängte Inhalte mit `tail` beobachten.

1. Zeige standardmäßig die letzten zehn Zeilen an.
2. Wähle ausdrücklich eine Zeilen- oder Byteanzahl.
3. Beginne mit `-n +N` bei einer nummerierten Zeile.
4. Verfolge angehängte Inhalte mit `-f` und stoppe mit `Ctrl+C`.
5. Verwende GNU `-F`, wenn ein benanntes Protokoll rotiert werden kann.
