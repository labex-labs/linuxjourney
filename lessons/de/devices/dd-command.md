---
lesson_id: "dd-command"
course_id: "devices"
lang: "de"
order_index: 7
title: "dd"
description: "Lerne, wie `dd` Blockdatenströme kopiert und wie du zerstörerische Fehler bei Eingabe, Ausgabe und Größe vermeidest."
meta_title: "dd – Geräte"
meta_description: "Lerne den Linux-Befehl dd zum Kopieren von Datenströmen und Datenträgerabbildern kennen. Verstehe if, of, bs und count sowie wichtige Sicherheitsmaßnahmen."
meta_keywords: "dd Befehl, dd Linux, dd Werkzeug, Daten kopieren, Datenträgerabbild, Linux Tutorial, Datensicherung, Blockgerät"
---

`dd` kopiert Daten von einem Eingabe- in einen Ausgabestrom und wendet dabei die angeforderten Blockgrößen und Umwandlungen an. Das Werkzeug versteht weder Dateisysteme und Partitionsgrenzen noch, ob ein Ausgabeziel wertvolle Daten enthält. Dadurch eignet es sich für Abbilder und rohe Geräte – und wirkt bei einem falschen Ziel sofort zerstörerisch.

## Eingabe, Ausgabe und Blockgröße

Ein Befehl besitzt diese allgemeine Form:

```bash
$ dd if=input.img of=output.img bs=4M status=progress
```

- `if=` wählt die Eingabe; ohne diese Angabe liest `dd` von der Standardeingabe.
- `of=` wählt die Ausgabe; ohne diese Angabe schreibt `dd` auf die Standardausgabe.
- `bs=` legt beim gewöhnlichen Kopieren die Blockgröße für Ein- und Ausgabe fest.
- `status=progress` fordert GNU `dd` auf, regelmäßig den Übertragungsfortschritt zu melden.

`dd` kopiert Blöcke und nicht grundsätzlich einzelne Bytes. Ein größeres `bs` kann den Aufwand für Systemaufrufe verringern, doch der optimale Wert hängt von Geräten, Ausrichtung, Caches und Arbeitslast ab. Die logisch kopierten Daten verändern sich dadurch nicht.

