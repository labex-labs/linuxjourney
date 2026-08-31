---
lesson_id: "disk-usage"
course_id: "filesystem"
lang: "de"
order_index: 9
title: "Speicherbelegung"
description: "Lerne, wie `df` und `du` unterschiedliche Ansichten des Block- und Inode-Verbrauchs eines Dateisystems messen."
meta_title: "Speicherbelegung – Das Dateisystem"
meta_description: "Lerne, mit df Dateisystemkapazität und Inodes sowie mit du die erreichbare Pfadbelegung unter Linux zu untersuchen und Abweichungen sicher zu erklären."
meta_keywords: "df Befehl, du Befehl, Linux Speicherbelegung, freien Speicher prüfen, df -i, Inodes, Dateisystemnutzung"
---

Die Kapazität eines Dateisystems besitzt mindestens zwei Grenzen: Datenblöcke und Metadatenobjekte wie Inodes. `df` meldet die Zuweisung aus Sicht des Dateisystems, während `du` erreichbare Pfadnamen durchläuft und die ihnen zugeordnete Belegung summiert. Die Werte beantworten verschiedene Fragen und müssen nicht übereinstimmen.

## Dateisystemkapazität mit `df`

Zeige den Typ eingehängter Dateisysteme und menschenlesbare Blockwerte an:

```bash
$ df -hT
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/sda1      ext4  6.2G  2.3G  3.6G  40% /
```

`Size`, `Used` und `Avail` stammen aus der Dateisystembuchhaltung. Der verfügbare Platz kann wegen reservierter Blöcke, Metadaten, Zuweisungsrichtlinien, Quoten oder Rundung kleiner als Gesamtgröße minus Belegung sein. Führe `df` mit einem Pfad aus, um das Dateisystem zu melden, das diesen Pfad enthält:

```bash
$ df -hT /var/log
```

