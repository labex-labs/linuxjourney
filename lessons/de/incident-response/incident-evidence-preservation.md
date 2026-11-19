---
lesson_id: "incident-evidence-preservation"
course_id: "incident-response"
lang: "de"
order_index: 2
title: "Beweissicherung"
description: "Lerne, eine Übungsaufzeichnung, ihre Kopie und die Prüfsumme für eine spätere Prüfung aufzubewahren."
meta_title: "Beweissicherung - Reaktion auf Sicherheitsvorfälle"
meta_description: "Lerne, eine Übungsaufzeichnung, ihre Kopie und die Prüfsumme für eine spätere Prüfung aufzubewahren."
meta_keywords: "Beweissicherung, Prüfsummen, Vorfallreaktion, Cybersicherheit, Linux Journey"
---

Bei der Reaktion auf einen Vorfall kann ein Protokollauszug helfen, das Geschehen zu erklären. Sichere die Originalquelle oder den genehmigten Export zusammen mit den Angaben, die eine andere Person für die Auswertung braucht.

## Den Kontext festhalten

Notiere Host, Quelle, Zeitzone und Zeitfenster. Halte fest, wer die Aufzeichnungen gesammelt und welchen Filter die Person verwendet hat. Ohne diese Angaben lässt sich eine kopierte Zeile möglicherweise nicht von einer gleichlautenden Zeile eines anderen Rechners unterscheiden.

:::single-choice{#incident-evidence-preservation-context-fields} Ein Teammitglied erhält eine Zeile mit der Uhrzeit 09:22 Uhr und ohne weitere Angaben. Was solltest du ergänzen?

::option[Den Pfad, unter dem die Kopie lokal gespeichert wurde.]{#incident-evidence-preservation-context-fields-b explanation="Damit lässt sich die Kopie finden. Ihre ursprüngliche Quelle und Zeit bleiben unbekannt."}
::option[Eine Vermutung zur Ursache.]{#incident-evidence-preservation-context-fields-c explanation="Halte Angaben zur Erfassung getrennt von der Auswertung fest."}
::option[Den Quellhost, die Zeitzone und den Erfassungszeitraum.]{#incident-evidence-preservation-context-fields-a .correct explanation="Damit lässt sich die Zeile auf der richtigen Zeitleiste einordnen."}
:::

## Eine Kopie vergleichen

Speichere in einem neuen Übungsverzeichnis eine harmlose Beispielzeile, kopiere die Datei und berechne für beide Dateien den SHA-256-Wert. Verwende ausschließlich die Beispieldatei. Die Schreibvorgänge überschreiben gleichnamige Dateien in diesem Verzeichnis.

```bash
$ printf '%s\n' '09:22 UTC public homepage returned 503' > sample.log
$ cp sample.log review-copy.log
$ sha256sum sample.log review-copy.log
```

In der ersten Spalte steht der Hashwert des Inhalts. Die beiden Werte sollten übereinstimmen. Damit prüfst du zum Zeitpunkt der Messung, ob die Bytes der Kopie mit denen des Originals übereinstimmen. Ob das ursprüngliche Ereignis korrekt protokolliert wurde, lässt sich so nicht feststellen.

:::single-choice{#incident-evidence-preservation-copy-meaning} Welche Aussage stützen die übereinstimmenden Hashwerte?

::option[Der Zeitstempel der Quelle muss stimmen.]{#incident-evidence-preservation-copy-meaning-a explanation="Ein Hashwert beschreibt den Dateiinhalt und kann die Uhr nicht überprüfen."}
::option[Die geprüften Bytes der Prüfungskopie stimmen mit denen der Beispieldatei überein.]{#incident-evidence-preservation-copy-meaning-b .correct explanation="Beide Hashwerte wurden mit demselben Verfahren berechnet."}
::option[Die Kopie ist zur Veröffentlichung freigegeben.]{#incident-evidence-preservation-copy-meaning-c explanation="Die Freigabe regelt, wer die Datei sehen darf. Der Hashwert sagt darüber nichts aus."}
:::

![Aufgezeichnete LabEx-Ausgabe mit übereinstimmenden Hashwerten für eine Übungsdatei und ihre Prüfungskopie](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-evidence-preservation/matching-copy-hashes.png)

## Einen sicheren Auszug vorbereiten

Bewahre die Originalaufzeichnung unverändert auf und beschränke den Zugriff. Wenn ein anderes Team nur wenige Felder braucht, erstelle einen eigenen Auszug und entferne daraus sensible Angaben. Vermerke die Kürzung und bewahre den Verweis auf die geschützte Quelle auf.

:::single-choice{#incident-evidence-preservation-redact-copy} Aus welcher Datei solltest du vor der Weitergabe sensible Angaben entfernen?

::option[Aus einem separaten Auszug für die Prüfung.]{#incident-evidence-preservation-redact-copy-c .correct explanation="So bleibt die Quelle erhalten und du gibst nur die benötigten Angaben weiter."}
::option[Aus dem geschützten Original, damit sich alle Kopien ändern.]{#incident-evidence-preservation-redact-copy-a explanation="Dadurch würdest du den Beleg verändern, den du sichern willst."}
::option[Aus dem Text mit der Prüfsumme, damit eine geänderte Datei gleich aussieht.]{#incident-evidence-preservation-redact-copy-b explanation="Bewahre die gemessenen Werte und die dazugehörigen Dateien auf."}
:::

## Zusammenfassung

Du kannst jetzt Belege so vorbereiten, dass eine andere Person sie auswerten kann.

1. Halte fest, wo und wann das Material erhoben wurde.
2. Prüfe, ob die Bytes der Kopie mit der Quelle übereinstimmen.
3. Entferne sensible Angaben in einem separaten Auszug für die Weitergabe.