:::single-choice{#dd-command-output-operand} Welcher Operand wählt das von `dd` beschriebene Ziel aus?

::option[`if=`]{#dd-command-input-file explanation="`if` bezeichnet die Eingabequelle."}
::option[`of=`]{#dd-command-output-file .correct explanation="`of` benennt den Ausgabestrom oder die Datei, die die kopierten Daten empfängt."}
::option[`bs=`]{#dd-command-block-size explanation="`bs` wählt eine Übertragungsblockgröße und keinen Pfad."}
:::

## Die Kopie begrenzen

`count=` begrenzt die Anzahl der verarbeiteten Eingabeblöcke. Für eine gewöhnliche Eingabedatei:

```bash
$ dd if=source.img of=prefix.img bs=1M count=2 status=progress
```

Damit werden zwei Eingabeblöcke mit jeweils bis zu 1 MiB angefordert, also höchstens 2 MiB kopiert. Bei Datenströmen wie Pipes können kurze Lesevorgänge diese einfache Multiplikation erschweren; GNU `dd` bietet `iflag=fullblock`, wenn vollständige Eingabeblöcke erforderlich sind. Beachte Binäreinheiten und Suffixsyntax der lokal installierten Implementierung.

:::single-choice{#dd-command-count-result} Welche maximale Datenmenge fordert `bs=1M count=2` bei einer gewöhnlichen Datei an?

::option[1 MiB.]{#dd-command-one-mib explanation="Das wäre ein Block der ausgewählten Größe."}
::option[2 MiB.]{#dd-command-two-mib .correct explanation="Zwei Eingabeblöcke multipliziert mit 1 MiB pro Block ergeben höchstens 2 MiB."}
::option[2 GiB.]{#dd-command-two-gib explanation="Das Suffix `M` bezeichnet bei GNU `dd` Blöcke in Mebibyte-Größe und keine Gibibytes."}
:::

## Ein Abbild auf ein Blockgerät schreiben

Eine rohe Wiederherstellung kann so aussehen:

```bash
$ sudo dd if=backup.img of=/dev/sdX bs=4M status=progress conv=fsync
```

`/dev/sdX` ist absichtlich ein Platzhalter und kein direkt zu kopierender Befehl. Bevor du ihn ersetzt:

1. Halte eine geprüfte Sicherung aller wertvollen Daten vor.
2. Bestimme das Ziel mit `lsblk`, `udevadm` oder gleichwertigen Werkzeugen anhand von Modell, Seriennummer, Größe, Transport und dauerhaftem Link.
3. Bestätige, dass keine Zielpartition eingehängt, als Swap verwendet, Teil von RAID oder LVM oder von einem anderen Dienst geöffnet ist.
4. Prüfe das Gerät nach jedem Trennen, Neustart oder jeder Änderung der Topologie erneut.
5. Vergewissere dich, dass das Abbild passt und wirklich das vollständige Gerät beschrieben werden soll.

Das Ausgabegerät wird von seinem Anfang an überschrieben. Das Vertauschen von `if` und `of`, die Auswahl des Systemdatenträgers oder die Verwendung eines ganzen Datenträgers anstelle einer beabsichtigten Partition kann Daten ohne Bestätigungsfrage zerstören.

:::single-choice{#dd-command-target-verification} Was ist der wichtigste Grund, Modell, Seriennummer, Größe und aktive Nutzung vor dem Schreiben auf ein rohes Gerät zu prüfen?

::option[Gerätebuchstaben können sich ändern, und `dd` überschreibt das ausgewählte Ziel, ohne dessen Inhalt zu verstehen.]{#dd-command-target-can-change .correct explanation="Identitäts- und Nutzungsprüfungen verringern das Risiko, einen anderen Datenträger oder einen aktiven Speicherstapel zu zerstören."}
::option[`dd` verweigert das Schreiben, wenn die Dateisystembezeichnung nicht zum Abbild passt.]{#dd-command-label-check explanation="Das Werkzeug führt keine solche dateisystembezogene Sicherheitsprüfung aus."}
::option[Blockgeräte lassen sich nicht öffnen, solange irgendeine Sicherung existiert.]{#dd-command-backup-prevents-open explanation="Eine Sicherung verhindert Schreibvorgänge technisch nicht; eine gepflegte und geprüfte Sicherung ermöglicht die Wiederherstellung."}
:::

## Ein konsistentes Abbild erstellen

Das Lesen eines aktiven Blockgeräts, während sich sein Dateisystem verändert, kann ein intern inkonsistentes Abbild erzeugen. Bevorzuge ein nicht eingehängtes Dateisystem, einen anwendungskonsistenten Snapshot oder einen dokumentierten Freeze-/Snapshot-Ablauf. Datenbanken und virtuelle Maschinen können eigene Verfahren zum Ruhigstellen erfordern.

Ein rohes Geräteabbild kopiert Blöcke einschließlich Dateisystemmetadaten und unbenutzter Bereiche. Es kann daher wesentlich größer als eine dateibasierte Sicherung sein und Kennungen duplizieren, die geändert werden müssen, bevor ein Klon neben dem Original eingehängt wird.

:::single-choice{#dd-command-live-filesystem-image} Warum kann das Abbild eines eingehängten, sich verändernden Dateisystems unzuverlässig sein?

::option[Eingehängte Dateisysteme erlauben niemals das Lesen des Blockgeräts.]{#dd-command-mounted-no-read explanation="Rohe Lesevorgänge können möglich sein; gerade deshalb muss die Konsistenz geplant und darf nicht vorausgesetzt werden."}
::option[Unterschiedliche Blöcke können aus verschiedenen Zeitpunkten des Dateisystemzustands gelesen werden.]{#dd-command-inconsistent-moments .correct explanation="Gleichzeitige Änderungen können verhindern, dass das gesammelte Blockabbild einen einzigen konsistenten Zeitpunkt darstellt."}
::option[`dd` wandelt das Dateisystem automatisch in ein tar-Archiv um.]{#dd-command-converts-tar explanation="Das Werkzeug kopiert Rohdaten und erstellt kein dateisystembezogenes Archiv."}
:::

## Abschluss und Überprüfung

Ein Befehlsabschluss ohne Ein-/Ausgabefehler beweist weder die Auswahl der beabsichtigten Quelle und des richtigen Ziels noch die Verwendbarkeit des Abbilds. Notiere die genauen Identitäten und Größen, stelle sicher, dass gepufferte Ausgabe den Speicher erreicht hat, vergleiche einen angemessen begrenzten Rücklesevorgang oder kryptografische Hashes und teste die Wiederherstellung gemäß dem Sicherungsplan.

Bewirb Überschreibdurchläufe mit `dd` nicht als garantiert sichere Löschung für SSDs, Flash-Übersetzungsschichten, Thin-Provisioning-Speicher, Snapshots oder umgeleitete Sektoren. Verwende vom Gerät und der Plattform unterstützte Bereinigungsverfahren zusammen mit einer ausdrücklichen Richtlinie zur Datenvernichtung.

:::single-choice{#dd-command-success-meaning} Was beweist ein Exit-Status null von `dd` für sich allein nicht?

::option[Dass der Befehl alle angegebenen Operanden ausgewertet hat.]{#dd-command-parsed-operands explanation="Ungültige Operanden führen normalerweise zu einem Fehler statt zu einem erfolgreichen Abschluss."}
::option[Dass der Bediener die beabsichtigte Quelle und das beabsichtigte Ziel ausgewählt hat.]{#dd-command-does-not-prove-intent .correct explanation="Das Werkzeug kann erfolgreich auf das falsche Ziel kopieren, weil es die Absicht des Bedieners nicht erkennen kann."}
::option[Dass der Prozess seinen normalen Beendigungspfad erreicht hat.]{#dd-command-normal-exit explanation="Ein Status null zeigt einen normalen Erfolg auf Befehlsebene an, nicht jedoch die semantische Richtigkeit der ausgewählten Ziele."}
:::

Übe ausschließlich mit gewöhnlichen Dateien oder entbehrlichen virtuellen Datenträgern, bevor du rohe Hardware berührst. Die Partitions- und Dateisystemkonzepte im Lab [Linux-Partitionen und Dateisysteme verwalten](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) liefern wichtigen Kontext.

## Zusammenfassung

Du kannst `dd` nun als rohes Blockkopierwerkzeug ohne Verständnis deiner Absicht einordnen.

1. Unterscheide `if`, `of`, `bs` und `count`.
2. Prüfe die dauerhafte Zielidentität und jeden aktiven Verbraucher.
3. Erstelle Abbilder aus einem konsistenten Speicherzustand.
4. Leere Puffer, prüfe das Ergebnis und teste nach dem Kopieren die Wiederherstellung.
5. Behandle jede Ausgabe auf ein rohes Gerät als potenziell zerstörerisch.