:::single-choice{#disk-usage-df-scope}
Was meldet `df` in erster Linie?

::option[Den Byteinhalt jeder Datei in einem Verzeichnis.]{#disk-usage-df-file-content explanation="Die Buchhaltung eines Verzeichnisbaums ist Aufgabe von Werkzeugen wie `du`."}
::option[Kapazität, Belegung und verfügbaren Platz auf Dateisystemebene.]{#disk-usage-df-filesystem .correct explanation="Df fragt Zuweisungsstatistiken eingehängter Dateisysteme ab, statt jeden Pfadnamen zu durchlaufen."}
::option[Nur die auf einem Datenträgeretikett aufgedruckte physische Größe.]{#disk-usage-df-physical-label explanation="Die Werte beschreiben die Dateisystembuchhaltung und nicht bloß die beworbene Hardwarekapazität."}
:::

## Inode-Kapazität

Dateisysteme, die Inode-ähnliche Objekte zuweisen, können diese erschöpfen, obwohl noch Blöcke frei sind:

```bash
$ df -i /var
```

Eine große Anzahl kleiner Dateien kann die verfügbaren Inodes verbrauchen. Das Löschen einer großen Datei gibt viele Blöcke, aber im Allgemeinen nur einen Inode frei; das Löschen vieler unnötiger kleiner Dateien kann Inode-Druck verringern. Manche Dateisysteme weisen Metadaten dynamisch zu und melden diese Konzepte anders.

:::single-choice{#disk-usage-inode-exhaustion}
Was kann geschehen, wenn ein Dateisystem freie Blöcke, aber keine freien Inodes besitzt?

::option[Jede vorhandene Datei verdoppelt automatisch ihre Größe.]{#disk-usage-inode-double explanation="Inode-Erschöpfung verhindert die Zuweisung neuer Metadaten und vergrößert vorhandene Inhalte nicht."}
::option[Das Erstellen einer weiteren Datei kann fehlschlagen.]{#disk-usage-inode-create-fail .correct explanation="Ein neues Dateisystemobjekt benötigt Metadaten, auch wenn noch Platz für Dateidaten vorhanden ist."}
::option[Das Dateisystem wird in Swap umgewandelt.]{#disk-usage-inode-swap explanation="Ressourcenerschöpfung ändert den Dateisystemtyp nicht."}
:::

## Pfadbelegung mit `du`

Fasse den zugewiesenen Speicher zusammen, der unterhalb eines Verzeichnisses erreichbar ist:

```bash
$ du -sh /var/log
```

Vergleiche unmittelbare Untereinträge und bleibe dabei auf einem Dateisystem:

```bash
$ sudo du -xhd1 /var | sort -h
```

Die hier gezeigten GNU-Optionen stehen für menschenlesbare Ausgabe, maximale Tiefe eins und ein einziges Dateisystem. Berechtigungen können Unterbäume verbergen und eine unvollständige Summe erzeugen. `du` kann außerdem standardmäßig hart verlinkte Dateien nur einmal zählen, scheinbare Größe von zugewiesenen Blöcken unterscheiden und Sparse-Dateien abhängig von den Optionen verschieden behandeln.

:::single-choice{#disk-usage-du-purpose}
Welcher Befehl fasst die zugewiesene Belegung unter `/var/log` zusammen?

::option[`df -i /var/log`]{#disk-usage-df-inodes explanation="Dieser Befehl meldet Inode-Statistiken des enthaltenden Dateisystems."}
::option[`du -sh /var/log`]{#disk-usage-du-summary .correct explanation="Du durchläuft den angegebenen Baum; `-s` gibt eine einzelne Zusammenfassung in menschenlesbaren Einheiten aus."}
::option[`mount -a /var/log`]{#disk-usage-mount-a explanation="Das Einhängen steht in keinem Zusammenhang mit einer schreibgeschützten Zusammenfassung der Verzeichnisbelegung."}
:::

## Warum `df` und `du` abweichen

Häufige Ursachen sind:

- Ein Prozess hält eine gelöschte Datei geöffnet; ihre Blöcke bleiben zugewiesen, aber für `du` existiert kein Pfadname mehr.
- Dateisystemmetadaten, reservierter Speicher, Journale, Reflinks, Snapshots oder Kompression beeinflussen die Buchhaltung.
- Innerhalb des durchlaufenen Baums ist ein anderes Dateisystem eingehängt.
- Berechtigungen hindern `du` am Lesen mancher Verzeichnisse.
- Sparse-Dateien besitzen unterschiedliche scheinbare und zugewiesene Größen.

Untersuche gelöschte, aber geöffnete Dateien bei autorisierten Prozessen mit einem Werkzeug wie `lsof +L1`. Starte den verantwortlichen Dienst über sein normales Verfahren neu oder sende ihm ein passendes Signal, statt unbekannte Deskriptoren zu kürzen.

:::single-choice{#disk-usage-deleted-open-file}
Warum kann `df` belegten Platz anzeigen, den das pfadbasierte `du` nicht findet?

::option[`df` multipliziert jede Dateigröße immer mit zwei.]{#disk-usage-df-doubles explanation="Es gibt keine universelle Verdoppelungsregel."}
::option[Eine gelöschte Datei kann für einen laufenden Prozess geöffnet und zugewiesen bleiben.]{#disk-usage-open-deleted .correct explanation="Der Verzeichniseintrag ist entfernt, doch das Dateisystem behält die Blöcke bis zum Schließen der letzten offenen Referenz."}
::option[`du` löscht Dateien automatisch nach dem Zählen.]{#disk-usage-du-deletes explanation="Du ist ein Buchhaltungswerkzeug und entfernt die durchlaufenen Dateien nicht."}
:::

## Untersuchen, ohne den Vorfall zu verschlimmern

Beginne beim von `df` gemeldeten vollen Dateisystem, bestimme sein Einhängeziel mit `findmnt` und grenze `du`-Suchen anschließend auf dasselbe Dateisystem ein. Berücksichtige Snapshots, Containerschichten, Protokolle, Paket-Caches und Aufbewahrungsrichtlinien von Anwendungen. Lösche Dateien nicht allein aufgrund ihrer Größe; kläre zuerst Eigentümerschaft, Sicherung, Compliance und Dienstverhalten.

:::single-choice{#disk-usage-safe-investigation}
Was ist die sicherste Reaktion auf eine gefundene große Datei?

::option[Sie sofort löschen, während der Dienst sie beschreibt.]{#disk-usage-delete-immediately explanation="Dadurch können benötigte Daten verloren gehen; der Speicher wird möglicherweise nicht frei, solange die Datei geöffnet bleibt."}
::option[`mkfs` auf dem enthaltenden Gerät ausführen.]{#disk-usage-mkfs-device explanation="Eine Formatierung würde das Dateisystem zerstören, statt das Wachstum einer Datei zu beheben."}
::option[Vor einer Änderung ihren Eigentümer und ihre Aufbewahrungsfunktion bestimmen.]{#disk-usage-review-large-file .correct explanation="Die Größe allein beweist nicht, dass die Datei entbehrlich oder sicher zu kürzen ist."}
:::

## Zusammenfassung

Du kannst Berichte über Dateisystem- und pfadbasierte Speicherbelegung nun miteinander in Einklang bringen.

1. Verwende `df` für die Blockkapazität eingehängter Dateisysteme.
2. Verwende `df -i` für Inode-Druck, soweit unterstützt.
3. Verwende begrenzte `du`-Durchläufe, um die Belegung erreichbarer Pfade zuzuordnen.
4. Untersuche gelöschte offene Dateien und dateisystemspezifische Buchhaltungsunterschiede.
5. Wende Eigentums- und Aufbewahrungsrichtlinien an, bevor du Daten löschst.
